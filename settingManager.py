import json
import os
from typing import List

from pygame import Vector2
from pygame.surface import Surface

from border import Border


class SettingsManager:
    @classmethod
    def __get_filename(cls):
        base = os.path.dirname(__file__)
        rel_path = "settings.json"
        return os.path.join(base, rel_path)

    @classmethod
    def __get_json_data(cls):
        filename = cls.__get_filename()
        data = None
        with open(filename, "r") as json_file:
            data = json.load(json_file)
        if data is None:
            raise Exception("data is None")
        return data

    @classmethod
    def __set_json_data(cls, data):
        filename = cls.__get_filename()
        with open(filename, "w") as json_file:
            json.dump(data, json_file)

    @classmethod
    def is_init(cls) -> bool:
        data = cls.__get_json_data()
        return data["isInit"]

    @classmethod
    def init_borders(cls, screen: Surface):
        data = cls.__get_json_data()
        list_border: List[Border] = []
        if "borders" not in data:
            return []
        for i in data["borders"]:
            start = i["start"]
            finish = i["finish"]
            v_start = Vector2(start["x"], start["y"])
            v_finish = Vector2(finish["x"], finish["y"])
            b = Border(screen, v_start, v_finish)
            list_border.append(b)

        return list_border

    @classmethod
    def write_borders(cls, list_border: List[Border]):
        data = cls.__get_json_data()
        l = []
        for border in list_border:
            d = dict()
            start = dict()
            start["x"] = border.start.x
            start["y"] = border.start.y
            d["start"] = start
            finish = dict()
            finish["x"] = border.finish.x
            finish["y"] = border.finish.y
            d["finish"] = finish
            l.append(d)
        data["borders"] = l
        cls.__set_json_data(data)

    @classmethod
    def change_init(cls, condition):
        # type: (bool) -> None
        data = cls.__get_json_data()
        data["isInit"] = condition
        cls.__set_json_data(data)

    @classmethod
    def set_init_false(cls):
        data = cls.__get_json_data()
        data["isInit"] = False
        cls.__set_json_data(data)
