from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()
    
    # Hii ni ya Kuseed The Restaurants
    restaurants = [
        Restaurant(name="Pizza Inn", address="Moi Avenue"),
        Restaurant(name="Dominos", address="Peponi Street"),
        Restaurant(name="Dr Pizzaaa", address="Ngong Ln")
    ]
    db.session.bulk_save_objects(restaurants)
    
    # For seeding pizzas
    pizzas = [
        Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese, Basil"),
        Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
        Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Cheese, Veggies")
    ]
    db.session.bulk_save_objects(pizzas)
    
    db.session.commit()
    
    # For seeding RestaurantPizzas
    restaurant_pizzas = [
        RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
        RestaurantPizza(price=12, restaurant_id=1, pizza_id=2),
        RestaurantPizza(price=8, restaurant_id=2, pizza_id=3),
        RestaurantPizza(price=15, restaurant_id=3, pizza_id=1)
    ]
    db.session.bulk_save_objects(restaurant_pizzas)
    
    db.session.commit()
    print("Database seeded successfully!")