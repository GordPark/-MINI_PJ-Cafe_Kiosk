from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


# Create your views here.
class CategoryListView(ListView):
    model = Menu_Category
    template_name = "cafe/category_list.html"
    context_object_name = "category"    
    

    def get_queryset(self):
        return Menu_Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_id'] = self.kwargs.get('order_id')
        return context

class MenuDetailView(DetailView):
    model = Menu_Category
    template_name = "cafe/menu_detail.html"

    def get_object(self):
        # order_id는 URL에서 가져옵니다.
        order_id = self.kwargs.get('order_id')
        category_id = self.kwargs.get('category_id')
        # 주문 ID와 카테고리 ID를 모두 사용하여 카테고리를 가져옵니다.
        category = get_object_or_404(Menu_Category, id=category_id)
        return category
    

class ShoppingDetailView(DetailView):
    model = Shopping_Cart
    template_name = "cafe/shopping_cart.html"

