from flask import Flask, request
from flask_restful import Resource, Api
from scraper import get_scraped_data

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        postal_code = request.args.get('postal_code')
        if postal_code:
            data = get_scraped_data(postal_code)
        else:
            data = []
        return {'data':data}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
