from django.urls import path, include
from . import views


urlpatterns = [
    # Pizza Urls
    path('pizzas/', views.PizzaListCreateView.as_view()),
    path('pizzas/<int:pk>', views.PizzaUpdateRetriveDeleteView.as_view()),
]