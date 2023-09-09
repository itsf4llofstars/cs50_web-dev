from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     """http://127.0.0.1:8000/hello
#     This is the first example, it has been re-written
#     to the return render(request, ...) code below
#     """
#     return HttpResponse("Hello, world!")


def index(request):
    """http://127.0.0.1:8000/hello
    ./hello/urls.py remaines unchanged but when
    requesting :8000/hello we now load the index.html file
    """
    return render(request, "hello/index.html")


def harley(request):
    """http://127.0.0.1:8000/hello/harley"""
    return HttpResponse("Hello, Harley, you're a good girl!")


def sister(request):
    """http://127.0.0.1:8000/hello/sister"""
    return HttpResponse("Hello, sister")


def brother(request):
    """http://127.0.0.1:8000/hello/brother"""
    return HttpResponse("Hello, brother")

# def greet(request, name):
#     """http://127.0.0.1:8000/hello/brother
#     name.capitalize() can be used in lue of title()
#     This was a first example and has been re-written below
#     to utilize the render function
#     """
#     return HttpResponse(f"Hello, {name.title()}")


def greet(request, name):
    """http://127.0.0.1:8000/hello/brother
    render func takes a third argument that passes a
    dicitonary to template greet.html
    """
    return render(request, "hello/greet.html", {
        # this dictionary is the context of the render func,
        # it takes all the info for the tmeplate that is called
        "name": name.title(),
        "age": "3",
        })
