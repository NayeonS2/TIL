# Database

## Many to many relationship

### M:N
- Many-to-many relationships
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
- 양쪽 모두에서 N:1 관계를 가짐

---

## Intro
### 개요
- 병원에 내원하는 환자와 의사의 예약 시스템을 구축하라는 업무를 지시 받음
  - 필요한 데이터 베이스 모델을 고민해보고 모델링 진행하기
  - 모델링을 하는 이유는 현실 세계를 최대한 유사하게 반영하기 위함
- 무엇부터 고민해야 할까?
  - 병원 시스템에서 가장 핵심이 되는 것은? -> 의사와 환자
  - 이 둘의 관계를 어떻게 표현할 수 있을까?
- 우리 일상에 가까운 예시를 통해 DB를 모델링하고 그 내부에서 일어나는 데이터의 흐름을 어떻게 제어할 수 있을지 고민해보기

> [참고] 데이터 모델링
- 주어진 개념으로부터 논리적인 데이터 모델을 구성하는 작업
- 물리적인 데이터베이스 모델로 만들어 고객의 요구에 따라 특정 정보 시스템의 데이터베이스에 반영하는 작업


### 용어 정리
- target model
  - 관계 필드를 가지지 않은 모델
  - N:1 관계인 Comment-Article 에서 Article
- source model
  - 관계 필드를 가진 모델
  - N:1 관계인 Comment-Article 에서 Comment

### N:1의 한계
- 의사와 환자간 예약 시스템을 구현
- 지금까지 배운 N:1 관계를 생각해 한 명의 의사에게 여러 환자가 예약할 수 있다고 모델 관계를 설정

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```
- Migration 진행 및 shell_plus 실행
```python
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py shell_plus
```

- 각각 2명의 의사와 환자를 생성하고 환자는 서로 다른 의사에게 예약을 했다고 가정
```python
doctor1 = Doctor.objects.create(name='alice')
doctor2 = Doctor.objects.create(name='bella')
patient1 = Patient.objects.create(name='carol', doctor=doctor1)
patient2 = Patient.objects.create(name='dane', doctor=doctor2)
```

- 1번 환자(carol)가 두 의사 모두에게 방문하려고 함
```python
patient3 = Patient.objects.create(name='carol', doctor=doctor2)
```
- 동시에 예약할 수 는 없을까?
```python
patient4 = Patient.objects.create(name='carol', doctor=doctor1, doctor2) # error!
```
- 동일 환자지만 다른 의사에게 예약하려면 객체를 하나 더 만들어서 예약 진행해야함
- 새로운 환자 객체를 생성할 수 밖에 없음
- 외래 키 컬럼에 '1,2'형태로 참조하는 것은 Integer 타입이 아니기 때문에 불가능
- 그렇다면 "예약 테이블을 따로 만들자"

### 중개 모델
- 환자 모델의 외래키를 삭제하고 별도의 예약 모델을 새로 작성
- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐

```python
# 외래키 삭제
class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# 중개모델 작성
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```
- 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
  - migration 파일 삭제
  - 데이터베이스 파일 삭제
```python
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py shell_plus
```
- 의사와 환자 생성 후 예약 만들기
```python
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')

Reservation.objects.create(doctor=doctor1, patient=patient1)
```
- 예약 정보 조회
```python
# 의사 -> 예약 정보 찾기
doctor1.reservation_set.all()

# 환자 -> 예약 정보 찾기
patient1.reservation_set.all()
```

- 1번 의사에게 새로운 환자 예약이 생성 된다면
```python
patient2 = Patient.objects.create(name='dane')

Reservation.objects.create(doctor=doctor1, patient=patient2)
```

- 1번 의사의 예약 정보 조회
```python
# 의사 -> 환자 목록
doctor1.reservation_set.all()
```
---
### Django ManyToManyField
- 환자 모델에 Django ManyToManyField 작성
```python
class Patient(models.Model):
    # 환자가 의사를 참조
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

    # Reservation Class 주석 처리
