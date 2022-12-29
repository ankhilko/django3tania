
from rest_framework.serializers import ModelSerializer
from blog.models import Subject


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name',)

