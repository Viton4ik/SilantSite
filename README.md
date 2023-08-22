# Реальный кейс от компании «Силант»

## _сделано на Django_

##
✨Idea:✨
> сервис, в котором можно отслеживать состояние каждой купленной машины и всех её комплектующих

## BackEnd

- Django admin panel: (http://127.0.0.1:8000/admin/) 
- Django REST API: (http://127.0.0.1:8000/api/)
- Django REST API:swagger (http://127.0.0.1:8000/swagger/)
- Django REST API:redoc (http://127.0.0.1:8000/redoc/)

## FrontEnd

- HTML, JS
- Главная страница: (http://127.0.0.1:8000/)
- Таблица машины: (http://127.0.0.1:8000/main/)
- Таблица ТО: (http://127.0.0.1:8000/maintenance/)
- Таблица рекламации: (http://127.0.0.1:8000/claim/)
- Создание машин: (http://127.0.0.1:8000/vehicle_create/)
- Создание ТО: (http://127.0.0.1:8000/maintenance_create/)
- Создание рекламаций: (http://127.0.0.1:8000/claim_create/)
- Редактирование машин: (http://127.0.0.1:8000/main/"pk")
- Редактирование ТО: (http://127.0.0.1:8000/maintenance/"pk")
- Редактирование рекламаций: (http://127.0.0.1:8000/claim/"pk")


## Использование
#### _BackEnd_

- Создайте новую папку в VS Code/PyCharm/Atom и загрузите проект

```sh
git clone https://github.com/Viton4ik/SilantSite.git

```
- Создайте виртуальную среду

```sh
python3 -m venv venv
```
- Активируйте виртуальную среду

```sh
source venv/bin/activate
```
- Перейдите в папку с проектом
```sh
cd Project
```
- Скачайте библиотеки

```sh
pip3 install -r requirements.txt
```
- Запускайте Django сервер

```sh
python3 manage.py runserver
```
#### _FrontEnd_

- Не требует дополнительных загрузок. Работает на стороне сервера Django


## Views

<img src="https://img.shields.io/static/v1?label=1&message=view&color=9cf"/>
<h3 align="center"><img src="https://github.com/Viton4ik/publicPosts/blob/master/pic.png"/></h3> 
