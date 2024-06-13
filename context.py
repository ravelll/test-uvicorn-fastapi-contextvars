import contextvars
from typing import Any

class Context:
    values_dict: dict[str, Any]

    def __init__(self) -> None:
        self.values_dict = {}

    def set(self, key: str, value: Any) -> None:
        self.values_dict[key] = value

    def get(self, key: str) -> Any:
        return self.values_dict.get(key)

    def has_key(self, key: str) -> bool:
        return True if key in self.values_dict else False

c: contextvars.ContextVar[Context] = contextvars.ContextVar('c')

def get_context() -> Context:
    ctx = c.get(None)
    if ctx is None:
        ctx = Context()
        c.set(ctx)
    return ctx
