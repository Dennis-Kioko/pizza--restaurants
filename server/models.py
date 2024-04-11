from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    
    serialize_rules=('-pizzas.restaurant',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    address= db.Column(db.String,)
    
    
    # Relationship mapping the restaurant to related restaurantpizzas
    restaurantpizzas = db.relationship(
        'RestaurantPizza', back_populates="restaurant", cascade='all, delete-orphan')
    
    #Association proxy
    pizzas = association_proxy('restaurantpizzas', 'pizza',creator = lambda item_obj : RestaurantPizza(pizza =pizza_obj))
    
    @validates('name')
    def validate_name(self,key,name):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters.")
        return name
    
    def __repr__(self):
        return f"<Restaurant(id={self.id}, name={self.name}, address={self.address})>"
    

class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__ = 'restaurantpizzas'
    serialize_rules = ('-restaurant.restaurantpizzas','-pizza.restaurantpizzas')


    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    # relationship to Restaurant
    restaurant = db.relationship('Restaurant', back_populates='restaurantpizzas')

    # relationship to Pizza
    pizza = db.relationship('Pizza', back_populates='restaurantpizzas')

    @validates('price')
    def validate_price(self,key,price):
        if not 1 <= price <= 30:
            raise ValueError('Price must be between 1 and 30')
        return price

    
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    
    serialize_rules=('-restaurant.pizzas', '-restaurantpizza.pizzas',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String,)
    
    # Relationship mapping the pizza to related restaurantpizzas
    restaurantpizzas = db.relationship(
        'RestaurantPizza', back_populates='pizza', cascade="all, delete-orphan")
    
    
    restaurants = association_proxy('restaurantpizzas','restaurant', creator= lambda restaurant_obj: RestaurantPizza(restaurant = restaurant_obj) )
