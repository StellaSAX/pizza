from sqlmodel import SQLModel, Field, Relationship
from sqlmodel import Session, create_engine

#engine = create_engine("sqlite:///pizzeria.db")

class pizza(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: float
    
class customer(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    
class pizzaorder(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    customer_id: str = Field(foreign_key="customer.id")
    pizza_id: str = Field(foreign_key="pizza.id")
    quantity: int
    
class employee(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    position: str
    salary: float
    
class payment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="pizzaorder.id")
    amount: float
    payment_date: str  # Можно использовать тип datetime для более точного хранения

