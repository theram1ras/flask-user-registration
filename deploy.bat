@echo off
echo 🌟 Автоматическая загрузка проекта на GitHub
echo ================================================

echo 📦 Устанавливаю PyGithub...
pip install PyGithub

echo 🚀 Запускаю скрипт загрузки...
python deploy_to_github.py

pause
