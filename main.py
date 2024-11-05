from fastapi import FastAPI, Depends
from fastapi_utils.tasks import repeat_every
from sqlalchemy.orm import Session
from models import Task, init_db, SessionLocal
from tasks import scrape_and_generate_pdf

app = FastAPI()
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
@repeat_every(seconds=3600)  # Runs every hour
def periodic_update_check(db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.status == "completed").all()
    for task in tasks:
        scrape_and_generate_pdf(task.id, db)

@app.post("/start-task/")
async def start_task(url: str, db: Session = Depends(get_db)):
    task = Task(url=url, status="pending")
    db.add(task)
    db.commit()
    return {"task_id": task.id, "status": "started"}

@app.get("/task-status/{task_id}")
async def task_status(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return {"error": "Task not found"}
    return {"task_id": task.id, "status": task.status, "result_path": task.result_path}
