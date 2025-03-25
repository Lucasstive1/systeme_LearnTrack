from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import Document

# Create your views here.
def index(request):
    return render(request, 'fontend/index.html')



def about(request):
    return render(request, 'fontend/autres/about.html')



def comments(request):
    return render(request, 'fontend/autres/comments.html')



def faq(request):
    return render(request, 'fontend/autres/faq.html')



def inscription(request):
    return render(request, 'fontend/autres/inscription.html')



def connexion(request):
    return render(request, 'fontend/autres/connexion.html')

def epreuve(request):
    documents = Document.objects.all()
    return render(request, 'fontend/autres/epreuve.html', {'documents': documents})
