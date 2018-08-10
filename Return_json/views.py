import json
import pymongo
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from Send_POST_DB import settings


# Create your views here.
'''
def index(request, data):
    """response を JSON で返却"""
    json_str = json.dumps(data)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8')
    return response
'''


@csrf_exempt
def receive_post(request):
    print("ok")
    return HttpResponse(request)


def insert_json(request):
    print(Mongo_URL)

    print(json.dumps(receive_post(request)))

    client = pymongo.MongoClient(Mongo_URL)
    db = client['study']
    co = db['Hello_World']

    co.insert(receive_post(request))
    print(co.find())

    return HttpResponse('OK')
