from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..models.category import Category
from ..models.company import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name')

class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class CategorySerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    parent_category = ParentCategorySerializer()

    class Meta:
        model = Category
        fields = ('id','name', 'company', 'parent_category','created_at','updated_at')
