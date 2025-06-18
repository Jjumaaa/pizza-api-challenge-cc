Pizza Restaurant API ChallengeThis is a RESTful API for a Pizza Restaurant built using Flask, SQLAlchemy, and SQLite, following the MVC (Model-View-Controller) pattern.StatusProject setup is complete with all routes implemented, database migrations applied, and database seeded successfully. Currently testing the POST /restaurant_pizzas endpoint and other routes using Postman to ensure functionality meets requirements.Setup InstructionsClone the repository:git clone https://github.com/<your-username>/pizza-api-challenge.git
cd pizza-api-challengeSet up virtual environment:pipenv install flask flask_sqlalchemy flask_migrate
pipenv shellSet Flask environment variable:export FLASK_APP=server/app.pyInitialize database:flask db init
flask db migrate -m "Initial migration"
flask db upgradeSeed the database:python server/seed.pyRun the application:flask runDatabase Migration & SeedingMigration: The database is managed using Flask-Migrate. To create new migrations, run:flask db migrate -m "Your migration message"To apply migrations, run:flask db upgradeSeeding: The server/seed.py script populates the database with sample data, including:3 restaurants (e.g., "Dominion Pizza", "Kiki's Pizza", "Pizza Palace")3 pizzas (e.g., "Margherita", "Pepperoni", "Veggie")4 restaurant-pizza relationships To seed the database, run:python server/seed.pyRoute SummaryMethodEndpointDescriptionGET/restaurantsReturns a list of all restaurantsGET/restaurants/<id>Returns details of a restaurant and its pizzasDELETE/restaurants/<id>Deletes a restaurant and its related pizzasGET/pizzasReturns a list of all pizzasPOST/restaurant_pizzasCreates a new restaurant-pizza relationshipExample Requests & ResponsesGET /restaurantsResponse (200 OK):[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "123 Main St",
    "restaurant_pizzas": [
      {
        "id": 1,
        "price": 10,
        "pizza_id": 1,
        "restaurant_id": 1,
        "pizza": { "id": 1, "name": "Margherita", "ingredients": "Dough, Tomato Sauce, Cheese, Basil" },
        "restaurant": { "id": 1, "name": "Dominion Pizza", "address": "123 Main St" }
      }
    ]
  }
]GET /restaurants/Response (200 OK):{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "123 Main St",
  "restaurant_pizzas": [
    {
      "id": 1,
      "price": 10,
      "pizza_id": 1,
      "restaurant_id": 1,
      "pizza": { "id": 1, "name": "Margherita", "ingredients": "Dough, Tomato Sauce, Cheese, Basil" },
      "restaurant": { "id": 1, "name": "Dominion Pizza", "address": "123 Main St" }
    }
  ]
}Error (404 Not Found):{ "error": "Restaurant not found" }DELETE /restaurants/Response (204 No Content): (No body) Error (404 Not Found):{ "error": "Restaurant not found" }GET /pizzasResponse (200 OK):[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese, Basil"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  },
  {
    "id": 3,
    "name": "Veggie",
    "ingredients": "Dough, Tomato Sauce, Cheese, Veggies"
  }
]POST /restaurant_pizzasRequest:{ "price": 5, "pizza_id": 1, "restaurant_id": 3 }Response (201 Created):{
  "id": 5,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": { "id": 1, "name": "Margherita", "ingredients": "Dough, Tomato Sauce, Cheese, Basil" },
  "restaurant": { "id": 3, "name": "Pizza Palace", "address": "789 Pine Rd" }
}Error (400 Bad Request):{ "errors": ["Price must be between 1 and 30"] }Error (404 Not Found):{ "errors": ["Restaurant or Pizza not found"] }Validation RulesRestaurantPizza.price: Must be an integer between 1 and 30.RestaurantPizza.restaurant_id: Must reference an existing Restaurant in the database.RestaurantPizza.pizza_id: Must reference an existing Pizza in the database.Cascading Deletes: Deleting a Restaurant also deletes its associated RestaurantPizza records (enforced via cascade='all, delete-orphan').Postman Usage InstructionsOpen Postman.Click Import and upload challenge-1-pizzas.postman_collection.json.Set the baseUrl variable to http://localhost:5000.Ensure the Flask server is running:flask runExecute each request in the collection to test the API endpoints:GET /restaurantsGET /restaurants/DELETE /restaurants/GET /pizzasPOST /restaurant_pizzasVerify that responses match the expected status codes and payloads described above.Project Structurepizza-api-challenge/
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
└── README.mdDependenciesThe following Python packages are required and can be installed via Pipenv:flaskflask_sqlalchemyflask_migrateInstall them using:pipenv install flask flask_sqlalchemy flask_migrateNotesThe API uses SQLite (pizza_restaurant.db) as the database, configured in server/config.py.The server/seed.py script should be run after database migrations to populate sample data.Ensure the virtual environment is active (pipenv shell) before running Flask commands or the seed script.Test all endpoints thoroughly with Postman to confirm functionality, especially the POST /restaurant_pizzas endpoint for creating new restaurant-pizza relationships.