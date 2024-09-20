from django.urls import path
from Webapp import views

urlpatterns = [
     path('Home/', views.home_page, name="Home"),
     path('About/', views.about_page, name="About"),
     path('Contact/', views.contact_page, name="Contact"),
     path('Service/', views.service_page, name="Service"),
     path('Blog/', views.blog_page, name="Blog"),
     path('Checkout/', views.checkout_page, name="Checkout"),
     path('Shop/', views.shop_page, name="Shop"),
     path('Cart/', views.cart_page, name="Cart"),
     path('Each_Products/<cat_name>', views.product_filtered, name="Each_Products"),
     path('Product/<int:p_id>', views.single_product_page, name="Product"),
     path('', views.user_register_page, name="User_Register"),
     path('User_Login/', views.user_login_page, name="User_Login"),
     path('save_user_register/', views.save_user_register, name="save_user_register"),
     path('user_login_session/', views.user_login_session, name="user_login_session"),
     path('user_logout/', views.user_logout, name="user_logout"),
     path('cart_data_save/<int:c_id>', views.cart_data_save, name="cart_data_save"),
     path('delete_cart_data/<int:c_id>', views.delete_cart_data, name="delete_cart_data"),
     path('save_customer_data/', views.save_customer_data, name="save_customer_data"),
     path("Payment/", views.payment_page, name="Payment"),
     path("save_feedback_data/", views.save_feedback_data, name="save_feedback_data"),
]
