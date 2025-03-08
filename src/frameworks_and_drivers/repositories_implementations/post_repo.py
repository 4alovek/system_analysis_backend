from frameworks_and_drivers.django.posts.models import Post
from interface_adapters.repositories_interfaces.post_repo import PostRepositoryInterface

class PostRepository(PostRepositoryInterface):
    def create_post(self, title, content, user=None):
        return Post.objects.create(title=title, content=content, user=user)

    def get_posts_by_user(self, user):
        return Post.objects.filter(user=user)
