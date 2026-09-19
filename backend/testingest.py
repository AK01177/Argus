from app.db import SessionLocal
from app.models.repo import Repo
from app.models.user import User
from app.services.ingestion_service import IngestionService
from dotenv import load_dotenv

load_dotenv()

print("Starting ingestion test...")

db = SessionLocal()

try:
    # 1. Create a dummy user if it doesn't exist
    dummy_user = db.query(User).filter(User.id == 1).first()
    if not dummy_user:
        dummy_user = User(id=1, username="test_user", github_id="12345", email="test@argus.com")
        db.add(dummy_user)
        db.commit()
        print("Created Dummy User!")

    # 2. Create a dummy repo (or grab it if it already exists)
    repo_url = "/home/aryan/Desktop/Argus/"
    dummy_repo = db.query(Repo).filter(Repo.url == repo_url).first()
    
    if not dummy_repo:
        dummy_repo = Repo(
            name="Argus Backend Test", 
            url=repo_url,
            user_id=1, 
            is_private=False
        )
        db.add(dummy_repo)
        db.commit()
    
    print(f"Using Dummy Repo with ID: {dummy_repo.id}")


    # 3. Run the ingestion service on it
    service = IngestionService(db)
    service.process_repo(dummy_repo.id)
    
except Exception as e:
    print(f"Test failed: {e}")
finally:
    db.close()
