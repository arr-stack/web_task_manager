from sqlalchemy import select, update
from TasksORM import Session, Task

task_id = 2
#
# with Session() as session:
#     value = session.execute(select(Task.completed).where(Task.id == task_id))
#     value = value.first()
#     value = value[0]
#     value = not value
# with Session() as session:
#     session.execute(update(Task).where(Task.id == task_id).values(completed=value))
#     session.commit()

with Session() as session:
    tasks = session.execute(select(Task.id, Task.task, Task.completed))
    print(tasks.first())
    value = True if tasks.first() else False
    print(value)