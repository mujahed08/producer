"""
This is a thread-safe implementation of Singleton holding websocket.
"""

from threading import Lock
from websocket import create_connection, WebSocket
from PRODUCER.commons.logger import get_logger

logger = get_logger('ws.py')

class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class WebSocketConnector(metaclass=SingletonMeta):
    con: WebSocket = None
    """
    We'll use this property to prove that our Singleton really works.
    """

    def __init__(self) -> None:
        logger.info('   creating websocket connection to: \
            ws://localhost:8080/ws/broker/main/topic/PRODUCER')
        self.con = create_connection("ws://localhost:8080/ws/broker/main/topic/PRODUCER")
        logger.info('   connection established')

    def send(self, message:str):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        self.con.send(message)

    def close(self) -> None:
        logger.info('   method close called to close web scoket connection')
        self.con.close()

    def __del__(self) -> None:
        self.con.close()
