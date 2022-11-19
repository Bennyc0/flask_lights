from flask import Flask, render_template, request
from gpiozero import LED
from time import sleep

app = Flask(__name__)
led = LED(17)
last_cmd = "off"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/received', methods=['POST'])
def received():
    cmd = request.form['light_cmd'].lower()

    if cmd == "on" or cmd == "blink" or cmd == "off":
        if user != last_cmd:
            if user == "on":
                led.on()
            elif user == "off":
                led.off()
            last_cmd = cmd

        else:
            print(f"Hey! The lightbulb is already {last_cmd}! \n")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='7000')
