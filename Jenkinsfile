pipeline {
    agent { label 'slave' }
    stages {
        stage('Checkout git') {
            steps {
                git branch: 'master',
                    credentialsId: 'lehastro',
                    url: 'git@github.com:lehastro/currencies.git'
                    sh "ls -lat"
            }
        }
        stage('Testing code by Sonarqube'){
            steps{
              dir('backend') {
              sh "/opt/sonar-scanner/bin/sonar-scanner -X"
          }
        }
      }
        stage('Build docker image'){
            steps {
                dir('backend') {
                sh "sudo docker build -t lehastro/currencies-app-backend -f Dockerfile_back ."
               
              
            }
         }
        }
        stage('Push docker image to dockerhub'){
            steps {
              sh "sudo docker push lehastro/currencies-app-backend:latest"
          
          }
        }
        
      
      
       stage('Deploy to Kubernetes'){
          steps {
              sh "kubectl delete deployments.apps --all"
              sh "kubectl delete pods --all"
              
              dir('kubernetes') {
              sh "kubectl apply -f ."
              }
              
          }
      }
   } 
}
