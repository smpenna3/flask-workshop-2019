from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/loop')
def loop():
    return render_template('loop.html', array=[1, 2, 3, 4, 5, 6])

@app.route('/conditional')
def conditional():
    variable = random.randint(0, 10)
    return render_template('conditional.html', variable=variable)

@app.route('/conditional', methods=['POST'])
def retry_conditional():
    return redirect('/conditional')

if __name__ == '__main__':
    # Start application on default port 5000
    app.run()