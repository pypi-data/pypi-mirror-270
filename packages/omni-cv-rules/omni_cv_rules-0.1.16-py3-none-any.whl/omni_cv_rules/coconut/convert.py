#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xd2e969c0

# Compiled with Coconut version 3.1.0

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.0', '35', False)
_coconut_cached__coconut__ = _coconut_sys.modules.get('__coconut__')
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules['_coconut_cached__coconut__'] = _coconut_cached__coconut__
        del _coconut_sys.modules['__coconut__']
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == '__coconut__':
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == '__coconut__':
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and '__coconut_cache__' in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != '__coconut_cache__':
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

import numpy as np  #1: import numpy as np
from PIL import Image  #2: from PIL import Image
import re  #3: import re
from frozendict import frozendict as fdict  #4: from frozendict import frozendict as fdict
from frozendict import frozendict  #5: from frozendict import frozendict
from omni_cv_rules.py_38.torch_rules import ycbcr_to_rgb  #6: from omni_cv_rules.py_38.torch_rules import ycbcr_to_rgb,rgb_to_ycbcr
from omni_cv_rules.py_38.torch_rules import rgb_to_ycbcr  #6: from omni_cv_rules.py_38.torch_rules import ycbcr_to_rgb,rgb_to_ycbcr
from omni_cv_rules.place_holder.torch_proxy import torch  #7: from omni_cv_rules.place_holder.torch_proxy import torch
VR_0_1 = "0_1"  #8: VR_0_1 = "0_1"
VR_0_255 = "0_255"  #9: VR_0_255 = "0_255"
VR_None = "None"  #10: VR_None = "None"
VR_XYZ_Normalized = "XYZ_Normalized"  #11: VR_XYZ_Normalized = "XYZ_Normalized"
ch_splitter = re.compile("[A-Z][a-z]*").findall  #12: ch_splitter = re.compile("[A-Z][a-z]*").findall
class DataType(_coconut.collections.namedtuple("DataType", ())):  #13: data DataType
    __slots__ = ()  #13: data DataType
    _coconut_is_data = True  #13: data DataType
    __match_args__ = ()  #13: data DataType
    def __add__(self, other): return _coconut.NotImplemented  #13: data DataType
    def __mul__(self, other): return _coconut.NotImplemented  #13: data DataType
    def __rmul__(self, other): return _coconut.NotImplemented  #13: data DataType
    __ne__ = _coconut.object.__ne__  #13: data DataType
    def __eq__(self, other):  #13: data DataType
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #13: data DataType
    def __hash__(self):  #13: data DataType
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #13: data DataType

#TODO add shape information to tensorlike
#TODO add shape information to PILImage
#TODO make rules be able to handle other metadata.
#so let's assume the input state based on dict.

_coconut_call_set_names(DataType)  #19: KNOWN_COLOR_FMTS = {
KNOWN_COLOR_FMTS = {"HSV", "YCbCr", "RGB", "RGBA", "LAB", "CMYK"}  #19: KNOWN_COLOR_FMTS = {

class TensorLike(_coconut.collections.namedtuple("TensorLike", ('dtype', 'arrange', 'channel_repr', 'value_range')), DataType):  #28: data TensorLike(
    __slots__ = ()  #28: data TensorLike(
    _coconut_is_data = True  #28: data TensorLike(
    __match_args__ = ('dtype', 'arrange', 'channel_repr', 'value_range')  #28: data TensorLike(
    def __add__(self, other): return _coconut.NotImplemented  #28: data TensorLike(
    def __mul__(self, other): return _coconut.NotImplemented  #28: data TensorLike(
    def __rmul__(self, other): return _coconut.NotImplemented  #28: data TensorLike(
    __ne__ = _coconut.object.__ne__  #28: data TensorLike(
    def __eq__(self, other):  #28: data TensorLike(
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #28: data TensorLike(
    def __hash__(self):  #28: data TensorLike(
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #28: data TensorLike(
    def __new__(_coconut_cls, _coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #28: data TensorLike(
        _coconut_match_check_0 = False  #28: data TensorLike(
        _coconut_match_set_name_dtype = _coconut_sentinel  #28: data TensorLike(
        _coconut_match_set_name_arrange = _coconut_sentinel  #28: data TensorLike(
        _coconut_match_set_name_channel_repr = _coconut_sentinel  #28: data TensorLike(
        _coconut_match_set_name_value_range = _coconut_sentinel  #28: data TensorLike(
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #28: data TensorLike(
        if _coconut_match_first_arg is not _coconut_sentinel:  #28: data TensorLike(
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #28: data TensorLike(
        if (_coconut.len(_coconut_match_args) <= 4) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "dtype" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "arrange" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "channel_repr" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "value_range" in _coconut_match_kwargs)) == 1):  #28: data TensorLike(
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("dtype")  #28: data TensorLike(
            _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("arrange")  #28: data TensorLike(
            _coconut_match_temp_2 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("channel_repr")  #28: data TensorLike(
            _coconut_match_temp_3 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("value_range")  #28: data TensorLike(
            if (_coconut.isinstance(_coconut_match_temp_0, str)) and (_coconut.isinstance(_coconut_match_temp_1, str)) and (_coconut.isinstance(_coconut_match_temp_2, str)) and (_coconut.isinstance(_coconut_match_temp_3, str)):  #28: data TensorLike(
                _coconut_match_set_name_dtype = _coconut_match_temp_0  #28: data TensorLike(
                _coconut_match_set_name_arrange = _coconut_match_temp_1  #28: data TensorLike(
                _coconut_match_set_name_channel_repr = _coconut_match_temp_2  #28: data TensorLike(
                _coconut_match_set_name_value_range = _coconut_match_temp_3  #28: data TensorLike(
                if not _coconut_match_kwargs:  #28: data TensorLike(
                    _coconut_match_check_0 = True  #28: data TensorLike(
        if _coconut_match_check_0:  #28: data TensorLike(
            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #28: data TensorLike(
                dtype = _coconut_match_set_name_dtype  #28: data TensorLike(
            if _coconut_match_set_name_arrange is not _coconut_sentinel:  #28: data TensorLike(
                arrange = _coconut_match_set_name_arrange  #28: data TensorLike(
            if _coconut_match_set_name_channel_repr is not _coconut_sentinel:  #28: data TensorLike(
                channel_repr = _coconut_match_set_name_channel_repr  #28: data TensorLike(
            if _coconut_match_set_name_value_range is not _coconut_sentinel:  #28: data TensorLike(
                value_range = _coconut_match_set_name_value_range  #28: data TensorLike(

        if not _coconut_match_check_0:  #28: data TensorLike(
            raise _coconut_FunctionMatchError('data TensorLike(', _coconut_match_args)  #28: data TensorLike(

        return _coconut.tuple.__new__(_coconut_cls, (dtype, arrange, channel_repr, value_range))  #28: data TensorLike(
    def __repr__(self):  #33:     def __repr__(self):
        return ("Tensor({_coconut_format_0}|{_coconut_format_1}|{_coconut_format_2}|{_coconut_format_3}|{_coconut_format_4})".format(_coconut_format_0=(self.data_type), _coconut_format_1=(self.dtype), _coconut_format_2=(self.arrange), _coconut_format_3=(self.channel_repr), _coconut_format_4=(self.value_range)))  #34:         return f"Tensor({self.data_type}|{self.dtype}|{self.arrange}|{self.channel_repr}|{self.value_range})"


_coconut_call_set_names(TensorLike)  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
class Numpy(_coconut.collections.namedtuple("Numpy", ('dtype', 'arrange', 'channel_repr', 'value_range')), TensorLike):  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
    __slots__ = ()  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
    _coconut_is_data = True  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
    __match_args__ = ('dtype', 'arrange', 'channel_repr', 'value_range')  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __add__(self, other): return _coconut.NotImplemented  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __mul__(self, other): return _coconut.NotImplemented  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __rmul__(self, other): return _coconut.NotImplemented  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
    __ne__ = _coconut.object.__ne__  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __eq__(self, other):  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __hash__(self):  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #36: data Numpy(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __new__(cls, *args):  #37:     def __new__(cls,*args):
        return (makedata(cls, *args))  #38:         return makedata(cls,*args)

    def __repr__(self):  #39:     def __repr__(self):
        return ("Numpy({_coconut_format_0},{_coconut_format_1},{_coconut_format_2},{_coconut_format_3})".format(_coconut_format_0=(self.dtype), _coconut_format_1=(self.arrange), _coconut_format_2=(self.channel_repr), _coconut_format_3=(self.value_range)))  #40:         return f"Numpy({self.dtype},{self.arrange},{self.channel_repr},{self.value_range})"


_coconut_call_set_names(Numpy)  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
class Torch(_coconut.collections.namedtuple("Torch", ('dtype', 'arrange', 'channel_repr', 'value_range')), TensorLike):  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
    __slots__ = ()  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
    _coconut_is_data = True  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
    __match_args__ = ('dtype', 'arrange', 'channel_repr', 'value_range')  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __add__(self, other): return _coconut.NotImplemented  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __mul__(self, other): return _coconut.NotImplemented  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __rmul__(self, other): return _coconut.NotImplemented  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
    __ne__ = _coconut.object.__ne__  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __eq__(self, other):  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __hash__(self):  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #42: data Torch(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __new__(cls, *args):  #43:     def __new__(cls,*args):
        return (makedata(cls, *args))  #44:         return makedata(cls,*args)

    def __repr__(self):  #45:     def __repr__(self):
        return ("Torch({_coconut_format_0},{_coconut_format_1},{_coconut_format_2},{_coconut_format_3})".format(_coconut_format_0=(self.dtype), _coconut_format_1=(self.arrange), _coconut_format_2=(self.channel_repr), _coconut_format_3=(self.value_range)))  #46:         return f"Torch({self.dtype},{self.arrange},{self.channel_repr},{self.value_range})"


_coconut_call_set_names(Torch)  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
class Hdf5(_coconut.collections.namedtuple("Hdf5", ('dtype', 'arrange', 'channel_repr', 'value_range')), TensorLike):  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
    __slots__ = ()  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
    _coconut_is_data = True  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
    __match_args__ = ('dtype', 'arrange', 'channel_repr', 'value_range')  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __add__(self, other): return _coconut.NotImplemented  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __mul__(self, other): return _coconut.NotImplemented  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __rmul__(self, other): return _coconut.NotImplemented  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
    __ne__ = _coconut.object.__ne__  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __eq__(self, other):  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __hash__(self):  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #48: data Hdf5(dtype,arrange,channel_repr,value_range) from TensorLike:
    def __new__(cls, *args):  #49:     def __new__(cls,*args):
        return (makedata(cls, *args))  #50:         return makedata(cls,*args)

    def __repr__(self):  #51:     def __repr__(self):
        return ("Hdf5({_coconut_format_0},{_coconut_format_1},{_coconut_format_2},{_coconut_format_3})".format(_coconut_format_0=(self.dtype), _coconut_format_1=(self.arrange), _coconut_format_2=(self.channel_repr), _coconut_format_3=(self.value_range)))  #52:         return f"Hdf5({self.dtype},{self.arrange},{self.channel_repr},{self.value_range})"

# represents iterable of PIL.Images
_coconut_call_set_names(Hdf5)  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
class PILImages(_coconut.collections.namedtuple("PILImages", ('mode', 'channel_repr')), DataType):  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
    __slots__ = ()  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
    _coconut_is_data = True  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
    __match_args__ = ('mode', 'channel_repr')  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
    def __add__(self, other): return _coconut.NotImplemented  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
    def __mul__(self, other): return _coconut.NotImplemented  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
    def __rmul__(self, other): return _coconut.NotImplemented  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
    __ne__ = _coconut.object.__ne__  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
    def __eq__(self, other):  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
    def __hash__(self):  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  # represents iterable of PIL.Images  #54: data PILImages(mode,channel_repr) from DataType: # represents iterable of PIL.Images
    def __repr__(self):  #55:     def __repr__(self):
        return ("PILImages({_coconut_format_0},{_coconut_format_1})".format(_coconut_format_0=(self.mode), _coconut_format_1=(self.channel_repr)))  #56:         return f"PILImages({self.mode},{self.channel_repr})"

_coconut_call_set_names(PILImages)  #57: data PILImage(mode,channel_repr) from DataType:
class PILImage(_coconut.collections.namedtuple("PILImage", ('mode', 'channel_repr')), DataType):  #57: data PILImage(mode,channel_repr) from DataType:
    __slots__ = ()  #57: data PILImage(mode,channel_repr) from DataType:
    _coconut_is_data = True  #57: data PILImage(mode,channel_repr) from DataType:
    __match_args__ = ('mode', 'channel_repr')  #57: data PILImage(mode,channel_repr) from DataType:
    def __add__(self, other): return _coconut.NotImplemented  #57: data PILImage(mode,channel_repr) from DataType:
    def __mul__(self, other): return _coconut.NotImplemented  #57: data PILImage(mode,channel_repr) from DataType:
    def __rmul__(self, other): return _coconut.NotImplemented  #57: data PILImage(mode,channel_repr) from DataType:
    __ne__ = _coconut.object.__ne__  #57: data PILImage(mode,channel_repr) from DataType:
    def __eq__(self, other):  #57: data PILImage(mode,channel_repr) from DataType:
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #57: data PILImage(mode,channel_repr) from DataType:
    def __hash__(self):  #57: data PILImage(mode,channel_repr) from DataType:
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #57: data PILImage(mode,channel_repr) from DataType:
    def __repr__(self):  #58:     def __repr__(self):
        return ("PILImage({_coconut_format_0},{_coconut_format_1})".format(_coconut_format_0=(self.mode), _coconut_format_1=(self.channel_repr)))  #59:         return f"PILImage({self.mode},{self.channel_repr})"


_coconut_call_set_names(PILImage)  #61: data ImageDef(data_type is DataType,meta is frozendict):
class ImageDef(_coconut.collections.namedtuple("ImageDef", ('data_type', 'meta'))):  #61: data ImageDef(data_type is DataType,meta is frozendict):
    __slots__ = ()  #61: data ImageDef(data_type is DataType,meta is frozendict):
    _coconut_is_data = True  #61: data ImageDef(data_type is DataType,meta is frozendict):
    __match_args__ = ('data_type', 'meta')  #61: data ImageDef(data_type is DataType,meta is frozendict):
    def __add__(self, other): return _coconut.NotImplemented  #61: data ImageDef(data_type is DataType,meta is frozendict):
    def __mul__(self, other): return _coconut.NotImplemented  #61: data ImageDef(data_type is DataType,meta is frozendict):
    def __rmul__(self, other): return _coconut.NotImplemented  #61: data ImageDef(data_type is DataType,meta is frozendict):
    __ne__ = _coconut.object.__ne__  #61: data ImageDef(data_type is DataType,meta is frozendict):
    def __eq__(self, other):  #61: data ImageDef(data_type is DataType,meta is frozendict):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #61: data ImageDef(data_type is DataType,meta is frozendict):
    def __hash__(self):  #61: data ImageDef(data_type is DataType,meta is frozendict):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #61: data ImageDef(data_type is DataType,meta is frozendict):
    def __new__(_coconut_cls, _coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #61: data ImageDef(data_type is DataType,meta is frozendict):
        _coconut_match_check_1 = False  #61: data ImageDef(data_type is DataType,meta is frozendict):
        _coconut_match_set_name_data_type = _coconut_sentinel  #61: data ImageDef(data_type is DataType,meta is frozendict):
        _coconut_match_set_name_meta = _coconut_sentinel  #61: data ImageDef(data_type is DataType,meta is frozendict):
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #61: data ImageDef(data_type is DataType,meta is frozendict):
        if _coconut_match_first_arg is not _coconut_sentinel:  #61: data ImageDef(data_type is DataType,meta is frozendict):
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #61: data ImageDef(data_type is DataType,meta is frozendict):
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "data_type" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "meta" in _coconut_match_kwargs)) == 1):  #61: data ImageDef(data_type is DataType,meta is frozendict):
            _coconut_match_temp_4 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("data_type")  #61: data ImageDef(data_type is DataType,meta is frozendict):
            _coconut_match_temp_5 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("meta")  #61: data ImageDef(data_type is DataType,meta is frozendict):
            if (_coconut.isinstance(_coconut_match_temp_4, DataType)) and (_coconut.isinstance(_coconut_match_temp_5, frozendict)):  #61: data ImageDef(data_type is DataType,meta is frozendict):
                _coconut_match_set_name_data_type = _coconut_match_temp_4  #61: data ImageDef(data_type is DataType,meta is frozendict):
                _coconut_match_set_name_meta = _coconut_match_temp_5  #61: data ImageDef(data_type is DataType,meta is frozendict):
                if not _coconut_match_kwargs:  #61: data ImageDef(data_type is DataType,meta is frozendict):
                    _coconut_match_check_1 = True  #61: data ImageDef(data_type is DataType,meta is frozendict):
        if _coconut_match_check_1:  #61: data ImageDef(data_type is DataType,meta is frozendict):
            if _coconut_match_set_name_data_type is not _coconut_sentinel:  #61: data ImageDef(data_type is DataType,meta is frozendict):
                data_type = _coconut_match_set_name_data_type  #61: data ImageDef(data_type is DataType,meta is frozendict):
            if _coconut_match_set_name_meta is not _coconut_sentinel:  #61: data ImageDef(data_type is DataType,meta is frozendict):
                meta = _coconut_match_set_name_meta  #61: data ImageDef(data_type is DataType,meta is frozendict):

        if not _coconut_match_check_1:  #61: data ImageDef(data_type is DataType,meta is frozendict):
            raise _coconut_FunctionMatchError('data ImageDef(data_type is DataType,meta is frozendict):', _coconut_match_args)  #61: data ImageDef(data_type is DataType,meta is frozendict):

        return _coconut.tuple.__new__(_coconut_cls, (data_type, meta))  #61: data ImageDef(data_type is DataType,meta is frozendict):
    def __repr__(self):  #66:     def __repr__(self):
        if self.meta:  #67:         if self.meta:
            return ("ImageDef({_coconut_format_0}|{_coconut_format_1})".format(_coconut_format_0=(self.data_type), _coconut_format_1=(self.meta)))  #68:             return f"ImageDef({self.data_type}|{self.meta})"
        else:  #69:         else:
            return ("ImageDef({_coconut_format_0})".format(_coconut_format_0=(self.data_type)))  #70:             return f"ImageDef({self.data_type})"


_coconut_call_set_names(ImageDef)  #72: DTYPES={"float32","float64","int32","int64","uint8","bool"}
DTYPES = {"float32", "float64", "int32", "int64", "uint8", "bool"}  #72: DTYPES={"float32","float64","int32","int64","uint8","bool"}
class DataEdge(_coconut.collections.namedtuple("DataEdge", ('a', 'b', 'f', 'cost', 'name', 'meta_shifter'))):  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
    __slots__ = ()  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
    _coconut_is_data = True  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
    __match_args__ = ('a', 'b', 'f', 'cost', 'name', 'meta_shifter')  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
    def __add__(self, other): return _coconut.NotImplemented  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
    def __mul__(self, other): return _coconut.NotImplemented  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
    def __rmul__(self, other): return _coconut.NotImplemented  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
    __ne__ = _coconut.object.__ne__  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
    def __eq__(self, other):  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
    def __hash__(self):  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
    def __new__(_coconut_cls, _coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        _coconut_match_check_2 = False  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        _coconut_match_set_name_a = _coconut_sentinel  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        _coconut_match_set_name_b = _coconut_sentinel  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        _coconut_match_set_name_f = _coconut_sentinel  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        _coconut_match_set_name_cost = _coconut_sentinel  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        _coconut_match_set_name_name = _coconut_sentinel  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        _coconut_match_set_name_meta_shifter = _coconut_sentinel  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        if _coconut_match_first_arg is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        if (_coconut.len(_coconut_match_args) <= 6) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "a" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "b" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "f" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "cost" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 4, "name" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 5, "meta_shifter" in _coconut_match_kwargs)) <= 1):  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            _coconut_match_temp_20 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("a")  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            _coconut_match_temp_21 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("b")  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            _coconut_match_temp_22 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("f")  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            _coconut_match_temp_23 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("cost")  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            _coconut_match_temp_24 = _coconut_match_args[4] if _coconut.len(_coconut_match_args) > 4 else _coconut_match_kwargs.pop("name")  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            _coconut_match_temp_25 = _coconut_match_args[5] if _coconut.len(_coconut_match_args) > 5 else _coconut_match_kwargs.pop("meta_shifter") if "meta_shifter" in _coconut_match_kwargs else _coconut_sentinel  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            if (_coconut.isinstance(_coconut_match_temp_20, DataType)) and (_coconut.isinstance(_coconut_match_temp_21, DataType)) and (_coconut.isinstance(_coconut_match_temp_23, int)) and (_coconut.isinstance(_coconut_match_temp_24, str)):  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                _coconut_match_set_name_a = _coconut_match_temp_20  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                _coconut_match_set_name_b = _coconut_match_temp_21  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                _coconut_match_set_name_f = _coconut_match_temp_22  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                _coconut_match_set_name_cost = _coconut_match_temp_23  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                _coconut_match_set_name_name = _coconut_match_temp_24  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                if _coconut_match_temp_25 is _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                    _coconut_match_temp_26 = _coconut.globals().copy()  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                    _coconut_match_temp_26.update(_coconut.locals())  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                    if _coconut_match_set_name_a is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                        _coconut_match_temp_26["a"] = _coconut_match_set_name_a  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                    if _coconut_match_set_name_b is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                        _coconut_match_temp_26["b"] = _coconut_match_set_name_b  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                    if _coconut_match_set_name_f is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                        _coconut_match_temp_26["f"] = _coconut_match_set_name_f  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                    if _coconut_match_set_name_cost is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                        _coconut_match_temp_26["cost"] = _coconut_match_set_name_cost  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                    if _coconut_match_set_name_name is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                        _coconut_match_temp_26["name"] = _coconut_match_set_name_name  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                    _coconut_exec('_coconut_match_temp_25 = lambda x: x', _coconut_match_temp_26)  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                    _coconut_match_temp_25 = _coconut_match_temp_26["_coconut_match_temp_25"]  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                _coconut_match_set_name_meta_shifter = _coconut_match_temp_25  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                if not _coconut_match_kwargs:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                    _coconut_match_check_2 = True  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
        if _coconut_match_check_2:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            if _coconut_match_set_name_a is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                a = _coconut_match_set_name_a  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            if _coconut_match_set_name_b is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                b = _coconut_match_set_name_b  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            if _coconut_match_set_name_f is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                f = _coconut_match_set_name_f  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            if _coconut_match_set_name_cost is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                cost = _coconut_match_set_name_cost  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            if _coconut_match_set_name_name is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                name = _coconut_match_set_name_name  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            if _coconut_match_set_name_meta_shifter is not _coconut_sentinel:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
                meta_shifter = _coconut_match_set_name_meta_shifter  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):

        if not _coconut_match_check_2:  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
            raise _coconut_FunctionMatchError('data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):', _coconut_match_args)  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):

        return _coconut.tuple.__new__(_coconut_cls, (a, b, f, cost, name, meta_shifter))  #73: data DataEdge(a is DataType,b is DataType,f,cost is int,name is str,meta_shifter=x->x):
    def to_edge(self, src: 'ImageDef'):  #74:     def to_edge(self,src:ImageDef):
        try:  #75:         try:
            new_meta = self.meta_shifter(src.meta)  #76:             new_meta = self.meta_shifter(src.meta)

            return (Edge(src, ImageDef(self.b, new_meta), self.f, self.cost, self.name))  #78:             return Edge(src,ImageDef(self.b,new_meta),self.f,self.cost,self.name)
            _coconut_case_match_to_0 = (self.a, src.meta, self.b, new_meta)  #79:             case (self.a,src.meta,self.b,new_meta):
            _coconut_case_match_check_0 = False  #79:             case (self.a,src.meta,self.b,new_meta):
            _coconut_match_set_name_s1 = _coconut_sentinel  #79:             case (self.a,src.meta,self.b,new_meta):
            _coconut_match_set_name_s2 = _coconut_sentinel  #79:             case (self.a,src.meta,self.b,new_meta):
            if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 4) and (_coconut.isinstance(_coconut_case_match_to_0[1], _coconut.abc.Mapping)) and (_coconut.isinstance(_coconut_case_match_to_0[3], _coconut.abc.Mapping)):  #79:             case (self.a,src.meta,self.b,new_meta):
                _coconut_match_temp_6 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #79:             case (self.a,src.meta,self.b,new_meta):
                _coconut_match_temp_12 = _coconut_case_match_to_0[1].get("shape", _coconut_sentinel)  #79:             case (self.a,src.meta,self.b,new_meta):
                _coconut_match_temp_13 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #79:             case (self.a,src.meta,self.b,new_meta):
                _coconut_match_temp_19 = _coconut_case_match_to_0[3].get("shape", _coconut_sentinel)  #79:             case (self.a,src.meta,self.b,new_meta):
                if (_coconut_match_temp_12 is not _coconut_sentinel) and (_coconut_match_temp_19 is not _coconut_sentinel):  #79:             case (self.a,src.meta,self.b,new_meta):
                    _coconut_match_set_name_s1 = _coconut_match_temp_12  #79:             case (self.a,src.meta,self.b,new_meta):
                    _coconut_match_set_name_s2 = _coconut_match_temp_19  #79:             case (self.a,src.meta,self.b,new_meta):
                    _coconut_case_match_check_0 = True  #79:             case (self.a,src.meta,self.b,new_meta):
            if _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                _coconut_case_match_check_0 = False  #79:             case (self.a,src.meta,self.b,new_meta):
                if not _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                    _coconut_match_set_name_arng1 = _coconut_sentinel  #79:             case (self.a,src.meta,self.b,new_meta):
                    if (_coconut_match_temp_6) and (_coconut.isinstance(_coconut_case_match_to_0[0], TensorLike)) and (_coconut.len(_coconut_case_match_to_0[0]) >= 2):  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_match_set_name_arng1 = _coconut_case_match_to_0[0][1]  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_case_match_check_0 = True  #79:             case (self.a,src.meta,self.b,new_meta):
                    if _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                        if _coconut_match_set_name_arng1 is not _coconut_sentinel:  #79:             case (self.a,src.meta,self.b,new_meta):
                            arng1 = _coconut_match_set_name_arng1  #79:             case (self.a,src.meta,self.b,new_meta):

                if not _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                    if (not _coconut_match_temp_6) and (_coconut.isinstance(_coconut_case_match_to_0[0], TensorLike)):  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_match_temp_11 = _coconut.getattr(TensorLike, '__match_args__', ())  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_match_temp_10 = _coconut.tuple(_coconut.getattr(_coconut_case_match_to_0[0], _coconut_match_temp_11[i]) for i in _coconut.range(2, _coconut.len(_coconut_match_temp_11)))  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_case_match_check_0 = True  #79:             case (self.a,src.meta,self.b,new_meta):
                    if _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_case_match_check_0 = False  #79:             case (self.a,src.meta,self.b,new_meta):
                        if not _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                            if _coconut.type(_coconut_case_match_to_0[0]) in _coconut_self_match_types:  #79:             case (self.a,src.meta,self.b,new_meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports 1)")  #79:             case (self.a,src.meta,self.b,new_meta):
                                _coconut_case_match_check_0 = True  #79:             case (self.a,src.meta,self.b,new_meta):

                        if not _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                            _coconut_match_set_name_arng1 = _coconut_sentinel  #79:             case (self.a,src.meta,self.b,new_meta):
                            if not _coconut.type(_coconut_case_match_to_0[0]) in _coconut_self_match_types:  #79:             case (self.a,src.meta,self.b,new_meta):
                                _coconut_match_temp_7 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #79:             case (self.a,src.meta,self.b,new_meta):
                                if not _coconut.isinstance(_coconut_match_temp_7, _coconut.tuple):  #79:             case (self.a,src.meta,self.b,new_meta):
                                    raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #79:             case (self.a,src.meta,self.b,new_meta):
                                if _coconut.len(_coconut_match_temp_7) < 2:  #79:             case (self.a,src.meta,self.b,new_meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_7),))  #79:             case (self.a,src.meta,self.b,new_meta):
                                _coconut_match_temp_8 = _coconut.getattr(_coconut_case_match_to_0[0], _coconut_match_temp_7[0], _coconut_sentinel)  #79:             case (self.a,src.meta,self.b,new_meta):
                                _coconut_match_temp_9 = _coconut.getattr(_coconut_case_match_to_0[0], _coconut_match_temp_7[1], _coconut_sentinel)  #79:             case (self.a,src.meta,self.b,new_meta):
                                if (_coconut_match_temp_8 is not _coconut_sentinel) and (_coconut_match_temp_9 is not _coconut_sentinel):  #79:             case (self.a,src.meta,self.b,new_meta):
                                    _coconut_match_set_name_arng1 = _coconut_match_temp_9  #79:             case (self.a,src.meta,self.b,new_meta):
                                    _coconut_case_match_check_0 = True  #79:             case (self.a,src.meta,self.b,new_meta):
                            if _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                                if _coconut_match_set_name_arng1 is not _coconut_sentinel:  #79:             case (self.a,src.meta,self.b,new_meta):
                                    arng1 = _coconut_match_set_name_arng1  #79:             case (self.a,src.meta,self.b,new_meta):




            if _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                _coconut_case_match_check_0 = False  #79:             case (self.a,src.meta,self.b,new_meta):
                if not _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                    _coconut_match_set_name_arng2 = _coconut_sentinel  #79:             case (self.a,src.meta,self.b,new_meta):
                    if (_coconut_match_temp_13) and (_coconut.isinstance(_coconut_case_match_to_0[2], TensorLike)) and (_coconut.len(_coconut_case_match_to_0[2]) >= 2):  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_match_set_name_arng2 = _coconut_case_match_to_0[2][1]  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_case_match_check_0 = True  #79:             case (self.a,src.meta,self.b,new_meta):
                    if _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                        if _coconut_match_set_name_arng2 is not _coconut_sentinel:  #79:             case (self.a,src.meta,self.b,new_meta):
                            arng2 = _coconut_match_set_name_arng2  #79:             case (self.a,src.meta,self.b,new_meta):

                if not _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                    if (not _coconut_match_temp_13) and (_coconut.isinstance(_coconut_case_match_to_0[2], TensorLike)):  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_match_temp_18 = _coconut.getattr(TensorLike, '__match_args__', ())  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_match_temp_17 = _coconut.tuple(_coconut.getattr(_coconut_case_match_to_0[2], _coconut_match_temp_18[i]) for i in _coconut.range(2, _coconut.len(_coconut_match_temp_18)))  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_case_match_check_0 = True  #79:             case (self.a,src.meta,self.b,new_meta):
                    if _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                        _coconut_case_match_check_0 = False  #79:             case (self.a,src.meta,self.b,new_meta):
                        if not _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                            if _coconut.type(_coconut_case_match_to_0[2]) in _coconut_self_match_types:  #79:             case (self.a,src.meta,self.b,new_meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports 1)")  #79:             case (self.a,src.meta,self.b,new_meta):
                                _coconut_case_match_check_0 = True  #79:             case (self.a,src.meta,self.b,new_meta):

                        if not _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                            _coconut_match_set_name_arng2 = _coconut_sentinel  #79:             case (self.a,src.meta,self.b,new_meta):
                            if not _coconut.type(_coconut_case_match_to_0[2]) in _coconut_self_match_types:  #79:             case (self.a,src.meta,self.b,new_meta):
                                _coconut_match_temp_14 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #79:             case (self.a,src.meta,self.b,new_meta):
                                if not _coconut.isinstance(_coconut_match_temp_14, _coconut.tuple):  #79:             case (self.a,src.meta,self.b,new_meta):
                                    raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #79:             case (self.a,src.meta,self.b,new_meta):
                                if _coconut.len(_coconut_match_temp_14) < 2:  #79:             case (self.a,src.meta,self.b,new_meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_14),))  #79:             case (self.a,src.meta,self.b,new_meta):
                                _coconut_match_temp_15 = _coconut.getattr(_coconut_case_match_to_0[2], _coconut_match_temp_14[0], _coconut_sentinel)  #79:             case (self.a,src.meta,self.b,new_meta):
                                _coconut_match_temp_16 = _coconut.getattr(_coconut_case_match_to_0[2], _coconut_match_temp_14[1], _coconut_sentinel)  #79:             case (self.a,src.meta,self.b,new_meta):
                                if (_coconut_match_temp_15 is not _coconut_sentinel) and (_coconut_match_temp_16 is not _coconut_sentinel):  #79:             case (self.a,src.meta,self.b,new_meta):
                                    _coconut_match_set_name_arng2 = _coconut_match_temp_16  #79:             case (self.a,src.meta,self.b,new_meta):
                                    _coconut_case_match_check_0 = True  #79:             case (self.a,src.meta,self.b,new_meta):
                            if _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                                if _coconut_match_set_name_arng2 is not _coconut_sentinel:  #79:             case (self.a,src.meta,self.b,new_meta):
                                    arng2 = _coconut_match_set_name_arng2  #79:             case (self.a,src.meta,self.b,new_meta):




            if _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                if _coconut_match_set_name_s1 is not _coconut_sentinel:  #79:             case (self.a,src.meta,self.b,new_meta):
                    s1 = _coconut_match_set_name_s1  #79:             case (self.a,src.meta,self.b,new_meta):
                if _coconut_match_set_name_s2 is not _coconut_sentinel:  #79:             case (self.a,src.meta,self.b,new_meta):
                    s2 = _coconut_match_set_name_s2  #79:             case (self.a,src.meta,self.b,new_meta):
            if _coconut_case_match_check_0:  #79:             case (self.a,src.meta,self.b,new_meta):
                assert len(arng2) == len(s2)  #81:                     assert len(arng2) == len(s2)
                assert len(arng1) == len(s1)  #82:                     assert len(arng1) == len(s1)
            if src.meta != new_meta:  #83:             if src.meta != new_meta:
                if "shape" in src.meta and "shape" in new_meta:  #84:                 if "shape" in src.meta and "shape" in new_meta:
                    if len(src.meta["shape"]) > len(new_meta["shape"]):  #85:                     if len(src.meta["shape"]) > len(new_meta["shape"]):
                        from loguru import logger  #86:                         from loguru import logger
                        logger.info("{_coconut_format_0}:\n{_coconut_format_1}->{_coconut_format_2}".format(_coconut_format_0=(self.name), _coconut_format_1=(src.meta['shape']), _coconut_format_2=(new_meta['shape'])))  #87:                         logger.info(f"{self.name}:\n{src.meta['shape']}->{new_meta['shape']}")
        except Exception as e:  #88:         except Exception as e:
            from IPython import embed  #89:             from IPython import embed
            from loguru import logger  #90:             from loguru import logger
            logger.error("error while converting to edge!".format())  #91:             logger.error(f"error while converting to edge!")
            raise e  #92:             raise e

_coconut_call_set_names(DataEdge)  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
class Edge(_coconut.collections.namedtuple("Edge", ('a', 'b', 'f', 'cost', 'name'))):  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
    __slots__ = ()  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
    _coconut_is_data = True  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
    __match_args__ = ('a', 'b', 'f', 'cost', 'name')  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
    def __add__(self, other): return _coconut.NotImplemented  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
    def __mul__(self, other): return _coconut.NotImplemented  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
    def __rmul__(self, other): return _coconut.NotImplemented  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
    __ne__ = _coconut.object.__ne__  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
    def __eq__(self, other):  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
    def __hash__(self):  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
    def __new__(_coconut_cls, _coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        _coconut_match_check_3 = False  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        _coconut_match_set_name_a = _coconut_sentinel  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        _coconut_match_set_name_b = _coconut_sentinel  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        _coconut_match_set_name_f = _coconut_sentinel  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        _coconut_match_set_name_cost = _coconut_sentinel  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        _coconut_match_set_name_name = _coconut_sentinel  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        if _coconut_match_first_arg is not _coconut_sentinel:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        if (_coconut.len(_coconut_match_args) <= 5) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "a" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "b" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "f" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "cost" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 4, "name" in _coconut_match_kwargs)) <= 1):  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            _coconut_match_temp_27 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("a")  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            _coconut_match_temp_28 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("b")  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            _coconut_match_temp_29 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("f")  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            _coconut_match_temp_30 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("cost")  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            _coconut_match_temp_31 = _coconut_match_args[4] if _coconut.len(_coconut_match_args) > 4 else _coconut_match_kwargs.pop("name") if "name" in _coconut_match_kwargs else _coconut_sentinel  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            if (_coconut.isinstance(_coconut_match_temp_27, ImageDef)) and (_coconut.isinstance(_coconut_match_temp_28, ImageDef)) and (_coconut.isinstance(_coconut_match_temp_30, int)):  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                _coconut_match_set_name_a = _coconut_match_temp_27  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                _coconut_match_set_name_b = _coconut_match_temp_28  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                _coconut_match_set_name_f = _coconut_match_temp_29  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                _coconut_match_set_name_cost = _coconut_match_temp_30  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                if _coconut_match_temp_31 is _coconut_sentinel:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                    _coconut_match_temp_32 = _coconut.globals().copy()  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                    _coconut_match_temp_32.update(_coconut.locals())  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                    if _coconut_match_set_name_a is not _coconut_sentinel:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                        _coconut_match_temp_32["a"] = _coconut_match_set_name_a  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                    if _coconut_match_set_name_b is not _coconut_sentinel:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                        _coconut_match_temp_32["b"] = _coconut_match_set_name_b  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                    if _coconut_match_set_name_f is not _coconut_sentinel:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                        _coconut_match_temp_32["f"] = _coconut_match_set_name_f  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                    if _coconut_match_set_name_cost is not _coconut_sentinel:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                        _coconut_match_temp_32["cost"] = _coconut_match_set_name_cost  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                    _coconut_exec('_coconut_match_temp_31 = "undefined"', _coconut_match_temp_32)  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                    _coconut_match_temp_31 = _coconut_match_temp_32["_coconut_match_temp_31"]  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                _coconut_match_set_name_name = _coconut_match_temp_31  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                if not _coconut_match_kwargs:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                    _coconut_match_check_3 = True  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
        if _coconut_match_check_3:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            if _coconut_match_set_name_a is not _coconut_sentinel:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                a = _coconut_match_set_name_a  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            if _coconut_match_set_name_b is not _coconut_sentinel:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                b = _coconut_match_set_name_b  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            if _coconut_match_set_name_f is not _coconut_sentinel:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                f = _coconut_match_set_name_f  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            if _coconut_match_set_name_cost is not _coconut_sentinel:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                cost = _coconut_match_set_name_cost  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            if _coconut_match_set_name_name is not _coconut_sentinel:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
                name = _coconut_match_set_name_name  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):

        if not _coconut_match_check_3:  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
            raise _coconut_FunctionMatchError('data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):', _coconut_match_args)  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):

        return _coconut.tuple.__new__(_coconut_cls, (a, b, f, cost, name))  #93: data Edge(a is ImageDef,b is ImageDef,f,cost is int,name="undefined"):
    def __repr__(self):  #94:     def __repr__(self):
        return ("{_coconut_format_0} \t-> {_coconut_format_1}\t-> {_coconut_format_2}".format(_coconut_format_0=(self.a), _coconut_format_1=(self.name), _coconut_format_2=(self.b)))  #95:         return f"{self.a} \t-> {self.name}\t-> {self.b}"

_coconut_call_set_names(Edge)  #96: from typing import List
if _coconut.typing.TYPE_CHECKING:  #96: from typing import List
    from typing import List  #96: from typing import List
else:  #96: from typing import List
    try:  #96: from typing import List
        List = _coconut.typing.List  #96: from typing import List
    except _coconut.AttributeError as _coconut_imp_err:  #96: from typing import List
        raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #96: from typing import List
def to_imagedef(f):  #97: def to_imagedef(f):
    def _inner(imdef: 'ImageDef'):  #98:     def _inner(imdef:ImageDef):
        try:  #99:         try:
#logger.debug(type(imdef))
            if (isinstance)(imdef, ImageDef) and len(imdef) >= 1 and (hasattr)(imdef, "data_type"):  #101:             if imdef `isinstance` ImageDef and len(imdef) >= 1 and imdef `hasattr` "data_type":
#if imdef `isinstance` ImageDef:
                edges = f(imdef.data_type)  #103:                 edges = f(imdef.data_type)
                if edges is not None:  #104:                 if edges is not None:
                    return ([e.to_edge(imdef) for e in edges])  #105:                     return [e.to_edge(imdef) for e in edges]
                else:  #106:                 else:
                    return ([])  #107:                     return []
            else:  #108:             else:
                return ([])  #109:                 return []
        except Exception as e:  #110:         except Exception as e:
            from loguru import logger  #111:             from loguru import logger
            from IPython import embed  #112:             from IPython import embed
            logger.warning("unknown error...imdef:{_coconut_format_0}".format(_coconut_format_0=(imdef)))  #113:             logger.warning(f"unknown error...imdef:{imdef}")
            logger.warning("{_coconut_format_0} has attr causes exception?".format(_coconut_format_0=(imdef)))  #114:             logger.warning(f"{imdef} has attr causes exception?")
            logger.warning("{_coconut_format_0}".format(_coconut_format_0=(hasattr(imdef, 'data_type'))))  #115:             logger.warning(f"{hasattr(imdef,'data_type')}")
            embed()  #116:             embed()
            raise e  #117:             raise e

    return (_inner)  #118:     return _inner

@to_imagedef  #119: @to_imagedef
def to_torch(imdef):  #120: def to_torch(imdef):

    _coconut_case_match_to_1 = imdef  #122:     case imdef:
    _coconut_case_match_check_1 = False  #122:     case imdef:
    _coconut_match_temp_33 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #122:     case imdef:
    _coconut_case_match_check_1 = True  #122:     case imdef:
    if _coconut_case_match_check_1:  #122:     case imdef:
        _coconut_case_match_check_1 = False  #122:     case imdef:
        if not _coconut_case_match_check_1:  #122:     case imdef:
            _coconut_match_set_name_dtype = _coconut_sentinel  #122:     case imdef:
            _coconut_match_set_name_arng = _coconut_sentinel  #122:     case imdef:
            _coconut_match_set_name_ch_repr = _coconut_sentinel  #122:     case imdef:
            _coconut_match_set_name_vr = _coconut_sentinel  #122:     case imdef:
            if (_coconut_match_temp_33) and (_coconut.isinstance(_coconut_case_match_to_1, Numpy)) and (_coconut.len(_coconut_case_match_to_1) >= 4):  #122:     case imdef:
                _coconut_match_set_name_dtype = _coconut_case_match_to_1[0]  #122:     case imdef:
                _coconut_match_set_name_arng = _coconut_case_match_to_1[1]  #122:     case imdef:
                _coconut_match_set_name_ch_repr = _coconut_case_match_to_1[2]  #122:     case imdef:
                _coconut_match_set_name_vr = _coconut_case_match_to_1[3]  #122:     case imdef:
                _coconut_match_temp_34 = _coconut.len(_coconut_case_match_to_1) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_1.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_1, "_coconut_data_defaults", {}) and _coconut_case_match_to_1[i] == _coconut.getattr(_coconut_case_match_to_1, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_1.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_1, "__match_args__") else _coconut.len(_coconut_case_match_to_1) == 4  # type: ignore  #122:     case imdef:
                if _coconut_match_temp_34:  #122:     case imdef:
                    _coconut_case_match_check_1 = True  #122:     case imdef:
            if _coconut_case_match_check_1:  #122:     case imdef:
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #122:     case imdef:
                    dtype = _coconut_match_set_name_dtype  #122:     case imdef:
                if _coconut_match_set_name_arng is not _coconut_sentinel:  #122:     case imdef:
                    arng = _coconut_match_set_name_arng  #122:     case imdef:
                if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #122:     case imdef:
                    ch_repr = _coconut_match_set_name_ch_repr  #122:     case imdef:
                if _coconut_match_set_name_vr is not _coconut_sentinel:  #122:     case imdef:
                    vr = _coconut_match_set_name_vr  #122:     case imdef:

        if not _coconut_case_match_check_1:  #122:     case imdef:
            if (not _coconut_match_temp_33) and (_coconut.isinstance(_coconut_case_match_to_1, Numpy)):  #122:     case imdef:
                _coconut_case_match_check_1 = True  #122:     case imdef:
            if _coconut_case_match_check_1:  #122:     case imdef:
                _coconut_case_match_check_1 = False  #122:     case imdef:
                if not _coconut_case_match_check_1:  #122:     case imdef:
                    if _coconut.type(_coconut_case_match_to_1) in _coconut_self_match_types:  #122:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #122:     case imdef:
                        _coconut_case_match_check_1 = True  #122:     case imdef:

                if not _coconut_case_match_check_1:  #122:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #122:     case imdef:
                    _coconut_match_set_name_arng = _coconut_sentinel  #122:     case imdef:
                    _coconut_match_set_name_ch_repr = _coconut_sentinel  #122:     case imdef:
                    _coconut_match_set_name_vr = _coconut_sentinel  #122:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_1) in _coconut_self_match_types:  #122:     case imdef:
                        _coconut_match_temp_35 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #122:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_35, _coconut.tuple):  #122:     case imdef:
                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #122:     case imdef:
                        if _coconut.len(_coconut_match_temp_35) < 4:  #122:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_35),))  #122:     case imdef:
                        _coconut_match_temp_36 = _coconut.getattr(_coconut_case_match_to_1, _coconut_match_temp_35[0], _coconut_sentinel)  #122:     case imdef:
                        _coconut_match_temp_37 = _coconut.getattr(_coconut_case_match_to_1, _coconut_match_temp_35[1], _coconut_sentinel)  #122:     case imdef:
                        _coconut_match_temp_38 = _coconut.getattr(_coconut_case_match_to_1, _coconut_match_temp_35[2], _coconut_sentinel)  #122:     case imdef:
                        _coconut_match_temp_39 = _coconut.getattr(_coconut_case_match_to_1, _coconut_match_temp_35[3], _coconut_sentinel)  #122:     case imdef:
                        if (_coconut_match_temp_36 is not _coconut_sentinel) and (_coconut_match_temp_37 is not _coconut_sentinel) and (_coconut_match_temp_38 is not _coconut_sentinel) and (_coconut_match_temp_39 is not _coconut_sentinel):  #122:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_match_temp_36  #122:     case imdef:
                            _coconut_match_set_name_arng = _coconut_match_temp_37  #122:     case imdef:
                            _coconut_match_set_name_ch_repr = _coconut_match_temp_38  #122:     case imdef:
                            _coconut_match_set_name_vr = _coconut_match_temp_39  #122:     case imdef:
                            _coconut_case_match_check_1 = True  #122:     case imdef:
                    if _coconut_case_match_check_1:  #122:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #122:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #122:     case imdef:
                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #122:     case imdef:
                            arng = _coconut_match_set_name_arng  #122:     case imdef:
                        if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #122:     case imdef:
                            ch_repr = _coconut_match_set_name_ch_repr  #122:     case imdef:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #122:     case imdef:
                            vr = _coconut_match_set_name_vr  #122:     case imdef:




    if _coconut_case_match_check_1:  #122:     case imdef:
        return ([DataEdge(imdef, Torch(dtype, arng, ch_repr, vr), torch.from_numpy, 2, name="to_torch"),])  #124:             return [DataEdge(imdef,Torch(dtype,arng,ch_repr,vr),torch.from_numpy,2,name="to_torch")]
    return ([])  #125:     return []


# there are kinds of rules
# 1. doesnt care about shape, and no shape change
# 2. doesnt care shape, but shape changes
# 3. depends on input shape but shape doesn't change
# 4. depends on input and output shape changes
# well ,just give function a shape and return nop for shape?
# what if some other metadata is added?
# where should I store shape?
# If I change the signature, I have modify them all... for match syntax
# I just


# doesn't change shape, so no touch
@to_imagedef  # doesn't change shape, so no touch  #140: @to_imagedef # doesn't change shape, so no touch
def to_PILImages(imdef: 'ImageDef') -> '_coconut.typing.Sequence[Edge]':  #141: def to_PILImages(imdef:ImageDef)->Edge[]:
    _coconut_case_match_to_2 = imdef  #142:     case imdef:
    _coconut_case_match_check_2 = False  #142:     case imdef:
    _coconut_match_temp_40 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #142:     case imdef:
    _coconut_case_match_check_2 = True  #142:     case imdef:
    if _coconut_case_match_check_2:  #142:     case imdef:
        _coconut_case_match_check_2 = False  #142:     case imdef:
        if not _coconut_case_match_check_2:  #142:     case imdef:
            if (_coconut_match_temp_40) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)) and (_coconut.len(_coconut_case_match_to_2) >= 4) and (_coconut_case_match_to_2[2] == "LAB"):  #142:     case imdef:
                _coconut_match_temp_41 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 4  # type: ignore  #142:     case imdef:
                if _coconut_match_temp_41:  #142:     case imdef:
                    _coconut_case_match_check_2 = True  #142:     case imdef:

        if not _coconut_case_match_check_2:  #142:     case imdef:
            if (not _coconut_match_temp_40) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)):  #142:     case imdef:
                _coconut_case_match_check_2 = True  #142:     case imdef:
            if _coconut_case_match_check_2:  #142:     case imdef:
                _coconut_case_match_check_2 = False  #142:     case imdef:
                if not _coconut_case_match_check_2:  #142:     case imdef:
                    if _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #142:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #142:     case imdef:
                        _coconut_case_match_check_2 = True  #142:     case imdef:

                if not _coconut_case_match_check_2:  #142:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #142:     case imdef:
                        _coconut_match_temp_42 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #142:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_42, _coconut.tuple):  #142:     case imdef:
                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #142:     case imdef:
                        if _coconut.len(_coconut_match_temp_42) < 4:  #142:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_42),))  #142:     case imdef:
                        _coconut_match_temp_43 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_42[0], _coconut_sentinel)  #142:     case imdef:
                        _coconut_match_temp_44 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_42[1], _coconut_sentinel)  #142:     case imdef:
                        _coconut_match_temp_45 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_42[2], _coconut_sentinel)  #142:     case imdef:
                        _coconut_match_temp_46 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_42[3], _coconut_sentinel)  #142:     case imdef:
                        if (_coconut_match_temp_43 is not _coconut_sentinel) and (_coconut_match_temp_44 is not _coconut_sentinel) and (_coconut_match_temp_45 is not _coconut_sentinel) and (_coconut_match_temp_45 == "LAB") and (_coconut_match_temp_46 is not _coconut_sentinel):  #142:     case imdef:
                            _coconut_case_match_check_2 = True  #142:     case imdef:




    if _coconut_case_match_check_2:  #142:     case imdef:
        return ([])  # you cannot convert LAB data to PILImage  #144:             return []# you cannot convert LAB data to PILImage
    if not _coconut_case_match_check_2:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
        _coconut_match_temp_47 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
        _coconut_case_match_check_2 = True  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
        if _coconut_case_match_check_2:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
            _coconut_case_match_check_2 = False  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
            if not _coconut_case_match_check_2:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                _coconut_match_set_name_c_repr = _coconut_sentinel  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                if (_coconut_match_temp_47) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)) and (_coconut.len(_coconut_case_match_to_2) >= 4) and (_coconut_case_match_to_2[0] == "uint8") and (_coconut_case_match_to_2[1] == "BHWC") and (_coconut_case_match_to_2[3] == VR_0_255):  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                    _coconut_match_set_name_c_repr = _coconut_case_match_to_2[2]  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                    _coconut_match_temp_48 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 4  # type: ignore  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                    if _coconut_match_temp_48:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                        _coconut_case_match_check_2 = True  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                if _coconut_case_match_check_2:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                    if _coconut_match_set_name_c_repr is not _coconut_sentinel:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                        c_repr = _coconut_match_set_name_c_repr  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:

            if not _coconut_case_match_check_2:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                if (not _coconut_match_temp_47) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)):  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                    _coconut_case_match_check_2 = True  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                if _coconut_case_match_check_2:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                    _coconut_case_match_check_2 = False  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                    if not _coconut_case_match_check_2:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                        if _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                            _coconut_case_match_check_2 = True  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:

                    if not _coconut_case_match_check_2:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                        _coconut_match_set_name_c_repr = _coconut_sentinel  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                        if not _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                            _coconut_match_temp_49 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                            if not _coconut.isinstance(_coconut_match_temp_49, _coconut.tuple):  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                            if _coconut.len(_coconut_match_temp_49) < 4:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_49),))  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                            _coconut_match_temp_50 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_49[0], _coconut_sentinel)  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                            _coconut_match_temp_51 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_49[1], _coconut_sentinel)  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                            _coconut_match_temp_52 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_49[2], _coconut_sentinel)  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                            _coconut_match_temp_53 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_49[3], _coconut_sentinel)  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                            if (_coconut_match_temp_50 is not _coconut_sentinel) and (_coconut_match_temp_50 == "uint8") and (_coconut_match_temp_51 is not _coconut_sentinel) and (_coconut_match_temp_51 == "BHWC") and (_coconut_match_temp_52 is not _coconut_sentinel) and (_coconut_match_temp_53 is not _coconut_sentinel) and (_coconut_match_temp_53 == VR_0_255):  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                                _coconut_match_set_name_c_repr = _coconut_match_temp_52  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                                _coconut_case_match_check_2 = True  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                        if _coconut_case_match_check_2:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                            if _coconut_match_set_name_c_repr is not _coconut_sentinel:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
                                c_repr = _coconut_match_set_name_c_repr  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:




        if _coconut_case_match_check_2 and not (c_repr in KNOWN_COLOR_FMTS):  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
            _coconut_case_match_check_2 = False  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
        if _coconut_case_match_check_2:  #145:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if c_repr in KNOWN_COLOR_FMTS:
            return ([DataEdge(imdef, PILImages(c_repr, c_repr), lambda ary: [(Image.fromarray)(img, mode=c_repr) for img in ary], 2, name="numpy batch {_coconut_format_0} to Images with mode {_coconut_format_1}".format(_coconut_format_0=(c_repr), _coconut_format_1=(c_repr))),])  #146:             return [DataEdge(imdef,PILImages(c_repr,c_repr),ary -> [(Image.fromarray)(img,mode=c_repr) for img in ary],2,name=f"numpy batch {c_repr} to Images with mode {c_repr}")]
    if not _coconut_case_match_check_2:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
        _coconut_match_temp_54 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
        _coconut_case_match_check_2 = True  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
        if _coconut_case_match_check_2:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
            _coconut_case_match_check_2 = False  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
            if not _coconut_case_match_check_2:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                _coconut_match_set_name_c_repr = _coconut_sentinel  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                if (_coconut_match_temp_54) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)) and (_coconut.len(_coconut_case_match_to_2) >= 4) and (_coconut_case_match_to_2[0] == "uint8") and (_coconut_case_match_to_2[1] == "BHWC") and (_coconut_case_match_to_2[3] == VR_0_255):  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                    _coconut_match_set_name_c_repr = _coconut_case_match_to_2[2]  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                    _coconut_match_temp_55 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 4  # type: ignore  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                    if _coconut_match_temp_55:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                        _coconut_case_match_check_2 = True  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                if _coconut_case_match_check_2:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                    if _coconut_match_set_name_c_repr is not _coconut_sentinel:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                        c_repr = _coconut_match_set_name_c_repr  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):

            if not _coconut_case_match_check_2:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                if (not _coconut_match_temp_54) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)):  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                    _coconut_case_match_check_2 = True  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                if _coconut_case_match_check_2:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                    _coconut_case_match_check_2 = False  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                    if not _coconut_case_match_check_2:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                        if _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                            _coconut_case_match_check_2 = True  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):

                    if not _coconut_case_match_check_2:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                        _coconut_match_set_name_c_repr = _coconut_sentinel  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                        if not _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                            _coconut_match_temp_56 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                            if not _coconut.isinstance(_coconut_match_temp_56, _coconut.tuple):  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                            if _coconut.len(_coconut_match_temp_56) < 4:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_56),))  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                            _coconut_match_temp_57 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_56[0], _coconut_sentinel)  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                            _coconut_match_temp_58 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_56[1], _coconut_sentinel)  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                            _coconut_match_temp_59 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_56[2], _coconut_sentinel)  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                            _coconut_match_temp_60 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_56[3], _coconut_sentinel)  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                            if (_coconut_match_temp_57 is not _coconut_sentinel) and (_coconut_match_temp_57 == "uint8") and (_coconut_match_temp_58 is not _coconut_sentinel) and (_coconut_match_temp_58 == "BHWC") and (_coconut_match_temp_59 is not _coconut_sentinel) and (_coconut_match_temp_60 is not _coconut_sentinel) and (_coconut_match_temp_60 == VR_0_255):  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                                _coconut_match_set_name_c_repr = _coconut_match_temp_59  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                                _coconut_case_match_check_2 = True  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                        if _coconut_case_match_check_2:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                            if _coconut_match_set_name_c_repr is not _coconut_sentinel:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
                                c_repr = _coconut_match_set_name_c_repr  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):




        if _coconut_case_match_check_2 and not (len(ch_splitter(c_repr)) in (3, 4)):  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
            _coconut_case_match_check_2 = False  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
        if _coconut_case_match_check_2:  #147:         match Numpy("uint8","BHWC", c_repr, ==VR_0_255) if len(ch_splitter(c_repr)) in (3,4):
            return ([DataEdge(imdef, PILImages(c_repr, c_repr), lambda ary: [(Image.fromarray)(img) for img in ary], 2, name="numpy batch {_coconut_format_0} to Images".format(_coconut_format_0=(c_repr))),])  #148:             return [DataEdge(imdef,PILImages(c_repr,c_repr),ary -> [(Image.fromarray)(img) for img in ary],2,name=f"numpy batch {c_repr} to Images")]
    if not _coconut_case_match_check_2:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
        _coconut_match_temp_61 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
        _coconut_case_match_check_2 = True  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
        if _coconut_case_match_check_2:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
            _coconut_case_match_check_2 = False  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
            if not _coconut_case_match_check_2:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                _coconut_match_set_name_c_repr = _coconut_sentinel  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                if (_coconut_match_temp_61) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)) and (_coconut.len(_coconut_case_match_to_2) >= 4) and (_coconut_case_match_to_2[0] == "uint8") and (_coconut_case_match_to_2[1] == "BHW") and (_coconut_case_match_to_2[3] == VR_0_255):  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                    _coconut_match_set_name_c_repr = _coconut_case_match_to_2[2]  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                    _coconut_match_temp_62 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 4  # type: ignore  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                    if _coconut_match_temp_62:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                        _coconut_case_match_check_2 = True  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                if _coconut_case_match_check_2:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                    if _coconut_match_set_name_c_repr is not _coconut_sentinel:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                        c_repr = _coconut_match_set_name_c_repr  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):

            if not _coconut_case_match_check_2:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                if (not _coconut_match_temp_61) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)):  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                    _coconut_case_match_check_2 = True  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                if _coconut_case_match_check_2:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                    _coconut_case_match_check_2 = False  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                    if not _coconut_case_match_check_2:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                        if _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                            _coconut_case_match_check_2 = True  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):

                    if not _coconut_case_match_check_2:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                        _coconut_match_set_name_c_repr = _coconut_sentinel  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                        if not _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                            _coconut_match_temp_63 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                            if not _coconut.isinstance(_coconut_match_temp_63, _coconut.tuple):  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                            if _coconut.len(_coconut_match_temp_63) < 4:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_63),))  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                            _coconut_match_temp_64 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_63[0], _coconut_sentinel)  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                            _coconut_match_temp_65 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_63[1], _coconut_sentinel)  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                            _coconut_match_temp_66 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_63[2], _coconut_sentinel)  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                            _coconut_match_temp_67 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_63[3], _coconut_sentinel)  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                            if (_coconut_match_temp_64 is not _coconut_sentinel) and (_coconut_match_temp_64 == "uint8") and (_coconut_match_temp_65 is not _coconut_sentinel) and (_coconut_match_temp_65 == "BHW") and (_coconut_match_temp_66 is not _coconut_sentinel) and (_coconut_match_temp_67 is not _coconut_sentinel) and (_coconut_match_temp_67 == VR_0_255):  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                                _coconut_match_set_name_c_repr = _coconut_match_temp_66  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                                _coconut_case_match_check_2 = True  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                        if _coconut_case_match_check_2:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                            if _coconut_match_set_name_c_repr is not _coconut_sentinel:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
                                c_repr = _coconut_match_set_name_c_repr  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):




        if _coconut_case_match_check_2:  #149:         match Numpy("uint8","BHW",c_repr,==VR_0_255):
            return ([DataEdge(imdef, PILImages("L", c_repr), lambda ary: [(_coconut_base_compose(Image.fromarray, (_coconut.operator.methodcaller("convert", "L"), 0, False)))(img) for img in ary], 2, name="numpy batch to images"),])  #150:             return [DataEdge(imdef,PILImages("L",c_repr),ary -> [(Image.fromarray ..> .convert("L"))(img) for img in ary],2,name="numpy batch to images")]
    if not _coconut_case_match_check_2:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
        _coconut_match_temp_68 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
        _coconut_case_match_check_2 = True  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
        if _coconut_case_match_check_2:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
            _coconut_case_match_check_2 = False  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
            if not _coconut_case_match_check_2:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                _coconut_match_set_name_c_repr = _coconut_sentinel  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                if (_coconut_match_temp_68) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)) and (_coconut.len(_coconut_case_match_to_2) >= 4) and (_coconut_case_match_to_2[0] == "uint8") and (_coconut_case_match_to_2[1] == "HW") and (_coconut_case_match_to_2[3] == VR_0_255):  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                    _coconut_match_set_name_c_repr = _coconut_case_match_to_2[2]  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                    _coconut_match_temp_69 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 4  # type: ignore  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                    if _coconut_match_temp_69:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                        _coconut_case_match_check_2 = True  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                if _coconut_case_match_check_2:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                    if _coconut_match_set_name_c_repr is not _coconut_sentinel:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                        c_repr = _coconut_match_set_name_c_repr  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):

            if not _coconut_case_match_check_2:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                if (not _coconut_match_temp_68) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)):  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                    _coconut_case_match_check_2 = True  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                if _coconut_case_match_check_2:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                    _coconut_case_match_check_2 = False  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                    if not _coconut_case_match_check_2:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                        if _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                            _coconut_case_match_check_2 = True  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):

                    if not _coconut_case_match_check_2:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                        _coconut_match_set_name_c_repr = _coconut_sentinel  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                        if not _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                            _coconut_match_temp_70 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                            if not _coconut.isinstance(_coconut_match_temp_70, _coconut.tuple):  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                            if _coconut.len(_coconut_match_temp_70) < 4:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_70),))  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                            _coconut_match_temp_71 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_70[0], _coconut_sentinel)  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                            _coconut_match_temp_72 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_70[1], _coconut_sentinel)  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                            _coconut_match_temp_73 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_70[2], _coconut_sentinel)  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                            _coconut_match_temp_74 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_70[3], _coconut_sentinel)  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                            if (_coconut_match_temp_71 is not _coconut_sentinel) and (_coconut_match_temp_71 == "uint8") and (_coconut_match_temp_72 is not _coconut_sentinel) and (_coconut_match_temp_72 == "HW") and (_coconut_match_temp_73 is not _coconut_sentinel) and (_coconut_match_temp_74 is not _coconut_sentinel) and (_coconut_match_temp_74 == VR_0_255):  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                                _coconut_match_set_name_c_repr = _coconut_match_temp_73  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                                _coconut_case_match_check_2 = True  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                        if _coconut_case_match_check_2:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                            if _coconut_match_set_name_c_repr is not _coconut_sentinel:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
                                c_repr = _coconut_match_set_name_c_repr  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):




        if _coconut_case_match_check_2:  #151:         match Numpy("uint8","HW",c_repr,==VR_0_255):
            return ([DataEdge(imdef, PILImage("L", c_repr), _coconut_base_compose(Image.fromarray, (_coconut.operator.methodcaller("convert", "L"), 0, False)), 2, name="numpy HW to PIL Image"),])  #152:             return [DataEdge(imdef,PILImage("L",c_repr), Image.fromarray ..> .convert("L"),2,name="numpy HW to PIL Image")]
    return ([])  #153:     return []

@to_imagedef  #154: @to_imagedef
def to_numpy(imdef: 'ImageDef') -> 'List[DataEdge]':  #155: def to_numpy(imdef:ImageDef)->List[DataEdge]:
    _coconut_case_match_to_3 = imdef  #156:     case imdef:
    _coconut_case_match_check_3 = False  #156:     case imdef:
    _coconut_match_temp_75 = _coconut.getattr(Torch, "_coconut_is_data", False) or _coconut.isinstance(Torch, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Torch)  # type: ignore  #156:     case imdef:
    _coconut_case_match_check_3 = True  #156:     case imdef:
    if _coconut_case_match_check_3:  #156:     case imdef:
        _coconut_case_match_check_3 = False  #156:     case imdef:
        if not _coconut_case_match_check_3:  #156:     case imdef:
            _coconut_match_set_name_dtype = _coconut_sentinel  #156:     case imdef:
            _coconut_match_set_name_arng = _coconut_sentinel  #156:     case imdef:
            _coconut_match_set_name_ch_repr = _coconut_sentinel  #156:     case imdef:
            _coconut_match_set_name_vr = _coconut_sentinel  #156:     case imdef:
            if (_coconut_match_temp_75) and (_coconut.isinstance(_coconut_case_match_to_3, Torch)) and (_coconut.len(_coconut_case_match_to_3) >= 4):  #156:     case imdef:
                _coconut_match_set_name_dtype = _coconut_case_match_to_3[0]  #156:     case imdef:
                _coconut_match_set_name_arng = _coconut_case_match_to_3[1]  #156:     case imdef:
                _coconut_match_set_name_ch_repr = _coconut_case_match_to_3[2]  #156:     case imdef:
                _coconut_match_set_name_vr = _coconut_case_match_to_3[3]  #156:     case imdef:
                _coconut_match_temp_76 = _coconut.len(_coconut_case_match_to_3) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_3.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {}) and _coconut_case_match_to_3[i] == _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_3.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_3, "__match_args__") else _coconut.len(_coconut_case_match_to_3) == 4  # type: ignore  #156:     case imdef:
                if _coconut_match_temp_76:  #156:     case imdef:
                    _coconut_case_match_check_3 = True  #156:     case imdef:
            if _coconut_case_match_check_3:  #156:     case imdef:
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #156:     case imdef:
                    dtype = _coconut_match_set_name_dtype  #156:     case imdef:
                if _coconut_match_set_name_arng is not _coconut_sentinel:  #156:     case imdef:
                    arng = _coconut_match_set_name_arng  #156:     case imdef:
                if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #156:     case imdef:
                    ch_repr = _coconut_match_set_name_ch_repr  #156:     case imdef:
                if _coconut_match_set_name_vr is not _coconut_sentinel:  #156:     case imdef:
                    vr = _coconut_match_set_name_vr  #156:     case imdef:

        if not _coconut_case_match_check_3:  #156:     case imdef:
            if (not _coconut_match_temp_75) and (_coconut.isinstance(_coconut_case_match_to_3, Torch)):  #156:     case imdef:
                _coconut_case_match_check_3 = True  #156:     case imdef:
            if _coconut_case_match_check_3:  #156:     case imdef:
                _coconut_case_match_check_3 = False  #156:     case imdef:
                if not _coconut_case_match_check_3:  #156:     case imdef:
                    if _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #156:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports 1)")  #156:     case imdef:
                        _coconut_case_match_check_3 = True  #156:     case imdef:

                if not _coconut_case_match_check_3:  #156:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #156:     case imdef:
                    _coconut_match_set_name_arng = _coconut_sentinel  #156:     case imdef:
                    _coconut_match_set_name_ch_repr = _coconut_sentinel  #156:     case imdef:
                    _coconut_match_set_name_vr = _coconut_sentinel  #156:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #156:     case imdef:
                        _coconut_match_temp_77 = _coconut.getattr(Torch, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #156:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_77, _coconut.tuple):  #156:     case imdef:
                            raise _coconut.TypeError("Torch.__match_args__ must be a tuple")  #156:     case imdef:
                        if _coconut.len(_coconut_match_temp_77) < 4:  #156:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports %s)" % (_coconut.len(_coconut_match_temp_77),))  #156:     case imdef:
                        _coconut_match_temp_78 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_77[0], _coconut_sentinel)  #156:     case imdef:
                        _coconut_match_temp_79 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_77[1], _coconut_sentinel)  #156:     case imdef:
                        _coconut_match_temp_80 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_77[2], _coconut_sentinel)  #156:     case imdef:
                        _coconut_match_temp_81 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_77[3], _coconut_sentinel)  #156:     case imdef:
                        if (_coconut_match_temp_78 is not _coconut_sentinel) and (_coconut_match_temp_79 is not _coconut_sentinel) and (_coconut_match_temp_80 is not _coconut_sentinel) and (_coconut_match_temp_81 is not _coconut_sentinel):  #156:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_match_temp_78  #156:     case imdef:
                            _coconut_match_set_name_arng = _coconut_match_temp_79  #156:     case imdef:
                            _coconut_match_set_name_ch_repr = _coconut_match_temp_80  #156:     case imdef:
                            _coconut_match_set_name_vr = _coconut_match_temp_81  #156:     case imdef:
                            _coconut_case_match_check_3 = True  #156:     case imdef:
                    if _coconut_case_match_check_3:  #156:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #156:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #156:     case imdef:
                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #156:     case imdef:
                            arng = _coconut_match_set_name_arng  #156:     case imdef:
                        if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #156:     case imdef:
                            ch_repr = _coconut_match_set_name_ch_repr  #156:     case imdef:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #156:     case imdef:
                            vr = _coconut_match_set_name_vr  #156:     case imdef:




    if _coconut_case_match_check_3:  #156:     case imdef:
        return ([DataEdge(imdef, Numpy(dtype, arng, ch_repr, vr), (_coconut_base_compose(_coconut.operator.methodcaller("detach"), (_coconut.operator.methodcaller("cpu"), 0, False), (_coconut.operator.methodcaller("numpy"), 0, False))), 1, name="torch_to_numpy"),])  #158:             return [DataEdge(imdef,
    if not _coconut_case_match_check_3:  #163:         match PILImage("RGB",ch_repr):
        _coconut_match_temp_82 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #163:         match PILImage("RGB",ch_repr):
        _coconut_case_match_check_3 = True  #163:         match PILImage("RGB",ch_repr):
        if _coconut_case_match_check_3:  #163:         match PILImage("RGB",ch_repr):
            _coconut_case_match_check_3 = False  #163:         match PILImage("RGB",ch_repr):
            if not _coconut_case_match_check_3:  #163:         match PILImage("RGB",ch_repr):
                _coconut_match_set_name_ch_repr = _coconut_sentinel  #163:         match PILImage("RGB",ch_repr):
                if (_coconut_match_temp_82) and (_coconut.isinstance(_coconut_case_match_to_3, PILImage)) and (_coconut.len(_coconut_case_match_to_3) >= 2) and (_coconut_case_match_to_3[0] == "RGB"):  #163:         match PILImage("RGB",ch_repr):
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_3[1]  #163:         match PILImage("RGB",ch_repr):
                    _coconut_match_temp_83 = _coconut.len(_coconut_case_match_to_3) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_3.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {}) and _coconut_case_match_to_3[i] == _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_3.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_3, "__match_args__") else _coconut.len(_coconut_case_match_to_3) == 2  # type: ignore  #163:         match PILImage("RGB",ch_repr):
                    if _coconut_match_temp_83:  #163:         match PILImage("RGB",ch_repr):
                        _coconut_case_match_check_3 = True  #163:         match PILImage("RGB",ch_repr):
                if _coconut_case_match_check_3:  #163:         match PILImage("RGB",ch_repr):
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #163:         match PILImage("RGB",ch_repr):
                        ch_repr = _coconut_match_set_name_ch_repr  #163:         match PILImage("RGB",ch_repr):

            if not _coconut_case_match_check_3:  #163:         match PILImage("RGB",ch_repr):
                if (not _coconut_match_temp_82) and (_coconut.isinstance(_coconut_case_match_to_3, PILImage)):  #163:         match PILImage("RGB",ch_repr):
                    _coconut_case_match_check_3 = True  #163:         match PILImage("RGB",ch_repr):
                if _coconut_case_match_check_3:  #163:         match PILImage("RGB",ch_repr):
                    _coconut_case_match_check_3 = False  #163:         match PILImage("RGB",ch_repr):
                    if not _coconut_case_match_check_3:  #163:         match PILImage("RGB",ch_repr):
                        if _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #163:         match PILImage("RGB",ch_repr):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #163:         match PILImage("RGB",ch_repr):
                            _coconut_case_match_check_3 = True  #163:         match PILImage("RGB",ch_repr):

                    if not _coconut_case_match_check_3:  #163:         match PILImage("RGB",ch_repr):
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  #163:         match PILImage("RGB",ch_repr):
                        if not _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #163:         match PILImage("RGB",ch_repr):
                            _coconut_match_temp_84 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #163:         match PILImage("RGB",ch_repr):
                            if not _coconut.isinstance(_coconut_match_temp_84, _coconut.tuple):  #163:         match PILImage("RGB",ch_repr):
                                raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #163:         match PILImage("RGB",ch_repr):
                            if _coconut.len(_coconut_match_temp_84) < 2:  #163:         match PILImage("RGB",ch_repr):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_84),))  #163:         match PILImage("RGB",ch_repr):
                            _coconut_match_temp_85 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_84[0], _coconut_sentinel)  #163:         match PILImage("RGB",ch_repr):
                            _coconut_match_temp_86 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_84[1], _coconut_sentinel)  #163:         match PILImage("RGB",ch_repr):
                            if (_coconut_match_temp_85 is not _coconut_sentinel) and (_coconut_match_temp_85 == "RGB") and (_coconut_match_temp_86 is not _coconut_sentinel):  #163:         match PILImage("RGB",ch_repr):
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_86  #163:         match PILImage("RGB",ch_repr):
                                _coconut_case_match_check_3 = True  #163:         match PILImage("RGB",ch_repr):
                        if _coconut_case_match_check_3:  #163:         match PILImage("RGB",ch_repr):
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #163:         match PILImage("RGB",ch_repr):
                                ch_repr = _coconut_match_set_name_ch_repr  #163:         match PILImage("RGB",ch_repr):




        if _coconut_case_match_check_3:  #163:         match PILImage("RGB",ch_repr):
            return ([DataEdge(imdef, Numpy("uint8", "HWC", ch_repr, VR_0_255), np.array, 1, name="image_to_numpy"),])  #164:                     return [DataEdge(imdef,
    if not _coconut_case_match_check_3:  #169:         match PILImage("L",ch_repr):
        _coconut_match_temp_87 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #169:         match PILImage("L",ch_repr):
        _coconut_case_match_check_3 = True  #169:         match PILImage("L",ch_repr):
        if _coconut_case_match_check_3:  #169:         match PILImage("L",ch_repr):
            _coconut_case_match_check_3 = False  #169:         match PILImage("L",ch_repr):
            if not _coconut_case_match_check_3:  #169:         match PILImage("L",ch_repr):
                _coconut_match_set_name_ch_repr = _coconut_sentinel  #169:         match PILImage("L",ch_repr):
                if (_coconut_match_temp_87) and (_coconut.isinstance(_coconut_case_match_to_3, PILImage)) and (_coconut.len(_coconut_case_match_to_3) >= 2) and (_coconut_case_match_to_3[0] == "L"):  #169:         match PILImage("L",ch_repr):
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_3[1]  #169:         match PILImage("L",ch_repr):
                    _coconut_match_temp_88 = _coconut.len(_coconut_case_match_to_3) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_3.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {}) and _coconut_case_match_to_3[i] == _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_3.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_3, "__match_args__") else _coconut.len(_coconut_case_match_to_3) == 2  # type: ignore  #169:         match PILImage("L",ch_repr):
                    if _coconut_match_temp_88:  #169:         match PILImage("L",ch_repr):
                        _coconut_case_match_check_3 = True  #169:         match PILImage("L",ch_repr):
                if _coconut_case_match_check_3:  #169:         match PILImage("L",ch_repr):
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #169:         match PILImage("L",ch_repr):
                        ch_repr = _coconut_match_set_name_ch_repr  #169:         match PILImage("L",ch_repr):

            if not _coconut_case_match_check_3:  #169:         match PILImage("L",ch_repr):
                if (not _coconut_match_temp_87) and (_coconut.isinstance(_coconut_case_match_to_3, PILImage)):  #169:         match PILImage("L",ch_repr):
                    _coconut_case_match_check_3 = True  #169:         match PILImage("L",ch_repr):
                if _coconut_case_match_check_3:  #169:         match PILImage("L",ch_repr):
                    _coconut_case_match_check_3 = False  #169:         match PILImage("L",ch_repr):
                    if not _coconut_case_match_check_3:  #169:         match PILImage("L",ch_repr):
                        if _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #169:         match PILImage("L",ch_repr):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #169:         match PILImage("L",ch_repr):
                            _coconut_case_match_check_3 = True  #169:         match PILImage("L",ch_repr):

                    if not _coconut_case_match_check_3:  #169:         match PILImage("L",ch_repr):
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  #169:         match PILImage("L",ch_repr):
                        if not _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #169:         match PILImage("L",ch_repr):
                            _coconut_match_temp_89 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #169:         match PILImage("L",ch_repr):
                            if not _coconut.isinstance(_coconut_match_temp_89, _coconut.tuple):  #169:         match PILImage("L",ch_repr):
                                raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #169:         match PILImage("L",ch_repr):
                            if _coconut.len(_coconut_match_temp_89) < 2:  #169:         match PILImage("L",ch_repr):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_89),))  #169:         match PILImage("L",ch_repr):
                            _coconut_match_temp_90 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_89[0], _coconut_sentinel)  #169:         match PILImage("L",ch_repr):
                            _coconut_match_temp_91 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_89[1], _coconut_sentinel)  #169:         match PILImage("L",ch_repr):
                            if (_coconut_match_temp_90 is not _coconut_sentinel) and (_coconut_match_temp_90 == "L") and (_coconut_match_temp_91 is not _coconut_sentinel):  #169:         match PILImage("L",ch_repr):
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_91  #169:         match PILImage("L",ch_repr):
                                _coconut_case_match_check_3 = True  #169:         match PILImage("L",ch_repr):
                        if _coconut_case_match_check_3:  #169:         match PILImage("L",ch_repr):
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #169:         match PILImage("L",ch_repr):
                                ch_repr = _coconut_match_set_name_ch_repr  #169:         match PILImage("L",ch_repr):




        if _coconut_case_match_check_3:  #169:         match PILImage("L",ch_repr):
            return ([DataEdge(imdef, Numpy("uint8", "HW", ch_repr, VR_0_255), np.array, 1, name="image_to_numpy"),])  #170:                     return [DataEdge(imdef,
    if not _coconut_case_match_check_3:  #175:         match PILImage("YCbCr",ch_repr):
        _coconut_match_temp_92 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #175:         match PILImage("YCbCr",ch_repr):
        _coconut_case_match_check_3 = True  #175:         match PILImage("YCbCr",ch_repr):
        if _coconut_case_match_check_3:  #175:         match PILImage("YCbCr",ch_repr):
            _coconut_case_match_check_3 = False  #175:         match PILImage("YCbCr",ch_repr):
            if not _coconut_case_match_check_3:  #175:         match PILImage("YCbCr",ch_repr):
                _coconut_match_set_name_ch_repr = _coconut_sentinel  #175:         match PILImage("YCbCr",ch_repr):
                if (_coconut_match_temp_92) and (_coconut.isinstance(_coconut_case_match_to_3, PILImage)) and (_coconut.len(_coconut_case_match_to_3) >= 2) and (_coconut_case_match_to_3[0] == "YCbCr"):  #175:         match PILImage("YCbCr",ch_repr):
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_3[1]  #175:         match PILImage("YCbCr",ch_repr):
                    _coconut_match_temp_93 = _coconut.len(_coconut_case_match_to_3) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_3.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {}) and _coconut_case_match_to_3[i] == _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_3.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_3, "__match_args__") else _coconut.len(_coconut_case_match_to_3) == 2  # type: ignore  #175:         match PILImage("YCbCr",ch_repr):
                    if _coconut_match_temp_93:  #175:         match PILImage("YCbCr",ch_repr):
                        _coconut_case_match_check_3 = True  #175:         match PILImage("YCbCr",ch_repr):
                if _coconut_case_match_check_3:  #175:         match PILImage("YCbCr",ch_repr):
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #175:         match PILImage("YCbCr",ch_repr):
                        ch_repr = _coconut_match_set_name_ch_repr  #175:         match PILImage("YCbCr",ch_repr):

            if not _coconut_case_match_check_3:  #175:         match PILImage("YCbCr",ch_repr):
                if (not _coconut_match_temp_92) and (_coconut.isinstance(_coconut_case_match_to_3, PILImage)):  #175:         match PILImage("YCbCr",ch_repr):
                    _coconut_case_match_check_3 = True  #175:         match PILImage("YCbCr",ch_repr):
                if _coconut_case_match_check_3:  #175:         match PILImage("YCbCr",ch_repr):
                    _coconut_case_match_check_3 = False  #175:         match PILImage("YCbCr",ch_repr):
                    if not _coconut_case_match_check_3:  #175:         match PILImage("YCbCr",ch_repr):
                        if _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #175:         match PILImage("YCbCr",ch_repr):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #175:         match PILImage("YCbCr",ch_repr):
                            _coconut_case_match_check_3 = True  #175:         match PILImage("YCbCr",ch_repr):

                    if not _coconut_case_match_check_3:  #175:         match PILImage("YCbCr",ch_repr):
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  #175:         match PILImage("YCbCr",ch_repr):
                        if not _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #175:         match PILImage("YCbCr",ch_repr):
                            _coconut_match_temp_94 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #175:         match PILImage("YCbCr",ch_repr):
                            if not _coconut.isinstance(_coconut_match_temp_94, _coconut.tuple):  #175:         match PILImage("YCbCr",ch_repr):
                                raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #175:         match PILImage("YCbCr",ch_repr):
                            if _coconut.len(_coconut_match_temp_94) < 2:  #175:         match PILImage("YCbCr",ch_repr):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_94),))  #175:         match PILImage("YCbCr",ch_repr):
                            _coconut_match_temp_95 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_94[0], _coconut_sentinel)  #175:         match PILImage("YCbCr",ch_repr):
                            _coconut_match_temp_96 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_94[1], _coconut_sentinel)  #175:         match PILImage("YCbCr",ch_repr):
                            if (_coconut_match_temp_95 is not _coconut_sentinel) and (_coconut_match_temp_95 == "YCbCr") and (_coconut_match_temp_96 is not _coconut_sentinel):  #175:         match PILImage("YCbCr",ch_repr):
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_96  #175:         match PILImage("YCbCr",ch_repr):
                                _coconut_case_match_check_3 = True  #175:         match PILImage("YCbCr",ch_repr):
                        if _coconut_case_match_check_3:  #175:         match PILImage("YCbCr",ch_repr):
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #175:         match PILImage("YCbCr",ch_repr):
                                ch_repr = _coconut_match_set_name_ch_repr  #175:         match PILImage("YCbCr",ch_repr):




        if _coconut_case_match_check_3:  #175:         match PILImage("YCbCr",ch_repr):
            return ([DataEdge(imdef, Numpy("uint8", "HWC", ch_repr, VR_0_255), np.array, 1, name="YCbCr image to numpy"),])  #176:                     return [DataEdge(imdef,
    if not _coconut_case_match_check_3:  #182:         match PILImage(mode,ch_repr):
        _coconut_match_temp_97 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #182:         match PILImage(mode,ch_repr):
        _coconut_case_match_check_3 = True  #182:         match PILImage(mode,ch_repr):
        if _coconut_case_match_check_3:  #182:         match PILImage(mode,ch_repr):
            _coconut_case_match_check_3 = False  #182:         match PILImage(mode,ch_repr):
            if not _coconut_case_match_check_3:  #182:         match PILImage(mode,ch_repr):
                _coconut_match_set_name_mode = _coconut_sentinel  #182:         match PILImage(mode,ch_repr):
                _coconut_match_set_name_ch_repr = _coconut_sentinel  #182:         match PILImage(mode,ch_repr):
                if (_coconut_match_temp_97) and (_coconut.isinstance(_coconut_case_match_to_3, PILImage)) and (_coconut.len(_coconut_case_match_to_3) >= 2):  #182:         match PILImage(mode,ch_repr):
                    _coconut_match_set_name_mode = _coconut_case_match_to_3[0]  #182:         match PILImage(mode,ch_repr):
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_3[1]  #182:         match PILImage(mode,ch_repr):
                    _coconut_match_temp_98 = _coconut.len(_coconut_case_match_to_3) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_3.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {}) and _coconut_case_match_to_3[i] == _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_3.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_3, "__match_args__") else _coconut.len(_coconut_case_match_to_3) == 2  # type: ignore  #182:         match PILImage(mode,ch_repr):
                    if _coconut_match_temp_98:  #182:         match PILImage(mode,ch_repr):
                        _coconut_case_match_check_3 = True  #182:         match PILImage(mode,ch_repr):
                if _coconut_case_match_check_3:  #182:         match PILImage(mode,ch_repr):
                    if _coconut_match_set_name_mode is not _coconut_sentinel:  #182:         match PILImage(mode,ch_repr):
                        mode = _coconut_match_set_name_mode  #182:         match PILImage(mode,ch_repr):
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #182:         match PILImage(mode,ch_repr):
                        ch_repr = _coconut_match_set_name_ch_repr  #182:         match PILImage(mode,ch_repr):

            if not _coconut_case_match_check_3:  #182:         match PILImage(mode,ch_repr):
                if (not _coconut_match_temp_97) and (_coconut.isinstance(_coconut_case_match_to_3, PILImage)):  #182:         match PILImage(mode,ch_repr):
                    _coconut_case_match_check_3 = True  #182:         match PILImage(mode,ch_repr):
                if _coconut_case_match_check_3:  #182:         match PILImage(mode,ch_repr):
                    _coconut_case_match_check_3 = False  #182:         match PILImage(mode,ch_repr):
                    if not _coconut_case_match_check_3:  #182:         match PILImage(mode,ch_repr):
                        if _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #182:         match PILImage(mode,ch_repr):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #182:         match PILImage(mode,ch_repr):
                            _coconut_case_match_check_3 = True  #182:         match PILImage(mode,ch_repr):

                    if not _coconut_case_match_check_3:  #182:         match PILImage(mode,ch_repr):
                        _coconut_match_set_name_mode = _coconut_sentinel  #182:         match PILImage(mode,ch_repr):
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  #182:         match PILImage(mode,ch_repr):
                        if not _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #182:         match PILImage(mode,ch_repr):
                            _coconut_match_temp_99 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #182:         match PILImage(mode,ch_repr):
                            if not _coconut.isinstance(_coconut_match_temp_99, _coconut.tuple):  #182:         match PILImage(mode,ch_repr):
                                raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #182:         match PILImage(mode,ch_repr):
                            if _coconut.len(_coconut_match_temp_99) < 2:  #182:         match PILImage(mode,ch_repr):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_99),))  #182:         match PILImage(mode,ch_repr):
                            _coconut_match_temp_100 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_99[0], _coconut_sentinel)  #182:         match PILImage(mode,ch_repr):
                            _coconut_match_temp_101 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_99[1], _coconut_sentinel)  #182:         match PILImage(mode,ch_repr):
                            if (_coconut_match_temp_100 is not _coconut_sentinel) and (_coconut_match_temp_101 is not _coconut_sentinel):  #182:         match PILImage(mode,ch_repr):
                                _coconut_match_set_name_mode = _coconut_match_temp_100  #182:         match PILImage(mode,ch_repr):
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_101  #182:         match PILImage(mode,ch_repr):
                                _coconut_case_match_check_3 = True  #182:         match PILImage(mode,ch_repr):
                        if _coconut_case_match_check_3:  #182:         match PILImage(mode,ch_repr):
                            if _coconut_match_set_name_mode is not _coconut_sentinel:  #182:         match PILImage(mode,ch_repr):
                                mode = _coconut_match_set_name_mode  #182:         match PILImage(mode,ch_repr):
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #182:         match PILImage(mode,ch_repr):
                                ch_repr = _coconut_match_set_name_ch_repr  #182:         match PILImage(mode,ch_repr):




        if _coconut_case_match_check_3:  #182:         match PILImage(mode,ch_repr):
            return ([DataEdge(imdef, Numpy("uint8", "HWC", ch_repr, VR_0_255), np.array, 1, name="{_coconut_format_0} to numpy".format(_coconut_format_0=(ch_repr))),])  #183:                     return [DataEdge(

    if not _coconut_case_match_check_3:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
        _coconut_match_temp_102 = _coconut.getattr(PILImages, "_coconut_is_data", False) or _coconut.isinstance(PILImages, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImages)  # type: ignore  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
        _coconut_case_match_check_3 = True  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
        if _coconut_case_match_check_3:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
            _coconut_case_match_check_3 = False  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
            if not _coconut_case_match_check_3:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                _coconut_match_set_name_ch_repr = _coconut_sentinel  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                if (_coconut_match_temp_102) and (_coconut.isinstance(_coconut_case_match_to_3, PILImages)) and (_coconut.len(_coconut_case_match_to_3) >= 2) and (_coconut_case_match_to_3[0] == "L"):  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_3[1]  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                    _coconut_match_temp_103 = _coconut.len(_coconut_case_match_to_3) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_3.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {}) and _coconut_case_match_to_3[i] == _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_3.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_3, "__match_args__") else _coconut.len(_coconut_case_match_to_3) == 2  # type: ignore  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                    if _coconut_match_temp_103:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                        _coconut_case_match_check_3 = True  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                if _coconut_case_match_check_3:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                        ch_repr = _coconut_match_set_name_ch_repr  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
# A grayscale Image becomes a numpy array
            if not _coconut_case_match_check_3:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                if (not _coconut_match_temp_102) and (_coconut.isinstance(_coconut_case_match_to_3, PILImages)):  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                    _coconut_case_match_check_3 = True  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                if _coconut_case_match_check_3:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                    _coconut_case_match_check_3 = False  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                    if not _coconut_case_match_check_3:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                        if _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports 1)")  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                            _coconut_case_match_check_3 = True  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
# A grayscale Image becomes a numpy array
                    if not _coconut_case_match_check_3:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                        if not _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                            _coconut_match_temp_104 = _coconut.getattr(PILImages, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                            if not _coconut.isinstance(_coconut_match_temp_104, _coconut.tuple):  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                                raise _coconut.TypeError("PILImages.__match_args__ must be a tuple")  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                            if _coconut.len(_coconut_match_temp_104) < 2:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports %s)" % (_coconut.len(_coconut_match_temp_104),))  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                            _coconut_match_temp_105 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_104[0], _coconut_sentinel)  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                            _coconut_match_temp_106 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_104[1], _coconut_sentinel)  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                            if (_coconut_match_temp_105 is not _coconut_sentinel) and (_coconut_match_temp_105 == "L") and (_coconut_match_temp_106 is not _coconut_sentinel):  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_106  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                                _coconut_case_match_check_3 = True  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                        if _coconut_case_match_check_3:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
                                ch_repr = _coconut_match_set_name_ch_repr  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
# A grayscale Image becomes a numpy array
# A grayscale Image becomes a numpy array
# A grayscale Image becomes a numpy array
# A grayscale Image becomes a numpy array
        if _coconut_case_match_check_3:  # A grayscale Image becomes a numpy array  #191:         match PILImages("L",ch_repr): # A grayscale Image becomes a numpy array
            return ([DataEdge(imdef, Numpy("uint8", "BHW", ch_repr, VR_0_255), (_coconut_base_compose(_coconut_partial(fmap, np.array), (np.array, 0, False))), 1, name="image_to_numpy"),])  #192:             return [DataEdge(imdef,
    if not _coconut_case_match_check_3:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
        _coconut_match_temp_107 = _coconut.getattr(PILImages, "_coconut_is_data", False) or _coconut.isinstance(PILImages, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImages)  # type: ignore  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
        _coconut_case_match_check_3 = True  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
        if _coconut_case_match_check_3:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
            _coconut_case_match_check_3 = False  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
            if not _coconut_case_match_check_3:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                _coconut_match_set_name_mode = _coconut_sentinel  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                _coconut_match_set_name_ch_repr = _coconut_sentinel  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                if (_coconut_match_temp_107) and (_coconut.isinstance(_coconut_case_match_to_3, PILImages)) and (_coconut.len(_coconut_case_match_to_3) >= 2):  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                    _coconut_match_set_name_mode = _coconut_case_match_to_3[0]  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_3[1]  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                    _coconut_match_temp_108 = _coconut.len(_coconut_case_match_to_3) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_3.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {}) and _coconut_case_match_to_3[i] == _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_3.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_3, "__match_args__") else _coconut.len(_coconut_case_match_to_3) == 2  # type: ignore  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                    if _coconut_match_temp_108:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                        _coconut_case_match_check_3 = True  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                if _coconut_case_match_check_3:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                    if _coconut_match_set_name_mode is not _coconut_sentinel:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                        mode = _coconut_match_set_name_mode  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                        ch_repr = _coconut_match_set_name_ch_repr  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
# A multi-channel Image becomes a numpy array
            if not _coconut_case_match_check_3:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                if (not _coconut_match_temp_107) and (_coconut.isinstance(_coconut_case_match_to_3, PILImages)):  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                    _coconut_case_match_check_3 = True  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                if _coconut_case_match_check_3:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                    _coconut_case_match_check_3 = False  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                    if not _coconut_case_match_check_3:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                        if _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports 1)")  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                            _coconut_case_match_check_3 = True  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
# A multi-channel Image becomes a numpy array
                    if not _coconut_case_match_check_3:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                        _coconut_match_set_name_mode = _coconut_sentinel  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                        if not _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                            _coconut_match_temp_109 = _coconut.getattr(PILImages, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                            if not _coconut.isinstance(_coconut_match_temp_109, _coconut.tuple):  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                                raise _coconut.TypeError("PILImages.__match_args__ must be a tuple")  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                            if _coconut.len(_coconut_match_temp_109) < 2:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports %s)" % (_coconut.len(_coconut_match_temp_109),))  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                            _coconut_match_temp_110 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_109[0], _coconut_sentinel)  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                            _coconut_match_temp_111 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_109[1], _coconut_sentinel)  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                            if (_coconut_match_temp_110 is not _coconut_sentinel) and (_coconut_match_temp_111 is not _coconut_sentinel):  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                                _coconut_match_set_name_mode = _coconut_match_temp_110  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_111  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                                _coconut_case_match_check_3 = True  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                        if _coconut_case_match_check_3:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                            if _coconut_match_set_name_mode is not _coconut_sentinel:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                                mode = _coconut_match_set_name_mode  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
                                ch_repr = _coconut_match_set_name_ch_repr  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
# A multi-channel Image becomes a numpy array
# A multi-channel Image becomes a numpy array
# A multi-channel Image becomes a numpy array
# A multi-channel Image becomes a numpy array
        if _coconut_case_match_check_3:  # A multi-channel Image becomes a numpy array  #197:         match PILImages(mode,ch_repr):# A multi-channel Image becomes a numpy array
            return ([DataEdge(imdef, Numpy("uint8", "BHWC", ch_repr, VR_0_255), (_coconut_base_compose(_coconut_partial(fmap, np.array), (np.array, 0, False))), 1, name="image_to_numpy"),])  #198:             return [DataEdge(imdef,
    return ([])  #203:     return []


@to_imagedef  #205: @to_imagedef
def change_dtype(imdef: 'ImageDef'):  # TODO match value range to dtype with bool type  #206: def change_dtype(imdef:ImageDef):# TODO match value range to dtype with bool type
    _coconut_case_match_to_4 = imdef  #207:     case imdef:
    _coconut_case_match_check_4 = False  #207:     case imdef:
    _coconut_match_temp_112 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #207:     case imdef:
    _coconut_case_match_check_4 = True  #207:     case imdef:
    if _coconut_case_match_check_4:  #207:     case imdef:
        _coconut_case_match_check_4 = False  #207:     case imdef:
        if not _coconut_case_match_check_4:  #207:     case imdef:
            _coconut_match_set_name_dtype = _coconut_sentinel  #207:     case imdef:
            _coconut_match_set_name_arng = _coconut_sentinel  #207:     case imdef:
            _coconut_match_set_name_ch_repr = _coconut_sentinel  #207:     case imdef:
            _coconut_match_set_name_vr = _coconut_sentinel  #207:     case imdef:
            if (_coconut_match_temp_112) and (_coconut.isinstance(_coconut_case_match_to_4, Numpy)) and (_coconut.len(_coconut_case_match_to_4) >= 4):  #207:     case imdef:
                _coconut_match_set_name_dtype = _coconut_case_match_to_4[0]  #207:     case imdef:
                _coconut_match_set_name_arng = _coconut_case_match_to_4[1]  #207:     case imdef:
                _coconut_match_set_name_ch_repr = _coconut_case_match_to_4[2]  #207:     case imdef:
                _coconut_match_set_name_vr = _coconut_case_match_to_4[3]  #207:     case imdef:
                _coconut_match_temp_113 = _coconut.len(_coconut_case_match_to_4) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_4.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_4, "_coconut_data_defaults", {}) and _coconut_case_match_to_4[i] == _coconut.getattr(_coconut_case_match_to_4, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_4.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_4, "__match_args__") else _coconut.len(_coconut_case_match_to_4) == 4  # type: ignore  #207:     case imdef:
                if _coconut_match_temp_113:  #207:     case imdef:
                    _coconut_case_match_check_4 = True  #207:     case imdef:
            if _coconut_case_match_check_4:  #207:     case imdef:
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #207:     case imdef:
                    dtype = _coconut_match_set_name_dtype  #207:     case imdef:
                if _coconut_match_set_name_arng is not _coconut_sentinel:  #207:     case imdef:
                    arng = _coconut_match_set_name_arng  #207:     case imdef:
                if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #207:     case imdef:
                    ch_repr = _coconut_match_set_name_ch_repr  #207:     case imdef:
                if _coconut_match_set_name_vr is not _coconut_sentinel:  #207:     case imdef:
                    vr = _coconut_match_set_name_vr  #207:     case imdef:

        if not _coconut_case_match_check_4:  #207:     case imdef:
            if (not _coconut_match_temp_112) and (_coconut.isinstance(_coconut_case_match_to_4, Numpy)):  #207:     case imdef:
                _coconut_case_match_check_4 = True  #207:     case imdef:
            if _coconut_case_match_check_4:  #207:     case imdef:
                _coconut_case_match_check_4 = False  #207:     case imdef:
                if not _coconut_case_match_check_4:  #207:     case imdef:
                    if _coconut.type(_coconut_case_match_to_4) in _coconut_self_match_types:  #207:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #207:     case imdef:
                        _coconut_case_match_check_4 = True  #207:     case imdef:

                if not _coconut_case_match_check_4:  #207:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #207:     case imdef:
                    _coconut_match_set_name_arng = _coconut_sentinel  #207:     case imdef:
                    _coconut_match_set_name_ch_repr = _coconut_sentinel  #207:     case imdef:
                    _coconut_match_set_name_vr = _coconut_sentinel  #207:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_4) in _coconut_self_match_types:  #207:     case imdef:
                        _coconut_match_temp_114 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #207:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_114, _coconut.tuple):  #207:     case imdef:
                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #207:     case imdef:
                        if _coconut.len(_coconut_match_temp_114) < 4:  #207:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_114),))  #207:     case imdef:
                        _coconut_match_temp_115 = _coconut.getattr(_coconut_case_match_to_4, _coconut_match_temp_114[0], _coconut_sentinel)  #207:     case imdef:
                        _coconut_match_temp_116 = _coconut.getattr(_coconut_case_match_to_4, _coconut_match_temp_114[1], _coconut_sentinel)  #207:     case imdef:
                        _coconut_match_temp_117 = _coconut.getattr(_coconut_case_match_to_4, _coconut_match_temp_114[2], _coconut_sentinel)  #207:     case imdef:
                        _coconut_match_temp_118 = _coconut.getattr(_coconut_case_match_to_4, _coconut_match_temp_114[3], _coconut_sentinel)  #207:     case imdef:
                        if (_coconut_match_temp_115 is not _coconut_sentinel) and (_coconut_match_temp_116 is not _coconut_sentinel) and (_coconut_match_temp_117 is not _coconut_sentinel) and (_coconut_match_temp_118 is not _coconut_sentinel):  #207:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_match_temp_115  #207:     case imdef:
                            _coconut_match_set_name_arng = _coconut_match_temp_116  #207:     case imdef:
                            _coconut_match_set_name_ch_repr = _coconut_match_temp_117  #207:     case imdef:
                            _coconut_match_set_name_vr = _coconut_match_temp_118  #207:     case imdef:
                            _coconut_case_match_check_4 = True  #207:     case imdef:
                    if _coconut_case_match_check_4:  #207:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #207:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #207:     case imdef:
                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #207:     case imdef:
                            arng = _coconut_match_set_name_arng  #207:     case imdef:
                        if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #207:     case imdef:
                            ch_repr = _coconut_match_set_name_ch_repr  #207:     case imdef:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #207:     case imdef:
                            vr = _coconut_match_set_name_vr  #207:     case imdef:




    if _coconut_case_match_check_4:  #207:     case imdef:
        return ([DataEdge(imdef, imdef.__class__(_dtype, arng, ch_repr, vr), _coconut.operator.methodcaller("astype", _dtype), 1, name="{_coconut_format_0} to {_coconut_format_1}".format(_coconut_format_0=(dtype), _coconut_format_1=(_dtype))) for _dtype in DTYPES if _dtype != dtype])  #209:             return [DataEdge(
    return ([])  #216:     return []

# SHAPE SHIFTING RULES



def ss_to_ms(ss, meta):  #221: def ss_to_ms(ss,meta):
    if "shape" in meta:  #222:     if "shape" in meta:
        shape = meta["shape"]  #223:         shape=meta["shape"]
        new_shape = ss(shape)  #224:         new_shape = ss(shape)
        return (fdict(_coconut_dict_merge(meta, _coconut.dict((("shape", new_shape),)))))  #225:         return fdict({**meta,"shape":new_shape})
    return (meta)  #226:     return meta


ms_0231 = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], s[2], s[3], s[1])))  #228: ms_0231 = (s->(s[0],s[2],s[3],s[1])) |> ss_to_ms$
ms_0312 = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], s[3], s[1], s[2])))  #229: ms_0312 = (s->(s[0],s[3],s[1],s[2])) |> ss_to_ms$

def change_arng(imdef):  #231: def change_arng(imdef):
    _coconut_case_match_to_5 = imdef  #232:     case imdef:
    _coconut_case_match_check_5 = False  #232:     case imdef:
    _coconut_match_temp_119 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #232:     case imdef:
    _coconut_case_match_check_5 = True  #232:     case imdef:
    if _coconut_case_match_check_5:  #232:     case imdef:
        _coconut_case_match_check_5 = False  #232:     case imdef:
        if not _coconut_case_match_check_5:  #232:     case imdef:
            if (_coconut_match_temp_119) and (_coconut.isinstance(_coconut_case_match_to_5, Numpy)) and (_coconut.len(_coconut_case_match_to_5) >= 4) and (_coconut_case_match_to_5[1] == "BCHW"):  #232:     case imdef:
                _coconut_match_temp_120 = _coconut.len(_coconut_case_match_to_5) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_5.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_5, "_coconut_data_defaults", {}) and _coconut_case_match_to_5[i] == _coconut.getattr(_coconut_case_match_to_5, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_5.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_5, "__match_args__") else _coconut.len(_coconut_case_match_to_5) == 4  # type: ignore  #232:     case imdef:
                if _coconut_match_temp_120:  #232:     case imdef:
                    _coconut_case_match_check_5 = True  #232:     case imdef:

        if not _coconut_case_match_check_5:  #232:     case imdef:
            if (not _coconut_match_temp_119) and (_coconut.isinstance(_coconut_case_match_to_5, Numpy)):  #232:     case imdef:
                _coconut_case_match_check_5 = True  #232:     case imdef:
            if _coconut_case_match_check_5:  #232:     case imdef:
                _coconut_case_match_check_5 = False  #232:     case imdef:
                if not _coconut_case_match_check_5:  #232:     case imdef:
                    if _coconut.type(_coconut_case_match_to_5) in _coconut_self_match_types:  #232:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #232:     case imdef:
                        _coconut_case_match_check_5 = True  #232:     case imdef:

                if not _coconut_case_match_check_5:  #232:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_5) in _coconut_self_match_types:  #232:     case imdef:
                        _coconut_match_temp_121 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #232:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_121, _coconut.tuple):  #232:     case imdef:
                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #232:     case imdef:
                        if _coconut.len(_coconut_match_temp_121) < 4:  #232:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_121),))  #232:     case imdef:
                        _coconut_match_temp_122 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_121[0], _coconut_sentinel)  #232:     case imdef:
                        _coconut_match_temp_123 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_121[1], _coconut_sentinel)  #232:     case imdef:
                        _coconut_match_temp_124 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_121[2], _coconut_sentinel)  #232:     case imdef:
                        _coconut_match_temp_125 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_121[3], _coconut_sentinel)  #232:     case imdef:
                        if (_coconut_match_temp_122 is not _coconut_sentinel) and (_coconut_match_temp_123 is not _coconut_sentinel) and (_coconut_match_temp_123 == "BCHW") and (_coconut_match_temp_124 is not _coconut_sentinel) and (_coconut_match_temp_125 is not _coconut_sentinel):  #232:     case imdef:
                            _coconut_case_match_check_5 = True  #232:     case imdef:




    if _coconut_case_match_check_5:  #232:     case imdef:
        return ([(_coconut.operator.methodcaller("transpose", 0, 2, 3, 1), "BHWC", ms_0231),])  #234:             return [(.transpose(0,2,3,1),"BHWC",ms_0231)]
    if not _coconut_case_match_check_5:  #235:         match Numpy(_,"BHWC",_,_):
        _coconut_match_temp_126 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #235:         match Numpy(_,"BHWC",_,_):
        _coconut_case_match_check_5 = True  #235:         match Numpy(_,"BHWC",_,_):
        if _coconut_case_match_check_5:  #235:         match Numpy(_,"BHWC",_,_):
            _coconut_case_match_check_5 = False  #235:         match Numpy(_,"BHWC",_,_):
            if not _coconut_case_match_check_5:  #235:         match Numpy(_,"BHWC",_,_):
                if (_coconut_match_temp_126) and (_coconut.isinstance(_coconut_case_match_to_5, Numpy)) and (_coconut.len(_coconut_case_match_to_5) >= 4) and (_coconut_case_match_to_5[1] == "BHWC"):  #235:         match Numpy(_,"BHWC",_,_):
                    _coconut_match_temp_127 = _coconut.len(_coconut_case_match_to_5) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_5.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_5, "_coconut_data_defaults", {}) and _coconut_case_match_to_5[i] == _coconut.getattr(_coconut_case_match_to_5, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_5.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_5, "__match_args__") else _coconut.len(_coconut_case_match_to_5) == 4  # type: ignore  #235:         match Numpy(_,"BHWC",_,_):
                    if _coconut_match_temp_127:  #235:         match Numpy(_,"BHWC",_,_):
                        _coconut_case_match_check_5 = True  #235:         match Numpy(_,"BHWC",_,_):

            if not _coconut_case_match_check_5:  #235:         match Numpy(_,"BHWC",_,_):
                if (not _coconut_match_temp_126) and (_coconut.isinstance(_coconut_case_match_to_5, Numpy)):  #235:         match Numpy(_,"BHWC",_,_):
                    _coconut_case_match_check_5 = True  #235:         match Numpy(_,"BHWC",_,_):
                if _coconut_case_match_check_5:  #235:         match Numpy(_,"BHWC",_,_):
                    _coconut_case_match_check_5 = False  #235:         match Numpy(_,"BHWC",_,_):
                    if not _coconut_case_match_check_5:  #235:         match Numpy(_,"BHWC",_,_):
                        if _coconut.type(_coconut_case_match_to_5) in _coconut_self_match_types:  #235:         match Numpy(_,"BHWC",_,_):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #235:         match Numpy(_,"BHWC",_,_):
                            _coconut_case_match_check_5 = True  #235:         match Numpy(_,"BHWC",_,_):

                    if not _coconut_case_match_check_5:  #235:         match Numpy(_,"BHWC",_,_):
                        if not _coconut.type(_coconut_case_match_to_5) in _coconut_self_match_types:  #235:         match Numpy(_,"BHWC",_,_):
                            _coconut_match_temp_128 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #235:         match Numpy(_,"BHWC",_,_):
                            if not _coconut.isinstance(_coconut_match_temp_128, _coconut.tuple):  #235:         match Numpy(_,"BHWC",_,_):
                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #235:         match Numpy(_,"BHWC",_,_):
                            if _coconut.len(_coconut_match_temp_128) < 4:  #235:         match Numpy(_,"BHWC",_,_):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_128),))  #235:         match Numpy(_,"BHWC",_,_):
                            _coconut_match_temp_129 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_128[0], _coconut_sentinel)  #235:         match Numpy(_,"BHWC",_,_):
                            _coconut_match_temp_130 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_128[1], _coconut_sentinel)  #235:         match Numpy(_,"BHWC",_,_):
                            _coconut_match_temp_131 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_128[2], _coconut_sentinel)  #235:         match Numpy(_,"BHWC",_,_):
                            _coconut_match_temp_132 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_128[3], _coconut_sentinel)  #235:         match Numpy(_,"BHWC",_,_):
                            if (_coconut_match_temp_129 is not _coconut_sentinel) and (_coconut_match_temp_130 is not _coconut_sentinel) and (_coconut_match_temp_130 == "BHWC") and (_coconut_match_temp_131 is not _coconut_sentinel) and (_coconut_match_temp_132 is not _coconut_sentinel):  #235:         match Numpy(_,"BHWC",_,_):
                                _coconut_case_match_check_5 = True  #235:         match Numpy(_,"BHWC",_,_):




        if _coconut_case_match_check_5:  #235:         match Numpy(_,"BHWC",_,_):
            return ([(_coconut.operator.methodcaller("transpose", 0, 3, 1, 2), "BCHW", ms_0312),])  #236:             return [(.transpose(0,3,1,2),"BCHW",ms_0312)]
    if not _coconut_case_match_check_5:  #237:         match Torch(_,"BCHW",_,_):
        _coconut_match_temp_133 = _coconut.getattr(Torch, "_coconut_is_data", False) or _coconut.isinstance(Torch, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Torch)  # type: ignore  #237:         match Torch(_,"BCHW",_,_):
        _coconut_case_match_check_5 = True  #237:         match Torch(_,"BCHW",_,_):
        if _coconut_case_match_check_5:  #237:         match Torch(_,"BCHW",_,_):
            _coconut_case_match_check_5 = False  #237:         match Torch(_,"BCHW",_,_):
            if not _coconut_case_match_check_5:  #237:         match Torch(_,"BCHW",_,_):
                if (_coconut_match_temp_133) and (_coconut.isinstance(_coconut_case_match_to_5, Torch)) and (_coconut.len(_coconut_case_match_to_5) >= 4) and (_coconut_case_match_to_5[1] == "BCHW"):  #237:         match Torch(_,"BCHW",_,_):
                    _coconut_match_temp_134 = _coconut.len(_coconut_case_match_to_5) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_5.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_5, "_coconut_data_defaults", {}) and _coconut_case_match_to_5[i] == _coconut.getattr(_coconut_case_match_to_5, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_5.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_5, "__match_args__") else _coconut.len(_coconut_case_match_to_5) == 4  # type: ignore  #237:         match Torch(_,"BCHW",_,_):
                    if _coconut_match_temp_134:  #237:         match Torch(_,"BCHW",_,_):
                        _coconut_case_match_check_5 = True  #237:         match Torch(_,"BCHW",_,_):

            if not _coconut_case_match_check_5:  #237:         match Torch(_,"BCHW",_,_):
                if (not _coconut_match_temp_133) and (_coconut.isinstance(_coconut_case_match_to_5, Torch)):  #237:         match Torch(_,"BCHW",_,_):
                    _coconut_case_match_check_5 = True  #237:         match Torch(_,"BCHW",_,_):
                if _coconut_case_match_check_5:  #237:         match Torch(_,"BCHW",_,_):
                    _coconut_case_match_check_5 = False  #237:         match Torch(_,"BCHW",_,_):
                    if not _coconut_case_match_check_5:  #237:         match Torch(_,"BCHW",_,_):
                        if _coconut.type(_coconut_case_match_to_5) in _coconut_self_match_types:  #237:         match Torch(_,"BCHW",_,_):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports 1)")  #237:         match Torch(_,"BCHW",_,_):
                            _coconut_case_match_check_5 = True  #237:         match Torch(_,"BCHW",_,_):

                    if not _coconut_case_match_check_5:  #237:         match Torch(_,"BCHW",_,_):
                        if not _coconut.type(_coconut_case_match_to_5) in _coconut_self_match_types:  #237:         match Torch(_,"BCHW",_,_):
                            _coconut_match_temp_135 = _coconut.getattr(Torch, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #237:         match Torch(_,"BCHW",_,_):
                            if not _coconut.isinstance(_coconut_match_temp_135, _coconut.tuple):  #237:         match Torch(_,"BCHW",_,_):
                                raise _coconut.TypeError("Torch.__match_args__ must be a tuple")  #237:         match Torch(_,"BCHW",_,_):
                            if _coconut.len(_coconut_match_temp_135) < 4:  #237:         match Torch(_,"BCHW",_,_):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports %s)" % (_coconut.len(_coconut_match_temp_135),))  #237:         match Torch(_,"BCHW",_,_):
                            _coconut_match_temp_136 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_135[0], _coconut_sentinel)  #237:         match Torch(_,"BCHW",_,_):
                            _coconut_match_temp_137 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_135[1], _coconut_sentinel)  #237:         match Torch(_,"BCHW",_,_):
                            _coconut_match_temp_138 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_135[2], _coconut_sentinel)  #237:         match Torch(_,"BCHW",_,_):
                            _coconut_match_temp_139 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_135[3], _coconut_sentinel)  #237:         match Torch(_,"BCHW",_,_):
                            if (_coconut_match_temp_136 is not _coconut_sentinel) and (_coconut_match_temp_137 is not _coconut_sentinel) and (_coconut_match_temp_137 == "BCHW") and (_coconut_match_temp_138 is not _coconut_sentinel) and (_coconut_match_temp_139 is not _coconut_sentinel):  #237:         match Torch(_,"BCHW",_,_):
                                _coconut_case_match_check_5 = True  #237:         match Torch(_,"BCHW",_,_):




        if _coconut_case_match_check_5:  #237:         match Torch(_,"BCHW",_,_):
            return ([(_coconut_base_compose(_coconut.operator.methodcaller("transpose", 1, 2), (_coconut.operator.methodcaller("transpose", 2, 3), 0, False)), "BHWC", ms_0231),])  #238:             return [(.transpose(1,2) ..> .transpose(2,3),"BHWC",ms_0231)]
    if not _coconut_case_match_check_5:  #239:         match Torch(_,"BHWC",_,_):
        _coconut_match_temp_140 = _coconut.getattr(Torch, "_coconut_is_data", False) or _coconut.isinstance(Torch, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Torch)  # type: ignore  #239:         match Torch(_,"BHWC",_,_):
        _coconut_case_match_check_5 = True  #239:         match Torch(_,"BHWC",_,_):
        if _coconut_case_match_check_5:  #239:         match Torch(_,"BHWC",_,_):
            _coconut_case_match_check_5 = False  #239:         match Torch(_,"BHWC",_,_):
            if not _coconut_case_match_check_5:  #239:         match Torch(_,"BHWC",_,_):
                if (_coconut_match_temp_140) and (_coconut.isinstance(_coconut_case_match_to_5, Torch)) and (_coconut.len(_coconut_case_match_to_5) >= 4) and (_coconut_case_match_to_5[1] == "BHWC"):  #239:         match Torch(_,"BHWC",_,_):
                    _coconut_match_temp_141 = _coconut.len(_coconut_case_match_to_5) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_5.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_5, "_coconut_data_defaults", {}) and _coconut_case_match_to_5[i] == _coconut.getattr(_coconut_case_match_to_5, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_5.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_5, "__match_args__") else _coconut.len(_coconut_case_match_to_5) == 4  # type: ignore  #239:         match Torch(_,"BHWC",_,_):
                    if _coconut_match_temp_141:  #239:         match Torch(_,"BHWC",_,_):
                        _coconut_case_match_check_5 = True  #239:         match Torch(_,"BHWC",_,_):

            if not _coconut_case_match_check_5:  #239:         match Torch(_,"BHWC",_,_):
                if (not _coconut_match_temp_140) and (_coconut.isinstance(_coconut_case_match_to_5, Torch)):  #239:         match Torch(_,"BHWC",_,_):
                    _coconut_case_match_check_5 = True  #239:         match Torch(_,"BHWC",_,_):
                if _coconut_case_match_check_5:  #239:         match Torch(_,"BHWC",_,_):
                    _coconut_case_match_check_5 = False  #239:         match Torch(_,"BHWC",_,_):
                    if not _coconut_case_match_check_5:  #239:         match Torch(_,"BHWC",_,_):
                        if _coconut.type(_coconut_case_match_to_5) in _coconut_self_match_types:  #239:         match Torch(_,"BHWC",_,_):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports 1)")  #239:         match Torch(_,"BHWC",_,_):
                            _coconut_case_match_check_5 = True  #239:         match Torch(_,"BHWC",_,_):

                    if not _coconut_case_match_check_5:  #239:         match Torch(_,"BHWC",_,_):
                        if not _coconut.type(_coconut_case_match_to_5) in _coconut_self_match_types:  #239:         match Torch(_,"BHWC",_,_):
                            _coconut_match_temp_142 = _coconut.getattr(Torch, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #239:         match Torch(_,"BHWC",_,_):
                            if not _coconut.isinstance(_coconut_match_temp_142, _coconut.tuple):  #239:         match Torch(_,"BHWC",_,_):
                                raise _coconut.TypeError("Torch.__match_args__ must be a tuple")  #239:         match Torch(_,"BHWC",_,_):
                            if _coconut.len(_coconut_match_temp_142) < 4:  #239:         match Torch(_,"BHWC",_,_):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports %s)" % (_coconut.len(_coconut_match_temp_142),))  #239:         match Torch(_,"BHWC",_,_):
                            _coconut_match_temp_143 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_142[0], _coconut_sentinel)  #239:         match Torch(_,"BHWC",_,_):
                            _coconut_match_temp_144 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_142[1], _coconut_sentinel)  #239:         match Torch(_,"BHWC",_,_):
                            _coconut_match_temp_145 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_142[2], _coconut_sentinel)  #239:         match Torch(_,"BHWC",_,_):
                            _coconut_match_temp_146 = _coconut.getattr(_coconut_case_match_to_5, _coconut_match_temp_142[3], _coconut_sentinel)  #239:         match Torch(_,"BHWC",_,_):
                            if (_coconut_match_temp_143 is not _coconut_sentinel) and (_coconut_match_temp_144 is not _coconut_sentinel) and (_coconut_match_temp_144 == "BHWC") and (_coconut_match_temp_145 is not _coconut_sentinel) and (_coconut_match_temp_146 is not _coconut_sentinel):  #239:         match Torch(_,"BHWC",_,_):
                                _coconut_case_match_check_5 = True  #239:         match Torch(_,"BHWC",_,_):




        if _coconut_case_match_check_5:  #239:         match Torch(_,"BHWC",_,_):
            return ([(_coconut_base_compose(_coconut.operator.methodcaller("transpose", 2, 3), (_coconut.operator.methodcaller("transpose", 1, 2), 0, False)), "BCHW", ms_0312),])  #240:             return [(.transpose(2,3) ..> .transpose(1,2),"BCHW",ms_0312)]
    return ([])  #241:     return []

@to_imagedef  #242: @to_imagedef
def change_arrange(imdef: 'ImageDef'):  #243: def change_arrange(imdef:ImageDef):
    _coconut_match_to_0 = imdef  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
    _coconut_match_check_4 = False  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
    _coconut_match_temp_147 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
    _coconut_match_check_4 = True  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
    if _coconut_match_check_4:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
        _coconut_match_check_4 = False  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
        if not _coconut_match_check_4:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
            _coconut_match_set_name_dtype = _coconut_sentinel  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
            _coconut_match_set_name_arng = _coconut_sentinel  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
            _coconut_match_set_name_ch_repr = _coconut_sentinel  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
            _coconut_match_set_name_vr = _coconut_sentinel  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
            if (_coconut_match_temp_147) and (_coconut.isinstance(_coconut_match_to_0, TensorLike)) and (_coconut.len(_coconut_match_to_0) >= 4):  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                _coconut_match_set_name_dtype = _coconut_match_to_0[0]  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                _coconut_match_set_name_arng = _coconut_match_to_0[1]  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                _coconut_match_set_name_ch_repr = _coconut_match_to_0[2]  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                _coconut_match_set_name_vr = _coconut_match_to_0[3]  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                _coconut_match_temp_148 = _coconut.len(_coconut_match_to_0) <= _coconut.max(4, _coconut.len(_coconut_match_to_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_to_0, "_coconut_data_defaults", {}) and _coconut_match_to_0[i] == _coconut.getattr(_coconut_match_to_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_to_0.__match_args__))) if _coconut.hasattr(_coconut_match_to_0, "__match_args__") else _coconut.len(_coconut_match_to_0) == 4  # type: ignore  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                if _coconut_match_temp_148:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    _coconut_match_check_4 = True  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
            if _coconut_match_check_4:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    dtype = _coconut_match_set_name_dtype  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                if _coconut_match_set_name_arng is not _coconut_sentinel:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    arng = _coconut_match_set_name_arng  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    ch_repr = _coconut_match_set_name_ch_repr  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                if _coconut_match_set_name_vr is not _coconut_sentinel:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    vr = _coconut_match_set_name_vr  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:

        if not _coconut_match_check_4:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
            if (not _coconut_match_temp_147) and (_coconut.isinstance(_coconut_match_to_0, TensorLike)):  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                _coconut_match_check_4 = True  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
            if _coconut_match_check_4:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                _coconut_match_check_4 = False  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                if not _coconut_match_check_4:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    if _coconut.type(_coconut_match_to_0) in _coconut_self_match_types:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        _coconut_match_check_4 = True  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:

                if not _coconut_match_check_4:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    _coconut_match_set_name_arng = _coconut_sentinel  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    _coconut_match_set_name_ch_repr = _coconut_sentinel  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    _coconut_match_set_name_vr = _coconut_sentinel  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    if not _coconut.type(_coconut_match_to_0) in _coconut_self_match_types:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        _coconut_match_temp_149 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        if not _coconut.isinstance(_coconut_match_temp_149, _coconut.tuple):  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                            raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        if _coconut.len(_coconut_match_temp_149) < 4:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_149),))  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        _coconut_match_temp_150 = _coconut.getattr(_coconut_match_to_0, _coconut_match_temp_149[0], _coconut_sentinel)  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        _coconut_match_temp_151 = _coconut.getattr(_coconut_match_to_0, _coconut_match_temp_149[1], _coconut_sentinel)  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        _coconut_match_temp_152 = _coconut.getattr(_coconut_match_to_0, _coconut_match_temp_149[2], _coconut_sentinel)  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        _coconut_match_temp_153 = _coconut.getattr(_coconut_match_to_0, _coconut_match_temp_149[3], _coconut_sentinel)  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        if (_coconut_match_temp_150 is not _coconut_sentinel) and (_coconut_match_temp_151 is not _coconut_sentinel) and (_coconut_match_temp_152 is not _coconut_sentinel) and (_coconut_match_temp_153 is not _coconut_sentinel):  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                            _coconut_match_set_name_dtype = _coconut_match_temp_150  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                            _coconut_match_set_name_arng = _coconut_match_temp_151  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                            _coconut_match_set_name_ch_repr = _coconut_match_temp_152  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                            _coconut_match_set_name_vr = _coconut_match_temp_153  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                            _coconut_match_check_4 = True  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                    if _coconut_match_check_4:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                            dtype = _coconut_match_set_name_dtype  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                            arng = _coconut_match_set_name_arng  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                            ch_repr = _coconut_match_set_name_ch_repr  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
                            vr = _coconut_match_set_name_vr  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:




    if _coconut_match_check_4:  #244:     match TensorLike(dtype,arng,ch_repr,vr) in imdef:
        return ([DataEdge(imdef, imdef.__class__(dtype, _arng, ch_repr, vr), f, 1, name="{_coconut_format_0} to {_coconut_format_1}".format(_coconut_format_0=(arng), _coconut_format_1=(_arng)), meta_shifter=meta_shifter) for f, _arng, meta_shifter in change_arng(imdef)])  #245:         return [DataEdge(imdef,
    return ([])  #251:     return []

ms_drop_bhwc_alpha = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], s[1], s[2], 3)))  #252: ms_drop_bhwc_alpha = (s->(s[0],s[1],s[2],3)) |> ss_to_ms$
ms_drop_bchw_alpha = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], 3, s[2], s[3])))  #253: ms_drop_bchw_alpha = (s->(s[0],3,s[2],s[3])) |> ss_to_ms$
@to_imagedef  #254: @to_imagedef
def drop_alpha(imdef):  #255: def drop_alpha(imdef):
    _coconut_case_match_to_6 = imdef  #256:     case imdef:
    _coconut_case_match_check_6 = False  #256:     case imdef:
    _coconut_match_temp_154 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #256:     case imdef:
    _coconut_case_match_check_6 = True  #256:     case imdef:
    if _coconut_case_match_check_6:  #256:     case imdef:
        _coconut_case_match_check_6 = False  #256:     case imdef:
        if not _coconut_case_match_check_6:  #256:     case imdef:
            _coconut_match_set_name_dtype = _coconut_sentinel  #256:     case imdef:
            _coconut_match_set_name_vr = _coconut_sentinel  #256:     case imdef:
            if (_coconut_match_temp_154) and (_coconut.isinstance(_coconut_case_match_to_6, TensorLike)) and (_coconut.len(_coconut_case_match_to_6) >= 4) and (_coconut_case_match_to_6[1] == "BHWC") and (_coconut_case_match_to_6[2] == "RGBA"):  #256:     case imdef:
                _coconut_match_set_name_dtype = _coconut_case_match_to_6[0]  #256:     case imdef:
                _coconut_match_set_name_vr = _coconut_case_match_to_6[3]  #256:     case imdef:
                _coconut_match_temp_155 = _coconut.len(_coconut_case_match_to_6) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_6.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_6, "_coconut_data_defaults", {}) and _coconut_case_match_to_6[i] == _coconut.getattr(_coconut_case_match_to_6, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_6.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_6, "__match_args__") else _coconut.len(_coconut_case_match_to_6) == 4  # type: ignore  #256:     case imdef:
                if _coconut_match_temp_155:  #256:     case imdef:
                    _coconut_case_match_check_6 = True  #256:     case imdef:
            if _coconut_case_match_check_6:  #256:     case imdef:
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #256:     case imdef:
                    dtype = _coconut_match_set_name_dtype  #256:     case imdef:
                if _coconut_match_set_name_vr is not _coconut_sentinel:  #256:     case imdef:
                    vr = _coconut_match_set_name_vr  #256:     case imdef:

        if not _coconut_case_match_check_6:  #256:     case imdef:
            if (not _coconut_match_temp_154) and (_coconut.isinstance(_coconut_case_match_to_6, TensorLike)):  #256:     case imdef:
                _coconut_case_match_check_6 = True  #256:     case imdef:
            if _coconut_case_match_check_6:  #256:     case imdef:
                _coconut_case_match_check_6 = False  #256:     case imdef:
                if not _coconut_case_match_check_6:  #256:     case imdef:
                    if _coconut.type(_coconut_case_match_to_6) in _coconut_self_match_types:  #256:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #256:     case imdef:
                        _coconut_case_match_check_6 = True  #256:     case imdef:

                if not _coconut_case_match_check_6:  #256:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #256:     case imdef:
                    _coconut_match_set_name_vr = _coconut_sentinel  #256:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_6) in _coconut_self_match_types:  #256:     case imdef:
                        _coconut_match_temp_156 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #256:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_156, _coconut.tuple):  #256:     case imdef:
                            raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #256:     case imdef:
                        if _coconut.len(_coconut_match_temp_156) < 4:  #256:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_156),))  #256:     case imdef:
                        _coconut_match_temp_157 = _coconut.getattr(_coconut_case_match_to_6, _coconut_match_temp_156[0], _coconut_sentinel)  #256:     case imdef:
                        _coconut_match_temp_158 = _coconut.getattr(_coconut_case_match_to_6, _coconut_match_temp_156[1], _coconut_sentinel)  #256:     case imdef:
                        _coconut_match_temp_159 = _coconut.getattr(_coconut_case_match_to_6, _coconut_match_temp_156[2], _coconut_sentinel)  #256:     case imdef:
                        _coconut_match_temp_160 = _coconut.getattr(_coconut_case_match_to_6, _coconut_match_temp_156[3], _coconut_sentinel)  #256:     case imdef:
                        if (_coconut_match_temp_157 is not _coconut_sentinel) and (_coconut_match_temp_158 is not _coconut_sentinel) and (_coconut_match_temp_158 == "BHWC") and (_coconut_match_temp_159 is not _coconut_sentinel) and (_coconut_match_temp_159 == "RGBA") and (_coconut_match_temp_160 is not _coconut_sentinel):  #256:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_match_temp_157  #256:     case imdef:
                            _coconut_match_set_name_vr = _coconut_match_temp_160  #256:     case imdef:
                            _coconut_case_match_check_6 = True  #256:     case imdef:
                    if _coconut_case_match_check_6:  #256:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #256:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #256:     case imdef:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #256:     case imdef:
                            vr = _coconut_match_set_name_vr  #256:     case imdef:




    if _coconut_case_match_check_6:  #256:     case imdef:
        return ([DataEdge(a=imdef, b=imdef.__class__(dtype, "BHWC", "RGB", vr), f=lambda a: a[:, :, :, :3], cost=1, name="select rgb channel".format(), meta_shifter=ms_drop_bhwc_alpha),])  #258:             return [DataEdge(a=imdef,
    if not _coconut_case_match_check_6:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
        _coconut_match_temp_161 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
        _coconut_case_match_check_6 = True  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
        if _coconut_case_match_check_6:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
            _coconut_case_match_check_6 = False  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
            if not _coconut_case_match_check_6:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                _coconut_match_set_name_dtype = _coconut_sentinel  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                _coconut_match_set_name_vr = _coconut_sentinel  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                if (_coconut_match_temp_161) and (_coconut.isinstance(_coconut_case_match_to_6, TensorLike)) and (_coconut.len(_coconut_case_match_to_6) >= 4) and (_coconut_case_match_to_6[1] == "BCHW") and (_coconut_case_match_to_6[2] == "RGBA"):  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                    _coconut_match_set_name_dtype = _coconut_case_match_to_6[0]  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                    _coconut_match_set_name_vr = _coconut_case_match_to_6[3]  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                    _coconut_match_temp_162 = _coconut.len(_coconut_case_match_to_6) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_6.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_6, "_coconut_data_defaults", {}) and _coconut_case_match_to_6[i] == _coconut.getattr(_coconut_case_match_to_6, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_6.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_6, "__match_args__") else _coconut.len(_coconut_case_match_to_6) == 4  # type: ignore  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                    if _coconut_match_temp_162:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                        _coconut_case_match_check_6 = True  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                if _coconut_case_match_check_6:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                        dtype = _coconut_match_set_name_dtype  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                    if _coconut_match_set_name_vr is not _coconut_sentinel:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                        vr = _coconut_match_set_name_vr  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):

            if not _coconut_case_match_check_6:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                if (not _coconut_match_temp_161) and (_coconut.isinstance(_coconut_case_match_to_6, TensorLike)):  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                    _coconut_case_match_check_6 = True  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                if _coconut_case_match_check_6:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                    _coconut_case_match_check_6 = False  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                    if not _coconut_case_match_check_6:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                        if _coconut.type(_coconut_case_match_to_6) in _coconut_self_match_types:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            _coconut_case_match_check_6 = True  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):

                    if not _coconut_case_match_check_6:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                        _coconut_match_set_name_dtype = _coconut_sentinel  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                        _coconut_match_set_name_vr = _coconut_sentinel  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                        if not _coconut.type(_coconut_case_match_to_6) in _coconut_self_match_types:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            _coconut_match_temp_163 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            if not _coconut.isinstance(_coconut_match_temp_163, _coconut.tuple):  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                                raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            if _coconut.len(_coconut_match_temp_163) < 4:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_163),))  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            _coconut_match_temp_164 = _coconut.getattr(_coconut_case_match_to_6, _coconut_match_temp_163[0], _coconut_sentinel)  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            _coconut_match_temp_165 = _coconut.getattr(_coconut_case_match_to_6, _coconut_match_temp_163[1], _coconut_sentinel)  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            _coconut_match_temp_166 = _coconut.getattr(_coconut_case_match_to_6, _coconut_match_temp_163[2], _coconut_sentinel)  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            _coconut_match_temp_167 = _coconut.getattr(_coconut_case_match_to_6, _coconut_match_temp_163[3], _coconut_sentinel)  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            if (_coconut_match_temp_164 is not _coconut_sentinel) and (_coconut_match_temp_165 is not _coconut_sentinel) and (_coconut_match_temp_165 == "BCHW") and (_coconut_match_temp_166 is not _coconut_sentinel) and (_coconut_match_temp_166 == "RGBA") and (_coconut_match_temp_167 is not _coconut_sentinel):  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                                _coconut_match_set_name_dtype = _coconut_match_temp_164  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                                _coconut_match_set_name_vr = _coconut_match_temp_167  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                                _coconut_case_match_check_6 = True  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                        if _coconut_case_match_check_6:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                                dtype = _coconut_match_set_name_dtype  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                            if _coconut_match_set_name_vr is not _coconut_sentinel:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
                                vr = _coconut_match_set_name_vr  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):




        if _coconut_case_match_check_6:  #265:         match TensorLike(dtype,"BCHW","RGBA",vr):
            return ([DataEdge(a=imdef, b=imdef.__class__(dtype, "BCHW", "RGB", vr), f=lambda a: a[:, :3], cost=1, name="select rgb channel".format(), meta_shifter=ms_drop_bchw_alpha),])  #266:             return [DataEdge(a=imdef,


ms_select_bhwc_channel = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], s[1], s[2], 1)))  #274: ms_select_bhwc_channel = (s->(s[0],s[1],s[2],1)) |> ss_to_ms$
ms_select_bchw_channel = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], 1, s[2], s[3])))  #275: ms_select_bchw_channel = (s->(s[0],1,s[2],s[3])) |> ss_to_ms$

@to_imagedef  #277: @to_imagedef
def select_channel(imdef: 'ImageDef'):  #278: def select_channel(imdef:ImageDef):
    _coconut_case_match_to_7 = imdef  #279:     case imdef:
    _coconut_case_match_check_7 = False  #279:     case imdef:
    _coconut_match_temp_168 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #279:     case imdef:
    _coconut_case_match_check_7 = True  #279:     case imdef:
    if _coconut_case_match_check_7:  #279:     case imdef:
        _coconut_case_match_check_7 = False  #279:     case imdef:
        if not _coconut_case_match_check_7:  #279:     case imdef:
            _coconut_match_set_name_dtype = _coconut_sentinel  #279:     case imdef:
            _coconut_match_set_name_ch_repr = _coconut_sentinel  #279:     case imdef:
            _coconut_match_set_name_vr = _coconut_sentinel  #279:     case imdef:
            if (_coconut_match_temp_168) and (_coconut.isinstance(_coconut_case_match_to_7, TensorLike)) and (_coconut.len(_coconut_case_match_to_7) >= 4) and (_coconut_case_match_to_7[1] == "BHWC"):  #279:     case imdef:
                _coconut_match_set_name_dtype = _coconut_case_match_to_7[0]  #279:     case imdef:
                _coconut_match_set_name_ch_repr = _coconut_case_match_to_7[2]  #279:     case imdef:
                _coconut_match_set_name_vr = _coconut_case_match_to_7[3]  #279:     case imdef:
                _coconut_match_temp_169 = _coconut.len(_coconut_case_match_to_7) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_7.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_7, "_coconut_data_defaults", {}) and _coconut_case_match_to_7[i] == _coconut.getattr(_coconut_case_match_to_7, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_7.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_7, "__match_args__") else _coconut.len(_coconut_case_match_to_7) == 4  # type: ignore  #279:     case imdef:
                if _coconut_match_temp_169:  #279:     case imdef:
                    _coconut_case_match_check_7 = True  #279:     case imdef:
            if _coconut_case_match_check_7:  #279:     case imdef:
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #279:     case imdef:
                    dtype = _coconut_match_set_name_dtype  #279:     case imdef:
                if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #279:     case imdef:
                    ch_repr = _coconut_match_set_name_ch_repr  #279:     case imdef:
                if _coconut_match_set_name_vr is not _coconut_sentinel:  #279:     case imdef:
                    vr = _coconut_match_set_name_vr  #279:     case imdef:

        if not _coconut_case_match_check_7:  #279:     case imdef:
            if (not _coconut_match_temp_168) and (_coconut.isinstance(_coconut_case_match_to_7, TensorLike)):  #279:     case imdef:
                _coconut_case_match_check_7 = True  #279:     case imdef:
            if _coconut_case_match_check_7:  #279:     case imdef:
                _coconut_case_match_check_7 = False  #279:     case imdef:
                if not _coconut_case_match_check_7:  #279:     case imdef:
                    if _coconut.type(_coconut_case_match_to_7) in _coconut_self_match_types:  #279:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #279:     case imdef:
                        _coconut_case_match_check_7 = True  #279:     case imdef:

                if not _coconut_case_match_check_7:  #279:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #279:     case imdef:
                    _coconut_match_set_name_ch_repr = _coconut_sentinel  #279:     case imdef:
                    _coconut_match_set_name_vr = _coconut_sentinel  #279:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_7) in _coconut_self_match_types:  #279:     case imdef:
                        _coconut_match_temp_170 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #279:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_170, _coconut.tuple):  #279:     case imdef:
                            raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #279:     case imdef:
                        if _coconut.len(_coconut_match_temp_170) < 4:  #279:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_170),))  #279:     case imdef:
                        _coconut_match_temp_171 = _coconut.getattr(_coconut_case_match_to_7, _coconut_match_temp_170[0], _coconut_sentinel)  #279:     case imdef:
                        _coconut_match_temp_172 = _coconut.getattr(_coconut_case_match_to_7, _coconut_match_temp_170[1], _coconut_sentinel)  #279:     case imdef:
                        _coconut_match_temp_173 = _coconut.getattr(_coconut_case_match_to_7, _coconut_match_temp_170[2], _coconut_sentinel)  #279:     case imdef:
                        _coconut_match_temp_174 = _coconut.getattr(_coconut_case_match_to_7, _coconut_match_temp_170[3], _coconut_sentinel)  #279:     case imdef:
                        if (_coconut_match_temp_171 is not _coconut_sentinel) and (_coconut_match_temp_172 is not _coconut_sentinel) and (_coconut_match_temp_172 == "BHWC") and (_coconut_match_temp_173 is not _coconut_sentinel) and (_coconut_match_temp_174 is not _coconut_sentinel):  #279:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_match_temp_171  #279:     case imdef:
                            _coconut_match_set_name_ch_repr = _coconut_match_temp_173  #279:     case imdef:
                            _coconut_match_set_name_vr = _coconut_match_temp_174  #279:     case imdef:
                            _coconut_case_match_check_7 = True  #279:     case imdef:
                    if _coconut_case_match_check_7:  #279:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #279:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #279:     case imdef:
                        if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #279:     case imdef:
                            ch_repr = _coconut_match_set_name_ch_repr  #279:     case imdef:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #279:     case imdef:
                            vr = _coconut_match_set_name_vr  #279:     case imdef:




    if _coconut_case_match_check_7 and not (len(ch_repr) >= 1):  #279:     case imdef:
        _coconut_case_match_check_7 = False  #279:     case imdef:
    if _coconut_case_match_check_7:  #279:     case imdef:
        selector = lambda i: lambda a: a[:, :, :, [i,]]  #281:             selector = i->a->a[:,:,:,[i]]
        return ([DataEdge(a=imdef, b=imdef.__class__(dtype, "BHWC", c, vr), f=selector(i), cost=10, name="select {_coconut_format_0} channel".format(_coconut_format_0=(c)), meta_shifter=ms_select_bhwc_channel) for i, c in enumerate(ch_splitter(ch_repr))])  #282:             return [DataEdge(a=imdef,
    if not _coconut_case_match_check_7:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
        _coconut_match_temp_175 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
        _coconut_case_match_check_7 = True  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
        if _coconut_case_match_check_7:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
            _coconut_case_match_check_7 = False  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
            if not _coconut_case_match_check_7:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                _coconut_match_set_name_dtype = _coconut_sentinel  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                _coconut_match_set_name_ch_repr = _coconut_sentinel  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                _coconut_match_set_name_vr = _coconut_sentinel  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                if (_coconut_match_temp_175) and (_coconut.isinstance(_coconut_case_match_to_7, TensorLike)) and (_coconut.len(_coconut_case_match_to_7) >= 4) and (_coconut_case_match_to_7[1] == "BCHW"):  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                    _coconut_match_set_name_dtype = _coconut_case_match_to_7[0]  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_7[2]  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                    _coconut_match_set_name_vr = _coconut_case_match_to_7[3]  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                    _coconut_match_temp_176 = _coconut.len(_coconut_case_match_to_7) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_7.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_7, "_coconut_data_defaults", {}) and _coconut_case_match_to_7[i] == _coconut.getattr(_coconut_case_match_to_7, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_7.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_7, "__match_args__") else _coconut.len(_coconut_case_match_to_7) == 4  # type: ignore  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                    if _coconut_match_temp_176:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                        _coconut_case_match_check_7 = True  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                if _coconut_case_match_check_7:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                        dtype = _coconut_match_set_name_dtype  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                        ch_repr = _coconut_match_set_name_ch_repr  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                    if _coconut_match_set_name_vr is not _coconut_sentinel:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                        vr = _coconut_match_set_name_vr  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:

            if not _coconut_case_match_check_7:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                if (not _coconut_match_temp_175) and (_coconut.isinstance(_coconut_case_match_to_7, TensorLike)):  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                    _coconut_case_match_check_7 = True  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                if _coconut_case_match_check_7:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                    _coconut_case_match_check_7 = False  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                    if not _coconut_case_match_check_7:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                        if _coconut.type(_coconut_case_match_to_7) in _coconut_self_match_types:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            _coconut_case_match_check_7 = True  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:

                    if not _coconut_case_match_check_7:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                        _coconut_match_set_name_dtype = _coconut_sentinel  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                        _coconut_match_set_name_vr = _coconut_sentinel  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                        if not _coconut.type(_coconut_case_match_to_7) in _coconut_self_match_types:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            _coconut_match_temp_177 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            if not _coconut.isinstance(_coconut_match_temp_177, _coconut.tuple):  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                                raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            if _coconut.len(_coconut_match_temp_177) < 4:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_177),))  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            _coconut_match_temp_178 = _coconut.getattr(_coconut_case_match_to_7, _coconut_match_temp_177[0], _coconut_sentinel)  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            _coconut_match_temp_179 = _coconut.getattr(_coconut_case_match_to_7, _coconut_match_temp_177[1], _coconut_sentinel)  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            _coconut_match_temp_180 = _coconut.getattr(_coconut_case_match_to_7, _coconut_match_temp_177[2], _coconut_sentinel)  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            _coconut_match_temp_181 = _coconut.getattr(_coconut_case_match_to_7, _coconut_match_temp_177[3], _coconut_sentinel)  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            if (_coconut_match_temp_178 is not _coconut_sentinel) and (_coconut_match_temp_179 is not _coconut_sentinel) and (_coconut_match_temp_179 == "BCHW") and (_coconut_match_temp_180 is not _coconut_sentinel) and (_coconut_match_temp_181 is not _coconut_sentinel):  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                                _coconut_match_set_name_dtype = _coconut_match_temp_178  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_180  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                                _coconut_match_set_name_vr = _coconut_match_temp_181  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                                _coconut_case_match_check_7 = True  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                        if _coconut_case_match_check_7:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                                dtype = _coconut_match_set_name_dtype  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                                ch_repr = _coconut_match_set_name_ch_repr  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                            if _coconut_match_set_name_vr is not _coconut_sentinel:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
                                vr = _coconut_match_set_name_vr  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:




        if _coconut_case_match_check_7 and not (len(ch_repr) >= 1):  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
            _coconut_case_match_check_7 = False  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
        if _coconut_case_match_check_7:  #289:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_repr) >= 1:
            selector = lambda i: lambda a: a[:, [i,]]  #290:             selector = i->a->a[:,[i]]
            return ([DataEdge(a=imdef, b=imdef.__class__(dtype, "BCHW", c, vr), f=selector(i), cost=10, name="select {_coconut_format_0} channel".format(_coconut_format_0=(c)), meta_shifter=ms_select_bchw_channel) for i, c in enumerate(ch_splitter(ch_repr))])  #291:             return [DataEdge(a=imdef,
    return ([])  #298:     return []

ms_drop_bhwc_channel = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], s[1], s[2])))  #299: ms_drop_bhwc_channel = (s->(s[0],s[1],s[2])) |> ss_to_ms$
ms_drop_bchw_channel = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], s[2], s[3])))  #300: ms_drop_bchw_channel = (s->(s[0],s[2],s[3])) |> ss_to_ms$
ms_drop_chw_channel = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[1], s[2])))  #301: ms_drop_chw_channel = (s->(s[1],s[2])) |> ss_to_ms$
ms_drop_hwc_channel = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], s[1])))  #302: ms_drop_hwc_channel = (s->(s[0],s[1])) |> ss_to_ms$


@to_imagedef  #305: @to_imagedef
def drop_channel(imdef: 'ImageDef'):  #306: def drop_channel(imdef:ImageDef):
    _coconut_case_match_to_8 = imdef  #307:     case imdef:
    _coconut_case_match_check_8 = False  #307:     case imdef:
    _coconut_match_temp_182 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #307:     case imdef:
    _coconut_case_match_check_8 = True  #307:     case imdef:
    if _coconut_case_match_check_8:  #307:     case imdef:
        _coconut_case_match_check_8 = False  #307:     case imdef:
        if not _coconut_case_match_check_8:  #307:     case imdef:
            _coconut_match_set_name_dtype = _coconut_sentinel  #307:     case imdef:
            _coconut_match_set_name_ch_repr = _coconut_sentinel  #307:     case imdef:
            _coconut_match_set_name_vr = _coconut_sentinel  #307:     case imdef:
            if (_coconut_match_temp_182) and (_coconut.isinstance(_coconut_case_match_to_8, TensorLike)) and (_coconut.len(_coconut_case_match_to_8) >= 4) and (_coconut_case_match_to_8[1] == "BHWC"):  #307:     case imdef:
                _coconut_match_set_name_dtype = _coconut_case_match_to_8[0]  #307:     case imdef:
                _coconut_match_set_name_ch_repr = _coconut_case_match_to_8[2]  #307:     case imdef:
                _coconut_match_set_name_vr = _coconut_case_match_to_8[3]  #307:     case imdef:
                _coconut_match_temp_183 = _coconut.len(_coconut_case_match_to_8) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_8.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_8, "_coconut_data_defaults", {}) and _coconut_case_match_to_8[i] == _coconut.getattr(_coconut_case_match_to_8, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_8.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_8, "__match_args__") else _coconut.len(_coconut_case_match_to_8) == 4  # type: ignore  #307:     case imdef:
                if _coconut_match_temp_183:  #307:     case imdef:
                    _coconut_case_match_check_8 = True  #307:     case imdef:
            if _coconut_case_match_check_8:  #307:     case imdef:
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #307:     case imdef:
                    dtype = _coconut_match_set_name_dtype  #307:     case imdef:
                if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #307:     case imdef:
                    ch_repr = _coconut_match_set_name_ch_repr  #307:     case imdef:
                if _coconut_match_set_name_vr is not _coconut_sentinel:  #307:     case imdef:
                    vr = _coconut_match_set_name_vr  #307:     case imdef:

        if not _coconut_case_match_check_8:  #307:     case imdef:
            if (not _coconut_match_temp_182) and (_coconut.isinstance(_coconut_case_match_to_8, TensorLike)):  #307:     case imdef:
                _coconut_case_match_check_8 = True  #307:     case imdef:
            if _coconut_case_match_check_8:  #307:     case imdef:
                _coconut_case_match_check_8 = False  #307:     case imdef:
                if not _coconut_case_match_check_8:  #307:     case imdef:
                    if _coconut.type(_coconut_case_match_to_8) in _coconut_self_match_types:  #307:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #307:     case imdef:
                        _coconut_case_match_check_8 = True  #307:     case imdef:

                if not _coconut_case_match_check_8:  #307:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #307:     case imdef:
                    _coconut_match_set_name_ch_repr = _coconut_sentinel  #307:     case imdef:
                    _coconut_match_set_name_vr = _coconut_sentinel  #307:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_8) in _coconut_self_match_types:  #307:     case imdef:
                        _coconut_match_temp_184 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #307:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_184, _coconut.tuple):  #307:     case imdef:
                            raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #307:     case imdef:
                        if _coconut.len(_coconut_match_temp_184) < 4:  #307:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_184),))  #307:     case imdef:
                        _coconut_match_temp_185 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_184[0], _coconut_sentinel)  #307:     case imdef:
                        _coconut_match_temp_186 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_184[1], _coconut_sentinel)  #307:     case imdef:
                        _coconut_match_temp_187 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_184[2], _coconut_sentinel)  #307:     case imdef:
                        _coconut_match_temp_188 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_184[3], _coconut_sentinel)  #307:     case imdef:
                        if (_coconut_match_temp_185 is not _coconut_sentinel) and (_coconut_match_temp_186 is not _coconut_sentinel) and (_coconut_match_temp_186 == "BHWC") and (_coconut_match_temp_187 is not _coconut_sentinel) and (_coconut_match_temp_188 is not _coconut_sentinel):  #307:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_match_temp_185  #307:     case imdef:
                            _coconut_match_set_name_ch_repr = _coconut_match_temp_187  #307:     case imdef:
                            _coconut_match_set_name_vr = _coconut_match_temp_188  #307:     case imdef:
                            _coconut_case_match_check_8 = True  #307:     case imdef:
                    if _coconut_case_match_check_8:  #307:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #307:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #307:     case imdef:
                        if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #307:     case imdef:
                            ch_repr = _coconut_match_set_name_ch_repr  #307:     case imdef:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #307:     case imdef:
                            vr = _coconut_match_set_name_vr  #307:     case imdef:




    if _coconut_case_match_check_8 and not (len(ch_splitter(ch_repr)) == 1):  #307:     case imdef:
        _coconut_case_match_check_8 = False  #307:     case imdef:
    if _coconut_case_match_check_8:  #307:     case imdef:
        return ([DataEdge(a=imdef, b=imdef.__class__(dtype, "BHW", ch_repr, vr), f=lambda a: a[:, :, :, 0], cost=1, name="BHWC to BHW".format(), meta_shifter=ms_drop_bhwc_channel),])  #309:             return [DataEdge(a=imdef,
    if not _coconut_case_match_check_8:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        _coconut_match_temp_189 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        _coconut_case_match_check_8 = True  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        if _coconut_case_match_check_8:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            _coconut_case_match_check_8 = False  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            if not _coconut_case_match_check_8:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                _coconut_match_set_name_dtype = _coconut_sentinel  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                _coconut_match_set_name_ch_repr = _coconut_sentinel  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                _coconut_match_set_name_vr = _coconut_sentinel  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if (_coconut_match_temp_189) and (_coconut.isinstance(_coconut_case_match_to_8, TensorLike)) and (_coconut.len(_coconut_case_match_to_8) >= 4) and (_coconut_case_match_to_8[1] == "BCHW"):  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_set_name_dtype = _coconut_case_match_to_8[0]  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_8[2]  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_set_name_vr = _coconut_case_match_to_8[3]  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_temp_190 = _coconut.len(_coconut_case_match_to_8) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_8.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_8, "_coconut_data_defaults", {}) and _coconut_case_match_to_8[i] == _coconut.getattr(_coconut_case_match_to_8, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_8.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_8, "__match_args__") else _coconut.len(_coconut_case_match_to_8) == 4  # type: ignore  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_temp_190:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_case_match_check_8 = True  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if _coconut_case_match_check_8:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        dtype = _coconut_match_set_name_dtype  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        ch_repr = _coconut_match_set_name_ch_repr  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_set_name_vr is not _coconut_sentinel:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        vr = _coconut_match_set_name_vr  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:

            if not _coconut_case_match_check_8:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if (not _coconut_match_temp_189) and (_coconut.isinstance(_coconut_case_match_to_8, TensorLike)):  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_case_match_check_8 = True  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if _coconut_case_match_check_8:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_case_match_check_8 = False  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if not _coconut_case_match_check_8:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        if _coconut.type(_coconut_case_match_to_8) in _coconut_self_match_types:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_case_match_check_8 = True  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:

                    if not _coconut_case_match_check_8:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_match_set_name_dtype = _coconut_sentinel  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_match_set_name_vr = _coconut_sentinel  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        if not _coconut.type(_coconut_case_match_to_8) in _coconut_self_match_types:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_191 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if not _coconut.isinstance(_coconut_match_temp_191, _coconut.tuple):  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut.len(_coconut_match_temp_191) < 4:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_191),))  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_192 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_191[0], _coconut_sentinel)  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_193 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_191[1], _coconut_sentinel)  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_194 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_191[2], _coconut_sentinel)  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_195 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_191[3], _coconut_sentinel)  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if (_coconut_match_temp_192 is not _coconut_sentinel) and (_coconut_match_temp_193 is not _coconut_sentinel) and (_coconut_match_temp_193 == "BCHW") and (_coconut_match_temp_194 is not _coconut_sentinel) and (_coconut_match_temp_195 is not _coconut_sentinel):  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_match_set_name_dtype = _coconut_match_temp_192  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_194  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_match_set_name_vr = _coconut_match_temp_195  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_case_match_check_8 = True  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        if _coconut_case_match_check_8:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                dtype = _coconut_match_set_name_dtype  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                ch_repr = _coconut_match_set_name_ch_repr  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut_match_set_name_vr is not _coconut_sentinel:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                vr = _coconut_match_set_name_vr  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:




        if _coconut_case_match_check_8 and not (len(ch_splitter(ch_repr)) == 1):  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            _coconut_case_match_check_8 = False  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        if _coconut_case_match_check_8:  #316:         match TensorLike(dtype,"BCHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            return ([DataEdge(a=imdef, b=imdef.__class__(dtype, "BHW", ch_repr, vr), f=lambda a: a[:, 0], cost=1, name="BCHW to BHW".format(), meta_shifter=ms_drop_bchw_channel),])  #317:             return [DataEdge(a=imdef,
    if not _coconut_case_match_check_8:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        _coconut_match_temp_196 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        _coconut_case_match_check_8 = True  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        if _coconut_case_match_check_8:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            _coconut_case_match_check_8 = False  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            if not _coconut_case_match_check_8:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                _coconut_match_set_name_dtype = _coconut_sentinel  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                _coconut_match_set_name_ch_repr = _coconut_sentinel  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                _coconut_match_set_name_vr = _coconut_sentinel  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if (_coconut_match_temp_196) and (_coconut.isinstance(_coconut_case_match_to_8, TensorLike)) and (_coconut.len(_coconut_case_match_to_8) >= 4) and (_coconut_case_match_to_8[1] == "CHW"):  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_set_name_dtype = _coconut_case_match_to_8[0]  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_8[2]  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_set_name_vr = _coconut_case_match_to_8[3]  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_temp_197 = _coconut.len(_coconut_case_match_to_8) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_8.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_8, "_coconut_data_defaults", {}) and _coconut_case_match_to_8[i] == _coconut.getattr(_coconut_case_match_to_8, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_8.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_8, "__match_args__") else _coconut.len(_coconut_case_match_to_8) == 4  # type: ignore  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_temp_197:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_case_match_check_8 = True  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if _coconut_case_match_check_8:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        dtype = _coconut_match_set_name_dtype  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        ch_repr = _coconut_match_set_name_ch_repr  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_set_name_vr is not _coconut_sentinel:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        vr = _coconut_match_set_name_vr  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:

            if not _coconut_case_match_check_8:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if (not _coconut_match_temp_196) and (_coconut.isinstance(_coconut_case_match_to_8, TensorLike)):  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_case_match_check_8 = True  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if _coconut_case_match_check_8:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_case_match_check_8 = False  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if not _coconut_case_match_check_8:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        if _coconut.type(_coconut_case_match_to_8) in _coconut_self_match_types:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_case_match_check_8 = True  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:

                    if not _coconut_case_match_check_8:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_match_set_name_dtype = _coconut_sentinel  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_match_set_name_vr = _coconut_sentinel  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        if not _coconut.type(_coconut_case_match_to_8) in _coconut_self_match_types:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_198 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if not _coconut.isinstance(_coconut_match_temp_198, _coconut.tuple):  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut.len(_coconut_match_temp_198) < 4:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_198),))  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_199 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_198[0], _coconut_sentinel)  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_200 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_198[1], _coconut_sentinel)  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_201 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_198[2], _coconut_sentinel)  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_202 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_198[3], _coconut_sentinel)  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if (_coconut_match_temp_199 is not _coconut_sentinel) and (_coconut_match_temp_200 is not _coconut_sentinel) and (_coconut_match_temp_200 == "CHW") and (_coconut_match_temp_201 is not _coconut_sentinel) and (_coconut_match_temp_202 is not _coconut_sentinel):  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_match_set_name_dtype = _coconut_match_temp_199  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_201  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_match_set_name_vr = _coconut_match_temp_202  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_case_match_check_8 = True  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        if _coconut_case_match_check_8:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                dtype = _coconut_match_set_name_dtype  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                ch_repr = _coconut_match_set_name_ch_repr  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut_match_set_name_vr is not _coconut_sentinel:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                vr = _coconut_match_set_name_vr  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:




        if _coconut_case_match_check_8 and not (len(ch_splitter(ch_repr)) == 1):  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            _coconut_case_match_check_8 = False  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        if _coconut_case_match_check_8:  #324:         match TensorLike(dtype,"CHW",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            return ([DataEdge(a=imdef, b=imdef.__class__(dtype, "HW", ch_repr, vr), f=lambda a: a[0], cost=1, name="CHW to HW", meta_shifter=ms_drop_chw_channel),])  #325:             return [DataEdge(a = imdef,b=imdef.__class__(dtype,"HW",ch_repr,vr),
    if not _coconut_case_match_check_8:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        _coconut_match_temp_203 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        _coconut_case_match_check_8 = True  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        if _coconut_case_match_check_8:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            _coconut_case_match_check_8 = False  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            if not _coconut_case_match_check_8:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                _coconut_match_set_name_dtype = _coconut_sentinel  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                _coconut_match_set_name_ch_repr = _coconut_sentinel  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                _coconut_match_set_name_vr = _coconut_sentinel  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if (_coconut_match_temp_203) and (_coconut.isinstance(_coconut_case_match_to_8, TensorLike)) and (_coconut.len(_coconut_case_match_to_8) >= 4) and (_coconut_case_match_to_8[1] == "HWC"):  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_set_name_dtype = _coconut_case_match_to_8[0]  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_8[2]  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_set_name_vr = _coconut_case_match_to_8[3]  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_match_temp_204 = _coconut.len(_coconut_case_match_to_8) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_8.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_8, "_coconut_data_defaults", {}) and _coconut_case_match_to_8[i] == _coconut.getattr(_coconut_case_match_to_8, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_8.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_8, "__match_args__") else _coconut.len(_coconut_case_match_to_8) == 4  # type: ignore  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_temp_204:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_case_match_check_8 = True  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if _coconut_case_match_check_8:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        dtype = _coconut_match_set_name_dtype  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        ch_repr = _coconut_match_set_name_ch_repr  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if _coconut_match_set_name_vr is not _coconut_sentinel:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        vr = _coconut_match_set_name_vr  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:

            if not _coconut_case_match_check_8:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if (not _coconut_match_temp_203) and (_coconut.isinstance(_coconut_case_match_to_8, TensorLike)):  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_case_match_check_8 = True  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                if _coconut_case_match_check_8:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    _coconut_case_match_check_8 = False  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                    if not _coconut_case_match_check_8:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        if _coconut.type(_coconut_case_match_to_8) in _coconut_self_match_types:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_case_match_check_8 = True  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:

                    if not _coconut_case_match_check_8:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_match_set_name_dtype = _coconut_sentinel  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        _coconut_match_set_name_vr = _coconut_sentinel  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        if not _coconut.type(_coconut_case_match_to_8) in _coconut_self_match_types:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_205 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if not _coconut.isinstance(_coconut_match_temp_205, _coconut.tuple):  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut.len(_coconut_match_temp_205) < 4:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_205),))  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_206 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_205[0], _coconut_sentinel)  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_207 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_205[1], _coconut_sentinel)  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_208 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_205[2], _coconut_sentinel)  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            _coconut_match_temp_209 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_205[3], _coconut_sentinel)  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if (_coconut_match_temp_206 is not _coconut_sentinel) and (_coconut_match_temp_207 is not _coconut_sentinel) and (_coconut_match_temp_207 == "HWC") and (_coconut_match_temp_208 is not _coconut_sentinel) and (_coconut_match_temp_209 is not _coconut_sentinel):  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_match_set_name_dtype = _coconut_match_temp_206  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_208  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_match_set_name_vr = _coconut_match_temp_209  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                _coconut_case_match_check_8 = True  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                        if _coconut_case_match_check_8:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                dtype = _coconut_match_set_name_dtype  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                ch_repr = _coconut_match_set_name_ch_repr  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                            if _coconut_match_set_name_vr is not _coconut_sentinel:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
                                vr = _coconut_match_set_name_vr  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:




        if _coconut_case_match_check_8 and not (len(ch_splitter(ch_repr)) == 1):  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            _coconut_case_match_check_8 = False  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
        if _coconut_case_match_check_8:  #329:         match TensorLike(dtype,"HWC",ch_repr,vr) if len(ch_splitter(ch_repr)) == 1:
            return ([DataEdge(a=imdef, b=imdef.__class__(dtype, "HW", ch_repr, vr), f=lambda a: a[:, :, 0], cost=1, name="HWC to HW", meta_shifter=ms_drop_hwc_channel),])  #330:             return [DataEdge(a = imdef,b=imdef.__class__(dtype,"HW",ch_repr,vr),

    return ([])  #335:     return []

def enforce_mode(img, mode):  #336: def enforce_mode(img,mode):
    return (Image.fromarray(np.array(img), mode))  #337:     return Image.fromarray(np.array(img),mode)

"""
@to_imagedef
def RGB_to_YCbCr(state):
    case state:
        match PILImage("RGB","RGB"):
            return [DataEdge(
            a=state,
            b=PILImage("YCbCr","YCbCr"),
            f= enforce_mode$(mode="RGB") ..> .convert("YCbCr"),
            cost=1,
            name="RGB to YCbCr"
            )]
        match PILImage("YCbCr","YCbCr"):
            return [DataEdge(
            a=state,
            b=PILImage("RGB","RGB"),
            f= enforce_mode$(mode="YCbCr") ..> .convert("RGB"),
            cost=1,
            name="YCbCr to RGB"
            )]
"""  #358: """



@to_imagedef  #362: @to_imagedef
def RGB_to_YCbCr(state):  #363: def RGB_to_YCbCr(state):
    _coconut_case_match_to_9 = state  #364:     case state:
    _coconut_case_match_check_9 = False  #364:     case state:
    _coconut_match_temp_210 = _coconut.getattr(Torch, "_coconut_is_data", False) or _coconut.isinstance(Torch, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Torch)  # type: ignore  #364:     case state:
    _coconut_case_match_check_9 = True  #364:     case state:
    if _coconut_case_match_check_9:  #364:     case state:
        _coconut_case_match_check_9 = False  #364:     case state:
        if not _coconut_case_match_check_9:  #364:     case state:
            if (_coconut_match_temp_210) and (_coconut.isinstance(_coconut_case_match_to_9, Torch)) and (_coconut.len(_coconut_case_match_to_9) >= 4) and (_coconut_case_match_to_9[0] == "float32") and (_coconut_case_match_to_9[1] == "BCHW") and (_coconut_case_match_to_9[2] == "RGB") and (_coconut_case_match_to_9[3] == VR_0_1):  #364:     case state:
                _coconut_match_temp_211 = _coconut.len(_coconut_case_match_to_9) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_9.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_9, "_coconut_data_defaults", {}) and _coconut_case_match_to_9[i] == _coconut.getattr(_coconut_case_match_to_9, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_9.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_9, "__match_args__") else _coconut.len(_coconut_case_match_to_9) == 4  # type: ignore  #364:     case state:
                if _coconut_match_temp_211:  #364:     case state:
                    _coconut_case_match_check_9 = True  #364:     case state:

        if not _coconut_case_match_check_9:  #364:     case state:
            if (not _coconut_match_temp_210) and (_coconut.isinstance(_coconut_case_match_to_9, Torch)):  #364:     case state:
                _coconut_case_match_check_9 = True  #364:     case state:
            if _coconut_case_match_check_9:  #364:     case state:
                _coconut_case_match_check_9 = False  #364:     case state:
                if not _coconut_case_match_check_9:  #364:     case state:
                    if _coconut.type(_coconut_case_match_to_9) in _coconut_self_match_types:  #364:     case state:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports 1)")  #364:     case state:
                        _coconut_case_match_check_9 = True  #364:     case state:

                if not _coconut_case_match_check_9:  #364:     case state:
                    if not _coconut.type(_coconut_case_match_to_9) in _coconut_self_match_types:  #364:     case state:
                        _coconut_match_temp_212 = _coconut.getattr(Torch, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #364:     case state:
                        if not _coconut.isinstance(_coconut_match_temp_212, _coconut.tuple):  #364:     case state:
                            raise _coconut.TypeError("Torch.__match_args__ must be a tuple")  #364:     case state:
                        if _coconut.len(_coconut_match_temp_212) < 4:  #364:     case state:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports %s)" % (_coconut.len(_coconut_match_temp_212),))  #364:     case state:
                        _coconut_match_temp_213 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_212[0], _coconut_sentinel)  #364:     case state:
                        _coconut_match_temp_214 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_212[1], _coconut_sentinel)  #364:     case state:
                        _coconut_match_temp_215 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_212[2], _coconut_sentinel)  #364:     case state:
                        _coconut_match_temp_216 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_212[3], _coconut_sentinel)  #364:     case state:
                        if (_coconut_match_temp_213 is not _coconut_sentinel) and (_coconut_match_temp_213 == "float32") and (_coconut_match_temp_214 is not _coconut_sentinel) and (_coconut_match_temp_214 == "BCHW") and (_coconut_match_temp_215 is not _coconut_sentinel) and (_coconut_match_temp_215 == "RGB") and (_coconut_match_temp_216 is not _coconut_sentinel) and (_coconut_match_temp_216 == VR_0_1):  #364:     case state:
                            _coconut_case_match_check_9 = True  #364:     case state:




    if _coconut_case_match_check_9:  #364:     case state:
        return ([DataEdge(a=state, b=Torch("float32", "BCHW", "RGB", VR_0_1), f=rgb_to_ycbcr, cost=1, name="RGB_to_YCbCr(torch)"),])  #366:             return [DataEdge(a=state,
    if not _coconut_case_match_check_9:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
        _coconut_match_temp_217 = _coconut.getattr(Torch, "_coconut_is_data", False) or _coconut.isinstance(Torch, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Torch)  # type: ignore  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
        _coconut_case_match_check_9 = True  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
        if _coconut_case_match_check_9:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
            _coconut_case_match_check_9 = False  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
            if not _coconut_case_match_check_9:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                if (_coconut_match_temp_217) and (_coconut.isinstance(_coconut_case_match_to_9, Torch)) and (_coconut.len(_coconut_case_match_to_9) >= 4) and (_coconut_case_match_to_9[0] == "float32") and (_coconut_case_match_to_9[1] == "BCHW") and (_coconut_case_match_to_9[2] == "YCbCr") and (_coconut_case_match_to_9[3] == VR_0_1):  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                    _coconut_match_temp_218 = _coconut.len(_coconut_case_match_to_9) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_9.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_9, "_coconut_data_defaults", {}) and _coconut_case_match_to_9[i] == _coconut.getattr(_coconut_case_match_to_9, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_9.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_9, "__match_args__") else _coconut.len(_coconut_case_match_to_9) == 4  # type: ignore  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                    if _coconut_match_temp_218:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                        _coconut_case_match_check_9 = True  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):

            if not _coconut_case_match_check_9:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                if (not _coconut_match_temp_217) and (_coconut.isinstance(_coconut_case_match_to_9, Torch)):  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                    _coconut_case_match_check_9 = True  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                if _coconut_case_match_check_9:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                    _coconut_case_match_check_9 = False  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                    if not _coconut_case_match_check_9:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                        if _coconut.type(_coconut_case_match_to_9) in _coconut_self_match_types:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports 1)")  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                            _coconut_case_match_check_9 = True  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):

                    if not _coconut_case_match_check_9:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                        if not _coconut.type(_coconut_case_match_to_9) in _coconut_self_match_types:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                            _coconut_match_temp_219 = _coconut.getattr(Torch, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                            if not _coconut.isinstance(_coconut_match_temp_219, _coconut.tuple):  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                                raise _coconut.TypeError("Torch.__match_args__ must be a tuple")  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                            if _coconut.len(_coconut_match_temp_219) < 4:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports %s)" % (_coconut.len(_coconut_match_temp_219),))  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                            _coconut_match_temp_220 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_219[0], _coconut_sentinel)  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                            _coconut_match_temp_221 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_219[1], _coconut_sentinel)  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                            _coconut_match_temp_222 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_219[2], _coconut_sentinel)  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                            _coconut_match_temp_223 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_219[3], _coconut_sentinel)  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                            if (_coconut_match_temp_220 is not _coconut_sentinel) and (_coconut_match_temp_220 == "float32") and (_coconut_match_temp_221 is not _coconut_sentinel) and (_coconut_match_temp_221 == "BCHW") and (_coconut_match_temp_222 is not _coconut_sentinel) and (_coconut_match_temp_222 == "YCbCr") and (_coconut_match_temp_223 is not _coconut_sentinel) and (_coconut_match_temp_223 == VR_0_1):  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
                                _coconut_case_match_check_9 = True  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):




        if _coconut_case_match_check_9:  #372:         match Torch("float32","BCHW","YCbCr",==VR_0_1):
            return ([DataEdge(a=state, b=Torch("float32", "BCHW", "RGB", VR_0_1), f=ycbcr_to_rgb, cost=1, name="YCbCr_to_RGB(torch)"),])  #373:             return [DataEdge(a=state,
    if not _coconut_case_match_check_9:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
        _coconut_match_temp_224 = _coconut.getattr(Torch, "_coconut_is_data", False) or _coconut.isinstance(Torch, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Torch)  # type: ignore  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
        _coconut_case_match_check_9 = True  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
        if _coconut_case_match_check_9:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
            _coconut_case_match_check_9 = False  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
            if not _coconut_case_match_check_9:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                if (_coconut_match_temp_224) and (_coconut.isinstance(_coconut_case_match_to_9, Torch)) and (_coconut.len(_coconut_case_match_to_9) >= 4) and (_coconut_case_match_to_9[0] == "float32") and (_coconut_case_match_to_9[1] == "CHW") and (_coconut_case_match_to_9[2] == "RGB") and (_coconut_case_match_to_9[3] == VR_0_1):  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                    _coconut_match_temp_225 = _coconut.len(_coconut_case_match_to_9) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_9.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_9, "_coconut_data_defaults", {}) and _coconut_case_match_to_9[i] == _coconut.getattr(_coconut_case_match_to_9, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_9.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_9, "__match_args__") else _coconut.len(_coconut_case_match_to_9) == 4  # type: ignore  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                    if _coconut_match_temp_225:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                        _coconut_case_match_check_9 = True  #379:         match Torch("float32","CHW","RGB",==VR_0_1):

            if not _coconut_case_match_check_9:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                if (not _coconut_match_temp_224) and (_coconut.isinstance(_coconut_case_match_to_9, Torch)):  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                    _coconut_case_match_check_9 = True  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                if _coconut_case_match_check_9:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                    _coconut_case_match_check_9 = False  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                    if not _coconut_case_match_check_9:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                        if _coconut.type(_coconut_case_match_to_9) in _coconut_self_match_types:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports 1)")  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                            _coconut_case_match_check_9 = True  #379:         match Torch("float32","CHW","RGB",==VR_0_1):

                    if not _coconut_case_match_check_9:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                        if not _coconut.type(_coconut_case_match_to_9) in _coconut_self_match_types:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                            _coconut_match_temp_226 = _coconut.getattr(Torch, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                            if not _coconut.isinstance(_coconut_match_temp_226, _coconut.tuple):  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                                raise _coconut.TypeError("Torch.__match_args__ must be a tuple")  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                            if _coconut.len(_coconut_match_temp_226) < 4:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports %s)" % (_coconut.len(_coconut_match_temp_226),))  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                            _coconut_match_temp_227 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_226[0], _coconut_sentinel)  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                            _coconut_match_temp_228 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_226[1], _coconut_sentinel)  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                            _coconut_match_temp_229 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_226[2], _coconut_sentinel)  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                            _coconut_match_temp_230 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_226[3], _coconut_sentinel)  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                            if (_coconut_match_temp_227 is not _coconut_sentinel) and (_coconut_match_temp_227 == "float32") and (_coconut_match_temp_228 is not _coconut_sentinel) and (_coconut_match_temp_228 == "CHW") and (_coconut_match_temp_229 is not _coconut_sentinel) and (_coconut_match_temp_229 == "RGB") and (_coconut_match_temp_230 is not _coconut_sentinel) and (_coconut_match_temp_230 == VR_0_1):  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
                                _coconut_case_match_check_9 = True  #379:         match Torch("float32","CHW","RGB",==VR_0_1):




        if _coconut_case_match_check_9:  #379:         match Torch("float32","CHW","RGB",==VR_0_1):
            return ([DataEdge(a=state, b=Torch("float32", "CHW", "YCbCr", VR_0_1), f=rgb_to_ycbcr, cost=1, name="RGB_to_YCbCr(torch)"),])  #380:             return [DataEdge(a=state,
    if not _coconut_case_match_check_9:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
        _coconut_match_temp_231 = _coconut.getattr(Torch, "_coconut_is_data", False) or _coconut.isinstance(Torch, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Torch)  # type: ignore  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
        _coconut_case_match_check_9 = True  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
        if _coconut_case_match_check_9:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
            _coconut_case_match_check_9 = False  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
            if not _coconut_case_match_check_9:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                if (_coconut_match_temp_231) and (_coconut.isinstance(_coconut_case_match_to_9, Torch)) and (_coconut.len(_coconut_case_match_to_9) >= 4) and (_coconut_case_match_to_9[0] == "float32") and (_coconut_case_match_to_9[1] == "CHW") and (_coconut_case_match_to_9[2] == "YCbCr") and (_coconut_case_match_to_9[3] == VR_0_1):  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                    _coconut_match_temp_232 = _coconut.len(_coconut_case_match_to_9) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_9.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_9, "_coconut_data_defaults", {}) and _coconut_case_match_to_9[i] == _coconut.getattr(_coconut_case_match_to_9, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_9.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_9, "__match_args__") else _coconut.len(_coconut_case_match_to_9) == 4  # type: ignore  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                    if _coconut_match_temp_232:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                        _coconut_case_match_check_9 = True  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):

            if not _coconut_case_match_check_9:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                if (not _coconut_match_temp_231) and (_coconut.isinstance(_coconut_case_match_to_9, Torch)):  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                    _coconut_case_match_check_9 = True  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                if _coconut_case_match_check_9:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                    _coconut_case_match_check_9 = False  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                    if not _coconut_case_match_check_9:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                        if _coconut.type(_coconut_case_match_to_9) in _coconut_self_match_types:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports 1)")  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                            _coconut_case_match_check_9 = True  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):

                    if not _coconut_case_match_check_9:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                        if not _coconut.type(_coconut_case_match_to_9) in _coconut_self_match_types:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                            _coconut_match_temp_233 = _coconut.getattr(Torch, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                            if not _coconut.isinstance(_coconut_match_temp_233, _coconut.tuple):  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                                raise _coconut.TypeError("Torch.__match_args__ must be a tuple")  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                            if _coconut.len(_coconut_match_temp_233) < 4:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports %s)" % (_coconut.len(_coconut_match_temp_233),))  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                            _coconut_match_temp_234 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_233[0], _coconut_sentinel)  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                            _coconut_match_temp_235 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_233[1], _coconut_sentinel)  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                            _coconut_match_temp_236 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_233[2], _coconut_sentinel)  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                            _coconut_match_temp_237 = _coconut.getattr(_coconut_case_match_to_9, _coconut_match_temp_233[3], _coconut_sentinel)  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                            if (_coconut_match_temp_234 is not _coconut_sentinel) and (_coconut_match_temp_234 == "float32") and (_coconut_match_temp_235 is not _coconut_sentinel) and (_coconut_match_temp_235 == "CHW") and (_coconut_match_temp_236 is not _coconut_sentinel) and (_coconut_match_temp_236 == "YCbCr") and (_coconut_match_temp_237 is not _coconut_sentinel) and (_coconut_match_temp_237 == VR_0_1):  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
                                _coconut_case_match_check_9 = True  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):




        if _coconut_case_match_check_9:  #386:         match Torch("float32","CHW","YCbCr",==VR_0_1):
            return ([DataEdge(a=state, b=Torch("float32", "CHW", "RGB", VR_0_1), f=ycbcr_to_rgb, cost=1, name="YCbCr_to_RGB(torch)"),])  #387:             return [DataEdge(a=state,



#shape change!

ms_add_b_ch = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (1, *s)))  #397: ms_add_b_ch = (s->(1,*s)) |> ss_to_ms$
"adds 1 as batch shape"  #398: "adds 1 as batch shape"
ms_del_b_ch = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: s[1:]))  #399: ms_del_b_ch = (s->s[1:])  |> ss_to_ms$
# TODO what to do with non-batched states?

def en_batch(imdef: 'ImageDef'):  #402: def en_batch(imdef:ImageDef):
    _coconut_case_match_to_10 = imdef  #403:     case imdef:
    _coconut_case_match_check_10 = False  #403:     case imdef:
    _coconut_match_temp_238 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #403:     case imdef:
    _coconut_case_match_check_10 = True  #403:     case imdef:
    if _coconut_case_match_check_10:  #403:     case imdef:
        _coconut_case_match_check_10 = False  #403:     case imdef:
        if not _coconut_case_match_check_10:  #403:     case imdef:
            _coconut_match_set_name_meta = _coconut_sentinel  #403:     case imdef:
            if (_coconut_match_temp_238) and (_coconut.isinstance(_coconut_case_match_to_10, ImageDef)) and (_coconut.len(_coconut_case_match_to_10) >= 2):  #403:     case imdef:
                _coconut_match_temp_239 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #403:     case imdef:
                _coconut_match_set_name_meta = _coconut_case_match_to_10[1]  #403:     case imdef:
                _coconut_match_temp_246 = _coconut.len(_coconut_case_match_to_10) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_10.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_10, "_coconut_data_defaults", {}) and _coconut_case_match_to_10[i] == _coconut.getattr(_coconut_case_match_to_10, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_10.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_10, "__match_args__") else _coconut.len(_coconut_case_match_to_10) == 2  # type: ignore  #403:     case imdef:
                if _coconut_match_temp_246:  #403:     case imdef:
                    _coconut_case_match_check_10 = True  #403:     case imdef:
            if _coconut_case_match_check_10:  #403:     case imdef:
                _coconut_case_match_check_10 = False  #403:     case imdef:
                if not _coconut_case_match_check_10:  #403:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #403:     case imdef:
                    _coconut_match_set_name_ch_repr = _coconut_sentinel  #403:     case imdef:
                    _coconut_match_set_name_vr = _coconut_sentinel  #403:     case imdef:
                    if (_coconut_match_temp_239) and (_coconut.isinstance(_coconut_case_match_to_10[0], TensorLike)) and (_coconut.len(_coconut_case_match_to_10[0]) >= 4):  #403:     case imdef:
                        _coconut_match_set_name_dtype = _coconut_case_match_to_10[0][0]  #403:     case imdef:
                        _coconut_match_set_name_ch_repr = _coconut_case_match_to_10[0][2]  #403:     case imdef:
                        _coconut_match_set_name_vr = _coconut_case_match_to_10[0][3]  #403:     case imdef:
                        _coconut_match_temp_240 = _coconut.len(_coconut_case_match_to_10[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_10[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_10[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_10[0][i] == _coconut.getattr(_coconut_case_match_to_10[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_10[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_10[0], "__match_args__") else _coconut.len(_coconut_case_match_to_10[0]) == 4  # type: ignore  #403:     case imdef:
                        if _coconut_match_temp_240:  #403:     case imdef:
                            _coconut_case_match_check_10 = True  #403:     case imdef:
                    if _coconut_case_match_check_10:  #403:     case imdef:
                        _coconut_case_match_check_10 = False  #403:     case imdef:
                        if not _coconut_case_match_check_10:  #403:     case imdef:
                            if _coconut_case_match_to_10[0][1] == "HWC":  #403:     case imdef:
                                _coconut_case_match_check_10 = True  #403:     case imdef:

                        if not _coconut_case_match_check_10:  #403:     case imdef:
                            if _coconut_case_match_to_10[0][1] == "CHW":  #403:     case imdef:
                                _coconut_case_match_check_10 = True  #403:     case imdef:

                        if not _coconut_case_match_check_10:  #403:     case imdef:
                            if _coconut_case_match_to_10[0][1] == "HW":  #403:     case imdef:
                                _coconut_case_match_check_10 = True  #403:     case imdef:


                    if _coconut_case_match_check_10:  #403:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #403:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #403:     case imdef:
                        if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #403:     case imdef:
                            ch_repr = _coconut_match_set_name_ch_repr  #403:     case imdef:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #403:     case imdef:
                            vr = _coconut_match_set_name_vr  #403:     case imdef:

                if not _coconut_case_match_check_10:  #403:     case imdef:
                    if (not _coconut_match_temp_239) and (_coconut.isinstance(_coconut_case_match_to_10[0], TensorLike)):  #403:     case imdef:
                        _coconut_case_match_check_10 = True  #403:     case imdef:
                    if _coconut_case_match_check_10:  #403:     case imdef:
                        _coconut_case_match_check_10 = False  #403:     case imdef:
                        if not _coconut_case_match_check_10:  #403:     case imdef:
                            if _coconut.type(_coconut_case_match_to_10[0]) in _coconut_self_match_types:  #403:     case imdef:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #403:     case imdef:
                                _coconut_case_match_check_10 = True  #403:     case imdef:

                        if not _coconut_case_match_check_10:  #403:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #403:     case imdef:
                            _coconut_match_set_name_ch_repr = _coconut_sentinel  #403:     case imdef:
                            _coconut_match_set_name_vr = _coconut_sentinel  #403:     case imdef:
                            if not _coconut.type(_coconut_case_match_to_10[0]) in _coconut_self_match_types:  #403:     case imdef:
                                _coconut_match_temp_241 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #403:     case imdef:
                                if not _coconut.isinstance(_coconut_match_temp_241, _coconut.tuple):  #403:     case imdef:
                                    raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #403:     case imdef:
                                if _coconut.len(_coconut_match_temp_241) < 4:  #403:     case imdef:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_241),))  #403:     case imdef:
                                _coconut_match_temp_242 = _coconut.getattr(_coconut_case_match_to_10[0], _coconut_match_temp_241[0], _coconut_sentinel)  #403:     case imdef:
                                _coconut_match_temp_243 = _coconut.getattr(_coconut_case_match_to_10[0], _coconut_match_temp_241[1], _coconut_sentinel)  #403:     case imdef:
                                _coconut_match_temp_244 = _coconut.getattr(_coconut_case_match_to_10[0], _coconut_match_temp_241[2], _coconut_sentinel)  #403:     case imdef:
                                _coconut_match_temp_245 = _coconut.getattr(_coconut_case_match_to_10[0], _coconut_match_temp_241[3], _coconut_sentinel)  #403:     case imdef:
                                if (_coconut_match_temp_242 is not _coconut_sentinel) and (_coconut_match_temp_243 is not _coconut_sentinel) and (_coconut_match_temp_244 is not _coconut_sentinel) and (_coconut_match_temp_245 is not _coconut_sentinel):  #403:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_match_temp_242  #403:     case imdef:
                                    _coconut_match_set_name_ch_repr = _coconut_match_temp_244  #403:     case imdef:
                                    _coconut_match_set_name_vr = _coconut_match_temp_245  #403:     case imdef:
                                    _coconut_case_match_check_10 = True  #403:     case imdef:
                            if _coconut_case_match_check_10:  #403:     case imdef:
                                _coconut_case_match_check_10 = False  #403:     case imdef:
                                if not _coconut_case_match_check_10:  #403:     case imdef:
                                    if _coconut_match_temp_243 == "HWC":  #403:     case imdef:
                                        _coconut_case_match_check_10 = True  #403:     case imdef:

                                if not _coconut_case_match_check_10:  #403:     case imdef:
                                    if _coconut_match_temp_243 == "CHW":  #403:     case imdef:
                                        _coconut_case_match_check_10 = True  #403:     case imdef:

                                if not _coconut_case_match_check_10:  #403:     case imdef:
                                    if _coconut_match_temp_243 == "HW":  #403:     case imdef:
                                        _coconut_case_match_check_10 = True  #403:     case imdef:


                            if _coconut_case_match_check_10:  #403:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #403:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #403:     case imdef:
                                if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #403:     case imdef:
                                    ch_repr = _coconut_match_set_name_ch_repr  #403:     case imdef:
                                if _coconut_match_set_name_vr is not _coconut_sentinel:  #403:     case imdef:
                                    vr = _coconut_match_set_name_vr  #403:     case imdef:




            if _coconut_case_match_check_10:  #403:     case imdef:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #403:     case imdef:
                    meta = _coconut_match_set_name_meta  #403:     case imdef:

        if not _coconut_case_match_check_10:  #403:     case imdef:
            if (not _coconut_match_temp_238) and (_coconut.isinstance(_coconut_case_match_to_10, ImageDef)):  #403:     case imdef:
                _coconut_case_match_check_10 = True  #403:     case imdef:
            if _coconut_case_match_check_10:  #403:     case imdef:
                _coconut_case_match_check_10 = False  #403:     case imdef:
                if not _coconut_case_match_check_10:  #403:     case imdef:
                    if _coconut.type(_coconut_case_match_to_10) in _coconut_self_match_types:  #403:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #403:     case imdef:
                        _coconut_case_match_check_10 = True  #403:     case imdef:

                if not _coconut_case_match_check_10:  #403:     case imdef:
                    _coconut_match_set_name_meta = _coconut_sentinel  #403:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_10) in _coconut_self_match_types:  #403:     case imdef:
                        _coconut_match_temp_247 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #403:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_247, _coconut.tuple):  #403:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #403:     case imdef:
                        if _coconut.len(_coconut_match_temp_247) < 2:  #403:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_247),))  #403:     case imdef:
                        _coconut_match_temp_248 = _coconut.getattr(_coconut_case_match_to_10, _coconut_match_temp_247[0], _coconut_sentinel)  #403:     case imdef:
                        _coconut_match_temp_256 = _coconut.getattr(_coconut_case_match_to_10, _coconut_match_temp_247[1], _coconut_sentinel)  #403:     case imdef:
                        if (_coconut_match_temp_248 is not _coconut_sentinel) and (_coconut_match_temp_256 is not _coconut_sentinel):  #403:     case imdef:
                            _coconut_match_temp_249 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #403:     case imdef:
                            _coconut_match_set_name_meta = _coconut_match_temp_256  #403:     case imdef:
                            _coconut_case_match_check_10 = True  #403:     case imdef:
                    if _coconut_case_match_check_10:  #403:     case imdef:
                        _coconut_case_match_check_10 = False  #403:     case imdef:
                        if not _coconut_case_match_check_10:  #403:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #403:     case imdef:
                            _coconut_match_set_name_ch_repr = _coconut_sentinel  #403:     case imdef:
                            _coconut_match_set_name_vr = _coconut_sentinel  #403:     case imdef:
                            if (_coconut_match_temp_249) and (_coconut.isinstance(_coconut_match_temp_248, TensorLike)) and (_coconut.len(_coconut_match_temp_248) >= 4):  #403:     case imdef:
                                _coconut_match_set_name_dtype = _coconut_match_temp_248[0]  #403:     case imdef:
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_248[2]  #403:     case imdef:
                                _coconut_match_set_name_vr = _coconut_match_temp_248[3]  #403:     case imdef:
                                _coconut_match_temp_250 = _coconut.len(_coconut_match_temp_248) <= _coconut.max(4, _coconut.len(_coconut_match_temp_248.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_248, "_coconut_data_defaults", {}) and _coconut_match_temp_248[i] == _coconut.getattr(_coconut_match_temp_248, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_248.__match_args__))) if _coconut.hasattr(_coconut_match_temp_248, "__match_args__") else _coconut.len(_coconut_match_temp_248) == 4  # type: ignore  #403:     case imdef:
                                if _coconut_match_temp_250:  #403:     case imdef:
                                    _coconut_case_match_check_10 = True  #403:     case imdef:
                            if _coconut_case_match_check_10:  #403:     case imdef:
                                _coconut_case_match_check_10 = False  #403:     case imdef:
                                if not _coconut_case_match_check_10:  #403:     case imdef:
                                    if _coconut_match_temp_248[1] == "HWC":  #403:     case imdef:
                                        _coconut_case_match_check_10 = True  #403:     case imdef:

                                if not _coconut_case_match_check_10:  #403:     case imdef:
                                    if _coconut_match_temp_248[1] == "CHW":  #403:     case imdef:
                                        _coconut_case_match_check_10 = True  #403:     case imdef:

                                if not _coconut_case_match_check_10:  #403:     case imdef:
                                    if _coconut_match_temp_248[1] == "HW":  #403:     case imdef:
                                        _coconut_case_match_check_10 = True  #403:     case imdef:


                            if _coconut_case_match_check_10:  #403:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #403:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #403:     case imdef:
                                if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #403:     case imdef:
                                    ch_repr = _coconut_match_set_name_ch_repr  #403:     case imdef:
                                if _coconut_match_set_name_vr is not _coconut_sentinel:  #403:     case imdef:
                                    vr = _coconut_match_set_name_vr  #403:     case imdef:

                        if not _coconut_case_match_check_10:  #403:     case imdef:
                            if (not _coconut_match_temp_249) and (_coconut.isinstance(_coconut_match_temp_248, TensorLike)):  #403:     case imdef:
                                _coconut_case_match_check_10 = True  #403:     case imdef:
                            if _coconut_case_match_check_10:  #403:     case imdef:
                                _coconut_case_match_check_10 = False  #403:     case imdef:
                                if not _coconut_case_match_check_10:  #403:     case imdef:
                                    if _coconut.type(_coconut_match_temp_248) in _coconut_self_match_types:  #403:     case imdef:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #403:     case imdef:
                                        _coconut_case_match_check_10 = True  #403:     case imdef:

                                if not _coconut_case_match_check_10:  #403:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_sentinel  #403:     case imdef:
                                    _coconut_match_set_name_ch_repr = _coconut_sentinel  #403:     case imdef:
                                    _coconut_match_set_name_vr = _coconut_sentinel  #403:     case imdef:
                                    if not _coconut.type(_coconut_match_temp_248) in _coconut_self_match_types:  #403:     case imdef:
                                        _coconut_match_temp_251 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #403:     case imdef:
                                        if not _coconut.isinstance(_coconut_match_temp_251, _coconut.tuple):  #403:     case imdef:
                                            raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #403:     case imdef:
                                        if _coconut.len(_coconut_match_temp_251) < 4:  #403:     case imdef:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_251),))  #403:     case imdef:
                                        _coconut_match_temp_252 = _coconut.getattr(_coconut_match_temp_248, _coconut_match_temp_251[0], _coconut_sentinel)  #403:     case imdef:
                                        _coconut_match_temp_253 = _coconut.getattr(_coconut_match_temp_248, _coconut_match_temp_251[1], _coconut_sentinel)  #403:     case imdef:
                                        _coconut_match_temp_254 = _coconut.getattr(_coconut_match_temp_248, _coconut_match_temp_251[2], _coconut_sentinel)  #403:     case imdef:
                                        _coconut_match_temp_255 = _coconut.getattr(_coconut_match_temp_248, _coconut_match_temp_251[3], _coconut_sentinel)  #403:     case imdef:
                                        if (_coconut_match_temp_252 is not _coconut_sentinel) and (_coconut_match_temp_253 is not _coconut_sentinel) and (_coconut_match_temp_254 is not _coconut_sentinel) and (_coconut_match_temp_255 is not _coconut_sentinel):  #403:     case imdef:
                                            _coconut_match_set_name_dtype = _coconut_match_temp_252  #403:     case imdef:
                                            _coconut_match_set_name_ch_repr = _coconut_match_temp_254  #403:     case imdef:
                                            _coconut_match_set_name_vr = _coconut_match_temp_255  #403:     case imdef:
                                            _coconut_case_match_check_10 = True  #403:     case imdef:
                                    if _coconut_case_match_check_10:  #403:     case imdef:
                                        _coconut_case_match_check_10 = False  #403:     case imdef:
                                        if not _coconut_case_match_check_10:  #403:     case imdef:
                                            if _coconut_match_temp_253 == "HWC":  #403:     case imdef:
                                                _coconut_case_match_check_10 = True  #403:     case imdef:

                                        if not _coconut_case_match_check_10:  #403:     case imdef:
                                            if _coconut_match_temp_253 == "CHW":  #403:     case imdef:
                                                _coconut_case_match_check_10 = True  #403:     case imdef:

                                        if not _coconut_case_match_check_10:  #403:     case imdef:
                                            if _coconut_match_temp_253 == "HW":  #403:     case imdef:
                                                _coconut_case_match_check_10 = True  #403:     case imdef:


                                    if _coconut_case_match_check_10:  #403:     case imdef:
                                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #403:     case imdef:
                                            dtype = _coconut_match_set_name_dtype  #403:     case imdef:
                                        if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #403:     case imdef:
                                            ch_repr = _coconut_match_set_name_ch_repr  #403:     case imdef:
                                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #403:     case imdef:
                                            vr = _coconut_match_set_name_vr  #403:     case imdef:




                    if _coconut_case_match_check_10:  #403:     case imdef:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #403:     case imdef:
                            meta = _coconut_match_set_name_meta  #403:     case imdef:




    if _coconut_case_match_check_10:  #403:     case imdef:
        new_arng = "B" + imdef.data_type.arrange  #405:             new_arng = "B"+imdef.data_type.arrange
        return ([Edge(a=imdef, b=ImageDef(imdef.data_type.__class__(dtype, new_arng, ch_repr, vr), ms_add_b_ch(meta)), f=lambda a: a[None], cost=10, name="tensor_like en_batch".format()),])  #406:             return [Edge(a=imdef,
    if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
        _coconut_match_temp_257 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
        _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
        if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
            _coconut_case_match_check_10 = False  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
            if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                if (_coconut_match_temp_257) and (_coconut.isinstance(_coconut_case_match_to_10, ImageDef)) and (_coconut.len(_coconut_case_match_to_10) >= 2):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                    _coconut_match_temp_258 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_10[1]  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                    _coconut_match_temp_263 = _coconut.len(_coconut_case_match_to_10) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_10.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_10, "_coconut_data_defaults", {}) and _coconut_case_match_to_10[i] == _coconut.getattr(_coconut_case_match_to_10, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_10.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_10, "__match_args__") else _coconut.len(_coconut_case_match_to_10) == 2  # type: ignore  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                    if _coconut_match_temp_263:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                    _coconut_case_match_check_10 = False  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                    if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        _coconut_match_set_name_mode = _coconut_sentinel  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        _coconut_match_set_name_channel_repr = _coconut_sentinel  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        if (_coconut_match_temp_258) and (_coconut.isinstance(_coconut_case_match_to_10[0], PILImage)) and (_coconut.len(_coconut_case_match_to_10[0]) >= 2):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            _coconut_match_set_name_mode = _coconut_case_match_to_10[0][0]  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            _coconut_match_set_name_channel_repr = _coconut_case_match_to_10[0][1]  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            _coconut_match_temp_259 = _coconut.len(_coconut_case_match_to_10[0]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_10[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_10[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_10[0][i] == _coconut.getattr(_coconut_case_match_to_10[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_10[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_10[0], "__match_args__") else _coconut.len(_coconut_case_match_to_10[0]) == 2  # type: ignore  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            if _coconut_match_temp_259:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            if _coconut_match_set_name_mode is not _coconut_sentinel:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                mode = _coconut_match_set_name_mode  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            if _coconut_match_set_name_channel_repr is not _coconut_sentinel:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                channel_repr = _coconut_match_set_name_channel_repr  #412:         match ImageDef(PILImage(mode,channel_repr),meta):

                    if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        if (not _coconut_match_temp_258) and (_coconut.isinstance(_coconut_case_match_to_10[0], PILImage)):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            _coconut_case_match_check_10 = False  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                if _coconut.type(_coconut_case_match_to_10[0]) in _coconut_self_match_types:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):

                            if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                _coconut_match_set_name_mode = _coconut_sentinel  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                _coconut_match_set_name_channel_repr = _coconut_sentinel  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                if not _coconut.type(_coconut_case_match_to_10[0]) in _coconut_self_match_types:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    _coconut_match_temp_260 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_260, _coconut.tuple):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    if _coconut.len(_coconut_match_temp_260) < 2:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_260),))  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    _coconut_match_temp_261 = _coconut.getattr(_coconut_case_match_to_10[0], _coconut_match_temp_260[0], _coconut_sentinel)  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    _coconut_match_temp_262 = _coconut.getattr(_coconut_case_match_to_10[0], _coconut_match_temp_260[1], _coconut_sentinel)  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    if (_coconut_match_temp_261 is not _coconut_sentinel) and (_coconut_match_temp_262 is not _coconut_sentinel):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        _coconut_match_set_name_mode = _coconut_match_temp_261  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        _coconut_match_set_name_channel_repr = _coconut_match_temp_262  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    if _coconut_match_set_name_mode is not _coconut_sentinel:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        mode = _coconut_match_set_name_mode  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    if _coconut_match_set_name_channel_repr is not _coconut_sentinel:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        channel_repr = _coconut_match_set_name_channel_repr  #412:         match ImageDef(PILImage(mode,channel_repr),meta):




                if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        meta = _coconut_match_set_name_meta  #412:         match ImageDef(PILImage(mode,channel_repr),meta):

            if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                if (not _coconut_match_temp_257) and (_coconut.isinstance(_coconut_case_match_to_10, ImageDef)):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                    _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                    _coconut_case_match_check_10 = False  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                    if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        if _coconut.type(_coconut_case_match_to_10) in _coconut_self_match_types:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):

                    if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        if not _coconut.type(_coconut_case_match_to_10) in _coconut_self_match_types:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            _coconut_match_temp_264 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            if not _coconut.isinstance(_coconut_match_temp_264, _coconut.tuple):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            if _coconut.len(_coconut_match_temp_264) < 2:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_264),))  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            _coconut_match_temp_265 = _coconut.getattr(_coconut_case_match_to_10, _coconut_match_temp_264[0], _coconut_sentinel)  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            _coconut_match_temp_271 = _coconut.getattr(_coconut_case_match_to_10, _coconut_match_temp_264[1], _coconut_sentinel)  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            if (_coconut_match_temp_265 is not _coconut_sentinel) and (_coconut_match_temp_271 is not _coconut_sentinel):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                _coconut_match_temp_266 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_271  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                        if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            _coconut_case_match_check_10 = False  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                _coconut_match_set_name_mode = _coconut_sentinel  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                _coconut_match_set_name_channel_repr = _coconut_sentinel  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                if (_coconut_match_temp_266) and (_coconut.isinstance(_coconut_match_temp_265, PILImage)) and (_coconut.len(_coconut_match_temp_265) >= 2):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    _coconut_match_set_name_mode = _coconut_match_temp_265[0]  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    _coconut_match_set_name_channel_repr = _coconut_match_temp_265[1]  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    _coconut_match_temp_267 = _coconut.len(_coconut_match_temp_265) <= _coconut.max(2, _coconut.len(_coconut_match_temp_265.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_265, "_coconut_data_defaults", {}) and _coconut_match_temp_265[i] == _coconut.getattr(_coconut_match_temp_265, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_match_temp_265.__match_args__))) if _coconut.hasattr(_coconut_match_temp_265, "__match_args__") else _coconut.len(_coconut_match_temp_265) == 2  # type: ignore  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    if _coconut_match_temp_267:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    if _coconut_match_set_name_mode is not _coconut_sentinel:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        mode = _coconut_match_set_name_mode  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    if _coconut_match_set_name_channel_repr is not _coconut_sentinel:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        channel_repr = _coconut_match_set_name_channel_repr  #412:         match ImageDef(PILImage(mode,channel_repr),meta):

                            if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                if (not _coconut_match_temp_266) and (_coconut.isinstance(_coconut_match_temp_265, PILImage)):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    _coconut_case_match_check_10 = False  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                    if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        if _coconut.type(_coconut_match_temp_265) in _coconut_self_match_types:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                            _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):

                                    if not _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        _coconut_match_set_name_mode = _coconut_sentinel  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        _coconut_match_set_name_channel_repr = _coconut_sentinel  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        if not _coconut.type(_coconut_match_temp_265) in _coconut_self_match_types:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                            _coconut_match_temp_268 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_268, _coconut.tuple):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                                raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                            if _coconut.len(_coconut_match_temp_268) < 2:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_268),))  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                            _coconut_match_temp_269 = _coconut.getattr(_coconut_match_temp_265, _coconut_match_temp_268[0], _coconut_sentinel)  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                            _coconut_match_temp_270 = _coconut.getattr(_coconut_match_temp_265, _coconut_match_temp_268[1], _coconut_sentinel)  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                            if (_coconut_match_temp_269 is not _coconut_sentinel) and (_coconut_match_temp_270 is not _coconut_sentinel):  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                                _coconut_match_set_name_mode = _coconut_match_temp_269  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                                _coconut_match_set_name_channel_repr = _coconut_match_temp_270  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                                _coconut_case_match_check_10 = True  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                        if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                            if _coconut_match_set_name_mode is not _coconut_sentinel:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                                mode = _coconut_match_set_name_mode  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                            if _coconut_match_set_name_channel_repr is not _coconut_sentinel:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                                channel_repr = _coconut_match_set_name_channel_repr  #412:         match ImageDef(PILImage(mode,channel_repr),meta):




                        if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
                                meta = _coconut_match_set_name_meta  #412:         match ImageDef(PILImage(mode,channel_repr),meta):




        if _coconut_case_match_check_10:  #412:         match ImageDef(PILImage(mode,channel_repr),meta):
            return ([Edge(a=imdef, b=ImageDef(PILImages(mode, channel_repr), ms_add_b_ch(meta)), f=lambda a: [a,], cost=10, name="pil image en_batch".format()),])  #413:             return [Edge(a=imdef,
    return ([])  #419:     return []


def de_batch(imdef: 'ImageDef'):  #421: def de_batch(imdef:ImageDef):
    _coconut_case_match_to_11 = imdef  #422:     case imdef:
    _coconut_case_match_check_11 = False  #422:     case imdef:
    _coconut_match_temp_272 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #422:     case imdef:
    _coconut_case_match_check_11 = True  #422:     case imdef:
    if _coconut_case_match_check_11:  #422:     case imdef:
        _coconut_case_match_check_11 = False  #422:     case imdef:
        if not _coconut_case_match_check_11:  #422:     case imdef:
            _coconut_match_set_name_meta = _coconut_sentinel  #422:     case imdef:
            _coconut_match_set_name_shape = _coconut_sentinel  #422:     case imdef:
            if (_coconut_match_temp_272) and (_coconut.isinstance(_coconut_case_match_to_11, ImageDef)) and (_coconut.len(_coconut_case_match_to_11) >= 2) and (_coconut.isinstance(_coconut_case_match_to_11[1], _coconut.abc.Mapping)):  #422:     case imdef:
                _coconut_match_temp_273 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #422:     case imdef:
                _coconut_match_set_name_meta = _coconut_case_match_to_11[1]  #422:     case imdef:
                _coconut_match_temp_280 = _coconut_case_match_to_11[1].get("shape", _coconut_sentinel)  #422:     case imdef:
                _coconut_match_temp_281 = _coconut.len(_coconut_case_match_to_11) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_11.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_11, "_coconut_data_defaults", {}) and _coconut_case_match_to_11[i] == _coconut.getattr(_coconut_case_match_to_11, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_11.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_11, "__match_args__") else _coconut.len(_coconut_case_match_to_11) == 2  # type: ignore  #422:     case imdef:
                if (_coconut_match_temp_280 is not _coconut_sentinel) and (_coconut_match_temp_281):  #422:     case imdef:
                    _coconut_match_set_name_shape = _coconut_match_temp_280  #422:     case imdef:
                    _coconut_case_match_check_11 = True  #422:     case imdef:
            if _coconut_case_match_check_11:  #422:     case imdef:
                _coconut_case_match_check_11 = False  #422:     case imdef:
                if not _coconut_case_match_check_11:  #422:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #422:     case imdef:
                    _coconut_match_set_name_arng = _coconut_sentinel  #422:     case imdef:
                    _coconut_match_set_name_ch = _coconut_sentinel  #422:     case imdef:
                    _coconut_match_set_name_vr = _coconut_sentinel  #422:     case imdef:
                    if (_coconut_match_temp_273) and (_coconut.isinstance(_coconut_case_match_to_11[0], TensorLike)) and (_coconut.len(_coconut_case_match_to_11[0]) >= 4):  #422:     case imdef:
                        _coconut_match_set_name_dtype = _coconut_case_match_to_11[0][0]  #422:     case imdef:
                        _coconut_match_set_name_arng = _coconut_case_match_to_11[0][1]  #422:     case imdef:
                        _coconut_match_set_name_ch = _coconut_case_match_to_11[0][2]  #422:     case imdef:
                        _coconut_match_set_name_vr = _coconut_case_match_to_11[0][3]  #422:     case imdef:
                        _coconut_match_temp_274 = _coconut.len(_coconut_case_match_to_11[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_11[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_11[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_11[0][i] == _coconut.getattr(_coconut_case_match_to_11[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_11[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_11[0], "__match_args__") else _coconut.len(_coconut_case_match_to_11[0]) == 4  # type: ignore  #422:     case imdef:
                        if _coconut_match_temp_274:  #422:     case imdef:
                            _coconut_case_match_check_11 = True  #422:     case imdef:
                    if _coconut_case_match_check_11:  #422:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #422:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #422:     case imdef:
                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #422:     case imdef:
                            arng = _coconut_match_set_name_arng  #422:     case imdef:
                        if _coconut_match_set_name_ch is not _coconut_sentinel:  #422:     case imdef:
                            ch = _coconut_match_set_name_ch  #422:     case imdef:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #422:     case imdef:
                            vr = _coconut_match_set_name_vr  #422:     case imdef:

                if not _coconut_case_match_check_11:  #422:     case imdef:
                    if (not _coconut_match_temp_273) and (_coconut.isinstance(_coconut_case_match_to_11[0], TensorLike)):  #422:     case imdef:
                        _coconut_case_match_check_11 = True  #422:     case imdef:
                    if _coconut_case_match_check_11:  #422:     case imdef:
                        _coconut_case_match_check_11 = False  #422:     case imdef:
                        if not _coconut_case_match_check_11:  #422:     case imdef:
                            if _coconut.type(_coconut_case_match_to_11[0]) in _coconut_self_match_types:  #422:     case imdef:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #422:     case imdef:
                                _coconut_case_match_check_11 = True  #422:     case imdef:

                        if not _coconut_case_match_check_11:  #422:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #422:     case imdef:
                            _coconut_match_set_name_arng = _coconut_sentinel  #422:     case imdef:
                            _coconut_match_set_name_ch = _coconut_sentinel  #422:     case imdef:
                            _coconut_match_set_name_vr = _coconut_sentinel  #422:     case imdef:
                            if not _coconut.type(_coconut_case_match_to_11[0]) in _coconut_self_match_types:  #422:     case imdef:
                                _coconut_match_temp_275 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #422:     case imdef:
                                if not _coconut.isinstance(_coconut_match_temp_275, _coconut.tuple):  #422:     case imdef:
                                    raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #422:     case imdef:
                                if _coconut.len(_coconut_match_temp_275) < 4:  #422:     case imdef:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_275),))  #422:     case imdef:
                                _coconut_match_temp_276 = _coconut.getattr(_coconut_case_match_to_11[0], _coconut_match_temp_275[0], _coconut_sentinel)  #422:     case imdef:
                                _coconut_match_temp_277 = _coconut.getattr(_coconut_case_match_to_11[0], _coconut_match_temp_275[1], _coconut_sentinel)  #422:     case imdef:
                                _coconut_match_temp_278 = _coconut.getattr(_coconut_case_match_to_11[0], _coconut_match_temp_275[2], _coconut_sentinel)  #422:     case imdef:
                                _coconut_match_temp_279 = _coconut.getattr(_coconut_case_match_to_11[0], _coconut_match_temp_275[3], _coconut_sentinel)  #422:     case imdef:
                                if (_coconut_match_temp_276 is not _coconut_sentinel) and (_coconut_match_temp_277 is not _coconut_sentinel) and (_coconut_match_temp_278 is not _coconut_sentinel) and (_coconut_match_temp_279 is not _coconut_sentinel):  #422:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_match_temp_276  #422:     case imdef:
                                    _coconut_match_set_name_arng = _coconut_match_temp_277  #422:     case imdef:
                                    _coconut_match_set_name_ch = _coconut_match_temp_278  #422:     case imdef:
                                    _coconut_match_set_name_vr = _coconut_match_temp_279  #422:     case imdef:
                                    _coconut_case_match_check_11 = True  #422:     case imdef:
                            if _coconut_case_match_check_11:  #422:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #422:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #422:     case imdef:
                                if _coconut_match_set_name_arng is not _coconut_sentinel:  #422:     case imdef:
                                    arng = _coconut_match_set_name_arng  #422:     case imdef:
                                if _coconut_match_set_name_ch is not _coconut_sentinel:  #422:     case imdef:
                                    ch = _coconut_match_set_name_ch  #422:     case imdef:
                                if _coconut_match_set_name_vr is not _coconut_sentinel:  #422:     case imdef:
                                    vr = _coconut_match_set_name_vr  #422:     case imdef:




            if _coconut_case_match_check_11:  #422:     case imdef:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #422:     case imdef:
                    meta = _coconut_match_set_name_meta  #422:     case imdef:
                if _coconut_match_set_name_shape is not _coconut_sentinel:  #422:     case imdef:
                    shape = _coconut_match_set_name_shape  #422:     case imdef:

        if not _coconut_case_match_check_11:  #422:     case imdef:
            if (not _coconut_match_temp_272) and (_coconut.isinstance(_coconut_case_match_to_11, ImageDef)):  #422:     case imdef:
                _coconut_case_match_check_11 = True  #422:     case imdef:
            if _coconut_case_match_check_11:  #422:     case imdef:
                _coconut_case_match_check_11 = False  #422:     case imdef:
                if not _coconut_case_match_check_11:  #422:     case imdef:
                    if _coconut.type(_coconut_case_match_to_11) in _coconut_self_match_types:  #422:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #422:     case imdef:
                        _coconut_case_match_check_11 = True  #422:     case imdef:

                if not _coconut_case_match_check_11:  #422:     case imdef:
                    _coconut_match_set_name_meta = _coconut_sentinel  #422:     case imdef:
                    _coconut_match_set_name_shape = _coconut_sentinel  #422:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_11) in _coconut_self_match_types:  #422:     case imdef:
                        _coconut_match_temp_282 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #422:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_282, _coconut.tuple):  #422:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #422:     case imdef:
                        if _coconut.len(_coconut_match_temp_282) < 2:  #422:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_282),))  #422:     case imdef:
                        _coconut_match_temp_283 = _coconut.getattr(_coconut_case_match_to_11, _coconut_match_temp_282[0], _coconut_sentinel)  #422:     case imdef:
                        _coconut_match_temp_291 = _coconut.getattr(_coconut_case_match_to_11, _coconut_match_temp_282[1], _coconut_sentinel)  #422:     case imdef:
                        if (_coconut_match_temp_283 is not _coconut_sentinel) and (_coconut_match_temp_291 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_291, _coconut.abc.Mapping)):  #422:     case imdef:
                            _coconut_match_temp_284 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #422:     case imdef:
                            _coconut_match_set_name_meta = _coconut_match_temp_291  #422:     case imdef:
                            _coconut_match_temp_292 = _coconut_match_temp_291.get("shape", _coconut_sentinel)  #422:     case imdef:
                            if _coconut_match_temp_292 is not _coconut_sentinel:  #422:     case imdef:
                                _coconut_match_set_name_shape = _coconut_match_temp_292  #422:     case imdef:
                                _coconut_case_match_check_11 = True  #422:     case imdef:
                    if _coconut_case_match_check_11:  #422:     case imdef:
                        _coconut_case_match_check_11 = False  #422:     case imdef:
                        if not _coconut_case_match_check_11:  #422:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #422:     case imdef:
                            _coconut_match_set_name_arng = _coconut_sentinel  #422:     case imdef:
                            _coconut_match_set_name_ch = _coconut_sentinel  #422:     case imdef:
                            _coconut_match_set_name_vr = _coconut_sentinel  #422:     case imdef:
                            if (_coconut_match_temp_284) and (_coconut.isinstance(_coconut_match_temp_283, TensorLike)) and (_coconut.len(_coconut_match_temp_283) >= 4):  #422:     case imdef:
                                _coconut_match_set_name_dtype = _coconut_match_temp_283[0]  #422:     case imdef:
                                _coconut_match_set_name_arng = _coconut_match_temp_283[1]  #422:     case imdef:
                                _coconut_match_set_name_ch = _coconut_match_temp_283[2]  #422:     case imdef:
                                _coconut_match_set_name_vr = _coconut_match_temp_283[3]  #422:     case imdef:
                                _coconut_match_temp_285 = _coconut.len(_coconut_match_temp_283) <= _coconut.max(4, _coconut.len(_coconut_match_temp_283.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_283, "_coconut_data_defaults", {}) and _coconut_match_temp_283[i] == _coconut.getattr(_coconut_match_temp_283, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_283.__match_args__))) if _coconut.hasattr(_coconut_match_temp_283, "__match_args__") else _coconut.len(_coconut_match_temp_283) == 4  # type: ignore  #422:     case imdef:
                                if _coconut_match_temp_285:  #422:     case imdef:
                                    _coconut_case_match_check_11 = True  #422:     case imdef:
                            if _coconut_case_match_check_11:  #422:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #422:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #422:     case imdef:
                                if _coconut_match_set_name_arng is not _coconut_sentinel:  #422:     case imdef:
                                    arng = _coconut_match_set_name_arng  #422:     case imdef:
                                if _coconut_match_set_name_ch is not _coconut_sentinel:  #422:     case imdef:
                                    ch = _coconut_match_set_name_ch  #422:     case imdef:
                                if _coconut_match_set_name_vr is not _coconut_sentinel:  #422:     case imdef:
                                    vr = _coconut_match_set_name_vr  #422:     case imdef:

                        if not _coconut_case_match_check_11:  #422:     case imdef:
                            if (not _coconut_match_temp_284) and (_coconut.isinstance(_coconut_match_temp_283, TensorLike)):  #422:     case imdef:
                                _coconut_case_match_check_11 = True  #422:     case imdef:
                            if _coconut_case_match_check_11:  #422:     case imdef:
                                _coconut_case_match_check_11 = False  #422:     case imdef:
                                if not _coconut_case_match_check_11:  #422:     case imdef:
                                    if _coconut.type(_coconut_match_temp_283) in _coconut_self_match_types:  #422:     case imdef:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #422:     case imdef:
                                        _coconut_case_match_check_11 = True  #422:     case imdef:

                                if not _coconut_case_match_check_11:  #422:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_sentinel  #422:     case imdef:
                                    _coconut_match_set_name_arng = _coconut_sentinel  #422:     case imdef:
                                    _coconut_match_set_name_ch = _coconut_sentinel  #422:     case imdef:
                                    _coconut_match_set_name_vr = _coconut_sentinel  #422:     case imdef:
                                    if not _coconut.type(_coconut_match_temp_283) in _coconut_self_match_types:  #422:     case imdef:
                                        _coconut_match_temp_286 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #422:     case imdef:
                                        if not _coconut.isinstance(_coconut_match_temp_286, _coconut.tuple):  #422:     case imdef:
                                            raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #422:     case imdef:
                                        if _coconut.len(_coconut_match_temp_286) < 4:  #422:     case imdef:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_286),))  #422:     case imdef:
                                        _coconut_match_temp_287 = _coconut.getattr(_coconut_match_temp_283, _coconut_match_temp_286[0], _coconut_sentinel)  #422:     case imdef:
                                        _coconut_match_temp_288 = _coconut.getattr(_coconut_match_temp_283, _coconut_match_temp_286[1], _coconut_sentinel)  #422:     case imdef:
                                        _coconut_match_temp_289 = _coconut.getattr(_coconut_match_temp_283, _coconut_match_temp_286[2], _coconut_sentinel)  #422:     case imdef:
                                        _coconut_match_temp_290 = _coconut.getattr(_coconut_match_temp_283, _coconut_match_temp_286[3], _coconut_sentinel)  #422:     case imdef:
                                        if (_coconut_match_temp_287 is not _coconut_sentinel) and (_coconut_match_temp_288 is not _coconut_sentinel) and (_coconut_match_temp_289 is not _coconut_sentinel) and (_coconut_match_temp_290 is not _coconut_sentinel):  #422:     case imdef:
                                            _coconut_match_set_name_dtype = _coconut_match_temp_287  #422:     case imdef:
                                            _coconut_match_set_name_arng = _coconut_match_temp_288  #422:     case imdef:
                                            _coconut_match_set_name_ch = _coconut_match_temp_289  #422:     case imdef:
                                            _coconut_match_set_name_vr = _coconut_match_temp_290  #422:     case imdef:
                                            _coconut_case_match_check_11 = True  #422:     case imdef:
                                    if _coconut_case_match_check_11:  #422:     case imdef:
                                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #422:     case imdef:
                                            dtype = _coconut_match_set_name_dtype  #422:     case imdef:
                                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #422:     case imdef:
                                            arng = _coconut_match_set_name_arng  #422:     case imdef:
                                        if _coconut_match_set_name_ch is not _coconut_sentinel:  #422:     case imdef:
                                            ch = _coconut_match_set_name_ch  #422:     case imdef:
                                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #422:     case imdef:
                                            vr = _coconut_match_set_name_vr  #422:     case imdef:




                    if _coconut_case_match_check_11:  #422:     case imdef:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #422:     case imdef:
                            meta = _coconut_match_set_name_meta  #422:     case imdef:
                        if _coconut_match_set_name_shape is not _coconut_sentinel:  #422:     case imdef:
                            shape = _coconut_match_set_name_shape  #422:     case imdef:




    if _coconut_case_match_check_11 and not ("B" in arng and shape[0] == 1):  #422:     case imdef:
        _coconut_case_match_check_11 = False  #422:     case imdef:
    if _coconut_case_match_check_11:  #422:     case imdef:
        return ([Edge(a=imdef, b=ImageDef(imdef.data_type.__class__(dtype, arng[1:], ch, vr), ms_del_b_ch(meta)), f=lambda a: a[0], cost=1, name="de_batch en_batched image".format()),])  #424:             return [Edge(
    if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
        _coconut_match_temp_293 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
        _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
        if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
            _coconut_case_match_check_11 = False  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
            if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                _coconut_match_set_name_meta = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                _coconut_match_set_name_shape = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                if (_coconut_match_temp_293) and (_coconut.isinstance(_coconut_case_match_to_11, ImageDef)) and (_coconut.len(_coconut_case_match_to_11) >= 2) and (_coconut.isinstance(_coconut_case_match_to_11[1], _coconut.abc.Mapping)):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    _coconut_match_temp_294 = _coconut.getattr(PILImages, "_coconut_is_data", False) or _coconut.isinstance(PILImages, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImages)  # type: ignore  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    _coconut_match_set_name_meta = _coconut_case_match_to_11[1]  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    _coconut_match_temp_299 = _coconut_case_match_to_11[1].get("shape", _coconut_sentinel)  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    _coconut_match_temp_300 = _coconut.len(_coconut_case_match_to_11) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_11.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_11, "_coconut_data_defaults", {}) and _coconut_case_match_to_11[i] == _coconut.getattr(_coconut_case_match_to_11, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_11.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_11, "__match_args__") else _coconut.len(_coconut_case_match_to_11) == 2  # type: ignore  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    if (_coconut_match_temp_299 is not _coconut_sentinel) and (_coconut_match_temp_300):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        _coconut_match_set_name_shape = _coconut_match_temp_299  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    _coconut_case_match_check_11 = False  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        _coconut_match_set_name_mode = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        _coconut_match_set_name_ch = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        if (_coconut_match_temp_294) and (_coconut.isinstance(_coconut_case_match_to_11[0], PILImages)) and (_coconut.len(_coconut_case_match_to_11[0]) >= 2):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            _coconut_match_set_name_mode = _coconut_case_match_to_11[0][0]  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            _coconut_match_set_name_ch = _coconut_case_match_to_11[0][1]  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            _coconut_match_temp_295 = _coconut.len(_coconut_case_match_to_11[0]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_11[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_11[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_11[0][i] == _coconut.getattr(_coconut_case_match_to_11[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_11[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_11[0], "__match_args__") else _coconut.len(_coconut_case_match_to_11[0]) == 2  # type: ignore  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            if _coconut_match_temp_295:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            if _coconut_match_set_name_mode is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                mode = _coconut_match_set_name_mode  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            if _coconut_match_set_name_ch is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                ch = _coconut_match_set_name_ch  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:

                    if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        if (not _coconut_match_temp_294) and (_coconut.isinstance(_coconut_case_match_to_11[0], PILImages)):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            _coconut_case_match_check_11 = False  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                if _coconut.type(_coconut_case_match_to_11[0]) in _coconut_self_match_types:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports 1)")  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:

                            if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                _coconut_match_set_name_mode = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                _coconut_match_set_name_ch = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                if not _coconut.type(_coconut_case_match_to_11[0]) in _coconut_self_match_types:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    _coconut_match_temp_296 = _coconut.getattr(PILImages, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    if not _coconut.isinstance(_coconut_match_temp_296, _coconut.tuple):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        raise _coconut.TypeError("PILImages.__match_args__ must be a tuple")  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    if _coconut.len(_coconut_match_temp_296) < 2:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports %s)" % (_coconut.len(_coconut_match_temp_296),))  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    _coconut_match_temp_297 = _coconut.getattr(_coconut_case_match_to_11[0], _coconut_match_temp_296[0], _coconut_sentinel)  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    _coconut_match_temp_298 = _coconut.getattr(_coconut_case_match_to_11[0], _coconut_match_temp_296[1], _coconut_sentinel)  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    if (_coconut_match_temp_297 is not _coconut_sentinel) and (_coconut_match_temp_298 is not _coconut_sentinel):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        _coconut_match_set_name_mode = _coconut_match_temp_297  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        _coconut_match_set_name_ch = _coconut_match_temp_298  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    if _coconut_match_set_name_mode is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        mode = _coconut_match_set_name_mode  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    if _coconut_match_set_name_ch is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        ch = _coconut_match_set_name_ch  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:




                if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        meta = _coconut_match_set_name_meta  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    if _coconut_match_set_name_shape is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        shape = _coconut_match_set_name_shape  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:

            if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                if (not _coconut_match_temp_293) and (_coconut.isinstance(_coconut_case_match_to_11, ImageDef)):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    _coconut_case_match_check_11 = False  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                    if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        if _coconut.type(_coconut_case_match_to_11) in _coconut_self_match_types:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:

                    if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        _coconut_match_set_name_meta = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        _coconut_match_set_name_shape = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        if not _coconut.type(_coconut_case_match_to_11) in _coconut_self_match_types:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            _coconut_match_temp_301 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            if not _coconut.isinstance(_coconut_match_temp_301, _coconut.tuple):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            if _coconut.len(_coconut_match_temp_301) < 2:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_301),))  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            _coconut_match_temp_302 = _coconut.getattr(_coconut_case_match_to_11, _coconut_match_temp_301[0], _coconut_sentinel)  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            _coconut_match_temp_308 = _coconut.getattr(_coconut_case_match_to_11, _coconut_match_temp_301[1], _coconut_sentinel)  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            if (_coconut_match_temp_302 is not _coconut_sentinel) and (_coconut_match_temp_308 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_308, _coconut.abc.Mapping)):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                _coconut_match_temp_303 = _coconut.getattr(PILImages, "_coconut_is_data", False) or _coconut.isinstance(PILImages, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImages)  # type: ignore  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                _coconut_match_set_name_meta = _coconut_match_temp_308  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                _coconut_match_temp_309 = _coconut_match_temp_308.get("shape", _coconut_sentinel)  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                if _coconut_match_temp_309 is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    _coconut_match_set_name_shape = _coconut_match_temp_309  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                        if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            _coconut_case_match_check_11 = False  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                _coconut_match_set_name_mode = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                _coconut_match_set_name_ch = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                if (_coconut_match_temp_303) and (_coconut.isinstance(_coconut_match_temp_302, PILImages)) and (_coconut.len(_coconut_match_temp_302) >= 2):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    _coconut_match_set_name_mode = _coconut_match_temp_302[0]  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    _coconut_match_set_name_ch = _coconut_match_temp_302[1]  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    _coconut_match_temp_304 = _coconut.len(_coconut_match_temp_302) <= _coconut.max(2, _coconut.len(_coconut_match_temp_302.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_302, "_coconut_data_defaults", {}) and _coconut_match_temp_302[i] == _coconut.getattr(_coconut_match_temp_302, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_match_temp_302.__match_args__))) if _coconut.hasattr(_coconut_match_temp_302, "__match_args__") else _coconut.len(_coconut_match_temp_302) == 2  # type: ignore  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    if _coconut_match_temp_304:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    if _coconut_match_set_name_mode is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        mode = _coconut_match_set_name_mode  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    if _coconut_match_set_name_ch is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        ch = _coconut_match_set_name_ch  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:

                            if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                if (not _coconut_match_temp_303) and (_coconut.isinstance(_coconut_match_temp_302, PILImages)):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    _coconut_case_match_check_11 = False  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                    if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        if _coconut.type(_coconut_match_temp_302) in _coconut_self_match_types:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports 1)")  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                            _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:

                                    if not _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        _coconut_match_set_name_mode = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        _coconut_match_set_name_ch = _coconut_sentinel  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        if not _coconut.type(_coconut_match_temp_302) in _coconut_self_match_types:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                            _coconut_match_temp_305 = _coconut.getattr(PILImages, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                            if not _coconut.isinstance(_coconut_match_temp_305, _coconut.tuple):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                                raise _coconut.TypeError("PILImages.__match_args__ must be a tuple")  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                            if _coconut.len(_coconut_match_temp_305) < 2:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports %s)" % (_coconut.len(_coconut_match_temp_305),))  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                            _coconut_match_temp_306 = _coconut.getattr(_coconut_match_temp_302, _coconut_match_temp_305[0], _coconut_sentinel)  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                            _coconut_match_temp_307 = _coconut.getattr(_coconut_match_temp_302, _coconut_match_temp_305[1], _coconut_sentinel)  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                            if (_coconut_match_temp_306 is not _coconut_sentinel) and (_coconut_match_temp_307 is not _coconut_sentinel):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                                _coconut_match_set_name_mode = _coconut_match_temp_306  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                                _coconut_match_set_name_ch = _coconut_match_temp_307  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                                _coconut_case_match_check_11 = True  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                        if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                            if _coconut_match_set_name_mode is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                                mode = _coconut_match_set_name_mode  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                            if _coconut_match_set_name_ch is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                                ch = _coconut_match_set_name_ch  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:




                        if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                meta = _coconut_match_set_name_meta  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                            if _coconut_match_set_name_shape is not _coconut_sentinel:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
                                shape = _coconut_match_set_name_shape  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:




        if _coconut_case_match_check_11 and not ("en_batched" in meta):  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
            _coconut_case_match_check_11 = False  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
        if _coconut_case_match_check_11:  #431:         match ImageDef(PILImages(mode,ch),{"shape":shape} as meta) if "en_batched" in meta:
            return ([Edge(a=imdef, b=ImageDef(PILImage(mode, ch), ms_del_b_ch(meta)), f=lambda a: a[0], cost=1, name="de_batch en_batched image".format()),])  #432:             return [Edge(


def drop_meta(imdef: 'ImageDef'):  #440: def drop_meta(imdef:ImageDef):
    _coconut_case_match_to_12 = imdef  #441:     case imdef:
    _coconut_case_match_check_12 = False  #441:     case imdef:
    _coconut_match_temp_310 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #441:     case imdef:
    _coconut_case_match_check_12 = True  #441:     case imdef:
    if _coconut_case_match_check_12:  #441:     case imdef:
        _coconut_case_match_check_12 = False  #441:     case imdef:
        if not _coconut_case_match_check_12:  #441:     case imdef:
            _coconut_match_set_name_data_type = _coconut_sentinel  #441:     case imdef:
            _coconut_match_set_name_meta = _coconut_sentinel  #441:     case imdef:
            if (_coconut_match_temp_310) and (_coconut.isinstance(_coconut_case_match_to_12, ImageDef)) and (_coconut.len(_coconut_case_match_to_12) >= 2):  #441:     case imdef:
                _coconut_match_set_name_data_type = _coconut_case_match_to_12[0]  #441:     case imdef:
                _coconut_match_set_name_meta = _coconut_case_match_to_12[1]  #441:     case imdef:
                _coconut_match_temp_311 = _coconut.len(_coconut_case_match_to_12) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_12.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_12, "_coconut_data_defaults", {}) and _coconut_case_match_to_12[i] == _coconut.getattr(_coconut_case_match_to_12, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_12.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_12, "__match_args__") else _coconut.len(_coconut_case_match_to_12) == 2  # type: ignore  #441:     case imdef:
                if _coconut_match_temp_311:  #441:     case imdef:
                    _coconut_case_match_check_12 = True  #441:     case imdef:
            if _coconut_case_match_check_12:  #441:     case imdef:
                if _coconut_match_set_name_data_type is not _coconut_sentinel:  #441:     case imdef:
                    data_type = _coconut_match_set_name_data_type  #441:     case imdef:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #441:     case imdef:
                    meta = _coconut_match_set_name_meta  #441:     case imdef:

        if not _coconut_case_match_check_12:  #441:     case imdef:
            if (not _coconut_match_temp_310) and (_coconut.isinstance(_coconut_case_match_to_12, ImageDef)):  #441:     case imdef:
                _coconut_case_match_check_12 = True  #441:     case imdef:
            if _coconut_case_match_check_12:  #441:     case imdef:
                _coconut_case_match_check_12 = False  #441:     case imdef:
                if not _coconut_case_match_check_12:  #441:     case imdef:
                    if _coconut.type(_coconut_case_match_to_12) in _coconut_self_match_types:  #441:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #441:     case imdef:
                        _coconut_case_match_check_12 = True  #441:     case imdef:

                if not _coconut_case_match_check_12:  #441:     case imdef:
                    _coconut_match_set_name_data_type = _coconut_sentinel  #441:     case imdef:
                    _coconut_match_set_name_meta = _coconut_sentinel  #441:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_12) in _coconut_self_match_types:  #441:     case imdef:
                        _coconut_match_temp_312 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #441:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_312, _coconut.tuple):  #441:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #441:     case imdef:
                        if _coconut.len(_coconut_match_temp_312) < 2:  #441:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_312),))  #441:     case imdef:
                        _coconut_match_temp_313 = _coconut.getattr(_coconut_case_match_to_12, _coconut_match_temp_312[0], _coconut_sentinel)  #441:     case imdef:
                        _coconut_match_temp_314 = _coconut.getattr(_coconut_case_match_to_12, _coconut_match_temp_312[1], _coconut_sentinel)  #441:     case imdef:
                        if (_coconut_match_temp_313 is not _coconut_sentinel) and (_coconut_match_temp_314 is not _coconut_sentinel):  #441:     case imdef:
                            _coconut_match_set_name_data_type = _coconut_match_temp_313  #441:     case imdef:
                            _coconut_match_set_name_meta = _coconut_match_temp_314  #441:     case imdef:
                            _coconut_case_match_check_12 = True  #441:     case imdef:
                    if _coconut_case_match_check_12:  #441:     case imdef:
                        if _coconut_match_set_name_data_type is not _coconut_sentinel:  #441:     case imdef:
                            data_type = _coconut_match_set_name_data_type  #441:     case imdef:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #441:     case imdef:
                            meta = _coconut_match_set_name_meta  #441:     case imdef:




    if _coconut_case_match_check_12:  #441:     case imdef:
        return ([Edge(a=imdef, b=ImageDef(data_type, fdict()), f=lambda a: a, cost=1, name="drop all metadata"),])  #443:             return [Edge(


@to_imagedef  #451: @to_imagedef
def to_rgba(imdef: 'ImageDef'):  #452: def to_rgba(imdef:ImageDef):
    _coconut_case_match_to_13 = imdef  #453:     case imdef:
    _coconut_case_match_check_13 = False  #453:     case imdef:
    _coconut_match_temp_315 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #453:     case imdef:
    _coconut_case_match_check_13 = True  #453:     case imdef:
    if _coconut_case_match_check_13:  #453:     case imdef:
        _coconut_case_match_check_13 = False  #453:     case imdef:
        if not _coconut_case_match_check_13:  #453:     case imdef:
            _coconut_match_set_name_dtype = _coconut_sentinel  #453:     case imdef:
            _coconut_match_set_name_arng = _coconut_sentinel  #453:     case imdef:
            _coconut_match_set_name_ch_repr = _coconut_sentinel  #453:     case imdef:
            if (_coconut_match_temp_315) and (_coconut.isinstance(_coconut_case_match_to_13, TensorLike)) and (_coconut.len(_coconut_case_match_to_13) >= 4) and (_coconut_case_match_to_13[3] == "0_1"):  #453:     case imdef:
                _coconut_match_set_name_dtype = _coconut_case_match_to_13[0]  #453:     case imdef:
                _coconut_match_set_name_arng = _coconut_case_match_to_13[1]  #453:     case imdef:
                _coconut_match_set_name_ch_repr = _coconut_case_match_to_13[2]  #453:     case imdef:
                _coconut_match_temp_316 = _coconut.len(_coconut_case_match_to_13) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_13.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_13, "_coconut_data_defaults", {}) and _coconut_case_match_to_13[i] == _coconut.getattr(_coconut_case_match_to_13, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_13.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_13, "__match_args__") else _coconut.len(_coconut_case_match_to_13) == 4  # type: ignore  #453:     case imdef:
                if _coconut_match_temp_316:  #453:     case imdef:
                    _coconut_case_match_check_13 = True  #453:     case imdef:
            if _coconut_case_match_check_13:  #453:     case imdef:
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #453:     case imdef:
                    dtype = _coconut_match_set_name_dtype  #453:     case imdef:
                if _coconut_match_set_name_arng is not _coconut_sentinel:  #453:     case imdef:
                    arng = _coconut_match_set_name_arng  #453:     case imdef:
                if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #453:     case imdef:
                    ch_repr = _coconut_match_set_name_ch_repr  #453:     case imdef:

        if not _coconut_case_match_check_13:  #453:     case imdef:
            if (not _coconut_match_temp_315) and (_coconut.isinstance(_coconut_case_match_to_13, TensorLike)):  #453:     case imdef:
                _coconut_case_match_check_13 = True  #453:     case imdef:
            if _coconut_case_match_check_13:  #453:     case imdef:
                _coconut_case_match_check_13 = False  #453:     case imdef:
                if not _coconut_case_match_check_13:  #453:     case imdef:
                    if _coconut.type(_coconut_case_match_to_13) in _coconut_self_match_types:  #453:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #453:     case imdef:
                        _coconut_case_match_check_13 = True  #453:     case imdef:

                if not _coconut_case_match_check_13:  #453:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #453:     case imdef:
                    _coconut_match_set_name_arng = _coconut_sentinel  #453:     case imdef:
                    _coconut_match_set_name_ch_repr = _coconut_sentinel  #453:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_13) in _coconut_self_match_types:  #453:     case imdef:
                        _coconut_match_temp_317 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #453:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_317, _coconut.tuple):  #453:     case imdef:
                            raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #453:     case imdef:
                        if _coconut.len(_coconut_match_temp_317) < 4:  #453:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_317),))  #453:     case imdef:
                        _coconut_match_temp_318 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_317[0], _coconut_sentinel)  #453:     case imdef:
                        _coconut_match_temp_319 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_317[1], _coconut_sentinel)  #453:     case imdef:
                        _coconut_match_temp_320 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_317[2], _coconut_sentinel)  #453:     case imdef:
                        _coconut_match_temp_321 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_317[3], _coconut_sentinel)  #453:     case imdef:
                        if (_coconut_match_temp_318 is not _coconut_sentinel) and (_coconut_match_temp_319 is not _coconut_sentinel) and (_coconut_match_temp_320 is not _coconut_sentinel) and (_coconut_match_temp_321 is not _coconut_sentinel) and (_coconut_match_temp_321 == "0_1"):  #453:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_match_temp_318  #453:     case imdef:
                            _coconut_match_set_name_arng = _coconut_match_temp_319  #453:     case imdef:
                            _coconut_match_set_name_ch_repr = _coconut_match_temp_320  #453:     case imdef:
                            _coconut_case_match_check_13 = True  #453:     case imdef:
                    if _coconut_case_match_check_13:  #453:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #453:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #453:     case imdef:
                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #453:     case imdef:
                            arng = _coconut_match_set_name_arng  #453:     case imdef:
                        if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #453:     case imdef:
                            ch_repr = _coconut_match_set_name_ch_repr  #453:     case imdef:




    if _coconut_case_match_check_13 and not (ch_repr in KNOWN_COLOR_FMTS):  #453:     case imdef:
        _coconut_case_match_check_13 = False  #453:     case imdef:
    if _coconut_case_match_check_13:  #453:     case imdef:
        return ([])  # dont view color fmts in RGB space  #455:             return [] # dont view color fmts in RGB space
    if not _coconut_case_match_check_13:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
        _coconut_match_temp_322 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
        _coconut_case_match_check_13 = True  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
        if _coconut_case_match_check_13:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
            _coconut_case_match_check_13 = False  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
            if not _coconut_case_match_check_13:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                _coconut_match_set_name_dtype = _coconut_sentinel  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                _coconut_match_set_name_arng = _coconut_sentinel  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                _coconut_match_set_name_ch_repr = _coconut_sentinel  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                if (_coconut_match_temp_322) and (_coconut.isinstance(_coconut_case_match_to_13, TensorLike)) and (_coconut.len(_coconut_case_match_to_13) >= 4) and (_coconut_case_match_to_13[3] == "0_1"):  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                    _coconut_match_set_name_dtype = _coconut_case_match_to_13[0]  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                    _coconut_match_set_name_arng = _coconut_case_match_to_13[1]  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_13[2]  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                    _coconut_match_temp_323 = _coconut.len(_coconut_case_match_to_13) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_13.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_13, "_coconut_data_defaults", {}) and _coconut_case_match_to_13[i] == _coconut.getattr(_coconut_case_match_to_13, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_13.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_13, "__match_args__") else _coconut.len(_coconut_case_match_to_13) == 4  # type: ignore  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                    if _coconut_match_temp_323:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                        _coconut_case_match_check_13 = True  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                if _coconut_case_match_check_13:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                        dtype = _coconut_match_set_name_dtype  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                    if _coconut_match_set_name_arng is not _coconut_sentinel:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                        arng = _coconut_match_set_name_arng  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                        ch_repr = _coconut_match_set_name_ch_repr  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:

            if not _coconut_case_match_check_13:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                if (not _coconut_match_temp_322) and (_coconut.isinstance(_coconut_case_match_to_13, TensorLike)):  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                    _coconut_case_match_check_13 = True  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                if _coconut_case_match_check_13:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                    _coconut_case_match_check_13 = False  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                    if not _coconut_case_match_check_13:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                        if _coconut.type(_coconut_case_match_to_13) in _coconut_self_match_types:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            _coconut_case_match_check_13 = True  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:

                    if not _coconut_case_match_check_13:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                        _coconut_match_set_name_dtype = _coconut_sentinel  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                        _coconut_match_set_name_arng = _coconut_sentinel  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                        if not _coconut.type(_coconut_case_match_to_13) in _coconut_self_match_types:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            _coconut_match_temp_324 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            if not _coconut.isinstance(_coconut_match_temp_324, _coconut.tuple):  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                                raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            if _coconut.len(_coconut_match_temp_324) < 4:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_324),))  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            _coconut_match_temp_325 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_324[0], _coconut_sentinel)  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            _coconut_match_temp_326 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_324[1], _coconut_sentinel)  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            _coconut_match_temp_327 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_324[2], _coconut_sentinel)  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            _coconut_match_temp_328 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_324[3], _coconut_sentinel)  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            if (_coconut_match_temp_325 is not _coconut_sentinel) and (_coconut_match_temp_326 is not _coconut_sentinel) and (_coconut_match_temp_327 is not _coconut_sentinel) and (_coconut_match_temp_328 is not _coconut_sentinel) and (_coconut_match_temp_328 == "0_1"):  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                                _coconut_match_set_name_dtype = _coconut_match_temp_325  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                                _coconut_match_set_name_arng = _coconut_match_temp_326  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_327  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                                _coconut_case_match_check_13 = True  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                        if _coconut_case_match_check_13:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                                dtype = _coconut_match_set_name_dtype  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            if _coconut_match_set_name_arng is not _coconut_sentinel:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                                arng = _coconut_match_set_name_arng  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
                                ch_repr = _coconut_match_set_name_ch_repr  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:




        if _coconut_case_match_check_13 and not (len(ch_splitter(ch_repr)) == 4):  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
            _coconut_case_match_check_13 = False  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
        if _coconut_case_match_check_13:  #456:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 4:
            return ([DataEdge(a=imdef, b=imdef.__class__(dtype, arng, "RGBA", "0_1"), f=lambda a: a, cost=20, name="view {_coconut_format_0} as RGBA ".format(_coconut_format_0=(ch_repr))),])  #457:             return [DataEdge(a=imdef,
    if not _coconut_case_match_check_13:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
        _coconut_match_temp_329 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
        _coconut_case_match_check_13 = True  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
        if _coconut_case_match_check_13:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
            _coconut_case_match_check_13 = False  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
            if not _coconut_case_match_check_13:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                _coconut_match_set_name_dtype = _coconut_sentinel  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                _coconut_match_set_name_arng = _coconut_sentinel  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                _coconut_match_set_name_ch_repr = _coconut_sentinel  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                if (_coconut_match_temp_329) and (_coconut.isinstance(_coconut_case_match_to_13, TensorLike)) and (_coconut.len(_coconut_case_match_to_13) >= 4) and (_coconut_case_match_to_13[3] == "0_1"):  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                    _coconut_match_set_name_dtype = _coconut_case_match_to_13[0]  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                    _coconut_match_set_name_arng = _coconut_case_match_to_13[1]  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_13[2]  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                    _coconut_match_temp_330 = _coconut.len(_coconut_case_match_to_13) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_13.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_13, "_coconut_data_defaults", {}) and _coconut_case_match_to_13[i] == _coconut.getattr(_coconut_case_match_to_13, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_13.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_13, "__match_args__") else _coconut.len(_coconut_case_match_to_13) == 4  # type: ignore  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                    if _coconut_match_temp_330:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                        _coconut_case_match_check_13 = True  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                if _coconut_case_match_check_13:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                        dtype = _coconut_match_set_name_dtype  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                    if _coconut_match_set_name_arng is not _coconut_sentinel:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                        arng = _coconut_match_set_name_arng  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                        ch_repr = _coconut_match_set_name_ch_repr  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:

            if not _coconut_case_match_check_13:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                if (not _coconut_match_temp_329) and (_coconut.isinstance(_coconut_case_match_to_13, TensorLike)):  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                    _coconut_case_match_check_13 = True  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                if _coconut_case_match_check_13:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                    _coconut_case_match_check_13 = False  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                    if not _coconut_case_match_check_13:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                        if _coconut.type(_coconut_case_match_to_13) in _coconut_self_match_types:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            _coconut_case_match_check_13 = True  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:

                    if not _coconut_case_match_check_13:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                        _coconut_match_set_name_dtype = _coconut_sentinel  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                        _coconut_match_set_name_arng = _coconut_sentinel  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                        if not _coconut.type(_coconut_case_match_to_13) in _coconut_self_match_types:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            _coconut_match_temp_331 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            if not _coconut.isinstance(_coconut_match_temp_331, _coconut.tuple):  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                                raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            if _coconut.len(_coconut_match_temp_331) < 4:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_331),))  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            _coconut_match_temp_332 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_331[0], _coconut_sentinel)  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            _coconut_match_temp_333 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_331[1], _coconut_sentinel)  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            _coconut_match_temp_334 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_331[2], _coconut_sentinel)  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            _coconut_match_temp_335 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_331[3], _coconut_sentinel)  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            if (_coconut_match_temp_332 is not _coconut_sentinel) and (_coconut_match_temp_333 is not _coconut_sentinel) and (_coconut_match_temp_334 is not _coconut_sentinel) and (_coconut_match_temp_335 is not _coconut_sentinel) and (_coconut_match_temp_335 == "0_1"):  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                                _coconut_match_set_name_dtype = _coconut_match_temp_332  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                                _coconut_match_set_name_arng = _coconut_match_temp_333  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_334  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                                _coconut_case_match_check_13 = True  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                        if _coconut_case_match_check_13:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                                dtype = _coconut_match_set_name_dtype  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            if _coconut_match_set_name_arng is not _coconut_sentinel:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                                arng = _coconut_match_set_name_arng  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
                                ch_repr = _coconut_match_set_name_ch_repr  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:




        if _coconut_case_match_check_13 and not (len(ch_splitter(ch_repr)) == 3):  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
            _coconut_case_match_check_13 = False  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
        if _coconut_case_match_check_13:  #463:         match TensorLike(dtype,arng,ch_repr,"0_1") if len(ch_splitter(ch_repr)) == 3:
            return ([DataEdge(a=imdef, b=imdef.__class__(dtype, arng, "RGB", "0_1"), f=lambda a: a, cost=20, name="view {_coconut_format_0} as RGB ".format(_coconut_format_0=(ch_repr))),])  #464:             return [DataEdge(a=imdef,

@to_imagedef  #470: @to_imagedef
def change_value_range(imdef: 'ImageDef'):  #471: def change_value_range(imdef:ImageDef):
    _coconut_case_match_to_14 = imdef  #472:     case imdef:
    _coconut_case_match_check_14 = False  #472:     case imdef:
    _coconut_match_temp_336 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #472:     case imdef:
    _coconut_case_match_check_14 = True  #472:     case imdef:
    if _coconut_case_match_check_14:  #472:     case imdef:
        _coconut_case_match_check_14 = False  #472:     case imdef:
        if not _coconut_case_match_check_14:  #472:     case imdef:
            _coconut_match_set_name_arng = _coconut_sentinel  #472:     case imdef:
            _coconut_match_set_name_ch_repr = _coconut_sentinel  #472:     case imdef:
            if (_coconut_match_temp_336) and (_coconut.isinstance(_coconut_case_match_to_14, TensorLike)) and (_coconut.len(_coconut_case_match_to_14) >= 4) and (_coconut_case_match_to_14[3] == VR_0_255):  #472:     case imdef:
                _coconut_match_set_name_arng = _coconut_case_match_to_14[1]  #472:     case imdef:
                _coconut_match_set_name_ch_repr = _coconut_case_match_to_14[2]  #472:     case imdef:
                _coconut_match_temp_337 = _coconut.len(_coconut_case_match_to_14) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_14.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {}) and _coconut_case_match_to_14[i] == _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_14.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_14, "__match_args__") else _coconut.len(_coconut_case_match_to_14) == 4  # type: ignore  #472:     case imdef:
                if _coconut_match_temp_337:  #472:     case imdef:
                    _coconut_case_match_check_14 = True  #472:     case imdef:
            if _coconut_case_match_check_14:  #472:     case imdef:
                _coconut_case_match_check_14 = False  #472:     case imdef:
                if not _coconut_case_match_check_14:  #472:     case imdef:
                    if _coconut_case_match_to_14[0] == "float32":  #472:     case imdef:
                        _coconut_case_match_check_14 = True  #472:     case imdef:

                if not _coconut_case_match_check_14:  #472:     case imdef:
                    if _coconut_case_match_to_14[0] == "float64":  #472:     case imdef:
                        _coconut_case_match_check_14 = True  #472:     case imdef:


            if _coconut_case_match_check_14:  #472:     case imdef:
                if _coconut_match_set_name_arng is not _coconut_sentinel:  #472:     case imdef:
                    arng = _coconut_match_set_name_arng  #472:     case imdef:
                if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #472:     case imdef:
                    ch_repr = _coconut_match_set_name_ch_repr  #472:     case imdef:

        if not _coconut_case_match_check_14:  #472:     case imdef:
            if (not _coconut_match_temp_336) and (_coconut.isinstance(_coconut_case_match_to_14, TensorLike)):  #472:     case imdef:
                _coconut_case_match_check_14 = True  #472:     case imdef:
            if _coconut_case_match_check_14:  #472:     case imdef:
                _coconut_case_match_check_14 = False  #472:     case imdef:
                if not _coconut_case_match_check_14:  #472:     case imdef:
                    if _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #472:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #472:     case imdef:
                        _coconut_case_match_check_14 = True  #472:     case imdef:

                if not _coconut_case_match_check_14:  #472:     case imdef:
                    _coconut_match_set_name_arng = _coconut_sentinel  #472:     case imdef:
                    _coconut_match_set_name_ch_repr = _coconut_sentinel  #472:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #472:     case imdef:
                        _coconut_match_temp_338 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #472:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_338, _coconut.tuple):  #472:     case imdef:
                            raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #472:     case imdef:
                        if _coconut.len(_coconut_match_temp_338) < 4:  #472:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_338),))  #472:     case imdef:
                        _coconut_match_temp_339 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_338[0], _coconut_sentinel)  #472:     case imdef:
                        _coconut_match_temp_340 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_338[1], _coconut_sentinel)  #472:     case imdef:
                        _coconut_match_temp_341 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_338[2], _coconut_sentinel)  #472:     case imdef:
                        _coconut_match_temp_342 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_338[3], _coconut_sentinel)  #472:     case imdef:
                        if (_coconut_match_temp_339 is not _coconut_sentinel) and (_coconut_match_temp_340 is not _coconut_sentinel) and (_coconut_match_temp_341 is not _coconut_sentinel) and (_coconut_match_temp_342 is not _coconut_sentinel) and (_coconut_match_temp_342 == VR_0_255):  #472:     case imdef:
                            _coconut_match_set_name_arng = _coconut_match_temp_340  #472:     case imdef:
                            _coconut_match_set_name_ch_repr = _coconut_match_temp_341  #472:     case imdef:
                            _coconut_case_match_check_14 = True  #472:     case imdef:
                    if _coconut_case_match_check_14:  #472:     case imdef:
                        _coconut_case_match_check_14 = False  #472:     case imdef:
                        if not _coconut_case_match_check_14:  #472:     case imdef:
                            if _coconut_match_temp_339 == "float32":  #472:     case imdef:
                                _coconut_case_match_check_14 = True  #472:     case imdef:

                        if not _coconut_case_match_check_14:  #472:     case imdef:
                            if _coconut_match_temp_339 == "float64":  #472:     case imdef:
                                _coconut_case_match_check_14 = True  #472:     case imdef:


                    if _coconut_case_match_check_14:  #472:     case imdef:
                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #472:     case imdef:
                            arng = _coconut_match_set_name_arng  #472:     case imdef:
                        if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #472:     case imdef:
                            ch_repr = _coconut_match_set_name_ch_repr  #472:     case imdef:




    if _coconut_case_match_check_14:  #472:     case imdef:
        return ([DataEdge(a=imdef, b=imdef.__class__(imdef.dtype, arng, ch_repr, VR_0_1), f=lambda a: a / 255.0, cost=len(ch_repr), name="0-255 to 0-1"),])  #474:             return [DataEdge(a=imdef,
    if not _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
        _coconut_match_temp_343 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
        _coconut_case_match_check_14 = True  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
        if _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
            _coconut_case_match_check_14 = False  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
            if not _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                _coconut_match_set_name_arng = _coconut_sentinel  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                _coconut_match_set_name_ch_repr = _coconut_sentinel  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                if (_coconut_match_temp_343) and (_coconut.isinstance(_coconut_case_match_to_14, TensorLike)) and (_coconut.len(_coconut_case_match_to_14) >= 4) and (_coconut_case_match_to_14[3] == VR_0_1):  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                    _coconut_match_set_name_arng = _coconut_case_match_to_14[1]  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                    _coconut_match_set_name_ch_repr = _coconut_case_match_to_14[2]  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                    _coconut_match_temp_344 = _coconut.len(_coconut_case_match_to_14) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_14.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {}) and _coconut_case_match_to_14[i] == _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_14.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_14, "__match_args__") else _coconut.len(_coconut_case_match_to_14) == 4  # type: ignore  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                    if _coconut_match_temp_344:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                        _coconut_case_match_check_14 = True  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                if _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                    _coconut_case_match_check_14 = False  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                    if not _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                        if _coconut_case_match_to_14[0] == "float32":  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            _coconut_case_match_check_14 = True  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):

                    if not _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                        if _coconut_case_match_to_14[0] == "float64":  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            _coconut_case_match_check_14 = True  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):


                if _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                    if _coconut_match_set_name_arng is not _coconut_sentinel:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                        arng = _coconut_match_set_name_arng  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                    if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                        ch_repr = _coconut_match_set_name_ch_repr  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):

            if not _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                if (not _coconut_match_temp_343) and (_coconut.isinstance(_coconut_case_match_to_14, TensorLike)):  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                    _coconut_case_match_check_14 = True  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                if _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                    _coconut_case_match_check_14 = False  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                    if not _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                        if _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            _coconut_case_match_check_14 = True  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):

                    if not _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                        _coconut_match_set_name_arng = _coconut_sentinel  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                        _coconut_match_set_name_ch_repr = _coconut_sentinel  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                        if not _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            _coconut_match_temp_345 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            if not _coconut.isinstance(_coconut_match_temp_345, _coconut.tuple):  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                                raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            if _coconut.len(_coconut_match_temp_345) < 4:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_345),))  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            _coconut_match_temp_346 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_345[0], _coconut_sentinel)  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            _coconut_match_temp_347 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_345[1], _coconut_sentinel)  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            _coconut_match_temp_348 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_345[2], _coconut_sentinel)  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            _coconut_match_temp_349 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_345[3], _coconut_sentinel)  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            if (_coconut_match_temp_346 is not _coconut_sentinel) and (_coconut_match_temp_347 is not _coconut_sentinel) and (_coconut_match_temp_348 is not _coconut_sentinel) and (_coconut_match_temp_349 is not _coconut_sentinel) and (_coconut_match_temp_349 == VR_0_1):  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                                _coconut_match_set_name_arng = _coconut_match_temp_347  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                                _coconut_match_set_name_ch_repr = _coconut_match_temp_348  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                                _coconut_case_match_check_14 = True  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                        if _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            _coconut_case_match_check_14 = False  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            if not _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                                if _coconut_match_temp_346 == "float32":  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                                    _coconut_case_match_check_14 = True  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):

                            if not _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                                if _coconut_match_temp_346 == "float64":  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                                    _coconut_case_match_check_14 = True  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):


                        if _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            if _coconut_match_set_name_arng is not _coconut_sentinel:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                                arng = _coconut_match_set_name_arng  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                            if _coconut_match_set_name_ch_repr is not _coconut_sentinel:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
                                ch_repr = _coconut_match_set_name_ch_repr  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):




        if _coconut_case_match_check_14:  #480:         match TensorLike("float32" or "float64",arng,ch_repr,==VR_0_1):
            return ([DataEdge(a=imdef, b=imdef.__class__(imdef.dtype, arng, ch_repr, VR_0_255), f=lambda a: a * 255.0, cost=len(ch_repr), name="0-1 to 0-255"),])  #481:             return [DataEdge(a=imdef,
    return ([])  #487:     return []


def xyza_to_rgba(xyza):  #489: def xyza_to_rgba(xyza):
    xyz = xyza[:3]  #490:     xyz = xyza[:3]
    a = xyza[[3,]]  #491:     a = xyza[[3]]
    rgb = (xyz + 1) / 2  #492:     rgb = (xyz+1)/2
    return (np.concatenate((rgb, a), axis=0))  #493:     return np.concatenate((rgb,a),axis=0)

def xyz_to_rgb(xyz):  #494: def xyz_to_rgb(xyz):
    return ((xyz + 1) / 2)  #495:     return (xyz+1)/2

def rgb_to_xyz(rgb):  #496: def rgb_to_xyz(rgb):
    return ((rgb * 2) - 1)  #497:     return (rgb*2)-1

def rgba_to_xyza(rgba):  #498: def rgba_to_xyza(rgba):
    rgb = rgba[:3]  #499:     rgb = rgba[:3]
    a = rgba[[3,]]  #500:     a = rgba[[3]]
    xyz = (rgb * 2) - 1  #501:     xyz = (rgb*2)-1
    return (np.concatenate((xyz, a), axis=0))  #502:     return np.concatenate((xyz,a),axis=0)


def rule_xyz_to_rgb(imdef):  #504: def rule_xyz_to_rgb(imdef):
    _coconut_case_match_to_15 = imdef  #505:     case imdef:
    _coconut_case_match_check_15 = False  #505:     case imdef:
    _coconut_match_temp_350 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #505:     case imdef:
    _coconut_case_match_check_15 = True  #505:     case imdef:
    if _coconut_case_match_check_15:  #505:     case imdef:
        _coconut_case_match_check_15 = False  #505:     case imdef:
        if not _coconut_case_match_check_15:  #505:     case imdef:
            _coconut_match_set_name_meta = _coconut_sentinel  #505:     case imdef:
            if (_coconut_match_temp_350) and (_coconut.isinstance(_coconut_case_match_to_15, ImageDef)) and (_coconut.len(_coconut_case_match_to_15) >= 2):  #505:     case imdef:
                _coconut_match_temp_351 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #505:     case imdef:
                _coconut_match_set_name_meta = _coconut_case_match_to_15[1]  #505:     case imdef:
                _coconut_match_temp_358 = _coconut.len(_coconut_case_match_to_15) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_15.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_15, "_coconut_data_defaults", {}) and _coconut_case_match_to_15[i] == _coconut.getattr(_coconut_case_match_to_15, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_15.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_15, "__match_args__") else _coconut.len(_coconut_case_match_to_15) == 2  # type: ignore  #505:     case imdef:
                if _coconut_match_temp_358:  #505:     case imdef:
                    _coconut_case_match_check_15 = True  #505:     case imdef:
            if _coconut_case_match_check_15:  #505:     case imdef:
                _coconut_case_match_check_15 = False  #505:     case imdef:
                if not _coconut_case_match_check_15:  #505:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #505:     case imdef:
                    if (_coconut_match_temp_351) and (_coconut.isinstance(_coconut_case_match_to_15[0], Numpy)) and (_coconut.len(_coconut_case_match_to_15[0]) >= 4) and (_coconut_case_match_to_15[0][1] == "CHW") and (_coconut_case_match_to_15[0][2] == "XYZA") and (_coconut_case_match_to_15[0][3] == "-1_1"):  #505:     case imdef:
                        _coconut_match_set_name_dtype = _coconut_case_match_to_15[0][0]  #505:     case imdef:
                        _coconut_match_temp_352 = _coconut.len(_coconut_case_match_to_15[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_15[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_15[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_15[0][i] == _coconut.getattr(_coconut_case_match_to_15[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_15[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_15[0], "__match_args__") else _coconut.len(_coconut_case_match_to_15[0]) == 4  # type: ignore  #505:     case imdef:
                        if _coconut_match_temp_352:  #505:     case imdef:
                            _coconut_case_match_check_15 = True  #505:     case imdef:
                    if _coconut_case_match_check_15:  #505:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #505:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #505:     case imdef:

                if not _coconut_case_match_check_15:  #505:     case imdef:
                    if (not _coconut_match_temp_351) and (_coconut.isinstance(_coconut_case_match_to_15[0], Numpy)):  #505:     case imdef:
                        _coconut_case_match_check_15 = True  #505:     case imdef:
                    if _coconut_case_match_check_15:  #505:     case imdef:
                        _coconut_case_match_check_15 = False  #505:     case imdef:
                        if not _coconut_case_match_check_15:  #505:     case imdef:
                            if _coconut.type(_coconut_case_match_to_15[0]) in _coconut_self_match_types:  #505:     case imdef:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #505:     case imdef:
                                _coconut_case_match_check_15 = True  #505:     case imdef:

                        if not _coconut_case_match_check_15:  #505:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #505:     case imdef:
                            if not _coconut.type(_coconut_case_match_to_15[0]) in _coconut_self_match_types:  #505:     case imdef:
                                _coconut_match_temp_353 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #505:     case imdef:
                                if not _coconut.isinstance(_coconut_match_temp_353, _coconut.tuple):  #505:     case imdef:
                                    raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #505:     case imdef:
                                if _coconut.len(_coconut_match_temp_353) < 4:  #505:     case imdef:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_353),))  #505:     case imdef:
                                _coconut_match_temp_354 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_353[0], _coconut_sentinel)  #505:     case imdef:
                                _coconut_match_temp_355 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_353[1], _coconut_sentinel)  #505:     case imdef:
                                _coconut_match_temp_356 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_353[2], _coconut_sentinel)  #505:     case imdef:
                                _coconut_match_temp_357 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_353[3], _coconut_sentinel)  #505:     case imdef:
                                if (_coconut_match_temp_354 is not _coconut_sentinel) and (_coconut_match_temp_355 is not _coconut_sentinel) and (_coconut_match_temp_355 == "CHW") and (_coconut_match_temp_356 is not _coconut_sentinel) and (_coconut_match_temp_356 == "XYZA") and (_coconut_match_temp_357 is not _coconut_sentinel) and (_coconut_match_temp_357 == "-1_1"):  #505:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_match_temp_354  #505:     case imdef:
                                    _coconut_case_match_check_15 = True  #505:     case imdef:
                            if _coconut_case_match_check_15:  #505:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #505:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #505:     case imdef:




            if _coconut_case_match_check_15:  #505:     case imdef:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #505:     case imdef:
                    meta = _coconut_match_set_name_meta  #505:     case imdef:

        if not _coconut_case_match_check_15:  #505:     case imdef:
            if (not _coconut_match_temp_350) and (_coconut.isinstance(_coconut_case_match_to_15, ImageDef)):  #505:     case imdef:
                _coconut_case_match_check_15 = True  #505:     case imdef:
            if _coconut_case_match_check_15:  #505:     case imdef:
                _coconut_case_match_check_15 = False  #505:     case imdef:
                if not _coconut_case_match_check_15:  #505:     case imdef:
                    if _coconut.type(_coconut_case_match_to_15) in _coconut_self_match_types:  #505:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #505:     case imdef:
                        _coconut_case_match_check_15 = True  #505:     case imdef:

                if not _coconut_case_match_check_15:  #505:     case imdef:
                    _coconut_match_set_name_meta = _coconut_sentinel  #505:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_15) in _coconut_self_match_types:  #505:     case imdef:
                        _coconut_match_temp_359 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #505:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_359, _coconut.tuple):  #505:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #505:     case imdef:
                        if _coconut.len(_coconut_match_temp_359) < 2:  #505:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_359),))  #505:     case imdef:
                        _coconut_match_temp_360 = _coconut.getattr(_coconut_case_match_to_15, _coconut_match_temp_359[0], _coconut_sentinel)  #505:     case imdef:
                        _coconut_match_temp_368 = _coconut.getattr(_coconut_case_match_to_15, _coconut_match_temp_359[1], _coconut_sentinel)  #505:     case imdef:
                        if (_coconut_match_temp_360 is not _coconut_sentinel) and (_coconut_match_temp_368 is not _coconut_sentinel):  #505:     case imdef:
                            _coconut_match_temp_361 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #505:     case imdef:
                            _coconut_match_set_name_meta = _coconut_match_temp_368  #505:     case imdef:
                            _coconut_case_match_check_15 = True  #505:     case imdef:
                    if _coconut_case_match_check_15:  #505:     case imdef:
                        _coconut_case_match_check_15 = False  #505:     case imdef:
                        if not _coconut_case_match_check_15:  #505:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #505:     case imdef:
                            if (_coconut_match_temp_361) and (_coconut.isinstance(_coconut_match_temp_360, Numpy)) and (_coconut.len(_coconut_match_temp_360) >= 4) and (_coconut_match_temp_360[1] == "CHW") and (_coconut_match_temp_360[2] == "XYZA") and (_coconut_match_temp_360[3] == "-1_1"):  #505:     case imdef:
                                _coconut_match_set_name_dtype = _coconut_match_temp_360[0]  #505:     case imdef:
                                _coconut_match_temp_362 = _coconut.len(_coconut_match_temp_360) <= _coconut.max(4, _coconut.len(_coconut_match_temp_360.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_360, "_coconut_data_defaults", {}) and _coconut_match_temp_360[i] == _coconut.getattr(_coconut_match_temp_360, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_360.__match_args__))) if _coconut.hasattr(_coconut_match_temp_360, "__match_args__") else _coconut.len(_coconut_match_temp_360) == 4  # type: ignore  #505:     case imdef:
                                if _coconut_match_temp_362:  #505:     case imdef:
                                    _coconut_case_match_check_15 = True  #505:     case imdef:
                            if _coconut_case_match_check_15:  #505:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #505:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #505:     case imdef:

                        if not _coconut_case_match_check_15:  #505:     case imdef:
                            if (not _coconut_match_temp_361) and (_coconut.isinstance(_coconut_match_temp_360, Numpy)):  #505:     case imdef:
                                _coconut_case_match_check_15 = True  #505:     case imdef:
                            if _coconut_case_match_check_15:  #505:     case imdef:
                                _coconut_case_match_check_15 = False  #505:     case imdef:
                                if not _coconut_case_match_check_15:  #505:     case imdef:
                                    if _coconut.type(_coconut_match_temp_360) in _coconut_self_match_types:  #505:     case imdef:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #505:     case imdef:
                                        _coconut_case_match_check_15 = True  #505:     case imdef:

                                if not _coconut_case_match_check_15:  #505:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_sentinel  #505:     case imdef:
                                    if not _coconut.type(_coconut_match_temp_360) in _coconut_self_match_types:  #505:     case imdef:
                                        _coconut_match_temp_363 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #505:     case imdef:
                                        if not _coconut.isinstance(_coconut_match_temp_363, _coconut.tuple):  #505:     case imdef:
                                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #505:     case imdef:
                                        if _coconut.len(_coconut_match_temp_363) < 4:  #505:     case imdef:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_363),))  #505:     case imdef:
                                        _coconut_match_temp_364 = _coconut.getattr(_coconut_match_temp_360, _coconut_match_temp_363[0], _coconut_sentinel)  #505:     case imdef:
                                        _coconut_match_temp_365 = _coconut.getattr(_coconut_match_temp_360, _coconut_match_temp_363[1], _coconut_sentinel)  #505:     case imdef:
                                        _coconut_match_temp_366 = _coconut.getattr(_coconut_match_temp_360, _coconut_match_temp_363[2], _coconut_sentinel)  #505:     case imdef:
                                        _coconut_match_temp_367 = _coconut.getattr(_coconut_match_temp_360, _coconut_match_temp_363[3], _coconut_sentinel)  #505:     case imdef:
                                        if (_coconut_match_temp_364 is not _coconut_sentinel) and (_coconut_match_temp_365 is not _coconut_sentinel) and (_coconut_match_temp_365 == "CHW") and (_coconut_match_temp_366 is not _coconut_sentinel) and (_coconut_match_temp_366 == "XYZA") and (_coconut_match_temp_367 is not _coconut_sentinel) and (_coconut_match_temp_367 == "-1_1"):  #505:     case imdef:
                                            _coconut_match_set_name_dtype = _coconut_match_temp_364  #505:     case imdef:
                                            _coconut_case_match_check_15 = True  #505:     case imdef:
                                    if _coconut_case_match_check_15:  #505:     case imdef:
                                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #505:     case imdef:
                                            dtype = _coconut_match_set_name_dtype  #505:     case imdef:




                    if _coconut_case_match_check_15:  #505:     case imdef:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #505:     case imdef:
                            meta = _coconut_match_set_name_meta  #505:     case imdef:




    if _coconut_case_match_check_15:  #505:     case imdef:
        return ([(xyza_to_rgba, ImageDef(Numpy(dtype, "CHW", "RGBA", VR_0_1), meta), 2, "xyza_to_rgba"),])  #507:             return [
    if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
        _coconut_match_temp_369 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
        _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
        if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
            _coconut_case_match_check_15 = False  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
            if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                if (_coconut_match_temp_369) and (_coconut.isinstance(_coconut_case_match_to_15, ImageDef)) and (_coconut.len(_coconut_case_match_to_15) >= 2):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                    _coconut_match_temp_370 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_15[1]  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                    _coconut_match_temp_377 = _coconut.len(_coconut_case_match_to_15) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_15.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_15, "_coconut_data_defaults", {}) and _coconut_case_match_to_15[i] == _coconut.getattr(_coconut_case_match_to_15, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_15.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_15, "__match_args__") else _coconut.len(_coconut_case_match_to_15) == 2  # type: ignore  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                    if _coconut_match_temp_377:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                        _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                    _coconut_case_match_check_15 = False  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                    if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                        _coconut_match_set_name_dtype = _coconut_sentinel  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                        if (_coconut_match_temp_370) and (_coconut.isinstance(_coconut_case_match_to_15[0], Numpy)) and (_coconut.len(_coconut_case_match_to_15[0]) >= 4) and (_coconut_case_match_to_15[0][1] == "CHW") and (_coconut_case_match_to_15[0][2] == "XYZ") and (_coconut_case_match_to_15[0][3] == "-1_1"):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            _coconut_match_set_name_dtype = _coconut_case_match_to_15[0][0]  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            _coconut_match_temp_371 = _coconut.len(_coconut_case_match_to_15[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_15[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_15[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_15[0][i] == _coconut.getattr(_coconut_case_match_to_15[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_15[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_15[0], "__match_args__") else _coconut.len(_coconut_case_match_to_15[0]) == 4  # type: ignore  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            if _coconut_match_temp_371:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                        if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                dtype = _coconut_match_set_name_dtype  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):

                    if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                        if (not _coconut_match_temp_370) and (_coconut.isinstance(_coconut_case_match_to_15[0], Numpy)):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                        if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            _coconut_case_match_check_15 = False  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                if _coconut.type(_coconut_case_match_to_15[0]) in _coconut_self_match_types:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):

                            if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                if not _coconut.type(_coconut_case_match_to_15[0]) in _coconut_self_match_types:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_372 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_372, _coconut.tuple):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    if _coconut.len(_coconut_match_temp_372) < 4:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_372),))  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_373 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_372[0], _coconut_sentinel)  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_374 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_372[1], _coconut_sentinel)  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_375 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_372[2], _coconut_sentinel)  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_376 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_372[3], _coconut_sentinel)  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    if (_coconut_match_temp_373 is not _coconut_sentinel) and (_coconut_match_temp_374 is not _coconut_sentinel) and (_coconut_match_temp_374 == "CHW") and (_coconut_match_temp_375 is not _coconut_sentinel) and (_coconut_match_temp_375 == "XYZ") and (_coconut_match_temp_376 is not _coconut_sentinel) and (_coconut_match_temp_376 == "-1_1"):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                        _coconut_match_set_name_dtype = _coconut_match_temp_373  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                        _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                        dtype = _coconut_match_set_name_dtype  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):




                if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                        meta = _coconut_match_set_name_meta  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):

            if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                if (not _coconut_match_temp_369) and (_coconut.isinstance(_coconut_case_match_to_15, ImageDef)):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                    _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                    _coconut_case_match_check_15 = False  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                    if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                        if _coconut.type(_coconut_case_match_to_15) in _coconut_self_match_types:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):

                    if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                        if not _coconut.type(_coconut_case_match_to_15) in _coconut_self_match_types:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            _coconut_match_temp_378 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            if not _coconut.isinstance(_coconut_match_temp_378, _coconut.tuple):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            if _coconut.len(_coconut_match_temp_378) < 2:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_378),))  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            _coconut_match_temp_379 = _coconut.getattr(_coconut_case_match_to_15, _coconut_match_temp_378[0], _coconut_sentinel)  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            _coconut_match_temp_387 = _coconut.getattr(_coconut_case_match_to_15, _coconut_match_temp_378[1], _coconut_sentinel)  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            if (_coconut_match_temp_379 is not _coconut_sentinel) and (_coconut_match_temp_387 is not _coconut_sentinel):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                _coconut_match_temp_380 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_387  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                        if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            _coconut_case_match_check_15 = False  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                if (_coconut_match_temp_380) and (_coconut.isinstance(_coconut_match_temp_379, Numpy)) and (_coconut.len(_coconut_match_temp_379) >= 4) and (_coconut_match_temp_379[1] == "CHW") and (_coconut_match_temp_379[2] == "XYZ") and (_coconut_match_temp_379[3] == "-1_1"):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    _coconut_match_set_name_dtype = _coconut_match_temp_379[0]  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_381 = _coconut.len(_coconut_match_temp_379) <= _coconut.max(4, _coconut.len(_coconut_match_temp_379.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_379, "_coconut_data_defaults", {}) and _coconut_match_temp_379[i] == _coconut.getattr(_coconut_match_temp_379, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_379.__match_args__))) if _coconut.hasattr(_coconut_match_temp_379, "__match_args__") else _coconut.len(_coconut_match_temp_379) == 4  # type: ignore  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    if _coconut_match_temp_381:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                        _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                        dtype = _coconut_match_set_name_dtype  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):

                            if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                if (not _coconut_match_temp_380) and (_coconut.isinstance(_coconut_match_temp_379, Numpy)):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    _coconut_case_match_check_15 = False  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                    if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                        if _coconut.type(_coconut_match_temp_379) in _coconut_self_match_types:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                            _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):

                                    if not _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                        _coconut_match_set_name_dtype = _coconut_sentinel  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                        if not _coconut.type(_coconut_match_temp_379) in _coconut_self_match_types:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                            _coconut_match_temp_382 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_382, _coconut.tuple):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                            if _coconut.len(_coconut_match_temp_382) < 4:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_382),))  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                            _coconut_match_temp_383 = _coconut.getattr(_coconut_match_temp_379, _coconut_match_temp_382[0], _coconut_sentinel)  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                            _coconut_match_temp_384 = _coconut.getattr(_coconut_match_temp_379, _coconut_match_temp_382[1], _coconut_sentinel)  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                            _coconut_match_temp_385 = _coconut.getattr(_coconut_match_temp_379, _coconut_match_temp_382[2], _coconut_sentinel)  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                            _coconut_match_temp_386 = _coconut.getattr(_coconut_match_temp_379, _coconut_match_temp_382[3], _coconut_sentinel)  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                            if (_coconut_match_temp_383 is not _coconut_sentinel) and (_coconut_match_temp_384 is not _coconut_sentinel) and (_coconut_match_temp_384 == "CHW") and (_coconut_match_temp_385 is not _coconut_sentinel) and (_coconut_match_temp_385 == "XYZ") and (_coconut_match_temp_386 is not _coconut_sentinel) and (_coconut_match_temp_386 == "-1_1"):  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                                _coconut_match_set_name_dtype = _coconut_match_temp_383  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                                _coconut_case_match_check_15 = True  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                        if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                                dtype = _coconut_match_set_name_dtype  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):




                        if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
                                meta = _coconut_match_set_name_meta  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):




        if _coconut_case_match_check_15:  #510:         match ImageDef(Numpy(dtype,"CHW","XYZ","-1_1"),meta):
            return ([(xyz_to_rgb, ImageDef(Numpy(dtype, "CHW", "RGB", VR_0_1), meta), 2, "xyz_to_rgb"),])  #511:             return [
    if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
        _coconut_match_temp_388 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
        _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
        if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
            _coconut_case_match_check_15 = False  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
            if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                if (_coconut_match_temp_388) and (_coconut.isinstance(_coconut_case_match_to_15, ImageDef)) and (_coconut.len(_coconut_case_match_to_15) >= 2):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                    _coconut_match_temp_389 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_15[1]  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                    _coconut_match_temp_396 = _coconut.len(_coconut_case_match_to_15) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_15.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_15, "_coconut_data_defaults", {}) and _coconut_case_match_to_15[i] == _coconut.getattr(_coconut_case_match_to_15, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_15.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_15, "__match_args__") else _coconut.len(_coconut_case_match_to_15) == 2  # type: ignore  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                    if _coconut_match_temp_396:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                        _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                    _coconut_case_match_check_15 = False  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                    if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                        _coconut_match_set_name_dtype = _coconut_sentinel  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                        if (_coconut_match_temp_389) and (_coconut.isinstance(_coconut_case_match_to_15[0], Numpy)) and (_coconut.len(_coconut_case_match_to_15[0]) >= 4) and (_coconut_case_match_to_15[0][1] == "CHW") and (_coconut_case_match_to_15[0][2] == "RGBA") and (_coconut_case_match_to_15[0][3] == VR_0_1):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            _coconut_match_set_name_dtype = _coconut_case_match_to_15[0][0]  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            _coconut_match_temp_390 = _coconut.len(_coconut_case_match_to_15[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_15[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_15[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_15[0][i] == _coconut.getattr(_coconut_case_match_to_15[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_15[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_15[0], "__match_args__") else _coconut.len(_coconut_case_match_to_15[0]) == 4  # type: ignore  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            if _coconut_match_temp_390:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                        if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                dtype = _coconut_match_set_name_dtype  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):

                    if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                        if (not _coconut_match_temp_389) and (_coconut.isinstance(_coconut_case_match_to_15[0], Numpy)):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                        if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            _coconut_case_match_check_15 = False  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                if _coconut.type(_coconut_case_match_to_15[0]) in _coconut_self_match_types:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):

                            if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                if not _coconut.type(_coconut_case_match_to_15[0]) in _coconut_self_match_types:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_391 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_391, _coconut.tuple):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    if _coconut.len(_coconut_match_temp_391) < 4:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_391),))  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_392 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_391[0], _coconut_sentinel)  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_393 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_391[1], _coconut_sentinel)  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_394 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_391[2], _coconut_sentinel)  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_395 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_391[3], _coconut_sentinel)  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    if (_coconut_match_temp_392 is not _coconut_sentinel) and (_coconut_match_temp_393 is not _coconut_sentinel) and (_coconut_match_temp_393 == "CHW") and (_coconut_match_temp_394 is not _coconut_sentinel) and (_coconut_match_temp_394 == "RGBA") and (_coconut_match_temp_395 is not _coconut_sentinel) and (_coconut_match_temp_395 == VR_0_1):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                        _coconut_match_set_name_dtype = _coconut_match_temp_392  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                        _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                        dtype = _coconut_match_set_name_dtype  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):




                if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                        meta = _coconut_match_set_name_meta  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):

            if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                if (not _coconut_match_temp_388) and (_coconut.isinstance(_coconut_case_match_to_15, ImageDef)):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                    _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                    _coconut_case_match_check_15 = False  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                    if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                        if _coconut.type(_coconut_case_match_to_15) in _coconut_self_match_types:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):

                    if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                        if not _coconut.type(_coconut_case_match_to_15) in _coconut_self_match_types:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            _coconut_match_temp_397 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            if not _coconut.isinstance(_coconut_match_temp_397, _coconut.tuple):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            if _coconut.len(_coconut_match_temp_397) < 2:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_397),))  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            _coconut_match_temp_398 = _coconut.getattr(_coconut_case_match_to_15, _coconut_match_temp_397[0], _coconut_sentinel)  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            _coconut_match_temp_406 = _coconut.getattr(_coconut_case_match_to_15, _coconut_match_temp_397[1], _coconut_sentinel)  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            if (_coconut_match_temp_398 is not _coconut_sentinel) and (_coconut_match_temp_406 is not _coconut_sentinel):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                _coconut_match_temp_399 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_406  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                        if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            _coconut_case_match_check_15 = False  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                if (_coconut_match_temp_399) and (_coconut.isinstance(_coconut_match_temp_398, Numpy)) and (_coconut.len(_coconut_match_temp_398) >= 4) and (_coconut_match_temp_398[1] == "CHW") and (_coconut_match_temp_398[2] == "RGBA") and (_coconut_match_temp_398[3] == VR_0_1):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_set_name_dtype = _coconut_match_temp_398[0]  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_400 = _coconut.len(_coconut_match_temp_398) <= _coconut.max(4, _coconut.len(_coconut_match_temp_398.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_398, "_coconut_data_defaults", {}) and _coconut_match_temp_398[i] == _coconut.getattr(_coconut_match_temp_398, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_398.__match_args__))) if _coconut.hasattr(_coconut_match_temp_398, "__match_args__") else _coconut.len(_coconut_match_temp_398) == 4  # type: ignore  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    if _coconut_match_temp_400:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                        _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                        dtype = _coconut_match_set_name_dtype  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):

                            if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                if (not _coconut_match_temp_399) and (_coconut.isinstance(_coconut_match_temp_398, Numpy)):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    _coconut_case_match_check_15 = False  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                    if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                        if _coconut.type(_coconut_match_temp_398) in _coconut_self_match_types:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                            _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):

                                    if not _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                        _coconut_match_set_name_dtype = _coconut_sentinel  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                        if not _coconut.type(_coconut_match_temp_398) in _coconut_self_match_types:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                            _coconut_match_temp_401 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_401, _coconut.tuple):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                            if _coconut.len(_coconut_match_temp_401) < 4:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_401),))  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                            _coconut_match_temp_402 = _coconut.getattr(_coconut_match_temp_398, _coconut_match_temp_401[0], _coconut_sentinel)  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                            _coconut_match_temp_403 = _coconut.getattr(_coconut_match_temp_398, _coconut_match_temp_401[1], _coconut_sentinel)  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                            _coconut_match_temp_404 = _coconut.getattr(_coconut_match_temp_398, _coconut_match_temp_401[2], _coconut_sentinel)  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                            _coconut_match_temp_405 = _coconut.getattr(_coconut_match_temp_398, _coconut_match_temp_401[3], _coconut_sentinel)  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                            if (_coconut_match_temp_402 is not _coconut_sentinel) and (_coconut_match_temp_403 is not _coconut_sentinel) and (_coconut_match_temp_403 == "CHW") and (_coconut_match_temp_404 is not _coconut_sentinel) and (_coconut_match_temp_404 == "RGBA") and (_coconut_match_temp_405 is not _coconut_sentinel) and (_coconut_match_temp_405 == VR_0_1):  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                                _coconut_match_set_name_dtype = _coconut_match_temp_402  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                                _coconut_case_match_check_15 = True  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                        if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                                dtype = _coconut_match_set_name_dtype  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):




                        if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
                                meta = _coconut_match_set_name_meta  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):




        if _coconut_case_match_check_15:  #514:         match ImageDef(Numpy(dtype,"CHW","RGBA",==VR_0_1),meta):
            return ([(rgba_to_xyza, ImageDef(Numpy(dtype, "CHW", "XYZA", "-1_1"), meta), 2, "rgba_to_xyza"),])  #515:             return [
    if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
        _coconut_match_temp_407 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
        _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
        if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
            _coconut_case_match_check_15 = False  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
            if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                if (_coconut_match_temp_407) and (_coconut.isinstance(_coconut_case_match_to_15, ImageDef)) and (_coconut.len(_coconut_case_match_to_15) >= 2):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                    _coconut_match_temp_408 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_15[1]  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                    _coconut_match_temp_415 = _coconut.len(_coconut_case_match_to_15) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_15.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_15, "_coconut_data_defaults", {}) and _coconut_case_match_to_15[i] == _coconut.getattr(_coconut_case_match_to_15, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_15.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_15, "__match_args__") else _coconut.len(_coconut_case_match_to_15) == 2  # type: ignore  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                    if _coconut_match_temp_415:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                        _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                    _coconut_case_match_check_15 = False  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                    if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                        _coconut_match_set_name_dtype = _coconut_sentinel  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                        if (_coconut_match_temp_408) and (_coconut.isinstance(_coconut_case_match_to_15[0], Numpy)) and (_coconut.len(_coconut_case_match_to_15[0]) >= 4) and (_coconut_case_match_to_15[0][1] == "CHW") and (_coconut_case_match_to_15[0][2] == "RGB") and (_coconut_case_match_to_15[0][3] == VR_0_1):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            _coconut_match_set_name_dtype = _coconut_case_match_to_15[0][0]  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            _coconut_match_temp_409 = _coconut.len(_coconut_case_match_to_15[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_15[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_15[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_15[0][i] == _coconut.getattr(_coconut_case_match_to_15[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_15[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_15[0], "__match_args__") else _coconut.len(_coconut_case_match_to_15[0]) == 4  # type: ignore  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            if _coconut_match_temp_409:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                        if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                dtype = _coconut_match_set_name_dtype  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):

                    if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                        if (not _coconut_match_temp_408) and (_coconut.isinstance(_coconut_case_match_to_15[0], Numpy)):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                        if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            _coconut_case_match_check_15 = False  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                if _coconut.type(_coconut_case_match_to_15[0]) in _coconut_self_match_types:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):

                            if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                if not _coconut.type(_coconut_case_match_to_15[0]) in _coconut_self_match_types:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_410 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_410, _coconut.tuple):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    if _coconut.len(_coconut_match_temp_410) < 4:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_410),))  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_411 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_410[0], _coconut_sentinel)  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_412 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_410[1], _coconut_sentinel)  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_413 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_410[2], _coconut_sentinel)  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_414 = _coconut.getattr(_coconut_case_match_to_15[0], _coconut_match_temp_410[3], _coconut_sentinel)  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    if (_coconut_match_temp_411 is not _coconut_sentinel) and (_coconut_match_temp_412 is not _coconut_sentinel) and (_coconut_match_temp_412 == "CHW") and (_coconut_match_temp_413 is not _coconut_sentinel) and (_coconut_match_temp_413 == "RGB") and (_coconut_match_temp_414 is not _coconut_sentinel) and (_coconut_match_temp_414 == VR_0_1):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                        _coconut_match_set_name_dtype = _coconut_match_temp_411  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                        _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                        dtype = _coconut_match_set_name_dtype  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):




                if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                        meta = _coconut_match_set_name_meta  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):

            if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                if (not _coconut_match_temp_407) and (_coconut.isinstance(_coconut_case_match_to_15, ImageDef)):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                    _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                    _coconut_case_match_check_15 = False  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                    if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                        if _coconut.type(_coconut_case_match_to_15) in _coconut_self_match_types:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):

                    if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                        if not _coconut.type(_coconut_case_match_to_15) in _coconut_self_match_types:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            _coconut_match_temp_416 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            if not _coconut.isinstance(_coconut_match_temp_416, _coconut.tuple):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            if _coconut.len(_coconut_match_temp_416) < 2:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_416),))  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            _coconut_match_temp_417 = _coconut.getattr(_coconut_case_match_to_15, _coconut_match_temp_416[0], _coconut_sentinel)  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            _coconut_match_temp_425 = _coconut.getattr(_coconut_case_match_to_15, _coconut_match_temp_416[1], _coconut_sentinel)  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            if (_coconut_match_temp_417 is not _coconut_sentinel) and (_coconut_match_temp_425 is not _coconut_sentinel):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                _coconut_match_temp_418 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_425  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                        if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            _coconut_case_match_check_15 = False  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                if (_coconut_match_temp_418) and (_coconut.isinstance(_coconut_match_temp_417, Numpy)) and (_coconut.len(_coconut_match_temp_417) >= 4) and (_coconut_match_temp_417[1] == "CHW") and (_coconut_match_temp_417[2] == "RGB") and (_coconut_match_temp_417[3] == VR_0_1):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    _coconut_match_set_name_dtype = _coconut_match_temp_417[0]  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_419 = _coconut.len(_coconut_match_temp_417) <= _coconut.max(4, _coconut.len(_coconut_match_temp_417.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_417, "_coconut_data_defaults", {}) and _coconut_match_temp_417[i] == _coconut.getattr(_coconut_match_temp_417, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_417.__match_args__))) if _coconut.hasattr(_coconut_match_temp_417, "__match_args__") else _coconut.len(_coconut_match_temp_417) == 4  # type: ignore  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    if _coconut_match_temp_419:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                        _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                        dtype = _coconut_match_set_name_dtype  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):

                            if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                if (not _coconut_match_temp_418) and (_coconut.isinstance(_coconut_match_temp_417, Numpy)):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    _coconut_case_match_check_15 = False  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                    if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                        if _coconut.type(_coconut_match_temp_417) in _coconut_self_match_types:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                            _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):

                                    if not _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                        _coconut_match_set_name_dtype = _coconut_sentinel  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                        if not _coconut.type(_coconut_match_temp_417) in _coconut_self_match_types:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                            _coconut_match_temp_420 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_420, _coconut.tuple):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                            if _coconut.len(_coconut_match_temp_420) < 4:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_420),))  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                            _coconut_match_temp_421 = _coconut.getattr(_coconut_match_temp_417, _coconut_match_temp_420[0], _coconut_sentinel)  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                            _coconut_match_temp_422 = _coconut.getattr(_coconut_match_temp_417, _coconut_match_temp_420[1], _coconut_sentinel)  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                            _coconut_match_temp_423 = _coconut.getattr(_coconut_match_temp_417, _coconut_match_temp_420[2], _coconut_sentinel)  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                            _coconut_match_temp_424 = _coconut.getattr(_coconut_match_temp_417, _coconut_match_temp_420[3], _coconut_sentinel)  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                            if (_coconut_match_temp_421 is not _coconut_sentinel) and (_coconut_match_temp_422 is not _coconut_sentinel) and (_coconut_match_temp_422 == "CHW") and (_coconut_match_temp_423 is not _coconut_sentinel) and (_coconut_match_temp_423 == "RGB") and (_coconut_match_temp_424 is not _coconut_sentinel) and (_coconut_match_temp_424 == VR_0_1):  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                                _coconut_match_set_name_dtype = _coconut_match_temp_421  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                                _coconut_case_match_check_15 = True  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                        if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                                dtype = _coconut_match_set_name_dtype  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):




                        if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
                                meta = _coconut_match_set_name_meta  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):




        if _coconut_case_match_check_15:  #518:         match ImageDef(Numpy(dtype,"CHW","RGB",==VR_0_1),meta):
            return ([(rgb_to_xyz, ImageDef(Numpy(dtype, "CHW", "XYZ", "-1_1"), meta), 2, "rgb_to_xyz"),])  #519:             return [


def b_xyza_to_rgba(xyza):  #523: def b_xyza_to_rgba(xyza):
    xyz = xyza[:, :3]  #524:     xyz = xyza[:,:3]
    a = xyza[:, [3,]]  #525:     a = xyza[:,[3]]
    rgb = (xyz + 1) / 2  #526:     rgb = (xyz+1)/2
    return (np.concatenate((rgb, a), axis=1))  #527:     return np.concatenate((rgb,a),axis=1)

def b_xyz_to_rgb(xyz):  #528: def b_xyz_to_rgb(xyz):
    return ((xyz + 1) / 2)  #529:     return (xyz+1)/2

def b_rgb_to_xyz(rgb):  #530: def b_rgb_to_xyz(rgb):
    return ((rgb * 2) - 1)  #531:     return (rgb*2)-1

def b_rgba_to_xyza(rgba):  #532: def b_rgba_to_xyza(rgba):
    rgb = rgba[:, :3]  #533:     rgb = rgba[:,:3]
    a = rgba[:, [3,]]  #534:     a = rgba[:,[3]]
    xyz = (rgb * 2) - 1  #535:     xyz = (rgb*2)-1
    return (np.concatenate((xyz, a), axis=1))  #536:     return np.concatenate((xyz,a),axis=1)


def rule_batch_xyz_to_rgb(imdef):  #538: def rule_batch_xyz_to_rgb(imdef):
    _coconut_case_match_to_16 = imdef  #539:     case imdef:
    _coconut_case_match_check_16 = False  #539:     case imdef:
    _coconut_match_temp_426 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #539:     case imdef:
    _coconut_case_match_check_16 = True  #539:     case imdef:
    if _coconut_case_match_check_16:  #539:     case imdef:
        _coconut_case_match_check_16 = False  #539:     case imdef:
        if not _coconut_case_match_check_16:  #539:     case imdef:
            _coconut_match_set_name_meta = _coconut_sentinel  #539:     case imdef:
            if (_coconut_match_temp_426) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)) and (_coconut.len(_coconut_case_match_to_16) >= 2):  #539:     case imdef:
                _coconut_match_temp_427 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #539:     case imdef:
                _coconut_match_set_name_meta = _coconut_case_match_to_16[1]  #539:     case imdef:
                _coconut_match_temp_434 = _coconut.len(_coconut_case_match_to_16) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_16.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {}) and _coconut_case_match_to_16[i] == _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_16.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16, "__match_args__") else _coconut.len(_coconut_case_match_to_16) == 2  # type: ignore  #539:     case imdef:
                if _coconut_match_temp_434:  #539:     case imdef:
                    _coconut_case_match_check_16 = True  #539:     case imdef:
            if _coconut_case_match_check_16:  #539:     case imdef:
                _coconut_case_match_check_16 = False  #539:     case imdef:
                if not _coconut_case_match_check_16:  #539:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #539:     case imdef:
                    if (_coconut_match_temp_427) and (_coconut.isinstance(_coconut_case_match_to_16[0], Numpy)) and (_coconut.len(_coconut_case_match_to_16[0]) >= 4) and (_coconut_case_match_to_16[0][1] == "BCHW") and (_coconut_case_match_to_16[0][2] == "XYZA") and (_coconut_case_match_to_16[0][3] == "-1_1"):  #539:     case imdef:
                        _coconut_match_set_name_dtype = _coconut_case_match_to_16[0][0]  #539:     case imdef:
                        _coconut_match_temp_428 = _coconut.len(_coconut_case_match_to_16[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_16[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_16[0][i] == _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_16[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16[0], "__match_args__") else _coconut.len(_coconut_case_match_to_16[0]) == 4  # type: ignore  #539:     case imdef:
                        if _coconut_match_temp_428:  #539:     case imdef:
                            _coconut_case_match_check_16 = True  #539:     case imdef:
                    if _coconut_case_match_check_16:  #539:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #539:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #539:     case imdef:

                if not _coconut_case_match_check_16:  #539:     case imdef:
                    if (not _coconut_match_temp_427) and (_coconut.isinstance(_coconut_case_match_to_16[0], Numpy)):  #539:     case imdef:
                        _coconut_case_match_check_16 = True  #539:     case imdef:
                    if _coconut_case_match_check_16:  #539:     case imdef:
                        _coconut_case_match_check_16 = False  #539:     case imdef:
                        if not _coconut_case_match_check_16:  #539:     case imdef:
                            if _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #539:     case imdef:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #539:     case imdef:
                                _coconut_case_match_check_16 = True  #539:     case imdef:

                        if not _coconut_case_match_check_16:  #539:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #539:     case imdef:
                            if not _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #539:     case imdef:
                                _coconut_match_temp_429 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #539:     case imdef:
                                if not _coconut.isinstance(_coconut_match_temp_429, _coconut.tuple):  #539:     case imdef:
                                    raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #539:     case imdef:
                                if _coconut.len(_coconut_match_temp_429) < 4:  #539:     case imdef:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_429),))  #539:     case imdef:
                                _coconut_match_temp_430 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_429[0], _coconut_sentinel)  #539:     case imdef:
                                _coconut_match_temp_431 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_429[1], _coconut_sentinel)  #539:     case imdef:
                                _coconut_match_temp_432 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_429[2], _coconut_sentinel)  #539:     case imdef:
                                _coconut_match_temp_433 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_429[3], _coconut_sentinel)  #539:     case imdef:
                                if (_coconut_match_temp_430 is not _coconut_sentinel) and (_coconut_match_temp_431 is not _coconut_sentinel) and (_coconut_match_temp_431 == "BCHW") and (_coconut_match_temp_432 is not _coconut_sentinel) and (_coconut_match_temp_432 == "XYZA") and (_coconut_match_temp_433 is not _coconut_sentinel) and (_coconut_match_temp_433 == "-1_1"):  #539:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_match_temp_430  #539:     case imdef:
                                    _coconut_case_match_check_16 = True  #539:     case imdef:
                            if _coconut_case_match_check_16:  #539:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #539:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #539:     case imdef:




            if _coconut_case_match_check_16:  #539:     case imdef:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #539:     case imdef:
                    meta = _coconut_match_set_name_meta  #539:     case imdef:

        if not _coconut_case_match_check_16:  #539:     case imdef:
            if (not _coconut_match_temp_426) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)):  #539:     case imdef:
                _coconut_case_match_check_16 = True  #539:     case imdef:
            if _coconut_case_match_check_16:  #539:     case imdef:
                _coconut_case_match_check_16 = False  #539:     case imdef:
                if not _coconut_case_match_check_16:  #539:     case imdef:
                    if _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #539:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #539:     case imdef:
                        _coconut_case_match_check_16 = True  #539:     case imdef:

                if not _coconut_case_match_check_16:  #539:     case imdef:
                    _coconut_match_set_name_meta = _coconut_sentinel  #539:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #539:     case imdef:
                        _coconut_match_temp_435 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #539:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_435, _coconut.tuple):  #539:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #539:     case imdef:
                        if _coconut.len(_coconut_match_temp_435) < 2:  #539:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_435),))  #539:     case imdef:
                        _coconut_match_temp_436 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_435[0], _coconut_sentinel)  #539:     case imdef:
                        _coconut_match_temp_444 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_435[1], _coconut_sentinel)  #539:     case imdef:
                        if (_coconut_match_temp_436 is not _coconut_sentinel) and (_coconut_match_temp_444 is not _coconut_sentinel):  #539:     case imdef:
                            _coconut_match_temp_437 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #539:     case imdef:
                            _coconut_match_set_name_meta = _coconut_match_temp_444  #539:     case imdef:
                            _coconut_case_match_check_16 = True  #539:     case imdef:
                    if _coconut_case_match_check_16:  #539:     case imdef:
                        _coconut_case_match_check_16 = False  #539:     case imdef:
                        if not _coconut_case_match_check_16:  #539:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #539:     case imdef:
                            if (_coconut_match_temp_437) and (_coconut.isinstance(_coconut_match_temp_436, Numpy)) and (_coconut.len(_coconut_match_temp_436) >= 4) and (_coconut_match_temp_436[1] == "BCHW") and (_coconut_match_temp_436[2] == "XYZA") and (_coconut_match_temp_436[3] == "-1_1"):  #539:     case imdef:
                                _coconut_match_set_name_dtype = _coconut_match_temp_436[0]  #539:     case imdef:
                                _coconut_match_temp_438 = _coconut.len(_coconut_match_temp_436) <= _coconut.max(4, _coconut.len(_coconut_match_temp_436.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_436, "_coconut_data_defaults", {}) and _coconut_match_temp_436[i] == _coconut.getattr(_coconut_match_temp_436, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_436.__match_args__))) if _coconut.hasattr(_coconut_match_temp_436, "__match_args__") else _coconut.len(_coconut_match_temp_436) == 4  # type: ignore  #539:     case imdef:
                                if _coconut_match_temp_438:  #539:     case imdef:
                                    _coconut_case_match_check_16 = True  #539:     case imdef:
                            if _coconut_case_match_check_16:  #539:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #539:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #539:     case imdef:

                        if not _coconut_case_match_check_16:  #539:     case imdef:
                            if (not _coconut_match_temp_437) and (_coconut.isinstance(_coconut_match_temp_436, Numpy)):  #539:     case imdef:
                                _coconut_case_match_check_16 = True  #539:     case imdef:
                            if _coconut_case_match_check_16:  #539:     case imdef:
                                _coconut_case_match_check_16 = False  #539:     case imdef:
                                if not _coconut_case_match_check_16:  #539:     case imdef:
                                    if _coconut.type(_coconut_match_temp_436) in _coconut_self_match_types:  #539:     case imdef:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #539:     case imdef:
                                        _coconut_case_match_check_16 = True  #539:     case imdef:

                                if not _coconut_case_match_check_16:  #539:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_sentinel  #539:     case imdef:
                                    if not _coconut.type(_coconut_match_temp_436) in _coconut_self_match_types:  #539:     case imdef:
                                        _coconut_match_temp_439 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #539:     case imdef:
                                        if not _coconut.isinstance(_coconut_match_temp_439, _coconut.tuple):  #539:     case imdef:
                                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #539:     case imdef:
                                        if _coconut.len(_coconut_match_temp_439) < 4:  #539:     case imdef:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_439),))  #539:     case imdef:
                                        _coconut_match_temp_440 = _coconut.getattr(_coconut_match_temp_436, _coconut_match_temp_439[0], _coconut_sentinel)  #539:     case imdef:
                                        _coconut_match_temp_441 = _coconut.getattr(_coconut_match_temp_436, _coconut_match_temp_439[1], _coconut_sentinel)  #539:     case imdef:
                                        _coconut_match_temp_442 = _coconut.getattr(_coconut_match_temp_436, _coconut_match_temp_439[2], _coconut_sentinel)  #539:     case imdef:
                                        _coconut_match_temp_443 = _coconut.getattr(_coconut_match_temp_436, _coconut_match_temp_439[3], _coconut_sentinel)  #539:     case imdef:
                                        if (_coconut_match_temp_440 is not _coconut_sentinel) and (_coconut_match_temp_441 is not _coconut_sentinel) and (_coconut_match_temp_441 == "BCHW") and (_coconut_match_temp_442 is not _coconut_sentinel) and (_coconut_match_temp_442 == "XYZA") and (_coconut_match_temp_443 is not _coconut_sentinel) and (_coconut_match_temp_443 == "-1_1"):  #539:     case imdef:
                                            _coconut_match_set_name_dtype = _coconut_match_temp_440  #539:     case imdef:
                                            _coconut_case_match_check_16 = True  #539:     case imdef:
                                    if _coconut_case_match_check_16:  #539:     case imdef:
                                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #539:     case imdef:
                                            dtype = _coconut_match_set_name_dtype  #539:     case imdef:




                    if _coconut_case_match_check_16:  #539:     case imdef:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #539:     case imdef:
                            meta = _coconut_match_set_name_meta  #539:     case imdef:




    if _coconut_case_match_check_16:  #539:     case imdef:
        return ([(b_xyza_to_rgba, ImageDef(Numpy(dtype, "BCHW", "RGBA", VR_0_1), meta), 2, "xyza_to_rgba(batch)"),])  #541:             return [
    if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
        _coconut_match_temp_445 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
        _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
        if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
            _coconut_case_match_check_16 = False  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
            if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                if (_coconut_match_temp_445) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)) and (_coconut.len(_coconut_case_match_to_16) >= 2):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                    _coconut_match_temp_446 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_16[1]  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                    _coconut_match_temp_453 = _coconut.len(_coconut_case_match_to_16) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_16.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {}) and _coconut_case_match_to_16[i] == _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_16.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16, "__match_args__") else _coconut.len(_coconut_case_match_to_16) == 2  # type: ignore  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                    if _coconut_match_temp_453:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                        _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                    _coconut_case_match_check_16 = False  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                    if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                        _coconut_match_set_name_dtype = _coconut_sentinel  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                        if (_coconut_match_temp_446) and (_coconut.isinstance(_coconut_case_match_to_16[0], Numpy)) and (_coconut.len(_coconut_case_match_to_16[0]) >= 4) and (_coconut_case_match_to_16[0][1] == "BCHW") and (_coconut_case_match_to_16[0][2] == "XYZ") and (_coconut_case_match_to_16[0][3] == "-1_1"):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            _coconut_match_set_name_dtype = _coconut_case_match_to_16[0][0]  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            _coconut_match_temp_447 = _coconut.len(_coconut_case_match_to_16[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_16[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_16[0][i] == _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_16[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16[0], "__match_args__") else _coconut.len(_coconut_case_match_to_16[0]) == 4  # type: ignore  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            if _coconut_match_temp_447:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                        if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                dtype = _coconut_match_set_name_dtype  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):

                    if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                        if (not _coconut_match_temp_446) and (_coconut.isinstance(_coconut_case_match_to_16[0], Numpy)):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                        if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            _coconut_case_match_check_16 = False  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                if _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):

                            if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                if not _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_448 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_448, _coconut.tuple):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    if _coconut.len(_coconut_match_temp_448) < 4:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_448),))  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_449 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_448[0], _coconut_sentinel)  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_450 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_448[1], _coconut_sentinel)  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_451 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_448[2], _coconut_sentinel)  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_452 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_448[3], _coconut_sentinel)  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    if (_coconut_match_temp_449 is not _coconut_sentinel) and (_coconut_match_temp_450 is not _coconut_sentinel) and (_coconut_match_temp_450 == "BCHW") and (_coconut_match_temp_451 is not _coconut_sentinel) and (_coconut_match_temp_451 == "XYZ") and (_coconut_match_temp_452 is not _coconut_sentinel) and (_coconut_match_temp_452 == "-1_1"):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                        _coconut_match_set_name_dtype = _coconut_match_temp_449  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                        _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                        dtype = _coconut_match_set_name_dtype  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):




                if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                        meta = _coconut_match_set_name_meta  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):

            if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                if (not _coconut_match_temp_445) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                    _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                    _coconut_case_match_check_16 = False  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                    if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                        if _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):

                    if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                        if not _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            _coconut_match_temp_454 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            if not _coconut.isinstance(_coconut_match_temp_454, _coconut.tuple):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            if _coconut.len(_coconut_match_temp_454) < 2:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_454),))  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            _coconut_match_temp_455 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_454[0], _coconut_sentinel)  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            _coconut_match_temp_463 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_454[1], _coconut_sentinel)  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            if (_coconut_match_temp_455 is not _coconut_sentinel) and (_coconut_match_temp_463 is not _coconut_sentinel):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                _coconut_match_temp_456 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_463  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                        if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            _coconut_case_match_check_16 = False  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                if (_coconut_match_temp_456) and (_coconut.isinstance(_coconut_match_temp_455, Numpy)) and (_coconut.len(_coconut_match_temp_455) >= 4) and (_coconut_match_temp_455[1] == "BCHW") and (_coconut_match_temp_455[2] == "XYZ") and (_coconut_match_temp_455[3] == "-1_1"):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    _coconut_match_set_name_dtype = _coconut_match_temp_455[0]  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    _coconut_match_temp_457 = _coconut.len(_coconut_match_temp_455) <= _coconut.max(4, _coconut.len(_coconut_match_temp_455.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_455, "_coconut_data_defaults", {}) and _coconut_match_temp_455[i] == _coconut.getattr(_coconut_match_temp_455, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_455.__match_args__))) if _coconut.hasattr(_coconut_match_temp_455, "__match_args__") else _coconut.len(_coconut_match_temp_455) == 4  # type: ignore  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    if _coconut_match_temp_457:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                        _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                        dtype = _coconut_match_set_name_dtype  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):

                            if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                if (not _coconut_match_temp_456) and (_coconut.isinstance(_coconut_match_temp_455, Numpy)):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    _coconut_case_match_check_16 = False  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                    if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                        if _coconut.type(_coconut_match_temp_455) in _coconut_self_match_types:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                            _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):

                                    if not _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                        _coconut_match_set_name_dtype = _coconut_sentinel  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                        if not _coconut.type(_coconut_match_temp_455) in _coconut_self_match_types:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                            _coconut_match_temp_458 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_458, _coconut.tuple):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                            if _coconut.len(_coconut_match_temp_458) < 4:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_458),))  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                            _coconut_match_temp_459 = _coconut.getattr(_coconut_match_temp_455, _coconut_match_temp_458[0], _coconut_sentinel)  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                            _coconut_match_temp_460 = _coconut.getattr(_coconut_match_temp_455, _coconut_match_temp_458[1], _coconut_sentinel)  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                            _coconut_match_temp_461 = _coconut.getattr(_coconut_match_temp_455, _coconut_match_temp_458[2], _coconut_sentinel)  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                            _coconut_match_temp_462 = _coconut.getattr(_coconut_match_temp_455, _coconut_match_temp_458[3], _coconut_sentinel)  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                            if (_coconut_match_temp_459 is not _coconut_sentinel) and (_coconut_match_temp_460 is not _coconut_sentinel) and (_coconut_match_temp_460 == "BCHW") and (_coconut_match_temp_461 is not _coconut_sentinel) and (_coconut_match_temp_461 == "XYZ") and (_coconut_match_temp_462 is not _coconut_sentinel) and (_coconut_match_temp_462 == "-1_1"):  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                                _coconut_match_set_name_dtype = _coconut_match_temp_459  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                                _coconut_case_match_check_16 = True  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                        if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                                dtype = _coconut_match_set_name_dtype  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):




                        if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
                                meta = _coconut_match_set_name_meta  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):




        if _coconut_case_match_check_16:  #544:         match ImageDef(Numpy(dtype,"BCHW","XYZ","-1_1"),meta):
            return ([(b_xyz_to_rgb, ImageDef(Numpy(dtype, "BCHW", "RGB", VR_0_1), meta), 2, "xyz_to_rgb(batch)"),])  #545:             return [
    if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
        _coconut_match_temp_464 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
        _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
        if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
            _coconut_case_match_check_16 = False  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
            if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                if (_coconut_match_temp_464) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)) and (_coconut.len(_coconut_case_match_to_16) >= 2):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                    _coconut_match_temp_465 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_16[1]  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                    _coconut_match_temp_472 = _coconut.len(_coconut_case_match_to_16) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_16.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {}) and _coconut_case_match_to_16[i] == _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_16.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16, "__match_args__") else _coconut.len(_coconut_case_match_to_16) == 2  # type: ignore  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                    if _coconut_match_temp_472:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                        _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                    _coconut_case_match_check_16 = False  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                    if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                        _coconut_match_set_name_dtype = _coconut_sentinel  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                        if (_coconut_match_temp_465) and (_coconut.isinstance(_coconut_case_match_to_16[0], Numpy)) and (_coconut.len(_coconut_case_match_to_16[0]) >= 4) and (_coconut_case_match_to_16[0][1] == "BCHW") and (_coconut_case_match_to_16[0][2] == "RGBA") and (_coconut_case_match_to_16[0][3] == VR_0_1):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            _coconut_match_set_name_dtype = _coconut_case_match_to_16[0][0]  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            _coconut_match_temp_466 = _coconut.len(_coconut_case_match_to_16[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_16[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_16[0][i] == _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_16[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16[0], "__match_args__") else _coconut.len(_coconut_case_match_to_16[0]) == 4  # type: ignore  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            if _coconut_match_temp_466:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                        if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                dtype = _coconut_match_set_name_dtype  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):

                    if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                        if (not _coconut_match_temp_465) and (_coconut.isinstance(_coconut_case_match_to_16[0], Numpy)):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                        if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            _coconut_case_match_check_16 = False  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                if _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):

                            if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                if not _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_467 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_467, _coconut.tuple):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    if _coconut.len(_coconut_match_temp_467) < 4:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_467),))  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_468 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_467[0], _coconut_sentinel)  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_469 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_467[1], _coconut_sentinel)  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_470 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_467[2], _coconut_sentinel)  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_471 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_467[3], _coconut_sentinel)  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    if (_coconut_match_temp_468 is not _coconut_sentinel) and (_coconut_match_temp_469 is not _coconut_sentinel) and (_coconut_match_temp_469 == "BCHW") and (_coconut_match_temp_470 is not _coconut_sentinel) and (_coconut_match_temp_470 == "RGBA") and (_coconut_match_temp_471 is not _coconut_sentinel) and (_coconut_match_temp_471 == VR_0_1):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                        _coconut_match_set_name_dtype = _coconut_match_temp_468  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                        _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                        dtype = _coconut_match_set_name_dtype  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):




                if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                        meta = _coconut_match_set_name_meta  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):

            if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                if (not _coconut_match_temp_464) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                    _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                    _coconut_case_match_check_16 = False  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                    if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                        if _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):

                    if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                        if not _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            _coconut_match_temp_473 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            if not _coconut.isinstance(_coconut_match_temp_473, _coconut.tuple):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            if _coconut.len(_coconut_match_temp_473) < 2:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_473),))  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            _coconut_match_temp_474 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_473[0], _coconut_sentinel)  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            _coconut_match_temp_482 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_473[1], _coconut_sentinel)  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            if (_coconut_match_temp_474 is not _coconut_sentinel) and (_coconut_match_temp_482 is not _coconut_sentinel):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                _coconut_match_temp_475 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_482  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                        if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            _coconut_case_match_check_16 = False  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                if (_coconut_match_temp_475) and (_coconut.isinstance(_coconut_match_temp_474, Numpy)) and (_coconut.len(_coconut_match_temp_474) >= 4) and (_coconut_match_temp_474[1] == "BCHW") and (_coconut_match_temp_474[2] == "RGBA") and (_coconut_match_temp_474[3] == VR_0_1):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_set_name_dtype = _coconut_match_temp_474[0]  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    _coconut_match_temp_476 = _coconut.len(_coconut_match_temp_474) <= _coconut.max(4, _coconut.len(_coconut_match_temp_474.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_474, "_coconut_data_defaults", {}) and _coconut_match_temp_474[i] == _coconut.getattr(_coconut_match_temp_474, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_474.__match_args__))) if _coconut.hasattr(_coconut_match_temp_474, "__match_args__") else _coconut.len(_coconut_match_temp_474) == 4  # type: ignore  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    if _coconut_match_temp_476:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                        _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                        dtype = _coconut_match_set_name_dtype  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):

                            if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                if (not _coconut_match_temp_475) and (_coconut.isinstance(_coconut_match_temp_474, Numpy)):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    _coconut_case_match_check_16 = False  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                    if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                        if _coconut.type(_coconut_match_temp_474) in _coconut_self_match_types:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                            _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):

                                    if not _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                        _coconut_match_set_name_dtype = _coconut_sentinel  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                        if not _coconut.type(_coconut_match_temp_474) in _coconut_self_match_types:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                            _coconut_match_temp_477 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_477, _coconut.tuple):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                            if _coconut.len(_coconut_match_temp_477) < 4:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_477),))  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                            _coconut_match_temp_478 = _coconut.getattr(_coconut_match_temp_474, _coconut_match_temp_477[0], _coconut_sentinel)  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                            _coconut_match_temp_479 = _coconut.getattr(_coconut_match_temp_474, _coconut_match_temp_477[1], _coconut_sentinel)  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                            _coconut_match_temp_480 = _coconut.getattr(_coconut_match_temp_474, _coconut_match_temp_477[2], _coconut_sentinel)  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                            _coconut_match_temp_481 = _coconut.getattr(_coconut_match_temp_474, _coconut_match_temp_477[3], _coconut_sentinel)  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                            if (_coconut_match_temp_478 is not _coconut_sentinel) and (_coconut_match_temp_479 is not _coconut_sentinel) and (_coconut_match_temp_479 == "BCHW") and (_coconut_match_temp_480 is not _coconut_sentinel) and (_coconut_match_temp_480 == "RGBA") and (_coconut_match_temp_481 is not _coconut_sentinel) and (_coconut_match_temp_481 == VR_0_1):  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                                _coconut_match_set_name_dtype = _coconut_match_temp_478  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                                _coconut_case_match_check_16 = True  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                        if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                                dtype = _coconut_match_set_name_dtype  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):




                        if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
                                meta = _coconut_match_set_name_meta  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):




        if _coconut_case_match_check_16:  #548:         match ImageDef(Numpy(dtype,"BCHW","RGBA",==VR_0_1),meta):
            return ([(b_rgba_to_xyza, ImageDef(Numpy(dtype, "BCHW", "XYZA", "-1_1"), meta), 2, "rgba_to_xyza(batch)"),])  #549:             return [
    if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
        _coconut_match_temp_483 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
        _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
        if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
            _coconut_case_match_check_16 = False  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
            if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                if (_coconut_match_temp_483) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)) and (_coconut.len(_coconut_case_match_to_16) >= 2):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                    _coconut_match_temp_484 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_16[1]  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                    _coconut_match_temp_491 = _coconut.len(_coconut_case_match_to_16) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_16.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {}) and _coconut_case_match_to_16[i] == _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_16.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16, "__match_args__") else _coconut.len(_coconut_case_match_to_16) == 2  # type: ignore  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                    if _coconut_match_temp_491:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                        _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                    _coconut_case_match_check_16 = False  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                    if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                        _coconut_match_set_name_dtype = _coconut_sentinel  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                        if (_coconut_match_temp_484) and (_coconut.isinstance(_coconut_case_match_to_16[0], Numpy)) and (_coconut.len(_coconut_case_match_to_16[0]) >= 4) and (_coconut_case_match_to_16[0][1] == "BCHW") and (_coconut_case_match_to_16[0][2] == "RGB") and (_coconut_case_match_to_16[0][3] == VR_0_1):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            _coconut_match_set_name_dtype = _coconut_case_match_to_16[0][0]  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            _coconut_match_temp_485 = _coconut.len(_coconut_case_match_to_16[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_16[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_16[0][i] == _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_16[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16[0], "__match_args__") else _coconut.len(_coconut_case_match_to_16[0]) == 4  # type: ignore  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            if _coconut_match_temp_485:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                        if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                dtype = _coconut_match_set_name_dtype  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):

                    if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                        if (not _coconut_match_temp_484) and (_coconut.isinstance(_coconut_case_match_to_16[0], Numpy)):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                        if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            _coconut_case_match_check_16 = False  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                if _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):

                            if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                if not _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_486 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_486, _coconut.tuple):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    if _coconut.len(_coconut_match_temp_486) < 4:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_486),))  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_487 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_486[0], _coconut_sentinel)  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_488 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_486[1], _coconut_sentinel)  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_489 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_486[2], _coconut_sentinel)  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_490 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_486[3], _coconut_sentinel)  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    if (_coconut_match_temp_487 is not _coconut_sentinel) and (_coconut_match_temp_488 is not _coconut_sentinel) and (_coconut_match_temp_488 == "BCHW") and (_coconut_match_temp_489 is not _coconut_sentinel) and (_coconut_match_temp_489 == "RGB") and (_coconut_match_temp_490 is not _coconut_sentinel) and (_coconut_match_temp_490 == VR_0_1):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                        _coconut_match_set_name_dtype = _coconut_match_temp_487  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                        _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                        dtype = _coconut_match_set_name_dtype  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):




                if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                        meta = _coconut_match_set_name_meta  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):

            if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                if (not _coconut_match_temp_483) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                    _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                    _coconut_case_match_check_16 = False  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                    if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                        if _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):

                    if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                        if not _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            _coconut_match_temp_492 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            if not _coconut.isinstance(_coconut_match_temp_492, _coconut.tuple):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            if _coconut.len(_coconut_match_temp_492) < 2:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_492),))  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            _coconut_match_temp_493 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_492[0], _coconut_sentinel)  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            _coconut_match_temp_501 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_492[1], _coconut_sentinel)  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            if (_coconut_match_temp_493 is not _coconut_sentinel) and (_coconut_match_temp_501 is not _coconut_sentinel):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                _coconut_match_temp_494 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_501  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                        if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            _coconut_case_match_check_16 = False  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                if (_coconut_match_temp_494) and (_coconut.isinstance(_coconut_match_temp_493, Numpy)) and (_coconut.len(_coconut_match_temp_493) >= 4) and (_coconut_match_temp_493[1] == "BCHW") and (_coconut_match_temp_493[2] == "RGB") and (_coconut_match_temp_493[3] == VR_0_1):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    _coconut_match_set_name_dtype = _coconut_match_temp_493[0]  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    _coconut_match_temp_495 = _coconut.len(_coconut_match_temp_493) <= _coconut.max(4, _coconut.len(_coconut_match_temp_493.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_493, "_coconut_data_defaults", {}) and _coconut_match_temp_493[i] == _coconut.getattr(_coconut_match_temp_493, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_493.__match_args__))) if _coconut.hasattr(_coconut_match_temp_493, "__match_args__") else _coconut.len(_coconut_match_temp_493) == 4  # type: ignore  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    if _coconut_match_temp_495:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                        _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                        dtype = _coconut_match_set_name_dtype  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):

                            if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                if (not _coconut_match_temp_494) and (_coconut.isinstance(_coconut_match_temp_493, Numpy)):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    _coconut_case_match_check_16 = False  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                    if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                        if _coconut.type(_coconut_match_temp_493) in _coconut_self_match_types:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                            _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):

                                    if not _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                        _coconut_match_set_name_dtype = _coconut_sentinel  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                        if not _coconut.type(_coconut_match_temp_493) in _coconut_self_match_types:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                            _coconut_match_temp_496 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_496, _coconut.tuple):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                            if _coconut.len(_coconut_match_temp_496) < 4:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_496),))  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                            _coconut_match_temp_497 = _coconut.getattr(_coconut_match_temp_493, _coconut_match_temp_496[0], _coconut_sentinel)  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                            _coconut_match_temp_498 = _coconut.getattr(_coconut_match_temp_493, _coconut_match_temp_496[1], _coconut_sentinel)  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                            _coconut_match_temp_499 = _coconut.getattr(_coconut_match_temp_493, _coconut_match_temp_496[2], _coconut_sentinel)  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                            _coconut_match_temp_500 = _coconut.getattr(_coconut_match_temp_493, _coconut_match_temp_496[3], _coconut_sentinel)  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                            if (_coconut_match_temp_497 is not _coconut_sentinel) and (_coconut_match_temp_498 is not _coconut_sentinel) and (_coconut_match_temp_498 == "BCHW") and (_coconut_match_temp_499 is not _coconut_sentinel) and (_coconut_match_temp_499 == "RGB") and (_coconut_match_temp_500 is not _coconut_sentinel) and (_coconut_match_temp_500 == VR_0_1):  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                                _coconut_match_set_name_dtype = _coconut_match_temp_497  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                                _coconut_case_match_check_16 = True  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                        if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                                dtype = _coconut_match_set_name_dtype  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):




                        if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
                                meta = _coconut_match_set_name_meta  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):




        if _coconut_case_match_check_16:  #552:         match ImageDef(Numpy(dtype,"BCHW","RGB",==VR_0_1),meta):
            return ([(b_rgb_to_xyz, ImageDef(Numpy(dtype, "BCHW", "XYZ", "-1_1"), meta), 2, "rgb_to_xyz(batch)"),])  #553:             return [




_conversions = [to_PILImages, to_numpy, to_torch, change_dtype, change_arrange, select_channel, drop_channel, en_batch, change_value_range, drop_alpha, to_rgba, drop_meta, de_batch, RGB_to_YCbCr]  #559: _conversions =[


@memoize(1024)  #577: @memoize(1024)
def _edges(imdef):  #578: def _edges(imdef):
    res = []  #579:     res = []
    for f in (_conversions):  #580:     for f in _conversions:
        edges = f(imdef)  #581:         edges = f(imdef)
        if edges is not None:  #582:         if edges is not None:
            res += edges  #583:             res += edges
    return (res)  #584:     return res





@memoize(1024)  #589: @memoize(1024)
def str_to_img_def(query):  #590: def str_to_img_def(query):
    """
    ex1: 'numpy,float32,BCHW,RGB,0_255 | hello,world'
    ex2: 'torch,float32,BCHW,RGBA,0_1'
    ex3: 'image,RGBA,RGBA'
    ex4: 'images,RGB,RGB' => ImageDef(PILImage("RGB","RGB"),{shape:(None,None,3)})
    ex5: 'image,RGBA,RGBA,128:128:3' => ImageDef(PILImage("RGB","RGB"),{shape:(128,128,3)})
    """  #597:     """
    vrs = _coconut.dict((("0_255", VR_0_255), ("0_1", VR_0_1), ("None", VR_None)))  #598:     vrs = {
    query = query.replace(" ", "")  #603:     query = query.replace(" ","")
    def arng_to_shape(arng, ch_repr):  #604:     def arng_to_shape(arng,ch_repr):
        ch = len(ch_splitter(ch_repr))  #605:         ch = len(ch_splitter(ch_repr))
        c_idx = arng.find("C")  #606:         c_idx = arng.find("C")
        shape = [None,] * len(arng)  #607:         shape = [None]*len(arng)
        if c_idx != -1:  #608:         if c_idx != -1:
            shape[c_idx] = ch  #609:             shape[c_idx] = ch
#logger.info(f"{arng},{ch_repr}->{tuple(shape)}")
        return (tuple(shape))  #611:         return tuple(shape)


    def shape_str_to_shape(ss):  #613:     def shape_str_to_shape(ss):
        tokens = ss.split(":")  #614:         tokens = ss.split(":")
        return (tuple([int(t) if t != "None" else None for t in tokens]))  #615:         return tuple([int(t) if t!="None" else None for t in tokens])


    def query_to_data_type(query):  #617:     def query_to_data_type(query):
        _coconut_case_match_to_17 = query.split(",")  #618:         case query.split(","):
        _coconut_case_match_check_17 = False  #618:         case query.split(","):
        _coconut_match_set_name_dtype = _coconut_sentinel  #618:         case query.split(","):
        _coconut_match_set_name_arng = _coconut_sentinel  #618:         case query.split(","):
        _coconut_match_set_name_ch = _coconut_sentinel  #618:         case query.split(","):
        _coconut_match_set_name_vr = _coconut_sentinel  #618:         case query.split(","):
        if (_coconut.isinstance(_coconut_case_match_to_17, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_17) == 5) and (_coconut_case_match_to_17[0] == "numpy"):  #618:         case query.split(","):
            _coconut_match_set_name_dtype = _coconut_case_match_to_17[1]  #618:         case query.split(","):
            _coconut_match_set_name_arng = _coconut_case_match_to_17[2]  #618:         case query.split(","):
            _coconut_match_set_name_ch = _coconut_case_match_to_17[3]  #618:         case query.split(","):
            _coconut_match_set_name_vr = _coconut_case_match_to_17[4]  #618:         case query.split(","):
            _coconut_case_match_check_17 = True  #618:         case query.split(","):
        if _coconut_case_match_check_17:  #618:         case query.split(","):
            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #618:         case query.split(","):
                dtype = _coconut_match_set_name_dtype  #618:         case query.split(","):
            if _coconut_match_set_name_arng is not _coconut_sentinel:  #618:         case query.split(","):
                arng = _coconut_match_set_name_arng  #618:         case query.split(","):
            if _coconut_match_set_name_ch is not _coconut_sentinel:  #618:         case query.split(","):
                ch = _coconut_match_set_name_ch  #618:         case query.split(","):
            if _coconut_match_set_name_vr is not _coconut_sentinel:  #618:         case query.split(","):
                vr = _coconut_match_set_name_vr  #618:         case query.split(","):
        if _coconut_case_match_check_17:  #618:         case query.split(","):
            return (Numpy(dtype, arng, ch, vrs[vr] if vr in vrs else vr), arng_to_shape(arng, ch))  #620:                 return Numpy(dtype,arng,ch,vrs[vr] if vr in vrs else vr),arng_to_shape(arng,ch)
        if not _coconut_case_match_check_17:  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
            _coconut_match_set_name_dtype = _coconut_sentinel  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
            _coconut_match_set_name_arng = _coconut_sentinel  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
            _coconut_match_set_name_ch = _coconut_sentinel  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
            _coconut_match_set_name_vr = _coconut_sentinel  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
            _coconut_match_set_name_shape = _coconut_sentinel  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
            if (_coconut.isinstance(_coconut_case_match_to_17, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_17) == 6) and (_coconut_case_match_to_17[0] == "numpy"):  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                _coconut_match_set_name_dtype = _coconut_case_match_to_17[1]  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                _coconut_match_set_name_arng = _coconut_case_match_to_17[2]  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                _coconut_match_set_name_ch = _coconut_case_match_to_17[3]  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                _coconut_match_set_name_vr = _coconut_case_match_to_17[4]  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                _coconut_match_set_name_shape = _coconut_case_match_to_17[5]  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                _coconut_case_match_check_17 = True  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
            if _coconut_case_match_check_17:  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                    dtype = _coconut_match_set_name_dtype  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                if _coconut_match_set_name_arng is not _coconut_sentinel:  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                    arng = _coconut_match_set_name_arng  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                if _coconut_match_set_name_ch is not _coconut_sentinel:  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                    ch = _coconut_match_set_name_ch  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                if _coconut_match_set_name_vr is not _coconut_sentinel:  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                    vr = _coconut_match_set_name_vr  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                if _coconut_match_set_name_shape is not _coconut_sentinel:  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                    shape = _coconut_match_set_name_shape  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
            if _coconut_case_match_check_17:  #621:             match ["numpy",dtype,arng,ch,vr,shape]:
                return (Numpy(dtype, arng, ch, vrs[vr] if vr in vrs else vr), shape_str_to_shape(shape))  #622:                 return Numpy(dtype,arng,ch,vrs[vr] if vr in vrs else vr),shape_str_to_shape(shape)
        if not _coconut_case_match_check_17:  #623:             match ["torch",dtype,arng,ch,vr]:
            _coconut_match_set_name_dtype = _coconut_sentinel  #623:             match ["torch",dtype,arng,ch,vr]:
            _coconut_match_set_name_arng = _coconut_sentinel  #623:             match ["torch",dtype,arng,ch,vr]:
            _coconut_match_set_name_ch = _coconut_sentinel  #623:             match ["torch",dtype,arng,ch,vr]:
            _coconut_match_set_name_vr = _coconut_sentinel  #623:             match ["torch",dtype,arng,ch,vr]:
            if (_coconut.isinstance(_coconut_case_match_to_17, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_17) == 5) and (_coconut_case_match_to_17[0] == "torch"):  #623:             match ["torch",dtype,arng,ch,vr]:
                _coconut_match_set_name_dtype = _coconut_case_match_to_17[1]  #623:             match ["torch",dtype,arng,ch,vr]:
                _coconut_match_set_name_arng = _coconut_case_match_to_17[2]  #623:             match ["torch",dtype,arng,ch,vr]:
                _coconut_match_set_name_ch = _coconut_case_match_to_17[3]  #623:             match ["torch",dtype,arng,ch,vr]:
                _coconut_match_set_name_vr = _coconut_case_match_to_17[4]  #623:             match ["torch",dtype,arng,ch,vr]:
                _coconut_case_match_check_17 = True  #623:             match ["torch",dtype,arng,ch,vr]:
            if _coconut_case_match_check_17:  #623:             match ["torch",dtype,arng,ch,vr]:
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #623:             match ["torch",dtype,arng,ch,vr]:
                    dtype = _coconut_match_set_name_dtype  #623:             match ["torch",dtype,arng,ch,vr]:
                if _coconut_match_set_name_arng is not _coconut_sentinel:  #623:             match ["torch",dtype,arng,ch,vr]:
                    arng = _coconut_match_set_name_arng  #623:             match ["torch",dtype,arng,ch,vr]:
                if _coconut_match_set_name_ch is not _coconut_sentinel:  #623:             match ["torch",dtype,arng,ch,vr]:
                    ch = _coconut_match_set_name_ch  #623:             match ["torch",dtype,arng,ch,vr]:
                if _coconut_match_set_name_vr is not _coconut_sentinel:  #623:             match ["torch",dtype,arng,ch,vr]:
                    vr = _coconut_match_set_name_vr  #623:             match ["torch",dtype,arng,ch,vr]:
            if _coconut_case_match_check_17:  #623:             match ["torch",dtype,arng,ch,vr]:
                return (Torch(dtype, arng, ch, vrs[vr] if vr in vrs else vr), arng_to_shape(arng, ch))  #624:                 return Torch(dtype,arng,ch,vrs[vr] if vr in vrs else vr),arng_to_shape(arng,ch)
        if not _coconut_case_match_check_17:  #625:             match ["torch",dtype,arng,ch,vr,shape]:
            _coconut_match_set_name_dtype = _coconut_sentinel  #625:             match ["torch",dtype,arng,ch,vr,shape]:
            _coconut_match_set_name_arng = _coconut_sentinel  #625:             match ["torch",dtype,arng,ch,vr,shape]:
            _coconut_match_set_name_ch = _coconut_sentinel  #625:             match ["torch",dtype,arng,ch,vr,shape]:
            _coconut_match_set_name_vr = _coconut_sentinel  #625:             match ["torch",dtype,arng,ch,vr,shape]:
            _coconut_match_set_name_shape = _coconut_sentinel  #625:             match ["torch",dtype,arng,ch,vr,shape]:
            if (_coconut.isinstance(_coconut_case_match_to_17, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_17) == 6) and (_coconut_case_match_to_17[0] == "torch"):  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                _coconut_match_set_name_dtype = _coconut_case_match_to_17[1]  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                _coconut_match_set_name_arng = _coconut_case_match_to_17[2]  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                _coconut_match_set_name_ch = _coconut_case_match_to_17[3]  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                _coconut_match_set_name_vr = _coconut_case_match_to_17[4]  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                _coconut_match_set_name_shape = _coconut_case_match_to_17[5]  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                _coconut_case_match_check_17 = True  #625:             match ["torch",dtype,arng,ch,vr,shape]:
            if _coconut_case_match_check_17:  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                    dtype = _coconut_match_set_name_dtype  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                if _coconut_match_set_name_arng is not _coconut_sentinel:  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                    arng = _coconut_match_set_name_arng  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                if _coconut_match_set_name_ch is not _coconut_sentinel:  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                    ch = _coconut_match_set_name_ch  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                if _coconut_match_set_name_vr is not _coconut_sentinel:  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                    vr = _coconut_match_set_name_vr  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                if _coconut_match_set_name_shape is not _coconut_sentinel:  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                    shape = _coconut_match_set_name_shape  #625:             match ["torch",dtype,arng,ch,vr,shape]:
            if _coconut_case_match_check_17:  #625:             match ["torch",dtype,arng,ch,vr,shape]:
                return (Torch(dtype, arng, ch, vrs[vr] if vr in vrs else vr), shape_str_to_shape(shape))  #626:                 return Torch(dtype,arng,ch,vrs[vr] if vr in vrs else vr),shape_str_to_shape(shape)
        if not _coconut_case_match_check_17:  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
            _coconut_match_set_name_mode = _coconut_sentinel  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
            _coconut_match_set_name_ch = _coconut_sentinel  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
            if (_coconut.isinstance(_coconut_case_match_to_17, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_17) == 3) and (_coconut_case_match_to_17[0] == "image"):  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
                _coconut_match_set_name_mode = _coconut_case_match_to_17[1]  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
                _coconut_match_set_name_ch = _coconut_case_match_to_17[2]  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
                _coconut_case_match_check_17 = True  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
            if _coconut_case_match_check_17:  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
                if _coconut_match_set_name_mode is not _coconut_sentinel:  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
                    mode = _coconut_match_set_name_mode  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
                if _coconut_match_set_name_ch is not _coconut_sentinel:  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
                    ch = _coconut_match_set_name_ch  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
            if _coconut_case_match_check_17 and not (len(ch_splitter(ch)) > 1):  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
                _coconut_case_match_check_17 = False  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
            if _coconut_case_match_check_17:  #627:             match ["image",mode,ch] if len(ch_splitter(ch)) > 1:
                return (PILImage(mode, ch), (None, None, len(ch_splitter(ch))))  #628:                 return PILImage(mode,ch),(None,None,len(ch_splitter(ch)))
        if not _coconut_case_match_check_17:  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
            _coconut_match_set_name_mode = _coconut_sentinel  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
            _coconut_match_set_name_ch = _coconut_sentinel  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
            if (_coconut.isinstance(_coconut_case_match_to_17, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_17) == 3) and (_coconut_case_match_to_17[0] == "image"):  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
                _coconut_match_set_name_mode = _coconut_case_match_to_17[1]  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
                _coconut_match_set_name_ch = _coconut_case_match_to_17[2]  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
                _coconut_case_match_check_17 = True  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
            if _coconut_case_match_check_17:  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
                if _coconut_match_set_name_mode is not _coconut_sentinel:  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
                    mode = _coconut_match_set_name_mode  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
                if _coconut_match_set_name_ch is not _coconut_sentinel:  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
                    ch = _coconut_match_set_name_ch  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
            if _coconut_case_match_check_17 and not (len(ch_splitter(ch)) == 1):  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
                _coconut_case_match_check_17 = False  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
            if _coconut_case_match_check_17:  #629:             match ["image",mode,ch] if len(ch_splitter(ch)) ==1:
                return (PILImage(mode, ch), (None, None))  #630:                 return PILImage(mode,ch),(None,None)
        if not _coconut_case_match_check_17:  #631:             match ["image",mode,ch,shape]:
            _coconut_match_set_name_mode = _coconut_sentinel  #631:             match ["image",mode,ch,shape]:
            _coconut_match_set_name_ch = _coconut_sentinel  #631:             match ["image",mode,ch,shape]:
            _coconut_match_set_name_shape = _coconut_sentinel  #631:             match ["image",mode,ch,shape]:
            if (_coconut.isinstance(_coconut_case_match_to_17, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_17) == 4) and (_coconut_case_match_to_17[0] == "image"):  #631:             match ["image",mode,ch,shape]:
                _coconut_match_set_name_mode = _coconut_case_match_to_17[1]  #631:             match ["image",mode,ch,shape]:
                _coconut_match_set_name_ch = _coconut_case_match_to_17[2]  #631:             match ["image",mode,ch,shape]:
                _coconut_match_set_name_shape = _coconut_case_match_to_17[3]  #631:             match ["image",mode,ch,shape]:
                _coconut_case_match_check_17 = True  #631:             match ["image",mode,ch,shape]:
            if _coconut_case_match_check_17:  #631:             match ["image",mode,ch,shape]:
                if _coconut_match_set_name_mode is not _coconut_sentinel:  #631:             match ["image",mode,ch,shape]:
                    mode = _coconut_match_set_name_mode  #631:             match ["image",mode,ch,shape]:
                if _coconut_match_set_name_ch is not _coconut_sentinel:  #631:             match ["image",mode,ch,shape]:
                    ch = _coconut_match_set_name_ch  #631:             match ["image",mode,ch,shape]:
                if _coconut_match_set_name_shape is not _coconut_sentinel:  #631:             match ["image",mode,ch,shape]:
                    shape = _coconut_match_set_name_shape  #631:             match ["image",mode,ch,shape]:
            if _coconut_case_match_check_17:  #631:             match ["image",mode,ch,shape]:
                return (PILImage(mode, ch), shape_str_to_shape(shape))  #632:                 return PILImage(mode,ch),shape_str_to_shape(shape)
        if not _coconut_case_match_check_17:  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
            _coconut_match_set_name_mode = _coconut_sentinel  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
            _coconut_match_set_name_ch = _coconut_sentinel  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
            if (_coconut.isinstance(_coconut_case_match_to_17, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_17) == 3) and (_coconut_case_match_to_17[0] == "images"):  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
                _coconut_match_set_name_mode = _coconut_case_match_to_17[1]  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
                _coconut_match_set_name_ch = _coconut_case_match_to_17[2]  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
                _coconut_case_match_check_17 = True  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
            if _coconut_case_match_check_17:  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
                if _coconut_match_set_name_mode is not _coconut_sentinel:  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
                    mode = _coconut_match_set_name_mode  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
                if _coconut_match_set_name_ch is not _coconut_sentinel:  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
                    ch = _coconut_match_set_name_ch  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
            if _coconut_case_match_check_17 and not (len(ch_splitter(ch)) > 1):  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
                _coconut_case_match_check_17 = False  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
            if _coconut_case_match_check_17:  #633:             match ["images",mode,ch] if len(ch_splitter(ch)) > 1:
                return (PILImages(mode, ch), (None, None, None, len(ch_splitter(ch))))  #634:                 return PILImages(mode,ch),(None,None,None,len(ch_splitter(ch)))
        if not _coconut_case_match_check_17:  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
            _coconut_match_set_name_mode = _coconut_sentinel  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
            _coconut_match_set_name_ch = _coconut_sentinel  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
            if (_coconut.isinstance(_coconut_case_match_to_17, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_17) == 3) and (_coconut_case_match_to_17[0] == "images"):  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
                _coconut_match_set_name_mode = _coconut_case_match_to_17[1]  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
                _coconut_match_set_name_ch = _coconut_case_match_to_17[2]  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
                _coconut_case_match_check_17 = True  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
            if _coconut_case_match_check_17:  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
                if _coconut_match_set_name_mode is not _coconut_sentinel:  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
                    mode = _coconut_match_set_name_mode  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
                if _coconut_match_set_name_ch is not _coconut_sentinel:  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
                    ch = _coconut_match_set_name_ch  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
            if _coconut_case_match_check_17 and not (len(ch_splitter(ch)) == 1):  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
                _coconut_case_match_check_17 = False  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
            if _coconut_case_match_check_17:  #635:             match ["images",mode,ch] if len(ch_splitter(ch)) == 1:
                return (PILImages(mode, ch), (None, None, None))  #636:                 return PILImages(mode,ch),(None,None,None)
        if not _coconut_case_match_check_17:  #637:             match ["images",mode,ch,shape]:
            _coconut_match_set_name_mode = _coconut_sentinel  #637:             match ["images",mode,ch,shape]:
            _coconut_match_set_name_ch = _coconut_sentinel  #637:             match ["images",mode,ch,shape]:
            _coconut_match_set_name_shape = _coconut_sentinel  #637:             match ["images",mode,ch,shape]:
            if (_coconut.isinstance(_coconut_case_match_to_17, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_17) == 4) and (_coconut_case_match_to_17[0] == "images"):  #637:             match ["images",mode,ch,shape]:
                _coconut_match_set_name_mode = _coconut_case_match_to_17[1]  #637:             match ["images",mode,ch,shape]:
                _coconut_match_set_name_ch = _coconut_case_match_to_17[2]  #637:             match ["images",mode,ch,shape]:
                _coconut_match_set_name_shape = _coconut_case_match_to_17[3]  #637:             match ["images",mode,ch,shape]:
                _coconut_case_match_check_17 = True  #637:             match ["images",mode,ch,shape]:
            if _coconut_case_match_check_17:  #637:             match ["images",mode,ch,shape]:
                if _coconut_match_set_name_mode is not _coconut_sentinel:  #637:             match ["images",mode,ch,shape]:
                    mode = _coconut_match_set_name_mode  #637:             match ["images",mode,ch,shape]:
                if _coconut_match_set_name_ch is not _coconut_sentinel:  #637:             match ["images",mode,ch,shape]:
                    ch = _coconut_match_set_name_ch  #637:             match ["images",mode,ch,shape]:
                if _coconut_match_set_name_shape is not _coconut_sentinel:  #637:             match ["images",mode,ch,shape]:
                    shape = _coconut_match_set_name_shape  #637:             match ["images",mode,ch,shape]:
            if _coconut_case_match_check_17:  #637:             match ["images",mode,ch,shape]:
                return (PILImages(mode, ch), shape_str_to_shape(shape))  #638:                 return PILImages(mode,ch),shape_str_to_shape(shape)

    _coconut_case_match_to_18 = query_to_data_type(query)  #639:     case query_to_data_type(query):
    _coconut_case_match_check_18 = False  #639:     case query_to_data_type(query):
    _coconut_match_set_name_data_type = _coconut_sentinel  #639:     case query_to_data_type(query):
    _coconut_match_set_name_shape = _coconut_sentinel  #639:     case query_to_data_type(query):
    if (_coconut.isinstance(_coconut_case_match_to_18, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_18) == 2):  #639:     case query_to_data_type(query):
        _coconut_match_set_name_data_type = _coconut_case_match_to_18[0]  #639:     case query_to_data_type(query):
        _coconut_match_set_name_shape = _coconut_case_match_to_18[1]  #639:     case query_to_data_type(query):
        _coconut_case_match_check_18 = True  #639:     case query_to_data_type(query):
    if _coconut_case_match_check_18:  #639:     case query_to_data_type(query):
        if _coconut_match_set_name_data_type is not _coconut_sentinel:  #639:     case query_to_data_type(query):
            data_type = _coconut_match_set_name_data_type  #639:     case query_to_data_type(query):
        if _coconut_match_set_name_shape is not _coconut_sentinel:  #639:     case query_to_data_type(query):
            shape = _coconut_match_set_name_shape  #639:     case query_to_data_type(query):
    if _coconut_case_match_check_18:  #639:     case query_to_data_type(query):
        return (ImageDef(data_type, fdict(shape=shape)))  #641:             return ImageDef(data_type,fdict(shape=shape))
    if not _coconut_case_match_check_18:  #642:     else:
        raise RuntimeError("could not parse image def string!:{_coconut_format_0}".format(_coconut_format_0=(query)))  #643:         raise RuntimeError(f"could not parse image def string!:{query}")


def parse_def(img_def):  #645: def parse_def(img_def):
    try:  #646:     try:
        return (str_to_img_def(img_def) if (isinstance)(img_def, str) else img_def)  #647:         return str_to_img_def(img_def) if img_def `isinstance` str else img_def
    except Exception as e:  #648:     except Exception as e:
        return (img_def)  #649:         return img_def




accept_def_str = lambda f: _coconut_base_compose(parse_def, (f, 0, False))  #653: accept_def_str = f -> parse_def ..> f
def imdef_neighbors(imdef):  #654: def imdef_neighbors(imdef):
    return ([(e.f, e.b, e.cost, e.name) for e in _edges(imdef)])  #655:     return [(e.f,e.b,e.cost,e.name) for e in _edges(imdef)]

#from data_tree.coconut.convert import AutoImage,PILImage,str_to_img_def,PILImages
#from data_tree.coconut.convert import ImageDef,Torch,Numpy,TensorLike,VR_0_1,VR_None,VR_0_255


def normalize_numpy_img(ary):  #660: def normalize_numpy_img(ary):
    _min = ary.min()  #661:     _min = ary.min()
    _max = ary.max()  #662:     _max = ary.max()
    return (((ary - _min) / (_max - _min)))  #663:     return ((ary-_min)/(_max-_min))


def rule_VR_None_to_normalized(imdef):  #665: def rule_VR_None_to_normalized(imdef):
    _coconut_case_match_to_19 = imdef  #666:     case imdef:
    _coconut_case_match_check_19 = False  #666:     case imdef:
    _coconut_match_temp_502 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #666:     case imdef:
    _coconut_case_match_check_19 = True  #666:     case imdef:
    if _coconut_case_match_check_19:  #666:     case imdef:
        _coconut_case_match_check_19 = False  #666:     case imdef:
        if not _coconut_case_match_check_19:  #666:     case imdef:
            _coconut_match_set_name_meta = _coconut_sentinel  #666:     case imdef:
            if (_coconut_match_temp_502) and (_coconut.isinstance(_coconut_case_match_to_19, ImageDef)) and (_coconut.len(_coconut_case_match_to_19) >= 2):  #666:     case imdef:
                _coconut_match_temp_503 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #666:     case imdef:
                _coconut_match_set_name_meta = _coconut_case_match_to_19[1]  #666:     case imdef:
                _coconut_match_temp_510 = _coconut.len(_coconut_case_match_to_19) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_19.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_19, "_coconut_data_defaults", {}) and _coconut_case_match_to_19[i] == _coconut.getattr(_coconut_case_match_to_19, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_19.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_19, "__match_args__") else _coconut.len(_coconut_case_match_to_19) == 2  # type: ignore  #666:     case imdef:
                if _coconut_match_temp_510:  #666:     case imdef:
                    _coconut_case_match_check_19 = True  #666:     case imdef:
            if _coconut_case_match_check_19:  #666:     case imdef:
                _coconut_case_match_check_19 = False  #666:     case imdef:
                if not _coconut_case_match_check_19:  #666:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #666:     case imdef:
                    _coconut_match_set_name_arng = _coconut_sentinel  #666:     case imdef:
                    _coconut_match_set_name_ch = _coconut_sentinel  #666:     case imdef:
                    if (_coconut_match_temp_503) and (_coconut.isinstance(_coconut_case_match_to_19[0], Numpy)) and (_coconut.len(_coconut_case_match_to_19[0]) >= 4) and (_coconut_case_match_to_19[0][3] == VR_None):  #666:     case imdef:
                        _coconut_match_set_name_dtype = _coconut_case_match_to_19[0][0]  #666:     case imdef:
                        _coconut_match_set_name_arng = _coconut_case_match_to_19[0][1]  #666:     case imdef:
                        _coconut_match_set_name_ch = _coconut_case_match_to_19[0][2]  #666:     case imdef:
                        _coconut_match_temp_504 = _coconut.len(_coconut_case_match_to_19[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_19[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_19[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_19[0][i] == _coconut.getattr(_coconut_case_match_to_19[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_19[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_19[0], "__match_args__") else _coconut.len(_coconut_case_match_to_19[0]) == 4  # type: ignore  #666:     case imdef:
                        if _coconut_match_temp_504:  #666:     case imdef:
                            _coconut_case_match_check_19 = True  #666:     case imdef:
                    if _coconut_case_match_check_19:  #666:     case imdef:
                        _coconut_case_match_check_19 = False  #666:     case imdef:
                        if not _coconut_case_match_check_19:  #666:     case imdef:
                            if _coconut_case_match_to_19[0][1] == "CHW":  #666:     case imdef:
                                _coconut_case_match_check_19 = True  #666:     case imdef:

                        if not _coconut_case_match_check_19:  #666:     case imdef:
                            if _coconut_case_match_to_19[0][1] == "HW":  #666:     case imdef:
                                _coconut_case_match_check_19 = True  #666:     case imdef:


                    if _coconut_case_match_check_19:  #666:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #666:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #666:     case imdef:
                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #666:     case imdef:
                            arng = _coconut_match_set_name_arng  #666:     case imdef:
                        if _coconut_match_set_name_ch is not _coconut_sentinel:  #666:     case imdef:
                            ch = _coconut_match_set_name_ch  #666:     case imdef:

                if not _coconut_case_match_check_19:  #666:     case imdef:
                    if (not _coconut_match_temp_503) and (_coconut.isinstance(_coconut_case_match_to_19[0], Numpy)):  #666:     case imdef:
                        _coconut_case_match_check_19 = True  #666:     case imdef:
                    if _coconut_case_match_check_19:  #666:     case imdef:
                        _coconut_case_match_check_19 = False  #666:     case imdef:
                        if not _coconut_case_match_check_19:  #666:     case imdef:
                            if _coconut.type(_coconut_case_match_to_19[0]) in _coconut_self_match_types:  #666:     case imdef:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #666:     case imdef:
                                _coconut_case_match_check_19 = True  #666:     case imdef:

                        if not _coconut_case_match_check_19:  #666:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #666:     case imdef:
                            _coconut_match_set_name_arng = _coconut_sentinel  #666:     case imdef:
                            _coconut_match_set_name_ch = _coconut_sentinel  #666:     case imdef:
                            if not _coconut.type(_coconut_case_match_to_19[0]) in _coconut_self_match_types:  #666:     case imdef:
                                _coconut_match_temp_505 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #666:     case imdef:
                                if not _coconut.isinstance(_coconut_match_temp_505, _coconut.tuple):  #666:     case imdef:
                                    raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #666:     case imdef:
                                if _coconut.len(_coconut_match_temp_505) < 4:  #666:     case imdef:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_505),))  #666:     case imdef:
                                _coconut_match_temp_506 = _coconut.getattr(_coconut_case_match_to_19[0], _coconut_match_temp_505[0], _coconut_sentinel)  #666:     case imdef:
                                _coconut_match_temp_507 = _coconut.getattr(_coconut_case_match_to_19[0], _coconut_match_temp_505[1], _coconut_sentinel)  #666:     case imdef:
                                _coconut_match_temp_508 = _coconut.getattr(_coconut_case_match_to_19[0], _coconut_match_temp_505[2], _coconut_sentinel)  #666:     case imdef:
                                _coconut_match_temp_509 = _coconut.getattr(_coconut_case_match_to_19[0], _coconut_match_temp_505[3], _coconut_sentinel)  #666:     case imdef:
                                if (_coconut_match_temp_506 is not _coconut_sentinel) and (_coconut_match_temp_507 is not _coconut_sentinel) and (_coconut_match_temp_508 is not _coconut_sentinel) and (_coconut_match_temp_509 is not _coconut_sentinel) and (_coconut_match_temp_509 == VR_None):  #666:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_match_temp_506  #666:     case imdef:
                                    _coconut_match_set_name_arng = _coconut_match_temp_507  #666:     case imdef:
                                    _coconut_match_set_name_ch = _coconut_match_temp_508  #666:     case imdef:
                                    _coconut_case_match_check_19 = True  #666:     case imdef:
                            if _coconut_case_match_check_19:  #666:     case imdef:
                                _coconut_case_match_check_19 = False  #666:     case imdef:
                                if not _coconut_case_match_check_19:  #666:     case imdef:
                                    if _coconut_match_temp_507 == "CHW":  #666:     case imdef:
                                        _coconut_case_match_check_19 = True  #666:     case imdef:

                                if not _coconut_case_match_check_19:  #666:     case imdef:
                                    if _coconut_match_temp_507 == "HW":  #666:     case imdef:
                                        _coconut_case_match_check_19 = True  #666:     case imdef:


                            if _coconut_case_match_check_19:  #666:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #666:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #666:     case imdef:
                                if _coconut_match_set_name_arng is not _coconut_sentinel:  #666:     case imdef:
                                    arng = _coconut_match_set_name_arng  #666:     case imdef:
                                if _coconut_match_set_name_ch is not _coconut_sentinel:  #666:     case imdef:
                                    ch = _coconut_match_set_name_ch  #666:     case imdef:




            if _coconut_case_match_check_19:  #666:     case imdef:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #666:     case imdef:
                    meta = _coconut_match_set_name_meta  #666:     case imdef:

        if not _coconut_case_match_check_19:  #666:     case imdef:
            if (not _coconut_match_temp_502) and (_coconut.isinstance(_coconut_case_match_to_19, ImageDef)):  #666:     case imdef:
                _coconut_case_match_check_19 = True  #666:     case imdef:
            if _coconut_case_match_check_19:  #666:     case imdef:
                _coconut_case_match_check_19 = False  #666:     case imdef:
                if not _coconut_case_match_check_19:  #666:     case imdef:
                    if _coconut.type(_coconut_case_match_to_19) in _coconut_self_match_types:  #666:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #666:     case imdef:
                        _coconut_case_match_check_19 = True  #666:     case imdef:

                if not _coconut_case_match_check_19:  #666:     case imdef:
                    _coconut_match_set_name_meta = _coconut_sentinel  #666:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_19) in _coconut_self_match_types:  #666:     case imdef:
                        _coconut_match_temp_511 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #666:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_511, _coconut.tuple):  #666:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #666:     case imdef:
                        if _coconut.len(_coconut_match_temp_511) < 2:  #666:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_511),))  #666:     case imdef:
                        _coconut_match_temp_512 = _coconut.getattr(_coconut_case_match_to_19, _coconut_match_temp_511[0], _coconut_sentinel)  #666:     case imdef:
                        _coconut_match_temp_520 = _coconut.getattr(_coconut_case_match_to_19, _coconut_match_temp_511[1], _coconut_sentinel)  #666:     case imdef:
                        if (_coconut_match_temp_512 is not _coconut_sentinel) and (_coconut_match_temp_520 is not _coconut_sentinel):  #666:     case imdef:
                            _coconut_match_temp_513 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #666:     case imdef:
                            _coconut_match_set_name_meta = _coconut_match_temp_520  #666:     case imdef:
                            _coconut_case_match_check_19 = True  #666:     case imdef:
                    if _coconut_case_match_check_19:  #666:     case imdef:
                        _coconut_case_match_check_19 = False  #666:     case imdef:
                        if not _coconut_case_match_check_19:  #666:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #666:     case imdef:
                            _coconut_match_set_name_arng = _coconut_sentinel  #666:     case imdef:
                            _coconut_match_set_name_ch = _coconut_sentinel  #666:     case imdef:
                            if (_coconut_match_temp_513) and (_coconut.isinstance(_coconut_match_temp_512, Numpy)) and (_coconut.len(_coconut_match_temp_512) >= 4) and (_coconut_match_temp_512[3] == VR_None):  #666:     case imdef:
                                _coconut_match_set_name_dtype = _coconut_match_temp_512[0]  #666:     case imdef:
                                _coconut_match_set_name_arng = _coconut_match_temp_512[1]  #666:     case imdef:
                                _coconut_match_set_name_ch = _coconut_match_temp_512[2]  #666:     case imdef:
                                _coconut_match_temp_514 = _coconut.len(_coconut_match_temp_512) <= _coconut.max(4, _coconut.len(_coconut_match_temp_512.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_512, "_coconut_data_defaults", {}) and _coconut_match_temp_512[i] == _coconut.getattr(_coconut_match_temp_512, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_512.__match_args__))) if _coconut.hasattr(_coconut_match_temp_512, "__match_args__") else _coconut.len(_coconut_match_temp_512) == 4  # type: ignore  #666:     case imdef:
                                if _coconut_match_temp_514:  #666:     case imdef:
                                    _coconut_case_match_check_19 = True  #666:     case imdef:
                            if _coconut_case_match_check_19:  #666:     case imdef:
                                _coconut_case_match_check_19 = False  #666:     case imdef:
                                if not _coconut_case_match_check_19:  #666:     case imdef:
                                    if _coconut_match_temp_512[1] == "CHW":  #666:     case imdef:
                                        _coconut_case_match_check_19 = True  #666:     case imdef:

                                if not _coconut_case_match_check_19:  #666:     case imdef:
                                    if _coconut_match_temp_512[1] == "HW":  #666:     case imdef:
                                        _coconut_case_match_check_19 = True  #666:     case imdef:


                            if _coconut_case_match_check_19:  #666:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #666:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #666:     case imdef:
                                if _coconut_match_set_name_arng is not _coconut_sentinel:  #666:     case imdef:
                                    arng = _coconut_match_set_name_arng  #666:     case imdef:
                                if _coconut_match_set_name_ch is not _coconut_sentinel:  #666:     case imdef:
                                    ch = _coconut_match_set_name_ch  #666:     case imdef:

                        if not _coconut_case_match_check_19:  #666:     case imdef:
                            if (not _coconut_match_temp_513) and (_coconut.isinstance(_coconut_match_temp_512, Numpy)):  #666:     case imdef:
                                _coconut_case_match_check_19 = True  #666:     case imdef:
                            if _coconut_case_match_check_19:  #666:     case imdef:
                                _coconut_case_match_check_19 = False  #666:     case imdef:
                                if not _coconut_case_match_check_19:  #666:     case imdef:
                                    if _coconut.type(_coconut_match_temp_512) in _coconut_self_match_types:  #666:     case imdef:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #666:     case imdef:
                                        _coconut_case_match_check_19 = True  #666:     case imdef:

                                if not _coconut_case_match_check_19:  #666:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_sentinel  #666:     case imdef:
                                    _coconut_match_set_name_arng = _coconut_sentinel  #666:     case imdef:
                                    _coconut_match_set_name_ch = _coconut_sentinel  #666:     case imdef:
                                    if not _coconut.type(_coconut_match_temp_512) in _coconut_self_match_types:  #666:     case imdef:
                                        _coconut_match_temp_515 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #666:     case imdef:
                                        if not _coconut.isinstance(_coconut_match_temp_515, _coconut.tuple):  #666:     case imdef:
                                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #666:     case imdef:
                                        if _coconut.len(_coconut_match_temp_515) < 4:  #666:     case imdef:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_515),))  #666:     case imdef:
                                        _coconut_match_temp_516 = _coconut.getattr(_coconut_match_temp_512, _coconut_match_temp_515[0], _coconut_sentinel)  #666:     case imdef:
                                        _coconut_match_temp_517 = _coconut.getattr(_coconut_match_temp_512, _coconut_match_temp_515[1], _coconut_sentinel)  #666:     case imdef:
                                        _coconut_match_temp_518 = _coconut.getattr(_coconut_match_temp_512, _coconut_match_temp_515[2], _coconut_sentinel)  #666:     case imdef:
                                        _coconut_match_temp_519 = _coconut.getattr(_coconut_match_temp_512, _coconut_match_temp_515[3], _coconut_sentinel)  #666:     case imdef:
                                        if (_coconut_match_temp_516 is not _coconut_sentinel) and (_coconut_match_temp_517 is not _coconut_sentinel) and (_coconut_match_temp_518 is not _coconut_sentinel) and (_coconut_match_temp_519 is not _coconut_sentinel) and (_coconut_match_temp_519 == VR_None):  #666:     case imdef:
                                            _coconut_match_set_name_dtype = _coconut_match_temp_516  #666:     case imdef:
                                            _coconut_match_set_name_arng = _coconut_match_temp_517  #666:     case imdef:
                                            _coconut_match_set_name_ch = _coconut_match_temp_518  #666:     case imdef:
                                            _coconut_case_match_check_19 = True  #666:     case imdef:
                                    if _coconut_case_match_check_19:  #666:     case imdef:
                                        _coconut_case_match_check_19 = False  #666:     case imdef:
                                        if not _coconut_case_match_check_19:  #666:     case imdef:
                                            if _coconut_match_temp_517 == "CHW":  #666:     case imdef:
                                                _coconut_case_match_check_19 = True  #666:     case imdef:

                                        if not _coconut_case_match_check_19:  #666:     case imdef:
                                            if _coconut_match_temp_517 == "HW":  #666:     case imdef:
                                                _coconut_case_match_check_19 = True  #666:     case imdef:


                                    if _coconut_case_match_check_19:  #666:     case imdef:
                                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #666:     case imdef:
                                            dtype = _coconut_match_set_name_dtype  #666:     case imdef:
                                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #666:     case imdef:
                                            arng = _coconut_match_set_name_arng  #666:     case imdef:
                                        if _coconut_match_set_name_ch is not _coconut_sentinel:  #666:     case imdef:
                                            ch = _coconut_match_set_name_ch  #666:     case imdef:




                    if _coconut_case_match_check_19:  #666:     case imdef:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #666:     case imdef:
                            meta = _coconut_match_set_name_meta  #666:     case imdef:




    if _coconut_case_match_check_19:  #666:     case imdef:
        return ([(normalize_numpy_img, ImageDef(Numpy(dtype, arng, ch, VR_0_1), meta), 1, "minmax_0_1_numpy_img"),])  #668:             return [(
    if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
        _coconut_match_temp_521 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
        _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
        if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
            _coconut_case_match_check_19 = False  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
            if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                if (_coconut_match_temp_521) and (_coconut.isinstance(_coconut_case_match_to_19, ImageDef)) and (_coconut.len(_coconut_case_match_to_19) >= 2):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                    _coconut_match_temp_522 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_19[1]  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                    _coconut_match_temp_529 = _coconut.len(_coconut_case_match_to_19) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_19.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_19, "_coconut_data_defaults", {}) and _coconut_case_match_to_19[i] == _coconut.getattr(_coconut_case_match_to_19, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_19.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_19, "__match_args__") else _coconut.len(_coconut_case_match_to_19) == 2  # type: ignore  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                    if _coconut_match_temp_529:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                    _coconut_case_match_check_19 = False  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                    if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        _coconut_match_set_name_dtype = _coconut_sentinel  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        _coconut_match_set_name_ch = _coconut_sentinel  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        if (_coconut_match_temp_522) and (_coconut.isinstance(_coconut_case_match_to_19[0], Numpy)) and (_coconut.len(_coconut_case_match_to_19[0]) >= 4) and (_coconut_case_match_to_19[0][1] == "BCHW") and (_coconut_case_match_to_19[0][3] == VR_None):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            _coconut_match_set_name_dtype = _coconut_case_match_to_19[0][0]  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            _coconut_match_set_name_ch = _coconut_case_match_to_19[0][2]  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            _coconut_match_temp_523 = _coconut.len(_coconut_case_match_to_19[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_19[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_19[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_19[0][i] == _coconut.getattr(_coconut_case_match_to_19[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_19[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_19[0], "__match_args__") else _coconut.len(_coconut_case_match_to_19[0]) == 4  # type: ignore  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            if _coconut_match_temp_523:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                dtype = _coconut_match_set_name_dtype  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            if _coconut_match_set_name_ch is not _coconut_sentinel:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                ch = _coconut_match_set_name_ch  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):

                    if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        if (not _coconut_match_temp_522) and (_coconut.isinstance(_coconut_case_match_to_19[0], Numpy)):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            _coconut_case_match_check_19 = False  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                if _coconut.type(_coconut_case_match_to_19[0]) in _coconut_self_match_types:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):

                            if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                _coconut_match_set_name_ch = _coconut_sentinel  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                if not _coconut.type(_coconut_case_match_to_19[0]) in _coconut_self_match_types:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    _coconut_match_temp_524 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_524, _coconut.tuple):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    if _coconut.len(_coconut_match_temp_524) < 4:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_524),))  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    _coconut_match_temp_525 = _coconut.getattr(_coconut_case_match_to_19[0], _coconut_match_temp_524[0], _coconut_sentinel)  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    _coconut_match_temp_526 = _coconut.getattr(_coconut_case_match_to_19[0], _coconut_match_temp_524[1], _coconut_sentinel)  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    _coconut_match_temp_527 = _coconut.getattr(_coconut_case_match_to_19[0], _coconut_match_temp_524[2], _coconut_sentinel)  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    _coconut_match_temp_528 = _coconut.getattr(_coconut_case_match_to_19[0], _coconut_match_temp_524[3], _coconut_sentinel)  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    if (_coconut_match_temp_525 is not _coconut_sentinel) and (_coconut_match_temp_526 is not _coconut_sentinel) and (_coconut_match_temp_526 == "BCHW") and (_coconut_match_temp_527 is not _coconut_sentinel) and (_coconut_match_temp_528 is not _coconut_sentinel) and (_coconut_match_temp_528 == VR_None):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        _coconut_match_set_name_dtype = _coconut_match_temp_525  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        _coconut_match_set_name_ch = _coconut_match_temp_527  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        dtype = _coconut_match_set_name_dtype  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    if _coconut_match_set_name_ch is not _coconut_sentinel:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        ch = _coconut_match_set_name_ch  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):




                if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        meta = _coconut_match_set_name_meta  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):

            if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                if (not _coconut_match_temp_521) and (_coconut.isinstance(_coconut_case_match_to_19, ImageDef)):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                    _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                    _coconut_case_match_check_19 = False  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                    if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        if _coconut.type(_coconut_case_match_to_19) in _coconut_self_match_types:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):

                    if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        if not _coconut.type(_coconut_case_match_to_19) in _coconut_self_match_types:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            _coconut_match_temp_530 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            if not _coconut.isinstance(_coconut_match_temp_530, _coconut.tuple):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            if _coconut.len(_coconut_match_temp_530) < 2:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_530),))  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            _coconut_match_temp_531 = _coconut.getattr(_coconut_case_match_to_19, _coconut_match_temp_530[0], _coconut_sentinel)  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            _coconut_match_temp_539 = _coconut.getattr(_coconut_case_match_to_19, _coconut_match_temp_530[1], _coconut_sentinel)  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            if (_coconut_match_temp_531 is not _coconut_sentinel) and (_coconut_match_temp_539 is not _coconut_sentinel):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                _coconut_match_temp_532 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_539  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                        if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            _coconut_case_match_check_19 = False  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                _coconut_match_set_name_ch = _coconut_sentinel  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                if (_coconut_match_temp_532) and (_coconut.isinstance(_coconut_match_temp_531, Numpy)) and (_coconut.len(_coconut_match_temp_531) >= 4) and (_coconut_match_temp_531[1] == "BCHW") and (_coconut_match_temp_531[3] == VR_None):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    _coconut_match_set_name_dtype = _coconut_match_temp_531[0]  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    _coconut_match_set_name_ch = _coconut_match_temp_531[2]  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    _coconut_match_temp_533 = _coconut.len(_coconut_match_temp_531) <= _coconut.max(4, _coconut.len(_coconut_match_temp_531.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_531, "_coconut_data_defaults", {}) and _coconut_match_temp_531[i] == _coconut.getattr(_coconut_match_temp_531, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_531.__match_args__))) if _coconut.hasattr(_coconut_match_temp_531, "__match_args__") else _coconut.len(_coconut_match_temp_531) == 4  # type: ignore  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    if _coconut_match_temp_533:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        dtype = _coconut_match_set_name_dtype  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    if _coconut_match_set_name_ch is not _coconut_sentinel:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        ch = _coconut_match_set_name_ch  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):

                            if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                if (not _coconut_match_temp_532) and (_coconut.isinstance(_coconut_match_temp_531, Numpy)):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    _coconut_case_match_check_19 = False  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                    if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        if _coconut.type(_coconut_match_temp_531) in _coconut_self_match_types:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):

                                    if not _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        _coconut_match_set_name_dtype = _coconut_sentinel  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        _coconut_match_set_name_ch = _coconut_sentinel  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        if not _coconut.type(_coconut_match_temp_531) in _coconut_self_match_types:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            _coconut_match_temp_534 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_534, _coconut.tuple):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            if _coconut.len(_coconut_match_temp_534) < 4:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_534),))  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            _coconut_match_temp_535 = _coconut.getattr(_coconut_match_temp_531, _coconut_match_temp_534[0], _coconut_sentinel)  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            _coconut_match_temp_536 = _coconut.getattr(_coconut_match_temp_531, _coconut_match_temp_534[1], _coconut_sentinel)  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            _coconut_match_temp_537 = _coconut.getattr(_coconut_match_temp_531, _coconut_match_temp_534[2], _coconut_sentinel)  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            _coconut_match_temp_538 = _coconut.getattr(_coconut_match_temp_531, _coconut_match_temp_534[3], _coconut_sentinel)  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            if (_coconut_match_temp_535 is not _coconut_sentinel) and (_coconut_match_temp_536 is not _coconut_sentinel) and (_coconut_match_temp_536 == "BCHW") and (_coconut_match_temp_537 is not _coconut_sentinel) and (_coconut_match_temp_538 is not _coconut_sentinel) and (_coconut_match_temp_538 == VR_None):  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                                _coconut_match_set_name_dtype = _coconut_match_temp_535  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                                _coconut_match_set_name_ch = _coconut_match_temp_537  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                                _coconut_case_match_check_19 = True  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                        if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                                dtype = _coconut_match_set_name_dtype  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                            if _coconut_match_set_name_ch is not _coconut_sentinel:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                                ch = _coconut_match_set_name_ch  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):




                        if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
                                meta = _coconut_match_set_name_meta  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):




        if _coconut_case_match_check_19:  #674:         match ImageDef(Numpy(dtype,"BCHW",ch,=VR_None),meta):
            return ([(lambda batch: np.array([normalize_numpy_img(img) for img in batch]), ImageDef(Numpy(dtype, "BCHW", ch, VR_0_1), meta), 1, "batch_minmax_0_1_numpy_img"),])  #675:             return [(

ms_add_ch_to_hw = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (1, s[0], s[1])))  #681: ms_add_ch_to_hw = (s->(1,s[0],s[1])) |> ss_to_ms$
ms_add_ch_to_bhw = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], 1, s[1], s[2])))  #682: ms_add_ch_to_bhw = (s->(s[0],1,s[1],s[2])) |> ss_to_ms$
def rule_add_channel(imdef):  #683: def rule_add_channel(imdef):
    _coconut_case_match_to_20 = imdef  #684:     case imdef:
    _coconut_case_match_check_20 = False  #684:     case imdef:
    _coconut_match_temp_540 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #684:     case imdef:
    _coconut_case_match_check_20 = True  #684:     case imdef:
    if _coconut_case_match_check_20:  #684:     case imdef:
        _coconut_case_match_check_20 = False  #684:     case imdef:
        if not _coconut_case_match_check_20:  #684:     case imdef:
            _coconut_match_set_name_meta = _coconut_sentinel  #684:     case imdef:
            if (_coconut_match_temp_540) and (_coconut.isinstance(_coconut_case_match_to_20, ImageDef)) and (_coconut.len(_coconut_case_match_to_20) >= 2):  #684:     case imdef:
                _coconut_match_temp_541 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #684:     case imdef:
                _coconut_match_set_name_meta = _coconut_case_match_to_20[1]  #684:     case imdef:
                _coconut_match_temp_548 = _coconut.len(_coconut_case_match_to_20) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_20.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_20, "_coconut_data_defaults", {}) and _coconut_case_match_to_20[i] == _coconut.getattr(_coconut_case_match_to_20, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_20.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_20, "__match_args__") else _coconut.len(_coconut_case_match_to_20) == 2  # type: ignore  #684:     case imdef:
                if _coconut_match_temp_548:  #684:     case imdef:
                    _coconut_case_match_check_20 = True  #684:     case imdef:
            if _coconut_case_match_check_20:  #684:     case imdef:
                _coconut_case_match_check_20 = False  #684:     case imdef:
                if not _coconut_case_match_check_20:  #684:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #684:     case imdef:
                    _coconut_match_set_name_ch = _coconut_sentinel  #684:     case imdef:
                    _coconut_match_set_name_vr = _coconut_sentinel  #684:     case imdef:
                    if (_coconut_match_temp_541) and (_coconut.isinstance(_coconut_case_match_to_20[0], Numpy)) and (_coconut.len(_coconut_case_match_to_20[0]) >= 4) and (_coconut_case_match_to_20[0][1] == "HW"):  #684:     case imdef:
                        _coconut_match_set_name_dtype = _coconut_case_match_to_20[0][0]  #684:     case imdef:
                        _coconut_match_set_name_ch = _coconut_case_match_to_20[0][2]  #684:     case imdef:
                        _coconut_match_set_name_vr = _coconut_case_match_to_20[0][3]  #684:     case imdef:
                        _coconut_match_temp_542 = _coconut.len(_coconut_case_match_to_20[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_20[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_20[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_20[0][i] == _coconut.getattr(_coconut_case_match_to_20[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_20[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_20[0], "__match_args__") else _coconut.len(_coconut_case_match_to_20[0]) == 4  # type: ignore  #684:     case imdef:
                        if _coconut_match_temp_542:  #684:     case imdef:
                            _coconut_case_match_check_20 = True  #684:     case imdef:
                    if _coconut_case_match_check_20:  #684:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #684:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #684:     case imdef:
                        if _coconut_match_set_name_ch is not _coconut_sentinel:  #684:     case imdef:
                            ch = _coconut_match_set_name_ch  #684:     case imdef:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #684:     case imdef:
                            vr = _coconut_match_set_name_vr  #684:     case imdef:

                if not _coconut_case_match_check_20:  #684:     case imdef:
                    if (not _coconut_match_temp_541) and (_coconut.isinstance(_coconut_case_match_to_20[0], Numpy)):  #684:     case imdef:
                        _coconut_case_match_check_20 = True  #684:     case imdef:
                    if _coconut_case_match_check_20:  #684:     case imdef:
                        _coconut_case_match_check_20 = False  #684:     case imdef:
                        if not _coconut_case_match_check_20:  #684:     case imdef:
                            if _coconut.type(_coconut_case_match_to_20[0]) in _coconut_self_match_types:  #684:     case imdef:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #684:     case imdef:
                                _coconut_case_match_check_20 = True  #684:     case imdef:

                        if not _coconut_case_match_check_20:  #684:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #684:     case imdef:
                            _coconut_match_set_name_ch = _coconut_sentinel  #684:     case imdef:
                            _coconut_match_set_name_vr = _coconut_sentinel  #684:     case imdef:
                            if not _coconut.type(_coconut_case_match_to_20[0]) in _coconut_self_match_types:  #684:     case imdef:
                                _coconut_match_temp_543 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #684:     case imdef:
                                if not _coconut.isinstance(_coconut_match_temp_543, _coconut.tuple):  #684:     case imdef:
                                    raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #684:     case imdef:
                                if _coconut.len(_coconut_match_temp_543) < 4:  #684:     case imdef:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_543),))  #684:     case imdef:
                                _coconut_match_temp_544 = _coconut.getattr(_coconut_case_match_to_20[0], _coconut_match_temp_543[0], _coconut_sentinel)  #684:     case imdef:
                                _coconut_match_temp_545 = _coconut.getattr(_coconut_case_match_to_20[0], _coconut_match_temp_543[1], _coconut_sentinel)  #684:     case imdef:
                                _coconut_match_temp_546 = _coconut.getattr(_coconut_case_match_to_20[0], _coconut_match_temp_543[2], _coconut_sentinel)  #684:     case imdef:
                                _coconut_match_temp_547 = _coconut.getattr(_coconut_case_match_to_20[0], _coconut_match_temp_543[3], _coconut_sentinel)  #684:     case imdef:
                                if (_coconut_match_temp_544 is not _coconut_sentinel) and (_coconut_match_temp_545 is not _coconut_sentinel) and (_coconut_match_temp_545 == "HW") and (_coconut_match_temp_546 is not _coconut_sentinel) and (_coconut_match_temp_547 is not _coconut_sentinel):  #684:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_match_temp_544  #684:     case imdef:
                                    _coconut_match_set_name_ch = _coconut_match_temp_546  #684:     case imdef:
                                    _coconut_match_set_name_vr = _coconut_match_temp_547  #684:     case imdef:
                                    _coconut_case_match_check_20 = True  #684:     case imdef:
                            if _coconut_case_match_check_20:  #684:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #684:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #684:     case imdef:
                                if _coconut_match_set_name_ch is not _coconut_sentinel:  #684:     case imdef:
                                    ch = _coconut_match_set_name_ch  #684:     case imdef:
                                if _coconut_match_set_name_vr is not _coconut_sentinel:  #684:     case imdef:
                                    vr = _coconut_match_set_name_vr  #684:     case imdef:




            if _coconut_case_match_check_20:  #684:     case imdef:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #684:     case imdef:
                    meta = _coconut_match_set_name_meta  #684:     case imdef:

        if not _coconut_case_match_check_20:  #684:     case imdef:
            if (not _coconut_match_temp_540) and (_coconut.isinstance(_coconut_case_match_to_20, ImageDef)):  #684:     case imdef:
                _coconut_case_match_check_20 = True  #684:     case imdef:
            if _coconut_case_match_check_20:  #684:     case imdef:
                _coconut_case_match_check_20 = False  #684:     case imdef:
                if not _coconut_case_match_check_20:  #684:     case imdef:
                    if _coconut.type(_coconut_case_match_to_20) in _coconut_self_match_types:  #684:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #684:     case imdef:
                        _coconut_case_match_check_20 = True  #684:     case imdef:

                if not _coconut_case_match_check_20:  #684:     case imdef:
                    _coconut_match_set_name_meta = _coconut_sentinel  #684:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_20) in _coconut_self_match_types:  #684:     case imdef:
                        _coconut_match_temp_549 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #684:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_549, _coconut.tuple):  #684:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #684:     case imdef:
                        if _coconut.len(_coconut_match_temp_549) < 2:  #684:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_549),))  #684:     case imdef:
                        _coconut_match_temp_550 = _coconut.getattr(_coconut_case_match_to_20, _coconut_match_temp_549[0], _coconut_sentinel)  #684:     case imdef:
                        _coconut_match_temp_558 = _coconut.getattr(_coconut_case_match_to_20, _coconut_match_temp_549[1], _coconut_sentinel)  #684:     case imdef:
                        if (_coconut_match_temp_550 is not _coconut_sentinel) and (_coconut_match_temp_558 is not _coconut_sentinel):  #684:     case imdef:
                            _coconut_match_temp_551 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #684:     case imdef:
                            _coconut_match_set_name_meta = _coconut_match_temp_558  #684:     case imdef:
                            _coconut_case_match_check_20 = True  #684:     case imdef:
                    if _coconut_case_match_check_20:  #684:     case imdef:
                        _coconut_case_match_check_20 = False  #684:     case imdef:
                        if not _coconut_case_match_check_20:  #684:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #684:     case imdef:
                            _coconut_match_set_name_ch = _coconut_sentinel  #684:     case imdef:
                            _coconut_match_set_name_vr = _coconut_sentinel  #684:     case imdef:
                            if (_coconut_match_temp_551) and (_coconut.isinstance(_coconut_match_temp_550, Numpy)) and (_coconut.len(_coconut_match_temp_550) >= 4) and (_coconut_match_temp_550[1] == "HW"):  #684:     case imdef:
                                _coconut_match_set_name_dtype = _coconut_match_temp_550[0]  #684:     case imdef:
                                _coconut_match_set_name_ch = _coconut_match_temp_550[2]  #684:     case imdef:
                                _coconut_match_set_name_vr = _coconut_match_temp_550[3]  #684:     case imdef:
                                _coconut_match_temp_552 = _coconut.len(_coconut_match_temp_550) <= _coconut.max(4, _coconut.len(_coconut_match_temp_550.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_550, "_coconut_data_defaults", {}) and _coconut_match_temp_550[i] == _coconut.getattr(_coconut_match_temp_550, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_550.__match_args__))) if _coconut.hasattr(_coconut_match_temp_550, "__match_args__") else _coconut.len(_coconut_match_temp_550) == 4  # type: ignore  #684:     case imdef:
                                if _coconut_match_temp_552:  #684:     case imdef:
                                    _coconut_case_match_check_20 = True  #684:     case imdef:
                            if _coconut_case_match_check_20:  #684:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #684:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #684:     case imdef:
                                if _coconut_match_set_name_ch is not _coconut_sentinel:  #684:     case imdef:
                                    ch = _coconut_match_set_name_ch  #684:     case imdef:
                                if _coconut_match_set_name_vr is not _coconut_sentinel:  #684:     case imdef:
                                    vr = _coconut_match_set_name_vr  #684:     case imdef:

                        if not _coconut_case_match_check_20:  #684:     case imdef:
                            if (not _coconut_match_temp_551) and (_coconut.isinstance(_coconut_match_temp_550, Numpy)):  #684:     case imdef:
                                _coconut_case_match_check_20 = True  #684:     case imdef:
                            if _coconut_case_match_check_20:  #684:     case imdef:
                                _coconut_case_match_check_20 = False  #684:     case imdef:
                                if not _coconut_case_match_check_20:  #684:     case imdef:
                                    if _coconut.type(_coconut_match_temp_550) in _coconut_self_match_types:  #684:     case imdef:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #684:     case imdef:
                                        _coconut_case_match_check_20 = True  #684:     case imdef:

                                if not _coconut_case_match_check_20:  #684:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_sentinel  #684:     case imdef:
                                    _coconut_match_set_name_ch = _coconut_sentinel  #684:     case imdef:
                                    _coconut_match_set_name_vr = _coconut_sentinel  #684:     case imdef:
                                    if not _coconut.type(_coconut_match_temp_550) in _coconut_self_match_types:  #684:     case imdef:
                                        _coconut_match_temp_553 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #684:     case imdef:
                                        if not _coconut.isinstance(_coconut_match_temp_553, _coconut.tuple):  #684:     case imdef:
                                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #684:     case imdef:
                                        if _coconut.len(_coconut_match_temp_553) < 4:  #684:     case imdef:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_553),))  #684:     case imdef:
                                        _coconut_match_temp_554 = _coconut.getattr(_coconut_match_temp_550, _coconut_match_temp_553[0], _coconut_sentinel)  #684:     case imdef:
                                        _coconut_match_temp_555 = _coconut.getattr(_coconut_match_temp_550, _coconut_match_temp_553[1], _coconut_sentinel)  #684:     case imdef:
                                        _coconut_match_temp_556 = _coconut.getattr(_coconut_match_temp_550, _coconut_match_temp_553[2], _coconut_sentinel)  #684:     case imdef:
                                        _coconut_match_temp_557 = _coconut.getattr(_coconut_match_temp_550, _coconut_match_temp_553[3], _coconut_sentinel)  #684:     case imdef:
                                        if (_coconut_match_temp_554 is not _coconut_sentinel) and (_coconut_match_temp_555 is not _coconut_sentinel) and (_coconut_match_temp_555 == "HW") and (_coconut_match_temp_556 is not _coconut_sentinel) and (_coconut_match_temp_557 is not _coconut_sentinel):  #684:     case imdef:
                                            _coconut_match_set_name_dtype = _coconut_match_temp_554  #684:     case imdef:
                                            _coconut_match_set_name_ch = _coconut_match_temp_556  #684:     case imdef:
                                            _coconut_match_set_name_vr = _coconut_match_temp_557  #684:     case imdef:
                                            _coconut_case_match_check_20 = True  #684:     case imdef:
                                    if _coconut_case_match_check_20:  #684:     case imdef:
                                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #684:     case imdef:
                                            dtype = _coconut_match_set_name_dtype  #684:     case imdef:
                                        if _coconut_match_set_name_ch is not _coconut_sentinel:  #684:     case imdef:
                                            ch = _coconut_match_set_name_ch  #684:     case imdef:
                                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #684:     case imdef:
                                            vr = _coconut_match_set_name_vr  #684:     case imdef:




                    if _coconut_case_match_check_20:  #684:     case imdef:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #684:     case imdef:
                            meta = _coconut_match_set_name_meta  #684:     case imdef:




    if _coconut_case_match_check_20:  #684:     case imdef:
        return ([(lambda a: a[None], ImageDef(Numpy(dtype, "CHW", ch, vr), (ms_add_ch_to_hw)(meta)), 1, "add_channel_dim"),])  #686:             return [(
    if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
        _coconut_match_temp_559 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
        _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
        if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
            _coconut_case_match_check_20 = False  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
            if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                if (_coconut_match_temp_559) and (_coconut.isinstance(_coconut_case_match_to_20, ImageDef)) and (_coconut.len(_coconut_case_match_to_20) >= 2):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                    _coconut_match_temp_560 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_20[1]  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                    _coconut_match_temp_567 = _coconut.len(_coconut_case_match_to_20) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_20.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_20, "_coconut_data_defaults", {}) and _coconut_case_match_to_20[i] == _coconut.getattr(_coconut_case_match_to_20, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_20.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_20, "__match_args__") else _coconut.len(_coconut_case_match_to_20) == 2  # type: ignore  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                    if _coconut_match_temp_567:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                    _coconut_case_match_check_20 = False  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                    if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        _coconut_match_set_name_dtype = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        _coconut_match_set_name_ch = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        _coconut_match_set_name_vr = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        if (_coconut_match_temp_560) and (_coconut.isinstance(_coconut_case_match_to_20[0], Numpy)) and (_coconut.len(_coconut_case_match_to_20[0]) >= 4) and (_coconut_case_match_to_20[0][1] == "BHW"):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            _coconut_match_set_name_dtype = _coconut_case_match_to_20[0][0]  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            _coconut_match_set_name_ch = _coconut_case_match_to_20[0][2]  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            _coconut_match_set_name_vr = _coconut_case_match_to_20[0][3]  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            _coconut_match_temp_561 = _coconut.len(_coconut_case_match_to_20[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_20[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_20[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_20[0][i] == _coconut.getattr(_coconut_case_match_to_20[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_20[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_20[0], "__match_args__") else _coconut.len(_coconut_case_match_to_20[0]) == 4  # type: ignore  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            if _coconut_match_temp_561:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                dtype = _coconut_match_set_name_dtype  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            if _coconut_match_set_name_ch is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                ch = _coconut_match_set_name_ch  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            if _coconut_match_set_name_vr is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                vr = _coconut_match_set_name_vr  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):

                    if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        if (not _coconut_match_temp_560) and (_coconut.isinstance(_coconut_case_match_to_20[0], Numpy)):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            _coconut_case_match_check_20 = False  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                if _coconut.type(_coconut_case_match_to_20[0]) in _coconut_self_match_types:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):

                            if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                _coconut_match_set_name_ch = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                _coconut_match_set_name_vr = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                if not _coconut.type(_coconut_case_match_to_20[0]) in _coconut_self_match_types:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_match_temp_562 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_562, _coconut.tuple):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    if _coconut.len(_coconut_match_temp_562) < 4:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_562),))  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_match_temp_563 = _coconut.getattr(_coconut_case_match_to_20[0], _coconut_match_temp_562[0], _coconut_sentinel)  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_match_temp_564 = _coconut.getattr(_coconut_case_match_to_20[0], _coconut_match_temp_562[1], _coconut_sentinel)  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_match_temp_565 = _coconut.getattr(_coconut_case_match_to_20[0], _coconut_match_temp_562[2], _coconut_sentinel)  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_match_temp_566 = _coconut.getattr(_coconut_case_match_to_20[0], _coconut_match_temp_562[3], _coconut_sentinel)  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    if (_coconut_match_temp_563 is not _coconut_sentinel) and (_coconut_match_temp_564 is not _coconut_sentinel) and (_coconut_match_temp_564 == "BHW") and (_coconut_match_temp_565 is not _coconut_sentinel) and (_coconut_match_temp_566 is not _coconut_sentinel):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        _coconut_match_set_name_dtype = _coconut_match_temp_563  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        _coconut_match_set_name_ch = _coconut_match_temp_565  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        _coconut_match_set_name_vr = _coconut_match_temp_566  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        dtype = _coconut_match_set_name_dtype  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    if _coconut_match_set_name_ch is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        ch = _coconut_match_set_name_ch  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    if _coconut_match_set_name_vr is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        vr = _coconut_match_set_name_vr  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):




                if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        meta = _coconut_match_set_name_meta  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):

            if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                if (not _coconut_match_temp_559) and (_coconut.isinstance(_coconut_case_match_to_20, ImageDef)):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                    _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                    _coconut_case_match_check_20 = False  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                    if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        if _coconut.type(_coconut_case_match_to_20) in _coconut_self_match_types:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):

                    if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        if not _coconut.type(_coconut_case_match_to_20) in _coconut_self_match_types:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            _coconut_match_temp_568 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            if not _coconut.isinstance(_coconut_match_temp_568, _coconut.tuple):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            if _coconut.len(_coconut_match_temp_568) < 2:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_568),))  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            _coconut_match_temp_569 = _coconut.getattr(_coconut_case_match_to_20, _coconut_match_temp_568[0], _coconut_sentinel)  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            _coconut_match_temp_577 = _coconut.getattr(_coconut_case_match_to_20, _coconut_match_temp_568[1], _coconut_sentinel)  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            if (_coconut_match_temp_569 is not _coconut_sentinel) and (_coconut_match_temp_577 is not _coconut_sentinel):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                _coconut_match_temp_570 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_577  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                        if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            _coconut_case_match_check_20 = False  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                _coconut_match_set_name_dtype = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                _coconut_match_set_name_ch = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                _coconut_match_set_name_vr = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                if (_coconut_match_temp_570) and (_coconut.isinstance(_coconut_match_temp_569, Numpy)) and (_coconut.len(_coconut_match_temp_569) >= 4) and (_coconut_match_temp_569[1] == "BHW"):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_match_set_name_dtype = _coconut_match_temp_569[0]  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_match_set_name_ch = _coconut_match_temp_569[2]  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_match_set_name_vr = _coconut_match_temp_569[3]  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_match_temp_571 = _coconut.len(_coconut_match_temp_569) <= _coconut.max(4, _coconut.len(_coconut_match_temp_569.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_569, "_coconut_data_defaults", {}) and _coconut_match_temp_569[i] == _coconut.getattr(_coconut_match_temp_569, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_569.__match_args__))) if _coconut.hasattr(_coconut_match_temp_569, "__match_args__") else _coconut.len(_coconut_match_temp_569) == 4  # type: ignore  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    if _coconut_match_temp_571:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        dtype = _coconut_match_set_name_dtype  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    if _coconut_match_set_name_ch is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        ch = _coconut_match_set_name_ch  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    if _coconut_match_set_name_vr is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        vr = _coconut_match_set_name_vr  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):

                            if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                if (not _coconut_match_temp_570) and (_coconut.isinstance(_coconut_match_temp_569, Numpy)):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    _coconut_case_match_check_20 = False  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                    if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        if _coconut.type(_coconut_match_temp_569) in _coconut_self_match_types:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):

                                    if not _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        _coconut_match_set_name_dtype = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        _coconut_match_set_name_ch = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        _coconut_match_set_name_vr = _coconut_sentinel  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        if not _coconut.type(_coconut_match_temp_569) in _coconut_self_match_types:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            _coconut_match_temp_572 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_572, _coconut.tuple):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            if _coconut.len(_coconut_match_temp_572) < 4:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_572),))  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            _coconut_match_temp_573 = _coconut.getattr(_coconut_match_temp_569, _coconut_match_temp_572[0], _coconut_sentinel)  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            _coconut_match_temp_574 = _coconut.getattr(_coconut_match_temp_569, _coconut_match_temp_572[1], _coconut_sentinel)  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            _coconut_match_temp_575 = _coconut.getattr(_coconut_match_temp_569, _coconut_match_temp_572[2], _coconut_sentinel)  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            _coconut_match_temp_576 = _coconut.getattr(_coconut_match_temp_569, _coconut_match_temp_572[3], _coconut_sentinel)  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            if (_coconut_match_temp_573 is not _coconut_sentinel) and (_coconut_match_temp_574 is not _coconut_sentinel) and (_coconut_match_temp_574 == "BHW") and (_coconut_match_temp_575 is not _coconut_sentinel) and (_coconut_match_temp_576 is not _coconut_sentinel):  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                                _coconut_match_set_name_dtype = _coconut_match_temp_573  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                                _coconut_match_set_name_ch = _coconut_match_temp_575  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                                _coconut_match_set_name_vr = _coconut_match_temp_576  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                                _coconut_case_match_check_20 = True  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                        if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                                dtype = _coconut_match_set_name_dtype  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            if _coconut_match_set_name_ch is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                                ch = _coconut_match_set_name_ch  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                            if _coconut_match_set_name_vr is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                                vr = _coconut_match_set_name_vr  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):




                        if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
                                meta = _coconut_match_set_name_meta  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):




        if _coconut_case_match_check_20:  #692:         match ImageDef(Numpy(dtype,"BHW",ch,vr),meta):
            return ([(lambda a: a[:, None], ImageDef(Numpy(dtype, "BCHW", ch, vr), (ms_add_ch_to_bhw)(meta)), 1, "add_channel_dim"),])  #693:             return [(


def rule_swap_RGB_BGR(imdef):  #700: def rule_swap_RGB_BGR(imdef):
    _coconut_case_match_to_21 = imdef  #701:     case imdef:
    _coconut_case_match_check_21 = False  #701:     case imdef:
    _coconut_match_temp_578 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #701:     case imdef:
    _coconut_case_match_check_21 = True  #701:     case imdef:
    if _coconut_case_match_check_21:  #701:     case imdef:
        _coconut_case_match_check_21 = False  #701:     case imdef:
        if not _coconut_case_match_check_21:  #701:     case imdef:
            _coconut_match_set_name_tl = _coconut_sentinel  #701:     case imdef:
            _coconut_match_set_name_meta = _coconut_sentinel  #701:     case imdef:
            if (_coconut_match_temp_578) and (_coconut.isinstance(_coconut_case_match_to_21, ImageDef)) and (_coconut.len(_coconut_case_match_to_21) >= 2):  #701:     case imdef:
                _coconut_match_set_name_tl = _coconut_case_match_to_21[0]  #701:     case imdef:
                _coconut_match_temp_579 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #701:     case imdef:
                _coconut_match_set_name_meta = _coconut_case_match_to_21[1]  #701:     case imdef:
                _coconut_match_temp_586 = _coconut.len(_coconut_case_match_to_21) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_21.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_21, "_coconut_data_defaults", {}) and _coconut_case_match_to_21[i] == _coconut.getattr(_coconut_case_match_to_21, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_21.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_21, "__match_args__") else _coconut.len(_coconut_case_match_to_21) == 2  # type: ignore  #701:     case imdef:
                if _coconut_match_temp_586:  #701:     case imdef:
                    _coconut_case_match_check_21 = True  #701:     case imdef:
            if _coconut_case_match_check_21:  #701:     case imdef:
                _coconut_case_match_check_21 = False  #701:     case imdef:
                if not _coconut_case_match_check_21:  #701:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_sentinel  #701:     case imdef:
                    _coconut_match_set_name_rgb_order = _coconut_sentinel  #701:     case imdef:
                    _coconut_match_set_name_vr = _coconut_sentinel  #701:     case imdef:
                    if (_coconut_match_temp_579) and (_coconut.isinstance(_coconut_case_match_to_21[0], TensorLike)) and (_coconut.len(_coconut_case_match_to_21[0]) >= 4) and (_coconut_case_match_to_21[0][1] == "BHWC"):  #701:     case imdef:
                        _coconut_match_set_name_dtype = _coconut_case_match_to_21[0][0]  #701:     case imdef:
                        _coconut_match_set_name_rgb_order = _coconut_case_match_to_21[0][2]  #701:     case imdef:
                        _coconut_match_set_name_vr = _coconut_case_match_to_21[0][3]  #701:     case imdef:
                        _coconut_match_temp_580 = _coconut.len(_coconut_case_match_to_21[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_21[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_21[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_21[0][i] == _coconut.getattr(_coconut_case_match_to_21[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_21[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_21[0], "__match_args__") else _coconut.len(_coconut_case_match_to_21[0]) == 4  # type: ignore  #701:     case imdef:
                        if _coconut_match_temp_580:  #701:     case imdef:
                            _coconut_case_match_check_21 = True  #701:     case imdef:
                    if _coconut_case_match_check_21:  #701:     case imdef:
                        _coconut_case_match_check_21 = False  #701:     case imdef:
                        if not _coconut_case_match_check_21:  #701:     case imdef:
                            if _coconut_case_match_to_21[0][2] == "RGB":  #701:     case imdef:
                                _coconut_case_match_check_21 = True  #701:     case imdef:

                        if not _coconut_case_match_check_21:  #701:     case imdef:
                            if _coconut_case_match_to_21[0][2] == "BGR":  #701:     case imdef:
                                _coconut_case_match_check_21 = True  #701:     case imdef:


                    if _coconut_case_match_check_21:  #701:     case imdef:
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #701:     case imdef:
                            dtype = _coconut_match_set_name_dtype  #701:     case imdef:
                        if _coconut_match_set_name_rgb_order is not _coconut_sentinel:  #701:     case imdef:
                            rgb_order = _coconut_match_set_name_rgb_order  #701:     case imdef:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #701:     case imdef:
                            vr = _coconut_match_set_name_vr  #701:     case imdef:

                if not _coconut_case_match_check_21:  #701:     case imdef:
                    if (not _coconut_match_temp_579) and (_coconut.isinstance(_coconut_case_match_to_21[0], TensorLike)):  #701:     case imdef:
                        _coconut_case_match_check_21 = True  #701:     case imdef:
                    if _coconut_case_match_check_21:  #701:     case imdef:
                        _coconut_case_match_check_21 = False  #701:     case imdef:
                        if not _coconut_case_match_check_21:  #701:     case imdef:
                            if _coconut.type(_coconut_case_match_to_21[0]) in _coconut_self_match_types:  #701:     case imdef:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #701:     case imdef:
                                _coconut_case_match_check_21 = True  #701:     case imdef:

                        if not _coconut_case_match_check_21:  #701:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #701:     case imdef:
                            _coconut_match_set_name_rgb_order = _coconut_sentinel  #701:     case imdef:
                            _coconut_match_set_name_vr = _coconut_sentinel  #701:     case imdef:
                            if not _coconut.type(_coconut_case_match_to_21[0]) in _coconut_self_match_types:  #701:     case imdef:
                                _coconut_match_temp_581 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #701:     case imdef:
                                if not _coconut.isinstance(_coconut_match_temp_581, _coconut.tuple):  #701:     case imdef:
                                    raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #701:     case imdef:
                                if _coconut.len(_coconut_match_temp_581) < 4:  #701:     case imdef:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_581),))  #701:     case imdef:
                                _coconut_match_temp_582 = _coconut.getattr(_coconut_case_match_to_21[0], _coconut_match_temp_581[0], _coconut_sentinel)  #701:     case imdef:
                                _coconut_match_temp_583 = _coconut.getattr(_coconut_case_match_to_21[0], _coconut_match_temp_581[1], _coconut_sentinel)  #701:     case imdef:
                                _coconut_match_temp_584 = _coconut.getattr(_coconut_case_match_to_21[0], _coconut_match_temp_581[2], _coconut_sentinel)  #701:     case imdef:
                                _coconut_match_temp_585 = _coconut.getattr(_coconut_case_match_to_21[0], _coconut_match_temp_581[3], _coconut_sentinel)  #701:     case imdef:
                                if (_coconut_match_temp_582 is not _coconut_sentinel) and (_coconut_match_temp_583 is not _coconut_sentinel) and (_coconut_match_temp_583 == "BHWC") and (_coconut_match_temp_584 is not _coconut_sentinel) and (_coconut_match_temp_585 is not _coconut_sentinel):  #701:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_match_temp_582  #701:     case imdef:
                                    _coconut_match_set_name_rgb_order = _coconut_match_temp_584  #701:     case imdef:
                                    _coconut_match_set_name_vr = _coconut_match_temp_585  #701:     case imdef:
                                    _coconut_case_match_check_21 = True  #701:     case imdef:
                            if _coconut_case_match_check_21:  #701:     case imdef:
                                _coconut_case_match_check_21 = False  #701:     case imdef:
                                if not _coconut_case_match_check_21:  #701:     case imdef:
                                    if _coconut_match_temp_584 == "RGB":  #701:     case imdef:
                                        _coconut_case_match_check_21 = True  #701:     case imdef:

                                if not _coconut_case_match_check_21:  #701:     case imdef:
                                    if _coconut_match_temp_584 == "BGR":  #701:     case imdef:
                                        _coconut_case_match_check_21 = True  #701:     case imdef:


                            if _coconut_case_match_check_21:  #701:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #701:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #701:     case imdef:
                                if _coconut_match_set_name_rgb_order is not _coconut_sentinel:  #701:     case imdef:
                                    rgb_order = _coconut_match_set_name_rgb_order  #701:     case imdef:
                                if _coconut_match_set_name_vr is not _coconut_sentinel:  #701:     case imdef:
                                    vr = _coconut_match_set_name_vr  #701:     case imdef:




            if _coconut_case_match_check_21:  #701:     case imdef:
                if _coconut_match_set_name_tl is not _coconut_sentinel:  #701:     case imdef:
                    tl = _coconut_match_set_name_tl  #701:     case imdef:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #701:     case imdef:
                    meta = _coconut_match_set_name_meta  #701:     case imdef:

        if not _coconut_case_match_check_21:  #701:     case imdef:
            if (not _coconut_match_temp_578) and (_coconut.isinstance(_coconut_case_match_to_21, ImageDef)):  #701:     case imdef:
                _coconut_case_match_check_21 = True  #701:     case imdef:
            if _coconut_case_match_check_21:  #701:     case imdef:
                _coconut_case_match_check_21 = False  #701:     case imdef:
                if not _coconut_case_match_check_21:  #701:     case imdef:
                    if _coconut.type(_coconut_case_match_to_21) in _coconut_self_match_types:  #701:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #701:     case imdef:
                        _coconut_case_match_check_21 = True  #701:     case imdef:

                if not _coconut_case_match_check_21:  #701:     case imdef:
                    _coconut_match_set_name_tl = _coconut_sentinel  #701:     case imdef:
                    _coconut_match_set_name_meta = _coconut_sentinel  #701:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_21) in _coconut_self_match_types:  #701:     case imdef:
                        _coconut_match_temp_587 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #701:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_587, _coconut.tuple):  #701:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #701:     case imdef:
                        if _coconut.len(_coconut_match_temp_587) < 2:  #701:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_587),))  #701:     case imdef:
                        _coconut_match_temp_588 = _coconut.getattr(_coconut_case_match_to_21, _coconut_match_temp_587[0], _coconut_sentinel)  #701:     case imdef:
                        _coconut_match_temp_596 = _coconut.getattr(_coconut_case_match_to_21, _coconut_match_temp_587[1], _coconut_sentinel)  #701:     case imdef:
                        if (_coconut_match_temp_588 is not _coconut_sentinel) and (_coconut_match_temp_596 is not _coconut_sentinel):  #701:     case imdef:
                            _coconut_match_set_name_tl = _coconut_match_temp_588  #701:     case imdef:
                            _coconut_match_temp_589 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #701:     case imdef:
                            _coconut_match_set_name_meta = _coconut_match_temp_596  #701:     case imdef:
                            _coconut_case_match_check_21 = True  #701:     case imdef:
                    if _coconut_case_match_check_21:  #701:     case imdef:
                        _coconut_case_match_check_21 = False  #701:     case imdef:
                        if not _coconut_case_match_check_21:  #701:     case imdef:
                            _coconut_match_set_name_dtype = _coconut_sentinel  #701:     case imdef:
                            _coconut_match_set_name_rgb_order = _coconut_sentinel  #701:     case imdef:
                            _coconut_match_set_name_vr = _coconut_sentinel  #701:     case imdef:
                            if (_coconut_match_temp_589) and (_coconut.isinstance(_coconut_match_temp_588, TensorLike)) and (_coconut.len(_coconut_match_temp_588) >= 4) and (_coconut_match_temp_588[1] == "BHWC"):  #701:     case imdef:
                                _coconut_match_set_name_dtype = _coconut_match_temp_588[0]  #701:     case imdef:
                                _coconut_match_set_name_rgb_order = _coconut_match_temp_588[2]  #701:     case imdef:
                                _coconut_match_set_name_vr = _coconut_match_temp_588[3]  #701:     case imdef:
                                _coconut_match_temp_590 = _coconut.len(_coconut_match_temp_588) <= _coconut.max(4, _coconut.len(_coconut_match_temp_588.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_588, "_coconut_data_defaults", {}) and _coconut_match_temp_588[i] == _coconut.getattr(_coconut_match_temp_588, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_588.__match_args__))) if _coconut.hasattr(_coconut_match_temp_588, "__match_args__") else _coconut.len(_coconut_match_temp_588) == 4  # type: ignore  #701:     case imdef:
                                if _coconut_match_temp_590:  #701:     case imdef:
                                    _coconut_case_match_check_21 = True  #701:     case imdef:
                            if _coconut_case_match_check_21:  #701:     case imdef:
                                _coconut_case_match_check_21 = False  #701:     case imdef:
                                if not _coconut_case_match_check_21:  #701:     case imdef:
                                    if _coconut_match_temp_588[2] == "RGB":  #701:     case imdef:
                                        _coconut_case_match_check_21 = True  #701:     case imdef:

                                if not _coconut_case_match_check_21:  #701:     case imdef:
                                    if _coconut_match_temp_588[2] == "BGR":  #701:     case imdef:
                                        _coconut_case_match_check_21 = True  #701:     case imdef:


                            if _coconut_case_match_check_21:  #701:     case imdef:
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #701:     case imdef:
                                    dtype = _coconut_match_set_name_dtype  #701:     case imdef:
                                if _coconut_match_set_name_rgb_order is not _coconut_sentinel:  #701:     case imdef:
                                    rgb_order = _coconut_match_set_name_rgb_order  #701:     case imdef:
                                if _coconut_match_set_name_vr is not _coconut_sentinel:  #701:     case imdef:
                                    vr = _coconut_match_set_name_vr  #701:     case imdef:

                        if not _coconut_case_match_check_21:  #701:     case imdef:
                            if (not _coconut_match_temp_589) and (_coconut.isinstance(_coconut_match_temp_588, TensorLike)):  #701:     case imdef:
                                _coconut_case_match_check_21 = True  #701:     case imdef:
                            if _coconut_case_match_check_21:  #701:     case imdef:
                                _coconut_case_match_check_21 = False  #701:     case imdef:
                                if not _coconut_case_match_check_21:  #701:     case imdef:
                                    if _coconut.type(_coconut_match_temp_588) in _coconut_self_match_types:  #701:     case imdef:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports 1)")  #701:     case imdef:
                                        _coconut_case_match_check_21 = True  #701:     case imdef:

                                if not _coconut_case_match_check_21:  #701:     case imdef:
                                    _coconut_match_set_name_dtype = _coconut_sentinel  #701:     case imdef:
                                    _coconut_match_set_name_rgb_order = _coconut_sentinel  #701:     case imdef:
                                    _coconut_match_set_name_vr = _coconut_sentinel  #701:     case imdef:
                                    if not _coconut.type(_coconut_match_temp_588) in _coconut_self_match_types:  #701:     case imdef:
                                        _coconut_match_temp_591 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #701:     case imdef:
                                        if not _coconut.isinstance(_coconut_match_temp_591, _coconut.tuple):  #701:     case imdef:
                                            raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #701:     case imdef:
                                        if _coconut.len(_coconut_match_temp_591) < 4:  #701:     case imdef:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_591),))  #701:     case imdef:
                                        _coconut_match_temp_592 = _coconut.getattr(_coconut_match_temp_588, _coconut_match_temp_591[0], _coconut_sentinel)  #701:     case imdef:
                                        _coconut_match_temp_593 = _coconut.getattr(_coconut_match_temp_588, _coconut_match_temp_591[1], _coconut_sentinel)  #701:     case imdef:
                                        _coconut_match_temp_594 = _coconut.getattr(_coconut_match_temp_588, _coconut_match_temp_591[2], _coconut_sentinel)  #701:     case imdef:
                                        _coconut_match_temp_595 = _coconut.getattr(_coconut_match_temp_588, _coconut_match_temp_591[3], _coconut_sentinel)  #701:     case imdef:
                                        if (_coconut_match_temp_592 is not _coconut_sentinel) and (_coconut_match_temp_593 is not _coconut_sentinel) and (_coconut_match_temp_593 == "BHWC") and (_coconut_match_temp_594 is not _coconut_sentinel) and (_coconut_match_temp_595 is not _coconut_sentinel):  #701:     case imdef:
                                            _coconut_match_set_name_dtype = _coconut_match_temp_592  #701:     case imdef:
                                            _coconut_match_set_name_rgb_order = _coconut_match_temp_594  #701:     case imdef:
                                            _coconut_match_set_name_vr = _coconut_match_temp_595  #701:     case imdef:
                                            _coconut_case_match_check_21 = True  #701:     case imdef:
                                    if _coconut_case_match_check_21:  #701:     case imdef:
                                        _coconut_case_match_check_21 = False  #701:     case imdef:
                                        if not _coconut_case_match_check_21:  #701:     case imdef:
                                            if _coconut_match_temp_594 == "RGB":  #701:     case imdef:
                                                _coconut_case_match_check_21 = True  #701:     case imdef:

                                        if not _coconut_case_match_check_21:  #701:     case imdef:
                                            if _coconut_match_temp_594 == "BGR":  #701:     case imdef:
                                                _coconut_case_match_check_21 = True  #701:     case imdef:


                                    if _coconut_case_match_check_21:  #701:     case imdef:
                                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #701:     case imdef:
                                            dtype = _coconut_match_set_name_dtype  #701:     case imdef:
                                        if _coconut_match_set_name_rgb_order is not _coconut_sentinel:  #701:     case imdef:
                                            rgb_order = _coconut_match_set_name_rgb_order  #701:     case imdef:
                                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #701:     case imdef:
                                            vr = _coconut_match_set_name_vr  #701:     case imdef:




                    if _coconut_case_match_check_21:  #701:     case imdef:
                        if _coconut_match_set_name_tl is not _coconut_sentinel:  #701:     case imdef:
                            tl = _coconut_match_set_name_tl  #701:     case imdef:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #701:     case imdef:
                            meta = _coconut_match_set_name_meta  #701:     case imdef:




    if _coconut_case_match_check_21:  #701:     case imdef:
        return ([(lambda a: a[:, :, :, [2, 1, 0]], ImageDef(tl.__class__(dtype, "BHWC", "RGB" if rgb_order.startswith("B") else "BGR", vr), meta), 1, "swap rgb or bgr"),])  #703:             return [(


def rule_BGR_to_LAB(imdef):  #710: def rule_BGR_to_LAB(imdef):
    from skimage.color import rgb2lab  #711:     from skimage.color import rgb2lab,lab2rgb
    from skimage.color import lab2rgb  #711:     from skimage.color import rgb2lab,lab2rgb
    _coconut_case_match_to_22 = imdef  #712:     case imdef:
    _coconut_case_match_check_22 = False  #712:     case imdef:
    _coconut_match_temp_597 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #712:     case imdef:
    _coconut_case_match_check_22 = True  #712:     case imdef:
    if _coconut_case_match_check_22:  #712:     case imdef:
        _coconut_case_match_check_22 = False  #712:     case imdef:
        if not _coconut_case_match_check_22:  #712:     case imdef:
            _coconut_match_set_name_meta = _coconut_sentinel  #712:     case imdef:
            if (_coconut_match_temp_597) and (_coconut.isinstance(_coconut_case_match_to_22, ImageDef)) and (_coconut.len(_coconut_case_match_to_22) >= 2):  #712:     case imdef:
                _coconut_match_temp_598 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #712:     case imdef:
                _coconut_match_set_name_meta = _coconut_case_match_to_22[1]  #712:     case imdef:
                _coconut_match_temp_605 = _coconut.len(_coconut_case_match_to_22) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_22.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_22, "_coconut_data_defaults", {}) and _coconut_case_match_to_22[i] == _coconut.getattr(_coconut_case_match_to_22, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_22.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_22, "__match_args__") else _coconut.len(_coconut_case_match_to_22) == 2  # type: ignore  #712:     case imdef:
                if _coconut_match_temp_605:  #712:     case imdef:
                    _coconut_case_match_check_22 = True  #712:     case imdef:
            if _coconut_case_match_check_22:  #712:     case imdef:
                _coconut_case_match_check_22 = False  #712:     case imdef:
                if not _coconut_case_match_check_22:  #712:     case imdef:
                    if (_coconut_match_temp_598) and (_coconut.isinstance(_coconut_case_match_to_22[0], Numpy)) and (_coconut.len(_coconut_case_match_to_22[0]) >= 4) and (_coconut_case_match_to_22[0][0] == "float32") and (_coconut_case_match_to_22[0][1] == "HWC") and (_coconut_case_match_to_22[0][2] == "BGR") and (_coconut_case_match_to_22[0][3] == VR_0_1):  #712:     case imdef:
                        _coconut_match_temp_599 = _coconut.len(_coconut_case_match_to_22[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_22[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_22[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_22[0][i] == _coconut.getattr(_coconut_case_match_to_22[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_22[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_22[0], "__match_args__") else _coconut.len(_coconut_case_match_to_22[0]) == 4  # type: ignore  #712:     case imdef:
                        if _coconut_match_temp_599:  #712:     case imdef:
                            _coconut_case_match_check_22 = True  #712:     case imdef:

                if not _coconut_case_match_check_22:  #712:     case imdef:
                    if (not _coconut_match_temp_598) and (_coconut.isinstance(_coconut_case_match_to_22[0], Numpy)):  #712:     case imdef:
                        _coconut_case_match_check_22 = True  #712:     case imdef:
                    if _coconut_case_match_check_22:  #712:     case imdef:
                        _coconut_case_match_check_22 = False  #712:     case imdef:
                        if not _coconut_case_match_check_22:  #712:     case imdef:
                            if _coconut.type(_coconut_case_match_to_22[0]) in _coconut_self_match_types:  #712:     case imdef:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #712:     case imdef:
                                _coconut_case_match_check_22 = True  #712:     case imdef:

                        if not _coconut_case_match_check_22:  #712:     case imdef:
                            if not _coconut.type(_coconut_case_match_to_22[0]) in _coconut_self_match_types:  #712:     case imdef:
                                _coconut_match_temp_600 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #712:     case imdef:
                                if not _coconut.isinstance(_coconut_match_temp_600, _coconut.tuple):  #712:     case imdef:
                                    raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #712:     case imdef:
                                if _coconut.len(_coconut_match_temp_600) < 4:  #712:     case imdef:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_600),))  #712:     case imdef:
                                _coconut_match_temp_601 = _coconut.getattr(_coconut_case_match_to_22[0], _coconut_match_temp_600[0], _coconut_sentinel)  #712:     case imdef:
                                _coconut_match_temp_602 = _coconut.getattr(_coconut_case_match_to_22[0], _coconut_match_temp_600[1], _coconut_sentinel)  #712:     case imdef:
                                _coconut_match_temp_603 = _coconut.getattr(_coconut_case_match_to_22[0], _coconut_match_temp_600[2], _coconut_sentinel)  #712:     case imdef:
                                _coconut_match_temp_604 = _coconut.getattr(_coconut_case_match_to_22[0], _coconut_match_temp_600[3], _coconut_sentinel)  #712:     case imdef:
                                if (_coconut_match_temp_601 is not _coconut_sentinel) and (_coconut_match_temp_601 == "float32") and (_coconut_match_temp_602 is not _coconut_sentinel) and (_coconut_match_temp_602 == "HWC") and (_coconut_match_temp_603 is not _coconut_sentinel) and (_coconut_match_temp_603 == "BGR") and (_coconut_match_temp_604 is not _coconut_sentinel) and (_coconut_match_temp_604 == VR_0_1):  #712:     case imdef:
                                    _coconut_case_match_check_22 = True  #712:     case imdef:




            if _coconut_case_match_check_22:  #712:     case imdef:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #712:     case imdef:
                    meta = _coconut_match_set_name_meta  #712:     case imdef:

        if not _coconut_case_match_check_22:  #712:     case imdef:
            if (not _coconut_match_temp_597) and (_coconut.isinstance(_coconut_case_match_to_22, ImageDef)):  #712:     case imdef:
                _coconut_case_match_check_22 = True  #712:     case imdef:
            if _coconut_case_match_check_22:  #712:     case imdef:
                _coconut_case_match_check_22 = False  #712:     case imdef:
                if not _coconut_case_match_check_22:  #712:     case imdef:
                    if _coconut.type(_coconut_case_match_to_22) in _coconut_self_match_types:  #712:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #712:     case imdef:
                        _coconut_case_match_check_22 = True  #712:     case imdef:

                if not _coconut_case_match_check_22:  #712:     case imdef:
                    _coconut_match_set_name_meta = _coconut_sentinel  #712:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_22) in _coconut_self_match_types:  #712:     case imdef:
                        _coconut_match_temp_606 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #712:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_606, _coconut.tuple):  #712:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #712:     case imdef:
                        if _coconut.len(_coconut_match_temp_606) < 2:  #712:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_606),))  #712:     case imdef:
                        _coconut_match_temp_607 = _coconut.getattr(_coconut_case_match_to_22, _coconut_match_temp_606[0], _coconut_sentinel)  #712:     case imdef:
                        _coconut_match_temp_615 = _coconut.getattr(_coconut_case_match_to_22, _coconut_match_temp_606[1], _coconut_sentinel)  #712:     case imdef:
                        if (_coconut_match_temp_607 is not _coconut_sentinel) and (_coconut_match_temp_615 is not _coconut_sentinel):  #712:     case imdef:
                            _coconut_match_temp_608 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #712:     case imdef:
                            _coconut_match_set_name_meta = _coconut_match_temp_615  #712:     case imdef:
                            _coconut_case_match_check_22 = True  #712:     case imdef:
                    if _coconut_case_match_check_22:  #712:     case imdef:
                        _coconut_case_match_check_22 = False  #712:     case imdef:
                        if not _coconut_case_match_check_22:  #712:     case imdef:
                            if (_coconut_match_temp_608) and (_coconut.isinstance(_coconut_match_temp_607, Numpy)) and (_coconut.len(_coconut_match_temp_607) >= 4) and (_coconut_match_temp_607[0] == "float32") and (_coconut_match_temp_607[1] == "HWC") and (_coconut_match_temp_607[2] == "BGR") and (_coconut_match_temp_607[3] == VR_0_1):  #712:     case imdef:
                                _coconut_match_temp_609 = _coconut.len(_coconut_match_temp_607) <= _coconut.max(4, _coconut.len(_coconut_match_temp_607.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_607, "_coconut_data_defaults", {}) and _coconut_match_temp_607[i] == _coconut.getattr(_coconut_match_temp_607, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_607.__match_args__))) if _coconut.hasattr(_coconut_match_temp_607, "__match_args__") else _coconut.len(_coconut_match_temp_607) == 4  # type: ignore  #712:     case imdef:
                                if _coconut_match_temp_609:  #712:     case imdef:
                                    _coconut_case_match_check_22 = True  #712:     case imdef:

                        if not _coconut_case_match_check_22:  #712:     case imdef:
                            if (not _coconut_match_temp_608) and (_coconut.isinstance(_coconut_match_temp_607, Numpy)):  #712:     case imdef:
                                _coconut_case_match_check_22 = True  #712:     case imdef:
                            if _coconut_case_match_check_22:  #712:     case imdef:
                                _coconut_case_match_check_22 = False  #712:     case imdef:
                                if not _coconut_case_match_check_22:  #712:     case imdef:
                                    if _coconut.type(_coconut_match_temp_607) in _coconut_self_match_types:  #712:     case imdef:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #712:     case imdef:
                                        _coconut_case_match_check_22 = True  #712:     case imdef:

                                if not _coconut_case_match_check_22:  #712:     case imdef:
                                    if not _coconut.type(_coconut_match_temp_607) in _coconut_self_match_types:  #712:     case imdef:
                                        _coconut_match_temp_610 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #712:     case imdef:
                                        if not _coconut.isinstance(_coconut_match_temp_610, _coconut.tuple):  #712:     case imdef:
                                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #712:     case imdef:
                                        if _coconut.len(_coconut_match_temp_610) < 4:  #712:     case imdef:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_610),))  #712:     case imdef:
                                        _coconut_match_temp_611 = _coconut.getattr(_coconut_match_temp_607, _coconut_match_temp_610[0], _coconut_sentinel)  #712:     case imdef:
                                        _coconut_match_temp_612 = _coconut.getattr(_coconut_match_temp_607, _coconut_match_temp_610[1], _coconut_sentinel)  #712:     case imdef:
                                        _coconut_match_temp_613 = _coconut.getattr(_coconut_match_temp_607, _coconut_match_temp_610[2], _coconut_sentinel)  #712:     case imdef:
                                        _coconut_match_temp_614 = _coconut.getattr(_coconut_match_temp_607, _coconut_match_temp_610[3], _coconut_sentinel)  #712:     case imdef:
                                        if (_coconut_match_temp_611 is not _coconut_sentinel) and (_coconut_match_temp_611 == "float32") and (_coconut_match_temp_612 is not _coconut_sentinel) and (_coconut_match_temp_612 == "HWC") and (_coconut_match_temp_613 is not _coconut_sentinel) and (_coconut_match_temp_613 == "BGR") and (_coconut_match_temp_614 is not _coconut_sentinel) and (_coconut_match_temp_614 == VR_0_1):  #712:     case imdef:
                                            _coconut_case_match_check_22 = True  #712:     case imdef:




                    if _coconut_case_match_check_22:  #712:     case imdef:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #712:     case imdef:
                            meta = _coconut_match_set_name_meta  #712:     case imdef:




    if _coconut_case_match_check_22:  #712:     case imdef:
        return ([(rgb2lab, ImageDef(Numpy("float32", "HWC", "LAB", "VR_LAB"), meta), 1, "bgr_0_1 to lab"),])  #714:             return[(
    if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
        _coconut_match_temp_616 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
        _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
        if _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
            _coconut_case_match_check_22 = False  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
            if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                if (_coconut_match_temp_616) and (_coconut.isinstance(_coconut_case_match_to_22, ImageDef)) and (_coconut.len(_coconut_case_match_to_22) >= 2):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                    _coconut_match_temp_617 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_22[1]  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                    _coconut_match_temp_624 = _coconut.len(_coconut_case_match_to_22) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_22.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_22, "_coconut_data_defaults", {}) and _coconut_case_match_to_22[i] == _coconut.getattr(_coconut_case_match_to_22, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_22.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_22, "__match_args__") else _coconut.len(_coconut_case_match_to_22) == 2  # type: ignore  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                    if _coconut_match_temp_624:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                        _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                if _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                    _coconut_case_match_check_22 = False  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                    if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                        if (_coconut_match_temp_617) and (_coconut.isinstance(_coconut_case_match_to_22[0], Numpy)) and (_coconut.len(_coconut_case_match_to_22[0]) >= 4) and (_coconut_case_match_to_22[0][0] == "float32") and (_coconut_case_match_to_22[0][1] == "HWC") and (_coconut_case_match_to_22[0][2] == "LAB") and (_coconut_case_match_to_22[0][3] == "VR_LAB"):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            _coconut_match_temp_618 = _coconut.len(_coconut_case_match_to_22[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_22[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_22[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_22[0][i] == _coconut.getattr(_coconut_case_match_to_22[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_22[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_22[0], "__match_args__") else _coconut.len(_coconut_case_match_to_22[0]) == 4  # type: ignore  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            if _coconut_match_temp_618:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):

                    if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                        if (not _coconut_match_temp_617) and (_coconut.isinstance(_coconut_case_match_to_22[0], Numpy)):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                        if _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            _coconut_case_match_check_22 = False  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                if _coconut.type(_coconut_case_match_to_22[0]) in _coconut_self_match_types:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):

                            if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                if not _coconut.type(_coconut_case_match_to_22[0]) in _coconut_self_match_types:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    _coconut_match_temp_619 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_619, _coconut.tuple):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    if _coconut.len(_coconut_match_temp_619) < 4:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_619),))  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    _coconut_match_temp_620 = _coconut.getattr(_coconut_case_match_to_22[0], _coconut_match_temp_619[0], _coconut_sentinel)  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    _coconut_match_temp_621 = _coconut.getattr(_coconut_case_match_to_22[0], _coconut_match_temp_619[1], _coconut_sentinel)  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    _coconut_match_temp_622 = _coconut.getattr(_coconut_case_match_to_22[0], _coconut_match_temp_619[2], _coconut_sentinel)  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    _coconut_match_temp_623 = _coconut.getattr(_coconut_case_match_to_22[0], _coconut_match_temp_619[3], _coconut_sentinel)  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    if (_coconut_match_temp_620 is not _coconut_sentinel) and (_coconut_match_temp_620 == "float32") and (_coconut_match_temp_621 is not _coconut_sentinel) and (_coconut_match_temp_621 == "HWC") and (_coconut_match_temp_622 is not _coconut_sentinel) and (_coconut_match_temp_622 == "LAB") and (_coconut_match_temp_623 is not _coconut_sentinel) and (_coconut_match_temp_623 == "VR_LAB"):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                        _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):




                if _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                        meta = _coconut_match_set_name_meta  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):

            if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                if (not _coconut_match_temp_616) and (_coconut.isinstance(_coconut_case_match_to_22, ImageDef)):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                    _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                if _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                    _coconut_case_match_check_22 = False  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                    if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                        if _coconut.type(_coconut_case_match_to_22) in _coconut_self_match_types:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):

                    if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                        if not _coconut.type(_coconut_case_match_to_22) in _coconut_self_match_types:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            _coconut_match_temp_625 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            if not _coconut.isinstance(_coconut_match_temp_625, _coconut.tuple):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            if _coconut.len(_coconut_match_temp_625) < 2:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_625),))  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            _coconut_match_temp_626 = _coconut.getattr(_coconut_case_match_to_22, _coconut_match_temp_625[0], _coconut_sentinel)  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            _coconut_match_temp_634 = _coconut.getattr(_coconut_case_match_to_22, _coconut_match_temp_625[1], _coconut_sentinel)  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            if (_coconut_match_temp_626 is not _coconut_sentinel) and (_coconut_match_temp_634 is not _coconut_sentinel):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                _coconut_match_temp_627 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_634  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                        if _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            _coconut_case_match_check_22 = False  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                if (_coconut_match_temp_627) and (_coconut.isinstance(_coconut_match_temp_626, Numpy)) and (_coconut.len(_coconut_match_temp_626) >= 4) and (_coconut_match_temp_626[0] == "float32") and (_coconut_match_temp_626[1] == "HWC") and (_coconut_match_temp_626[2] == "LAB") and (_coconut_match_temp_626[3] == "VR_LAB"):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    _coconut_match_temp_628 = _coconut.len(_coconut_match_temp_626) <= _coconut.max(4, _coconut.len(_coconut_match_temp_626.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_626, "_coconut_data_defaults", {}) and _coconut_match_temp_626[i] == _coconut.getattr(_coconut_match_temp_626, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_626.__match_args__))) if _coconut.hasattr(_coconut_match_temp_626, "__match_args__") else _coconut.len(_coconut_match_temp_626) == 4  # type: ignore  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    if _coconut_match_temp_628:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                        _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):

                            if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                if (not _coconut_match_temp_627) and (_coconut.isinstance(_coconut_match_temp_626, Numpy)):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                if _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    _coconut_case_match_check_22 = False  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                    if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                        if _coconut.type(_coconut_match_temp_626) in _coconut_self_match_types:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                            _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):

                                    if not _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                        if not _coconut.type(_coconut_match_temp_626) in _coconut_self_match_types:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                            _coconut_match_temp_629 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_629, _coconut.tuple):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                            if _coconut.len(_coconut_match_temp_629) < 4:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_629),))  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                            _coconut_match_temp_630 = _coconut.getattr(_coconut_match_temp_626, _coconut_match_temp_629[0], _coconut_sentinel)  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                            _coconut_match_temp_631 = _coconut.getattr(_coconut_match_temp_626, _coconut_match_temp_629[1], _coconut_sentinel)  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                            _coconut_match_temp_632 = _coconut.getattr(_coconut_match_temp_626, _coconut_match_temp_629[2], _coconut_sentinel)  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                            _coconut_match_temp_633 = _coconut.getattr(_coconut_match_temp_626, _coconut_match_temp_629[3], _coconut_sentinel)  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                            if (_coconut_match_temp_630 is not _coconut_sentinel) and (_coconut_match_temp_630 == "float32") and (_coconut_match_temp_631 is not _coconut_sentinel) and (_coconut_match_temp_631 == "HWC") and (_coconut_match_temp_632 is not _coconut_sentinel) and (_coconut_match_temp_632 == "LAB") and (_coconut_match_temp_633 is not _coconut_sentinel) and (_coconut_match_temp_633 == "VR_LAB"):  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                                _coconut_case_match_check_22 = True  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):




                        if _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
                                meta = _coconut_match_set_name_meta  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):




        if _coconut_case_match_check_22:  #720:         match ImageDef(Numpy("float32","HWC","LAB","VR_LAB"),meta):
            return ([(lab2rgb, ImageDef(Numpy("float32", "HWC", "BGR", VR_0_1), meta), 1, "lab to bgr_0_1"),])  #721:             return [(



def make_grid(imgs, nrow, padding=0):  #729: def make_grid(imgs, nrow, padding=0):
    """Numpy配列の複数枚の画像を、1枚の画像にタイルします

    Arguments:
        imgs {np.ndarray} -- 複数枚の画像からなるテンソル
        nrow {int} -- 1行あたりにタイルする枚数

    Keyword Arguments:
        padding {int} -- グリッドの間隔 (default: {0})

    Returns:
        [np.ndarray] -- 3階テンソル。1枚の画像
    """  #741:     """
    assert imgs.ndim == 4 and nrow > 0  #742:     assert imgs.ndim == 4 and nrow > 0
    batch, height, width, ch = imgs.shape  #743:     batch, height, width, ch = imgs.shape
    n = nrow * (batch // nrow + np.sign(batch % nrow))  #744:     n = nrow * (batch // nrow + np.sign(batch % nrow))
    ncol = n // nrow  #745:     ncol = n // nrow
    pad = np.zeros((n - batch, height, width, ch), imgs.dtype)  #746:     pad = np.zeros((n - batch, height, width, ch), imgs.dtype)
    x = np.concatenate([imgs, pad], axis=0)  #747:     x = np.concatenate([imgs, pad], axis=0)
# border padding if required
    if padding > 0:  #749:     if padding > 0:
        x = np.pad(x, ((0, 0), (0, padding), (0, padding), (0, 0)), "constant", constant_values=(0, 0))  # 下と右だけにpaddingを入れる  #750:         x = np.pad(x, ((0, 0), (0, padding), (0, padding), (0, 0)),
        height += padding  #752:         height += padding
        width += padding  #753:         width += padding
    x = x.reshape(ncol, nrow, height, width, ch)  #754:     x = x.reshape(ncol, nrow, height, width, ch)
    x = x.transpose([0, 2, 1, 3, 4])  # (ncol, height, nrow, width, ch)  #755:     x = x.transpose([0, 2, 1, 3, 4])  # (ncol, height, nrow, width, ch)
    x = x.reshape(height * ncol, width * nrow, ch)  #756:     x = x.reshape(height * ncol, width * nrow, ch)
    if padding > 0:  #757:     if padding > 0:
        x = x[:(height * ncol - padding), :(width * nrow - padding), :]  # 右端と下端のpaddingを削除  #758:         x = x[:(height * ncol - padding),:(width * nrow - padding),:] # 右端と下端のpaddingを削除
    return (x)  #759:     return x
