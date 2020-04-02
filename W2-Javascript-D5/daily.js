/*
Jorge Iacobsohn 2/4/20
X Numbers of beer on the wall

Algorithm:
1. There are X beers on the wall
2. 1 to X beers are falling from the wall
3. Each time number of beers are falling from the wall from the amount of current number of beers on the wall
4. For the first falling beer write "pass it" since it is one falling beer
5. For the first time "bottles of beer on the wall" is displayed once else twice
6. For the rest of falling beers write "pass them around" since more than 1 beer are falling from the wall
7. For the last iteration all beers the are on the wall are falling down
*/

let numOfBeersOnTheWall = prompt("How Many Beers on the wall?") ;
//1 to X beers are falling from the wall
for( let fallDownBeerIndex = 0 ; fallDownBeerIndex < numOfBeersOnTheWall ; fallDownBeerIndex++ )
{
    if( (fallDownBeerIndex) == 0)
    {
        let newNumOfBeers = numOfBeersOnTheWall - fallDownBeerIndex  ;
        console.log(numOfBeersOnTheWall + " bottles of beer on the wall\n") ;
        //For the first time "bottles of beer on the wall" is displayed once
        console.log(numOfBeersOnTheWall + " bottles of beer\n") ;
        //For the first falling beer write "pass it" since it is one falling beer
        console.log("Take "+(fallDownBeerIndex+1)+" down, pass it around\n") ;

    }
    else
    {
        //Each time number of beers are falling from the wall from the amount of current number of beers on the wall
        let newNumOfBeers = numOfBeersOnTheWall - fallDownBeerIndex;
        console.log(newNumOfBeers  + " bottles of beer on the wall\n") ;
        console.log(newNumOfBeers  + " bottles of beer on the wall\n") ;
        console.log(newNumOfBeers  + " bottles of beer\n") ;

         //For the last iteration all beers the are on the wall are falling down
         if( numOfBeersOnTheWall-fallDownBeerIndex < fallDownBeerIndex)
         {
            //For the rest of falling beers write "pass them around" since more than 1 beer are falling from the wall
            console.log("Take "+(newNumOfBeers)+" down, pass them around and no more beers on the wall\n") ;
         }
         else
         {
            //For the rest of falling beers write "pass them around" since more than 1 beer are falling from the wall
            console.log("Take "+(fallDownBeerIndex+1)+" down, pass them around\n") ;
         }
        //This is how I keep the current number of beers on the wall
        numOfBeersOnTheWall-= fallDownBeerIndex;
    }
} 