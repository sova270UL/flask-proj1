from typing import List
import model
import db

title_limit = 30
text_limit = 200

class LogicException(Exception):
    pass

class Eventlogic:
    def __init__(self):
        self.event_db = db.EventDB()
        
        
    @staticmethod
    def validate_event(event: model.Event):
        if event is None:
            raise LogicException('event is None')
        if event.title is None or len(event.title) > title_limit:
            raise LogicException('title lenght > max: {title_limit}')
        if event.text is None or len(event.text) > text_limit:
            raise LogicException('text lenght > max: {text}')
        
        
    def create(self, event: model.Event) -> str:
        self.validate_event(event)
        try:
            return self.event_db.create(event)
        except Exception as e:
            raise LogicException(f"failed CREATE operation with: {e}")
        
    def list(self) -> List[model.Event]:
        try:
            return self.event_db.list()
        except Exception as e:
            raise LogicException(f"failed LIST operation with: {e}")
        
    def read(self, id: str) -> model.Event:
        try:
            return self.event_db.read(id)
        except Exception as e:
            raise LogicException(f"failed READ operation with: {e}")
        
    def update(self, id, event: model.Event):
        self.validate_event(event)
        try:
            return self.event_db.update(id, event)
        except Exception as e:
            raise LogicException(f"failed UPDATE operation with: {e}")
        
    def delete(self, id: str):
        try:
            return self.event_db.delete(id)
        except Exception as e:
            raise LogicException(f"failed DELETE operation with: {e}")