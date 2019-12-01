from flask import Flask, render_template, request, redirect
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def forms():
    return render_template('forms.html')

@app.route('/', methods=['POST'])
def my_form():
    text = request.form['text']
    print(f'Got data: "{text}"')
    return redirect('/')

if __name__ == '__main__':
    # Start application on default port 5000
    app.run()