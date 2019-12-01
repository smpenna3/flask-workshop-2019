from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return 'Index page'

@app.route('/test')
def test():
    return 'Test page'

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 
    # 404 status explicitly
    return 'ERROR', 404

if __name__ == '__main__':
    # Start application on default port 5000
    app.run()