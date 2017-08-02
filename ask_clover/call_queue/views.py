import datetime as dt

from django.shortcuts import HttpResponse, render

from .forms import CallForm
from .models import Call


def index(request):
    return HttpResponse('hi!')


def queued_calls(request):
    queued_calls = Call.objects.order_by('timestamp')
    context = {'queued_calls': queued_calls}
    return render(request, 'call_queue/queued_calls.html', context)


def add_call(request):
    if request.method == 'POST':
        data = dict(request.POST)
        data['timestamp'] = dt.datetime.now()
        form = CallForm(data)
        if form.is_valid():
            form.save()
            return HttpResponse('thanks!')
        else:
            return HttpResponse('error!')
    else:
        form = CallForm()
    return render(request, 'call_queue/add_call.html', {'form': form, })


def thanks(request):
    return HttpResponse('thanks!')
