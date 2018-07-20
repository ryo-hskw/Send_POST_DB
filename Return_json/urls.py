from django.urls import path
from Return_json import views


app_name = 'Return_json'
urlpatterns = [
    path('', views.hello_world, name='hello_world'),
#    path('return_request', views.return_request, name='return_request'),
    path('receive_post', views.receive_post, name='receive_post')
]


