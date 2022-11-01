#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import config
from pprint import pprint


def get_bookmarks(path=config.BOOKMARKS_PATH):
    """ Возвращает все закладки """
    with open(path, 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)
        return bookmarks


def save_bookmarks(bookmarks, path=config.BOOKMARKS_PATH):
    with open(path, 'w', encoding='utf=8') as file:
        json.dump(bookmarks, file, indent=4, ensure_ascii=False)


def add_bookmark(post_id):
    """ Добавляет закладку """
    bookmarks = get_bookmarks()  # Возвращает все закладки
    new_bookmarks = {"post_id": int(post_id), "pk": len(bookmarks) + 1}
    bookmarks.append(new_bookmarks)
    save_bookmarks(bookmarks)
    # if post_id in bookmarks or not post_id:
    #     return bookmarks


# def del_bookmark(self, post_id):
#     """ Удаляет закладку"""
#     get_bookmark = self.get_bookmarks()
#     if post_id not in get_bookmark or not post_id:
#         return
#     get_bookmark.remove(post_id)
#     self.session.delete(get_bookmark)
#     self.session.commit()


# pprint(get_bookmarks(BOOKMARKS_PATH))

