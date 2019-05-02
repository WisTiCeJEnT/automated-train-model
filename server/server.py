from flask import Flask, request, jsonify

app = Flask(__name__)

horn_status = '0'
dest = 1
source = 0
train_position = "0000"
move = 0
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
