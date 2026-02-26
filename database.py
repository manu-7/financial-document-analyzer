from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///analysis.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(Text)
    query = Column(Text)
    result = Column(Text)

Base.metadata.create_all(bind=engine)