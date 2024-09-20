from django.urls import path
from Backend import views

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("add_categories_page/", views.add_categories_page, name="add_categories_page"),
    path("display_categories/", views.display_categories, name="display_categories"),
    path("save_categories/", views.save_categories, name="save_categories"),
    path("edit_category_page/<int:cat_id>", views.edit_category_page, name="edit_category_page"),
    path("update_category_page/<int:cat_id>", views.update_category_page, name="update_category_page"),
    path("delete_category_item/<int:cat_id>", views.delete_category_item, name="delete_category_item"),
    path("add_product_page", views.add_product_page, name="add_product_page"),
    path("save_products", views.save_products, name="save_products"),
    path("display_products_page", views.display_products_page, name="display_products_page"),
    path("edit_products_page/<int:pro_id>", views.edit_products_page, name="edit_products_page"),
    path("update_edit_products/<int:pro_id>", views.update_edit_products, name="update_edit_products"),
    path("delete_product_item/<int:pro_id>", views.delete_product_item, name="delete_product_item"),
    path("login_page/", views.login_page, name="login_page"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("feedback_page/", views.feedback_page, name="feedback_page"),
    path("feedback_data_delete/<int:f_id>", views.feedback_data_delete, name="feedback_data_delete"),
]
