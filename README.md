* Получить всех пользователей: GET http://localhost:5000/api/v1/users
* Получить одного пользователя:  http://localhost:5000/api/v1/users/<user.id>
* Удалить пользователя по ID: DELETE http://localhost:5000/api/v1/users/<user.id>
* Создание пользователя: POST http://localhost:5000/api/v1/users
* Поиск по полям: GET http://localhost:5000/api/v1/users/filter=first_name::Test....... (Без учета регистра)
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

* Изменение пользователя: PATCH http://localhost:5000/api/v1/users/<user.id>.json
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