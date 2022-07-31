from cgitb import reset
from django.shortcuts import redirect, render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def webpage2(request):
    return render(request,'hereditary.html')

def webpage3(request):
    return render(request,'donate.html')

def webpage4(request):
    return render(request,'receive.html')

def suggest(request):
    if request.method == "GET":
        bg = request.GET['bloodgroup_1']
        bg2 = request.GET['bloodgroup_2']
        if bg and bg2 == 'A':
            res = ['O','A']
            return render(request,'hereditary.html',{'res':res})
        elif bg and bg2 == 'B':
            res = ['B','O']
            return render(request,'hereditary.html',{'res':res})
        elif bg == 'O' and bg2 == 'O':
            res = ['O','O']
            return render(request,'hereditary.html',{'res':res})
        elif bg == 'AB' and bg2 == 'AB':
            res = ['A','B','AB']
            return render(request,'hereditary.html',{'res':res})
        elif bg == 'A' and bg2 == 'B' or bg == 'B' and bg2 == 'A':
            res = ['O','A','B','AB']
            return render(request,'hereditary.html',{'res':res})
        elif bg == 'A' and bg2 == 'AB' or bg == 'AB' and bg2 == 'A':
            res = ['A','B','AB']
            return render(request,'hereditary.html',{'res':res})
        elif bg == 'A' and bg2 == 'O' or bg == 'O' and bg2 == 'A':
            res = ['O','A']
            return render(request,'hereditary.html',{'res':res})
        elif bg == 'AB' and bg2 == 'B' or bg == 'B' and bg2 == 'AB':
            res = ['A','B','AB']
            return render(request,'hereditary.html',{'res':res})
        elif bg == 'O' and bg2 == 'B' or bg == 'B' and bg2 == 'O':
            res = ['O','B']
            return render(request,'hereditary.html',{'res':res})
        elif bg == 'AB' and bg2 == 'O' or bg == 'O' and bg2 == 'AB':
            res = ['A','B']
            return render(request,'hereditary.html',{'res':res})

def donar_request(request):
    if request.method == 'GET':
        bg = request.GET['bloodgroup']
        if bg == 'A':
            res = ['A','AB']
            return render(request,'donate.html',{'res':res})
        elif bg == 'B':
            res = ['B','AB']
            return render(request,'donate.html',{'res':res})
        elif bg == 'AB':
            res = ['AB']
            return render(request,'donate.html',{'res':res})
        elif bg == 'O':
            res = ['A','B','AB','O']
            return render(request,'donate.html',{'res':res})
    
def recevier_request(request):
    if request.method == 'GET':
        bg = request.GET['bloodgroup']
        if bg == 'A':
            res = ['A','O']
            return render(request,'receive.html',{'res':res})
        elif bg == 'B':
            res = ['B','O']
            return render(request,'receive.html',{'res':res})
        elif bg == 'AB':
            res = ['A','AB','B','O']
            return render(request,'receive.html',{'res':res})
        elif bg == 'O':
            res = ['O']
            return render(request,'receive.html',{'res':res})


        
        


