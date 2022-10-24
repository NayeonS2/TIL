from rest_framework import serializers
from .models import Book, Comment


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title',) # book_list 함수는 게시글의 'title'정보를 반환


class BookTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title',)


class CommentSerializer(serializers.ModelSerializer):
    # Q 6.
    book = BookTitleSerializer(read_only=True)  # 댓글이 참조하고 있는 게시글 정보 (title)
    class Meta:
        model = Comment
        fields = ('book','id','content','created_at','updated_at',)
       


class BookSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
   

    # Q 11.
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Book

        #fields = '__all__'
        exclude = ('id',)   # book_detail 함수는 title, content, created_at, updated_at , comment_count 정보 반환
