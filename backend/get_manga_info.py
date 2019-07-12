import copy
import json


def get_manga(manga):
    manga_dict = {
        "id": manga.id,
        "title": manga.title,
        "manga_url": manga.manga_url,
        "image_url": manga.image_url,
        "tag": manga.tag
    }
    return manga_dict


def get_manga_list(mangas):
    manga_list = []
    for manga in mangas:
        manga_list.append({
            "id": manga.id,
            "title": manga.title,
            "manga_url": manga.manga_url,
            "image_url": manga.image_url,
            "tag": manga.tag
        })
    return manga_list
