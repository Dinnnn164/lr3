import os
import sys
from sqlalchemy import create_engine, text

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from config import settings
    print(" Підключення до бази даних...")
    
    engine = create_engine(settings.postgres_sync)
    
    with engine.connect() as conn:
        print(" Підключення успішне")
        
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS lr3_schema"))
        print(" Схема lr3_schema створена/перевірена")
        
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS lr3_schema.alembic_version (
                version_num VARCHAR(32) NOT NULL,
                CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
            )
        """))
        conn.commit()
        print(" Таблиця alembic_version створена в схемі lr3_schema")
        
        result = conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'lr3_schema' AND table_name = 'alembic_version'
        """))
        
        if result.fetchone():
            print(" Перевірка: таблиця alembic_version успішно створена")
        else:
            print(" Помилка: таблиця не створена")
            
except ImportError as e:
    print(f"Не вдалося імпортувати налаштування: {e}")
    print(" Переконайтеся, що config.py існує в корені проекту")
except Exception as e:
    print(f" Помилка підключення до бази даних: {e}")