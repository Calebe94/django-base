from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['POST','GET'])
    def rate_movie(self, request, pk=None):
        response = dict()
        status_code = status.HTTP_200_OK
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            print(movie.title)
            response = {'message': "{}".format(movie.title)}
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {'message': "you need to provide stars"}
        return Response(response, status=status_code)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
