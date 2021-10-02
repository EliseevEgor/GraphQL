from graphene import String, ObjectType, Field

"""
Тут описываем Ннаши типы
 EducationType - хранит информацию об обучении преподователя
 TeacherType   - хранит информацию о преподавателе
 LectureType   - хранит информацию о курсе
"""


class EducationType(ObjectType):
    university = String()  # университет
    faculty = String()     # факультет
    date = String()        # дата окончания


class TeacherType(ObjectType):
    name = String(required=True)  # умя преподавателя
    birthday = String()           # дата рождения
    info = String()               # общая информация о преподавателе
    education = Field(EducationType)


class LectureType(ObjectType):
    id = String(required=True)
    name = String(required=True)  # Название предмета
    teacher = Field(TeacherType)  # Препрдаватель
    day = String(required=True)   # День недели
