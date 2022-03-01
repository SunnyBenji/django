from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="shop"
urlpatterns = [
    path('', views.index, name="all_product"),
    path('<int:product_id>/', views.details, name="details_product"),
    path('create', views.create, name="create_product"),
    path('edit/<int:product_id>', views.edit, name="edit_product"),
    path('delete/<int:product_id>', views.delete, name="delete_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
