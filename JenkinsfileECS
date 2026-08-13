pipeline {
    agent { label 'majlis' }

    environment {
        AWS_REGION      = "ap-south-1"
        AWS_ACCOUNT_ID  = "405634363888"
        NAMESPACE       = "Wandarlusr-prod"

        ECR_REGISTRY    = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        ECR_REPOSITORY  = "${NAMESPACE}/${JOB_NAME}"

        ECS_CLUSTER     = "majlis-prod-api-ecs-cluster"
        ECS_SERVICE     = "${JOB_NAME}-service"
        TASK_FAMILY     = "${JOB_NAME}-task"

        IMAGE_TAG       = "${env.GIT_COMMIT.take(7)}"
    }
       parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['development', 'testing', 'production'],
            description: 'Select deployment environment'
        )
    }

    stages {
        stage('SonarQube Scan') {

    steps {

        withSonarQubeEnv('SonarQube') {

            sh '''

            sonar-scanner \
            -Dsonar.projectKey=wanderlust \
            -Dsonar.sources=. \
            -Dsonar.host.url=$SONAR_HOST_URL \
            -Dsonar.login=$SONAR_AUTH_TOKEN

            '''

        }

    }

}

stage('Quality Gate') {

    steps {

        timeout(time: 5, unit: 'MINUTES') {

            waitForQualityGate abortPipeline: true

        }

    }

}

        stage('Validate') {
            steps {
                sh '''
                aws --version
                docker --version

                aws ecr get-login-password --region $AWS_REGION \
                  | docker login \
                    --username AWS \
                    --password-stdin \
                    $ECR_REGISTRY
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                cp $ENV .env

                docker build \
                  -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .

                docker push \
                  $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
                '''
            }
        }
       
stage('Update Task Definition') {
    steps {
        sh '''
        sed -i "s|590398356271.dkr.ecr.us-east-1.amazonaws.com/wandarlustfrontpipeline:.*|590398356271.dkr.ecr.us-east-1.amazonaws.com/wandarlustfrontpipeline:${BUILD_NUMBER}|g" ecs/task.json

        sed -i "s|590398356271.dkr.ecr.us-east-1.amazonaws.com/wandarlustbackpipeline:.*|590398356271.dkr.ecr.us-east-1.amazonaws.com/wandarlustbackpipeline:${BUILD_NUMBER}|g" ecs/task.json

        cat ecs/task.json
        '''
    }
}stage('Register Task Definition') {
    steps {
        sh '''
        TASK_ARN=$(aws ecs register-task-definition \
            --cli-input-json file://ecs/task.json \
            --query "taskDefinition.taskDefinitionArn" \
            --output text)

        echo $TASK_ARN > task-arn.txt

        echo "Registered Task Definition"

        cat task-arn.txt
        '''
    }
}


stage('Deploy to ECS') {
    steps {
        sh '''
        NEW_TASK=$(cat task-arn.txt)

        aws ecs update-service \
            --cluster wanderlust-cluster \
            --service wanderlust-service \
            --task-definition $NEW_TASK \
            --force-new-deployment

        aws ecs wait services-stable \
            --cluster wanderlust-cluster \
            --services wanderlust-service

        echo "Deployment Completed"
        '''
    }
}

stage('Wait Until Stable') {
    steps {
        sh '''
        aws ecs wait services-stable \
            --cluster $ECS_CLUSTER \
            --services $ECS_SERVICE
        '''
    }
}

stage('Configure Auto Scaling') {
    steps {
        sh '''
        POLICY_EXISTS=$(aws application-autoscaling describe-scaling-policies \
            --service-namespace ecs \
            --resource-id service/$ECS_CLUSTER/$ECS_SERVICE \
            --query "ScalingPolicies[?PolicyName=='cpu-scaling'].PolicyName" \
            --output text)

        if [ -z "$POLICY_EXISTS" ]; then

            aws application-autoscaling register-scalable-target \
                --service-namespace ecs \
                --resource-id service/$ECS_CLUSTER/$ECS_SERVICE \
                --scalable-dimension ecs:service:DesiredCount \
                --min-capacity 1 \
                --max-capacity 10

            aws application-autoscaling put-scaling-policy \
                --service-namespace ecs \
                --resource-id service/$ECS_CLUSTER/$ECS_SERVICE \
                --scalable-dimension ecs:service:DesiredCount \
                --policy-name cpu-scaling \
                --policy-type TargetTrackingScaling \
                --target-tracking-scaling-policy-configuration '{
                    "TargetValue":70,
                    "PredefinedMetricSpecification":{
                        "PredefinedMetricType":"ECSServiceAverageCPUUtilization"
                    },
                    "ScaleOutCooldown":60,
                    "ScaleInCooldown":300
                }'

        else
            echo "Auto Scaling already configured."
        fi
        '''
    }
}


stage('OWASP ZAP') {

    when {
        expression {
            params.ENVIRONMENT == 'testing'
        }
    }

    steps {
        sh '''
        docker run --rm \
          -v $(pwd):/zap/wrk/:rw \
          ghcr.io/zaproxy/zaproxy:stable \
          zap-baseline.py \
          -t https://wandarlust.com \
          -r zap-report.html
        '''
    }

    post {
        always {
            archiveArtifacts 'zap-report.html'
        }
    }
}
        stage('Cleanup') {
            steps {
                sh 'docker system prune -af --filter "until=72h"'
            }
        }
    }

 post {

    always {

        archiveArtifacts 'report.html'

    }

}
}