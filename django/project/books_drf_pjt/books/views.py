from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import serializers

from .serializers import BookListSerializer, BookSerializer, CommentSerializer
from .models import Book, Comment

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    if request.method == 'GET':
        books = get_list_or_404(Book)
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    # Q 2.
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):   # 데이터 유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    # 201 성공 응답 상태 코드
    
        


@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):
    book = get_object_or_404(Book,pk=book_pk)   # 조회대상 존재하지 않을때, 404 오류 응답 상태 코드 반환
    # Q 3.
    if request.method == 'GET':
        serializer = BookSerializer(book)
        res = serializer.data
        ans = {}
        for key,value in res.items():
            if key != 'comment_set':    # book_detail 함수는 title, content, created_at, updated_at , comment_count 정보만 반환
                ans[key] = value
        return Response(ans)
    
    # Q 4.
    elif request.method == 'DELETE':
        book.delete()
        return Response({'delete': f'{ book_pk }'}, status=status.HTTP_204_NO_CONTENT)  # key: 'delte', value: pk


    # Q 5.
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            res = serializer.data
            ans = {}
            for key,value in res.items():
                if key != 'comment_set':
                    ans[key] = value
            return Response(ans)
            #return Response(serializer.data)



@api_view(['GET'])
def comment_list(request):
    # Q 7.
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    res = serializer.data
    final = []
    
    for elem in res:
        ans = {}
        for key,value in elem.items():
            if key != 'book':   # comment_list 함수는 id,content,created_at,updated_at만 반환
                ans[key] = value
        final.append(ans)
    return Response(final)
    #return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, book_pk):
    # Q 8.
    book = get_object_or_404(Book,pk=book_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):   # 유효성 검사
        serializer.save(book=book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    # Q 9.
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    # Q 10.
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'delete': f'{ comment_pk }'}, status=status.HTTP_204_NO_CONTENT)

