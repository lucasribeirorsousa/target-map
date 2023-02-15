from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import folium

from .models import Target
from apps.targets.forms import TargetForm


@csrf_exempt
def home(request):
    targets = Target.objects.all()

    map = folium.Map(location=[-12.6, -50.9], zoom_start=3)

    for target in targets:
        marker = folium.Marker([target.latitude, target.longitude], tooltip=target.name)
        marker.add_child(folium.Popup('id="{}" latitude="{}" longitude="{}"'.format(target.id, target.latitude, target.longitude)))
        marker.add_to(map)

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
            return JsonResponse({'success': True})
        else:
            messages.error(request, 'Houve um erro ao adicionar o target. Por favor, corrija os erros abaixo.')
    else:
        form = TargetForm()
    return render(request, 'add_target.html', {'form': form})

@csrf_exempt
def get_target(request, target_id):
    target = Target.objects.get(pk=target_id)
    data = {
        'id': target.id,
        'name': target.name,
        'latitude': target.latitude,
        'longitude': target.longitude,
        'date_expiry': target.date_expiry,
        # add any other target fields you want to include in the JSON response
    }
    return JsonResponse(data)

@csrf_exempt
def edit_target(request, target_id):
    target = get_object_or_404(Target, id=target_id)
    if request.method == 'POST':
        form = TargetForm(request.POST, instance=target)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alvo atualizado com sucesso!')
            return redirect('target_detail', target_id=target_id)
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = TargetForm(instance=target)
    return render(request, 'edit_target.html', {'form': form, 'target': target})


@csrf_exempt
def delete_target(request, target_id):
    target = get_object_or_404(Target, id=target_id)
    target.delete()
    return redirect('map')