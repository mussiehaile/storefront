from django.urls import path
from . import views
#from rest_framework.routers import SimpleRouter,DefaultRouter
from rest_framework_nested import routers



router = routers.DefaultRouter()
router.register('products',views.ProductViewSet,basename='products')
router.register('collections',views.CollectionViewSet)

product_router =routers.NestedDefaultRouter(router,'products',lookup = 'product')
product_router.register('reviews',views.ReviewViewSet,basename='product-reviews')
# URLConf
urlpatterns = router.urls + product_router.urls
    # path('products/', views.ProductList.as_view()),
    # path('products/<int:pk>/', views.ProductDetail.as_view()),
    # path('collections/', views.ColloectionList.as_view()),
    # path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
  


