from django.urls import path
from Return_json import views


app_name = 'Return_json'
urlpatterns = [
    # path('index', views.index, name='index'),
    path('receive_post', views.receive_post, name='receive_post')
]
