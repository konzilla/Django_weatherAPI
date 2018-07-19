import requests
import os

os.system('clear')

api_address = 'http://api.apixu.com/v1/current.json?key=21ef922400764f56a2c150914182906&q=33040'
api_address1 = 'http://api.apixu.com/v1/current.json?key=21ef922400764f56a2c150914182906&q=48708'

data = requests.get(api_address).json()
temp_f = data['current']['temp_f']
current = data['current']['condition']['text']
feelslike_f = data['current']['feelslike_f']
localtime = data['location']['localtime']
humidity = data['current']['humidity']
city = data['location']['name']
state = data['location']['region']

#f_temp = 1.8 * (formatted_data - 273) + 32
print('Location: ' + city +', ' + state)
print('Current Temp: ' + str(temp_f))
print('Feels Like: ' + str(feelslike_f))
print('Humidity: '  + str(humidity))
print('Current Conditions: ' + current)
print('Local Time: ' + localtime)
print()

data1= requests.get(api_address1).json()
temp_f1 = data1['current']['temp_f']
current1 = data1['current']['condition']['text']
feelslike_f1 = data1['current']['feelslike_f']
localtime1 = data1['location']['localtime']
humidity1 = data1['current']['humidity']
city1 = data1['location']['name']
state1 = data1['location']['region']
#f_temp = 1.8 * (formatted_data - 273) + 32
print('Location: ' + city1 +', ' + state1)
print('Current Temp: ' + str(temp_f1))
print('Feels Like: ' + str(feelslike_f1))
print('Humidity: '  + str(humidity1))
print('Current Conditions: ' + current1)
print('Local Time: ' + localtime1)