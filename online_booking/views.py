from django.shortcuts import render

# Create your views here.


def get_home_page(request):
    """This function will display the home page"""
    return render(request, 'online_booking/home_page.html')
