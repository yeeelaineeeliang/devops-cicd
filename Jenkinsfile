pipeline {
    agent none
    
    stages {
        stage('Checkout') {
            agent any
            steps {
                echo "Building branch: ${env.BRANCH_NAME}"
                checkout scm
            }
        }
        
        stage('Build') {
            agent any
            steps {
                echo 'Installing dependencies...'
                sh '''
                    pip install flask flask-sqlalchemy pytest
                '''
            }
        }
        
        stage('Test') {
            agent { label 'testing' }
            steps {
                echo 'Running tests...'
                sh '''
                    pytest test_api.py -v
                '''
            }
        }
        
        stage('Code Quality - Main Branch Only') {
            when {
                branch 'main'
            }
            agent { label 'testing' }
            steps {
                echo 'Running SonarQube on main branch...'
                sh '''
                    echo "SonarQube analysis would run here"
                '''
            }
        }
        
        stage('Deploy to Staging - Main Branch') {
            when {
                branch 'main'
            }
            agent { label 'deployment' }
            steps {
                echo 'Deploying to staging...'
                sh '''
                    echo "Deploying to staging environment"
                '''
            }
        }
        
        stage('Deploy to Production - Main Branch Only') {
            when {
                branch 'main'
            }
            agent { label 'deployment' }
            steps {
                input message: 'Deploy to production?', ok: 'Deploy'
                echo 'Deploying to production...'
                sh '''
                    echo "Deploying to production environment"
                '''
            }
        }
        
        stage('Feature Branch Notification') {
            when {
                not {
                    branch 'main'
                }
            }
            agent any
            steps {
                echo "Feature branch ${env.BRANCH_NAME} tested successfully!"
                echo "No deployment for feature branches"
            }
        }
    }
    
    post {
        success {
            echo "Pipeline completed successfully for branch ${env.BRANCH_NAME}"
        }
        failure {
            echo "Pipeline failed for branch ${env.BRANCH_NAME}"
        }
    }
}