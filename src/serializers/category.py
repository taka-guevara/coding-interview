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

    def create(self, validated_data):
        print(validated_data)
        c = Company.objects.get(name=validated_data["company"]["name"])
        p = Category.objects.get(name=validated_data["parent_category"]["name"])
        return Category.objects.create(
            name = validated_data["name"],
            company = c,
            parent_category = p
        )
    
    def update(self, instance, validated_data):
        print(validated_data)
        c = Company.objects.get(name=validated_data["company"]["name"])
        p = Category.objects.get(name=validated_data["parent_category"]["name"])
        instance.name = validated_data["name"]
        instance.company = c
        instance.parent_category = p

        return instance
