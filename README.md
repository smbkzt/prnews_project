# PR news company test

### Prerequisites
To use this app you need:
```
* python >= 3
* Flask==0.12.1
* Flask-RESTful==0.3.5
* Flask-SQLAlchemy==2.2
```

### Installing
```
pip install -r req.txt
```

### Use
* Получить всех пользователей: GET http://localhost:5000/api/v1/users/
* Получить одного пользователя:  http://localhost:5000/api/v1/users/<user.id>
* Удалить пользователя по ID: DELETE http://localhost:5000/api/v1/users/<user.id>
* Поиск по полям: GET http://localhost:5000/api/v1/users/filter=first_name::Test....... (Без учета регистра)

* Создание пользователя: POST http://localhost:5000/api/v1/users

{
  "data": {
    "attributes": {
      "first_name": "test first name",
      "last_name": "test last name",
      "middle_name": "test middle name",
      "password": "testpass",
      "city": "test",
      "gender": "male"
    },
    "type": "user"
  }
}


* Изменение пользователя: PATCH http://localhost:5000/api/v1/users/<user.id>

{
  "data": {
    "attributes": {
      "first_name": "test first name",
      "last_name": "test last name",
      "middle_name": "test middle name",
      "password": "testpass",
      "city": "test",
      "male": "male"
    },
    "type": "user"
  }
}
