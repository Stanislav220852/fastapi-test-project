from app.db.base import Base   
from sqlalchemy.orm import Mapped,mapped_column

class UserModel(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    password:Mapped[str]
    email:Mapped[str]

