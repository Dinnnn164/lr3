import os
import sys
from sqlalchemy import create_engine, text

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from config import settings
    print("🔗 Підключення до бази даних...")
    
    engine = create_engine(settings.postgres_sync)
    
    with engine.connect() as conn:
        conn.execute(text("DROP SCHEMA IF EXISTS lr3_schema CASCADE"))
        conn.execute(text("CREATE SCHEMA lr3_schema"))
        conn.commit()
        
        print(" Схема lr3_schema успішно скинута!")
        
        result = conn.execute(text("SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'lr3_schema'"))
        if result.fetchone():
            print(" Схема lr3_schema існує в базі даних")
        else:
            print("❌ Помилка: схема не створилася")
            
except ImportError:
    print(" Не вдалося імпортувати налаштування")
except Exception as e:
    print(f" Помилка: {e}")