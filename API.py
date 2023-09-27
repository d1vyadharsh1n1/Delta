from flask import Flask

app = Flask(__name__)

# Initialize a counter
endpoint_count = 0

@app.route('/index')
def hello_world():
    global endpoint_count
    endpoint_count += 1
    return f'Hello, World! This endpoint has been called {endpoint_count} times.'

if __name__ == '__main__':
    app.run()
