from django.urls import path
from . import views

urlpatterns = {
    path("", views.index, name="index"),
    path("harley", views.harley, name="harley"),
    path("sister", views.sister, name="sister"),
    path("brother", views.brother, name="brother"),
    path("<str:name>", views.greet, name="greet"),
}
