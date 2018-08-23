import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


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
    if request.method == "POST":
        print(json.loads(request.body))
        print(request.POST)
        dec = json.loads(request.body)
        print(dec['name'])
    return HttpResponse(request)


def insert_json(request):
    print(json.dumps(receive_post(request)))
    return HttpResponse('ok')

