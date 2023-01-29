from sqlalchemy import or_

from src.__Parents.Repository import Repository
from .IUserRepo import IUserRepo
from .UserModel import User
from flask_bcrypt import generate_password_hash


class UserRepository(Repository, IUserRepo):
    user: User = User

    def create(self, body: dict) -> User:
        user = self.user()
        user.name = body['name']
        user.password_hash = generate_password_hash(body['password'])
        user.first_name = body['first_name'].title()
        user.last_name = body['last_name'].title()
        user.save_db()
        return user

    def update(self, user_id: int, body: dict) -> dict:
        user = self.user.query.filter_by(id=user_id).first()

        if body.get('name'):
            user.name = body['name']

        if body.get('first_name'):
            user.first_name = body['first_name']

        if body.get('last_name'):
            user.last_name = body['last_name']

        user.update_db()
        return self.get_dict_items(user)

    def update_role(self, user_id: int, role_id: int) -> dict:
        user = self.user.query.filter_by(id=user_id).first()
        user.role_id = role_id
        user.update_db()
        return self.get_dict_items(user)

    def delete(self, user_id: int) -> dict:
        user = self.user.query.filter_by(id=user_id).first()
        user.delete_db()
        return self.get_dict_items(user)

    def get_by_id(self, user_id: int) -> User:
        user = self.user.query.filter_by(id=user_id).first()
        return user

    def get_by_name(self, name: str) -> User:
        user = self.user.query.filter_by(name=name).first()
        return user

    def get_by_email_address_exclude_id(self, user_id: int, email_address: str):
        user = self.user.query.filter(self.user.id != user_id, self.user.email_address == email_address).first()
        return user

    def get_by_name_exclude_id(self, user_id: int, name: str) -> dict:
        user = self.user.query.filter(self.user.id != user_id, self.user.name == name).first()
        return self.get_dict_items(user)

    def get_all(self, page: int, per_page: int) -> dict:
        users = self.user.query.paginate(page=page, per_page=per_page)
        return users

    def get_all_by_ids(self, user_ids: list[int]) -> list[User]:
        users: list[User] = User.query.filter(User.id.in_(user_ids)).all()
        return users


