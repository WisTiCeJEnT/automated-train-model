from flask import Flask

i = 0

app = Flask(__name__)

@app.route('/')
def root():
    return "Working"

@app.route('/i', methods = ['GET', 'POST'])
def iplusplus():
    global i
    i=(i+1)%2
    return str(i)

@app.route('/jui', methods = ['GET', 'POST'])
def jui():
    return str(i)

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
