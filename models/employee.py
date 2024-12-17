from sqlalchemy import Integer, String, orm
import typing as tp

from models.base import Base

if tp.TYPE_CHECKING:
    from order import Order


__all__ = ["Employee"]


class Employee(Base):
    __tablename__ = "employees"
    id: orm.Mapped[int] = orm.mapped_column(Integer, primary_key=True, autoincrement=True)
    fio: orm.Mapped[str] = orm.mapped_column(String)
    experience: orm.Mapped[str] = orm.mapped_column(String)
    salary: orm.Mapped[str] = orm.mapped_column(String)

    orders: orm.Mapped[tp.List['Order']] = orm.relationship(
        back_populates="employee", cascade="all, delete")