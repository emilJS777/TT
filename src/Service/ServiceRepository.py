from sqlalchemy import or_
from .IServiceRepo import IServiceRepo
from .ServiceModel import Service
from flask import g


class ServiceRepository(IServiceRepo):
    def create(self, body: dict) -> Service:
        service: Service = Service()
        service.title = body['title']
        service.short_description = body['short_description']
        service.long_description = body['long_description']

        service.name = body['name']
        service.last_name = body['last_name']
        service.patronymic = body['patronymic']
        service.data = body['data']
        service.city = body['city']
        service.gender = body['gender']
        service.problem = body['problem']
        service.exercise = body['exercise']

        service.creator_id = g.user_id
        service.save_db()
        return service

    def update(self, service: Service, body: dict):
        service.title = body['title']
        service.short_description = body['short_description']
        service.long_description = body['long_description']
        service.name = body['name']
        service.last_name = body['last_name']
        service.patronymic = body['patronymic']
        service.data = body['data']
        service.city = body['city']
        service.gender = body['gender']
        service.problem = body['problem']
        service.exercise = body['exercise']
        service.update_db()

    def delete(self, service: Service):
        service.delete_db()

    def get_by_id(self, service_id: int) -> Service:
        service: Service = Service.query.filter_by(id=service_id).first()
        return service

    def get_all(self, page: int, per_page: int, exclude_id: int or None, search: str or None):

        services = Service.query.filter(Service.id != exclude_id if exclude_id else Service.id.isnot(None),
                                        Service.creator_id == g.user_id,
                                        or_(Service.title.like(f"%{search}%"), Service.short_description.like(f"%{search}%")) if search else Service.id.isnot(None)) \
            .paginate(page=page, per_page=per_page)
        return services
