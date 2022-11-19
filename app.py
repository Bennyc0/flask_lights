from flask import Flask, render_template, request
from gpiozero import LED
from time import sleep

app = Flask(__name__)
led = LED(17)
last_cmd = "off"

@app.route('/')
def index_page():
    global active
    active = False
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/received', methods=['POST'])
def received_page():
    global active
    if request.form['light_cmd'].lower() != "":
        cmd = request.form['light_cmd'].lower()

        if cmd == "on" or cmd == "blink" or cmd == "off":
            active = False
            if cmd == "on":
                led.on()
            elif cmd == "blink":
                active = True
                while active:
                    led.on()
                    sleep(0.5)
                    led.off()
                    sleep(0.5)
            elif cmd == "off":
                led.off()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