```
- 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
  - migration 파일 삭제
  - 데이터베이스 파일 삭제
```python
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py shell_plus
```
- 생성된 중개 테이블 hospitals_patient_doctors 확인

- 의사 1명과 환자 2명 생성
```python
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='dane')
```
- 예약 생성(환자가 의사에게 예약)
```python
# patient1이 doctor1에게 예약
patient1.doctors.add(doctor1)

# patient1 - 자신이 예약한 의사목록 확인
patient1.doctors.all()

# doctor1 - 자신의 예약된 환자목록 확인
doctor1.patient_set.all()
```

- 예약 생성(의사가 환자를 예약)
```python
# doctor1이 patient2를 예약
doctor1.patient_set.add(patient2)

# doctor1 - 자신의 예약 환자목록 확인
doctor1.patient_set.all()

# patient1,2 - 자신이 예약한 의사목록 확인
patient1.doctors.all()
patient2.doctors.all()
```

- 예약 취소하기(삭제)
- 기존에는 해당하는 Reservation을 찾아서 지워야 했다면, 이제는 .remove() 사용
```python
# doctor1이 patient1 진료 예약 취소
doctor1.patient_set.remove(patient1)

doctor1.patient_set.all()

patient1.doctors.all()

# patient2가 doctor1 진료 예약 취소
patient2.doctors.remove(doctor1)

patient2.doctors.all()

doctor1.patient_set.all()
```
- Django는 ManyToManyField를 통해 중개 테이블을 자동으로 생성함

### 'related_name' argument
- target model이 source model을 참조할 때 사용할 manager name
- ForeignKey()의 related_name과 동일
```python

class Patient(models.Model):
   
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```
- Migration 진행 및 shell_plus 실행
```python
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py shell_plus
```

- related_name 설정 값 확인하기

```python
# 1번 의사 조회하기
doctor1 = Doctor.objects.get(pk=1)

# 에러 발생 (related_name을 설정하면 기존 _set manager는 사용 불가)
doctor1.patient_set.all()

# 변경 후
doctor1.patients.all()
```
### 'through' argument
- 그렇다면 중개 모델을 직접 작성하는 경우는 없을까?
- 중개 테이블을 수동으로 지정하려는 경우 through 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정 가능
- 가장 일반적인 용도는 **중개테이블에 추가 데이터를 사용**해 다대다 관계와 연결하려는 경우

- through 설정 및 Reservation Class 수정
- 이제는 예약 정보에 증상과 예약일이라는 추가데이터가 생김
```python
class Patient(models.Model):
    # 환자가 의사를 참조
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')    # 편한곳에 생성하면 됨!
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```
- 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
  - migration 파일 삭제
  - 데이터베이스 파일 삭제
```python
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py shell_plus
```

- 의사 1명과 환자 2명 생성
```python
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='dane')
```
- 예약 생성 1
```python
# 1. Reservagion 클래스를 통한 예약 생성
reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
reservation1.save()

doctor1.patient_set.all()

patient1.doctors.all()
```
- 예약 생성 2

```python
# 2. Patient 객체를 통한 예약 생성

# through_defaults 값에 딕셔너리 타입으로 입력
patient2.doctors.add(doctor1, through_defaults={'symptom':'flu'})

doctor1.patient_set.all()

patient2.doctors.all()
```
- 예약 삭제

```python
doctor1.patient_set.remove(patient1)

