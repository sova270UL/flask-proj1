from flask import Flask, request
import model
import logic

event_logic = logic.Eventlogic()

app = Flask(__name__)

class apiException(Exception):
    pass

def from_raw(raw_event) -> model.Event:
    parts = raw_event.split('|')
    if len(parts) == 4:
        event = model.Event()
        event.id = str(parts[0])
        event.date = str(parts[1])
        event.title = str(parts[2])
        event.text = str(parts[3])
        return event
    elif len(parts) == 3:
        event = model.Event()
        event.id = None
        event.date = str(parts[0])
        event.title = str(parts[1])
        event.text = str(parts[2])
        return event
    else:
        raise apiException(f'Invalid event format {raw_event}')
    
def to_raw(event) -> str:
    if event.id:
        return f'{event.id}|{event.date}|{event.title}|{event.text}'
    else:
        return f'{event.date}|{event.title}|{event.text}'
    
    
    
@app.route('/api/v1/calendar/', methods=['GET'])
def list():
    try:
        events = event_logic.list()
        raw_event = ''
        for event in events:
            raw_event += to_raw(event) + '\n'
        return raw_event, 200
    except apiException as e:
        return f"failed to LIST with: {e}", 404

@app.route('/api/v1/calendar/<id>/', methods=['GET'])
def read(id):
    try: 
        event = event_logic.read(id)
        raw_event = to_raw(event)
        return raw_event, 200
    except apiException as e:
        return f"failed to READ with: {e}", 404

@app.route('/api/v1/calendar/', methods=['POST'])
def create():
    '''date|title|text|'''
    try:
        data = request.get_data().decode('utf-8')
        event = from_raw(data)
        id = event_logic.create(event)
        return f'new id: {id}', 201
    except apiException as e:
        return f"failed to CREATE with: {e}", 404

@app.route('/api/v1/calendar/<id>/', methods=['PUT'])
def update(id):
    try:
        data = request.get_data().decode('utf-8')
        event = from_raw(data)
        event_logic.update(id, event)
        return 'updated', 204
    except apiException as e:
        return f"failed to UPDATE with: {e}", 404

@app.route('/api/v1/calendar/<id>/', methods=['DELETE'])
def delete(id):
    try:
        event_logic.delete(id)
        return 'deleted', 204
    except apiException as e:
        return f"failed to DELETE with: {e}", 404