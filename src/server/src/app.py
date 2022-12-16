from flask import Flask, request
from controller.GraphUtils import get_shortest_path, get_shortest_path_helper
from model.LocationHelper import get_details
from model.utility import save_graph, check_graph_present
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
    city, state, country = get_details(src, dest)
    if(city == ""): return "error"

    flag = int(flag)

    file_name = "../data/"+(city+state+country).replace(' ', '')+".graphml"
    if(check_graph_present(file_name) == False):
        save_graph(city + ", " + state + ", " + country, file_name)

    if flag == 1 or flag == 2:
        res = get_shortest_path((float(src[0]), float(src[1])), (float(dest[0]), float(dest[1])), float(percent), flag, file_name)
    else:
        res = get_shortest_path_helper((float(src[0]), float(src[1])), (float(dest[0]), float(dest[1])), file_name)
        
    return res

if __name__ == '__main__':
    app.run()