import json
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

from pydantic import BaseModel


@dataclass
class Person:
    name: str
    position: str
    time_of_birth: datetime


class PersonPy(BaseModel):
    name: str
    position: str
    time_of_birth: datetime

if __name__ == '__main__':
    czesiek = Person('Czesiek', 'developer', datetime(1990, 1, 1, tzinfo=ZoneInfo('Europe/Warsaw')))
    dd = czesiek.__dict__
    print(dd)
    # tekst = json.dumps(dd, indent=4) # error for datetimes...
    # print(tekst)

    szymek = PersonPy(name='Szymek', position='developer', time_of_birth=datetime(1990, 1, 1, tzinfo=ZoneInfo('Europe/Warsaw')))
    print(szymek)

    dd = szymek.model_dump()
    print(dd)
    teksst = szymek.model_dump_json()
    print(teksst)

    clone = PersonPy.model_validate_json(teksst)
    print(clone)
    print(szymek == clone)