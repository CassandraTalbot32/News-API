from django.shortcuts import render

import requests

API_KEY = '09cdaa56db4d4a6cb93bf1bedde04bd7'



def home(request):
 	url = f'https://newsapi.org/v2/top-headlines?country=gb&apikey={API_KEY}'
 	response = requests.get(url)
 	data = response.json()
 	

 	articles = data['articles']

 	context = {
 		'articles' : articles
 	}

 	return render (request, 'home.html', context)