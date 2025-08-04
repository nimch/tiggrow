from pathlib import Path

from sqlmodel import create_engine

database_file_path = Path(__file__).resolve().parent.absolute() / "database.db"
engine = create_engine(f"sqlite:///{database_file_path}")
