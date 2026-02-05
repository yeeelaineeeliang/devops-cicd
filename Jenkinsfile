pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo "Building from GitHub webhook"
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Build completed'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Tests passed'
            }
        }
        
        stage('Deploy - Main Branch Only') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying to production (main branch only)'
            }
        }
        
        stage('Feature Branch') {
            when {
                not { branch 'main' }
            }
            steps {
                echo 'Feature branch - deployment skipped'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully'
        }
    }
}