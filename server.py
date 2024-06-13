import uvicorn
from fastapi import FastAPI, Request, Response
import context as ctx
import threading

server = FastAPI()

@server.get("/context")
# Omit "async" and it's run in an external threadpool
# https://fastapi.tiangolo.com/async/#path-operation-functions
async def get_context(_: Request) -> Response:
    thread_id = threading.get_native_id()
    print(f"thread_id: {thread_id}")

    c = ctx.get_context()

    # If the key exists in the context, it means the context is reused.
    if c.has_key("test"):
        return Response(status_code=500, content="Key exists")
    else:
        c.set("test", 1)
        return Response(status_code=200, content="Key doesn't exists")

if __name__ == '__main__':
    uvicorn.run(
        'server:server',
        port=13000,
        log_level='info',
        host='127.0.0.1',
    )
