#!/usr/bin/env python3
"""
Скрипт для автоматической загрузки проекта на GitHub с токеном
Использование: python deploy_with_token.py YOUR_TOKEN
"""

import os
import subprocess
import sys
from github import Github

def create_github_repo(token, repo_name="flask-user-registration", description="Flask web app with user registration and SQLite database"):
    """Создает репозиторий на GitHub и загружает код"""
    
    print("\n🚀 Создание репозитория на GitHub")
    print("=" * 50)
    
    try:
        # Подключаемся к GitHub
        g = Github(token)
        user = g.get_user()
        print(f"✅ Подключен к GitHub как: {user.login}")
        
        # Создаем репозиторий
        print(f"📝 Создаю репозиторий '{repo_name}'...")
        repo = user.create_repo(
            repo_name,
            description=description,
            private=False,
            auto_init=False
        )
        print(f"✅ Репозиторий создан: {repo.html_url}")
        
        # Добавляем remote origin
        print("🔗 Настраиваю Git remote...")
        subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
        subprocess.run(["git", "remote", "add", "origin", repo.clone_url], check=True)
        
        # Переименовываем ветку в main
        print("🌿 Переименовываю ветку в main...")
        subprocess.run(["git", "branch", "-M", "main"], check=True)
        
        # Загружаем код
        print("📤 Загружаю код на GitHub...")
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        
        print("\n🎉 УСПЕХ!")
        print("=" * 50)
        print(f"📋 Репозиторий: {repo.html_url}")
        print(f"🔗 Клонирование: {repo.clone_url}")
        print("\n📝 Следующие шаги:")
        print("1. Перейдите на Railway.app")
        print("2. Подключите ваш GitHub репозиторий")
        print("3. Railway автоматически развернет приложение")
        print(f"4. Ваш сайт будет доступен по публичному URL")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def main():
    """Основная функция"""
    print("🌟 Автоматическая загрузка на GitHub")
    print("=" * 50)
    
    # Проверяем аргументы командной строки
    if len(sys.argv) < 2:
        print("❌ Использование: python deploy_with_token.py YOUR_GITHUB_TOKEN")
        print("💡 Пример: python deploy_with_token.py ghp_xxxxxxxxxxxx")
        return
    
    token = sys.argv[1]
    
    # Проверяем, что мы в Git репозитории
    if not os.path.exists(".git"):
        print("❌ Это не Git репозиторий. Сначала выполните: git init")
        return
    
    # Проверяем наличие коммитов
    try:
        result = subprocess.run(["git", "log", "--oneline", "-1"], 
                              capture_output=True, text=True)
        if not result.stdout.strip():
            print("❌ Нет коммитов. Сначала выполните: git add . && git commit -m 'Initial commit'")
            return
    except subprocess.CalledProcessError:
        print("❌ Ошибка при проверке Git")
        return
    
    # Создаем репозиторий
    if create_github_repo(token):
        print("\n✨ Готово! Ваш проект загружен на GitHub.")
    else:
        print("\n❌ Не удалось загрузить проект на GitHub.")

if __name__ == "__main__":
    main()
