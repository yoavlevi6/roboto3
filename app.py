from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# משתנה לאחסון הזמן של העדכון האחרון
last_update_time = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    global last_update_time
    last_update_time = time.time()
    return jsonify(success=True)

@app.route('/status', methods=['GET'])
def status():
    global last_update_time
    current_time = time.time()
    if current_time - last_update_time < 10:
        return jsonify(status='green')
    return jsonify(status='red')

if __name__ == '__main__':
    app.run(debug=True)
