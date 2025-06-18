## Pizza Restaurant API Challenge
- A Flask-based RESTful API for a pizza restaurant, built with Flask, SQLAlchemy, SQLite, and following the MVC pattern.
## Setup Instructions
# 1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Jjuma/pizza-api-challenge-cc.git
cd pizza-api-challenge
# 2. Open in VS Code
Launch VS Code
Open the folder: File > Open Folder > pizza-api-challenge
# 3. Install Dependencies
bash
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
# 4. Set Flask Environment
bash
export FLASK_APP=server/app.py
# 5. Initialize and Migrate Database
bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
# 6. Seed the Database
bash
python server/seed.py
# 7. Run the Server
bash
flask run
## Project Structure
pizza-api-challenge-cc/
├── server/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   ├── restaurant_pizza.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   ├── restaurant_pizza_controller.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
├── .gitignore
├── Pipfile
└── README.md

# API Endpoints
Method	Endpoint	Description
GET	/restaurants	List all restaurants with their pizzas
GET	/restaurants/<id>	Get details of a specific restaurant
DELETE	/restaurants/<id>	Delete a restaurant and its pizzas
GET	/pizzas	List all pizzas
POST	/restaurant_pizzas	Create a new restaurant-pizza relation

# Postman Testing
Import challenge-1-pizzas.postman_collection.json into Postman

Set base URL:
http://localhost:5000
Start the server:

bash
flask run
Test all endpoints using the Postman collection

Notes
SQLite database: pizza_restaurant.db

Always run seed.py before testing
