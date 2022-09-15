import datetime
from typing import Optional, Tuple


__cache = {}
cache_lifetime_in_hrs = 1.0


def get_cached_weather(city: str, country: str) -> Optional[dict]:
    key = __get_key(city, country)
    data: dict = __cache.get(key)
    if not data:
        return None
    last_dt = data["time"]
    dt = datetime.datetime.now() - last_dt
    if dt / datetime.timedelta(minutes=60) < cache_lifetime_in_hrs:
        return data["value"]
    return None


def set_weather_cache(city: str, country: str, value: dict):
    key = __get_key(city, country)
    data = {"time": datetime.datetime.now(), "value": value}
    __cache[key] = data
    __clear_old_cache()


def __get_key(city: str, country: str) -> Tuple[str, str, str, str]:
    if not city or not country:
        raise Exception("City, country, and units are required")
    return city.strip().lower(), country.strip().lower()


def __clear_old_cache():
    for key, data in list(__cache.items()):
        dt = datetime.datetime.now() - data.get("time")
        if dt / datetime.timedelta(minutes=60) > cache_lifetime_in_hrs:
            del __cache[key]
