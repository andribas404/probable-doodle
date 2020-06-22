# -*- coding: utf-8 -*-
"""Coroutine as_completed."""

import asyncio
from probable_doodle import as_completed


async def test_echo(msg):
    await asyncio.sleep(1)
    return msg

async def test_agen():
    for item in map(test_echo, "ab"*3):
        yield item

async def main():
    async for item in as_completed(test_agen(), capacity=2):
        print(item)

asyncio.run(main())
