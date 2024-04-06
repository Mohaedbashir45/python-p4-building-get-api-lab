from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bakeries.db'
db = SQLAlchemy(app)

# Define your models (Bakery and BakedGood) here using SQLAlchemy


# Implement your routes here
@app.route('/bakeries', methods=['GET'])
def get_bakeries():
    # Query all bakeries from the database
    # Serialize the data and return as JSON
    return jsonify([bakery.serialize() for bakery in Bakery.query.all()])

@app.route('/bakeries/<int:id>', methods=['GET'])
def get_bakery(id):
    # Query a single bakery by id from the database
    # Serialize the data and return as JSON
    bakery = Bakery.query.get(id)
    if bakery:
        return jsonify(bakery.serialize())
    else:
        return jsonify({"message": "Bakery not found"}), 404

@app.route('/baked_goods/by_price', methods=['GET'])
def get_baked_goods_by_price():
    # Query all baked goods sorted by price in descending order
    # Serialize the data and return as JSON
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    return jsonify([good.serialize() for good in baked_goods])

@app.route('/baked_goods/most_expensive', methods=['GET'])
def get_most_expensive_baked_good():
    # Query the most expensive baked good from the database
    # Serialize the data and return as JSON
    most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).first()
    if most_expensive:
        return jsonify(most_expensive.serialize())
    else:
        return jsonify({"message": "No baked goods found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
