from django.contrib.auth.models import User, Group
from rest_framework import permissions
from tutorial.quickstart.serializers import *
from tutorial.quickstart.models import *
from rest_framework.views import APIView
from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostView(viewsets.ModelViewSet):
    """
    API endpoint that allows post to be viewed, added, edited and deleted
    """
    #permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["post_text"]
    ordering_fields = ["pub_date", "author"]


class CommentView(viewsets.ModelViewSet):
    """
    API endpoint that allows comment to be viewed, added, edited and deleted
    """
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CategoryView(viewsets.ModelViewSet):
    """
       API endpoint that allows category to be viewed, added, edited and deleted
    """
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)