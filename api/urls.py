from django.urls import path
from api.views import AudioProcessingView, ProductView


urlpatterns = [
    path('products/', ProductView.as_view(), name='product-list'),
    path('process-audio/', AudioProcessingView.as_view(), name='process-audio'),
]
