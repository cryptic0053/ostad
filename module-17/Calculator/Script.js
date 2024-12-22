    var num1 = document.getElementById("num1");
    var num2 = document.getElementById("num2");
    var result = document.getElementById("result");

    document.getElementsByTagName("button")[0].onclick = function(){
        document.getElementsByTagName("button")[5].onclick = function(){
            result.innerHTML = parseFloat(num1.value) + parseFloat(num2.value);
    }   
    }

    document.getElementsByTagName("button")[1].onclick = function(){
        document.getElementsByTagName("button")[5].onclick = function(){
            result.innerHTML = parseFloat(num1.value) - parseFloat(num2.value);
    }   
    }

    document.getElementsByTagName("button")[2].onclick = function(){   
        document.getElementsByTagName("button")[5].onclick = function(){
            result.innerHTML = parseFloat(num1.value) * parseFloat(num2.value);
    }   
    }

    document.getElementsByTagName("button")[3].onclick = function(){
        document.getElementsByTagName("button")[5].onclick = function(){
            result.innerHTML = parseFloat(num1.value) / parseFloat(num2.value);
    }   
    }

    document.getElementsByTagName("button")[4].onclick = function(){
        document.getElementsByTagName("button")[5].onclick = function(){
            result.innerHTML = parseFloat(num1.value) % parseFloat(num2.value);
    }   
    }