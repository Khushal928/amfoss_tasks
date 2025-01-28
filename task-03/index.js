function funct(inputbutton) {
    if (inputbutton === 'w') {
        var sound = new Audio('sounds/crash.mp3');
        sound.play();
    }
    if (inputbutton === 'a') {
        var sound = new Audio('sounds/kick-bass.mp3');
        sound.play();
    }
    if (inputbutton === 's') {
        var sound = new Audio('sounds/snare.mp3');
        sound.play();
    }
    if (inputbutton === 'd') {
        var sound = new Audio('sounds/tom-1.mp3');
        sound.play();
    }
    if (inputbutton === 'j') {
        var sound = new Audio('sounds/tom-2.mp3');
        sound.play();
    }
    if (inputbutton === 'k') {
        var sound = new Audio('sounds/tom-3.mp3');
        sound.play();
    }
    if (inputbutton === 'l') {
        var sound = new Audio('sounds/tom-4.mp3');
        sound.play();
    }
}




document.getElementById('w').onclick = function () { funct('w'); };
document.getElementById('a').onclick = function () { funct('a'); };
document.getElementById('s').onclick = function () { funct('s'); };
document.getElementById('d').onclick = function () { funct('d'); };
document.getElementById('j').onclick = function () { funct('j'); };
document.getElementById('k').onclick = function () { funct('k'); };
document.getElementById('l').onclick = function () { funct('l'); };
