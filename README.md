# 점프 투 장고 클론 코딩

웹 개발 입문을 위한 [점프 투 장고](https://wikidocs.net/book/4223) ~~무작정~~ 생각하며 따라하기

## 버전 관리

Django는 Python과 버전 호환성이 있어 주의해야 한다. 이 프로젝트에서는 아래 버전들을 사용하기로 한다.  

- Python==3.10.7
- Django==4.1.1

Django와 Python의 전체 버전 호환성은 아래표와 같다.([출처](https://docs.djangoproject.com/en/4.1/faq/install/#what-python-version-can-i-use-with-django))  

|Django version|Python versions|
|-|-|
|2.2|3.5, 3.6, 3.7, 3.8, 3.9|
|3.1|3.6, 3.7, 3.8, 3.9|
|3.2|3.6, 3.7, 3.8, 3.9, 3.10|
|4.0|3.8, 3.9, 3.10|
|4.1|3.8, 3.9, 3.10, 3.11|

## 개발 서버 구동

아래 명령어로 개발 서버를 구동하고, 특정 포트를 할당할 수도 있다.  

```powershell
# basic command
> manage.py runserver

# port setting
> manage.py runserver [port_num]
```

별도로 포트를 설정하지 않으면 아래 주소의 로컬호스트로 개발 서버가 구동된다.  

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://localhost:8000/](http://localhost:8000/)