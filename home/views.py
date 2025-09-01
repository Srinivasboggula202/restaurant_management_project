from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    """Homepage displaying the restaurant details."""
    try:
        context = {
            "restaurant_name": getattr(settings, "RESTAURANT_NAME", "Restaurant"),
            "phone_number": getattr(settings, "RESTAURANT_PHONE_NUMBER", "Not Available"),
        }
        return render(request,"home.html",context)
    except Exception as e:
        return HttpResponse("Oops! something went wrong while loading the homepage.", status=500)

def about(request):
    return render(request,"about_us.html")

def contact_us(request):
    return render(request,"contact_us.html")

if __name__ == "__main__":
    print("Main file is running - Restaurant Homepage setup ready")