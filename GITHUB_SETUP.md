# 🚀 Инструкция по загрузке на GitHub

## Автоматическая загрузка (Рекомендуется)

### Шаг 1: Получите GitHub Personal Access Token

1. Перейдите на [GitHub.com](https://github.com) и войдите в аккаунт
2. Нажмите на ваш аватар в правом верхнем углу
3. Выберите **Settings**
4. В левом меню выберите **Developer settings**
5. Выберите **Personal access tokens** → **Tokens (classic)**
6. Нажмите **Generate new token** → **Generate new token (classic)**
7. Заполните форму:
   - **Note**: "Flask App Deployment"
   - **Expiration**: Выберите срок действия (например, 90 days)
   - **Select scopes**: Отметьте `repo` (полный доступ к репозиториям)
8. Нажмите **Generate token**
9. **ВАЖНО**: Скопируйте токен и сохраните его! Он больше не будет показан.

### Шаг 2: Запустите автоматический скрипт

**Вариант 1: Через Python скрипт**
```bash
python deploy_to_github.py
```

**Вариант 2: Через batch файл (Windows)**
```bash
deploy.bat
```

### Шаг 3: Следуйте инструкциям скрипта

Скрипт попросит:
- Ваш GitHub Personal Access Token
- Название репозитория (по умолчанию: `flask-user-registration`)
- Описание репозитория

## Ручная загрузка

Если автоматический скрипт не работает:

### 1. Создайте репозиторий на GitHub

1. Перейдите на [GitHub.com](https://github.com)
2. Нажмите **New repository** (зеленая кнопка)
3. Заполните:
   - **Repository name**: `flask-user-registration`
   - **Description**: `Flask web app with user registration and SQLite database`
   - **Public** (отметьте)
   - **НЕ** отмеченте "Add a README file"
4. Нажмите **Create repository**

### 2. Загрузите код через командную строку

```bash
# Добавьте remote origin (замените YOUR_USERNAME на ваш GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/flask-user-registration.git

# Переименуйте ветку в main
git branch -M main

# Загрузите код
git push -u origin main
```

## 🔗 Развертывание на Railway

После загрузки на GitHub:

1. Перейдите на [Railway.app](https://railway.app)
2. Нажмите **Login** и войдите через GitHub
3. Нажмите **New Project**
4. Выберите **Deploy from GitHub repo**
5. Найдите ваш репозиторий `flask-user-registration`
6. Нажмите **Deploy Now**
7. Railway автоматически:
   - Определит Python приложение
   - Установит зависимости из `requirements.txt`
   - Запустит приложение через `Procfile`
8. Получите публичный URL вашего сайта!

## ✅ Проверка

После развертывания:
- Ваш сайт будет доступен по URL от Railway
- Можете протестировать регистрацию и вход
- База данных SQLite будет создана автоматически

## 🆘 Помощь

Если возникли проблемы:
1. Проверьте, что все файлы загружены на GitHub
2. Убедитесь, что Railway подключен к правильному репозиторию
3. Проверьте логи развертывания в Railway dashboard
