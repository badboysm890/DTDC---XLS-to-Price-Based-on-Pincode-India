from flask import request, make_response, send_file, Flask
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

@app.route('/download_csv', methods=['GET', 'POST'])
def download_csv():
    try:
        os.remove('data.csv')
    except:
        pass
    data = request.get_json()
    print(data)
    csv_file = create_csv_file(data)
    return "success"
 
 # endpoint to download csv file
@app.route('/download_file', methods=['GET', 'POST'])
def download_file():
    path = "data.csv"
    return send_file(path, as_attachment=True) 

def create_csv_file(data):

    #  {'0': {'pincode': 636005, 'weight': 1.02, 'mode': 'AR'}, ... }
    # convert to csv file
    df = pd.DataFrame.from_dict(data, orient='index')
    df.to_csv('data.csv', index=False)
    
    return "success"



if __name__ == "__main__":
    app.run(debug=True)
