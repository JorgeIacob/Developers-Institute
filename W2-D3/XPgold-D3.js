//EX 1

let family = {

father: "Avi",
mother: "Sarah"};

for (let x in family) {

	console.log(x) //father mother
	console.log(family[x]) //Avi Sarah
}

//EX 2

var building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
}

console.log(building.number_levels) 		//Display the number of levels in the building
let display1 = building.number_of_apt_by_level[1];// Display how many apartments are on level 1 and 3. Do the sum of these apartments
let display2 = building.number_of_apt_by_level[3];
let sum = display2+display1;
console.log(display1,display2,sum)
		
var tentantTwo = building.name_of_tenants[1];	// Display the name of the second tenant and the number of rooms he has in his apartment
var tentantTwo_rooms = building.number_of_rooms_and_rent[tentantTwo][0];
console.log (tentantTwo,tentantTwo_rooms);


let sumTwo = building.number_of_rooms_and_rent.Sarah[1] + building.number_of_rooms_and_rent.David[1] ;	
console.log ("The sum of the rent of Sarah and David is "+sumTwo) // sum of the rent of Sarah and David:2010

if (sumTwo>building.number_of_rooms_and_rent.Dan[1]) {
	let newRent = prompt("You need to increase the rent of Dan. Put the value here")// Check if the rent of Sarah plus the rent David is bigger than the rent of Dan.
	building.number_of_rooms_and_rent.Dan[1] = newRent ;
	console.log("The new rent of Dan is " + newRent)
}
// If it is than inform the owner that he has to inscrease the rent of Dan. And change the rent of Dan accordingly inside the object.

//EX 3 Create two objects, each one should hold a person details. Here are the details: fullName, mass, height and compare

let personOne = {
	fullName: "Nicola Pesin",
	mass: 78,	//kg
	height: 1.70,	//cm
}

personOne.bmi=personOne.mass/(personOne.height*personOne.height)

let personTwo = {
	fullName: "Amitai Ziv",
	mass: 85,	//kg
	height: 1.78,	//cm
}

personTwo.bmi=personTwo.mass/(personTwo.height*personTwo.height)

function comparison (){

let bmi1 = personOne.bmi;
let bmi2 = personTwo.bmi;

if (bmi1>bmi2){
	console.log(personOne.fullName + " has the biggest BMI")
}else{
	console.log(personTwo.fullName + "has the biggest BMI")
}

}
comparison()

