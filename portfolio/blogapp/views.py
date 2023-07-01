from django.shortcuts import render, get_object_or_404
from .models import bloging

# Create your views here.
def blog(request):
    value = bloging.objects.all()
    return render(request,'blog.html',{'value':value})

def detail(request , num):
    #value = bloging.objects.all()
    value = get_object_or_404(bloging, pk=num)
    return render(request,'detail.html',{'value':value})