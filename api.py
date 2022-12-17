from .rabbit import Rabbit


class Api:
    def __init__(self, rabbit: Rabbit) -> None:
        pass

    def root(self) -> int, str:
        try:
            # send to rabbit
            pass
        except:
            return 404, "failure"

        return 200, "great success"
