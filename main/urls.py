from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('show/<int:id>/',views.show,name='show'),
    path('reviews/<int:id>/',views.reviews,name='reviews'),
    path('cart/',views.cart,name='cart'),
    path('index/',views.index,name='cart'),
    path('delete_cart_item/<int:id>/',views.delete_cart_item,name='delete_cart_item'),
    path('update_quantity/<int:id>/',views.update_quantity,name='update_quantity'),
    path("go_to_carts/",views.go_to_carts,name='carts'),
    path('delete_review/<int:id>/',views.delete_review,name='delete_review'),
    path('adress/',views.adress,name='adress'),
    path('order/',views.order,name='order')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)