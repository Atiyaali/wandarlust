def deploying(variable){   
                echo 'Deploying application...'
                echo "this is my params for choices ${params.VERSIONCHOICE}" 
                echo "deploying with ${variable}"    
}
def testing() {
      echo "Running tests on branch ${BRANCH_name}.."
}
def building() {
     echo "buildind docker from ${BRANCH_NAME}"
}
return this