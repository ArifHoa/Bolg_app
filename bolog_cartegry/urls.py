from django.urls import path
from .import views 

urlpatterns = [
    
    path('post-pag1',views.post_pag1, name='post_pag1'),
    path('post-pag2',views.post_pag2, name='post_pag2'),
    path('post-pag3',views.post_pag3, name='post_pag3'),
    path('post-pag4',views.post_pag4, name='post_pag4'),
    path('post-pag5',views.post_pag5, name='post_pag5'),
    path('post-pag6',views.post_pag6, name='post_pag6'),
    path('post-pag7',views.post_pag7, name='post_pag7'),
    path('post-pag8',views.post_pag8, name='post_pag8'),
    path('post-pag9',views.post_pag9, name='post_pag9'),
    path('post-pag10',views.post_pag10, name='post_pag10'),
    path('post-pag11',views.post_pag11, name='post_pag11'),
  
  
]