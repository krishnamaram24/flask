
  pipeline {
  environment {
    registry = 'krishnamaram2/myrepo1'
    registryCredential = 'dockerhub'
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git branch: 'main', url: 'https://github.com/krishnamaram24/flask.git'
      }
    }
    stage('Building image') {
      steps{
        script {
          docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('pull image and run') {
            steps {
                sh '''
                docker run -d --name flask -p 5001:5001 krishnamaram2/myrepo1:$BUILD_NUMBER
                '''
            }
        }
    
    
  }
}
