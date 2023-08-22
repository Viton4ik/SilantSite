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
- Для проверке работы в базе данных созданы сущности: 
1. Manager1 (роль - Менеджер)
2. Client1 (роль - Клиент)
3. Service1 (роль - Сервисная компания)
- Пароль пользователя для каждой сущности: 123456789//


## Views

<img src="https://img.shields.io/static/v1?label=1&message=localhost&color=9cf"/>
<h3 align="center"><img src="https://github.com/Viton4ik/SilantSite/blob/master/pic/localhost.png"/></h3> 

<img src="https://img.shields.io/static/v1?label=2&message=main&color=9cf"/>
<h3 align="center"><img src="https://github.com/Viton4ik/SilantSite/blob/master/pic/main.png"/></h3> 

<img src="https://img.shields.io/static/v1?label=3&message=maintenance&color=9cf"/>
<h3 align="center"><img src="https://github.com/Viton4ik/SilantSite/blob/master/pic/maintenance.png"/></h3> 

<img src="https://img.shields.io/static/v1?label=4&message=claim&color=9cf"/>
<h3 align="center"><img src="https://github.com/Viton4ik/SilantSite/blob/master/pic/claim.png"/></h3> 

<img src="https://img.shields.io/static/v1?label=5&message=edit_create&color=9cf"/>
<h3 align="center"><img src="https://github.com/Viton4ik/SilantSite/blob/master/pic/edit_create.png"/></h3> 

<img src="https://img.shields.io/static/v1?label=6&message=filters&color=9cf"/>
<h3 align="center"><img src="https://github.com/Viton4ik/SilantSite/blob/master/pic/filters.png"/></h3> 

<img src="https://img.shields.io/static/v1?label=7&message=dict&color=9cf"/>
<h3 align="center"><img src="https://github.com/Viton4ik/SilantSite/blob/master/pic/dict.png"/></h3>

<img src="https://img.shields.io/static/v1?label=8&message=api&color=9cf"/>
<h3 align="center"><img src="https://github.com/Viton4ik/SilantSite/blob/master/pic/api.png"/></h3>

<img src="https://img.shields.io/static/v1?label=9&message=redoc&color=9cf"/>
<h3 align="center"><img src="https://github.com/Viton4ik/SilantSite/blob/master/pic/redoc.png"/></h3>

<img src="https://img.shields.io/static/v1?label=10&message=swagger&color=9cf"/>
<h3 align="center"><img src="https://github.com/Viton4ik/SilantSite/blob/master/pic/swagger.png"/></h3>