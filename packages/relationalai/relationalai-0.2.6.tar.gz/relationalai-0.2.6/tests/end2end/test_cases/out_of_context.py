# pyright: reportUnusedExpression=false
import relationalai as rai
from relationalai.errors import RAIException
import pytest

model = rai.Model(name=globals().get("name", ""), config=globals().get("config"))
Person = model.Type("Person")
Adult = model.Type("Adult")

with model.rule():
    p = Person()
    p.age >= 18
    woop = p.woop
    p.set(Adult)

with pytest.raises(RAIException):
    with model.query() as select:
        a = Adult()
        p.foo
        select(a)

with pytest.raises(RAIException):
    with model.query() as select:
        a = Adult()
        select(a, a.name, a.age, p)

with pytest.raises(RAIException):
    with model.query() as select:
        a = Adult()
        select(a, a.name, a.age, woop)
