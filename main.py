import requests
from datetime import datetime
today=datetime.now()
APP_ID="fb3e7551"
API_KEY="4852a5fb86cd93784f5fd44a3cc384fd"
NUTRITIONIX_URL="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL="https://api.sheety.co/42cb5bde418929433e856c9d98b0c704/myWorkouts/workouts"
SHEETY_AUTH="ezsrxdtcfybhzdrxfcghv"
headers={
	"x-app-id":APP_ID,
	"x-app-key":API_KEY,
	"x-remote-user-id":"akshay"
}
query=input("What kind of workout did you do today? ")
params={
	"query":query,
	"gender":"male",
	"weight_kg":73,
	"height_cm":180,
	"age":21
}
headers_sheety={
	"Authorization":"Bearer ezsrxdtcfybhzdrxfcghv"
}
response=requests.post(url=NUTRITIONIX_URL,headers=headers,json=params)
work=response.json()
for i in work.get('exercises'):
	workout={
		"Content-Type": "application/json",
		"workout":{
			"date":today.strftime("%d-%m-%Y"),
			"time":today.strftime("%H:%M"),
			"exercise":i.get('name').title(),
			"calories":i.get('nf_calories'),
			"duration":i['duration_min'],
				}
	}
	sheety_response=requests.post(url=SHEETY_URL,json=workout,headers=headers_sheety)
	print(sheety_response.text)
	

