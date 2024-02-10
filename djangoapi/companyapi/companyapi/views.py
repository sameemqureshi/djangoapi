from django.http import HttpRequest,HttpResponse

def home_page(request):
    print("hello world")
    return HttpResponse("this is a home page")
