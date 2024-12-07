
document.write("Hello Javascript")
document.write("A")

var a=20;
var b=30;
document.write(a+b);

var q = true;
document.write(q);

var A = {
    Name:"Argha",
    Age:22,
    City:"Rajshahi"
}

document.write(A.Name);

var marks = 7;
if(marks>=80){
    document.write("A+");
}
else if(marks>=70 && marks<=79)
{
    document.write("A");
}
else
{
    document.write("F")
}

switch(true){
    case (marks>=80):
    document.write('A+');
    break;
    case (marks>=70 && marks<=79):
    document.write('A');
    break;
    default:
    document.write('F')
}


for(var i=0;i<10;i++)
{
    if(i==5)
    {
        continue;
    }
    if(i===7){
        break;
    }
    document.write(i+"<button>Abc</button><br>");
}

var z=0;
while(z<7)
{
    document.write(z+"<br>");
    z++;
}

function addTwoNum(x,y)
{
    document.write(x+y);
}

addTwoNum(20,30);




