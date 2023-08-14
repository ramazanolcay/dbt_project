from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from id_pw import my_id,my_pw
from faker import Faker
import faker_commerce
import numpy as np
from datetime import datetime,timedelta

db_url = f"postgresql://{my_id}:{my_pw}@localhost:5432"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    pw = Column(String)
    
class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    item_name = Column(String)


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    name_id = Column(Integer)
    item_id = Column(Integer)
    order_time = Column(DateTime)

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
faker = Faker()
for i in range(10000):
    name = faker.name()
    name = name.split(" ")
    surname = name[1]
    name = name[0]
    email = faker.email()
    pw = faker.password()
    new_user = User(name = name, surname= surname, email=email, pw=pw)
    try:
        session.add(new_user)
    except:
        pass

faker.add_provider(faker_commerce.Provider)
for i in range(200):
    item_name = faker.ecommerce_name()
    new_item = Items(item_name=item_name)
    try:
        session.add(new_item)
    except:
        pass

user_num = session.query(User).count()
item_num = session.query(Items).count()

start_date = datetime(2020, 1, 1, 0, 0, 0)
for i in range(30000):
    user_random = np.random.randint(low=1, high = user_num)
    item_random = np.random.randint(low=1, high = item_num)
    order_time = faker.date_time_between(start_date= start_date, end_date = (start_date + timedelta(hours=1)))
    start_date += timedelta(hours=1)
    new_order = Orders(name_id = user_random, item_id = item_random, order_time = order_time)
    try:
        session.add(new_order)
    except:
        pass

session.commit()
session.close()