from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


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
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_id'] = self.kwargs.get('order_id')
        return context
    
    def get_object(self):
        # order_id는 URL에서 가져옵니다.
        
        category_id = self.kwargs.get('category_id')
        # 주문 ID와 카테고리 ID를 모두 사용하여 카테고리를 가져옵니다.
        category = get_object_or_404(Menu_Category, id=category_id)
        return category
    
    

class ShoppingDetailView(DetailView):
    model = Shopping_Cart
    template_name = "cafe/shopping_cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_id'] = self.kwargs.get('order_id')
        context['category_id'] = self.kwargs.get('category_id')
        context['shopping_id'] = self.kwargs.get('shopping_id')
        return context   
    # def get_object(self):
    #     # shopping_id는 URL에서 가져옵니다.
        
    #     shopping_id = self.kwargs.get('pk')        # pk를 가져옴
    #     shopping = get_object_or_404(Shopping_Cart, id=shopping_id)      
    
    
    def post(self, request, *args, **kwargs):
        menu_id = request.POST.get('menu_id')
        quantity = request.POST.get('quantity')
        option = request.POST.get('option')
        shopping_cart_item = Shopping_Cart.objects.create(
            menu_id=menu_id,
            quantity=quantity,
            option=option,
            # 다른 필드들 설정
        )
         # 처리가 완료되면 JSON 응답 반환
        return JsonResponse({'message': '장바구니에 추가되었습니다.'})
    
    # quantity = 

    # def get_queryset(self):
    #     """Return the last fiv publisehd questions."""
    #     return Question.objects.order_by("-pub_date")[:7]
    
    # def vote(request, question_id):
    #     # choice 데이터에서 해당하는 값에 votes를 1 더하기
    #     question = get_object_or_404(Shopping_Cart, pk=question_id)
    #     try:
    #         selected_choice = question.choice_set.get(pk=request.POST["choice"])
    #     except (KeyError, Choice.DoesNotExist):
    #         # Redisplay the question voting form.
    #         return render(
    #             request,
    #             "prg_pj/detail.html",
    #             {
    #                 "question": question,
    #                 "error_message": "You didn't select a choice.",
    #             },
    #         )
    #     else:
    #         selected_choice.votes = F("votes") + 1
    #         # 모든 선택지의 투표수 1증가
    #         Choice.objects.filter(question_id=question_id).update(votes=F('votes')+1)
    #         # 특정 선택지의 투표 수 감소
    #         Choice.objects.filter(question_id=question_id).update(votes=F('votes')-1)
            
            
    #         # 모든 선택지의 튜표 두배로 늘리기
    #         Choice.objects.filter(question_id=question_id).update(votes=F('votes')*2)

    #         selected_choice.save()
    #         # Always return an HttpResponseRedirect after successfully dealing
    #         # with POST data. This prevents data from being posted twice if a
    #         # user hits the Back button.
    #         return HttpResponseRedirect(reverse("prg_pj:results", args=(question.id,)))
        
    #     # return HttpResponse("You're voting on question %s." % question_id)
        
