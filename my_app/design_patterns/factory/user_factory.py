from abc import ABC, abstractmethod

from dtos.user_dto import UserDTO
from domain.user import CommonUser, AdminUser

class UserFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_user(user: UserDTO):
        raise NotImplementedError("Not implemented create user method.")

class CommonUserFactory(UserFactory):
    @staticmethod
    def create_user(user: UserDTO):
        return CommonUser(user.name, user.currency, user.balance)

class AdminUserFactory(UserFactory):
    @staticmethod
    def create_user(user: UserDTO):
        return AdminUser(user.name)