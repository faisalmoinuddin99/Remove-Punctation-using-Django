# I have created this file - Faisal
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext = request.GET.get('text', 'default')
    removePunc = request.GET.get('removepunc','off')
    if removePunc == 'on':
        puncutaion = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzer = ''
        for char in djtext:
            if char not in puncutaion:
                analyzer = analyzer + char
        params = {'purpose':'Puncuation Remover','analyze_text':analyzer}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")


