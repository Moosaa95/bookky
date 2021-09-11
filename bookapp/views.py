from django.shortcuts import render, HttpResponse

# Create your views here.

def layout(request):
    big = "man"
    return render(request, 'index.html', {'big':big})

