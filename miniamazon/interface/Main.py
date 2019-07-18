from dataframe.datas import Main
from flask import *


app = Flask(__name__)
main = Main()


@app.route('/')
def main_page():
    return jsonify({'MESSAGE': 'Welcome to Mini Amazon'})


@app.route('/<string:types>', methods=['GET'])
def search_cat(types):
    return jsonify(main.get_cat(types, request.args))


@app.route('/<string:types>/<string:item>', methods=['GET'])
def search_pro(types, item):
    df = Main.get_pro(types, item)
    return jsonify({})



if __name__ == "__main__":
    app.run(debug=True)
