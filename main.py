from fastapi import FastAPI

from api.employee.controllers import router as employee_router
from api.order.controllers import router as order_router

app = FastAPI()


app.include_router(employee_router)
app.include_router(order_router)
