from flask import Flask, request, jsonify

app = Flask(__name__)

horn_status = '0'
dest = 1
source = 0
train_position = "0000"
move = 0

def check_train_position():
    return train_position.find('1')+1

@app.route('/')
def root():
    return "Working"

@app.route('/horn', methods = ['GET', 'POST'])
def horn():
    data = request.get_json()
    global horn_status
    horn_status = str(data["horn"])
    print(horn_status)
    return jsonify({"status": "got horn status"})

@app.route('/movetrain', methods = ['GET', 'POST'])
def move_train():
    data = request.get_json()
    if(int(data["destination"]) != check_train_position):
        global dest
        dest = int(data["destination"])
        global source
        source = check_train_position()
    return jsonify({"status": "got destination"})

@app.route('/station', methods = ['GET', 'POST'])
def station():
    data = request.get_json()
    global train_position
    train_position = data["train_position"]
    print(train_position)
    return jsonify({"status": "got train position"})

@app.route('/train', methods = ['GET'])
def train():
    global move
    print("train position", check_train_position())
    if(check_train_position() == dest):
        command = "0"+horn_status+"00"
        print("train is standby")
        return command
    elif(check_train_position() == 0):
        print("train is runnning")
    elif(check_train_position() < dest):#forward
        move = 1
    else:
        move = 2
    command = str(move)+horn_status+str(source)+str(dest)
    print("command to train", command)
    return command

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
