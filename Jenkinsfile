pipeline {
    agent any
    
    environment {
        VERSION = "${BUILD_NUMBER}"
        ARTIFACT_NAME = "library-app-${VERSION}.tar.gz"
        SONAR_PROJECT_KEY = "YOUR_PROJECT_KEY"
        SONAR_ORG = "YOUR_ORG_KEY"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code"
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo "Building application version ${VERSION}"
                sh '''
                    mkdir -p build
                    cp *.py build/ 2>/dev/null || true
                    cp *.sql build/ 2>/dev/null || true
                    echo "Build ${VERSION}" > build/version.txt
                '''
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarCloud') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                            -Dsonar.organization=${SONAR_ORG}
                        """
                    }
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
        
        stage('Create Artifacts') {
            steps {
                echo "Creating build artifacts"
                sh '''
                    tar -czf ${ARTIFACT_NAME} build/
                '''
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '*.tar.gz', fingerprint: true
            }
        }
        
        stage('Deploy - Main Only') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying version ${VERSION}"
            }
        }
    }
    
    post {
        success {
            echo "Build ${VERSION} passed quality gate"
        }
        failure {
            echo "Build ${VERSION} failed quality gate"
        }
    }
}