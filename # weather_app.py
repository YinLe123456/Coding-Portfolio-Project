# weather_app_fixed.py
"""
Simple Weather App using wttr.in API - No API key required!
"""

import requests
import json

def get_weather(city):
    """Get weather for any city using wttr.in API"""
    try:
        # Clean the city name for URL
        city_clean = city.strip().replace(" ", "+")
        
        # Use wttr.in API - free and doesn't need API key
        url = f"https://wttr.in/{city_clean}?format=j1"
        
        print(f"🌍 Fetching weather data...")
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ Error: City '{city}' not found or network issue")
            return None
        
        # Parse the JSON response
        data = response.json()
        
        # Extract current weather data
        current = data['current_condition'][0]
        area = data['nearest_area'][0]
        
        # Prepare weather information
        weather_info = {
            "temperature": current['temp_C'],
            "humidity": current['humidity'],
            "description": current['weatherDesc'][0]['value'],
            "city": area['areaName'][0]['value'],
            "region": area['region'][0]['value'] if area['region'] else "",
            "country": area['country'][0]['value'],
            "feels_like": current['FeelsLikeC'],
            "wind_speed": current['windspeedKmph'],
            "wind_direction": current['winddir16Point'],
            "visibility": current['visibility'],
            "pressure": current['pressure'],
            "cloud_cover": current['cloudcover']
        }
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return None
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"❌ Error parsing weather data")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def display_weather(weather):
    """Display weather information in a nice format"""
    if not weather:
        return
    
    print("\n" + "="*50)
    print(f"🌤️  WEATHER REPORT")
    print("="*50)
    
    # Location info
    location = weather['city']
    if weather.get('region'):
        location += f", {weather['region']}"
    if weather.get('country'):
        location += f", {weather['country']}"
    
    print(f"📍 Location: {location}")
    print("-"*50)
    
    # Main weather info
    print(f"🌡️  Temperature: {weather['temperature']}°C")
    print(f"🤔 Feels like: {weather['feels_like']}°C")
    print(f"💧 Humidity: {weather['humidity']}%")
    print(f"☁️  Conditions: {weather['description']}")
    print(f"💨 Wind: {weather['wind_speed']} km/h {weather['wind_direction']}")
    
    # Additional info
    if 'visibility' in weather:
        print(f"👁️  Visibility: {weather['visibility']} km")
    if 'pressure' in weather:
        print(f"📊 Pressure: {weather['pressure']} mb")
    if 'cloud_cover' in weather:
        print(f"☁️  Cloud cover: {weather['cloud_cover']}%")
    
    # Weather recommendation
    print("-"*50)
    temp = float(weather['temperature'])
    
    if temp <= 0:
        print("🧊 ❄️  It's freezing! Wear heavy winter clothes!")
    elif temp < 10:
        print("🧥 It's cold! Wear a warm coat, scarf, and gloves.")
    elif temp < 20:
        print("🧥 It's cool! A light jacket would be perfect.")
    elif temp < 30:
        print("😎 Pleasant weather! T-shirt weather!")
    else:
        print("🔥 It's hot! Stay hydrated and wear light clothes!")
    
    # Wind recommendation
    wind_speed = float(weather['wind_speed'])
    if wind_speed > 30:
        print("💨 It's windy! Hold onto your hat!")

def get_weather_icon(description):
    """Get emoji icon based on weather description"""
    desc_lower = description.lower()
    
    if "sunny" in desc_lower or "clear" in desc_lower:
        return "☀️"
    elif "cloud" in desc_lower:
        return "☁️"
    elif "rain" in desc_lower or "drizzle" in desc_lower:
        return "🌧️"
    elif "storm" in desc_lower or "thunder" in desc_lower:
        return "⛈️"
    elif "snow" in desc_lower or "ice" in desc_lower or "sleet" in desc_lower:
        return "❄️"
    elif "fog" in desc_lower or "mist" in desc_lower or "haze" in desc_lower:
        return "🌫️"
    elif "wind" in desc_lower:
        return "💨"
    else:
        return "🌤️"

def main():
    """Main program with interactive menu"""
    print("="*60)
    print("🌤️  SIMPLE WEATHER APP")
    print("Get real-time weather for any city worldwide!")
    print("="*60)
    
    # Show example cities
    print("\n💡 Try these cities:")
    print("  New York, London, Tokyo, Paris, Sydney, Delhi, Dubai")
    
    while True:
        print("\n" + "-"*60)
        city = input("\nEnter city name (or 'menu' for options, 'quit' to exit): ").strip()
        
        if city.lower() in ['quit', 'exit', 'q']:
            print("\n" + "="*60)
            print("Thanks for using Weather App! Stay safe! 👋")
            print("="*60)
            break
        
        elif city.lower() == 'menu':
            print("\n📱 MENU OPTIONS:")
            print("1. Enter city name (e.g., 'London')")
            print("2. City with country (e.g., 'Paris, France')")
            print("3. Multiple words (e.g., 'New York')")
            print("4. 'quit' - Exit the app")
            continue
        
        elif not city:
            print("⚠️  Please enter a city name")
            continue
        
        # Get and display weather
        weather = get_weather(city)
        
        if weather:
            # Add icon to description
            icon = get_weather_icon(weather['description'])
            weather['description'] = f"{icon} {weather['description']}"
            
            display_weather(weather)
            
            # Offer to save or share
            save = input("\n📝 Save this report to file? (y/n): ").lower()
            if save == 'y':
                try:
                    with open(f"weather_{city.replace(' ', '_')}.txt", "w") as f:
                        f.write(f"Weather Report for {weather['city']}\n")
                        f.write("="*50 + "\n")
                        f.write(f"Temperature: {weather['temperature']}°C\n")
                        f.write(f"Feels like: {weather['feels_like']}°C\n")
                        f.write(f"Humidity: {weather['humidity']}%\n")
                        f.write(f"Conditions: {weather['description']}\n")
                        f.write(f"Wind: {weather['wind_speed']} km/h {weather['wind_direction']}\n")
                    print(f"✅ Report saved as 'weather_{city.replace(' ', '_')}.txt'")
                except:
                    print("❌ Could not save file")
        else:
            print(f"😔 Could not get weather for '{city}'")
            print("💡 Try: Check spelling, use English city names, or try a nearby city")

if __name__ == "__main__":
    main()