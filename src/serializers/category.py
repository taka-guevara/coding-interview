from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # json で出力するフィールド
        fields = ('id','company', 'parent_category','created_at','updated_at')