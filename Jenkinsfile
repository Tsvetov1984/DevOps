pipeline {
    agent any
    stages {
        stage('Подготовка окружения') {
            steps {
                echo 'Выполнение 1 этапа: Установка зависимостей и клонирование'
                ansiblePlaybook(
                    playbook: 'ansible/firstPlaybook.yml',
                    inventory: 'ansible/inventory/stend1/hosts',
                    tags: 'install,deploy',
                    colorized: true
                )
            }
        }
        stage('Запуск приложений') {
            steps {
                echo 'Выполнение 2 этапа: Запуск Docker-контейнеров'
                ansiblePlaybook(
                    playbook: 'ansible/firstPlaybook.yml',
                    inventory: 'ansible/inventory/stend1/hosts',
                    tags: 'start',
                    colorized: true
                )
            }
        }
    }
}