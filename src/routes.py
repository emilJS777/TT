from src import api
from .Auth.AuthController import AuthController
from .User.UserController import UserController
from .Service.ServiceController import ServiceController
from .Image.ImageController import ImageController


api.add_resource(AuthController, "/auth")
api.add_resource(UserController, "/user")
api.add_resource(ServiceController, "/service")
api.add_resource(ImageController, "/image")



