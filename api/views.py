from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST','GET'])
    def rate_movie(self, request, pk=None):
        response = dict()
        status_code = status.HTTP_200_OK
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': "Rating updated: {}".format(serializer.data)}
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': "Rating created: {}".format(serializer.data)}
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {'message': "you need to provide stars"}
        return Response(response, status=status_code)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        status_code = status.HTTP_400_BAD_REQUEST
        response = {'message': "You can't create rating like that"}
        return Response(response, status=status_code)

    def update(self, request, *args, **kwargs):
        status_code = status.HTTP_400_BAD_REQUEST
        response = {'message': "You can't update rating like that"}
        return Response(response, status=status_code)
