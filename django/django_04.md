# Django 04

## The Django authentication system

- Django authentication system은 인증(Authentication)과 권한(Authorization)부여를 함께 제공(처리)하며, 이러한 기능이 어느정도 결합되어 일반적으로 인증 시스템이라고 함
- 필수 구성은 settings.py에 이미 포함되어 있으며 INSTALLED_APPS에서 확인 가능
  - django.contrib.auth
- Authentication (인증)
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
- Authorization (권한,허가)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정

- 두번째 app accounts 생성 및 등록
- $ python manage.py startapp accounts
- 사전설정 ...

## Substituting a custom User model
- "커스텀 User 모델로 대체하기"
- 기본 User model을 필수적으로 custom User model로 대체하는 이유 이해
- 일부 프로젝트에서는 django에서 제공하는 built-in User model의 기본 인증 요구사항이 적절치 않을 수 있음
- ex) 회원가입시 username 대신 email을 식별값으로 사용하는 것이 더 적합한 사이트인 경우는 django의 User model이 기본적으로 username을 식별값으로 사용하기 때문에 기존 User model을 수정해야하나 쉽지 않은 작업이기때문
- 그래서 Django는 현재 프로젝트에서 나타낼 User를 참조하는 AUTH_USER_MODEL 설정값을 제공하여 default user model을 재정의(override)할 수 있도록 함

## How to substituting a custom User model
- AbstractUser를 상속받는 커스텀 User 클래스 작성
- 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가지게 됨
```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

- User 모델 상속관계
<img src="./django04_img/usermodel01.png">

- 반드시 User 모델을 대체해야하나?
  - Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분하더라도 커스텀 User 모델을 설정하는 것을 강력하게 권장
  - 커스텀 User 모델을 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문
  - 단 User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함

- 데이터베이스 초기화
    - 프로젝트 중간일 경우엔 데이터베이스 초기화!





