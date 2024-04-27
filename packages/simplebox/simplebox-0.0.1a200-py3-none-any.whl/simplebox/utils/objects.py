#!/usr/bin/env python
# -*- coding:utf-8 -*-
from inspect import stack, getframeinfo, currentframe
from random import sample
from collections.abc import Iterable

import regex as re
from regex import findall

from ..classes import StaticClass
from ..exceptions import raise_exception, NonePointerException
from ..generic import V, T

_base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
loc = locals()


class ObjectsUtils(metaclass=StaticClass):
    """
    object backend
    """

    @staticmethod
    def check_contains(iterable_obj: T, content: V, throw: BaseException = None):
        """
        Check whether obj contains content, and throw an exception if it does not
        """
        if not issubclass(type(throw), BaseException):
            frame = getframeinfo(currentframe().f_back)
            parameters = findall(re.compile(r".*check_contains[(](.*?)[)]", re.S), frame.code_context[0])[0].split(',')
            msg = f"object [{parameters[0]}] not contain content[{parameters[1].strip()}]."
            cause = NonePointerException(msg)
        else:
            cause = throw

        flag = False
        # noinspection PyBroadException
        try:
            if not iterable_obj or content not in iterable_obj:
                flag = True
                raise_exception(cause)
        except BaseException:
            if flag:
                raise
            else:
                raise_exception(cause)

    @staticmethod
    def check_none(obj: T, throw: BaseException = None):
        """
        if object only is not None,will raise exception
        """
        if not issubclass(type(throw), BaseException):
            frame = getframeinfo(currentframe().f_back)
            parameters = findall(re.compile(r".*check_none[(](.*?)[)]", re.S), frame.code_context[0])
            msg = f"Excepted [{parameters[0]}] is None, got not None."
            cause = NonePointerException(msg)
        else:
            cause = throw
        if obj is not None:
            raise_exception(cause)

    @staticmethod
    def check_non_none(obj: T, throw: BaseException = None):
        """
        if object only is None,will raise exception
        """
        if not issubclass(type(throw), BaseException):
            frame = getframeinfo(currentframe().f_back)
            parameters = findall(re.compile(r".*check_non_none[(](.*?)[)]", re.S), frame.code_context[0])
            msg = f"Excepted [{parameters[0]}] is not None, got None."
            cause = NonePointerException(msg)
        else:
            cause = throw
        if obj is None:
            raise_exception(cause)

    @staticmethod
    def check_any_none(iterable: Iterable[T], throw: BaseException = None):
        """
        Stop checking as long as one element is None,
        otherwise if all elements are checked and None is not found, an exception will be thrown.
        """
        if not issubclass(type(throw), BaseException):
            frame = getframeinfo(currentframe().f_back)
            parameters = findall(re.compile(r".*check_any_none[(](.*?)[)]", re.S), frame.code_context[0])
            msg = f"Excepted '{parameters[0]}' has any None, but all not found None."
            cause = NonePointerException(msg)
        else:
            cause = throw
        for i in iterable:
            if i is None:
                return
        else:
            raise_exception(cause)

    @staticmethod
    def check_all_none(iterable: Iterable[T], throw: BaseException = None):
        """
        Check that all elements are None, otherwise an exception is thrown.
        """
        if not issubclass(type(throw), BaseException):
            frame = getframeinfo(currentframe().f_back)
            parameters = findall(re.compile(r".*check_all_none[(](.*?)[)]", re.S), frame.code_context[0])
            msg = f"Excepted '{parameters[0]}' is all None, but found not None."
            cause = NonePointerException(msg)
        else:
            cause = throw
        flag = set()
        index = 0
        for i in iterable:
            index += 1
            flag.add(i is None)
        if index > 0 and not (len(flag) == 1 and True in flag):
            raise_exception(cause)

    @staticmethod
    def check_all_not_none(iterable: Iterable[T], throw: BaseException = None):
        """
        Check that all elements are not None, otherwise an exception is thrown.
        """
        if not issubclass(type(throw), BaseException):
            frame = getframeinfo(currentframe().f_back)
            parameters = findall(re.compile(r".*check_all_not_none[(](.*?)[)]", re.S), frame.code_context[0])
            msg = f"Excepted '{parameters[0]}' is all not None, but found None."
            cause = NonePointerException(msg)
        else:
            cause = throw
        flag = set()
        index = 0
        for i in iterable:
            index += 1
            flag.add(i is not None)
        if index > 0 and not (len(flag) == 1 and True in flag):
            raise_exception(cause)

    @staticmethod
    def check_empty(obj: T, throw: BaseException = None):
        """
        If the object is not None, False, empty string "", 0, empty list[], empty dictionary{}, empty tuple(),
        will raise exception
        """
        if not issubclass(type(throw), BaseException):
            frame = getframeinfo(currentframe().f_back)
            parameters = findall(re.compile(r".*check_empty[(](.*?)[)]", re.S), frame.code_context[0])
            msg = f"Excepted [{parameters[0]}] is empty, got a not empty object."
            cause = NonePointerException(msg)
        else:
            cause = throw
        if obj:  # not empty
            raise_exception(cause)

    @staticmethod
    def check_non_empty(obj: T, throw: BaseException = None):
        """
        If the object is None, False, empty string "", 0, empty list[], empty dictionary{}, empty tuple(),
        will raise exception
        """
        if not issubclass(type(throw), BaseException):
            frame = getframeinfo(currentframe().f_back)
            parameters = findall(re.compile(r".*check_non_empty[(](.*?)[)]", re.S), frame.code_context[0])
            msg = f"Excepted [{parameters[0]}] is not empty, got a empty object."
            cause = NonePointerException(msg)
        else:
            cause = throw
        if not obj:  # empty
            raise_exception(cause)

    @staticmethod
    def check_any_empty(iterable: Iterable[T], throw: BaseException = None):
        """
        Reference check_any_none.
        """
        if not issubclass(type(throw), BaseException):
            frame = getframeinfo(currentframe().f_back)
            parameters = findall(re.compile(r".*check_any_empty[(](.*?)[)]", re.S), frame.code_context[0])
            msg = f"Excepted '{parameters[0]}' has any empty, but all not found empty."
            cause = NonePointerException(msg)
        else:
            cause = throw
        for i in iterable:
            if i:  # not empty
                return
        else:
            raise_exception(cause)

    @staticmethod
    def check_all_empty(iterable: Iterable[T], throw: BaseException = None):
        """
        Reference check_all_none.
        """
        if not issubclass(type(throw), BaseException):
            frame = getframeinfo(currentframe().f_back)
            parameters = findall(re.compile(r".*check_all_empty[(](.*?)[)]", re.S), frame.code_context[0])
            msg = f"Excepted '{parameters[0]}' is all empty, but found not empty."
            cause = NonePointerException(msg)
        else:
            cause = throw
        index = 0
        flag = set()
        for i in iterable:
            index += 1
            if i:  # not empty
                flag.add(False)
            else:  # empty
                flag.add(True)
        if index > 0 and not (len(flag) == 1 and True in flag):
            raise_exception(cause)

    @staticmethod
    def check_all_not_empty(iterable: Iterable[T], throw: BaseException = None):
        """
        Reference check_all_not_none.
        """
        if not issubclass(type(throw), BaseException):
            frame = getframeinfo(currentframe().f_back)
            parameters = findall(re.compile(r".*check_all_not_empty[(](.*?)[)]", re.S), frame.code_context[0])
            msg = f"Excepted '{parameters[0]}' is all not empty, but found empty."
            cause = NonePointerException(msg)
        else:
            cause = throw
        flag = set()
        index = 0
        for i in iterable:
            index += 1
            if i:  # not empty
                flag.add(False)
            else:  # empty
                flag.add(True)
        if index > 0 and not (len(flag) == 1 and True in flag):
            raise_exception(cause)

    @staticmethod
    def none_of_default(src: T, default: T) -> T:
        """
        Judge whether SRC is empty, and return the value of default if it is empty
        :param src: Object to be judged
        :param default: Default value
        """
        if src:
            return src
        return default

    @staticmethod
    def generate_random_str(length: int = 16, base_str: str = None, prefix: str = '', suffix: str = '') -> str:
        """
        Generates a random string of a specified length
        :params length:  of generated string
        """
        ObjectsUtils.check_type(length, int)
        ObjectsUtils.check_type(base_str, str)
        ObjectsUtils.check_type(prefix, str)
        ObjectsUtils.check_type(suffix, str)
        if len(base_str) == 0 or length == 0:
            return ""
        base_str_len = len(base_str)
        if length <= base_str_len:
            content = "".join(sample(base_str, length))
        else:
            strings = []
            step = length // base_str_len
            remainder = length % base_str_len
            for _ in range(step):
                strings.extend(sample(base_str, base_str_len))
            strings.extend(sample(base_str, remainder))
            content = "".join(strings)
        return f'{suffix}{content}{prefix}'

    @staticmethod
    def get_current_function_name() -> str:
        """
        Gets the name of the current function inside the function
        """
        return stack()[1][3]

    @staticmethod
    def get_private_attribute(obj, name: str):
        """
        Gets the private property value of the object, and if it is a private method, returns the function object.
        """
        obj_name = obj.__class__.__name__
        for attribute in obj.__dir__():
            attr_name = f"_{obj_name}{name}"
            if obj_name in attribute and attr_name == attribute:
                return getattr(obj, attr_name)
        return None

    @staticmethod
    def call_limit(func_file=None, func_names=None):
        """
        Limit the call of functions
        example:
            a.py
                def inner_f1():
                    # expect to only be called in the a.py
                    ObjectUtils.call_limit('a.py')
                def f1():
                    inner_f1() # call success.
            b.py
                from a import inner_f1
                def f():
                    inner_f1() # raise exception.
        """
        called = stack()[1]
        call_enter = stack()[2]
        if func_file != call_enter.filename or (func_names and call_enter.function not in func_names):
            frame = called.frame
            if params := frame.f_locals:
                if "self" in params:
                    name = params.get("self").__class__.__name__
                    raise RuntimeError(f"'{name}' is restricted from being called.")
                else:
                    raise RuntimeError(f"limit calls.")
            else:
                raise RuntimeError(f"'{called.function}' is restricted from being called.")

    @staticmethod
    def check_type(src_type: type, except_type: type or tuple[type]):
        """
        check that src_type is a subclass of except_type.
        :param src_type:
        :param except_type:
        :return:
        """
        if not isinstance(src_type, type):
            raise TypeError(f'excepted type is \'type\', got a \'{type(src_type)}\'')
        if isinstance(except_type, tuple):
            for t in except_type:
                if not isinstance(t, type):
                    raise TypeError(f'excepted type is \'type\', got a \'{type(t)}\'')
        else:
            if not isinstance(except_type, type):
                raise TypeError(f'excepted type is \'type\', got a \'{type(except_type)}\'')

        if not issubclass(t_ := type(src_type), except_type):
            raise TypeError(f'excepted type is \'{except_type}\', got a \'{t_}\'')

    @staticmethod
    def check_instance(instance, except_type: type or tuple[type]):
        """
        check that instance is an instance of except_type.

        """
        if isinstance(except_type, tuple):
            for t in except_type:
                if not isinstance(t, type):
                    raise TypeError(f'excepted type is \'type\', got a \'{type(t)}\'')
        else:
            if not isinstance(except_type, type):
                raise TypeError(f'excepted type is \'type\', got a \'{type(except_type)}\'')
        if not isinstance(instance, except_type):
            raise TypeError(f'excepted type is \'{except_type}\', got a \'{type(instance)}\'')


__all__ = [ObjectsUtils]
