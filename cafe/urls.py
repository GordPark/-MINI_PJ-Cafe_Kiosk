from django.urls import path
from . import views

app_name = "cafe"

urlpatterns = [
    path("<int:order_id>/", views.CategoryListView.as_view(), name="category"),
    path("<int:order_id>/<int:category_id>/shopping/<int:shopping_id>/", views.ShoppingDetailView.as_view(), name="shopping"),
    path("<int:order_id>/<int:category_id>/", views.MenuDetailView.as_view(), name="menu_detail"),
    
    # path("", views.index, name="index")
]