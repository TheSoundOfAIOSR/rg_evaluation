import pytest
from app.survey.sofaidb import DBInterface


def test_connect():
    db = DBInterface()
    db.connect()
