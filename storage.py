from typing import List

import model

class StorageException(Exception):
    pass

class LocalStorage:
    def __init__(self):
        self.id_counter = 0
        self.storage = {}

    def create(self, event: model.Event) -> str:
        if event.date in self.storage:
            raise StorageException('this date: {event.date} is already in use')
        self.id_counter += 1
        event.id = str(self.id_counter)
        self.storage[event.id] = event
        return event.id

    def list(self) -> List[model.Event]:
        return list(self.storage.values())

    def read(self, id: str) -> model.Event:
        if id not in self.storage:
            raise StorageException(f"{id} not found in storage")
        return self.storage[id]

    def update(self, id: str, event: model.Event):
        if id not in self.storage:
            raise StorageException(f"{id} not found in storage")
        event.id = id
        self.storage[event.id] = event

    def delete(self, id: str):
        if id not in self.storage:
            raise StorageException(f"{id} not found in storage")
        del self.storage[id]
