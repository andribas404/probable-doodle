# -*- coding: utf-8 -*-
"""Coroutine as_completed."""

import asyncio
from probable_doodle import as_completed


async def test_func(url):
    await asyncio.sleep(1)
    return url + url


async def main():
    aws = map(test_func, "ab"*3)
    async for item in as_completed(aws, capacity=2):
        print(item)

asyncio.run(main())
