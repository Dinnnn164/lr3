import os

class Settings:
    postgres_sync = os.getenv("INTERNAL_DATABASE_URL", "postgresql://lr3_user:Sumsung@localhost:5432/lr3")

settings = Settings()