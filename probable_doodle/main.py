# -*- coding: utf-8 -*-
"""Coroutine as_completed."""
import asyncio
from collections.abc import AsyncGenerator
from functools import partial
import typing
from typing import Any

DEFAULT_CAPACITY = 32


async def as_completed(aws: typing.Iterable, capacity=DEFAULT_CAPACITY) -> AsyncGenerator:
    """Coroutine as_completed.

    Receive completed tasks as they are done.
    """
    async for item in Waiter(aws, capacity=capacity):
        yield item


class Waiter:
    """Waiter."""

    def __init__(self, items: typing.Iterable, *, capacity=DEFAULT_CAPACITY):
        """Init Waiter."""
        self.items = items
        self.counter = asyncio.Queue(maxsize=capacity)
        self.queue_out = asyncio.Queue()

    def __aiter__(self):
        """Async iter method."""
        consume_task = asyncio.current_task()
        produce_task = asyncio.create_task(self.produce())
        cancel_callback = partial(Waiter.stop_consuming, consume_task)
        produce_task.add_done_callback(cancel_callback)
        return self

    async def __anext__(self):
        """Async next method."""
        item = await self.queue_out.get()
        self.queue_out.task_done()
        return item

    @staticmethod
    def stop_consuming(consume_task: asyncio.Task, task_done):
        try:
            consume_task.get_coro().throw(StopAsyncIteration)
        except StopIteration:
            pass

    async def produce(self):
        """Produce method."""
        for aw in self.items:
            await self.counter.put(0)
            self.launch_task(aw)
        await self.counter.join()
        await self.queue_out.join()

    def launch_task(self, aw: typing.Awaitable):
        task = asyncio.create_task(aw)
        task.add_done_callback(self.done_task)

    def done_task(self, task_done):
        self.counter.get_nowait()
        self.queue_out.put_nowait(task_done)
        self.counter.task_done()
