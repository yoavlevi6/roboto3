from flask import Flask, Response, request, send_from_directory
import time
import os

app = Flask(__name__)

ultrasonic_status = 100  # initialize with a value greater than 25

def ultrasonic_sensor_events():
    while True:
        yield f"data: {ultrasonic_status}\n\n"
        time.sleep(1)

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/script.js')
def script():
    return send_from_directory(os.getcwd(), 'script.js')

@app.route('/ultrasonic_events', methods=['GET'])
def ultrasonic_events():
    return Response(ultrasonic_sensor_events(), content_type='text/event-stream')

@app.route('/update_ultrasonic_status', methods=['GET'])
def update_ultrasonic_status():
    global ultrasonic_status
    ultrasonic_status = request.args.get('status')
    print(f"Received status: {ultrasonic_status}")  # הוסף את השורה הזו לאבחון
    return "Status received", 200

if __name__ == '__main__':
    app.run(debug=True)
