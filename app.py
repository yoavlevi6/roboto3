from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)
last_button_update_time = 0
ultrasonic_status = 'red'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status', methods=['GET'])
def status():
    global last_button_update_time
    current_time = time.time()
    button_status = 'green' if current_time - last_button_update_time < 10 else 'red'
    return jsonify(button_status=button_status, ultrasonic_status=ultrasonic_status)

@app.route('/update', methods=['POST'])
def update():
    global last_button_update_time
    last_button_update_time = time.time()
    return '', 204

@app.route('/update_ultrasonic', methods=['POST'])
def update_ultrasonic():
    global ultrasonic_status
    distance = request.json.get('distance', 100)  # Default distance if not provided
    if 25 <= distance <= 50:
        ultrasonic_status = 'green'
    else:
        ultrasonic_status = 'red'
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
