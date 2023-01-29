service_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 4, "maxLength": 40},
        "short_description": {"type": "string", "maxLength": 400},
        "long_description": {"type": "string", "maxLength": 9000}
      },
    "required": []
}