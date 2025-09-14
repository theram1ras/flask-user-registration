#!/usr/bin/env python3
"""
Проверка прав GitHub токена
"""

import sys
from github import Github

def check_token_permissions(token):
    """Проверяет права токена"""
    try:
        g = Github(token)
        user = g.get_user()
        
        print(f"✅ Подключен к GitHub как: {user.login}")
        print(f"📧 Email: {user.email}")
        print(f"🏠 URL профиля: {user.html_url}")
        
        # Проверяем права
        print("\n🔍 Проверка прав токена:")
        
        # Проверяем доступ к репозиториям
        try:
            repos = user.get_repos()
            print(f"✅ Доступ к репозиториям: {repos.totalCount} репозиториев")
        except Exception as e:
            print(f"❌ Нет доступа к репозиториям: {e}")
        
        # Проверяем возможность создания репозиториев
        try:
            # Пробуем получить список репозиториев
            user.get_repos(type='owner')
            print("✅ Права на чтение репозиториев: OK")
        except Exception as e:
            print(f"❌ Нет прав на чтение репозиториев: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("❌ Использование: python check_token.py YOUR_GITHUB_TOKEN")
        return
    
    token = sys.argv[1]
    check_token_permissions(token)

if __name__ == "__main__":
    main()
