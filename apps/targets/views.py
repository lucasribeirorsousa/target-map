from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import folium

from .models import Target
from apps.targets.forms import TargetForm

def home(request):
    targets = Target.objects.all()

    map = folium.Map(location=[-12.6, -50.9], zoom_start=3)

    for target in targets:
        folium.Marker([target.latitude, target.longitude], tooltip=target.name).add_to(map)
                  
    map = map._repr_html_()
  
    context = {'map': map}
    return render(request, 'home.html', context)

@csrf_exempt
def add_target(request):
    if request.method == 'POST':
        form = TargetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Target adicionado com sucesso.')
            return redirect('home')
        else:
            messages.error(request, 'Houve um erro ao adicionar o target. Por favor, corrija os erros abaixo.')
    else:
        form = TargetForm()
    return render(request, 'add_target.html', {'form': form})