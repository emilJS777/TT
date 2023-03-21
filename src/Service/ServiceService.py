from .IServiceRepo import IServiceRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from datetime import datetime
from src import app
import os
from flask import g
from src.Image.IImageRepo import IImageRepo


class ServiceService(Service, Repository):

    def __init__(self, service_repository: IServiceRepo, image_repository: IImageRepo):
        self.service_repository: IServiceRepo = service_repository
        self.image_repository: IImageRepo = image_repository

    def create(self, body: dict) -> dict:
        service = self.service_repository.create(
                  body=body)
        return self.response_ok({'id': service.id, 'msg': 'услуга успешно создана'})

    def update(self, service_id: int, body: dict) -> dict:
        service = self.service_repository.get_by_id(service_id)
        if not service or not service.creator_id == g.user_id:
            return self.response_updated('услуга не найдена')
        self.service_repository.update(
            service=service,
            body=body)
        return self.response_updated('услуга успешно обновлена')

    def delete(self, service_id: int) -> dict:
        service = self.service_repository.get_by_id(service_id)
        if not service or not service.creator_id == g.user_id:
            return self.response_updated('услуга не найдена')

        if service.image:
            self.image_repository.delete(service.image)

        self.service_repository.delete(service)
        return self.response_deleted('услуга успешно удалена')

    def get_by_id(self, service_id: int) -> dict:
        service = self.service_repository.get_by_id(service_id)
        if not service:
            return self.response_updated('услуга не найдена')
        return self.response_ok({
            'id': service.id,
            'title': service.title,
            'short_description': service.short_description,
            'long_description': service.long_description,
            'creation_date': service.creation_date.strftime("%Y-%m-%d"),
            'image': self.get_dict_items(service.image) if service.image else None,

            'name': service.name,
            'last_name': service.last_name,
            'patronymic': service.patronymic,
            'data': service.data,
            'city': service.city,
            'gender': service.gender,
            'problem': service.problem,
            'exercise': service.exercise,

            "creator": {
                "id": service.creator.id,
                "name": service.creator.name,
                "first_name": service.creator.first_name,
                "last_name": service.creator.last_name,
                'image': self.get_dict_items(service.creator.image) if service.creator.image else None
            },
        })

    def get_all(self, page: int, per_page: int, exclude_id: int or None, search: str or None) -> dict:

        services = self.service_repository.get_all(
            page=page,
            per_page=per_page,
            exclude_id=exclude_id,
            search=search)
        return self.response_ok({
            'total': services.total,
            'page': services.page,
            'pages': services.pages,
            'per_page': services.per_page,
            'items': [{
                'id': service.id,
                'title': service.title,
                'short_description': service.short_description,
                'creation_date': service.creation_date.strftime("%Y-%m-%d"),
                'image': self.get_dict_items(service.image) if service.image else None,
                'name': service.name,
                'last_name': service.last_name,
                'patronymic': service.patronymic,
                'data': service.data,
                'city': service.city,
                'gender': service.gender,
                'problem': service.problem,
                'exercise': service.exercise,
            } for service in services.items]
        })
