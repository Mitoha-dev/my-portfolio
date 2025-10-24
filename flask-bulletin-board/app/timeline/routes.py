from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from ..models import db, Post
from ..forms import PostForm
from . import timeline_bp   # __init__.py で作った Blueprint を import

@timeline_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('timeline.index'))
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('timeline/timeline.html', form=form, posts=posts)