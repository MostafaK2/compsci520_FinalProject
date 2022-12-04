from flask import Flask, request
from controller.GraphUtils import get_shortest_path
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
    return 'ELeNA Server'

@app.route('/metadata')
@cross_origin()
def get_path():
    src = []
    dest = []
    flag = 0
    percent = 0
    for arg in request.args:
        if(arg == "flag"):
            flag = request.args[arg]
        elif(arg == "src"):
            src = request.args[arg].split(',')
        elif(arg == "dest"):
            dest = request.args[arg].split(',')
        else:
            percent = request.args[arg]
    path = get_shortest_path(src, dest)
    return path

 
if __name__ == '__main__':
    app.run()