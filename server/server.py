from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

my_map = [0,2,4,6]
horn_status = '0'
dest = 1
source = 0
train_position = "0000"
move = 0
last_move = 1
signal = [False, False, False]

def check_train_position():
    return train_position.find('1')+1

def light_signal():
    global signal
    if(check_train_position() == dest):
        print("all red")
        signal = [False, False, False] 
    elif(check_train_position() < dest and check_train_position() != 0):#forward
        signal = [False, False, False] 
        for i in range(check_train_position(),dest):
            signal[i-1] = True
    elif(check_train_position() > dest):#backward
        signal = [False, False, False] 
        for i in range(check_train_position()-1,dest-1,-1):
            signal[i-1] = True
    return signal

@app.route('/')
def root():
    return "Working"

@app.route('/horn', methods = ['GET', 'POST'])
def horn():
    data = request.get_json()
    global horn_status
    horn_status = str(data["horn"])
    print(horn_status)
    return jsonify({
        "status": "got horn status",
        "train_position": check_train_position(),
        "destination": dest
        })

@app.route('/movetrain', methods = ['GET', 'POST'])
def move_train():
    data = request.get_json()
    print(data["destination"])
    if(int(data["destination"]) != check_train_position):
        global dest
        dest = int(data["destination"])
        global source
        source = check_train_position()
    return jsonify({
        "status": "got destination", 
        "traffic_signal": light_signal(),
        "train_position": check_train_position(),
        "destination": dest
        })

@app.route('/controller', methods = ['GET'])
def trainController():
    global last_move
    c_pos = 0
    if(check_train_position()!=0):
        last_move = my_map[check_train_position()-1]
        c_pos = last_move
    else:
        if(move == 1):
            c_pos = last_move+1
        else:
            c_pos = last_move-1
    return jsonify({
        "traffic_signal": light_signal(),
        "current_position": c_pos,
        "jui_nine": (dest==check_train_position())
    })

@app.route('/station', methods = ['GET', 'POST'])
def station():
    data = request.get_json()
    global train_position
    train_position = data["train_position"]
    print("train_position(from station):",train_position)
    return jsonify({
        "status": "got train position", 
        "traffic_signal": light_signal(),
        #"train_position": check_train_position(),
        #"destination": dest
        })

@app.route('/train', methods = ['GET'])
def train():
    global move
    print("train position", check_train_position())
    if(check_train_position() == dest):
        command = "0"+horn_status+str(check_train_position())+"0"
        print("command to train", command)
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
