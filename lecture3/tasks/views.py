from django.shortcuts import render

# Global that which will be avail to everything in
# the project
tasks = ["foo", "bar", "baz", "buz", "fiz", "buz"]


# Create your views here.
def index(request):
    return render(
        request,
        "tasks/index.html",
        {
            # Information that index.html needs
            "tasks": tasks
        },
    )


def add(request):
    return render(request, "tasks/add.html")
