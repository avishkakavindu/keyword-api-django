from rest_framework import serializers
from api.models import *


class AssignmentSerializer(serializers.ModelSerializer):
    available_days = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'subject', 'due_date', 'available_days']

    def get_available_days(self, obj):
        return obj.get_num_of_days


class UserSerializer(serializers.ModelSerializer):
    assignment_set = AssignmentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'assignment_set']

