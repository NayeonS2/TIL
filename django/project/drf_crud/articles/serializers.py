from rest_framework import serializers
from .models import Article, Comment

# 여러 데이터의 정보를 보여줄 때 사용하는 serializer
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)


# 역참조 시 댓글 정보를 보여주기 위해 CommentSerializer 위치 이동
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)




# detail 한 내용을 보여주는 serializer 사용
# 생성, 수정을 할 때 모든 필드의 유효성 검사를 위해 사용
class ArticleSerializer(serializers.ModelSerializer):
    # related manager 이름을 필드명으로
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


