
from django.shortcuts import render
from .models import UserName

def index(request):
    msg = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            UserName.objects.create(name=name)
            msg = f'Привет, {name}!'
        else:
            msg = 'Имя не может быть пустым'
    return render(request, 'index.html', {'message': msg})
