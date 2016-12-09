from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile, Testimonial


class TestimonialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testimonial
        fields = (
           'id',
           'owner',
           'recipient',
           'quote', 
        )
        read_only_fields = ('owner',)

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
           'about',
           'image',
           'facebook',
           'instagram',
           'snapchat',
           'pinterest',
           'twitter',
           'linkedin',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = (
           'username',
           'first_name',
           'last_name', 
           'email', 
           'profile',
        )

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user_data = validated_data
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(owner=user,**profile_data) 
        return user

    def update(self, user,validated_data, *args):
        profile_data = validated_data.pop('profile')
        user_data = validated_data
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.email = user_data['email']
        user.save()
#        User.objects.update(**user_data)
#        User.objects.update(pk=user.pk, **user_data)
        profile = Profile.objects.update(owner=user,**profile_data) 
        return user

