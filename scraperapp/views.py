import requests
import bs4 
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse('Hello, World')
    #return render(request,'home.html')
    page=requests.get('https://fabpedigree.com/james/mathmen.htm')
    
    soup=bs4.BeautifulSoup(page.content,'html.parser')
    li=soup.findAll('li')
    name=[]
    for each in li:
        var=each.find('a')
        name.append(var.get_text())
        d={'names':name}

    return render(request,'home.html',d)
def home1(request):
    return HttpResponse('Hello, bootcamp')


