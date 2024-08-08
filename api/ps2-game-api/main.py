from flask import Flask
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

data = pd.read_csv('ps2_data.csv')
ps2_data = data.to_dict(orient='records')

class GetGame(Resource):
    def get(self,Game):
        parsed_data = []
        try: 
            for record in range(len(ps2_data)):
                if ps2_data[record]["Game"].lower() == Game.lower():
                    user_search = ps2_data[record]
                    # game = ps2_data[record].pop("Game")  # Extract the 'Game' field
                    # rest_of_data = ps2_data[record]  # The rest of the data
                    # parsed_data.append({
                    #     'Game': game,
                    #     'Details': rest_of_data
                    # })
                    return user_search
            raise Exception(f"{Game} not found")
        except:
            return(f"{Game} not found")
        
class AllGame(Resource):
    def get(self):
        return ps2_data 

api.add_resource(AllGame, "/")    
api.add_resource(GetGame, "/getgame/<string:Game>")

if __name__ == "__main__":
    app.run(debug=True)