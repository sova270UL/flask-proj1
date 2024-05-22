# flask-proj1
API для создания событий в календаре

# '/api/v1/calendar/', methods=['POST'] 
создание событие date|title|text|

# '/api/v1/calendar/<id>/', methods=['GET']
получение события по ID

# '/api/v1/calendar/', methods=['GET']
просмотр всех созданных событий

# '/api/v1/calendar/<id>/', methods=['PUT']
изминеие события по ID id|date|title|text|

# '/api/v1/calendar/<id>/', methods=['DELETE']
удаление события по ID