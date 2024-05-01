# -*- coding: utf-8 -*-
# @Time   : 2024/5/1 01:27
import os

from scrawlpy.setting import Settings
from attr import s, attrib


# @s
class MySettings(Settings):
    # Timeout = attrib(type=float, default=os.environ.get("Timeout", 3), converter=float)
    # TTimeout = attrib(type=float, default=os.environ.get("Timeout", 2), converter=float)
    pass
    # MYNAME = attrib(type=str, default="scrawlpy")


import os


class SmsSettings:
    Timeout = float(os.environ.get("Timeout", 3))
    TTimeout = 2.0

    # 辅助函数，用于类型转换


def _convert_type(type_, value):
    if type_ == str:
        return str(value)
    elif type_ == bool:
        return bool(value)
    elif type_ in (int, float):
        return type_(value)
    elif type_ in (list, tuple):
        return type_(eval(value))
    else:
        raise ValueError(f"Unsupported type: {type_}")


if __name__ == '__main__':
    sms_settings = SmsSettings()

    # 获取类属性的映射，排除以双下划线开头的魔法属性
    fields_map = {k: v for k, v in vars(SmsSettings).items() if not k.startswith("__")}

    # 获取属性类型映射
    fields_map_type = {k: type(v) for k, v in fields_map.items()}
    print(fields_map_type)

    # 动态设置属性值
    dk = {"Timeout": "2.4", "KEEP_ALIVE": False}
    for k, v in dk.items():
        if hasattr(sms_settings, k):
            print(f"Setting {k} to {v}")
            setattr(sms_settings, k, _convert_type(fields_map_type[k], v))
            print(getattr(sms_settings, k))
        else:
            # print(f"No such attribute: {k}")
            setattr(sms_settings, k, v)

    print(vars(sms_settings))
