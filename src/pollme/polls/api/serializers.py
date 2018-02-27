
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

from ..models import Question, Choice

class QuestionListSerializer(ModelSerializer):
    """
    This serializer serializes the Question model
    It should also include a field "choices" that will serialize all the
        choices for a question
    You well need a SerializerMethodField for choices,
        http://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    Reference this stack overflow for the choices:
        https://stackoverflow.com/questions/33945148/return-nested-serializer-in-serializer-method-field
    """
    choices = SerializerMethodField()

    def get_choices(self, obj):
        choices = obj.choice_set.all()
        return ChoiceSerailizer(choices, many=True).data

    class Meta:
        model = Polls
        fields = ('id', 'text', 'pub_data', 'choices')


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Question.objects.create(**validated_data)




class ChoiceSerializer(ModelSerializer):
    """
    This serializes the Choice model
    """
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Choice.objects.create(**validated_data)

    class Meta:
        model = Polls
        fields = ["choice_text","votes"]
