
from django.urls import path, include
from .views import articleViewset, UserViewset

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
 
#APIView
# from .views import article_list, article_details

#from function base
#article_list, article_details

router = DefaultRouter()
router.register('article', articleViewset, basename = 'article')
router.register('users', UserViewset)

urlpatterns = [
    path('api/', include(router.urls)),
   
    # path('auth', obtain_auth_token)
]



    # path('article/', article_list.as_view()),
    # path('article/<int:id>/', article_details.as_view()),


    # path('article/', article_list),
    # path('article/<int:pk>/', article_details),
    
    
   
