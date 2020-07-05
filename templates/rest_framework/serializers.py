from rest_framework import serializers

from .models import User1, Activity_period1
"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('UserID', 'Real_name','tz','activity_period')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
class Actiity_PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity_period
        fields = ('start_time','end_time')

"""
"""
class Activity_PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity_period1 
        fields = ('start_time','end_time')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    activity_period = Activity_PeriodSerializer(many=False, read_only=True);

    class Meta:
        model = User1
        fields = ('UserID', 'Real_name','tz','activity_period');
"""

class Activity_periodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity_period1
        fields = ('start_time','end_time',)

        
class UserSerializer(serializers.ModelSerializer):

    activity_period = Activity_periodSerializer(many=True)
    
    class Meta:
        model = User1
        fields = '__all__'
        
    def create(self, validated_data):
        Activity_validated_data = validated_data.pop('activity_period')
        user = User1.objects.create(**validated_data)
        activity_period_serializer = self.fields['activity_period']
        for each in Activity_validated_data:
            each['user'] = user
        activities = activity_period_serializer.create(Activity_validated_data)
        return user 





