from django.urls import path, include
from store import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from store.views import ReviewViewSet, CartItemViewSet

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)
product_router = routers.NestedDefaultRouter(router, 'products', lookup="product")
product_router.register('reviews', ReviewViewSet, basename="product-reviews")
cartItem_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cartItem_router.register('items', CartItemViewSet, basename='cart-cartItem')

#urlpatterns = router.urls+product_router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cartItem_router.urls)),
    path('collection/', views.CollectionList.as_view(), name='collection_detail'),

]
