from django.shortcuts import render
import requests
import datetime 
from datetime import date




def index(request):     

    ## api with zip code for city locations    
    api_keywest = 'https://api.apixu.com/v1/current.json?key=21ef922400764f56a2c150914182906&q=33040'
    api_baycity = 'https://api.apixu.com/v1/current.json?key=21ef922400764f56a2c150914182906&q=48708'
    api_scottsdale = 'https://api.apixu.com/v1/current.json?key=21ef922400764f56a2c150914182906&q=85257'

    keywest = requests.get(api_keywest).json()
    kw_temp_f = keywest['current']['temp_f']
    kw_conditions = keywest['current']['condition']['text']
    kw_icon_code = keywest['current']['condition']['icon']
    kw_icon = 'http:' + kw_icon_code    
    kw_feelslike_f = keywest['current']['feelslike_f']
    kw_humidity = keywest['current']['humidity']
    kw_city = keywest['location']['name']
    kw_state = keywest['location']['region']
    kw_update = keywest['current']['last_updated']


    baycity = requests.get(api_baycity).json()
    bc_temp_f = baycity['current']['temp_f']
    bc_conditions = baycity['current']['condition']['text']
    bc_icon_code = baycity['current']['condition']['icon']
    bc_icon = 'http:' + bc_icon_code    
    bc_feelslike_f = baycity['current']['feelslike_f']
    bc_humidity = baycity['current']['humidity']
    bc_city = baycity['location']['name']
    bc_state = baycity['location']['region']
   
    scottsdale = requests.get(api_scottsdale).json()
    az_temp_f = scottsdale['current']['temp_f']
    az_conditions = scottsdale['current']['condition']['text']
    az_icon_code = scottsdale['current']['condition']['icon']
    az_icon = 'http:' + az_icon_code    
    az_feelslike_f = scottsdale['current']['feelslike_f']
    az_humidity = scottsdale['current']['humidity']
    az_city = scottsdale['location']['name']
    az_state = scottsdale['location']['region']
        
    context = {
        'kw_temp_f' : kw_temp_f,
        'kw_conditions' : kw_conditions,
        'kw_feelslike_f' : kw_feelslike_f,
        'kw_humidity' : kw_humidity,
        'kw_city' : kw_city,
        'kw_state' : kw_state,             
        'kw_humidity' : kw_humidity,
        'kw_icon' : kw_icon,
        'kw_update' : kw_update,

        'bc_temp_f' : bc_temp_f,
        'bc_conditions' : bc_conditions,
        'bc_feelslike_f' : bc_feelslike_f,
        'bc_humidity' : bc_humidity,
        'bc_city' : bc_city,
        'bc_state' : bc_state,             
        'bc_humidity' : bc_humidity,
        'bc_icon' : bc_icon,        

        'az_temp_f' : az_temp_f,
        'az_conditions' : az_conditions,
        'az_feelslike_f' : az_feelslike_f,
        'az_humidity' : az_humidity,
        'az_city' : az_city,
        'az_state' : az_state,             
        'az_humidity' : az_humidity,
        'az_icon' : az_icon,

        # 'days' : number_of_days,
        # 'weeks' : weeks,
        # 'percent' : percent,
    }


    return render(request, 'keywest/index.html', context)