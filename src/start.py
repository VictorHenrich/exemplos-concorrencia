from app import app
from utils import PORT, HOST
from route import *
from multiprocessing import cpu_count, Process


def start_app():
    app.run(HOST, PORT)



def init() -> None:
    processes: list[Process] = [
        Process(target=start_app)
        for _ in range(cpu_count())
    ]

    [process.start() for process in processes]
    [process.join() for process in processes]


if __name__ == "__main__":
    init()