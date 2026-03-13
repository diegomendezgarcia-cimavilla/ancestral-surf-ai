import requests

def get_weather(city="Vigo"):

    try:

        url=f"https://wttr.in/{city}?format=j1"

        data=requests.get(url).json()

        temp=data["current_condition"][0]["temp_C"]

        return f"{temp}°C"

    except:

        return "clima no disponible"
