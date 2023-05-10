from abc import abstractmethod, ABC
from dataclasses import dataclass


class Parser(ABC):
    @abstractmethod
    def data_parse(self, data):
        pass


@dataclass
class HouseData:
    url: str
    title: str
    created_time: str
    params: list
    photos: list
    city: str
    region: str


class ParserHouse(Parser):
    def data_parse(self, data: dict | None):
        objects = []
        for object in data["data"]:
            url = object["url"]
            title = object["title"]
            created_time = object["created_time"]
            city = object["location"]["city"]["name"]
            region = object["location"]["region"]["name"]
            params = object.get("params", [])

            params_values = []
            for param in params:
                param_value = param.get("value")
                if param_value is not None:
                    params_values.append(param_value)

            photos_url = []
            for photo in object['photos']:
                photos_url.append(photo['link'])

            objects.append(
                HouseData(
                    url=url,
                    title=title,
                    created_time=created_time,
                    params=params_values,
                    photos=photos_url,
                    city=city,
                    region=region,
                )
            )
        return objects