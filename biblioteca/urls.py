from django.urls import path
from biblioteca import views


app_name = 'biblioteca'


urlpatterns = [
    path('', views.LivroList.as_view(), name='list'),
    path('create/', views.LivroCreate.as_view(), name='create'),
    path('update/<int:pk>', views.LivroUpdate.as_view(), name='update'),
    path('detail/<int:pk>', views.LivroDetail.as_view(), name='detail'),
    path('delete/<int:pk>', views.LivroDelete.as_view(), name='delete'),
]