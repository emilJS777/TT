from abc import ABC, abstractmethod
from .ServiceModel import Service


class IServiceRepo(ABC):
    @abstractmethod
    def create(self, body: dict) -> Service:
        pass

    @abstractmethod
    def update(self, service: Service, body: dict):
        pass

    @abstractmethod
    def delete(self, service: Service):
        pass

    @abstractmethod
    def get_by_id(self, service_id: int) -> Service:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, exclude_id: int or None, search: str or None):
        pass
