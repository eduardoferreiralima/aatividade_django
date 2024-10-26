from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    return render(request, 'enquetes/core-index.html')
def criar_enquete(request):
    return render(request, 'enquetes/enquetes-index.html')
# Create your views here.
