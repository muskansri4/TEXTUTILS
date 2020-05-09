from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request, 'index.html')
    #return HttpResponse("about om")

def analyse(request):
    #get the text
    djtext=request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc', 'off')
    newline = request.GET.get('newline', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    removespace = request.GET.get('removespace', 'off')
    charcount = request.GET.get('charcount', 'off')

    if removepunc == 'on':
      punc = '''!()-[]{};:'"\,<>?/.'''
      analyzed = " "
      for char in djtext:
        if char not in punc:
            analyzed = analyzed + char

      params={'purpose':'Removed punctuation', 'analyzed_text': analyzed}
      djtext=analyzed
     # return render(request, 'analyse.html', params)
    if(fullcaps=="on"):
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Captalised', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyse.html', params)
    if(newline=="on"):
        analyzed = " "
        for char in djtext:
           if char !="\n":
            analyzed = analyzed + char
        params = {'purpose': 'newline', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyse.html', params)
    if (removespace == "on"):
        analyzed = " "
        for i,char in enumerate(djtext):
            if djtext[i]==" " :
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'removespace', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyse.html', params)
    '''if (charcount == "on"):
        analyzed = " "
        l=len(djtext)
        params = {'purpose': 'removespace', 'analyzed_text': l}'''

    if(removepunc != 'on' and fullcaps !="on" and newline !="on" and  removespace != "on"):

       return HttpResponse("Please choose at least on option")




    return render(request, 'analyse.html', params)
def capt(request):
    return HttpResponse("remove capt <a href='/'>return to home page</a>")
def ex1(request):
    s='''<h1>NAVIGATION BAR</h1>
    <a href="https://www.google.com/">google</a>'''
    return HttpResponse(s)

