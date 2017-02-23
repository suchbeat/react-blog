
from flask import jsonify
from flask.views import MethodView

from sqlalchemy import desc

from server.models.post import Post


class PostView(MethodView):

    def get(self, post_id):
        if post_id is None:
            posts = Post.query.order_by(desc(Post.pub_date)).all()
            result = jsonify(data=[p.serialize() for p in posts])
        else:
            post = Post.query.filter_by(id=post_id).first()
            result = jsonify(data=post.serialize())
        return result
