import os.path
import pytest
import app
import config
import posts_func


class TestApi:
    post_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    def test_all_posts_have_correct_keys(self):
        test_client = app.app.test_client()
        result = test_client.get("/api/posts/")
        list_of_posts = result.get_json(config.POST_PATH)
        for post in list_of_posts:
            assert post.keys() == self.post_keys, "Неправильные ключи у словаря"

    def test_one_post(self):
        post = posts_func.get_post_by_pk(3)
        assert post["pk"] == 3, "возвращается неправильный пост"
