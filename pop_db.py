from Pizzza import pizza,customer,pizzaorder,employee,payment
from sqlmodel import SQLModel, Session, create_engine

# Создаем базу данных
engine = create_engine("sqlite:///pizzeria.db")
SQLModel.metadata.create_all(engine)
# Заполняем базу данных
with Session(engine) as session:
    # Добавляем пиццы
    pizza1 = pizza(id=1,name="Маргарита", price=8.50)
    pizza2 = pizza(id=2,name="Пепперони", price=9.00)
    session.add(pizza1)
    session.add(pizza2)
    # Добавляем клиентов
    customer1 = customer(id=1,name="Иван Иванов", email="ivan@example.com")
    customer2 = customer(id=2,name="Мария Петрова", email="maria@example.com")
    session.add(customer1)
    session.add(customer2)
    # Добавляем заказы
    order1 = pizzaorder(id=1,customer_id=customer1.id, pizza_id=pizza1.id, quantity=2)
    order2 = pizzaorder(id=2,customer_id=customer2.id, pizza_id=pizza2.id, quantity=1)
    session.add(order1)
    session.add(order2)
    # Создаем сотрудников
    employee1 = employee(id=1,name="Алексей Смирнов", position="Повар", salary=30000)
    employee2 = employee(id=2,name="Ольга Кузнецова", position="Официант", salary=25000)
    session.add(employee1)
    session.add(employee2)
    
    # Создаем платежи
    payment1 = payment(id=1,order_id=order1.id, amount=17.00, payment_date="2024-12-15")
    payment2 = payment(id=2,order_id=order2.id, amount=9.00, payment_date="2024-12-15")
    session.add(payment1)
    session.add(payment2)
    
    session.commit()

