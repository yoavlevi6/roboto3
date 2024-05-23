from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    # Get the current time
    current_time = time.time()

    # Determine if an hour has passed since a certain event
    if (current_time - start_time) >= 3600:
        circle_color = 'red'
        text_color = 'green'
    else:
        circle_color = 'green'
        text_color = 'red'

    return render_template('index.html', circle_color=circle_color, text_color=text_color)

if __name__ == '__main__':
    start_time = time.time()  # Store the starting time
    app.run(debug=True)