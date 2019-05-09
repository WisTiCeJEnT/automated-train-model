//alert('Hello :)')
console.log("Hello It's me ... ")

function printTest() {
    console.log('Test')
}
function delay() {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            printTest()
            resolve()
        }, 1000)

    })
}
printTest()
delay().then(function() {
    console.log("inside delay().then()")

})
console.log("GG")
/*
var x = 1
var y = "y"
console.log(x+y)

var iden = {
    name: "Nine"
}
var list = [1,3,5,6]
iden.age = 20
console.log(iden)
console.log(list)
console.log(iden.name)
console.log(iden.name.name)
console.log(iden.name.name.name)
*/