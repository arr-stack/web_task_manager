import uvicorn
from fastapi import FastAPI, Request, Form
from starlette import status
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from TasksORM import Session, Task
from sqlalchemy import select, insert, delete, update


app = FastAPI()
template = Jinja2Templates(directory='templates')

@app.get('/home')
def home(request: Request):
    with Session() as session:
        tasks = session.execute(select(Task.id, Task.task, Task.completed))
    return template.TemplateResponse(request, 'home.html', {'tasks': tasks, 'title': "Task Manager"})

@app.post('/home/add-task')
def test(task: str = Form(), check: bool = Form()):
    with Session() as session:
        session.execute(insert(Task).values(task=task, completed=check))
        session.commit()
    return RedirectResponse(url='/home', status_code=status.HTTP_303_SEE_OTHER)

@app.post('/home/delete')
def delete_task(task_id: int = Form()):
    with Session() as session:
        session.execute(delete(Task).where(Task.id == task_id))
        session.commit()
    return RedirectResponse(url='/home', status_code=status.HTTP_303_SEE_OTHER)

@app.post('/home/check')
def check_task(task_id: int = Form()):
    with Session() as session:
        value = session.execute(select(Task.completed).where(Task.id == task_id))
        value = value.first()
        value = value[0]
        value = not value
    with Session() as session:
        session.execute(update(Task).where(Task.id == task_id).values(completed=value))
        session.commit()
    return RedirectResponse(url='/home', status_code=status.HTTP_303_SEE_OTHER)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)