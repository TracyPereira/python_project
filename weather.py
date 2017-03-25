#! python
import requests
#Requests allow you to send HTTP/1.1 requests.
#You can add headers, form data, multipart files, and parameters with simple Python dictionaries, and access the response data in the same way.
def get_weather_forecast():
    # Connecting to the weather api
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Mumbai,fl&units=imperial&appid=f641b59e03463c808393605f493b1f93'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # Parsing JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # Creating our forecast string
    forecast = 'The Circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'

    return forecast
