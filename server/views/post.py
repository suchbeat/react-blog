
from flask import jsonify, request
from flask.views import MethodView

from sqlalchemy import desc

from server.extensions import db
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

    def post(self, post_id):
        if not request.json.get('title'):
            return jsonify({'error': 'Bad request'}), 400
        if not request.json.get('content'):
            return jsonify({'error': 'Bad request'}), 400
        post = Post(request.json['title'], request.json['content'])
        db.session.add(post)
        db.session.commit()
        return jsonify(data=post.serialize())
