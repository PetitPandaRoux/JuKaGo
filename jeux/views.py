from django.shortcuts import render

# Create your views here.

def show_jeux(request):
    return render(request,'jeux.html')