var array = ["Banana", "Apples", "Oranges", "Blueberries"];
array.splice(0,1);
alert(array);
array.sort();
alert(array);
array.push("kiwi");
alert(array);
array.splice(0,1);
alert(array);
array.reverse();
alert(array);

//Exercise two

var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(array2[1][1]);