user_create_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 60},
        "password": {"type": "string", "minLength": 6, "maxLength": 18},
        "first_name": {"type": "string", "minLength": 3, "maxLength": 60},
        "last_name": {"type": "string", "minLength": 3, "maxLength": 60},
      },
    "required": ["name", "password", "first_name", "last_name"]
}

user_update_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "maxLength": 60},
        "first_name": {"type": "string", "maxLength": 60},
        "last_name": {"type": "string", "maxLength": 60},
      },
    "required": []
}