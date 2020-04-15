from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from PIL import Image
from . import bw2color_image
import requests


def homepg(request):
    return render(request, "colorizer/index.html")


@csrf_exempt
def cont(request):
    data = request.POST["actualdata"]
    requests.post("https://ensn9rhi4ak5.x.pipedream.net", data=data)
    return HttpResponse("OK")


@csrf_exempt
def colorpg(request):
    greyimage = request.FILES.get("image")
    uploaded_image = Image.open(greyimage)
    before, after = bw2color_image.colorit(uploaded_image)
    # JsonResponse(text)
    return JsonResponse({"beforeimg": before, "afterimg": after})
