console.log("hello console")

function myFun(){
    console.log("I am function")
}

myFun();

function sumOfTwoNums(a,b){
    let c = a+b;
    console.log(c);
}

sumOfTwoNums(10,70);

function subOfTwoNums(a,b){
    return a-b;
}

let subt = subOfTwoNums(1,70);

console.log(subt*3);

let sum = sumOfTwoNums(100,89);
console.log(sum*67)

function greet(name)
{
    console.log(`Hello ${name}`);
}
greet("Argha");

x = function(a,b)
{
    return a*b;
}

console.log(x(6,8));

const mul = (s,t) => s*t;

console.log(mul(6,7));

const appConfig = (function(){
    const apikey = "123456";
    return(apikey);
})();

console.log(appConfig);

function normalTest(){
    console.log("Hello 1");
    console.log("Hello 2");
    console.log("Hello 3");
    console.log("Hello 4");
}
normalTest();

function* generatorFunc(){
    yield "First Value";
    yield "Second Value";
    yield "Third value";
    yield "Forth Value";
}

const gen = generatorFunc();
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());

function factorial(n)
{
    if (n===1)
    {
        return 1;
    }
    return n*factorial(n-1);
}

console.log(factorial(6));