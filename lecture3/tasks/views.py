from django import forms
from django.shortcuts import render

# Global that which will be avail to everything in
# the project
tasks = ["foo", "bar", "baz"]


# class that represents the form to be created by django
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


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
    if request.method == "POST":
        # create a form with the user submitted data
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # Gets the task the user submitted
            task = form.cleaned_data("tasks")
            tasks.append(task)
        else:
            # if bad data send back the data
            return render(request, "tasks/add.html", {
                "form": form
            })
        
    return render(request, "tasks/add.html", {"form": NewTaskForm()})
