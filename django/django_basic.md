# jangogirls

<h6><참조> : [](https://tutorial.djangogirls.org/ko/django_models/)[들어가며 · HonKit](https://tutorial.djangogirls.org/ko/)</h6>

# 가상환경(Venv)

- 프로젝트 기초 전부를 Python/Django와 분리해줌
- 즉, 웹사이트가 변경되어도 개발 중인 것에 영향을 주지 않는다는 것

## 가상환경만들기

- command line
  
  `C:\\Users\\Name\\djangogirls> C:\\Python35\\python -m venv myvenv`

## 가상환경 사용하기

- command-line

- 가상환경 활성화시키기
  
  `C:\\Users\\Name\\djangogirls> myvenv\\Scripts\\activate`

- 접두어에 myvenv가 없다면 활성화시켜야 함

# 프로젝트 시작하기

## 1. 스크립트 실행

- 장고의 기본 골격 만들기
- 디렉토리와 파일명은 변경, 이동 금지
- command-line

```python
(myvenv) C:\\Users\\Name\\djangogirls> django-admin.py startproject mysite .
```

- ModuleNotFoundError 발생
- django-admin은 명령어이기 때문에 .py를 빼야 한다.

```python
(myvenv) C:\\Users\\Name\\djangogirls> django-admin startproject mysite 
```

- 디렉토리 구조

```python
djangogirls
├───manage.py # 사이트 관리를 도와주는 역할
└───mysite
        settings.py  # 웹사이트 설정이 있는 파일
        urls.py   # urlresolver가 사용하는 패턴 목록을 포함
        wsgi.py
        __init__.py
```

## 2. 설정 변경

- 웹사이트 시간대 변경

```python
TIME_ZONE = 'Asia/Seoul'
```

- 정적파일 경로

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

- 애플리케이션을 배포 시 PythonAnywhere 호스트 이름과 일치시키기

```python
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
```

## 3. 데이터베이스 설정하기

- `sqlite3`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

- 블로그에 데이터베이스 생성하기
  
  - `python [manage.py](<http://manage.py/>) migrate`

- 웹 서버 작동시키기
  
  - `(myvenv) ~/djangogirls$ python manage.py runserver`
  - browser
    - `http://127.0.0.1:8000/`

- 웹서버가 실행되는 동안 프롬프트에 추가 명령 실행되지 않음

- 웹 서버가 들어오는 요청을 수신 대기

- ## 웹 서버가 실행되는 동안 추가 명령하기

> > 새 터미널 열고 `venv` 활성화시키기

- 웹 서버 중지

> > 실행중인 창에서 ctrl + c

---

# 장고 모델

- 블로그 글을 위한 장고 모델 만들기
- SQLite 데이터 베이스 사용
  - 기본 장고 데이터베이스 어뎁터
  - 데이터베이스 안의 모델이란, 엑셀 스프레드시트같은 느낌

## 1. 어플리케이션 만들기

- 잘 정돈된 상태에서 시작하기 위해, 프로젝트 내부에 별도의 어플리케이션 만들기
  
  - command line
  
  - `(myvenv) ~/djangogirls$ python manage.py startapp blog`
  
  - 디렉토리 구조
    
    ```python
    djangogirls
        ├── mysite
        |       __init__.py
        |       settings.py
        |       urls.py
        |       wsgi.py
        ├── manage.py
        └── blog
            ├── migrations
            |       __init__.py
            ├── __init__.py
            ├── admin.py
            ├── models.py
            ├── tests.py
            └── views.py
    ```
  
  - 앱 생성 후, 장고에서 사용해야한다고 알리기
    
    ```python
    # mysite/settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',  # blog 추가
    ]
    ```

## 2. 블로그 글 모델 만들기

- 모든 `model`객체는 `blog/models.py`파일에서 선언하여 모델을 만듬

- 이 파일에 우리의 블로그 글 모델도 정의할 예정

- `blog/models.py`파일열어서 모든 내용 삭제 후 아래 코드 추가
  
  ```python
  from django.conf import settings
  from django.db import models
  from django.utils import timezone
  
  # Post클래스를 장고모델로 정의.
  # 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됨
  class Post(models.Model): 
      author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      title = models.CharField(max_length=200)
      text = models.TextField()
      created_date = models.DateTimeField(
              default=timezone.now)
      published_date = models.DateTimeField(
              blank=True, null=True)
  
      def publish(self):
          self.published_date = timezone.now()
          self.save()
      def __str__(self):
          return self.title
  ```
  
  - `models.CharField` : 글자 수가 제한된 텍스트를 정의할 때 사용
  - `models.TextField` : 글자 수에 제한이 없는 긴 텍스트를 위한 속성(블로그 콘텐츠를 담기 좋음)
  - `models.DateTimeField` : 날짜와 시간을 의미
  - `models.ForeignKey` : 다른 모델에 대한 링크를 의미

## 3. 데이터베이스에 모델을 위한 테이블 만들기

### 데이터베이스에 우리의 새 모델, Post모델을 추가하기

1. 장고모델에 방금 만들 클래스를 알려주기
   - `(myvenv) ~/djangogirls$ python manage.py makemigrations blog`
   - 장고가 데이터베이스에 지금 반영될 수 있도록 마이그레이션파일을 준비해 뒀음.
2. 실제 데이터베이스에 모델추가를 반영하기
   - `(myvenv) ~/djangogirls$ python manage.py migrate blog`

---

# 장고 관리자

- 방금 모델링 한 글들을 장고 관리자에서 추가, 수정, 삭제하기

- `blog/admin.py` 파일 열어서 아래 코드 추가
  
  ```python
  # blog/admin.py
  
  from django.contrib import admin
  from .models import Post # Post룰 가져옴
  
  admin.site.register(Post)
  ```
  
  - 관리자 페이지에서 만든 모델을 보려면 `admin.site.register(Post)`로 모델을 등록해야 함.

## 1. superuser 생성하기

- `python [manage.py](<http://manage.py>) runserver` 이후 [](http://127.0.0.1:8000/admin/)http://127.0.0.1:8000/admin/로 접속하면 로그인 페이지가 뜸
- 모든 권한을 가지는 슈퍼 사용자를 생성해야 함
  - `(myvenv) ~/djangogirls$ python manage.py createsuperuser`
  - 사용자명, 이메일, 패스워드 작성하기# jangogirls
    
    <h6><참조> : [](https://tutorial.djangogirls.org/ko/django_models/)[들어가며 · HonKit](https://tutorial.djangogirls.org/ko/)</h6>
    
    # 가상환경(Venv)
    - 프로젝트 기초 전부를 Python/Django와 분리해줌
    - 즉, 웹사이트가 변경되어도 개발 중인 것에 영향을 주지 않는다는 것
    
    ## 가상환경만들기
    
    - command line
      
      `C:\\Users\\Name\\djangogirls> C:\\Python35\\python -m venv myvenv`
    
    ## 가상환경 사용하기
    
    - command-line
    
    - 가상환경 활성화시키기
      
      `C:\\Users\\Name\\djangogirls> myvenv\\Scripts\\activate`
    
    - 접두어에 myvenv가 없다면 활성화시켜야 함
    
    # 프로젝트 시작하기
    
    ## 1. 스크립트 실행
    
    - 장고의 기본 골격 만들기
    - 디렉토리와 파일명은 변경, 이동 금지
    - command-line
    
    ```python
    (myvenv) C:\\Users\\Name\\djangogirls> django-admin.py startproject mysite .
    ```
    
    - ModuleNotFoundError 발생
    - django-admin은 명령어이기 때문에 .py를 빼야 한다.
    
    ```python
    (myvenv) C:\\Users\\Name\\djangogirls> django-admin startproject mysite 
    ```
    
    - 디렉토리 구조
    
    ```python
    djangogirls
    ├───manage.py # 사이트 관리를 도와주는 역할
    └───mysite
            settings.py  # 웹사이트 설정이 있는 파일
            urls.py   # urlresolver가 사용하는 패턴 목록을 포함
            wsgi.py
            __init__.py
    ```
    
    ## 2. 설정 변경
    
    - 웹사이트 시간대 변경
    
    ```python
    TIME_ZONE = 'Asia/Seoul'
    ```
    
    - 정적파일 경로
    
    ```python
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    ```
    
    - 애플리케이션을 배포 시 PythonAnywhere 호스트 이름과 일치시키기
    
    ```python
    ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
    ```
    
    ## 3. 데이터베이스 설정하기
    
    - `sqlite3`
    
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    ```
    
    - 블로그에 데이터베이스 생성하기
      
      - `python [manage.py](<http://manage.py/>) migrate`
    
    - 웹 서버 작동시키기
      
      - `(myvenv) ~/djangogirls$ python manage.py runserver`
      - browser
        - `http://127.0.0.1:8000/`
    
    - 웹서버가 실행되는 동안 프롬프트에 추가 명령 실행되지 않음
    
    - 웹 서버가 들어오는 요청을 수신 대기
    
    - ## 웹 서버가 실행되는 동안 추가 명령하기
    
    > > 새 터미널 열고 `venv` 활성화시키기
    
    - 웹 서버 중지
    
    > > 실행중인 창에서 ctrl + c
    
    ---
    
    # 장고 모델
    
    - 블로그 글을 위한 장고 모델 만들기
    - SQLite 데이터 베이스 사용
      - 기본 장고 데이터베이스 어뎁터
      - 데이터베이스 안의 모델이란, 엑셀 스프레드시트같은 느낌
    
    ## 1. 어플리케이션 만들기
    
    - 잘 정돈된 상태에서 시작하기 위해, 프로젝트 내부에 별도의 어플리케이션 만들기
      
      - command line
      
      - `(myvenv) ~/djangogirls$ python manage.py startapp blog`
      
      - 디렉토리 구조
        
        ```python
        djangogirls
            ├── mysite
            |       __init__.py
            |       settings.py
            |       urls.py
            |       wsgi.py
            ├── manage.py
            └── blog
                ├── migrations
                |       __init__.py
                ├── __init__.py
                ├── admin.py
                ├── models.py
                ├── tests.py
                └── views.py
        ```
      
      - 앱 생성 후, 장고에서 사용해야한다고 알리기
        
        ```python
        # mysite/settings.py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'blog',  # blog 추가
        ]
        ```
    
    ## 2. 블로그 글 모델 만들기
    
    - 모든 `model`객체는 `blog/models.py`파일에서 선언하여 모델을 만듬
    
    - 이 파일에 우리의 블로그 글 모델도 정의할 예정
    
    - `blog/models.py`파일열어서 모든 내용 삭제 후 아래 코드 추가
      
      ```python
      from django.conf import settings
      from django.db import models
      from django.utils import timezone
      
      # Post클래스를 장고모델로 정의.
      # 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됨
      class Post(models.Model): 
          author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
          title = models.CharField(max_length=200)
          text = models.TextField()
          created_date = models.DateTimeField(
                  default=timezone.now)
          published_date = models.DateTimeField(
                  blank=True, null=True)
      
          def publish(self):
              self.published_date = timezone.now()
              self.save()
          def __str__(self):
              return self.title
      ```
      
      - `models.CharField` : 글자 수가 제한된 텍스트를 정의할 때 사용
      - `models.TextField` : 글자 수에 제한이 없는 긴 텍스트를 위한 속성(블로그 콘텐츠를 담기 좋음)
      - `models.DateTimeField` : 날짜와 시간을 의미
      - `models.ForeignKey` : 다른 모델에 대한 링크를 의미
    
    ## 3. 데이터베이스에 모델을 위한 테이블 만들기
    
    ### 데이터베이스에 우리의 새 모델, Post모델을 추가하기
    
    1. 장고모델에 방금 만들 클래스를 알려주기
       - `(myvenv) ~/djangogirls$ python manage.py makemigrations blog`
       - 장고가 데이터베이스에 지금 반영될 수 있도록 마이그레이션파일을 준비해 뒀음.
    2. 실제 데이터베이스에 모델추가를 반영하기
       - `(myvenv) ~/djangogirls$ python manage.py migrate blog`
    
    ---
    
    # 장고 관리자
    
    - 방금 모델링 한 글들을 장고 관리자에서 추가, 수정, 삭제하기
    
    - `blog/admin.py` 파일 열어서 아래 코드 추가
      
      ```python
      # blog/admin.py
      
      from django.contrib import admin
      from .models import Post # Post룰 가져옴
      
      admin.site.register(Post)
      ```
      
      - 관리자 페이지에서 만든 모델을 보려면 `admin.site.register(Post)`로 모델을 등록해야 함.
    
    ## 1. superuser 생성하기
    
    - `python [manage.py](<http://manage.py>) runserver` 이후 [](http://127.0.0.1:8000/admin/)http://127.0.0.1:8000/admin/로 접속하면 로그인 페이지가 뜸
    - 모든 권한을 가지는 슈퍼 사용자를 생성해야 함
      - `(myvenv) ~/djangogirls$ python manage.py createsuperuser`
      - 사용자명, 이메일, 패스워드 작성하기
