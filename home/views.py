from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def hakkimizda(request):
    return render(request, 'home/hakkimizda.html')

def iletisim(request):
    return render(request, 'home/iletisim.html')
