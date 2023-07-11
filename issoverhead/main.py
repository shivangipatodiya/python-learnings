import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude
MY_EMAIL = "myemail@gmail.com"
MY_PASSWORD = "mypassword"


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 >= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 >= iss_longitude >= MY_LONG + 5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT + 5 or MY_LAT - 5,
        "lng": MY_LONG + 5 or MY_LONG - 5,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now < sunrise or time_now > sunset:
        return True

# If the ISS is close to my current position
# ,and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    time.sleep(60)
    if iss_overhead() and is_dark():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look up\n\nThe ISS is above you in the sky."
        )
