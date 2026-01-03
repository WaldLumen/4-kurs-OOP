from abc import ABC, abstractmethod

class IProgressListener(ABC):
    @abstractmethod
    def init_task(self):
        pass

    @abstractmethod
    def update_progress(self, progress: float):
        pass

    @abstractmethod
    def finish_task(self):
        pass


class TextProcessor:
    def __init__(self):
        self._listener = None

    def set_progress_listener(self, listener: IProgressListener):
        self._listener = listener

    def remove_progress_listener(self):
        self._listener = None

    def count_chars(self, text: str, ch: str) -> int:
        if self._listener:
            self._listener.init_task()

        length = len(text)
        counter = 0

        for pos, char in enumerate(text):
            if char == ch:
                counter += 1

            if self._listener:
                self._listener.update_progress((pos + 1) / length)

        if self._listener:
            self._listener.finish_task()

        return counter


class PercentageProgressListener(IProgressListener):
    def __init__(self):
        self._percent = 0

    def init_task(self):
        self._percent = 0
        print("0%")

    def update_progress(self, progress: float):
        current = int(progress * 100)
        if current > self._percent:
            print(f"{current}%")
            self._percent = current

    def finish_task(self):
        self._percent = 0


class PointsProgressListener(IProgressListener):
    def __init__(self, width: int):
        self._width = width
        self._points = 0

    def init_task(self):
        self._points = 0

    def update_progress(self, progress: float):
        points_count = int(progress * self._width)
        to_print = points_count - self._points
        if to_print > 0:
            print("." * to_print, end="")
            self._points = points_count

    def finish_task(self):
        print()
        self._points = 0


processor = TextProcessor()
listener = PercentageProgressListener()
processor.set_progress_listener(listener)
print("Count:", processor.count_chars("Happy birthday to you", "y"))

processor.remove_progress_listener()
listener = PointsProgressListener(10)
processor.set_progress_listener(listener)
print("Count:", processor.count_chars("Happy birthday to you", "y"))
