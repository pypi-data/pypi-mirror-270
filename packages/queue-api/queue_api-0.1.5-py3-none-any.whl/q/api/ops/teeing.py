from typing import TypeVar, Generic, Sequence, overload
import asyncio
from ..api import WriteQueue

A = TypeVar('A')

class tee(WriteQueue[A], Generic[A]):
  """A queue that pushes to the multiple queues at once"""

  @overload
  def __init__(self, queues: Sequence[WriteQueue[A]]): ...
  @overload
  def __init__(self, q1: WriteQueue[A], q2: WriteQueue[A], /, *qs: WriteQueue[A]): ...
  
  def __init__(self, *args):
    self._queues = args[0] if len(args) == 1 else args

  async def push(self, key: str, value: A):
    await asyncio.gather(*[q.push(key, value) for q in self._queues])
