import json
import os
import sys

import graphene
import uvicorn
from fastapi import FastAPI
from graphene import List, ObjectType, Field, String
from graphql import GraphQLError
from starlette.graphql import GraphQLApp

from graphQL.schemas import LectureType

"""
Наша главная функция.
Без аргументов     - возвращает информацию о всех лекциях
С аргументом id    - возвращает информацию о курсе с переданным id
Если такого id нет - бросает исключение GrahQLError
"""

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class Query(ObjectType):
    lectures = None
    get_lectures = Field(List(LectureType), id=String())

    def resolve_get_lectures(self, info, id=None):

        with open(ROOT_DIR + "/graphQL/lectures.json") as lec:
            lectures = json.load(lec)
        if id:
            for lecture in lectures:
                if lecture['id'] == id:
                    return [lecture]
            raise GraphQLError("lecture not found")
        else:
            return lectures


app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, lifespan="on")
