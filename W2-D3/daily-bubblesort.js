

function bubblesort (array){
    //go over all the elements to n-i
    for(i=0;i<(array.length);i++)
    //go over all the elements to n-j
    for(j=0;j<(array.length);j++){
 
        //comparise 
        if(array[j]<array[j+1]){
             //saving the high number in the auxiliar
             aux=array[j];
             //saving the minor number
             array[j]=array[j+1];
             //asigning the auxiliar in the correspondent place
             array[j+1]=aux;
 
        }
 
    }
 
    return array
}

//array to order
var arrtoOrder=[5,0,9,1,7,4,2,6,3,8];
arrtoOrder=bubblesort(arrtoOrder);
alert(arrtoOrder)


let newarr = arrtoOrder.toString();
console.log("This is a string " + newarr);
console.log(arrtoOrder.join())
console.log(arrtoOrder.join("+"))
console.log(arrtoOrder.join(" "))