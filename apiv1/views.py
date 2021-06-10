from os import setpriority
from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from shop.models import Book
from .serializers import BookSerializer



class BookViewSet(viewsets.ModelViewSet):
    """本モデルのCRUD用APIクラス"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]