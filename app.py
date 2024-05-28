from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)
last_update_time = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status', methods=['GET'])
def status():
    global last_update_time
    current_time = time.time()
    if current_time - last_update_time < 10:
        return jsonify(status='green')
    else:
        return jsonify(status='red')

@app.route('/update', methods=['POST'])
def update():
    global last_update_time
    last_update_time = time.time()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
