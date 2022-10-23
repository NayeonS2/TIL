from dataclasses import fields
from rest_framework import serializers
from .models import Actor, Movie, Review

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)




class ReviewTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)


class ActorNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):

    review_set = ReviewTitleSerializer(many=True, read_only=True)
    actors = ActorNameSerializer(many=True, read_only=True)


    class Meta:
        model = Movie
        fields = ('id','actors','review_set','title','overview','release_date','poster_path',)


class MovieTitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id','movie','title','content',)



class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ( 'id', 'name', )

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'movies', 'name',)


class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title', 'content',)






