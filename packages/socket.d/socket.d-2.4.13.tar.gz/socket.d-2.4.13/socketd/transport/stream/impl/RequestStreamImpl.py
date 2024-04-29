import asyncio
from typing import Callable

from socketd.exception.SocketDExecption import SocketDTimeoutException, SocketDException
from socketd.transport.core.Costants import Constants
from socketd.transport.core.Entity import Reply
from socketd.transport.core.Message import MessageInternal
from socketd.transport.stream.RequestStream import RequestStream
from socketd.transport.stream.impl.StreamBase import StreamBase
from socketd.utils.CompletableFuture import CompletableFuture


class RequestStreamImpl(StreamBase, RequestStream):
    def __init__(self, sid: str, timeout: int):
        super().__init__(sid, Constants.DEMANDS_SINGLE, timeout)
        self.__future: CompletableFuture = CompletableFuture()

    def is_done(self):
        return self.__future.done()

    def __await__(self):
        try:
            return self.__future.get(self.timeout() / 1000.0)
        except asyncio.TimeoutError as _e:
            raise SocketDTimeoutException(f"Request reply timeout>{self.timeout()}  sid={self.sid()}")
        except Exception as _e:
            raise SocketDException(f"Request failed, sid= sid={self.sid()} {str(_e)}")

    async def waiter(self) -> Reply:
        if self.__future.done():
            return self.__future.get_result()
        return await self.__await__()

    async def on_reply(self, reply: MessageInternal):
        return await self.__future.set_result(reply)

    def then_reply(self, onReply: Callable[[MessageInternal], None]) -> RequestStream:
        self.__future.then_callback(onReply)
        return self

    def then_error(self, onError: Callable[[Exception], None]) -> RequestStream:
        super().then_error_do(onError)
        return self

    def then_progress(self, onProgress: Callable[[bool, int, int], None]) -> RequestStream:
        super().then_progress_do(onProgress)
        return self