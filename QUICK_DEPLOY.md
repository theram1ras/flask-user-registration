# 🚀 Быстрое развертывание на GitHub и Railway

## Вариант 1: Автоматический скрипт (Рекомендуется)

### 1. Получите GitHub токен:
1. Идите на [github.com/settings/tokens](https://github.com/settings/tokens)
2. Нажмите **Generate new token (classic)**
3. Отметьте **repo** (полный доступ к репозиториям)
4. Скопируйте токен

### 2. Запустите скрипт:
```bash
python deploy_to_github.py
```

## Вариант 2: Ручная загрузка (Проще)

### 1. Создайте репозиторий на GitHub:
1. Идите на [github.com/new](https://github.com/new)
2. Название: `flask-user-registration`
3. Описание: `Flask web app with user registration`
4. **Public** ✅
5. **НЕ** отмечайте "Add README"
6. Нажмите **Create repository**

### 2. Загрузите код:
```bash
# Замените YOUR_USERNAME на ваш GitHub username
git remote add origin https://github.com/YOUR_USERNAME/flask-user-registration.git
git branch -M main
git push -u origin main
```

## 🚂 Развертывание на Railway

### 1. Подключите GitHub:
1. Идите на [railway.app](https://railway.app)
2. **Login with GitHub**
3. **New Project** → **Deploy from GitHub repo**
4. Найдите `flask-user-registration`
5. **Deploy Now**

### 2. Готово! 🎉
- Railway автоматически установит зависимости
- Создаст SQLite базу данных
- Запустит приложение
- Даст публичный URL

## 📋 Что получится:

✅ **Веб-сайт с регистрацией**  
✅ **SQLite база данных**  
✅ **Красивый дизайн**  
✅ **Безопасные пароли**  
✅ **Публичный URL**  

## 🔗 Полезные ссылки:

- [GitHub токены](https://github.com/settings/tokens)
- [Railway.app](https://railway.app)
- [Создать репозиторий](https://github.com/new)

## ⚡ Быстрый старт:

1. `python deploy_to_github.py` (с токеном)
2. Или создайте репозиторий вручную
3. `git push -u origin main`
4. Подключите к Railway
5. Готово! 🚀
