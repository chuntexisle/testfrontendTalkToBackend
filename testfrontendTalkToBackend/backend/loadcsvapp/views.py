from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


from rest_framework import generics
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer

posts = [{
    'author': 'Anna',
    'title': 'Blog post 1'}]
    
def index(request):
    context = {'posts': posts}
    return render(request, 'index.html', context)

#def index(request):
#    return HttpResponse("Hello World") 

class BlogView(viewsets.ModelViewSet):
   	queryset = Blog.objects.all()
   	serializer_class = BlogSerializer

class EndpointView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class= BlogSerializer

class HelloWorld(APIView):
    def get(self, request, format=None):
        data = {'message': 'Hello World!'}
        return Response(data['message'])

def get_data(request):
    data = {"message": "Hello, World!"}
    return JsonResponse(data)

                                
