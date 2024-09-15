from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return 'API SHORTENER!'

@app.route('/shorten', methods=['POST'])
def shorten():


@app.route('/retrieve', methods=['GET'])
def retrieve():


@app.route('/update', methods=['PUT'])
def update():


@app.route('/delete', methods=['DELETE'])
def delete():


@app.route('/get_statistics', methods=['GET'])
def get_statistics():


if __name__ == '__main__':
    app.run()
