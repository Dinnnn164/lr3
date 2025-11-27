import os
import sys
from sqlalchemy import create_engine, text, inspect

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from config import settings
    
    engine = create_engine(settings.postgres_sync)
    
    print(" ДЕБАГ АЛЕМБІК:")
    
    print("\n1. Таблиця alembic_version:")
    with engine.connect() as conn:
        try:
            result = conn.execute(text("SELECT * FROM lr3_schema.alembic_version"))
            versions = [row[0] for row in result]
            print(f"   Версії: {versions}")
            print(f"   Остання версія: {versions[-1] if versions else 'NONE'}")
        except Exception as e:
            print(f" Помилка: {e}")
    
    print("\n2. Всі таблиці в lr3_schema:")
    inspector = inspect(engine)
    tables = inspector.get_table_names(schema='lr3_schema')
    for table in tables:
        print(f"   - {table}")
    
    print("\n3. Таблиці моделей:")
    model_tables = ['cat_facts', 'cat_fact_stats']
    for table in model_tables:
        exists = table in tables
        print(f"   - {table}: {'' if exists else ''}")
    
    print(f"\n Всього таблиць у схемі: {len(tables)}")
    
except Exception as e:
    print(f" Помилка: {e}")