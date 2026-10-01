function getNums()
{
    const num1 = Number(document.getElementById("num1").value); 
    const num2 = Number(document.getElementById("num2").value);
    return {num1,num2};
}

function multiply()
{
    const {num1,num2} = getNums();
    const res = num1*num2;
    document.getElementById("res").innerText = `${res}`;
}

function divide()
{
    const {num1,num2} = getNums();
    if(num2 == 0) 
    {
        alert("Mẫu số không thể = 0!");
    }
    const res = num1/num2;
    document.getElementById("res").innerText = `${res}`;
}

