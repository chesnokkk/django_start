from django.shortcuts import render

# Create your views here.
def home(request):

    data ={
       'title':'Main page'
    }
    return render(request, 'servicies/index.html',data)
def uslugi(request):
    data = {
        'title': 'Uslugi'
    }
    return render(request, 'servicies/servicies.html',data)