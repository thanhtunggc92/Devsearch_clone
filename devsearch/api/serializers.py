from rest_framework import serializers
from projects import models
from users.models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Tags
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Reviews
        fields = '__all__'
class ProjectSerializers(serializers.ModelSerializer):
    owner = ProfileSerializer(many =False)
    tags = TagsSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    
    class Meta:
   

        model = models.Project
        fields = '__all__'

    def get_reviews(self,obj):
        reviews = obj.reviews_set.all()
        serializer = ReviewSerializer(reviews, many = True)

        return serializer.data

