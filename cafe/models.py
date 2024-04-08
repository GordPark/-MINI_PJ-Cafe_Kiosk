from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
# 메뉴 카테고리 : coffe / tea / Beverages

class Menu_Category(models.Model):
    category = models.CharField(verbose_name="category",max_length=20)
    # 외래키 참조 시 문자열로 참조하여 클래스 정의 처리
    # 다음페이지로 넘어갈 url에 사용될 키 값
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='menu_categories', null=True) 

    class Meta:
        ordering = ('category',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category
    


# 메뉴 : 카테고리[Coffe / Tea / Beverage / ] - 메뉴[Americano/Espresso/Latte/Cappuccino/...]
class Menu(models.Model):    
    menu_name = models.CharField('MENU NAME',max_length=20)
    category = models.ForeignKey(Menu_Category, on_delete=models.CASCADE)
    # 옵션: Hot / Iced / Only Iced
    option = models.CharField('OPTION',max_length=20, default='default_option')
    price = models.IntegerField()
    description = models.TextField()    
    best = models.BooleanField(default=True)
    # 품절처리
    disabled = models.BooleanField(default=True)
    
    ## 해당경로 만들고 디비에 저장하고 만들어야함
    # 메서드 만들어서 
    # get_absolute_url처럼 가져와도됨    
    def get_image_path(self):
        pass
    
    
    class Meta:
        ordering = ('category',)
    
    def __str__(self):
        return self.menu_name
    
    

# 장바구니(메뉴이름 / 단가 / 수량 / 총액)
class Shopping_Cart(models.Model):
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_name_items')
    price = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_price_items' )
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    total_amount = models.IntegerField()
    option = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_option', null=True)
    

# 주문 
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)   
    menu_name = models.ForeignKey('Shopping_Cart',  related_name='menu_order_set', on_delete=models.CASCADE, null=True)
    menu_quantity = models.ForeignKey('Shopping_Cart', related_name='menu_quantity_set', on_delete=models.CASCADE, null=True)
    order_dt = models.DateTimeField(auto_now_add=True)  
    wait_id = models.IntegerField(null=True)

# 결제
class Charge(models.Model):
    pass

def get_absolute_url(self):
    return reverse('cafe:cafe_detail', args=(self.slug,))