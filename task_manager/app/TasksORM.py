from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column

engine = create_engine('sqlite:///tasks_manager.db')


class Base(DeclarativeBase):
    pass


Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


class Task(Base):
    __tablename__ = 'Tasks'
    id: Mapped[int] = mapped_column('id', primary_key=True)
    task: Mapped[str] = mapped_column('task')
    completed: Mapped[bool] = mapped_column('completed')