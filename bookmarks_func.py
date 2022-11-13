#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import config
from posts_func import get_posts_all
from pprint import pprint


def get_bookmarks(path=config.BOOKMARKS_PATH):
    """ Возвращает все закладки """
    with open(path, 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)
        return bookmarks


def get_bookmark_post_id():
    all_bookmarks = get_bookmarks()
    all_posts = get_posts_all()

    for pk_id in all_posts:
        for b_pk in all_bookmarks:
            if pk_id['pk'] == b_pk['post_id']:
                a = pk_id['content']
                return a

# pprint(get_bookmark_post_id())


def save_bookmarks(bookmarks, path=config.BOOKMARKS_PATH):
    with open(path, 'w', encoding='utf=8') as file:
        json.dump(bookmarks, file, indent=4, ensure_ascii=False)


def add_bookmarks(post_id):
    """ Добавляет закладку """
    bookmarks = get_bookmarks()  # Возвращает все закладки
    new_bookmarks = {"post_id": int(post_id), "pk": len(bookmarks) + 1}
    bookmarks.append(new_bookmarks)
    save_bookmarks(bookmarks)
    return bookmarks


def remove_bookmarks(post_id):
    del_bookmarks = get_bookmarks(config.BOOKMARKS_PATH)
    nd = [item for item in del_bookmarks if item["post_id"] != post_id]
    save_bookmarks(nd)
    return del_bookmarks


# pprint(get_bookmarks(config.BOOKMARKS_PATH))
# pprint(add_bookmarks(77))
# pprint(get_bookmark_pk(6))
# pprint(del_bookmarks(53))
# pprint(remove_bookmarks(77))
