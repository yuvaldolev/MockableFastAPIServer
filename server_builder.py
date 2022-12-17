from fastapi import FastAPI

from .api import Api


class ServerBuilder:
    def __init__(self, api: Api) -> None:
        self._api = api
        self._app = FastAPI()

    def build(self) -> FastAPI:
        return self._app

    def root(self) -> "ServerBuilder":
        @self._app.get("/")
        def root():
            return self._api.root()

    def hello(self) -> "ServerBuilder":
        @self._app.get("/hello/{name}")
        def hello(name: str) -> str:
            return f"Hello, {name}"

        return self
