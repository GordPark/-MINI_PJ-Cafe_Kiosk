from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("환영합니다. 무인카페 코코입니다. [주문시작]버튼을 눌러주세요.")