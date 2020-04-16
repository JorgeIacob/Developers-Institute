//Exercise 1

var me = ["my","favourite","color","is","blue"];
console.log(me.join(' ')) //output: my favourite color is blue

//Exercise 2 Mixup

let str1 = "mix";
let str2 = "pod";

let myData = str1+str2;
[str1,str2] = [str2,str1];

console.log(str1,str2); //pod mix

//calculator

let first = Number(prompt('Enter first number '));
let second = Number(prompt('Enter second number '));
let sum = first + second;
alert(sum);
let substract = first - second;
let multiply = first * second;
let div = first /second;
alert("The difference of the numbers is "+ substract);
alert("The multiplication of the numbers is " + multiply);
alert("The division of the numbers is "+ div);
 



