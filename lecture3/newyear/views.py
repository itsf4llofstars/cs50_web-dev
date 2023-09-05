import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    """http://127.0.0.1:8000/newyear
    Gets and sets the current month and day
    to be compared if newyear. Sets newyear key
    to the returned bool if month and day are 1
    (newyear)

    NOTE: Changing the now.month &/| now.day values
    may require a server restart
    """
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })