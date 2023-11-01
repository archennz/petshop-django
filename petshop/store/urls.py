from django.urls import path


from . import views
app_name = "store"
urlpatterns = [
    path("product", views.IndexView.as_view(), name="index"),
    path("product/<int:pk>", views.DetailView.as_view(), name="detail"),
    path("product/<int:pk>/order/", views.submitOrder, name="order")
]