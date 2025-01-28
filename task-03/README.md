I have started this task by linking javascript and css files with html file
```html
<script src="index.js"></script>
```
at the end of body to link index.js with my html file
```html
<link rel="stylesheet" href="styles.css">
```
to link styles.css with html file, I have given an id to each button so that when it is clicked,using onclick, function _funct_ is triggered with parameter as the letter
<br>
```javascript
document.getElementById(ID).onclick = function () { funct(LETTER THAT IS CLICKED); }
```
when that function is triggered, a unique sound stored in sounds folder is played
<br>
```javascript
if (inputbutton ===  LETTER THAT IS CLICKED) {
        var sound = new Audio('sounds/crash.mp3');
        sound.play();
    }
```
<br>


A class is also given for each button so each button can be decorated 
```css
.j {
  background-color: chocolate;
}
```
Whole part is aligned in center cause body is center-aligned and heading drum kit is highlighted 
<br>


finally whole font in webpage is changed 
<br>
```html
  <link href="https://fonts.googleapis.com/css2?family=Playwrite+AU+SA&display=swap" rel="stylesheet">
```


This task is a good introduction with web devolopment for me.its quite fun to create this webpage

