from sqlalchemy import Column, Integer, String, DateTime, Text

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class CatFact(Base):
    __tablename__ = "cat_facts"
    __table_args__ = {'schema': 'lr3_schema'}
    
    id = Column(Integer, primary_key=True, index=True)
    fact = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)

class CatFactStats(Base):
    __tablename__ = "cat_fact_stats"
    __table_args__ = {'schema': 'lr3_schema'}
    
    id = Column(Integer, primary_key=True, index=True)
    total_facts = Column(Integer, default=0)
    last_updated = Column(DateTime, nullable=False)