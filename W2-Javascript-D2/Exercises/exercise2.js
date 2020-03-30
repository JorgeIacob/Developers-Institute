var a = 2 + 2;
a = prompt ("Here a sum 2+2, Write a number from 2 to 5")*1; //Open the window for put values, *1 transforms string value  to number

switch (a) {  //in case of the value is...
  case 3:
    alert( 'Too small' );//expected output: "Too small."
    break;
  case 4:
    alert( 'Exactly!' );//expected output: "Exactly!"
    break;
  case 5:
    alert( 'Too large' );//expected output: "Too large."
    break;
  default:
    alert( "I don't know such values" );//expected output: "I don't know such values."
}