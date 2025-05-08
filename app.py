from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Almacenamiento temporal de ubicaciones (en memoria)
user_locations = {}

# Ruta para actualizar la ubicación de un usuario
@app.route('/update-location', methods=['POST'])
def update_location():
    data = request.json
    user_id = data.get('userId')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if not user_id or latitude is None or longitude is None:
        return jsonify({'error': 'Faltan datos'}), 400

    user_locations[user_id] = {'latitude': latitude, 'longitude': longitude}
    return jsonify({'message': 'Ubicación actualizada'})

# Ruta para obtener la ubicación de un usuario por ID
@app.route('/get-location/<user_id>', methods=['GET'])
def get_location(user_id):
    location = user_locations.get(user_id)
    if not location:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    return jsonify(location)

if __name__ == '__main__':
    app.run(debug=True)