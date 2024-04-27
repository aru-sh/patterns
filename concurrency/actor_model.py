import time
from typing import Any

import pykka


class Greeter(pykka.ThreadingActor):
    def __init__(self, greeting="Hi There!"):
        super().__init__()
        self.greeting = greeting

    def on_receive(self, message: Any) -> Any:
        return self.greeting


if __name__ == "__main__":
    actor_ref = Greeter.start(greeting="Hi!")
    time.sleep(0.5)
    answer = actor_ref.ask('Hi?')
    print(answer)

    actor_ref.stop()
