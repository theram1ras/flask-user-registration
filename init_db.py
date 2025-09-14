#!/usr/bin/env python3
"""
Скрипт для инициализации базы данных
Запускать на Railway для создания таблиц
"""

from app import app, db, User

def init_database():
    """Создает все таблицы в базе данных"""
    print("🚀 Инициализация базы данных...")
    
    with app.app_context():
        try:
            # Создаем все таблицы
            db.create_all()
            print("✅ Таблицы созданы успешно!")
            
            # Проверяем, что таблица user существует
            if db.engine.dialect.has_table(db.engine, 'user'):
                print("✅ Таблица 'user' существует")
            else:
                print("❌ Таблица 'user' не найдена")
                
            # Показываем структуру таблицы
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"📋 Найденные таблицы: {tables}")
            
            if 'user' in tables:
                columns = inspector.get_columns('user')
                print("📊 Структура таблицы 'user':")
                for col in columns:
                    print(f"  - {col['name']}: {col['type']}")
            
        except Exception as e:
            print(f"❌ Ошибка при создании таблиц: {e}")
            return False
    
    print("🎉 База данных готова к использованию!")
    return True

if __name__ == '__main__':
    init_database()
