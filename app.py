from flask import Flask
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api= Api(app)
csv_path = './api.csv'

class csv(Resource):
    def get(self):
        data = pd.read_csv(csv_path)
        data = data.to_dict()
        return {'data': data}, 200

api.add_resource(csv, '/csv')

if __name__ == '__main__':
    app.run(debug=True)