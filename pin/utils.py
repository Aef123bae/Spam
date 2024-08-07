import re
import csv

class Utils:

    @staticmethod
    def cookie_string_to_dict(cookie: str) -> dict:
        array = re.findall(r"([^;]+)", cookie)
        objects = {}
        for string in array:
            string = string.strip()
            string_array = string.split("=")
            objects[string_array[0]] = "=".join(string_array[1:])
        return objects

    @staticmethod
    def cookie_dict_to_string(cookie: dict) -> str:
        return ";".join(["%s=%s"%(name, values) for name,values in cookie.items()])

    @staticmethod
    def load_cookie_from_csv(file: str):
        cookies = dict()
        with open(file, "r", encoding="utf-8") as f:
            data = list(csv.DictReader(f))
            for item in data:
                item = dict((name.lower(), value) for name, value in item.items())
                name = item.get("name", item.get("names"))
                value = item.get("value", item.get("values"))
                if isinstance(name, str) and isinstance(value, str):
                    cookies[name] = value
            f.close()
        return cookies