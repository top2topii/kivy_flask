import threading
import kivy
from kivy.app import App
from flask import Flask
import os
from kivy.uix.label import Label

kivy.require('1.10.0')
new_environ = os.environ.copy()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'
def start_app():
    print("Starting Flask app...")
    app.run(port=5000, debug=False)     #specify separate port to run Flask app

class MyApp(App):

    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    if os.environ.get("WERKZEUG_RUN_MAIN") != 'true':
        threading.Thread(target=start_app).start()
    MyApp().run()
