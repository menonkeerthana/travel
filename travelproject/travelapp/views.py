from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def demo(request):
#     return render(request,'home.html')
#     # return HttpResponse("hello world")
#
# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse('I am contact')

from . models import Place
from . models import Team
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request, 'index.html',({'result':obj,'team':obj1}))
    # name="India"
    # return render(request,'home.html',{'obj':name})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})


