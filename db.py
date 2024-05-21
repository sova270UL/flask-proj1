from typing import List
import model
import storage

class DBException(Exception):
    pass

class EventDB:
    def __init__(self):
        self.storage = storage.LocalStorage()

    def create(self, event: model.Event) -> str:
        try:
            return self.storage.create(event)
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Event]:
        try:
            return self.storage.list()
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, id: str) -> model.Event:
        try:
            return self.storage.read(id)
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, id: str, event: model.Event):
        try:
            return self._storage.update(id, event)
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def delete(self, id: str):
        try:
            return self.storage.delete(id)
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")
