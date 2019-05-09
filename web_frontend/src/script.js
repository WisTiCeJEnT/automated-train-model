var btn0 = document.getElementById("btn0")
var btn1 = document.getElementById("btn1")
var btn2 = document.getElementById("btn2")
var btn3 = document.getElementById("btn3")
var addBtn = document.getElementById("add")
var todos = []

btn0.addEventListener('click', function () {
    console.log("Go to 1")
    var xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/movetrain";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
        }
    };
    var data = JSON.stringify({ "destination": "1"});
    xhr.send(data);

})
btn1.addEventListener('click', function () {
    console.log("Go to 2")
    var xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/movetrain";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
        }
    };
    var data = JSON.stringify({ "destination": "2"});
    xhr.send(data);

})
btn2.addEventListener('click', function () {
    console.log("Go to 3")
    var xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/movetrain";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
        }
    };
    var data = JSON.stringify({ "destination": "3"});
    xhr.send(data);

})
btn3.addEventListener('click', function () {
    console.log("Go to 4")
    var xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/movetrain";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
        }
    };
    var data = JSON.stringify({ "destination": "4"});
    xhr.send(data);

})
