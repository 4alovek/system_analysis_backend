from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from frameworks_and_drivers.django.posts.post_controller import PostController

api = NinjaExtraAPI(title="XY", version="1.0")
api.register_controllers(PostController, NinjaJWTDefaultController)
