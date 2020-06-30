# probable-doodle

Problem statement
-----------------

В кафе привезли робота-официанта, который умеет принимать заказы и приносить готовые блюда из кухни.

Каждый заказ может иметь разное время приготовления, одновременно может готовиться не более 5 заказов.

Запрограммировать робота на прием и обработку заказов.

Примечание: Робот не должен спать.

```python
import asyncio
from probable_doodle import as_completed


async def test_echo(msg):
    await asyncio.sleep(1)
    return msg

async def test_agen():
    for item in map(test_echo, "abc" * 10):
        yield item

async def main():
    async for item in as_completed(test_agen(), capacity=5):
        print(item)

asyncio.run(main())
```

Helpful links:
-----
* [AsyncGenerator](https://docs.python.org/3.8/library/collections.abc.html?highlight=asend#collections.abc.AsyncGenerator)
* [async for](https://docs.python.org/3.8/reference/compound_stmts.html#the-async-for-statement)

* [PEP 525](https://www.python.org/dev/peps/pep-0525/#pyasyncgenasend-and-pyasyncgenathrow)
* [Using Asyncio in Python (book)](https://www.oreilly.com/library/view/using-asyncio-in/9781492075325/)
