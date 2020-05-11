from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from notes_api import models
from notes_api import serializers


# Create your views here.
class NoteViews(viewsets.ModelViewSet):
    serializer_class = serializers.NotesSerializers
    queryset = models.NotesTry1.objects.all()

    def get(self, request):
        """Return objects for the current authenticated user only"""
        return self.queryset

    def post(self, request):
        serializer = serializers.NotesSerializers(data=request.data)

        if serializer.is_valid():
            notes_saved = serializer.save()
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response({"success": "Notes '{}' created successfully".format(notes_saved.title)})
