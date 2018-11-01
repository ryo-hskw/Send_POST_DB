import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Return_json.models import Fruits


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
        # print(json.loads(request.body)) # json形式で受信
        # print(request.POST) # jsonをDict形式で受信(Dictには何も受信できていない)
        json_list = json.loads(request.body)
        print(json_list)

        # for i in json_list:
        #     print(i.get(json_list.keys()))

        # print(json_list.get(json_list.keys()))

        for i in json_list.values():
            insert_json = Fruits(price=i)
            insert_json.save()
    return HttpResponse(request)
