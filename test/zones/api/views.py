from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from zones.models import Zone,Distribution
from django.contrib import messages

from .business import delete_spaces
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from datetime import datetime

@api_view(['POST'])
def edit(request):
    distributions = request.data.get("distributions")
    zone_id = request.data.get('id')
    name = request.data.get('name')
    if (name == '' or name == None):
         return Response('', status=status.HTTP_400_BAD_REQUEST)
    name = delete_spaces(name)
    zone = Zone.objects.filter(pk=zone_id).first()
    if not zone:
        return Response('', status=status.HTTP_400_BAD_REQUEST)
    Zone.objects.filter(pk=zone_id).update(name=name,updated_at = datetime.today())
    # zone.name = name
    # zone.update_at = datetime.today()
    # zone.save()
    # t = zone.distribution_set.all()
    _zone_id = int(zone_id)
    _distributions = Distribution.objects.filter(zone_id = _zone_id)
    if not _distributions:
        return Response()
    counter = 0
    for d in distributions:
        counter = counter + int(d["percentage"])
    if counter != 100:
        return Response('', status=status.HTTP_400_BAD_REQUEST)
    i=0
    for d in _distributions:
        d.percentage = distributions[i]["percentage"]
        d.save()
        i += 1
    messages.success(request, 'Ok')
    return Response()


@api_view(['POST'])
def delete(request):
    zone_id = request.data.get('id')
    zone = Zone.objects.filter(pk=zone_id).first()
    if not zone:
        return Response('', status=status.HTTP_400_BAD_REQUEST)
    zone.delete()
    return Response()

@api_view(['POST'])
def add(request):
    if request.method == 'POST':
      var = request.POST
    return Response()

@api_view(['POST'])
def add(request):
    if request.method == 'POST':
        distributions = request.data.get("distributions")
        name = request.data.get('name')
        d = Zone.objects.create(name=name,updated_at = datetime.today())
        for di in distributions:
            Distribution.objects.create(percentage = di['percentage'])
            #d.distribution_set.create(distributions[di.pk-1]["percentage"])
    return Response()

class ZoneCreateView(CreateView):
    model = Zone
    fields = ['name']
    template_name = "create.html"
    success_url = reverse_lazy("test:home")