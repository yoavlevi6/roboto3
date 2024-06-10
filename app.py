from flask import Flask, Response, send_from_directory
import time
import os

app = Flask(__name__)

# פונקציה זו מפיקה אירועים לחיישן מגנט
def magnet_sensor_events():
    while True:
        magnet_detected = True if time.time() % 5 < 2 else False
        yield f"data: {'detected' if magnet_detected else 'not detected'}\n\n"
        time.sleep(1)

# פונקציה זו מפיקה אירועים לחיישן אולטרהסוניק
def ultrasonic_sensor_events():
    while True:
        distance = 20 if time.time() % 7 < 2 else 30
        yield f"data: {distance}\n\n"
        time.sleep(1)

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/magnet_events', methods=['GET'])
def magnet_events():
    return Response(magnet_sensor_events(), content_type='text/event-stream')

@app.route('/ultrasonic_events', methods=['GET'])
def ultrasonic_events():
    return Response(ultrasonic_sensor_events(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
