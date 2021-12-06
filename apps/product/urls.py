from django.urls import path

from . import views

urlpatterns = [
    path('cover/category/create/', views.CoverCategoryCreateAPIView.as_view()),
    path('covers/categories/list/', views.CoverCategoryListAPIView.as_view()),
    path('cover/category/detail/<int:pk>/', views.CoverCategoryRetrieveAPIVIew.as_view()),
    path('cover/category/update/<int:pk>/', views.CoverCategoryUpdateViewSet.as_view({'put': 'update'})),
    path('cover/category/destroy/<int:pk>/', views.CoverCategoryDestroyAPIView.as_view()),
    path('car/category/create/', views.CarsCategoryCreateUpdateViewSet.as_view({'post': 'create'})),
    path('car/categories/list/', views.CarsCategoryListAPIView.as_view()),
    path('car/category/detail/<int:pk>/', views.CarsRetrieveAPIView.as_view()),
    path('car/category/update/<int:pk>/', views.CarsCategoryCreateUpdateViewSet.as_view({'put': 'update'})),
    path('car/category/destroy/<int:pk>/', views.CarsCategoryDestroyViewSet.as_view({'delete': 'destroy'})),
    path('cover/product/create/', views.CoverCreateUpdateViewSet.as_view({'post': 'create'})),
    path('covers/products/list/', views.CoverListViewSet.as_view({'get': 'list'})),
    path('cover/product/detail/<int:pk>/', views.CoverRetrieveAPIView.as_view()),
    path('cover/product/update/<int:pk>/', views.CoverCreateUpdateViewSet.as_view({'put': 'update'})),
    path('cover/product/destroy/<int:pk>/', views.CoverDestroyViewSet.as_view({'delete': 'destroy'})),
]