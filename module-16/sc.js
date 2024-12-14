document.write("hello")

console.log("hello")

var name = "Argha";

let age = 22;

const pi = 3.1416;

document.write(name,age,pi,"<br/>")

function testFun(){
    var firstName = "Argha";
    if(true)
    {
        var firstName = "Anirban";
        console.log(firstName);
    }
    console.log(firstName);
}


function testFun(){
    let firstName = "Argha";
    if(true)
    {
        let firstName = "Anirban";
        console.log(firstName);
    }
    console.log(firstName);
}

testFun();

let Age=20;
let Name="Arg";
let isAdult=true;
let empty=null;
let notAssigned;

let object = {N:"A",a:20,ad:"Raj"};

let array = ["red,green,blue"];

document.write(typeof(Age));
document.write(typeof(array));
document.write(typeof empty);