# This file is created by Pradip Kumar Murmu

from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
     
     return render(request, 'index.html')

def analyze(request):
     djtext = request.GET.get('text','default')
     removepun = request.GET.get('removepunc', 'off')
     if removepun == 'on':

          punctuations ='''~`!@#$%^&*()_+-={[]}|:;"'<,.>/'''
          analyzed = ''
          for char in djtext:
               if char not in punctuations:
                    analyzed +=char
          params = {
               'purpose' : 'Removed Punctuations',
               'analyzed_text':analyzed,
          }
          return render(request, 'analyze.html', params)
     else:
          return HttpResponse('Error')

# def capitalizefirst(request):
#      return HttpResponse('capitalize first')


# def newlineremove(request):
#      return HttpResponse(' NEW Line remove')

# def charcount(request):
#      return HttpResponse('Char count')

# def spaceremove(request):
#      return HttpResponse('space remove')
          