// index page text slide
var textArray = ['Digital Inclusion Program',
        'ICT Training', 'Entreprenuership Training'],
        curIndex = 0;
        imgDuration = 4000;

    function slideShow() {
        document.getElementById('text').innerHTML = textArray[curIndex];
        curIndex++;
        if (curIndex == textArray.length) { curIndex = 0; }
        setTimeout("slideShow()", imgDuration);
    }
    slideShow();


//responsive nav bar 
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}


