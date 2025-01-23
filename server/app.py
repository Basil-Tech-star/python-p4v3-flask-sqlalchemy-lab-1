# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake_by_id(id):
    earthquake = Earthquake.query.get(id)

    if earthquake is None:
        response_data = {
            'message': f'Earthquake {id} not found.'
        }
        return jsonify(response_data), 404
    
    earthquake_data = earthquake.to_dict()

    return jsonify(earthquake_data), 200

# Add views here
@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    earthquake_data = [earthquake.to_dict() for earthquake in earthquakes]

    response_data = {
        'count': len(earthquake_data),
        'quakes': earthquake_data
    }

    return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
