from flask import Flask, jsonify
import csv
import api_logger
app = Flask(__name__)

import os
def getfileName(filename):
    file = os.path.join(os.path.dirname(__file__), filename)
    print(file)
    return file

@app.route('/api/data',methods=['GET'])
def getSmokingData():
    api_logger.logger.info(msg='Calling GET METHOD')
    data = []
    '''
    Read Data from CVS
    '''
    file = getfileName("data/smoking.csv")
    with open(file,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
        return jsonify(data)
    
        
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
        
