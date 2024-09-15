from flask import Flask

app = Flask(__name__)

# Defining endpoint for home
@app.route('/')
def home():  # put application's code here
    return 'API SHORTENER!'

# Defining endpoint for shortening urls
@app.route('/shorten', methods=['POST'])
def shorten():
    return 0

# Defining endpoint for retrieving original urls from shortened ones
@app.route('/retrieve', methods=['GET'])
def retrieve():
    return 0


# Defining endpoint for updating a shorten url
@app.route('/update', methods=['PUT'])
def update():
    return 0


# Defining endpoint for deleting a shorten url
@app.route('/delete', methods=['DELETE'])
def delete():
    return 0


# Defining endpoint for getting the statistics on short url
@app.route('/get_statistics', methods=['GET'])
def get_statistics():
    return 0


if __name__ == '__main__':
    app.run()
