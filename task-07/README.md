search button, city display, temp, description is given an id 
<br>
```html
<div id="city-display"></div>
<div id="temperature"></div>
<div id="description"></div>
```


if search-button is triggered, then city stores the value in place holder and getWeather() will be called with city as parameter and error message is displayed if no city is entered
<br>
```javascript
document.getElementById("serch-button").addEventListener("click", 
    function () 
    {
        const city = document.getElementById("city").value;

        if (city) 
            {
                getWeatherData(city);
            } 
        else 
            {
                alert("Please enter a city name.");
            }
    }
);
```


if response is not ok, an error will be displayed else, "parsed data" will be stored in "data" and since each division is given an id, each info is placed in that place. for example, data.name is placed at "city-display". and since margin-top and margin-bottom is given and body is center-aligned, when all the content is displayed, they get rearranged!
<br>
```javascript
function getWeatherData(city) {
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=db8c70f6188598bd408cb973802b361c&units=metric`)
    .then
    (response => {
      if (!response.ok) throw new Error("City not found");
      return response.json();
    })
    .then
    (data => {
      document.getElementById("city-display").textContent = data.name;
      document.getElementById("temperature").textContent = `${data.main.temp}°C`;
      document.getElementById("description").textContent = data.weather[0].description;
    })
    .catch(error => alert(error.message));
}
```
<br>
this task introduced me new tools like addEventListener