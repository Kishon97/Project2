import requests



test = ['''!!!INTRUDER DETECTED!!!

PLEASE LOGIN TO YOUR WEBSERVER TO VIEW IT
http://0.0.0.0/login''']



for text in test:

    base_url= 'put ur chat token id'.format(text)

    requests.get(base_url)