patient2.doctors.remove(doctor1)
```

### 정리
- M:N 관계로 맺어진 두 테이블에는 변화가 없음
- Django의 ManyToManyField는 중개 테이블을 자동으로 생성함
- Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
- 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
- N:1은 완전한 종속의 관계였지만 M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 두가지 형태로 모두 표현이 가능한 것

---

## ManyToManyField

### ManyToManyField란
- ManyToManyField(to, **options)
- 다대다 (M:N, many-to-many) 관계 설정 시 사용하는 모델 필드
- 하나의 필수 위치인자 (M:N 관계로 설정할 모델 클래스)가 필요
- 모델 필드의 RelatedManger를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있음
  - add(), remove(), create(), clear()...

### 데이터베이스에서의 표현
- Django는 다대다 관계를 나타내는 중개 테이블을 만듦
- 테이블 이름은 ManyToManyField 이름과 이를 포함하는 모델의 테이블 이름을 조합하여 생성됨
- 'db_table' arguments을 사용하여 중개 테이블의 이름 변경 가능

### ManyToManyField's Arguments
1. related_name
2. through
3. symmetrical

### related_name
- target model이 source model을 참조할 때 사용할 manager name
- ForeignKey의 related_name과 동일

### through
- 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정
- 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우(extra data with a many-to-many relationship)에 사용됨

### symmetrical
- 기본값 : True
- ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
```python
class Person(models.Model):
    friends = models.ManyToManyField('self')
    # friends = models.ManyToManyField('self', symmetrical=False)
```
- True일 경우
  - _set 매니저를 추가하지 않음
  - source 모델의 인스턴스가 target모델의 인스턴스를 참조하면 자동으로 target모델 인스턴스도 source모델 인스턴스를 자동으로 참조하도록 함 (대칭)
  - 즉, 내가 당신의 친구라면 당신도 내 친구가 됨
- 대칭을 원하지 않는 경우 False로 설정
  - Follow 기능 구현에서 다시 확인 예정

### Related Manager
- N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조시에 사용할 수 있는 manager를 생성
  - 우리가 이전에 모델 생성 시 objects라는 매니저를 통해 queryset api를 사용했던 것 처럼
  - related maanger를 통해 queryset api를 사용할 수 있게 됨
- 같은 이름의 메서드여도 각 관계(N:1, M:N)에 따라 다르게 사용 및 동작됨
  - N:1에서는 target모델 객체만 사용 가능
  - **M:N 관계에서는 관련된 두 객체에서 모두 사용 가능**
- 메서드 종류
  - **add(), remove(),** create(), clear(), set() 등


### methods
- add()
  - "지정된 객체를 관련 객체 집합에 추가"
  - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
  - 모델 인스턴스, 필드 값(pk)을 인자로 허용
- remove()
  - "관련 객체 집합에서 지정된 모델 개체를 제거"
  - 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨
  - 모델 인스턴스, 필드 값(pk)을 인자로 허용

### 중개 테이블 필드 생성 규칙
- source 모델 및 target 모델이 다른 경우
  - id
  - <containing_model>_id
  - <other_model>_id
- ManyToManyField가 동일한 모델을 가리키는 경우
  - id
  - from_<model>_id
  - to_<model>_id

---

## M:N (Article-User)
### 개요
- Article과 User의 M:N 관계 설정을 통한 좋아요 기능 구현하기

## LIKE
### 모델 관계 설정
- ManyToManyField 작성

```python
from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
- Migration 진행 후 에러 확인

- like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성됨
- 그러나 이전 N:1(Article-User)관계에서 이미 해당 매니저를 사용 중
  - user.article_set.all() -> 해당 유저가 작성한 모든 게시글 조회
  - **user가 작성한 글들 (user.article_set)과**
  - **user가 좋아요를 누른 글(user.article_set)을 구분할 수 없게 됨**
- user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 함

- ManyToManyField에 related_name 작성 후 Migration
```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
- 생성된 중개 테이블 확인
  - articles_article_like_users
    - id
    - article_id
    - user_id

- User - Article 간 사용 가능한 related_manager 정리
  - article.user
    - 게시글을 작성한 유저 - N:1
  - user.article_set
    - 유저가 작성한 게시글(역참조) - N:1
  - article.like_users
    - 게시글을 좋아요한 유저 - M:N
  - user.like_articles
    - 유저가 좋아요한 게시글(역참조) - M:N

### LIKE 구현
- url 및 view 함수 작성
```python
# articles/urls.py
from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    # path('<int:comment_pk>/comments/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]

