from django.shortcuts import render
from rest_framework.views import APIView    # settings.py 맨 윗줄에 앱 등록

class Main(APIView):    # Main이라는 클래스를 get으로 실행하면 main.html 실행
    def get(self, request):
        return render(request, 'insta_pjt/main.html')

