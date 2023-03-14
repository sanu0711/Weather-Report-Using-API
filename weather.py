import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

API_Key="63ecba921803bb837ef5995110d62567"
Account_SID="AC0df3417cc475bf4b87f12fb7f4041b0e"
Auth_Token="85ce2750a6748e4455306f4173b96a85"
Twilio_phone_number="+12676098437"

weather_param={
    "lat":26.261700,
    "lon":81.544998,
    "appid":API_Key,
    }
req=requests.get("https://api.openweathermap.org/data/2.5/weather",params=weather_param)
req.raise_for_status()
weather_data=req.json()
print(weather_data["weather"][0])
print(weather_data["main"])
client = Client(Account_SID,Auth_Token)
message = client.messages.create(
                            body=f'Today Weather Report :\n\n{weather_data["weather"][0]}\n\n{weather_data["main"]}',
                            from_=Twilio_phone_number,
                            to='+917985459061'
                        )
print(message.status)
