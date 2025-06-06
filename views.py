from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Meu App - Hello World</h1>")
