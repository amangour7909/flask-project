from flask import Flask
app = Flask(__name__)

# set route where it will run 
# @app.route('/aman')
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    #run on localhost or on local machine and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True) 