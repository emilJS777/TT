service_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 4, "maxLength": 40},
        "short_description": {"type": "string", "maxLength": 400},
        "long_description": {"type": "string", "maxLength": 9000},
        "name": {"type": "string", "maxLength": 400},
        "last_name": {"type": "string", "maxLength": 400},
        "patronymic": {"type": "string", "maxLength": 400},
        "data": {"type": "string", "maxLength": 400},
        "city": {"type": "string", "maxLength": 400},
        "gender": {"type": "string", "maxLength": 400},
        "problem": {"type": "string", "maxLength": 400},
        "exercise": {"type": "string", "maxLength": 400},
      },
    "required": []
}