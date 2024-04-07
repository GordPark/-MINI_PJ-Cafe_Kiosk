from django.views.generic import TemplateView
from cafe.models import Menu_Category, Order 
from django.shortcuts import redirect


class HomeView(TemplateView):
    model = Menu_Category
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 새로운 주문 생성
        new_order = Order.objects.create()
        # 생성된 주문의 order_id 가져오기
        order_id = new_order.order_id
        # 템플릿 컨텍스트에 order_id 추가
        context['order_id'] = order_id
        return context