from django.urls import path
from users import views as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from products import views as ProductViews
from carts import views as CartViews

urlpatterns = [
    path('register/', UserViews.RegisterView.as_view()),
    
    # user API's
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserViews.ProfileView.as_view()),
    
    # product API's
    #product list (all)
    path('products/', ProductViews.ProductListView.as_view()),
    #product detail (one)
    path('products/<int:pk>/', ProductViews.ProductDetailView.as_view()),
    
    # cart API's
    path('cart/', CartViews.CartView.as_view()),
    
    # add to cart
    path('cart/add/', CartViews.AddToCartView.as_view()),
    
    # Manage cart
    path('cart/items/<int:item_id>/', CartViews.ManageCartItemView.as_view()),
]