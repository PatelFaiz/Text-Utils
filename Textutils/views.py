from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "Index.html")


def about(request):
    return render(request, "About.html")


def contact(request):
    return render(request, "Contact.html ")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspace = request.POST.get('extraspace', 'off')

    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-_{}[]:;'"\/,<>.?@#$%^&*~='''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char is not "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'New line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspace == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass;
            else:
                analyzed += char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}


    if extraspace != 'on' and newlineremover != 'on' and fullcaps != 'on' and removepunc != 'on':
        return HttpResponse('Please select options...')
    else:
        return render(request, 'Analyze.html', params)
