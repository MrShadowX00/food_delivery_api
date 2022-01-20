## Test PIZZA DELIVERY API
This is a REST API for a Pizza delivery service built for fun and learning with FastAPI, SQLAlchemy and PostgreSQL. The video playlist is 


## ROUTES TO IMPLEMENT
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/signup/``` | _Register new user_| _All users_|
| *POST* | ```/auth/login/``` | _Login user_|_All users_|
| *POST* | ```/orders/order/``` | _Place an order_|_All users_|
| *PUT* | ```/order/order/update/{order_id}/``` | _Update an order_|_All users_|
| *PUT* | ```/order/order/status/{order_id}/``` | _Update order status_|_Superuser_|
| *DELETE* | ```/order/order/delete/{order_id}/``` | _Delete/Remove an order_ |_All users_|
| *GET* | ```/order/user/orders/``` | _Get user's orders_|_All users_|
| *GET* | ```/order/orders/``` | _List all orders made_|_Superuser_|
| *GET* | ```/order/orders/{order_id}/``` | _Retrieve an order_|_Superuser_|
| *GET* | ```/order/user/orders/{order_id}/``` | _Get user's specific order_|
| *GET* | ```/docs/``` | _View API documentation_|_All users_|

## How to run the Project
- Install Postgreql
- Install Python
- Git clone the project with ``` git clone https://github.com/MrShadowX00/food_delivery_api```
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with ``` pip install -r requirements.txt ```
- Set Up your PostgreSQL database and set its URI in your ```database.py```
```
engine=create_engine('postgresql://postgres:<username>:<password>@localhost/<db_name>',
    echo=True
)
```

- Create your database by running ``` python init_db.py ```
- Finally run the API
``` uvicorn main:app ``