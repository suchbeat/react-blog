from views.index import IndexView
from views.post import PostView

post_view = PostView.as_view('posts')

ROUTES = (
    ('/', IndexView.as_view('index'), {}),
    ('/posts', post_view, {'defaults': {'post_id': None}}),
    ('/posts/<int:post_id>', post_view, {}),
)
