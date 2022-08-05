"""ocean_basket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from online_booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='Home'),
    path('create_booking/', views.CreateBooking.as_view(), name='Create Booking'),
    path('accounts/', include('allauth.urls')),
    path('view_booking/', views.ViewBooking.as_view(), name='View Booking'),
    path('edit_booking/<booking_id>', views.EditBooking.as_view(), name='Edit Booking'),
    path('delete_booking/<booking_id>', views.DeleteBooking.as_view(), name='Delete Booking'),
    path('view_day_bookings/', views.FilterBySelectedDate.as_view(), name='View Day Bookings'),
]
