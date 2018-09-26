from django.shortcuts import render, redirect, resolve_url
from django.views import View
from liuyanapp.models import LiuyanModels
from .forms import LiuyanForm


# Create your views here.
class HelloView(View):
    def get(self, request):
        return HttpResponse('hello')

class IndexView(View):
    # 使用get的方法获取大页面

    def get(self, request):
        liuyans = LiuyanModels.objects.all()
        return render(request, 'liuyan.html', {"liuyans": liuyans})

    # 使用post的方法提交页面
    def post(self, request):
        # 实例化数据库
        liuyan = LiuyanModels()
        liuyan.name = request.POST.get("name")
        liuyan.email = request.POST.get("email")
        liuyan.address = request.POST.get("address")
        liuyan.message = request.POST.get("message")
        # 保存数据到数据库
        liuyan.save()
        return redirect(resolve_url("index"))