from rest_framework import serializers
from notes_api import models


class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.NotesTry1
        fields = ["id", "title", "content"]

    # def create(self, validated_data):
    #     return models.NotesTry1.objects.create(**validated_data)


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Comment1
#         field = ["notes_id", "content"]
