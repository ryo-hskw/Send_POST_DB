import json
import pymongo
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Send_POST_DB import settings

Mongo_URL = settings.Mongo_Address


# Create your views here.
def index(request, data):
    """response を JSON で返却"""
    json_str = json.dumps(data)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8')
    return response


# Create your views here.
@csrf_exempt
def receive_post(request):
    print(request)
    return HttpResponse(request)


def hello_world(request):
    data = {'Result': 'Hello World!'}
    return index(request, data)


'''
def insert_json():
    print(Mongo_URL)

    client = pymongo.MongoClient(Mongo_URL)
    db = client['study']
    co = db['Hello_World']

    result = co.insert(receive_post())

    return
'''