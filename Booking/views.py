from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
    return render(request, 'Booking/booking.html')
    
