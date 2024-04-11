from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from models import db, Restaurant, RestaurantPizza, Pizza


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    body = '<h1>Pizza Restaurants API</h1>'
    return make_response(body, 200)


@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    if request.method == 'GET':
        restaurants = [
            restaurant.to_dict() for restaurant in Restaurant.query.all()]
        response = make_response(
            jsonify(restaurants),
            200
        )

        return response
    
@app.route('/restaurants/<int:id>', methods = ['GET'])
def restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        restaurant_data = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "pizzas": []
        }
        for pizza in restaurant.pizzas:
            pizza_data = pizza.to_dict()
            restaurant_data["pizzas"].append(pizza_data)

        response = make_response(jsonify(restaurant_data), 200)
        return response
    else:
        response_body = {
            "Error": "Restaurant not found."
        }
        response = make_response(jsonify(response_body), 404)
        return response
@app.route('/restaurants/<int:id>' , methods = ['DELETE'])
def delete_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()

        response_body =make_response({
            [],
            200
        })

        return response_body
    else:
        response_body = {
            "Error": "Restaurant not found."
        }
        response = make_response(
            jsonify(response_body),
            404
        )

        return response


@app.route('/pizzas',methods = ['GET'])
def pizzas():
    if request.method == 'GET':
        pizzas = [pizza.to_dict() for pizza in Pizza.query.all()]
        response = make_response(
            jsonify(pizzas),
            200
        )
        return response


@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    # Get data from request
    price = request.json.get('price')
    pizza_id = request.json.get('pizza_id')
    restaurant_id = request.json.get('restaurant_id')

    # Validate input data
    if not all([price, pizza_id, restaurant_id]):
        return jsonify({'errors': ['validation errors']}), 400

    # Check if Pizza and Restaurant exist
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)
    if not pizza or not restaurant:
        return jsonify({'errors': ['Pizza or Restaurant not found']}), 404

    # Create RestaurantPizza object
    new_restaurant_pizza = RestaurantPizza(
        price=price,
        pizza_id=pizza_id,
        restaurant_id=restaurant_id
    )

    # Add to database and commit
    db.session.add(new_restaurant_pizza)
    db.session.commit()

    # Prepare response data
    pizza_data = {
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    }
    response = make_response(
        jsonify(pizza_data), 200
    )
        
    # Return success response with pizza data
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)