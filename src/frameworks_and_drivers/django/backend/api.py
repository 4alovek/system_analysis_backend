from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from posts.post_controller import NinjaPostController
from posts.api import PostsController
from users.api import AuthController


api = NinjaExtraAPI(title="XY", version="1.0")
api.register_controllers(AuthController,
                         PostsController,
                         NinjaJWTDefaultController,
                         )
