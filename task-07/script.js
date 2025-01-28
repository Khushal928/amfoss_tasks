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