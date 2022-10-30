from typing import Any, Callable, Mapping, Optional, Sequence
from datetime import datetime, timedelta



class Timer:
    def __init__(self):
        self.__initial_time: Optional[datetime] = None

    def __enter__(self):
        print('AQUIII')
        self.__initial_time = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_result(self) -> timedelta:
        return self.__initial_time - datetime.now()



