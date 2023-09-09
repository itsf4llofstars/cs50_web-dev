from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render

# Global that which will be avail to everything in
# the project. Delete this when using sessions.
# tasks = []


# class that represents the form to be created by django
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.
def index(request):
    # Here is the tasks variable when using sessions
    if "tasks" not in request.session:  # is there a tasks in this session?
        request.session["tasks"] = []  # if not, then create it for this session
    return render(request, "tasks/index.html", {
            # Information that index.html needs
            # "tasks": tasks  # Not used when using sessions
            "tasks": request.session["tasks"]  # Use when using sessions
        },
    )


def add(request):
    if request.method == "POST":
        # create a form with the user submitted data
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # Gets the task the user submitted
            task = form.cleaned_data["task"]
            # tasks.append(task)  # remove when using sessions

            # Using sessions, adds the new tasks added as a list to the end of 
            # request.session["tasks"]
            request.session["tasks"] += [task]
            
            # redirect user to tasks/ page after submiting valid task
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # if bad data send back the data
            return render(request, "tasks/add.html", {"form": form})

    return render(request, "tasks/add.html", {"form": NewTaskForm()})
