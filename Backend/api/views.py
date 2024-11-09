from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializers,NoteSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Note

#listapiview do both create record and list all the records
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]  #notes only access by the authorized person or loged in person can see there notes only
    
    #it will return the note written by the authorized person
    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)
    
    #it check all the fields are filled correctly 
    def perform_create(self,serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)# then we are saving it but the author is saving mannualy because we give read only premission
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class=NoteSerializer    
    permission_classes=[IsAuthenticated]

    #it will delete the note written by the authorized person
    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    permission_classes=[AllowAny]