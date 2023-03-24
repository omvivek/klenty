from django.shortcuts import render
from django.http import HttpResponse
import requests
import matplotlib.pyplot as plt
import json



# Create your views here.
def home(request):
    return render(request,'index.html');

def page(request):
    return render(request,'page.html');

def search(request):
    val1= request.GET['s']
    #val2= request.GET['n']
    resp = requests.get('https://api.unsplash.com/search/photos?client_id=rAL9GKhdjQkArtdg-TMukOl3DnPc515verJrZHg6vHU&query='+val1+'&per_page=20')
    d = resp.json()
    p = json.dumps(d, sort_keys=True, indent=2)
    urls=[]
    for i in d['results']:
        i_title=i['alt_description']
        i_url=i['urls']['raw']
        urls.append(i_url)
    return render(request,'result.html',{'res':urls});