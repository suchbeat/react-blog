from server.views.index import IndexView
from server.views.post import PostView

ROUTES = (
    ('/', IndexView.as_view('index'), {}),
    ('/post', PostView.as_view('post'), {}),
)
