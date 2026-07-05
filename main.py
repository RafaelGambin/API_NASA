import os
import requests
from flask import Flask
from dotenv import load_dotenv
from flask_restx import Api, Resource, fields
from src.infra.database.connection import conection_db

load_dotenv()


api_key = os.getenv("API_KEY")

app = Flask(__name__)

api = Api(app, version='1.0', title='NASA API', description='This is The NASA API')

ns = api.namespace('astronomy_picture_of_the_day', description='Astronomy Picture of the Day operations')


todo = api.model('AstronomyPictureOfTheDay', {
    'token': fields.String(required=True, description='The token for the API request'),
})

@ns.route(f"/teste", methods=["GET"])
class GetAstronomyPictureOfTheDay(Resource):
    def get(self):

        data = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")


        return data.json(), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
