import requests

API_KEY = "0844c8be83c1e84a5df0e82ea78be6c7"


def get_weather_data(location, unit="metric"):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "units": unit,
        "appid": API_KEY,
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Failed to fetch weather data. Please check the location or API key.")
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print(f"Weather Conditions: {weather_data['weather'][0]['description']}")
    else:
        print("No weather data to display.")

def main():
    print("Welcome to the Weather Forecast Application!")
    location = input("Enter a city or location: ")
    unit = input("Choose temperature unit (Celsius or Fahrenheit): ").lower()
    
    if unit not in ["celsius", "fahrenheit"]:
        print("Invalid temperature unit. Defaulting to Celsius.")
        unit = "celsius"
    
    weather_data = get_weather_data(location, unit)
    display_weather(weather_data)

if __name__ == "__main__":
    main()