from threading import Lock
from os import SEEK_SET

class IO:
    def __init__(self, source):
        self.file = open(source, 'rb')
        self._lock = Lock()
        self._b_lock = Lock()

    def set_s_block_size(self, s_block_size):
        self.s_block_size = s_block_size

    def close(self):
        self.file.close()

    def read_block(self, block_number):
        self._b_lock.acquire()
        self.file.seek(block_number * self.s_block_size)
        buf = self.file.read(self.s_block_size)
        self._b_lock.release()
        return buf

    def read_at(self, count, offset=0, whence=SEEK_SET):
        self._b_lock.acquire()
        self.file.seek(offset, whence)
        buf = self.file.read(count)
        self._b_lock.release()
        return buf

    def lock(self): self._lock.acquire()

    def unlock(self): self._lock.release()