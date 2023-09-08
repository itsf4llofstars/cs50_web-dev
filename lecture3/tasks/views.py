from django import forms
from django.shortcuts import render

# Global that which will be avail to everything in
# the project
tasks = ["foo", "bar", "baz"]

# class that represents the form to be created by django
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


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
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
