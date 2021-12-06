from django.urls import path

from . import views

urlpatterns = [
    path('1112/create/', views.NewsViewSet.as_view({'post': 'create'}), name='news-create'),
    path('1215/update/<int:pk>/', views.NewsViewSet.as_view({'put': 'update'}), name='news-create'),
    path('1319/destroy/<int:pk>', views.NewsViewSet.as_view({'delete': 'destroy'}), name='news-create'),
    path('1417/list/', views.NewsViewSet.as_view({'get': 'list'}), name='news-create'),
    path('1520/deatil/<int:pk>', views.NewsDetailAPIView.as_view(), name='news-create'),
]
