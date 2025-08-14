from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def error(request):
    return render(render,'404.html')