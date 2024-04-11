from app import app
from models import db, Restaurant, Pizza, RestaurantPizza



with app.app_context():

    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()


    restaurants = []
    
    restaurants.append(Restaurant(name='Crispy Crust Pizzeria', address='345 Pie Avenue'))
    restaurants.append(Restaurant(name='Oven Fresh Pizzas', address='1212 Fresh Ave'))
    restaurants.append(Restaurant(name='Dough Delight', address='1111 Dough St'))
    restaurants.append(Restaurant(name='Pizza Planet', address='1010 Planet Pl'))
    restaurants.append(Restaurant(name='Cheesy Crust', address='999 Cheesy Rd'))
    restaurants.append(Restaurant(name='Slice of Heaven', address='888 Slice Blvd'))
    restaurants.append(Restaurant(name='The Pizza Hut', address='777 Pizza St'))
    restaurants.append(Restaurant(name='Pepperoni Paradise', address='666 Pepperoni Ln'))
    restaurants.append(Restaurant(name='Pizzeria Italia', address='555 Italia Ave'))
    restaurants.append(Restaurant(name='Pizza Palace', address='444 Pizza Pl'))
    restaurants.append(Restaurant(name='Dessert Dream', address='333 Dessert St'))
    restaurants.append(Restaurant(name='Noodle House', address='111 Noodle Ave'))
    
    db.session.add_all(restaurants)

    pizzas = []
    
    pizzas.append(Pizza(name='Margherita', ingredients='Tomato, Mozzarella, Basil'))
    pizzas.append(Pizza(name='Pepperoni', ingredients='Tomato, Mozzarella, Pepperoni'))
    pizzas.append(Pizza(name='Vegetarian', ingredients='Tomato, Mozzarella, Mixed Vegetables'))
    pizzas.append(Pizza(name='Hawaiian', ingredients='Tomato, Mozzarella, Ham, Pineapple'))
    pizzas.append(Pizza(name='BBQ Chicken', ingredients='BBQ Sauce, Mozzarella, Chicken, Red Onion'))
    pizzas.append(Pizza(name='Supreme', ingredients='Tomato, Mozzarella, Pepperoni, Mushroom, Bell Pepper, Olive'))
    pizzas.append(Pizza(name='Seafood', ingredients='Tomato, Mozzarella, Shrimp, Calamari, Clam"'))
    pizzas.append(Pizza(name='Mushroom Lovers', ingredients='Tomato, Mozzarella, Mushroom Variety'))
    pizzas.append(Pizza(name='Meat Feast', ingredients='Tomato, Mozzarella, Sausage, Bacon, Ham, Pepperoni'))
    pizzas.append(Pizza(name='Four Cheese', ingredients='Mozzarella, Cheddar, Gorgonzola, Parmesan'))
    
    
    restaurant_pizzas = []
    
    restaurant_pizzas.append(RestaurantPizza(price=10, restaurant=restaurants[0], pizza=pizzas[0]))
    restaurant_pizzas.append(RestaurantPizza(price=12, restaurant=restaurants[1], pizza=pizzas[1]))
    restaurant_pizzas.append(RestaurantPizza(price=11, restaurant=restaurants[2], pizza=pizzas[2]))
    restaurant_pizzas.append(RestaurantPizza(price=13, restaurant=restaurants[3], pizza=pizzas[3]))
    restaurant_pizzas.append(RestaurantPizza(price=15, restaurant=restaurants[4], pizza=pizzas[4]))
    restaurant_pizzas.append(RestaurantPizza(price=14, restaurant=restaurants[5], pizza=pizzas[5]))
    restaurant_pizzas.append(RestaurantPizza(price=16, restaurant=restaurants[6], pizza=pizzas[6]))
    restaurant_pizzas.append(RestaurantPizza(price=17, restaurant=restaurants[7], pizza=pizzas[7]))
    restaurant_pizzas.append(RestaurantPizza(price=18, restaurant=restaurants[8], pizza=pizzas[8]))
    restaurant_pizzas.append(RestaurantPizza(price=19, restaurant=restaurants[9], pizza=pizzas[9]))
    
    db.session.add_all(restaurant_pizzas)
    db.session.commit()