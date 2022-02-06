from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from discover.models import knowcode


def index(request):
    know_all = knowcode.objects.all()
    know20 = knowcode.objects.filter(year=2020).order_by('large_level')
    context = {
        'know20': know20,
        'know_all' : know_all
    }
    return render(request, 'discover/index.html', context)

def get_data(request):
    receive_message = request.GET.get('year_str')
    know = list(knowcode.objects.filter(year=receive_message).order_by('large_level').values())
    # print('views : ',know)
    send_message = {
        'know' : know
    }
    return JsonResponse(send_message)