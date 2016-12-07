from flask import Flask
import pytesla_tesla
import teslajson
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello')
def hello2():
    return 'Hello World'

pytesla_tesla.main()

"""
if __name__ == "__main__":
    app.run(host='0.0.0.0')
#
"""
