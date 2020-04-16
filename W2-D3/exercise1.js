//exercise 1

let user = {

	username : "Beiguele",
	password : "pretzel78",
};

var database = [user]


let newsfeed = {
	user1:{
		username : "Jorge",
		timeline : "12/3/76"
	},
	user2:{
		username : "Revital",
		timeline : "12/3/80"
	},
	user3:{
		username : "Yaniv",
		timeline : "12/2/80"
	}
} ;

console.log("Database first item username:"+database[0].username) ;
console.log("User1 name from newsfeed array of objects (collection)"+newsfeed["user1"].username) ;

console.log("user1 name:"+newsfeed.user1.username) ;
console.log("user1 timeline:"+newsfeed.user1.timeline) ;

console.log("user2 name:"+newsfeed.user2.username) ;
console.log("user2 timeline:"+newsfeed.user2.timeline) ;

console.log("user3 name:"+newsfeed.user3.username) ;
console.log("user3 timeline:"+newsfeed.user3.timeline) ;

//exercise 2


for (i=0; i<=15; i++) {
   if (i % 2 === 0) {
                console.log(i + " is even");   
        }
        else {
                console.log(i + " is odd");
        }
}

//exercise 3

let names = ["john", "sarah", 23, "Rudolf", 34]

for (i = 0; i < names.length; i++) {
    if (typeof names[i] == 'string') {
        if (names[i][0] != names[i][0].toUpperCase()) {
            console.log(names[i][0].toUpperCase() + names[i].slice(1))
        }
    }
}