
        
    function libIt() {
    var story = document.getElementById("story");
    var person = document.getElementById("person").value;
    var adjective = document.getElementById("adjective").value;
    var noun = document.getElementById("noun").value;
    story.innerHTML = person + " is a " + adjective + " " + noun + "... who would have imagined it!";
  }

  var libButton = document.getElementById('lib-button');
  libButton.addEventListener('click', libIt); 
    