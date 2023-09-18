import requests, pytz
from datetime import datetime

def get_iss_location():
    iss_url = "https://api.wheretheiss.at/v1/satellites/25544"

    response = requests.get(iss_url)
    response_data = response.json()

    latitude = response_data.get("latitude")
    longitude = response_data.get("longitude")

    return latitude, longitude

def get_iss_timezone(lat, long):
    coordinates_url = f"https://api.wheretheiss.at/v1/coordinates/{lat},{long}"
    response = requests.get(coordinates_url)
    response_data = response.json()
    timezone = response_data.get("timezone_id")
    return timezone

def is_daytime(timezone_str):
    current_time = datetime.now(pytz.timezone(timezone_str))
    #print(current_time)
    if 6 <= current_time.hour < 18:
        return True
    return False


lat, long = get_iss_location()
timezone_str = get_iss_timezone(lat, long)

if is_daytime(timezone_str):
    light = "Bright"
else:
    light = "Dark"

print("The Current Latitude and Longitude of the International Space Station is:")
print("(" + str(lat) + ", " + str(long) + ")")
print("This is within the timezone:")
print(timezone_str)
#print(light)
print(f"Which means it is {light} out")