import graphene
import unittest
from graphene.test import Client

from main import Query

str1 = '''
{
  getLectures
  {
    name
    teacher
     {
      name
     }
  }
}
'''


class RequestUtilsTest(unittest.TestCase):
    schema = graphene.Schema(query=Query)

    def test1(self):
        client = Client(self.schema)
        executed = client.execute(str1)

        self.assertEqual(executed, {
            "data": {
                "getLectures": [
                    {
                        "name": "Виртуальные машины",
                        "teacher": {
                            "name": "Олег Плисс"
                        }
                    },
                    {
                        "name": "Параллельное программирование",
                        "teacher": {
                            "name": "Евгений Калишенко"
                        }
                    },
                    {
                        "name": "Компиляторы",
                        "teacher": {
                            "name": "Дмитрий Юрьевич Булычев"
                        }
                    }
                ]
            }
        }
                         )

    def test2(self):
        client = Client(self.schema)
        executed = client.execute('''{ getLectures(id:"1") {
                                        name
                                        teacher {
                                         name
                                         birthday
                                         info
                                        }
                                       }
                                      }''')
        self.assertEqual(executed, {
            "data": {
                "getLectures": [
                    {
                        "name": "Виртуальные машины",
                        "teacher": {
                            "name": "Олег Плисс",
                            "birthday": "01.01.1981",
                            "info": "Олег Плисс – выпускник матмеха СПбГУ и бывший преподаватель кафедры системного программирования там же.\n Один из лучших в мире специалистов по «языковым» виртуальным машинам, управлению памятью и истории языков программирования.\n Ныне – сотрудник калифорнийского офиса компании Oracle, после приобретения последней компании Sun Microsystems.\n Больше 10 лет работает над JIT-компилятором и сборщиком мусора в CLDC HI JVM."
                        }
                    }
                ]
            }
        })

    def test3(self):
        client = Client(self.schema)
        executed = client.execute('''{ getLectures(id:"2") {
                                        name
                                        day
                                        teacher {
                                         name
                                         info
                                        }
                                       }
                                      }''')
        self.assertEqual(executed, {
            "data": {
                "getLectures": [
                    {
                        "name": "Параллельное программирование",
                        "day": "Вторник",
                        "teacher": {
                            "name": "Евгений Калишенко",
                            "info": "Руководитель группы разработки систем реального времени, Научно-инженерный центр Санкт-Петербургского электротехнического университета.\n Преподаватель АУ РАН, СПбГЭТУ ЛЭТИ, CS Center."
                        }
                    }
                ]
            }
        })
