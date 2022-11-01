#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_hashtags(text):
    hashtags = []
    for element in text.split(" "):
        if element.startswith("#"):
            hashtags.append(element[1:])
    return hashtags


# words = input()
# result = get_hashtags(words)
# print(" ".join(result))