# articles/views.py
@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)

        # 좋아요 추가할지 취소할지 무슨 기준으로 if문을 작성할까?
        # 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지를 확인
        # if request.user in article.like_users.all():
        
        # 현재 게시글에 좋아요를 누른 유저중에 현재 좋아요를 요청하는 유저를 검색해서 존재하는지를 확인 
        if article.like_users.filter(pk=request.user.pk).exists():  # get은 결과값이 없으면 에러가 나지만, filter는 빈값이 출력되므로 filter사용!
            # 좋아요 취소 (remove)
            article.like_users.remove(request.user)
        else:
            # 좋아요 추가 (add)
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
```

> [참고] .exists()
- QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
- 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

- index 템플릿에서 각 게시글에 좋아요 버튼 출력하기

```html
<!--articles/index.html-->
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">CREATE</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>
      <!--게시물 작성자의 username!-->
      <b>작성자 : <a href="{% url 'accounts:profile' article.user %}">{{ article.user }}</a></b>  
    </p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <div>
      <form action="{% url 'articles:likes' article.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <input type="submit" value="좋아요 취소">
        {% else %}
          <input type="submit" value="좋아요">
        {% endif %}
      </form>
    </div>
    <a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
    <hr>
  {% endfor %}
{% endblock content %}
```
---

## M:N (User-User)

### 개요
- User 자기 자신과의 M:N 관계 설정을 통한 팔로우 기능 구현하기

## Profile
### 개요
- 자연스러운 follow 흐름을 위한 프로필 페이지를 먼저 작성

### Profile 구현
- url 및 view 함수 작성

```python
# accounts/urls.py
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]

# accounts/views.py
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

- profile 템플릿 작성
```html
<!--accounts/profile.html-->
{% extends 'base.html' %}


{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    팔로워 : {{ person.followers.all|length }} / 팔로잉 : {{ person.followings.all|length }}
  </div>


  {% if request.user != person %}
  <div>
    <form action="{% url 'accounts:follow' person.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <input type="submit" value="언팔로우">
      {% else %}
        <input type="submit" value="팔로우">
      {% endif %}
    </form>
  <div>
  {% endif %}

  <h2>{{ person.username }}이 작성한 모든 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}이 작성한 모든 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}이 좋아요 한 모든 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <a href="{% url 'articles:index' %}">back</a>

{% endblock content %}
```

- Profile 템플릿으로 이동가능한 하이퍼링크 작성
```html
<!--base.html-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">  <title>Document</title>
</head>
<body>
  <div class="container">
    {% if request.user.is_authenticated %}
      <h3>{{ user }}</h3>
      <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
      </form>
      <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원탈퇴">
      </form>
      <a href="{% url 'accounts:update' %}">회원정보수정</a>
    {% else %}
      <a href="{% url 'accounts:login' %}">Login</a>
      <a href="{% url 'accounts:signup' %}">Signup</a>
    {% endif %}
    <hr>
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>


<!--articles/index.html-->
<p>
    <!--게시물 작성자의 username!-->
    <b>작성자 : <a href="{% url 'accounts:profile' article.user %}">{{ article.user }}</a></b>  
</p>
```

---
## Follow
### 모델 관계 설정
- ManyToManyField 작성 및 Migration 진행
```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 대체한 이유 -> 커스텀을 하기위해!
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')    # 참조할때는 followings/ 역참조는 followers
    # 'self'인자(유저와 유저간의 관계) 는 대댓글 구현에도 쓰임!
```

- 생성된 중개 테이블 확인
  - accounts_user_followings
    - id
    - from_user_id
    - to_user_id

- url 및 view 함수 작성
```python
# accounts/urls.py
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]


# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            # 내가(request.user) 그 사람의 팔로워 목록에 있다면
            # if me in you.followers.all():
            if you.followers.filter(pk=me.pk).exists():
                # 언팔로우
                you.followers.remove(me)
            else:
                # 팔로우
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

- 프로필 유저의 팔로잉, 팔로워 수 & 팔로우,언팔로우 버튼 작성
```html
<!--accounts/profile.html-->
{% extends 'base.html' %}


