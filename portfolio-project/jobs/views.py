from django.shortcuts import render

# Create your views here.
def madhav(request):
    return render(request, 'jobs/home.html')
