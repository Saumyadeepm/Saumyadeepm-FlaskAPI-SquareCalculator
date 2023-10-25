from flask import Flask, request, jsonify

app = Flask('__name__')

@app.route('/', methods=['GET', 'POST'])
def get_or_post_data():
    if request.method == 'GET':
        return jsonify({'data': 'Hello Melinda'})
    elif request.method == 'POST':
        data = request.data.decode('utf-8')
        return jsonify({'data': data})

@app.route('/square/<int:num>', methods=['GET'])
def calculate_square(num):
    square = num ** 2
    return jsonify({'square': square})

if __name__ == '__main__':
    app.run(debug=True)
