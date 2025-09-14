#!/usr/bin/env python3
"""
Скрипт для ручной загрузки на GitHub
"""

import subprocess
import sys

def main():
    print("🚀 Ручная загрузка на GitHub")
    print("=" * 50)
    
    print("📝 Инструкция:")
    print("1. Откройте https://github.com/new в браузере")
    print("2. Создайте репозиторий с названием 'flask-user-registration'")
    print("3. НЕ отмечайте 'Add a README file'")
    print("4. Нажмите 'Create repository'")
    print("5. Скопируйте URL репозитория")
    
    repo_url = input("\n🔗 Введите URL вашего репозитория (например: https://github.com/theram1ras/flask-user-registration.git): ").strip()
    
    if not repo_url:
        print("❌ URL не введен")
        return
    
    try:
        print("\n🔗 Настраиваю Git remote...")
        subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
        
        print("🌿 Переименовываю ветку в main...")
        subprocess.run(["git", "branch", "-M", "main"], check=True)
        
        print("📤 Загружаю код на GitHub...")
        print("💡 При запросе пароля используйте ваш GitHub токен")
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        
        print("\n🎉 УСПЕХ!")
        print("=" * 50)
        print(f"📋 Репозиторий: {repo_url.replace('.git', '')}")
        print("\n📝 Следующие шаги:")
        print("1. Перейдите на Railway.app")
        print("2. Подключите ваш GitHub репозиторий")
        print("3. Railway автоматически развернет приложение")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка: {e}")
        print("💡 Убедитесь, что:")
        print("   - Репозиторий создан на GitHub")
        print("   - URL правильный")
        print("   - Используете токен как пароль")

if __name__ == "__main__":
    main()
