from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Home(View):
    def get(self,request):
        return render(request,'home.html')
class GetInput(View):
    def get(self,request):
        return render(request,'getinput.html')
class PostInput(View):
    def get(self,request):
        return render(request,'getinput.html')
class Add(View):
    def get(self,request):
        p=int(request.GET["t1"])
        q=int(request.GET["t2"])
        r=p+q
        return HttpResponse("The sum is:" +str(r))
    def post(self,request):
        X=int(request.POST["t1"])
        Y=int(request.POST["t2"])
        Z=X+Y
        return HttpResponse("The sum is:"+str(z))

