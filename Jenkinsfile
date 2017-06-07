pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo Build'
      }
    }
    stage('Test') {
      steps {
        parallel(
          "JUnit": {
            sh 'echo JUnit'
            
          },
          "DBUnit": {
            sh 'echo DBUnit'
            
          },
          "Jasmine": {
            sh 'echo Jasmine'
            
          }
        )
      }
    }
    stage('Browser Tests') {
      steps {
        parallel(
          "Firefox": {
            sh 'echo Firefox'
            
          },
          "Edge": {
            sh 'echo Edge'
            
          },
          "Safari": {
            sh 'echo Safari'
            
          },
          "Chrome": {
            sh 'echo Chrome'
            
          }
        )
      }
    }
    stage('Dev') {
      steps {
        sh 'echo Dev'
      }
    }
    stage('Staging') {
      steps {
        sh 'echo Staging'
      }
    }
    stage('Production') {
      steps {
        sh 'echo Production'
      }
    }
  }
}
