from rest_framework import viewsets
from ..models.category import Category
from ..models.company import Company
from ..serializers.category import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = Category.objects.all()
    # シリアライザーを取得
    serializer_class = CategorySerializer