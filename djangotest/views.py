from django.http import HttpResponse

def hello(request):
    return HttpResponse('teste')

def test(request, year):
    return HttpResponse('Passou' + str(year))