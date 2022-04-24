
from django.urls import path, include
from .views import article_list, article_details,  Userarticle_details
# from rest_framework.routers import DefaultRouter
from api import views




# router = DefaultRouter()
# router.register('article', articleViewset, basename = 'article')
# router.register('users', UserViewset)


urlpatterns = [
    # path('api/', include(router.urls)),
    path('article_list', views.article_list.as_view()),
    path('article_details/<int:id>/',views.article_details.as_view()),
    path(' Userarticle_details/<int:id>/',views. Userarticle_details.as_view())

   

    
  

    

   
    
]


 
    
   
