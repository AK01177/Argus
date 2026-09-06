from dotenv import load_dotenv

# This magic line loads everything from your .env file into the system environment
load_dotenv() 

from app.db import SessionLocal
from app.services.ingestion_service import IngestionService

db = SessionLocal()
service = IngestionService(db)

print("Starting ingestion...")
service.process_repo(repo_id=1)
print("Done!")
