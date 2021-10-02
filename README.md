# GraphQL
Простой GraphQL сервис

Необходим, чтобы узнавать информацию о лекциях

## Запуск
Запускаем main, переходим по ссылке и пишем запрос

## Примеры команд

  ```
  {
    getLectures
    {
      name
      teacher
       {
        name
        birthday
        info
       }
    }
  }
```

  ```
  {
   getLectures(id : "2")
    {
      id
      name
      day
      teacher
       {
        name
        birthday
        info
        education
         {
          university
          faculty
          date
         }
       }
    }
  }
```

