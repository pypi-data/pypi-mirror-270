from big_thing_py.utils import *
from big_thing_py.core import MXThing
import functools
import asyncio


def list_arg_to_str(list_arg: List[Union[int, float, bool, str]]) -> str:
    formatted_list = []
    for x in list_arg:
        if isinstance(x, bool):
            formatted_list.append(str(x))
        elif isinstance(x, float):
            formatted_list.append(f"{x:.4f}")
        elif isinstance(x, (int, str)):
            formatted_list.append(str(x))
        else:
            raise ValueError(f"Unsupported type: {type(x)}")
    return '|'.join(formatted_list)


def print_func_info(func: Callable) -> None:

    @functools.wraps(func)
    async def async_wrap(self: MXThing, *args, **kwargs):
        # MXLOG_DEBUG 호출
        MXLOG_DEBUG(f'{func.__name__} at {self._name} actuate!!!', 'green')
        # 원래 함수 호출
        ret = await func(self, *args, **kwargs)
        return ret

    @functools.wraps(func)
    def sync_wrap(self: MXThing, *args, **kwargs):
        # MXLOG_DEBUG 호출
        MXLOG_DEBUG(f'{func.__name__} at {self._name} actuate!!!', 'green')
        # 원래 함수 호출
        ret = func(self, *args, **kwargs)
        return ret

    if asyncio.iscoroutinefunction(func):
        async_wrap.is_decorated = True
        return async_wrap
    else:
        sync_wrap.is_decorated = True
        return sync_wrap


def find_class_in_hierarchy(instance, target_class) -> bool:
    current_class = type(instance)

    while current_class is not object:
        if issubclass(current_class, target_class):
            return True
        current_class = current_class.__base__

    return False


def color_to_str(color0: Union[int, float], color1: Union[int, float], color2: Union[int, float]) -> str:
    return f'{color0:0.4f}|{color1:0.4f}|{color2:0.4f}'


def str_to_color(color_str: str) -> Tuple[int, int, int]:
    return tuple(map(float, color_str.split('|')))
