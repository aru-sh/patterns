## Quickstart
Pykka is a Python implementation of the actor model.
The actor model introduces some simple rules to control the sharing of state and cooperation between execution units,
which makes it easier to build concurrent applications.

## Quickstart

1. An actor is an execution unit that executes concurrently with other actors.
2. An actor does not share state with anybody else, but it can have its own state.
3. An actor can only communicate with other actors by sending and receiving messages. It can only send messages to actors whose address it has.
4. When an actor receives a message it may take actions like:
   1. altering its own state, e.g. so that it can react differently to a future message, 
   2. sending messages to other actors, or 
   3. starting new actors.
5. None of the actions are required, and they may be applied in any order.
6. An actor only processes one message at a time. In other words, a single actor does not give you any concurrency, and it does not need to use locks internally to protect its own state.

Taken from: https://pykka.readthedocs.io/en/stable/quickstart/