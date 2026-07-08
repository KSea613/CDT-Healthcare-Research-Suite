import threading
import time


class ResearchEngine:
    def __init__(self, update_callback=None):
        self._running = False
        self._paused = False
        self._thread = None
        self.update_callback = update_callback

    def start(self):
        if self._running:
            return
        self._running = True
        self._paused = False
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def _run_loop(self):
        while self._running:
            if self._paused:
                time.sleep(0.1)
                continue
            # Placeholder for processing step
            if self.update_callback:
                self.update_callback("running")
            time.sleep(1)

    def pause(self):
        self._paused = True
        if self.update_callback:
            self.update_callback("paused")

    def resume(self):
        self._paused = False
        if self.update_callback:
            self.update_callback("running")

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=1)
        if self.update_callback:
            self.update_callback("stopped")
