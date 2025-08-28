from django.shortcuts import render

# Create your views here.
def home(request):
    """Homepage displaying the restaurant name."""
    context = {
        "restaurant_name": settings.RESTAURANT_NAME
    }
    return render(request,"home.html",context)

def about(request):
    return render(request,"about_us.html")

def contact_us(request):
    return render(request,"contact_us.html")