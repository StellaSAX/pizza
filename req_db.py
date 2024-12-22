from sqlmodel import Session, select
from Pizzza import Pizza,Customer,PizzaOrder,Employee,Payment

def get_orders_with_details(session: Session):
    query = text(
        "SELECT c.name AS customer_name, p.name AS pizza_name,"
        "'Кол-во: ' as MESSAGE, o.quantity "
        "FROM PizzaOrder o "
        "JOIN Customer c ON o.customer_id = c.id "
        "JOIN Pizza p ON o.pizza_id = p.id"
    )
    orders = session.execute(query).all()
    return orders
def get_all_employees(session: Session):
    return session.query(Employee).all()
def get_all_payments(session: Session):
    return session.query(Payment).all()
