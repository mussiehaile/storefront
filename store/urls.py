from django.urls import path
from . import views
#from rest_framework.routers import SimpleRouter,DefaultRouter
from rest_framework_nested import routers



router = routers.DefaultRouter()
router.register('products',views.ProductViewSet,basename='products')
router.register('collections',views.CollectionViewSet)
router.register('carts', views.CartViewSet)

product_router =routers.NestedDefaultRouter(router,'products',lookup = 'product')
product_router.register('reviews',views.ReviewViewSet,basename='product-reviews')

carts_router =routers.NestedDefaultRouter(router, 'carts', lookup ='cart')
carts_router.register('items',views.CartItemViewset , basename='cart-items')
# URLConf
urlpatterns = router.urls + product_router.urls + carts_router.urls
    # path('products/', views.ProductList.as_view()),
    # path('products/<int:pk>/', views.ProductDetail.as_view()),
    # path('collections/', views.ColloectionList.as_view()),
    # path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
  


