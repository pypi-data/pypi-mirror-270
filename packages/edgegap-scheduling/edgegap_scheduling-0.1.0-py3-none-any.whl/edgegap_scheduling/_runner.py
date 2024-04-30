import logging
from datetime import datetime, timezone
from typing import Callable

from ._model import Task
from ._signature import TaskSignature
from ._state import TaskState

logger = logging.getLogger("scheduling.Runner")


class TaskRunner:
    def __init__(self, task: Task, sleep: Callable):
        super().__init__()
        self.__task = task
        self.__sleep = sleep
        self.__signature = TaskSignature(task.identifier, task.name, task.func)

    def __str__(self):
        return f"Runner: {self.__task}"

    @property
    def should_schedule(self) -> bool:
        return self.__task.need_to_loop

    def get_task(self) -> Task:
        return self.__task.model_copy()

    def update_task(self, every: str | None, delay: str | None):
        self.__task.every = every
        self.__task.delay = delay

    async def run(self):
        await self.__run()

    def __update_task_start(self):
        self.__task.state = TaskState.RUNNING
        self.__task.started_at = datetime.now(tz=timezone.utc)
        self.__task.sleep_at = None
        self.__task.begin_at = None
        self.__task.stopped_at = None

    async def start(self):
        if self.__task.safe_to_start:
            try:
                logger.info(f"Starting {self.__task}")
                self.__update_task_start()

                if self.__task.should_delay:
                    await self.__sleep(self.__task.identifier, self.__task.delay_in_seconds)

                if self.__task.need_to_loop:
                    await self.__loop()
                    self.__task.state = TaskState.STOPPED
                    logger.info(f"{self.__task} Stopped")
                else:
                    await self.__run()
                    self.__task.state = TaskState.COMPLETED
                    logger.info(f"{self.__task} Completed")
            except Exception as e:
                logger.exception(f"{self.__task} raised an exception: {e}")
                self.__task.state = TaskState.ERROR
                self.__task.error = str(e)

            self.__task.stopped_at = datetime.now(tz=timezone.utc)

    async def __loop(self):
        while self.__task.state == TaskState.RUNNING:
            try:
                await self.__run()
            except Exception as e:
                if self.__task.continue_on_exception:
                    logger.exception(f"{self.__task} raised an exception, continuing since defined by the task: {e}")
                else:
                    raise e

            if self.__task.every_in_seconds is None:
                logger.warning(f"Every changed in task {self.__task.name} without stopping it first!")
                break

            await self.__sleep(self.__task.identifier, self.__task.every_in_seconds)

    async def __run(self):
        self.__task.begin_at = datetime.now(tz=timezone.utc)
        arguments, generators = self.__signature.get_arguments()

        for name, generator in generators.items():
            arguments[name] = next(generator)

        await self.__task.func(**arguments)

        for generator in generators.values():
            generator.close()

        self.__task.sleep_at = datetime.now(tz=timezone.utc)

    def stop(self) -> bool:
        can_stop = self.__task.state == TaskState.RUNNING

        if can_stop:
            self.__task.state = TaskState.STOPPING

        return can_stop
