from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
class Login(APIView):
    template_name = "login.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Home(APIView):
    template_name = "home.html"
    def get(self, request):
        return render(request, self.template_name)

class Register(APIView):
    template_name = "register.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Comments(APIView):
    template_name = "comments.html"
    def get(self, request):
        return render(request, self.template_name)
    