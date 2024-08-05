import requests
from datetime import datetime

# Sunrise and Sunset based off the Charlotte Area
CLT_LAT = 35.2271
CLT_LONG = 80.8431

parameters = {
    "lat": CLT_LAT,
    "lng": CLT_LONG,
    "formatted": 0
}

def time_info():
    data = requests.get("https://api.sunrise-sunset.org/json", params=parameters).json()
    sunrise = float(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = float(data["results"]["sunset"].split("T")[1].split(":")[0])

    date = str(datetime.now())
    current_hour = float(date.split("-")[2].split(":")[0].split(" ")[1])
    # current_min = float(date.split("-")[2].split(":")[1])
    return {"sunrise": sunrise, "sunset": sunset, "current_hour": current_hour}

# Get current time info
time = time_info()

########################################################################################

def get_iss():
    iss_position = requests.get("http://api.open-notify.org/iss-now.json").json()
    return iss_position

# ISS Location

def iss_over_charlotte(time, CLT_LAT, CLT_LONG):
    # Fetch the current position of the ISS
    iss_position = get_iss()

    iss_lat = float(iss_position["iss_position"]["latitude"])
    iss_long = float(iss_position["iss_position"]["longitude"])

    iss_location = {"lat": iss_lat, "long": iss_long}
    charlotte_location = {"lat": CLT_LAT, "long": CLT_LONG}

    # Print current locations
    print("ISS Latitude:", iss_location["lat"])
    print("Charlotte Latitude:", charlotte_location["lat"])

    while True:
        iss_position = get_iss()
        # Check if the ISS is within 10 degrees latitude of Charlotte
        if -10 <= iss_location["lat"] - charlotte_location["lat"] <= 10:
            # Check if it's currently after sunset
            if time["current_hour"] >= time["sunset"]:
                print("ISS IS PASSING OVER CHARLOTTE GO LOOK!")
            else:
                break
        else: 
            print("ISS IS OUTSIDE OF RANGE COME BACK LATER")
            break

iss_over_charlotte(time, CLT_LAT, CLT_LONG)