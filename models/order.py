from sqlalchemy import orm, types, schema
import typing as tp

from models.base import Base

if tp.TYPE_CHECKING:
    from employee import Employee

__all__ = ["Order"]


class Order(Base):
    __tablename__ = 'orders'
    id: orm.Mapped[int] = orm.mapped_column(types.Integer, primary_key=True, autoincrement=True)
    name: orm.Mapped[str] = orm.mapped_column(types.String(32), nullable=False)
    description: orm.Mapped[str] = orm.mapped_column(types.String(32), nullable=False)
    cost: orm.Mapped[int] = orm.mapped_column(types.BigInteger, nullable=False)
    employee_id: orm.Mapped[int] = orm.mapped_column(
        schema.ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    employee: orm.Mapped["Employee"] = orm.relationship(back_populates="orders")
