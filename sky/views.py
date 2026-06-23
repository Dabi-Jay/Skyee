from django.shortcuts import render
import requests
import datetime

def home(request):
    #  Default values 
    city = 'Lagos'
    if request.method == 'POST' and request.POST.get('city'):
        city = request.POST['city'].strip()

    WEATHER_API_KEY = "5e9328edab73d3fe4d7e851902746fbf"

    #  Fetching Weather Data from OpenWeather
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(weather_url, params=params, timeout=5)
        
        if response.status_code == 200:
            json_data = response.json()
            
            # Looking up the main weather condition group (e.g Clouds , Rain, Clear)
            weather_main = json_data['weather'][0]['main'].lower()
            
            if 'cloud' in weather_main:
                bg_image = 'images/clouds.jpg'
            elif 'rain' in weather_main or 'drizzle' in weather_main or 'thunderstorm' in weather_main:
                bg_image = 'images/rain.jpg'
            else:
                bg_image = 'images/clear.jpg' 

            data = {
                "city": city.capitalize(),
                "country": json_data['sys']['country'],
                "temp": f"{round(json_data['main']['temp'], 1)}",
                "description": json_data['weather'][0]['description'].capitalize(),
                "icon": json_data['weather'][0]['icon'],
                "day": datetime.date.today().strftime("%A, %B %d"),
                "bg_image": bg_image  
            }
            exception_occurred = False
        else:
            raise ValueError("City not found")

    except Exception:
        exception_occurred = True
        data = {
            "city": "Nill",
            "country": "",
            "temp": "-",
            "description": "No man's land",
            "icon": "03d",
            "day": datetime.date.today().strftime("%A, %B %d"),
            "bg_image": "images/clear.jpg" 
        }

    context = {
        'data': data,
        'exception_occurred': exception_occurred
    }

    return render(request, 'index.html', context)