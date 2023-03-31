from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
import time

myBool=False

def Bool(request):
    global myBool
    if myBool:
        myBool=False
    else:
        myBool=True
    return HttpResponse(myBool)
        
def Home(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            while True:
                time.sleep(3)
                if myBool==False:
                    continue
                data = json.load(request)
                todo = data.get('payload')
                print(todo)
                return JsonResponse({'status': 'OK'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    # def event_stream():
    #     while True:
    #         yield f"data: {json.dumps(22)}\n\n"
    #         time.sleep(5)
    # return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    return render(request,"Home.html") 
