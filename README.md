# Flask Code Challenge - Pizza Restaurants

## Introduction
This Flask Code Challenge focuses on building a RESTful API for managing pizza restaurants and their menus. The task involves creating endpoints for retrieving restaurant information, deleting restaurants, listing available pizzas, and adding new pizzas to restaurants.

## Models
The application revolves around the following relationships:
- A Restaurant has many Pizzas through RestaurantPizza
- A Pizza has many Restaurants through RestaurantPizza
- A RestaurantPizza belongs to a Restaurant and belongs to a Pizza

## Validations
Validations are applied to ensure data integrity:
- RestaurantPizza must have a price between 1 and 30
- Restaurant name must be less than 50 characters in length and must be unique

## Routes
The following routes are provided:

- **GET /restaurants**: Retrieve a list of restaurants.
- **GET /restaurants/:id**: Retrieve details of a specific restaurant including its pizzas.
- **DELETE /restaurants/:id**: Delete a restaurant and its associated pizzas.
- **GET /pizzas**: Retrieve a list of available pizzas.
- **POST /restaurant_pizzas**: Add a new pizza to a restaurant.

Each route returns JSON data in the specified format and responds with appropriate HTTP status codes.

