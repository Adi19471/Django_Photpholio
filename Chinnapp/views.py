from django.shortcuts import render

# Create your views here.
def chinna_view(request):
    return render(request, 'Chinna/chinna.html')