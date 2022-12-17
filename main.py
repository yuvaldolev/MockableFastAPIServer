import uvicorn

from .server_builder import ServerBuilder


def main() -> None:
    rabbit = Rabbit(...)
    api = Api(rabbit)
    server = ServerBuilder(api).root().hello().build()
    uvicorn.run(server, host="0.0.0.0", port=5000)


if "__main__" == __name__:
    main()
