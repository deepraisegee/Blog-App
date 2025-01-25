from app.config import create_app
from app.posts.models import Post

app = create_app()


@app.context_processor
def globals():
    return {"trending_posts": Post.get_trending_posts()}


if __name__ == "__main__":
    app.run(debug=True)
