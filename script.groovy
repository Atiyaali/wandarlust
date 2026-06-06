def deploying(){   
                echo 'Deploying application...'
                echo "this is my params for choices ${params.VERSIONCHOICE}"     
}
def testing() {
      echo 'Running tests...'
}
def building() {
     echo 'buildind docker from jenkins branch'
}
return this