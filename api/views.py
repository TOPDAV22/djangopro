
from .models import Article
from .serializers import ArticleSerializer


# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# from rest_framework.decorators import APIView
# from rest_framework import generics, mixins



from rest_framework import viewsets
# from django.shortcuts import get_object_or_404

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from django.contrib.auth.models import User
from .serializers import UserSerializer


class articleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer
    # authentication_classes = (TokenAuthentication, )


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# viewset mixins  ----> 

# class articleViewset(viewsets.GenericViewSet, mixins.ListModelMixin,
# mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
# mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# end --->

#class ViewSet -->
# class articleViewset(viewsets.ViewSet):
#     def list(self, request):
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)
#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

#     def destroy(self, request, pk=None):
#         article = Article.objects.get(pk=pk)

#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    #--end -->  




#class base APIview   --->
# class article_list(generics.GenericAPIView, mixins.ListModelMixin,
# mixins.CreateModelMixin):
      
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

    

#     def get (self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)

       


# class article_details(generics.GenericAPIView, mixins.RetrieveModelMixin,
# mixins.UpdateModelMixin, mixins.DestroyModelMixin):

#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'id'

    

#     def get(self, request, id):

#         return self.retrieve(request, id=id)

#     def put(self, request, id):
#         return self.update(request, id=id)

#     def delete(self, request, id):
#         return self.destroy(request, id=id )
  

  #end --->

        


   

#     class article_list(APIView): ---->

#     def get(self, request):
#         article = Article.objects.all() 
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)
    

#     def post(self, request):
#         serializer = ArticleSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_204_CREATE)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class article_details(APIView):     

#     def get_object(self, id):
#         try:
#             return  Article.objects.get(id=id)

#         except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get (self, request, id):
#         article = self.get_object(id) 
#         serializer = ArticleSerializer(article  )
#         return Response(serializer.data)


#     def put(self, request, id):
#         article = self.get_object(id) 
#         serializer = ArticleSerializer(article, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
            
#--->

# Create your views here.
#---->
# function bace views
# @api_view(['GET','POST'])
# def article_list(request):

#     if request.method =='GET':
#         article = Article.objects.all() 
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)


#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])

# def article_details(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method =="DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#end function base view  ---->
        




