from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("Hello, world!")


def index(request):
    return render(request, "hello/index.html")


def harley(request):
    return HttpResponse("Hello, Harley, you're a good girl!")


def sister(request):
    return HttpResponse("Hello, sister")


def brother(request):
    return HttpResponse("Hello, brother")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.title()}")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.title(),
        "age": "3",
        })