{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    팔로워 : {{ person.followers.all|length }} / 팔로잉 : {{ person.followings.all|length }}
  </div>


  {% if request.user != person %}
  <div>
    <form action="{% url 'accounts:follow' person.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <input type="submit" value="언팔로우">
      {% else %}
        <input type="submit" value="팔로우">
      {% endif %}
    </form>
  <div>
  {% endif %}

  <h2>{{ person.username }}이 작성한 모든 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}이 작성한 모든 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}이 좋아요 한 모든 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <a href="{% url 'articles:index' %}">back</a>

{% endblock content %}
```

---

## SUMMARY

- Many-to-many relationship
  - ManyToManyField()
- M:N (Article-User)
  - Like
- M:N (User-User)
  - Profile
  - Follow


---


## Fixtures

### 개요
- Fixtures를 사용해 모델에 초기 데이터 제공하는 방법

### 초기 데이터의 필요성
- Django 프로젝트의 앱을 처음 설정할 때 동일하게 준비 된 데이터로 데이터베이스를 미리 채우는 것이 필요한 순간이 있음
- Django에서는 fixtures를 사용해 앱에 초기 데이터(initial data)를 제공 가능
- 즉, migrations와 fixtures를 사용하여 data와 구조를 공유하게 됨

## Providing data with fixtures

### 사전 준비
- 유저, 게시글, 댓글 좋아요 등 각 데이터를 최소 2개 이상 생성해두기

### fixtures
- Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
  - 가져오는 방법을 알고 있다?
    - Django가 직접 만들기 때문에 데이터베이스 구조에 맞추어 작성 되어있음

### fixtures 기본 경로
- app_name/fixtures
- Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾는다

### fixtures 생성 및 로드
- 생성 (추출)
  - dumpdata
- 로드 (불러오기)
  - loaddata

### dumpdata
- 응용 프로그램과 관련된 데이터베이스의 모든 데이터를 표준 출력으로 출력
- 여러 모델을 하나의 json 파일로 만들 수 있음
```python
# 작성 예시
$ python manage.py dumpdata [[app_name[.ModelName]] [app_name[.ModelName] ...]] > {filename}.json
```
- manage.py와 동일한 위치에 data가 담긴 articles.json 파일이 생성됨
- dumpdata의 출력 결과물은 loaddata의 입력으로 사용됨
```python
$ python manage.py dumpdata --indent 4 articles.article > articles.json
```

### loaddata
- migrate 먼저!
- fixtures의 내용을 검색하여 데이터베이스 로드
```python
$ python manage.py loaddata articles.json comments.json users.json
```
- 한번에 로드할땐 순서 상관없지만, 따로따로 할땐 순서 중요! (모델 관계 때문)
- 외래키가 없는 users를 가장 먼저! -> articles -> comments 순서로

---
## Improve Query
### 개요
- Query를 개선하는 방법
  - annotate
  - select_related (1:1 or N:1 참조관계)
  - prefetch_related (1:1 or N:1 역참조관계)

### annotate
```python
from django.shortcuts import render
from .models import Article, Comment
from django.db.models import Count

# Create your views here.
def index_1(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.annotate(Count('comment')).order_by('-pk')   # 비슷한 쿼리를 한번에 계산
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_1.html', context)
```
```html
<!--index1.html-->
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% for article in articles %}
    <p>제목 : {{ article.title }}</p>
    {% comment %} <p>댓글개수 : {{ article.comment_set.count }}</p> {% endcomment %}
    <p>댓글개수 : {{ article.comment__count }}</p>
    <hr>
  {% endfor %}
{% endblock content %}
```

### select_related
```python
def index_2(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.select_related('user').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_2.html', context)
```

### prefetch_related
```python
def index_3(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_3.html', context)


from django.db.models import Prefetch

# 동시 적용
def index_4(request):
    # articles = Article.objects.order_by('-pk')
    # articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    articles = Article.objects.prefetch_related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)
```