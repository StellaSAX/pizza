from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import List
from Pizzza import pizza,customer,pizzaorder,employee,payment

app = FastAPI()

# CRUD операции для Pizza
engine= create_engine("sqlite:///pizzeria.db")
@app.post("/pizzas/", response_model=pizza)
def create_pizza(pizza: pizza):
    with Session(engine) as session:
        session.add(pizza)
        session.commit()
        session.refresh(pizza)
        return pizza

@app.get("/pizzas/", response_model=List[pizza])
def read_pizzas():
    with Session(engine) as session:
        pizzas = session.exec(select(pizza)).all()
        return pizzas

@app.get("/pizzas/{pizza_id}", response_model=pizza)
def read_pizza(pizza_id: int):
    with Session(engine) as session:
        pizza0 = session.get(pizza, pizza_id)
        if not pizza0:
            raise HTTPException(status_code=404, detail="Pizza not found")
        return pizza0

@app.delete("/pizzas/{pizza_id}", response_model=pizza)
def delete_pizza(pizza_id: int):
    with Session(engine) as session:
        pizza1 = session.get(pizza, pizza_id)
        if not pizza1:
            raise HTTPException(status_code=404, detail="Pizza not found")
        session.delete(pizza1)
        session.commit()
        return pizza1

@app.put("/pizzas/{pizza_id}", response_model=pizza)
def update_pizza(pizza_id: int, pizza: pizza):
    with Session(engine) as session:
        existing_pizza = session.get(pizza, pizza_id)
        if not existing_pizza:
            raise HTTPException(status_code=404, detail="Pizza not found")
        
        # Обновляем поля существующей пиццы
        existing_pizza.name = pizza.name
        existing_pizza.price = pizza.price
        
        session.add(existing_pizza)
        session.commit()
        session.refresh(existing_pizza)
        return existing_pizza
        
@app.get("/pizzaorder/", response_model=List[order])
def read_order():
    with Session(engine) as session:
        order = session.exec(select(pizzaorder)).all()
        return order

@app.get("/pizzaorder/{order_id}", response_model=order)
def read_order(order_id: int):
    with Session(engine) as session:
        order_1 = session.get(pizzaorder, order_id)
        if not order_1:
            raise HTTPException(status_code=404, detail="Order not found")
        return order_1

@app.delete("/pizzaorder/{order_id}", response_model=order)
def delete_order(order_id: int):
    with Session(engine) as session:
        order_2 = session.get(pizzaorder, order_id)
        if not order_2:
            raise HTTPException(status_code=404, detail="Order not found")
        session.delete(order_2)
        session.commit()
        return order_2



# Аналогичные CRUD операции можно добавить для других моделей (Customer, PizzaOrder, Employee, Payment)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8010)
