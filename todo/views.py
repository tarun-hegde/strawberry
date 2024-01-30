from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index_view(request):
    context = {"title": "API"}
    response=JsonResponse(context)
    return response