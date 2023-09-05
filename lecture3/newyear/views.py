import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    """Gets and sets the current month and day
    to be compared if newyear. Sets newyear key
    to the returned bool if month and day are 1
    (newyear)
    """
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })