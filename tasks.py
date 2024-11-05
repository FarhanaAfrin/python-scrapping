# tasks.py
from sqlalchemy.orm import Session
from models import Task
from scrape import PDFGenerator

def scrape_and_generate_pdf(task_id: int, db: Session):
    task = db.query(Task).filter(Task.id == task_id).first()
    task.status = "in_progress"
    db.commit()

    with PDFGenerator() as generator:
        generator.extract_content_and_generate_pdf(task, db)
