#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb3d2fff8

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

from math import sqrt  #1: from math import sqrt

import PIL.Image  #3: import PIL.Image

from omni_cv_rules.coconut.convert import *  #5: from omni_cv_rules.coconut.convert import *
from frozendict import frozendict  #6: from frozendict import frozendict
if _coconut.typing.TYPE_CHECKING:  #7: from typing import Mapping
    from typing import Mapping  #7: from typing import Mapping
else:  #7: from typing import Mapping
    try:  #7: from typing import Mapping
        Mapping = _coconut.typing.Mapping  #7: from typing import Mapping
    except _coconut.AttributeError as _coconut_imp_err:  #7: from typing import Mapping
        raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #7: from typing import Mapping
from loguru import logger  #8: from loguru import logger
import numpy as np  #9: import numpy as np
from omni_cv_rules.coconut.visualization import infer_widget  #10: from omni_cv_rules.coconut.visualization import infer_widget
from omni_cv_rules.place_holder.torch_proxy import torch  #11: from omni_cv_rules.place_holder.torch_proxy import torch
def imagedef2dict(imdef: 'ImageDef'):  #12: def imagedef2dict(imdef:ImageDef):
    _coconut_case_match_to_1 = imdef  #13:     case imdef:
    _coconut_case_match_check_1 = False  #13:     case imdef:
    _coconut_match_temp_24 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #13:     case imdef:
    _coconut_case_match_check_1 = True  #13:     case imdef:
    if _coconut_case_match_check_1:  #13:     case imdef:
        _coconut_case_match_check_1 = False  #13:     case imdef:
        if not _coconut_case_match_check_1:  #13:     case imdef:
            _coconut_match_set_name_data_type = _coconut_sentinel  #13:     case imdef:
            _coconut_match_set_name_meta = _coconut_sentinel  #13:     case imdef:
            if (_coconut_match_temp_24) and (_coconut.isinstance(_coconut_case_match_to_1, ImageDef)) and (_coconut.len(_coconut_case_match_to_1) >= 2):  #13:     case imdef:
                _coconut_match_set_name_data_type = _coconut_case_match_to_1[0]  #13:     case imdef:
                _coconut_match_set_name_meta = _coconut_case_match_to_1[1]  #13:     case imdef:
                _coconut_match_temp_25 = _coconut.len(_coconut_case_match_to_1) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_1.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_1, "_coconut_data_defaults", {}) and _coconut_case_match_to_1[i] == _coconut.getattr(_coconut_case_match_to_1, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_1.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_1, "__match_args__") else _coconut.len(_coconut_case_match_to_1) == 2  # type: ignore  #13:     case imdef:
                if _coconut_match_temp_25:  #13:     case imdef:
                    _coconut_case_match_check_1 = True  #13:     case imdef:
            if _coconut_case_match_check_1:  #13:     case imdef:
                if _coconut_match_set_name_data_type is not _coconut_sentinel:  #13:     case imdef:
                    data_type = _coconut_match_set_name_data_type  #13:     case imdef:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #13:     case imdef:
                    meta = _coconut_match_set_name_meta  #13:     case imdef:

        if not _coconut_case_match_check_1:  #13:     case imdef:
            if (not _coconut_match_temp_24) and (_coconut.isinstance(_coconut_case_match_to_1, ImageDef)):  #13:     case imdef:
                _coconut_case_match_check_1 = True  #13:     case imdef:
            if _coconut_case_match_check_1:  #13:     case imdef:
                _coconut_case_match_check_1 = False  #13:     case imdef:
                if not _coconut_case_match_check_1:  #13:     case imdef:
                    if _coconut.type(_coconut_case_match_to_1) in _coconut_self_match_types:  #13:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #13:     case imdef:
                        _coconut_case_match_check_1 = True  #13:     case imdef:

                if not _coconut_case_match_check_1:  #13:     case imdef:
                    _coconut_match_set_name_data_type = _coconut_sentinel  #13:     case imdef:
                    _coconut_match_set_name_meta = _coconut_sentinel  #13:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_1) in _coconut_self_match_types:  #13:     case imdef:
                        _coconut_match_temp_26 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #13:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_26, _coconut.tuple):  #13:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #13:     case imdef:
                        if _coconut.len(_coconut_match_temp_26) < 2:  #13:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_26),))  #13:     case imdef:
                        _coconut_match_temp_27 = _coconut.getattr(_coconut_case_match_to_1, _coconut_match_temp_26[0], _coconut_sentinel)  #13:     case imdef:
                        _coconut_match_temp_28 = _coconut.getattr(_coconut_case_match_to_1, _coconut_match_temp_26[1], _coconut_sentinel)  #13:     case imdef:
                        if (_coconut_match_temp_27 is not _coconut_sentinel) and (_coconut_match_temp_28 is not _coconut_sentinel):  #13:     case imdef:
                            _coconut_match_set_name_data_type = _coconut_match_temp_27  #13:     case imdef:
                            _coconut_match_set_name_meta = _coconut_match_temp_28  #13:     case imdef:
                            _coconut_case_match_check_1 = True  #13:     case imdef:
                    if _coconut_case_match_check_1:  #13:     case imdef:
                        if _coconut_match_set_name_data_type is not _coconut_sentinel:  #13:     case imdef:
                            data_type = _coconut_match_set_name_data_type  #13:     case imdef:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #13:     case imdef:
                            meta = _coconut_match_set_name_meta  #13:     case imdef:




    if _coconut_case_match_check_1:  #13:     case imdef:
        _coconut_case_match_to_0 = data_type  #13:     case imdef:
        _coconut_case_match_check_0 = False  #13:     case imdef:
        _coconut_match_temp_0 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #13:     case imdef:
        _coconut_case_match_check_0 = True  #13:     case imdef:
        if _coconut_case_match_check_0:  #13:     case imdef:
            _coconut_case_match_check_0 = False  #13:     case imdef:
            if not _coconut_case_match_check_0:  #13:     case imdef:
                _coconut_match_set_name_dtype = _coconut_sentinel  #13:     case imdef:
                _coconut_match_set_name_arrange = _coconut_sentinel  #13:     case imdef:
                _coconut_match_set_name_ch_rpr = _coconut_sentinel  #13:     case imdef:
                _coconut_match_set_name_v_range = _coconut_sentinel  #13:     case imdef:
                if (_coconut_match_temp_0) and (_coconut.isinstance(_coconut_case_match_to_0, Numpy)) and (_coconut.len(_coconut_case_match_to_0) >= 4):  #13:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_case_match_to_0[0]  #13:     case imdef:
                    _coconut_match_set_name_arrange = _coconut_case_match_to_0[1]  #13:     case imdef:
                    _coconut_match_set_name_ch_rpr = _coconut_case_match_to_0[2]  #13:     case imdef:
                    _coconut_match_set_name_v_range = _coconut_case_match_to_0[3]  #13:     case imdef:
                    _coconut_match_temp_1 = _coconut.len(_coconut_case_match_to_0) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {}) and _coconut_case_match_to_0[i] == _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_0.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0, "__match_args__") else _coconut.len(_coconut_case_match_to_0) == 4  # type: ignore  #13:     case imdef:
                    if _coconut_match_temp_1:  #13:     case imdef:
                        _coconut_case_match_check_0 = True  #13:     case imdef:
                if _coconut_case_match_check_0:  #13:     case imdef:
                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #13:     case imdef:
                        dtype = _coconut_match_set_name_dtype  #13:     case imdef:
                    if _coconut_match_set_name_arrange is not _coconut_sentinel:  #13:     case imdef:
                        arrange = _coconut_match_set_name_arrange  #13:     case imdef:
                    if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #13:     case imdef:
                        ch_rpr = _coconut_match_set_name_ch_rpr  #13:     case imdef:
                    if _coconut_match_set_name_v_range is not _coconut_sentinel:  #13:     case imdef:
                        v_range = _coconut_match_set_name_v_range  #13:     case imdef:

            if not _coconut_case_match_check_0:  #13:     case imdef:
                if (not _coconut_match_temp_0) and (_coconut.isinstance(_coconut_case_match_to_0, Numpy)):  #13:     case imdef:
                    _coconut_case_match_check_0 = True  #13:     case imdef:
                if _coconut_case_match_check_0:  #13:     case imdef:
                    _coconut_case_match_check_0 = False  #13:     case imdef:
                    if not _coconut_case_match_check_0:  #13:     case imdef:
                        if _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #13:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #13:     case imdef:
                            _coconut_case_match_check_0 = True  #13:     case imdef:

                    if not _coconut_case_match_check_0:  #13:     case imdef:
                        _coconut_match_set_name_dtype = _coconut_sentinel  #13:     case imdef:
                        _coconut_match_set_name_arrange = _coconut_sentinel  #13:     case imdef:
                        _coconut_match_set_name_ch_rpr = _coconut_sentinel  #13:     case imdef:
                        _coconut_match_set_name_v_range = _coconut_sentinel  #13:     case imdef:
                        if not _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #13:     case imdef:
                            _coconut_match_temp_2 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #13:     case imdef:
                            if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #13:     case imdef:
                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #13:     case imdef:
                            if _coconut.len(_coconut_match_temp_2) < 4:  #13:     case imdef:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #13:     case imdef:
                            _coconut_match_temp_3 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_2[0], _coconut_sentinel)  #13:     case imdef:
                            _coconut_match_temp_4 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_2[1], _coconut_sentinel)  #13:     case imdef:
                            _coconut_match_temp_5 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_2[2], _coconut_sentinel)  #13:     case imdef:
                            _coconut_match_temp_6 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_2[3], _coconut_sentinel)  #13:     case imdef:
                            if (_coconut_match_temp_3 is not _coconut_sentinel) and (_coconut_match_temp_4 is not _coconut_sentinel) and (_coconut_match_temp_5 is not _coconut_sentinel) and (_coconut_match_temp_6 is not _coconut_sentinel):  #13:     case imdef:
                                _coconut_match_set_name_dtype = _coconut_match_temp_3  #13:     case imdef:
                                _coconut_match_set_name_arrange = _coconut_match_temp_4  #13:     case imdef:
                                _coconut_match_set_name_ch_rpr = _coconut_match_temp_5  #13:     case imdef:
                                _coconut_match_set_name_v_range = _coconut_match_temp_6  #13:     case imdef:
                                _coconut_case_match_check_0 = True  #13:     case imdef:
                        if _coconut_case_match_check_0:  #13:     case imdef:
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #13:     case imdef:
                                dtype = _coconut_match_set_name_dtype  #13:     case imdef:
                            if _coconut_match_set_name_arrange is not _coconut_sentinel:  #13:     case imdef:
                                arrange = _coconut_match_set_name_arrange  #13:     case imdef:
                            if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #13:     case imdef:
                                ch_rpr = _coconut_match_set_name_ch_rpr  #13:     case imdef:
                            if _coconut_match_set_name_v_range is not _coconut_sentinel:  #13:     case imdef:
                                v_range = _coconut_match_set_name_v_range  #13:     case imdef:




        if _coconut_case_match_check_0:  #13:     case imdef:
            info = dict(type="numpy", dtype=dtype, arrange=arrange, ch_rpr=ch_rpr, v_range=str(v_range))  #17:                     info = dict(type="numpy",dtype=dtype,arrange=arrange,ch_rpr=ch_rpr,v_range=str(v_range))
        if not _coconut_case_match_check_0:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_match_temp_7 = _coconut.getattr(Torch, "_coconut_is_data", False) or _coconut.isinstance(Torch, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Torch)  # type: ignore  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_case_match_check_0 = True  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
            if _coconut_case_match_check_0:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_case_match_check_0 = False  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                if not _coconut_case_match_check_0:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    _coconut_match_set_name_dtype = _coconut_sentinel  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    _coconut_match_set_name_arrange = _coconut_sentinel  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    _coconut_match_set_name_ch_rpr = _coconut_sentinel  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    _coconut_match_set_name_v_range = _coconut_sentinel  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    if (_coconut_match_temp_7) and (_coconut.isinstance(_coconut_case_match_to_0, Torch)) and (_coconut.len(_coconut_case_match_to_0) >= 4):  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_match_set_name_dtype = _coconut_case_match_to_0[0]  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_match_set_name_arrange = _coconut_case_match_to_0[1]  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_match_set_name_ch_rpr = _coconut_case_match_to_0[2]  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_match_set_name_v_range = _coconut_case_match_to_0[3]  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_match_temp_8 = _coconut.len(_coconut_case_match_to_0) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {}) and _coconut_case_match_to_0[i] == _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_0.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0, "__match_args__") else _coconut.len(_coconut_case_match_to_0) == 4  # type: ignore  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if _coconut_match_temp_8:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            _coconut_case_match_check_0 = True  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    if _coconut_case_match_check_0:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            dtype = _coconut_match_set_name_dtype  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if _coconut_match_set_name_arrange is not _coconut_sentinel:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            arrange = _coconut_match_set_name_arrange  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            ch_rpr = _coconut_match_set_name_ch_rpr  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if _coconut_match_set_name_v_range is not _coconut_sentinel:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            v_range = _coconut_match_set_name_v_range  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):

                if not _coconut_case_match_check_0:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    if (not _coconut_match_temp_7) and (_coconut.isinstance(_coconut_case_match_to_0, Torch)):  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_case_match_check_0 = True  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    if _coconut_case_match_check_0:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_case_match_check_0 = False  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if not _coconut_case_match_check_0:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            if _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports 1)")  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_case_match_check_0 = True  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):

                        if not _coconut_case_match_check_0:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            _coconut_match_set_name_dtype = _coconut_sentinel  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            _coconut_match_set_name_arrange = _coconut_sentinel  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            _coconut_match_set_name_v_range = _coconut_sentinel  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            if not _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_match_temp_9 = _coconut.getattr(Torch, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if not _coconut.isinstance(_coconut_match_temp_9, _coconut.tuple):  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    raise _coconut.TypeError("Torch.__match_args__ must be a tuple")  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if _coconut.len(_coconut_match_temp_9) < 4:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports %s)" % (_coconut.len(_coconut_match_temp_9),))  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_match_temp_10 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_9[0], _coconut_sentinel)  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_match_temp_11 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_9[1], _coconut_sentinel)  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_match_temp_12 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_9[2], _coconut_sentinel)  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_match_temp_13 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_9[3], _coconut_sentinel)  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if (_coconut_match_temp_10 is not _coconut_sentinel) and (_coconut_match_temp_11 is not _coconut_sentinel) and (_coconut_match_temp_12 is not _coconut_sentinel) and (_coconut_match_temp_13 is not _coconut_sentinel):  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    _coconut_match_set_name_dtype = _coconut_match_temp_10  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    _coconut_match_set_name_arrange = _coconut_match_temp_11  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    _coconut_match_set_name_ch_rpr = _coconut_match_temp_12  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    _coconut_match_set_name_v_range = _coconut_match_temp_13  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    _coconut_case_match_check_0 = True  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            if _coconut_case_match_check_0:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    dtype = _coconut_match_set_name_dtype  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if _coconut_match_set_name_arrange is not _coconut_sentinel:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    arrange = _coconut_match_set_name_arrange  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    ch_rpr = _coconut_match_set_name_ch_rpr  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if _coconut_match_set_name_v_range is not _coconut_sentinel:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    v_range = _coconut_match_set_name_v_range  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):




            if _coconut_case_match_check_0:  #18:                 match Torch(dtype,arrange,ch_rpr,v_range):
                info = dict(type="torch", dtype=dtype, arrange=arrange, ch_rpr=ch_rpr, v_range=str(v_range))  #19:                     info = dict(type="torch",dtype=dtype,arrange=arrange,ch_rpr=ch_rpr,v_range=str(v_range))
        if not _coconut_case_match_check_0:  #20:                 match PILImages(mode,ch_rpr):
            _coconut_match_temp_14 = _coconut.getattr(PILImages, "_coconut_is_data", False) or _coconut.isinstance(PILImages, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImages)  # type: ignore  #20:                 match PILImages(mode,ch_rpr):
            _coconut_case_match_check_0 = True  #20:                 match PILImages(mode,ch_rpr):
            if _coconut_case_match_check_0:  #20:                 match PILImages(mode,ch_rpr):
                _coconut_case_match_check_0 = False  #20:                 match PILImages(mode,ch_rpr):
                if not _coconut_case_match_check_0:  #20:                 match PILImages(mode,ch_rpr):
                    _coconut_match_set_name_mode = _coconut_sentinel  #20:                 match PILImages(mode,ch_rpr):
                    _coconut_match_set_name_ch_rpr = _coconut_sentinel  #20:                 match PILImages(mode,ch_rpr):
                    if (_coconut_match_temp_14) and (_coconut.isinstance(_coconut_case_match_to_0, PILImages)) and (_coconut.len(_coconut_case_match_to_0) >= 2):  #20:                 match PILImages(mode,ch_rpr):
                        _coconut_match_set_name_mode = _coconut_case_match_to_0[0]  #20:                 match PILImages(mode,ch_rpr):
                        _coconut_match_set_name_ch_rpr = _coconut_case_match_to_0[1]  #20:                 match PILImages(mode,ch_rpr):
                        _coconut_match_temp_15 = _coconut.len(_coconut_case_match_to_0) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {}) and _coconut_case_match_to_0[i] == _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_0.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0, "__match_args__") else _coconut.len(_coconut_case_match_to_0) == 2  # type: ignore  #20:                 match PILImages(mode,ch_rpr):
                        if _coconut_match_temp_15:  #20:                 match PILImages(mode,ch_rpr):
                            _coconut_case_match_check_0 = True  #20:                 match PILImages(mode,ch_rpr):
                    if _coconut_case_match_check_0:  #20:                 match PILImages(mode,ch_rpr):
                        if _coconut_match_set_name_mode is not _coconut_sentinel:  #20:                 match PILImages(mode,ch_rpr):
                            mode = _coconut_match_set_name_mode  #20:                 match PILImages(mode,ch_rpr):
                        if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #20:                 match PILImages(mode,ch_rpr):
                            ch_rpr = _coconut_match_set_name_ch_rpr  #20:                 match PILImages(mode,ch_rpr):

                if not _coconut_case_match_check_0:  #20:                 match PILImages(mode,ch_rpr):
                    if (not _coconut_match_temp_14) and (_coconut.isinstance(_coconut_case_match_to_0, PILImages)):  #20:                 match PILImages(mode,ch_rpr):
                        _coconut_case_match_check_0 = True  #20:                 match PILImages(mode,ch_rpr):
                    if _coconut_case_match_check_0:  #20:                 match PILImages(mode,ch_rpr):
                        _coconut_case_match_check_0 = False  #20:                 match PILImages(mode,ch_rpr):
                        if not _coconut_case_match_check_0:  #20:                 match PILImages(mode,ch_rpr):
                            if _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #20:                 match PILImages(mode,ch_rpr):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports 1)")  #20:                 match PILImages(mode,ch_rpr):
                                _coconut_case_match_check_0 = True  #20:                 match PILImages(mode,ch_rpr):

                        if not _coconut_case_match_check_0:  #20:                 match PILImages(mode,ch_rpr):
                            _coconut_match_set_name_mode = _coconut_sentinel  #20:                 match PILImages(mode,ch_rpr):
                            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #20:                 match PILImages(mode,ch_rpr):
                            if not _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #20:                 match PILImages(mode,ch_rpr):
                                _coconut_match_temp_16 = _coconut.getattr(PILImages, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #20:                 match PILImages(mode,ch_rpr):
                                if not _coconut.isinstance(_coconut_match_temp_16, _coconut.tuple):  #20:                 match PILImages(mode,ch_rpr):
                                    raise _coconut.TypeError("PILImages.__match_args__ must be a tuple")  #20:                 match PILImages(mode,ch_rpr):
                                if _coconut.len(_coconut_match_temp_16) < 2:  #20:                 match PILImages(mode,ch_rpr):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports %s)" % (_coconut.len(_coconut_match_temp_16),))  #20:                 match PILImages(mode,ch_rpr):
                                _coconut_match_temp_17 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_16[0], _coconut_sentinel)  #20:                 match PILImages(mode,ch_rpr):
                                _coconut_match_temp_18 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_16[1], _coconut_sentinel)  #20:                 match PILImages(mode,ch_rpr):
                                if (_coconut_match_temp_17 is not _coconut_sentinel) and (_coconut_match_temp_18 is not _coconut_sentinel):  #20:                 match PILImages(mode,ch_rpr):
                                    _coconut_match_set_name_mode = _coconut_match_temp_17  #20:                 match PILImages(mode,ch_rpr):
                                    _coconut_match_set_name_ch_rpr = _coconut_match_temp_18  #20:                 match PILImages(mode,ch_rpr):
                                    _coconut_case_match_check_0 = True  #20:                 match PILImages(mode,ch_rpr):
                            if _coconut_case_match_check_0:  #20:                 match PILImages(mode,ch_rpr):
                                if _coconut_match_set_name_mode is not _coconut_sentinel:  #20:                 match PILImages(mode,ch_rpr):
                                    mode = _coconut_match_set_name_mode  #20:                 match PILImages(mode,ch_rpr):
                                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #20:                 match PILImages(mode,ch_rpr):
                                    ch_rpr = _coconut_match_set_name_ch_rpr  #20:                 match PILImages(mode,ch_rpr):




            if _coconut_case_match_check_0:  #20:                 match PILImages(mode,ch_rpr):
                info = dict(type="images", ch_rpr=ch_rpr, mode=mode)  #21:                     info = dict(type="images",ch_rpr=ch_rpr,mode=mode)
        if not _coconut_case_match_check_0:  #22:                 match PILImage(mode,ch_rpr):
            _coconut_match_temp_19 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #22:                 match PILImage(mode,ch_rpr):
            _coconut_case_match_check_0 = True  #22:                 match PILImage(mode,ch_rpr):
            if _coconut_case_match_check_0:  #22:                 match PILImage(mode,ch_rpr):
                _coconut_case_match_check_0 = False  #22:                 match PILImage(mode,ch_rpr):
                if not _coconut_case_match_check_0:  #22:                 match PILImage(mode,ch_rpr):
                    _coconut_match_set_name_mode = _coconut_sentinel  #22:                 match PILImage(mode,ch_rpr):
                    _coconut_match_set_name_ch_rpr = _coconut_sentinel  #22:                 match PILImage(mode,ch_rpr):
                    if (_coconut_match_temp_19) and (_coconut.isinstance(_coconut_case_match_to_0, PILImage)) and (_coconut.len(_coconut_case_match_to_0) >= 2):  #22:                 match PILImage(mode,ch_rpr):
                        _coconut_match_set_name_mode = _coconut_case_match_to_0[0]  #22:                 match PILImage(mode,ch_rpr):
                        _coconut_match_set_name_ch_rpr = _coconut_case_match_to_0[1]  #22:                 match PILImage(mode,ch_rpr):
                        _coconut_match_temp_20 = _coconut.len(_coconut_case_match_to_0) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {}) and _coconut_case_match_to_0[i] == _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_0.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0, "__match_args__") else _coconut.len(_coconut_case_match_to_0) == 2  # type: ignore  #22:                 match PILImage(mode,ch_rpr):
                        if _coconut_match_temp_20:  #22:                 match PILImage(mode,ch_rpr):
                            _coconut_case_match_check_0 = True  #22:                 match PILImage(mode,ch_rpr):
                    if _coconut_case_match_check_0:  #22:                 match PILImage(mode,ch_rpr):
                        if _coconut_match_set_name_mode is not _coconut_sentinel:  #22:                 match PILImage(mode,ch_rpr):
                            mode = _coconut_match_set_name_mode  #22:                 match PILImage(mode,ch_rpr):
                        if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #22:                 match PILImage(mode,ch_rpr):
                            ch_rpr = _coconut_match_set_name_ch_rpr  #22:                 match PILImage(mode,ch_rpr):

                if not _coconut_case_match_check_0:  #22:                 match PILImage(mode,ch_rpr):
                    if (not _coconut_match_temp_19) and (_coconut.isinstance(_coconut_case_match_to_0, PILImage)):  #22:                 match PILImage(mode,ch_rpr):
                        _coconut_case_match_check_0 = True  #22:                 match PILImage(mode,ch_rpr):
                    if _coconut_case_match_check_0:  #22:                 match PILImage(mode,ch_rpr):
                        _coconut_case_match_check_0 = False  #22:                 match PILImage(mode,ch_rpr):
                        if not _coconut_case_match_check_0:  #22:                 match PILImage(mode,ch_rpr):
                            if _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #22:                 match PILImage(mode,ch_rpr):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #22:                 match PILImage(mode,ch_rpr):
                                _coconut_case_match_check_0 = True  #22:                 match PILImage(mode,ch_rpr):

                        if not _coconut_case_match_check_0:  #22:                 match PILImage(mode,ch_rpr):
                            _coconut_match_set_name_mode = _coconut_sentinel  #22:                 match PILImage(mode,ch_rpr):
                            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #22:                 match PILImage(mode,ch_rpr):
                            if not _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #22:                 match PILImage(mode,ch_rpr):
                                _coconut_match_temp_21 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #22:                 match PILImage(mode,ch_rpr):
                                if not _coconut.isinstance(_coconut_match_temp_21, _coconut.tuple):  #22:                 match PILImage(mode,ch_rpr):
                                    raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #22:                 match PILImage(mode,ch_rpr):
                                if _coconut.len(_coconut_match_temp_21) < 2:  #22:                 match PILImage(mode,ch_rpr):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_21),))  #22:                 match PILImage(mode,ch_rpr):
                                _coconut_match_temp_22 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_21[0], _coconut_sentinel)  #22:                 match PILImage(mode,ch_rpr):
                                _coconut_match_temp_23 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_21[1], _coconut_sentinel)  #22:                 match PILImage(mode,ch_rpr):
                                if (_coconut_match_temp_22 is not _coconut_sentinel) and (_coconut_match_temp_23 is not _coconut_sentinel):  #22:                 match PILImage(mode,ch_rpr):
                                    _coconut_match_set_name_mode = _coconut_match_temp_22  #22:                 match PILImage(mode,ch_rpr):
                                    _coconut_match_set_name_ch_rpr = _coconut_match_temp_23  #22:                 match PILImage(mode,ch_rpr):
                                    _coconut_case_match_check_0 = True  #22:                 match PILImage(mode,ch_rpr):
                            if _coconut_case_match_check_0:  #22:                 match PILImage(mode,ch_rpr):
                                if _coconut_match_set_name_mode is not _coconut_sentinel:  #22:                 match PILImage(mode,ch_rpr):
                                    mode = _coconut_match_set_name_mode  #22:                 match PILImage(mode,ch_rpr):
                                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #22:                 match PILImage(mode,ch_rpr):
                                    ch_rpr = _coconut_match_set_name_ch_rpr  #22:                 match PILImage(mode,ch_rpr):




            if _coconut_case_match_check_0:  #22:                 match PILImage(mode,ch_rpr):
                info = dict(type="image", ch_rpr=ch_rpr, mode=mode)  #23:                     info = dict(type="image",ch_rpr=ch_rpr,mode=mode)
        if not _coconut_case_match_check_0:  #24:             else:
            raise RuntimeError("cannot convert unknown imagedef:{_coconut_format_0} to dict.".format(_coconut_format_0=(imdef)))  #25:                 raise RuntimeError(f"cannot convert unknown imagedef:{imdef} to dict.")
        return (frozendict(meta=meta, **info))  #26:             return frozendict(
    if not _coconut_case_match_check_1:  #30:     else:
        raise RuntimeError("cannot convert unknown imdef:{_coconut_format_0} to dict.".format(_coconut_format_0=(imdef)))  #31:         raise RuntimeError(f"cannot convert unknown imdef:{imdef} to dict.")



def cast_imdef_to_dict(state):  #34: def cast_imdef_to_dict(state):
    if isinstance(state, ImageDef):  #35:     if isinstance(state,ImageDef):
        return ([imagedef2dict(state),])  #36:         return [imagedef2dict(state)]


def cast_imdef_str_to_imdef(state):  #38: def cast_imdef_str_to_imdef(state):
    if isinstance(state, str):  #39:     if isinstance(state,str):
        try:  #40:         try:
            res = str_to_img_def(state)  #41:             res = str_to_img_def(state)
            return ([res,])  #42:             return [res]
        except Exception as e:  #43:         except Exception as e:
            pass  #44:             pass

def imdef2imdef_str(imdef):  #45: def imdef2imdef_str(imdef):
    _coconut_case_match_to_3 = imdef  #46:     case imdef:
    _coconut_case_match_check_3 = False  #46:     case imdef:
    _coconut_match_temp_53 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #46:     case imdef:
    _coconut_case_match_check_3 = True  #46:     case imdef:
    if _coconut_case_match_check_3:  #46:     case imdef:
        _coconut_case_match_check_3 = False  #46:     case imdef:
        if not _coconut_case_match_check_3:  #46:     case imdef:
            _coconut_match_set_name_data_type = _coconut_sentinel  #46:     case imdef:
            _coconut_match_set_name_meta = _coconut_sentinel  #46:     case imdef:
            if (_coconut_match_temp_53) and (_coconut.isinstance(_coconut_case_match_to_3, ImageDef)) and (_coconut.len(_coconut_case_match_to_3) >= 2):  #46:     case imdef:
                _coconut_match_set_name_data_type = _coconut_case_match_to_3[0]  #46:     case imdef:
                _coconut_match_set_name_meta = _coconut_case_match_to_3[1]  #46:     case imdef:
                _coconut_match_temp_54 = _coconut.len(_coconut_case_match_to_3) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_3.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {}) and _coconut_case_match_to_3[i] == _coconut.getattr(_coconut_case_match_to_3, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_3.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_3, "__match_args__") else _coconut.len(_coconut_case_match_to_3) == 2  # type: ignore  #46:     case imdef:
                if _coconut_match_temp_54:  #46:     case imdef:
                    _coconut_case_match_check_3 = True  #46:     case imdef:
            if _coconut_case_match_check_3:  #46:     case imdef:
                if _coconut_match_set_name_data_type is not _coconut_sentinel:  #46:     case imdef:
                    data_type = _coconut_match_set_name_data_type  #46:     case imdef:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #46:     case imdef:
                    meta = _coconut_match_set_name_meta  #46:     case imdef:

        if not _coconut_case_match_check_3:  #46:     case imdef:
            if (not _coconut_match_temp_53) and (_coconut.isinstance(_coconut_case_match_to_3, ImageDef)):  #46:     case imdef:
                _coconut_case_match_check_3 = True  #46:     case imdef:
            if _coconut_case_match_check_3:  #46:     case imdef:
                _coconut_case_match_check_3 = False  #46:     case imdef:
                if not _coconut_case_match_check_3:  #46:     case imdef:
                    if _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #46:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #46:     case imdef:
                        _coconut_case_match_check_3 = True  #46:     case imdef:

                if not _coconut_case_match_check_3:  #46:     case imdef:
                    _coconut_match_set_name_data_type = _coconut_sentinel  #46:     case imdef:
                    _coconut_match_set_name_meta = _coconut_sentinel  #46:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_3) in _coconut_self_match_types:  #46:     case imdef:
                        _coconut_match_temp_55 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #46:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_55, _coconut.tuple):  #46:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #46:     case imdef:
                        if _coconut.len(_coconut_match_temp_55) < 2:  #46:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_55),))  #46:     case imdef:
                        _coconut_match_temp_56 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_55[0], _coconut_sentinel)  #46:     case imdef:
                        _coconut_match_temp_57 = _coconut.getattr(_coconut_case_match_to_3, _coconut_match_temp_55[1], _coconut_sentinel)  #46:     case imdef:
                        if (_coconut_match_temp_56 is not _coconut_sentinel) and (_coconut_match_temp_57 is not _coconut_sentinel):  #46:     case imdef:
                            _coconut_match_set_name_data_type = _coconut_match_temp_56  #46:     case imdef:
                            _coconut_match_set_name_meta = _coconut_match_temp_57  #46:     case imdef:
                            _coconut_case_match_check_3 = True  #46:     case imdef:
                    if _coconut_case_match_check_3:  #46:     case imdef:
                        if _coconut_match_set_name_data_type is not _coconut_sentinel:  #46:     case imdef:
                            data_type = _coconut_match_set_name_data_type  #46:     case imdef:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #46:     case imdef:
                            meta = _coconut_match_set_name_meta  #46:     case imdef:




    if _coconut_case_match_check_3:  #46:     case imdef:
        _coconut_case_match_to_2 = data_type  #46:     case imdef:
        _coconut_case_match_check_2 = False  #46:     case imdef:
        _coconut_match_temp_29 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #46:     case imdef:
        _coconut_case_match_check_2 = True  #46:     case imdef:
        if _coconut_case_match_check_2:  #46:     case imdef:
            _coconut_case_match_check_2 = False  #46:     case imdef:
            if not _coconut_case_match_check_2:  #46:     case imdef:
                _coconut_match_set_name_dtype = _coconut_sentinel  #46:     case imdef:
                _coconut_match_set_name_arrange = _coconut_sentinel  #46:     case imdef:
                _coconut_match_set_name_ch_rpr = _coconut_sentinel  #46:     case imdef:
                _coconut_match_set_name_v_range = _coconut_sentinel  #46:     case imdef:
                if (_coconut_match_temp_29) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)) and (_coconut.len(_coconut_case_match_to_2) >= 4):  #46:     case imdef:
                    _coconut_match_set_name_dtype = _coconut_case_match_to_2[0]  #46:     case imdef:
                    _coconut_match_set_name_arrange = _coconut_case_match_to_2[1]  #46:     case imdef:
                    _coconut_match_set_name_ch_rpr = _coconut_case_match_to_2[2]  #46:     case imdef:
                    _coconut_match_set_name_v_range = _coconut_case_match_to_2[3]  #46:     case imdef:
                    _coconut_match_temp_30 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 4  # type: ignore  #46:     case imdef:
                    if _coconut_match_temp_30:  #46:     case imdef:
                        _coconut_case_match_check_2 = True  #46:     case imdef:
                if _coconut_case_match_check_2:  #46:     case imdef:
                    if _coconut_match_set_name_dtype is not _coconut_sentinel:  #46:     case imdef:
                        dtype = _coconut_match_set_name_dtype  #46:     case imdef:
                    if _coconut_match_set_name_arrange is not _coconut_sentinel:  #46:     case imdef:
                        arrange = _coconut_match_set_name_arrange  #46:     case imdef:
                    if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #46:     case imdef:
                        ch_rpr = _coconut_match_set_name_ch_rpr  #46:     case imdef:
                    if _coconut_match_set_name_v_range is not _coconut_sentinel:  #46:     case imdef:
                        v_range = _coconut_match_set_name_v_range  #46:     case imdef:

            if not _coconut_case_match_check_2:  #46:     case imdef:
                if (not _coconut_match_temp_29) and (_coconut.isinstance(_coconut_case_match_to_2, Numpy)):  #46:     case imdef:
                    _coconut_case_match_check_2 = True  #46:     case imdef:
                if _coconut_case_match_check_2:  #46:     case imdef:
                    _coconut_case_match_check_2 = False  #46:     case imdef:
                    if not _coconut_case_match_check_2:  #46:     case imdef:
                        if _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #46:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #46:     case imdef:
                            _coconut_case_match_check_2 = True  #46:     case imdef:

                    if not _coconut_case_match_check_2:  #46:     case imdef:
                        _coconut_match_set_name_dtype = _coconut_sentinel  #46:     case imdef:
                        _coconut_match_set_name_arrange = _coconut_sentinel  #46:     case imdef:
                        _coconut_match_set_name_ch_rpr = _coconut_sentinel  #46:     case imdef:
                        _coconut_match_set_name_v_range = _coconut_sentinel  #46:     case imdef:
                        if not _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #46:     case imdef:
                            _coconut_match_temp_31 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #46:     case imdef:
                            if not _coconut.isinstance(_coconut_match_temp_31, _coconut.tuple):  #46:     case imdef:
                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #46:     case imdef:
                            if _coconut.len(_coconut_match_temp_31) < 4:  #46:     case imdef:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_31),))  #46:     case imdef:
                            _coconut_match_temp_32 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_31[0], _coconut_sentinel)  #46:     case imdef:
                            _coconut_match_temp_33 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_31[1], _coconut_sentinel)  #46:     case imdef:
                            _coconut_match_temp_34 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_31[2], _coconut_sentinel)  #46:     case imdef:
                            _coconut_match_temp_35 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_31[3], _coconut_sentinel)  #46:     case imdef:
                            if (_coconut_match_temp_32 is not _coconut_sentinel) and (_coconut_match_temp_33 is not _coconut_sentinel) and (_coconut_match_temp_34 is not _coconut_sentinel) and (_coconut_match_temp_35 is not _coconut_sentinel):  #46:     case imdef:
                                _coconut_match_set_name_dtype = _coconut_match_temp_32  #46:     case imdef:
                                _coconut_match_set_name_arrange = _coconut_match_temp_33  #46:     case imdef:
                                _coconut_match_set_name_ch_rpr = _coconut_match_temp_34  #46:     case imdef:
                                _coconut_match_set_name_v_range = _coconut_match_temp_35  #46:     case imdef:
                                _coconut_case_match_check_2 = True  #46:     case imdef:
                        if _coconut_case_match_check_2:  #46:     case imdef:
                            if _coconut_match_set_name_dtype is not _coconut_sentinel:  #46:     case imdef:
                                dtype = _coconut_match_set_name_dtype  #46:     case imdef:
                            if _coconut_match_set_name_arrange is not _coconut_sentinel:  #46:     case imdef:
                                arrange = _coconut_match_set_name_arrange  #46:     case imdef:
                            if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #46:     case imdef:
                                ch_rpr = _coconut_match_set_name_ch_rpr  #46:     case imdef:
                            if _coconut_match_set_name_v_range is not _coconut_sentinel:  #46:     case imdef:
                                v_range = _coconut_match_set_name_v_range  #46:     case imdef:




        if _coconut_case_match_check_2:  #46:     case imdef:
            base = "numpy,{_coconut_format_0},{_coconut_format_1},{_coconut_format_2},{_coconut_format_3}".format(_coconut_format_0=(dtype), _coconut_format_1=(arrange), _coconut_format_2=(ch_rpr), _coconut_format_3=(v_range))  #50:                     base = f"numpy,{dtype},{arrange},{ch_rpr},{v_range}"
        if not _coconut_case_match_check_2:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_match_temp_36 = _coconut.getattr(Torch, "_coconut_is_data", False) or _coconut.isinstance(Torch, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Torch)  # type: ignore  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
            _coconut_case_match_check_2 = True  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
            if _coconut_case_match_check_2:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                _coconut_case_match_check_2 = False  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                if not _coconut_case_match_check_2:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    _coconut_match_set_name_dtype = _coconut_sentinel  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    _coconut_match_set_name_arrange = _coconut_sentinel  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    _coconut_match_set_name_ch_rpr = _coconut_sentinel  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    _coconut_match_set_name_v_range = _coconut_sentinel  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    if (_coconut_match_temp_36) and (_coconut.isinstance(_coconut_case_match_to_2, Torch)) and (_coconut.len(_coconut_case_match_to_2) >= 4):  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_match_set_name_dtype = _coconut_case_match_to_2[0]  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_match_set_name_arrange = _coconut_case_match_to_2[1]  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_match_set_name_ch_rpr = _coconut_case_match_to_2[2]  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_match_set_name_v_range = _coconut_case_match_to_2[3]  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_match_temp_37 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 4  # type: ignore  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if _coconut_match_temp_37:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            _coconut_case_match_check_2 = True  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    if _coconut_case_match_check_2:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if _coconut_match_set_name_dtype is not _coconut_sentinel:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            dtype = _coconut_match_set_name_dtype  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if _coconut_match_set_name_arrange is not _coconut_sentinel:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            arrange = _coconut_match_set_name_arrange  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            ch_rpr = _coconut_match_set_name_ch_rpr  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if _coconut_match_set_name_v_range is not _coconut_sentinel:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            v_range = _coconut_match_set_name_v_range  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):

                if not _coconut_case_match_check_2:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    if (not _coconut_match_temp_36) and (_coconut.isinstance(_coconut_case_match_to_2, Torch)):  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_case_match_check_2 = True  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                    if _coconut_case_match_check_2:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        _coconut_case_match_check_2 = False  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                        if not _coconut_case_match_check_2:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            if _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports 1)")  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_case_match_check_2 = True  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):

                        if not _coconut_case_match_check_2:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            _coconut_match_set_name_dtype = _coconut_sentinel  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            _coconut_match_set_name_arrange = _coconut_sentinel  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            _coconut_match_set_name_v_range = _coconut_sentinel  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            if not _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_match_temp_38 = _coconut.getattr(Torch, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if not _coconut.isinstance(_coconut_match_temp_38, _coconut.tuple):  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    raise _coconut.TypeError("Torch.__match_args__ must be a tuple")  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if _coconut.len(_coconut_match_temp_38) < 4:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Torch' only supports %s)" % (_coconut.len(_coconut_match_temp_38),))  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_match_temp_39 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_38[0], _coconut_sentinel)  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_match_temp_40 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_38[1], _coconut_sentinel)  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_match_temp_41 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_38[2], _coconut_sentinel)  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                _coconut_match_temp_42 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_38[3], _coconut_sentinel)  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if (_coconut_match_temp_39 is not _coconut_sentinel) and (_coconut_match_temp_40 is not _coconut_sentinel) and (_coconut_match_temp_41 is not _coconut_sentinel) and (_coconut_match_temp_42 is not _coconut_sentinel):  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    _coconut_match_set_name_dtype = _coconut_match_temp_39  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    _coconut_match_set_name_arrange = _coconut_match_temp_40  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    _coconut_match_set_name_ch_rpr = _coconut_match_temp_41  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    _coconut_match_set_name_v_range = _coconut_match_temp_42  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    _coconut_case_match_check_2 = True  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                            if _coconut_case_match_check_2:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if _coconut_match_set_name_dtype is not _coconut_sentinel:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    dtype = _coconut_match_set_name_dtype  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if _coconut_match_set_name_arrange is not _coconut_sentinel:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    arrange = _coconut_match_set_name_arrange  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    ch_rpr = _coconut_match_set_name_ch_rpr  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                if _coconut_match_set_name_v_range is not _coconut_sentinel:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                                    v_range = _coconut_match_set_name_v_range  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):




            if _coconut_case_match_check_2:  #51:                 match Torch(dtype,arrange,ch_rpr,v_range):
                base = "torch,{_coconut_format_0},{_coconut_format_1},{_coconut_format_2},{_coconut_format_3}".format(_coconut_format_0=(dtype), _coconut_format_1=(arrange), _coconut_format_2=(ch_rpr), _coconut_format_3=(v_range))  #52:                     base = f"torch,{dtype},{arrange},{ch_rpr},{v_range}"
        if not _coconut_case_match_check_2:  #53:                 match PILImages(mode,ch_rpr):
            _coconut_match_temp_43 = _coconut.getattr(PILImages, "_coconut_is_data", False) or _coconut.isinstance(PILImages, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImages)  # type: ignore  #53:                 match PILImages(mode,ch_rpr):
            _coconut_case_match_check_2 = True  #53:                 match PILImages(mode,ch_rpr):
            if _coconut_case_match_check_2:  #53:                 match PILImages(mode,ch_rpr):
                _coconut_case_match_check_2 = False  #53:                 match PILImages(mode,ch_rpr):
                if not _coconut_case_match_check_2:  #53:                 match PILImages(mode,ch_rpr):
                    _coconut_match_set_name_mode = _coconut_sentinel  #53:                 match PILImages(mode,ch_rpr):
                    _coconut_match_set_name_ch_rpr = _coconut_sentinel  #53:                 match PILImages(mode,ch_rpr):
                    if (_coconut_match_temp_43) and (_coconut.isinstance(_coconut_case_match_to_2, PILImages)) and (_coconut.len(_coconut_case_match_to_2) >= 2):  #53:                 match PILImages(mode,ch_rpr):
                        _coconut_match_set_name_mode = _coconut_case_match_to_2[0]  #53:                 match PILImages(mode,ch_rpr):
                        _coconut_match_set_name_ch_rpr = _coconut_case_match_to_2[1]  #53:                 match PILImages(mode,ch_rpr):
                        _coconut_match_temp_44 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 2  # type: ignore  #53:                 match PILImages(mode,ch_rpr):
                        if _coconut_match_temp_44:  #53:                 match PILImages(mode,ch_rpr):
                            _coconut_case_match_check_2 = True  #53:                 match PILImages(mode,ch_rpr):
                    if _coconut_case_match_check_2:  #53:                 match PILImages(mode,ch_rpr):
                        if _coconut_match_set_name_mode is not _coconut_sentinel:  #53:                 match PILImages(mode,ch_rpr):
                            mode = _coconut_match_set_name_mode  #53:                 match PILImages(mode,ch_rpr):
                        if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #53:                 match PILImages(mode,ch_rpr):
                            ch_rpr = _coconut_match_set_name_ch_rpr  #53:                 match PILImages(mode,ch_rpr):

                if not _coconut_case_match_check_2:  #53:                 match PILImages(mode,ch_rpr):
                    if (not _coconut_match_temp_43) and (_coconut.isinstance(_coconut_case_match_to_2, PILImages)):  #53:                 match PILImages(mode,ch_rpr):
                        _coconut_case_match_check_2 = True  #53:                 match PILImages(mode,ch_rpr):
                    if _coconut_case_match_check_2:  #53:                 match PILImages(mode,ch_rpr):
                        _coconut_case_match_check_2 = False  #53:                 match PILImages(mode,ch_rpr):
                        if not _coconut_case_match_check_2:  #53:                 match PILImages(mode,ch_rpr):
                            if _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #53:                 match PILImages(mode,ch_rpr):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports 1)")  #53:                 match PILImages(mode,ch_rpr):
                                _coconut_case_match_check_2 = True  #53:                 match PILImages(mode,ch_rpr):

                        if not _coconut_case_match_check_2:  #53:                 match PILImages(mode,ch_rpr):
                            _coconut_match_set_name_mode = _coconut_sentinel  #53:                 match PILImages(mode,ch_rpr):
                            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #53:                 match PILImages(mode,ch_rpr):
                            if not _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #53:                 match PILImages(mode,ch_rpr):
                                _coconut_match_temp_45 = _coconut.getattr(PILImages, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #53:                 match PILImages(mode,ch_rpr):
                                if not _coconut.isinstance(_coconut_match_temp_45, _coconut.tuple):  #53:                 match PILImages(mode,ch_rpr):
                                    raise _coconut.TypeError("PILImages.__match_args__ must be a tuple")  #53:                 match PILImages(mode,ch_rpr):
                                if _coconut.len(_coconut_match_temp_45) < 2:  #53:                 match PILImages(mode,ch_rpr):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports %s)" % (_coconut.len(_coconut_match_temp_45),))  #53:                 match PILImages(mode,ch_rpr):
                                _coconut_match_temp_46 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_45[0], _coconut_sentinel)  #53:                 match PILImages(mode,ch_rpr):
                                _coconut_match_temp_47 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_45[1], _coconut_sentinel)  #53:                 match PILImages(mode,ch_rpr):
                                if (_coconut_match_temp_46 is not _coconut_sentinel) and (_coconut_match_temp_47 is not _coconut_sentinel):  #53:                 match PILImages(mode,ch_rpr):
                                    _coconut_match_set_name_mode = _coconut_match_temp_46  #53:                 match PILImages(mode,ch_rpr):
                                    _coconut_match_set_name_ch_rpr = _coconut_match_temp_47  #53:                 match PILImages(mode,ch_rpr):
                                    _coconut_case_match_check_2 = True  #53:                 match PILImages(mode,ch_rpr):
                            if _coconut_case_match_check_2:  #53:                 match PILImages(mode,ch_rpr):
                                if _coconut_match_set_name_mode is not _coconut_sentinel:  #53:                 match PILImages(mode,ch_rpr):
                                    mode = _coconut_match_set_name_mode  #53:                 match PILImages(mode,ch_rpr):
                                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #53:                 match PILImages(mode,ch_rpr):
                                    ch_rpr = _coconut_match_set_name_ch_rpr  #53:                 match PILImages(mode,ch_rpr):




            if _coconut_case_match_check_2:  #53:                 match PILImages(mode,ch_rpr):
                base = "images,{_coconut_format_0},{_coconut_format_1}".format(_coconut_format_0=(mode), _coconut_format_1=(ch_rpr))  #54:                     base = f"images,{mode},{ch_rpr}"
        if not _coconut_case_match_check_2:  #55:                 match PILImage(mode,ch_rpr):
            _coconut_match_temp_48 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #55:                 match PILImage(mode,ch_rpr):
            _coconut_case_match_check_2 = True  #55:                 match PILImage(mode,ch_rpr):
            if _coconut_case_match_check_2:  #55:                 match PILImage(mode,ch_rpr):
                _coconut_case_match_check_2 = False  #55:                 match PILImage(mode,ch_rpr):
                if not _coconut_case_match_check_2:  #55:                 match PILImage(mode,ch_rpr):
                    _coconut_match_set_name_mode = _coconut_sentinel  #55:                 match PILImage(mode,ch_rpr):
                    _coconut_match_set_name_ch_rpr = _coconut_sentinel  #55:                 match PILImage(mode,ch_rpr):
                    if (_coconut_match_temp_48) and (_coconut.isinstance(_coconut_case_match_to_2, PILImage)) and (_coconut.len(_coconut_case_match_to_2) >= 2):  #55:                 match PILImage(mode,ch_rpr):
                        _coconut_match_set_name_mode = _coconut_case_match_to_2[0]  #55:                 match PILImage(mode,ch_rpr):
                        _coconut_match_set_name_ch_rpr = _coconut_case_match_to_2[1]  #55:                 match PILImage(mode,ch_rpr):
                        _coconut_match_temp_49 = _coconut.len(_coconut_case_match_to_2) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_2.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {}) and _coconut_case_match_to_2[i] == _coconut.getattr(_coconut_case_match_to_2, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_2.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_2, "__match_args__") else _coconut.len(_coconut_case_match_to_2) == 2  # type: ignore  #55:                 match PILImage(mode,ch_rpr):
                        if _coconut_match_temp_49:  #55:                 match PILImage(mode,ch_rpr):
                            _coconut_case_match_check_2 = True  #55:                 match PILImage(mode,ch_rpr):
                    if _coconut_case_match_check_2:  #55:                 match PILImage(mode,ch_rpr):
                        if _coconut_match_set_name_mode is not _coconut_sentinel:  #55:                 match PILImage(mode,ch_rpr):
                            mode = _coconut_match_set_name_mode  #55:                 match PILImage(mode,ch_rpr):
                        if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #55:                 match PILImage(mode,ch_rpr):
                            ch_rpr = _coconut_match_set_name_ch_rpr  #55:                 match PILImage(mode,ch_rpr):

                if not _coconut_case_match_check_2:  #55:                 match PILImage(mode,ch_rpr):
                    if (not _coconut_match_temp_48) and (_coconut.isinstance(_coconut_case_match_to_2, PILImage)):  #55:                 match PILImage(mode,ch_rpr):
                        _coconut_case_match_check_2 = True  #55:                 match PILImage(mode,ch_rpr):
                    if _coconut_case_match_check_2:  #55:                 match PILImage(mode,ch_rpr):
                        _coconut_case_match_check_2 = False  #55:                 match PILImage(mode,ch_rpr):
                        if not _coconut_case_match_check_2:  #55:                 match PILImage(mode,ch_rpr):
                            if _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #55:                 match PILImage(mode,ch_rpr):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #55:                 match PILImage(mode,ch_rpr):
                                _coconut_case_match_check_2 = True  #55:                 match PILImage(mode,ch_rpr):

                        if not _coconut_case_match_check_2:  #55:                 match PILImage(mode,ch_rpr):
                            _coconut_match_set_name_mode = _coconut_sentinel  #55:                 match PILImage(mode,ch_rpr):
                            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #55:                 match PILImage(mode,ch_rpr):
                            if not _coconut.type(_coconut_case_match_to_2) in _coconut_self_match_types:  #55:                 match PILImage(mode,ch_rpr):
                                _coconut_match_temp_50 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #55:                 match PILImage(mode,ch_rpr):
                                if not _coconut.isinstance(_coconut_match_temp_50, _coconut.tuple):  #55:                 match PILImage(mode,ch_rpr):
                                    raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #55:                 match PILImage(mode,ch_rpr):
                                if _coconut.len(_coconut_match_temp_50) < 2:  #55:                 match PILImage(mode,ch_rpr):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_50),))  #55:                 match PILImage(mode,ch_rpr):
                                _coconut_match_temp_51 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_50[0], _coconut_sentinel)  #55:                 match PILImage(mode,ch_rpr):
                                _coconut_match_temp_52 = _coconut.getattr(_coconut_case_match_to_2, _coconut_match_temp_50[1], _coconut_sentinel)  #55:                 match PILImage(mode,ch_rpr):
                                if (_coconut_match_temp_51 is not _coconut_sentinel) and (_coconut_match_temp_52 is not _coconut_sentinel):  #55:                 match PILImage(mode,ch_rpr):
                                    _coconut_match_set_name_mode = _coconut_match_temp_51  #55:                 match PILImage(mode,ch_rpr):
                                    _coconut_match_set_name_ch_rpr = _coconut_match_temp_52  #55:                 match PILImage(mode,ch_rpr):
                                    _coconut_case_match_check_2 = True  #55:                 match PILImage(mode,ch_rpr):
                            if _coconut_case_match_check_2:  #55:                 match PILImage(mode,ch_rpr):
                                if _coconut_match_set_name_mode is not _coconut_sentinel:  #55:                 match PILImage(mode,ch_rpr):
                                    mode = _coconut_match_set_name_mode  #55:                 match PILImage(mode,ch_rpr):
                                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #55:                 match PILImage(mode,ch_rpr):
                                    ch_rpr = _coconut_match_set_name_ch_rpr  #55:                 match PILImage(mode,ch_rpr):




            if _coconut_case_match_check_2:  #55:                 match PILImage(mode,ch_rpr):
                base = "image,{_coconut_format_0},{_coconut_format_1}".format(_coconut_format_0=(mode), _coconut_format_1=(ch_rpr))  #56:                     base = f"image,{mode},{ch_rpr}"
        if not _coconut_case_match_check_2:  #57:             else:
            raise RuntimeError("cannot convert unknown imagedef:{_coconut_format_0} to str.".format(_coconut_format_0=(imdef)))  #58:                 raise RuntimeError(f"cannot convert unknown imagedef:{imdef} to str.")
        if "shape" in meta:  #59:             if "shape" in meta:
            shape_str = ":".join([str(s) for s in meta["shape"]])  #60:                 shape_str = ":".join([str(s) for s in meta["shape"]])
            res = base + "," + shape_str  #61:                 res =  base+","+shape_str
        else:  #62:             else:
            res = base  #63:                 res = base
#logger.info(f"imdef_to_str:{res}")
        return (res)  #65:             return res
    if not _coconut_case_match_check_3:  #66:     else:
        raise RuntimeError("cannot convert unknown imdef:{_coconut_format_0} to str.".format(_coconut_format_0=(imdef)))  #67:         raise RuntimeError(f"cannot convert unknown imdef:{imdef} to str.")

def cast_imdef_to_imdef_str(imdef):  #68: def cast_imdef_to_imdef_str(imdef):
    _coconut_case_match_to_4 = imdef  #69:     case imdef:
    _coconut_case_match_check_4 = False  #69:     case imdef:
    _coconut_match_temp_58 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #69:     case imdef:
    _coconut_case_match_check_4 = True  #69:     case imdef:
    if _coconut_case_match_check_4:  #69:     case imdef:
        _coconut_case_match_check_4 = False  #69:     case imdef:
        if not _coconut_case_match_check_4:  #69:     case imdef:
            if (_coconut_match_temp_58) and (_coconut.isinstance(_coconut_case_match_to_4, ImageDef)) and (_coconut.len(_coconut_case_match_to_4) >= 2):  #69:     case imdef:
                _coconut_match_temp_59 = _coconut.len(_coconut_case_match_to_4) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_4.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_4, "_coconut_data_defaults", {}) and _coconut_case_match_to_4[i] == _coconut.getattr(_coconut_case_match_to_4, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_4.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_4, "__match_args__") else _coconut.len(_coconut_case_match_to_4) == 2  # type: ignore  #69:     case imdef:
                if _coconut_match_temp_59:  #69:     case imdef:
                    _coconut_case_match_check_4 = True  #69:     case imdef:

        if not _coconut_case_match_check_4:  #69:     case imdef:
            if (not _coconut_match_temp_58) and (_coconut.isinstance(_coconut_case_match_to_4, ImageDef)):  #69:     case imdef:
                _coconut_case_match_check_4 = True  #69:     case imdef:
            if _coconut_case_match_check_4:  #69:     case imdef:
                _coconut_case_match_check_4 = False  #69:     case imdef:
                if not _coconut_case_match_check_4:  #69:     case imdef:
                    if _coconut.type(_coconut_case_match_to_4) in _coconut_self_match_types:  #69:     case imdef:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #69:     case imdef:
                        _coconut_case_match_check_4 = True  #69:     case imdef:

                if not _coconut_case_match_check_4:  #69:     case imdef:
                    if not _coconut.type(_coconut_case_match_to_4) in _coconut_self_match_types:  #69:     case imdef:
                        _coconut_match_temp_60 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #69:     case imdef:
                        if not _coconut.isinstance(_coconut_match_temp_60, _coconut.tuple):  #69:     case imdef:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #69:     case imdef:
                        if _coconut.len(_coconut_match_temp_60) < 2:  #69:     case imdef:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_60),))  #69:     case imdef:
                        _coconut_match_temp_61 = _coconut.getattr(_coconut_case_match_to_4, _coconut_match_temp_60[0], _coconut_sentinel)  #69:     case imdef:
                        _coconut_match_temp_62 = _coconut.getattr(_coconut_case_match_to_4, _coconut_match_temp_60[1], _coconut_sentinel)  #69:     case imdef:
                        if (_coconut_match_temp_61 is not _coconut_sentinel) and (_coconut_match_temp_62 is not _coconut_sentinel):  #69:     case imdef:
                            _coconut_case_match_check_4 = True  #69:     case imdef:




    if _coconut_case_match_check_4:  #69:     case imdef:
        res = [imdef2imdef_str(imdef),]  #71:             res = [imdef2imdef_str(imdef)]
        return (res)  #72:             return res
    if not _coconut_case_match_check_4:  #73:     else:
        return (None)  #74:         return None


def imgs2tile_shape(shape, w=1024, h=1024, max_image=100, padding=1):  #76: def imgs2tile_shape(shape,w=1024,h=1024,max_image=100,padding=1):
    _coconut_case_match_to_5 = shape  #77:     case shape:
    _coconut_case_match_check_5 = False  #77:     case shape:
    _coconut_match_set_name_B = _coconut_sentinel  #77:     case shape:
    _coconut_match_set_name_H = _coconut_sentinel  #77:     case shape:
    _coconut_match_set_name_W = _coconut_sentinel  #77:     case shape:
    if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 3):  #77:     case shape:
        _coconut_match_set_name_B = _coconut_case_match_to_5[0]  #77:     case shape:
        _coconut_match_set_name_H = _coconut_case_match_to_5[1]  #77:     case shape:
        _coconut_match_set_name_W = _coconut_case_match_to_5[2]  #77:     case shape:
        _coconut_case_match_check_5 = True  #77:     case shape:
    if _coconut_case_match_check_5:  #77:     case shape:
        if _coconut_match_set_name_B is not _coconut_sentinel:  #77:     case shape:
            B = _coconut_match_set_name_B  #77:     case shape:
        if _coconut_match_set_name_H is not _coconut_sentinel:  #77:     case shape:
            H = _coconut_match_set_name_H  #77:     case shape:
        if _coconut_match_set_name_W is not _coconut_sentinel:  #77:     case shape:
            W = _coconut_match_set_name_W  #77:     case shape:
    if _coconut_case_match_check_5:  #77:     case shape:
        ch = 1  #79:             ch = 1
    if not _coconut_case_match_check_5:  #80:         match (B,H,W,ch):
        _coconut_match_set_name_B = _coconut_sentinel  #80:         match (B,H,W,ch):
        _coconut_match_set_name_H = _coconut_sentinel  #80:         match (B,H,W,ch):
        _coconut_match_set_name_W = _coconut_sentinel  #80:         match (B,H,W,ch):
        _coconut_match_set_name_ch = _coconut_sentinel  #80:         match (B,H,W,ch):
        if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 4):  #80:         match (B,H,W,ch):
            _coconut_match_set_name_B = _coconut_case_match_to_5[0]  #80:         match (B,H,W,ch):
            _coconut_match_set_name_H = _coconut_case_match_to_5[1]  #80:         match (B,H,W,ch):
            _coconut_match_set_name_W = _coconut_case_match_to_5[2]  #80:         match (B,H,W,ch):
            _coconut_match_set_name_ch = _coconut_case_match_to_5[3]  #80:         match (B,H,W,ch):
            _coconut_case_match_check_5 = True  #80:         match (B,H,W,ch):
        if _coconut_case_match_check_5:  #80:         match (B,H,W,ch):
            if _coconut_match_set_name_B is not _coconut_sentinel:  #80:         match (B,H,W,ch):
                B = _coconut_match_set_name_B  #80:         match (B,H,W,ch):
            if _coconut_match_set_name_H is not _coconut_sentinel:  #80:         match (B,H,W,ch):
                H = _coconut_match_set_name_H  #80:         match (B,H,W,ch):
            if _coconut_match_set_name_W is not _coconut_sentinel:  #80:         match (B,H,W,ch):
                W = _coconut_match_set_name_W  #80:         match (B,H,W,ch):
            if _coconut_match_set_name_ch is not _coconut_sentinel:  #80:         match (B,H,W,ch):
                ch = _coconut_match_set_name_ch  #80:         match (B,H,W,ch):
        if _coconut_case_match_check_5:  #80:         match (B,H,W,ch):
            pass  #81:             pass
#nrow = int(sqrt(len(imgs[:max_image]))+0.5)
    if shape[0] is None:  #83:     if shape[0] is None:
# we cannot estimate actual shape.
        return ((None, None, ch))  #85:         return (None,None,ch)
    n_imgs = min(shape[0], max_image)  #86:     n_imgs = min(shape[0],max_image)
    nrow = int(sqrt(n_imgs))  #87:     nrow = int(sqrt(n_imgs))
    if (nrow * nrow < n_imgs):  #88:     if (nrow*nrow < n_imgs):
        nrow += 1  #89:         nrow += 1
    r = int((w - ((nrow + 1) * padding)) / nrow)  # width/height of each tile  #90:     r = int((w-((nrow+1)*padding))/nrow) # width/height of each tile
    new_shape = (r * nrow, r * nrow, ch)  #91:     new_shape = (r*nrow,r*nrow,ch)
    return (new_shape)  #92:     return new_shape


ms_imgs2tile = (_coconut_partial(_coconut_partial, ss_to_ms))(imgs2tile_shape)  #94: ms_imgs2tile = imgs2tile_shape |> ss_to_ms$

def imgs2tile(imgs, w=1024, h=1024, max_image=100, padding=1):  #96: def imgs2tile(imgs,w=1024,h=1024,max_image=100,padding=1):
    mode = imgs[0].mode  #97:     mode = imgs[0].mode
    ch = len(mode)  #98:     ch = len(mode)
#nrow = int(sqrt(len(imgs[:max_image]))+0.5)
    n_imgs = len(imgs[:max_image])  #100:     n_imgs = len(imgs[:max_image])
    nrow = int(sqrt(n_imgs))  #101:     nrow = int(sqrt(n_imgs))
    if (nrow * nrow < n_imgs):  #102:     if (nrow*nrow < n_imgs):
        nrow += 1  #103:         nrow += 1
    r = int((w - ((nrow + 1) * padding)) / nrow)  #104:     r = int((w-((nrow+1)*padding))/nrow)

    imgs = np.array([((np.array)(img.resize((r, r)))) for img in imgs[:max_image]])  #106:     imgs = np.array([(img.resize((r,r)) |> np.array) for img in imgs[:max_image]])
    if ch == 1:  #107:     if ch == 1:
        imgs = imgs[:, :, :, None]  #108:         imgs = imgs[:,:,:,None]
    return (make_grid(imgs, nrow, padding=padding))  #109:     return make_grid(imgs,nrow,padding=padding)


def rule_imgs2tile(state):  #111: def rule_imgs2tile(state):
    _coconut_case_match_to_6 = state  #112:     case state:
    _coconut_case_match_check_6 = False  #112:     case state:
    _coconut_match_temp_63 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #112:     case state:
    _coconut_case_match_check_6 = True  #112:     case state:
    if _coconut_case_match_check_6:  #112:     case state:
        _coconut_case_match_check_6 = False  #112:     case state:
        if not _coconut_case_match_check_6:  #112:     case state:
            _coconut_match_set_name_meta = _coconut_sentinel  #112:     case state:
            if (_coconut_match_temp_63) and (_coconut.isinstance(_coconut_case_match_to_6, ImageDef)) and (_coconut.len(_coconut_case_match_to_6) >= 2):  #112:     case state:
                _coconut_match_temp_64 = _coconut.getattr(PILImages, "_coconut_is_data", False) or _coconut.isinstance(PILImages, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImages)  # type: ignore  #112:     case state:
                _coconut_match_set_name_meta = _coconut_case_match_to_6[1]  #112:     case state:
                _coconut_match_temp_69 = _coconut.len(_coconut_case_match_to_6) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_6.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_6, "_coconut_data_defaults", {}) and _coconut_case_match_to_6[i] == _coconut.getattr(_coconut_case_match_to_6, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_6.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_6, "__match_args__") else _coconut.len(_coconut_case_match_to_6) == 2  # type: ignore  #112:     case state:
                if _coconut_match_temp_69:  #112:     case state:
                    _coconut_case_match_check_6 = True  #112:     case state:
            if _coconut_case_match_check_6:  #112:     case state:
                _coconut_case_match_check_6 = False  #112:     case state:
                if not _coconut_case_match_check_6:  #112:     case state:
                    _coconut_match_set_name_mode = _coconut_sentinel  #112:     case state:
                    _coconut_match_set_name_chrpr = _coconut_sentinel  #112:     case state:
                    if (_coconut_match_temp_64) and (_coconut.isinstance(_coconut_case_match_to_6[0], PILImages)) and (_coconut.len(_coconut_case_match_to_6[0]) >= 2):  #112:     case state:
                        _coconut_match_set_name_mode = _coconut_case_match_to_6[0][0]  #112:     case state:
                        _coconut_match_set_name_chrpr = _coconut_case_match_to_6[0][1]  #112:     case state:
                        _coconut_match_temp_65 = _coconut.len(_coconut_case_match_to_6[0]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_6[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_6[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_6[0][i] == _coconut.getattr(_coconut_case_match_to_6[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_6[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_6[0], "__match_args__") else _coconut.len(_coconut_case_match_to_6[0]) == 2  # type: ignore  #112:     case state:
                        if _coconut_match_temp_65:  #112:     case state:
                            _coconut_case_match_check_6 = True  #112:     case state:
                    if _coconut_case_match_check_6:  #112:     case state:
                        if _coconut_match_set_name_mode is not _coconut_sentinel:  #112:     case state:
                            mode = _coconut_match_set_name_mode  #112:     case state:
                        if _coconut_match_set_name_chrpr is not _coconut_sentinel:  #112:     case state:
                            chrpr = _coconut_match_set_name_chrpr  #112:     case state:

                if not _coconut_case_match_check_6:  #112:     case state:
                    if (not _coconut_match_temp_64) and (_coconut.isinstance(_coconut_case_match_to_6[0], PILImages)):  #112:     case state:
                        _coconut_case_match_check_6 = True  #112:     case state:
                    if _coconut_case_match_check_6:  #112:     case state:
                        _coconut_case_match_check_6 = False  #112:     case state:
                        if not _coconut_case_match_check_6:  #112:     case state:
                            if _coconut.type(_coconut_case_match_to_6[0]) in _coconut_self_match_types:  #112:     case state:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports 1)")  #112:     case state:
                                _coconut_case_match_check_6 = True  #112:     case state:

                        if not _coconut_case_match_check_6:  #112:     case state:
                            _coconut_match_set_name_mode = _coconut_sentinel  #112:     case state:
                            _coconut_match_set_name_chrpr = _coconut_sentinel  #112:     case state:
                            if not _coconut.type(_coconut_case_match_to_6[0]) in _coconut_self_match_types:  #112:     case state:
                                _coconut_match_temp_66 = _coconut.getattr(PILImages, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #112:     case state:
                                if not _coconut.isinstance(_coconut_match_temp_66, _coconut.tuple):  #112:     case state:
                                    raise _coconut.TypeError("PILImages.__match_args__ must be a tuple")  #112:     case state:
                                if _coconut.len(_coconut_match_temp_66) < 2:  #112:     case state:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports %s)" % (_coconut.len(_coconut_match_temp_66),))  #112:     case state:
                                _coconut_match_temp_67 = _coconut.getattr(_coconut_case_match_to_6[0], _coconut_match_temp_66[0], _coconut_sentinel)  #112:     case state:
                                _coconut_match_temp_68 = _coconut.getattr(_coconut_case_match_to_6[0], _coconut_match_temp_66[1], _coconut_sentinel)  #112:     case state:
                                if (_coconut_match_temp_67 is not _coconut_sentinel) and (_coconut_match_temp_68 is not _coconut_sentinel):  #112:     case state:
                                    _coconut_match_set_name_mode = _coconut_match_temp_67  #112:     case state:
                                    _coconut_match_set_name_chrpr = _coconut_match_temp_68  #112:     case state:
                                    _coconut_case_match_check_6 = True  #112:     case state:
                            if _coconut_case_match_check_6:  #112:     case state:
                                if _coconut_match_set_name_mode is not _coconut_sentinel:  #112:     case state:
                                    mode = _coconut_match_set_name_mode  #112:     case state:
                                if _coconut_match_set_name_chrpr is not _coconut_sentinel:  #112:     case state:
                                    chrpr = _coconut_match_set_name_chrpr  #112:     case state:




            if _coconut_case_match_check_6:  #112:     case state:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #112:     case state:
                    meta = _coconut_match_set_name_meta  #112:     case state:

        if not _coconut_case_match_check_6:  #112:     case state:
            if (not _coconut_match_temp_63) and (_coconut.isinstance(_coconut_case_match_to_6, ImageDef)):  #112:     case state:
                _coconut_case_match_check_6 = True  #112:     case state:
            if _coconut_case_match_check_6:  #112:     case state:
                _coconut_case_match_check_6 = False  #112:     case state:
                if not _coconut_case_match_check_6:  #112:     case state:
                    if _coconut.type(_coconut_case_match_to_6) in _coconut_self_match_types:  #112:     case state:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #112:     case state:
                        _coconut_case_match_check_6 = True  #112:     case state:

                if not _coconut_case_match_check_6:  #112:     case state:
                    _coconut_match_set_name_meta = _coconut_sentinel  #112:     case state:
                    if not _coconut.type(_coconut_case_match_to_6) in _coconut_self_match_types:  #112:     case state:
                        _coconut_match_temp_70 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #112:     case state:
                        if not _coconut.isinstance(_coconut_match_temp_70, _coconut.tuple):  #112:     case state:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #112:     case state:
                        if _coconut.len(_coconut_match_temp_70) < 2:  #112:     case state:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_70),))  #112:     case state:
                        _coconut_match_temp_71 = _coconut.getattr(_coconut_case_match_to_6, _coconut_match_temp_70[0], _coconut_sentinel)  #112:     case state:
                        _coconut_match_temp_77 = _coconut.getattr(_coconut_case_match_to_6, _coconut_match_temp_70[1], _coconut_sentinel)  #112:     case state:
                        if (_coconut_match_temp_71 is not _coconut_sentinel) and (_coconut_match_temp_77 is not _coconut_sentinel):  #112:     case state:
                            _coconut_match_temp_72 = _coconut.getattr(PILImages, "_coconut_is_data", False) or _coconut.isinstance(PILImages, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImages)  # type: ignore  #112:     case state:
                            _coconut_match_set_name_meta = _coconut_match_temp_77  #112:     case state:
                            _coconut_case_match_check_6 = True  #112:     case state:
                    if _coconut_case_match_check_6:  #112:     case state:
                        _coconut_case_match_check_6 = False  #112:     case state:
                        if not _coconut_case_match_check_6:  #112:     case state:
                            _coconut_match_set_name_mode = _coconut_sentinel  #112:     case state:
                            _coconut_match_set_name_chrpr = _coconut_sentinel  #112:     case state:
                            if (_coconut_match_temp_72) and (_coconut.isinstance(_coconut_match_temp_71, PILImages)) and (_coconut.len(_coconut_match_temp_71) >= 2):  #112:     case state:
                                _coconut_match_set_name_mode = _coconut_match_temp_71[0]  #112:     case state:
                                _coconut_match_set_name_chrpr = _coconut_match_temp_71[1]  #112:     case state:
                                _coconut_match_temp_73 = _coconut.len(_coconut_match_temp_71) <= _coconut.max(2, _coconut.len(_coconut_match_temp_71.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_71, "_coconut_data_defaults", {}) and _coconut_match_temp_71[i] == _coconut.getattr(_coconut_match_temp_71, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_match_temp_71.__match_args__))) if _coconut.hasattr(_coconut_match_temp_71, "__match_args__") else _coconut.len(_coconut_match_temp_71) == 2  # type: ignore  #112:     case state:
                                if _coconut_match_temp_73:  #112:     case state:
                                    _coconut_case_match_check_6 = True  #112:     case state:
                            if _coconut_case_match_check_6:  #112:     case state:
                                if _coconut_match_set_name_mode is not _coconut_sentinel:  #112:     case state:
                                    mode = _coconut_match_set_name_mode  #112:     case state:
                                if _coconut_match_set_name_chrpr is not _coconut_sentinel:  #112:     case state:
                                    chrpr = _coconut_match_set_name_chrpr  #112:     case state:

                        if not _coconut_case_match_check_6:  #112:     case state:
                            if (not _coconut_match_temp_72) and (_coconut.isinstance(_coconut_match_temp_71, PILImages)):  #112:     case state:
                                _coconut_case_match_check_6 = True  #112:     case state:
                            if _coconut_case_match_check_6:  #112:     case state:
                                _coconut_case_match_check_6 = False  #112:     case state:
                                if not _coconut_case_match_check_6:  #112:     case state:
                                    if _coconut.type(_coconut_match_temp_71) in _coconut_self_match_types:  #112:     case state:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports 1)")  #112:     case state:
                                        _coconut_case_match_check_6 = True  #112:     case state:

                                if not _coconut_case_match_check_6:  #112:     case state:
                                    _coconut_match_set_name_mode = _coconut_sentinel  #112:     case state:
                                    _coconut_match_set_name_chrpr = _coconut_sentinel  #112:     case state:
                                    if not _coconut.type(_coconut_match_temp_71) in _coconut_self_match_types:  #112:     case state:
                                        _coconut_match_temp_74 = _coconut.getattr(PILImages, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #112:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_74, _coconut.tuple):  #112:     case state:
                                            raise _coconut.TypeError("PILImages.__match_args__ must be a tuple")  #112:     case state:
                                        if _coconut.len(_coconut_match_temp_74) < 2:  #112:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports %s)" % (_coconut.len(_coconut_match_temp_74),))  #112:     case state:
                                        _coconut_match_temp_75 = _coconut.getattr(_coconut_match_temp_71, _coconut_match_temp_74[0], _coconut_sentinel)  #112:     case state:
                                        _coconut_match_temp_76 = _coconut.getattr(_coconut_match_temp_71, _coconut_match_temp_74[1], _coconut_sentinel)  #112:     case state:
                                        if (_coconut_match_temp_75 is not _coconut_sentinel) and (_coconut_match_temp_76 is not _coconut_sentinel):  #112:     case state:
                                            _coconut_match_set_name_mode = _coconut_match_temp_75  #112:     case state:
                                            _coconut_match_set_name_chrpr = _coconut_match_temp_76  #112:     case state:
                                            _coconut_case_match_check_6 = True  #112:     case state:
                                    if _coconut_case_match_check_6:  #112:     case state:
                                        if _coconut_match_set_name_mode is not _coconut_sentinel:  #112:     case state:
                                            mode = _coconut_match_set_name_mode  #112:     case state:
                                        if _coconut_match_set_name_chrpr is not _coconut_sentinel:  #112:     case state:
                                            chrpr = _coconut_match_set_name_chrpr  #112:     case state:




                    if _coconut_case_match_check_6:  #112:     case state:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #112:     case state:
                            meta = _coconut_match_set_name_meta  #112:     case state:




    if _coconut_case_match_check_6:  #112:     case state:
        return ([(imgs2tile, ImageDef(Numpy("uint8", "HWC", chrpr, VR_0_255), (ms_imgs2tile)(meta)), "imgs2tile", 10),])  #114:             return [(

# todo

def batch_to_tiled(ary, max_size=1024, padding=1):  #122: def batch_to_tiled(ary,max_size=1024,padding=1):
# ary shape == (B,H,W,C)
    w = ary.shape[2]  #124:     w = ary.shape[2]
    n_imgs = min((max_size // w)**2, ary.shape[0])  #125:     n_imgs = min((max_size//w)**2,ary.shape[0])
    ary = ary[:n_imgs]  #126:     ary = ary[:n_imgs]
    nrow = int(sqrt(n_imgs))  #127:     nrow = int(sqrt(n_imgs))
    if (nrow * nrow < n_imgs):  #128:     if (nrow*nrow < n_imgs):
        nrow += 1  #129:         nrow += 1
    return (make_grid(ary, nrow, padding=padding))  #130:     return make_grid(ary,nrow,padding=padding)

def batch_to_tiled_shape_shift(shape, max_size=1024, padding=1):  #131: def batch_to_tiled_shape_shift(shape,max_size=1024,padding=1):
    b, h, w, c = shape  #132:     b,h,w,c = shape
    if b is None:  #133:     if b is None:
        return ((None, None, c))  #134:         return (None,None,c)
    if w is None:  #135:     if w is None:
        return ((None, None, c))  #136:         return (None,None,c)
    n_imgs = min((max_size // w)**2, shape[0])  #137:     n_imgs = min((max_size//w)**2,shape[0])
#n_imgs = min(max_size//w,b.shape[0])
    nrow = int(sqrt(n_imgs))  #139:     nrow = int(sqrt(n_imgs))
    if (nrow * nrow < n_imgs):  #140:     if (nrow*nrow < n_imgs):
        nrow += 1  #141:         nrow += 1
    r = int((w - ((nrow + 1) * padding)) / nrow)  # width/height of each tile  #142:     r = int((w-((nrow+1)*padding))/nrow) # width/height of each tile
    nh = (nrow - 1) * padding + nrow * h  #143:     nh = (nrow-1)*padding + nrow*h
    nw = (nrow - 1) * padding + nrow * w  #144:     nw = (nrow-1)*padding + nrow*w
    new_shape = (nh, nw, c)  #145:     new_shape = (nh,nw,c)
    return (new_shape)  #146:     return new_shape

ms_batch_to_tiled = (_coconut_partial(_coconut_partial, ss_to_ms))(batch_to_tiled_shape_shift)  #147: ms_batch_to_tiled = batch_to_tiled_shape_shift |> ss_to_ms$
def rule_batch_to_tiled(state):  #148: def rule_batch_to_tiled(state):
    _coconut_case_match_to_7 = state  #149:     case state:
    _coconut_case_match_check_7 = False  #149:     case state:
    _coconut_match_temp_78 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #149:     case state:
    _coconut_case_match_check_7 = True  #149:     case state:
    if _coconut_case_match_check_7:  #149:     case state:
        _coconut_case_match_check_7 = False  #149:     case state:
        if not _coconut_case_match_check_7:  #149:     case state:
            _coconut_match_set_name_meta = _coconut_sentinel  #149:     case state:
            if (_coconut_match_temp_78) and (_coconut.isinstance(_coconut_case_match_to_7, ImageDef)) and (_coconut.len(_coconut_case_match_to_7) >= 2):  #149:     case state:
                _coconut_match_temp_79 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #149:     case state:
                _coconut_match_set_name_meta = _coconut_case_match_to_7[1]  #149:     case state:
                _coconut_match_temp_86 = _coconut.len(_coconut_case_match_to_7) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_7.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_7, "_coconut_data_defaults", {}) and _coconut_case_match_to_7[i] == _coconut.getattr(_coconut_case_match_to_7, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_7.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_7, "__match_args__") else _coconut.len(_coconut_case_match_to_7) == 2  # type: ignore  #149:     case state:
                if _coconut_match_temp_86:  #149:     case state:
                    _coconut_case_match_check_7 = True  #149:     case state:
            if _coconut_case_match_check_7:  #149:     case state:
                _coconut_case_match_check_7 = False  #149:     case state:
                if not _coconut_case_match_check_7:  #149:     case state:
                    _coconut_match_set_name_dt = _coconut_sentinel  #149:     case state:
                    _coconut_match_set_name_chrpr = _coconut_sentinel  #149:     case state:
                    _coconut_match_set_name_vr = _coconut_sentinel  #149:     case state:
                    if (_coconut_match_temp_79) and (_coconut.isinstance(_coconut_case_match_to_7[0], Numpy)) and (_coconut.len(_coconut_case_match_to_7[0]) >= 4) and (_coconut_case_match_to_7[0][1] == "BHWC"):  #149:     case state:
                        _coconut_match_set_name_dt = _coconut_case_match_to_7[0][0]  #149:     case state:
                        _coconut_match_set_name_chrpr = _coconut_case_match_to_7[0][2]  #149:     case state:
                        _coconut_match_set_name_vr = _coconut_case_match_to_7[0][3]  #149:     case state:
                        _coconut_match_temp_80 = _coconut.len(_coconut_case_match_to_7[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_7[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_7[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_7[0][i] == _coconut.getattr(_coconut_case_match_to_7[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_7[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_7[0], "__match_args__") else _coconut.len(_coconut_case_match_to_7[0]) == 4  # type: ignore  #149:     case state:
                        if _coconut_match_temp_80:  #149:     case state:
                            _coconut_case_match_check_7 = True  #149:     case state:
                    if _coconut_case_match_check_7:  #149:     case state:
                        if _coconut_match_set_name_dt is not _coconut_sentinel:  #149:     case state:
                            dt = _coconut_match_set_name_dt  #149:     case state:
                        if _coconut_match_set_name_chrpr is not _coconut_sentinel:  #149:     case state:
                            chrpr = _coconut_match_set_name_chrpr  #149:     case state:
                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #149:     case state:
                            vr = _coconut_match_set_name_vr  #149:     case state:

                if not _coconut_case_match_check_7:  #149:     case state:
                    if (not _coconut_match_temp_79) and (_coconut.isinstance(_coconut_case_match_to_7[0], Numpy)):  #149:     case state:
                        _coconut_case_match_check_7 = True  #149:     case state:
                    if _coconut_case_match_check_7:  #149:     case state:
                        _coconut_case_match_check_7 = False  #149:     case state:
                        if not _coconut_case_match_check_7:  #149:     case state:
                            if _coconut.type(_coconut_case_match_to_7[0]) in _coconut_self_match_types:  #149:     case state:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #149:     case state:
                                _coconut_case_match_check_7 = True  #149:     case state:

                        if not _coconut_case_match_check_7:  #149:     case state:
                            _coconut_match_set_name_dt = _coconut_sentinel  #149:     case state:
                            _coconut_match_set_name_chrpr = _coconut_sentinel  #149:     case state:
                            _coconut_match_set_name_vr = _coconut_sentinel  #149:     case state:
                            if not _coconut.type(_coconut_case_match_to_7[0]) in _coconut_self_match_types:  #149:     case state:
                                _coconut_match_temp_81 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #149:     case state:
                                if not _coconut.isinstance(_coconut_match_temp_81, _coconut.tuple):  #149:     case state:
                                    raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #149:     case state:
                                if _coconut.len(_coconut_match_temp_81) < 4:  #149:     case state:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_81),))  #149:     case state:
                                _coconut_match_temp_82 = _coconut.getattr(_coconut_case_match_to_7[0], _coconut_match_temp_81[0], _coconut_sentinel)  #149:     case state:
                                _coconut_match_temp_83 = _coconut.getattr(_coconut_case_match_to_7[0], _coconut_match_temp_81[1], _coconut_sentinel)  #149:     case state:
                                _coconut_match_temp_84 = _coconut.getattr(_coconut_case_match_to_7[0], _coconut_match_temp_81[2], _coconut_sentinel)  #149:     case state:
                                _coconut_match_temp_85 = _coconut.getattr(_coconut_case_match_to_7[0], _coconut_match_temp_81[3], _coconut_sentinel)  #149:     case state:
                                if (_coconut_match_temp_82 is not _coconut_sentinel) and (_coconut_match_temp_83 is not _coconut_sentinel) and (_coconut_match_temp_83 == "BHWC") and (_coconut_match_temp_84 is not _coconut_sentinel) and (_coconut_match_temp_85 is not _coconut_sentinel):  #149:     case state:
                                    _coconut_match_set_name_dt = _coconut_match_temp_82  #149:     case state:
                                    _coconut_match_set_name_chrpr = _coconut_match_temp_84  #149:     case state:
                                    _coconut_match_set_name_vr = _coconut_match_temp_85  #149:     case state:
                                    _coconut_case_match_check_7 = True  #149:     case state:
                            if _coconut_case_match_check_7:  #149:     case state:
                                if _coconut_match_set_name_dt is not _coconut_sentinel:  #149:     case state:
                                    dt = _coconut_match_set_name_dt  #149:     case state:
                                if _coconut_match_set_name_chrpr is not _coconut_sentinel:  #149:     case state:
                                    chrpr = _coconut_match_set_name_chrpr  #149:     case state:
                                if _coconut_match_set_name_vr is not _coconut_sentinel:  #149:     case state:
                                    vr = _coconut_match_set_name_vr  #149:     case state:




            if _coconut_case_match_check_7:  #149:     case state:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #149:     case state:
                    meta = _coconut_match_set_name_meta  #149:     case state:

        if not _coconut_case_match_check_7:  #149:     case state:
            if (not _coconut_match_temp_78) and (_coconut.isinstance(_coconut_case_match_to_7, ImageDef)):  #149:     case state:
                _coconut_case_match_check_7 = True  #149:     case state:
            if _coconut_case_match_check_7:  #149:     case state:
                _coconut_case_match_check_7 = False  #149:     case state:
                if not _coconut_case_match_check_7:  #149:     case state:
                    if _coconut.type(_coconut_case_match_to_7) in _coconut_self_match_types:  #149:     case state:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #149:     case state:
                        _coconut_case_match_check_7 = True  #149:     case state:

                if not _coconut_case_match_check_7:  #149:     case state:
                    _coconut_match_set_name_meta = _coconut_sentinel  #149:     case state:
                    if not _coconut.type(_coconut_case_match_to_7) in _coconut_self_match_types:  #149:     case state:
                        _coconut_match_temp_87 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #149:     case state:
                        if not _coconut.isinstance(_coconut_match_temp_87, _coconut.tuple):  #149:     case state:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #149:     case state:
                        if _coconut.len(_coconut_match_temp_87) < 2:  #149:     case state:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_87),))  #149:     case state:
                        _coconut_match_temp_88 = _coconut.getattr(_coconut_case_match_to_7, _coconut_match_temp_87[0], _coconut_sentinel)  #149:     case state:
                        _coconut_match_temp_96 = _coconut.getattr(_coconut_case_match_to_7, _coconut_match_temp_87[1], _coconut_sentinel)  #149:     case state:
                        if (_coconut_match_temp_88 is not _coconut_sentinel) and (_coconut_match_temp_96 is not _coconut_sentinel):  #149:     case state:
                            _coconut_match_temp_89 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #149:     case state:
                            _coconut_match_set_name_meta = _coconut_match_temp_96  #149:     case state:
                            _coconut_case_match_check_7 = True  #149:     case state:
                    if _coconut_case_match_check_7:  #149:     case state:
                        _coconut_case_match_check_7 = False  #149:     case state:
                        if not _coconut_case_match_check_7:  #149:     case state:
                            _coconut_match_set_name_dt = _coconut_sentinel  #149:     case state:
                            _coconut_match_set_name_chrpr = _coconut_sentinel  #149:     case state:
                            _coconut_match_set_name_vr = _coconut_sentinel  #149:     case state:
                            if (_coconut_match_temp_89) and (_coconut.isinstance(_coconut_match_temp_88, Numpy)) and (_coconut.len(_coconut_match_temp_88) >= 4) and (_coconut_match_temp_88[1] == "BHWC"):  #149:     case state:
                                _coconut_match_set_name_dt = _coconut_match_temp_88[0]  #149:     case state:
                                _coconut_match_set_name_chrpr = _coconut_match_temp_88[2]  #149:     case state:
                                _coconut_match_set_name_vr = _coconut_match_temp_88[3]  #149:     case state:
                                _coconut_match_temp_90 = _coconut.len(_coconut_match_temp_88) <= _coconut.max(4, _coconut.len(_coconut_match_temp_88.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_88, "_coconut_data_defaults", {}) and _coconut_match_temp_88[i] == _coconut.getattr(_coconut_match_temp_88, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_88.__match_args__))) if _coconut.hasattr(_coconut_match_temp_88, "__match_args__") else _coconut.len(_coconut_match_temp_88) == 4  # type: ignore  #149:     case state:
                                if _coconut_match_temp_90:  #149:     case state:
                                    _coconut_case_match_check_7 = True  #149:     case state:
                            if _coconut_case_match_check_7:  #149:     case state:
                                if _coconut_match_set_name_dt is not _coconut_sentinel:  #149:     case state:
                                    dt = _coconut_match_set_name_dt  #149:     case state:
                                if _coconut_match_set_name_chrpr is not _coconut_sentinel:  #149:     case state:
                                    chrpr = _coconut_match_set_name_chrpr  #149:     case state:
                                if _coconut_match_set_name_vr is not _coconut_sentinel:  #149:     case state:
                                    vr = _coconut_match_set_name_vr  #149:     case state:

                        if not _coconut_case_match_check_7:  #149:     case state:
                            if (not _coconut_match_temp_89) and (_coconut.isinstance(_coconut_match_temp_88, Numpy)):  #149:     case state:
                                _coconut_case_match_check_7 = True  #149:     case state:
                            if _coconut_case_match_check_7:  #149:     case state:
                                _coconut_case_match_check_7 = False  #149:     case state:
                                if not _coconut_case_match_check_7:  #149:     case state:
                                    if _coconut.type(_coconut_match_temp_88) in _coconut_self_match_types:  #149:     case state:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #149:     case state:
                                        _coconut_case_match_check_7 = True  #149:     case state:

                                if not _coconut_case_match_check_7:  #149:     case state:
                                    _coconut_match_set_name_dt = _coconut_sentinel  #149:     case state:
                                    _coconut_match_set_name_chrpr = _coconut_sentinel  #149:     case state:
                                    _coconut_match_set_name_vr = _coconut_sentinel  #149:     case state:
                                    if not _coconut.type(_coconut_match_temp_88) in _coconut_self_match_types:  #149:     case state:
                                        _coconut_match_temp_91 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #149:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_91, _coconut.tuple):  #149:     case state:
                                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #149:     case state:
                                        if _coconut.len(_coconut_match_temp_91) < 4:  #149:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_91),))  #149:     case state:
                                        _coconut_match_temp_92 = _coconut.getattr(_coconut_match_temp_88, _coconut_match_temp_91[0], _coconut_sentinel)  #149:     case state:
                                        _coconut_match_temp_93 = _coconut.getattr(_coconut_match_temp_88, _coconut_match_temp_91[1], _coconut_sentinel)  #149:     case state:
                                        _coconut_match_temp_94 = _coconut.getattr(_coconut_match_temp_88, _coconut_match_temp_91[2], _coconut_sentinel)  #149:     case state:
                                        _coconut_match_temp_95 = _coconut.getattr(_coconut_match_temp_88, _coconut_match_temp_91[3], _coconut_sentinel)  #149:     case state:
                                        if (_coconut_match_temp_92 is not _coconut_sentinel) and (_coconut_match_temp_93 is not _coconut_sentinel) and (_coconut_match_temp_93 == "BHWC") and (_coconut_match_temp_94 is not _coconut_sentinel) and (_coconut_match_temp_95 is not _coconut_sentinel):  #149:     case state:
                                            _coconut_match_set_name_dt = _coconut_match_temp_92  #149:     case state:
                                            _coconut_match_set_name_chrpr = _coconut_match_temp_94  #149:     case state:
                                            _coconut_match_set_name_vr = _coconut_match_temp_95  #149:     case state:
                                            _coconut_case_match_check_7 = True  #149:     case state:
                                    if _coconut_case_match_check_7:  #149:     case state:
                                        if _coconut_match_set_name_dt is not _coconut_sentinel:  #149:     case state:
                                            dt = _coconut_match_set_name_dt  #149:     case state:
                                        if _coconut_match_set_name_chrpr is not _coconut_sentinel:  #149:     case state:
                                            chrpr = _coconut_match_set_name_chrpr  #149:     case state:
                                        if _coconut_match_set_name_vr is not _coconut_sentinel:  #149:     case state:
                                            vr = _coconut_match_set_name_vr  #149:     case state:




                    if _coconut_case_match_check_7:  #149:     case state:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #149:     case state:
                            meta = _coconut_match_set_name_meta  #149:     case state:




    if _coconut_case_match_check_7:  #149:     case state:
        return ([(batch_to_tiled, ImageDef(Numpy(dt, "HWC", chrpr, vr), ms_batch_to_tiled(meta)), "numpy bhwc to hwc by tiling", 20),])  #151:             return [(


def rule_img2widget(state):  #158: def rule_img2widget(state):
    _coconut_case_match_to_8 = state  #159:     case state:
    _coconut_case_match_check_8 = False  #159:     case state:
    _coconut_match_temp_97 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #159:     case state:
    _coconut_case_match_check_8 = True  #159:     case state:
    if _coconut_case_match_check_8:  #159:     case state:
        _coconut_case_match_check_8 = False  #159:     case state:
        if not _coconut_case_match_check_8:  #159:     case state:
            _coconut_match_set_name_meta = _coconut_sentinel  #159:     case state:
            if (_coconut_match_temp_97) and (_coconut.isinstance(_coconut_case_match_to_8, ImageDef)) and (_coconut.len(_coconut_case_match_to_8) >= 2):  #159:     case state:
                _coconut_match_temp_98 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #159:     case state:
                _coconut_match_set_name_meta = _coconut_case_match_to_8[1]  #159:     case state:
                _coconut_match_temp_103 = _coconut.len(_coconut_case_match_to_8) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_8.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_8, "_coconut_data_defaults", {}) and _coconut_case_match_to_8[i] == _coconut.getattr(_coconut_case_match_to_8, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_8.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_8, "__match_args__") else _coconut.len(_coconut_case_match_to_8) == 2  # type: ignore  #159:     case state:
                if _coconut_match_temp_103:  #159:     case state:
                    _coconut_case_match_check_8 = True  #159:     case state:
            if _coconut_case_match_check_8:  #159:     case state:
                _coconut_case_match_check_8 = False  #159:     case state:
                if not _coconut_case_match_check_8:  #159:     case state:
                    if (_coconut_match_temp_98) and (_coconut.isinstance(_coconut_case_match_to_8[0], PILImage)) and (_coconut.len(_coconut_case_match_to_8[0]) >= 2):  #159:     case state:
                        _coconut_match_temp_99 = _coconut.len(_coconut_case_match_to_8[0]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_8[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_8[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_8[0][i] == _coconut.getattr(_coconut_case_match_to_8[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_8[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_8[0], "__match_args__") else _coconut.len(_coconut_case_match_to_8[0]) == 2  # type: ignore  #159:     case state:
                        if _coconut_match_temp_99:  #159:     case state:
                            _coconut_case_match_check_8 = True  #159:     case state:

                if not _coconut_case_match_check_8:  #159:     case state:
                    if (not _coconut_match_temp_98) and (_coconut.isinstance(_coconut_case_match_to_8[0], PILImage)):  #159:     case state:
                        _coconut_case_match_check_8 = True  #159:     case state:
                    if _coconut_case_match_check_8:  #159:     case state:
                        _coconut_case_match_check_8 = False  #159:     case state:
                        if not _coconut_case_match_check_8:  #159:     case state:
                            if _coconut.type(_coconut_case_match_to_8[0]) in _coconut_self_match_types:  #159:     case state:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #159:     case state:
                                _coconut_case_match_check_8 = True  #159:     case state:

                        if not _coconut_case_match_check_8:  #159:     case state:
                            if not _coconut.type(_coconut_case_match_to_8[0]) in _coconut_self_match_types:  #159:     case state:
                                _coconut_match_temp_100 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #159:     case state:
                                if not _coconut.isinstance(_coconut_match_temp_100, _coconut.tuple):  #159:     case state:
                                    raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #159:     case state:
                                if _coconut.len(_coconut_match_temp_100) < 2:  #159:     case state:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_100),))  #159:     case state:
                                _coconut_match_temp_101 = _coconut.getattr(_coconut_case_match_to_8[0], _coconut_match_temp_100[0], _coconut_sentinel)  #159:     case state:
                                _coconut_match_temp_102 = _coconut.getattr(_coconut_case_match_to_8[0], _coconut_match_temp_100[1], _coconut_sentinel)  #159:     case state:
                                if (_coconut_match_temp_101 is not _coconut_sentinel) and (_coconut_match_temp_102 is not _coconut_sentinel):  #159:     case state:
                                    _coconut_case_match_check_8 = True  #159:     case state:




            if _coconut_case_match_check_8:  #159:     case state:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #159:     case state:
                    meta = _coconut_match_set_name_meta  #159:     case state:

        if not _coconut_case_match_check_8:  #159:     case state:
            if (not _coconut_match_temp_97) and (_coconut.isinstance(_coconut_case_match_to_8, ImageDef)):  #159:     case state:
                _coconut_case_match_check_8 = True  #159:     case state:
            if _coconut_case_match_check_8:  #159:     case state:
                _coconut_case_match_check_8 = False  #159:     case state:
                if not _coconut_case_match_check_8:  #159:     case state:
                    if _coconut.type(_coconut_case_match_to_8) in _coconut_self_match_types:  #159:     case state:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #159:     case state:
                        _coconut_case_match_check_8 = True  #159:     case state:

                if not _coconut_case_match_check_8:  #159:     case state:
                    _coconut_match_set_name_meta = _coconut_sentinel  #159:     case state:
                    if not _coconut.type(_coconut_case_match_to_8) in _coconut_self_match_types:  #159:     case state:
                        _coconut_match_temp_104 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #159:     case state:
                        if not _coconut.isinstance(_coconut_match_temp_104, _coconut.tuple):  #159:     case state:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #159:     case state:
                        if _coconut.len(_coconut_match_temp_104) < 2:  #159:     case state:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_104),))  #159:     case state:
                        _coconut_match_temp_105 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_104[0], _coconut_sentinel)  #159:     case state:
                        _coconut_match_temp_111 = _coconut.getattr(_coconut_case_match_to_8, _coconut_match_temp_104[1], _coconut_sentinel)  #159:     case state:
                        if (_coconut_match_temp_105 is not _coconut_sentinel) and (_coconut_match_temp_111 is not _coconut_sentinel):  #159:     case state:
                            _coconut_match_temp_106 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #159:     case state:
                            _coconut_match_set_name_meta = _coconut_match_temp_111  #159:     case state:
                            _coconut_case_match_check_8 = True  #159:     case state:
                    if _coconut_case_match_check_8:  #159:     case state:
                        _coconut_case_match_check_8 = False  #159:     case state:
                        if not _coconut_case_match_check_8:  #159:     case state:
                            if (_coconut_match_temp_106) and (_coconut.isinstance(_coconut_match_temp_105, PILImage)) and (_coconut.len(_coconut_match_temp_105) >= 2):  #159:     case state:
                                _coconut_match_temp_107 = _coconut.len(_coconut_match_temp_105) <= _coconut.max(2, _coconut.len(_coconut_match_temp_105.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_105, "_coconut_data_defaults", {}) and _coconut_match_temp_105[i] == _coconut.getattr(_coconut_match_temp_105, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_match_temp_105.__match_args__))) if _coconut.hasattr(_coconut_match_temp_105, "__match_args__") else _coconut.len(_coconut_match_temp_105) == 2  # type: ignore  #159:     case state:
                                if _coconut_match_temp_107:  #159:     case state:
                                    _coconut_case_match_check_8 = True  #159:     case state:

                        if not _coconut_case_match_check_8:  #159:     case state:
                            if (not _coconut_match_temp_106) and (_coconut.isinstance(_coconut_match_temp_105, PILImage)):  #159:     case state:
                                _coconut_case_match_check_8 = True  #159:     case state:
                            if _coconut_case_match_check_8:  #159:     case state:
                                _coconut_case_match_check_8 = False  #159:     case state:
                                if not _coconut_case_match_check_8:  #159:     case state:
                                    if _coconut.type(_coconut_match_temp_105) in _coconut_self_match_types:  #159:     case state:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #159:     case state:
                                        _coconut_case_match_check_8 = True  #159:     case state:

                                if not _coconut_case_match_check_8:  #159:     case state:
                                    if not _coconut.type(_coconut_match_temp_105) in _coconut_self_match_types:  #159:     case state:
                                        _coconut_match_temp_108 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #159:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_108, _coconut.tuple):  #159:     case state:
                                            raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #159:     case state:
                                        if _coconut.len(_coconut_match_temp_108) < 2:  #159:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_108),))  #159:     case state:
                                        _coconut_match_temp_109 = _coconut.getattr(_coconut_match_temp_105, _coconut_match_temp_108[0], _coconut_sentinel)  #159:     case state:
                                        _coconut_match_temp_110 = _coconut.getattr(_coconut_match_temp_105, _coconut_match_temp_108[1], _coconut_sentinel)  #159:     case state:
                                        if (_coconut_match_temp_109 is not _coconut_sentinel) and (_coconut_match_temp_110 is not _coconut_sentinel):  #159:     case state:
                                            _coconut_case_match_check_8 = True  #159:     case state:




                    if _coconut_case_match_check_8:  #159:     case state:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #159:     case state:
                            meta = _coconut_match_set_name_meta  #159:     case state:




    if _coconut_case_match_check_8:  #159:     case state:
        return ([(infer_widget, "widget", "infer_widget", 1),])  #161:             return [(


def dict2imdef(state):  #168: def dict2imdef(state):
    if isinstance(state, Mapping):  #169:     if isinstance(state,Mapping):
        _coconut_case_match_to_9 = state  #170:         case state:
        _coconut_case_match_check_9 = False  #170:         case state:
        _coconut_match_set_name__dtype = _coconut_sentinel  #170:         case state:
        _coconut_match_set_name__arng = _coconut_sentinel  #170:         case state:
        _coconut_match_set_name__ch_rpr = _coconut_sentinel  #170:         case state:
        _coconut_match_set_name__v_range = _coconut_sentinel  #170:         case state:
        _coconut_match_set_name_meta = _coconut_sentinel  #170:         case state:
        if _coconut.isinstance(_coconut_case_match_to_9, _coconut.abc.Mapping):  #170:         case state:
            _coconut_match_temp_112 = _coconut_case_match_to_9.get("type", _coconut_sentinel)  #170:         case state:
            _coconut_match_temp_113 = _coconut_case_match_to_9.get("dtype", _coconut_sentinel)  #170:         case state:
            _coconut_match_temp_114 = _coconut_case_match_to_9.get("arrange", _coconut_sentinel)  #170:         case state:
            _coconut_match_temp_115 = _coconut_case_match_to_9.get("ch_rpr", _coconut_sentinel)  #170:         case state:
            _coconut_match_temp_116 = _coconut_case_match_to_9.get("v_range", _coconut_sentinel)  #170:         case state:
            _coconut_match_temp_117 = _coconut_case_match_to_9.get("meta", _coconut_sentinel)  #170:         case state:
            if (_coconut_match_temp_112 is not _coconut_sentinel) and (_coconut_match_temp_112 == "numpy") and (_coconut_match_temp_113 is not _coconut_sentinel) and (_coconut_match_temp_114 is not _coconut_sentinel) and (_coconut_match_temp_115 is not _coconut_sentinel) and (_coconut_match_temp_116 is not _coconut_sentinel) and (_coconut_match_temp_117 is not _coconut_sentinel):  #170:         case state:
                _coconut_match_set_name__dtype = _coconut_match_temp_113  #170:         case state:
                _coconut_match_set_name__arng = _coconut_match_temp_114  #170:         case state:
                _coconut_match_set_name__ch_rpr = _coconut_match_temp_115  #170:         case state:
                _coconut_match_set_name__v_range = _coconut_match_temp_116  #170:         case state:
                _coconut_match_set_name_meta = _coconut_match_temp_117  #170:         case state:
                _coconut_case_match_check_9 = True  #170:         case state:
        if _coconut_case_match_check_9:  #170:         case state:
            if _coconut_match_set_name__dtype is not _coconut_sentinel:  #170:         case state:
                _dtype = _coconut_match_set_name__dtype  #170:         case state:
            if _coconut_match_set_name__arng is not _coconut_sentinel:  #170:         case state:
                _arng = _coconut_match_set_name__arng  #170:         case state:
            if _coconut_match_set_name__ch_rpr is not _coconut_sentinel:  #170:         case state:
                _ch_rpr = _coconut_match_set_name__ch_rpr  #170:         case state:
            if _coconut_match_set_name__v_range is not _coconut_sentinel:  #170:         case state:
                _v_range = _coconut_match_set_name__v_range  #170:         case state:
            if _coconut_match_set_name_meta is not _coconut_sentinel:  #170:         case state:
                meta = _coconut_match_set_name_meta  #170:         case state:
        if _coconut_case_match_check_9:  #170:         case state:
            return ([ImageDef(Numpy(_dtype, _arng, _ch_rpr, _v_range), meta),])  #172:                 return [ImageDef(Numpy(_dtype,_arng,_ch_rpr,_v_range),meta)]
        if not _coconut_case_match_check_9:  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            _coconut_match_set_name__dtype = _coconut_sentinel  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            _coconut_match_set_name__arng = _coconut_sentinel  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            _coconut_match_set_name__ch_rpr = _coconut_sentinel  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            _coconut_match_set_name__v_range = _coconut_sentinel  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            _coconut_match_set_name_meta = _coconut_sentinel  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            if _coconut.isinstance(_coconut_case_match_to_9, _coconut.abc.Mapping):  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_118 = _coconut_case_match_to_9.get("type", _coconut_sentinel)  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_119 = _coconut_case_match_to_9.get("dtype", _coconut_sentinel)  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_120 = _coconut_case_match_to_9.get("arrange", _coconut_sentinel)  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_121 = _coconut_case_match_to_9.get("ch_rpr", _coconut_sentinel)  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_122 = _coconut_case_match_to_9.get("v_range", _coconut_sentinel)  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                _coconut_match_temp_123 = _coconut_case_match_to_9.get("meta", _coconut_sentinel)  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if (_coconut_match_temp_118 is not _coconut_sentinel) and (_coconut_match_temp_118 == "torch") and (_coconut_match_temp_119 is not _coconut_sentinel) and (_coconut_match_temp_120 is not _coconut_sentinel) and (_coconut_match_temp_121 is not _coconut_sentinel) and (_coconut_match_temp_122 is not _coconut_sentinel) and (_coconut_match_temp_123 is not _coconut_sentinel):  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_match_set_name__dtype = _coconut_match_temp_119  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_match_set_name__arng = _coconut_match_temp_120  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_match_set_name__ch_rpr = _coconut_match_temp_121  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_match_set_name__v_range = _coconut_match_temp_122  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_match_set_name_meta = _coconut_match_temp_123  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _coconut_case_match_check_9 = True  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            if _coconut_case_match_check_9:  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if _coconut_match_set_name__dtype is not _coconut_sentinel:  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _dtype = _coconut_match_set_name__dtype  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if _coconut_match_set_name__arng is not _coconut_sentinel:  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _arng = _coconut_match_set_name__arng  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if _coconut_match_set_name__ch_rpr is not _coconut_sentinel:  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _ch_rpr = _coconut_match_set_name__ch_rpr  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if _coconut_match_set_name__v_range is not _coconut_sentinel:  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    _v_range = _coconut_match_set_name__v_range  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                    meta = _coconut_match_set_name_meta  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
            if _coconut_case_match_check_9:  #173:             match {"type":"torch","dtype":_dtype,"arrange":_arng,"ch_rpr":_ch_rpr,"v_range":_v_range,"meta":meta}:
                return ([ImageDef(Torch(_dtype, _arng, _ch_rpr, _v_range), meta),])  #174:                 return [ImageDef(Torch(_dtype,_arng,_ch_rpr,_v_range),meta)]
        if not _coconut_case_match_check_9:  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name__mode = _coconut_sentinel  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name__ch_rpr = _coconut_sentinel  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name_meta = _coconut_sentinel  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if _coconut.isinstance(_coconut_case_match_to_9, _coconut.abc.Mapping):  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_124 = _coconut_case_match_to_9.get("type", _coconut_sentinel)  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_125 = _coconut_case_match_to_9.get("mode", _coconut_sentinel)  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_126 = _coconut_case_match_to_9.get("ch_rpr", _coconut_sentinel)  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_127 = _coconut_case_match_to_9.get("meta", _coconut_sentinel)  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if (_coconut_match_temp_124 is not _coconut_sentinel) and (_coconut_match_temp_124 == "image") and (_coconut_match_temp_125 is not _coconut_sentinel) and (_coconut_match_temp_126 is not _coconut_sentinel) and (_coconut_match_temp_127 is not _coconut_sentinel):  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name__mode = _coconut_match_temp_125  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name__ch_rpr = _coconut_match_temp_126  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name_meta = _coconut_match_temp_127  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_case_match_check_9 = True  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if _coconut_case_match_check_9:  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name__mode is not _coconut_sentinel:  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _mode = _coconut_match_set_name__mode  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name__ch_rpr is not _coconut_sentinel:  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _ch_rpr = _coconut_match_set_name__ch_rpr  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    meta = _coconut_match_set_name_meta  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if _coconut_case_match_check_9:  #175:             match {"type":"image","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                return ([ImageDef(PILImage(_mode, _ch_rpr), meta),])  #176:                 return [ImageDef(PILImage(_mode,_ch_rpr),meta)]
        if not _coconut_case_match_check_9:  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name__mode = _coconut_sentinel  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name__ch_rpr = _coconut_sentinel  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            _coconut_match_set_name_meta = _coconut_sentinel  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if _coconut.isinstance(_coconut_case_match_to_9, _coconut.abc.Mapping):  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_128 = _coconut_case_match_to_9.get("type", _coconut_sentinel)  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_129 = _coconut_case_match_to_9.get("mode", _coconut_sentinel)  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_130 = _coconut_case_match_to_9.get("ch_rpr", _coconut_sentinel)  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                _coconut_match_temp_131 = _coconut_case_match_to_9.get("meta", _coconut_sentinel)  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if (_coconut_match_temp_128 is not _coconut_sentinel) and (_coconut_match_temp_128 == "images") and (_coconut_match_temp_129 is not _coconut_sentinel) and (_coconut_match_temp_130 is not _coconut_sentinel) and (_coconut_match_temp_131 is not _coconut_sentinel):  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name__mode = _coconut_match_temp_129  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name__ch_rpr = _coconut_match_temp_130  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_match_set_name_meta = _coconut_match_temp_131  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _coconut_case_match_check_9 = True  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if _coconut_case_match_check_9:  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name__mode is not _coconut_sentinel:  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _mode = _coconut_match_set_name__mode  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name__ch_rpr is not _coconut_sentinel:  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    _ch_rpr = _coconut_match_set_name__ch_rpr  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                    meta = _coconut_match_set_name_meta  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
            if _coconut_case_match_check_9:  #177:             match {"type":"images","mode":_mode,"ch_rpr":_ch_rpr,"meta":meta}:
                return ([ImageDef(PILImages(_mode, _ch_rpr), meta),])  #178:                 return [ImageDef(PILImages(_mode,_ch_rpr),meta)]


def rule_numpy2img(state):  #180: def rule_numpy2img(state):
    if isinstance(state, Mapping):  #181:     if isinstance(state,Mapping):
        _coconut_case_match_to_10 = state  #182:         case state:
        _coconut_case_match_check_10 = False  #182:         case state:
        _coconut_match_set_name_cr = _coconut_sentinel  #182:         case state:
        _coconut_match_set_name_meta = _coconut_sentinel  #182:         case state:
        if _coconut.isinstance(_coconut_case_match_to_10, _coconut.abc.Mapping):  #182:         case state:
            _coconut_match_temp_132 = _coconut_case_match_to_10.get("type", _coconut_sentinel)  #182:         case state:
            _coconut_match_temp_133 = _coconut_case_match_to_10.get("dtype", _coconut_sentinel)  #182:         case state:
            _coconut_match_temp_134 = _coconut_case_match_to_10.get("ch_rpr", _coconut_sentinel)  #182:         case state:
            _coconut_match_temp_135 = _coconut_case_match_to_10.get("arrange", _coconut_sentinel)  #182:         case state:
            _coconut_match_temp_136 = _coconut_case_match_to_10.get("v_range", _coconut_sentinel)  #182:         case state:
            _coconut_match_temp_137 = _coconut_case_match_to_10.get("meta", _coconut_sentinel)  #182:         case state:
            if (_coconut_match_temp_132 is not _coconut_sentinel) and (_coconut_match_temp_132 == "numpy") and (_coconut_match_temp_133 is not _coconut_sentinel) and (_coconut_match_temp_133 == "uint8") and (_coconut_match_temp_134 is not _coconut_sentinel) and (_coconut_match_temp_135 is not _coconut_sentinel) and (_coconut_match_temp_135 == "HWC") and (_coconut_match_temp_136 is not _coconut_sentinel) and (_coconut_match_temp_136 == "0_255") and (_coconut_match_temp_137 is not _coconut_sentinel):  #182:         case state:
                _coconut_match_set_name_cr = _coconut_match_temp_134  #182:         case state:
                _coconut_match_set_name_meta = _coconut_match_temp_137  #182:         case state:
                _coconut_case_match_check_10 = True  #182:         case state:
        if _coconut_case_match_check_10:  #182:         case state:
            _coconut_case_match_check_10 = False  #182:         case state:
            if not _coconut_case_match_check_10:  #182:         case state:
                if _coconut_match_temp_134 == "RGB":  #182:         case state:
                    _coconut_case_match_check_10 = True  #182:         case state:

            if not _coconut_case_match_check_10:  #182:         case state:
                if _coconut_match_temp_134 == "RGBA":  #182:         case state:
                    _coconut_case_match_check_10 = True  #182:         case state:

            if not _coconut_case_match_check_10:  #182:         case state:
                if _coconut_match_temp_134 == "YCbCr":  #182:         case state:
                    _coconut_case_match_check_10 = True  #182:         case state:


        if _coconut_case_match_check_10:  #182:         case state:
            if _coconut_match_set_name_cr is not _coconut_sentinel:  #182:         case state:
                cr = _coconut_match_set_name_cr  #182:         case state:
            if _coconut_match_set_name_meta is not _coconut_sentinel:  #182:         case state:
                meta = _coconut_match_set_name_meta  #182:         case state:
        if _coconut_case_match_check_10:  #182:         case state:
            return ([(Image.fromarray, ImageDef(PILImage(cr, cr), meta), "Image.fromarray", 1),])  #184:                 return [(
        if not _coconut_case_match_check_10:  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
            _coconut_match_set_name_meta = _coconut_sentinel  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
            if _coconut.isinstance(_coconut_case_match_to_10, _coconut.abc.Mapping):  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                _coconut_match_temp_138 = _coconut_case_match_to_10.get("type", _coconut_sentinel)  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                _coconut_match_temp_139 = _coconut_case_match_to_10.get("dtype", _coconut_sentinel)  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                _coconut_match_temp_140 = _coconut_case_match_to_10.get("ch_rpr", _coconut_sentinel)  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                _coconut_match_temp_141 = _coconut_case_match_to_10.get("arrange", _coconut_sentinel)  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                _coconut_match_temp_142 = _coconut_case_match_to_10.get("v_range", _coconut_sentinel)  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                _coconut_match_temp_143 = _coconut_case_match_to_10.get("meta", _coconut_sentinel)  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                if (_coconut_match_temp_138 is not _coconut_sentinel) and (_coconut_match_temp_138 == "numpy") and (_coconut_match_temp_139 is not _coconut_sentinel) and (_coconut_match_temp_139 == "uint8") and (_coconut_match_temp_140 is not _coconut_sentinel) and (_coconut_match_temp_140 == "L") and (_coconut_match_temp_141 is not _coconut_sentinel) and (_coconut_match_temp_141 == "HW") and (_coconut_match_temp_142 is not _coconut_sentinel) and (_coconut_match_temp_142 == "0_255") and (_coconut_match_temp_143 is not _coconut_sentinel):  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                    _coconut_match_set_name_meta = _coconut_match_temp_143  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                    _coconut_case_match_check_10 = True  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
            if _coconut_case_match_check_10:  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                    meta = _coconut_match_set_name_meta  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
            if _coconut_case_match_check_10:  #190:             match {"type":"numpy","dtype":"uint8","ch_rpr":"L","arrange":"HW","v_range":"0_255","meta":meta}:
                return ([(Image.fromarray, ImageDef(PILImage("L", "L"), meta), "Image.fromarray", 1),])  #191:                 return [(


def rule_image_path_to_image(state):  #198: def rule_image_path_to_image(state):
    if isinstance(state, str) and state == "image_path":  #199:     if isinstance(state,str) and state == "image_path":
        return ([(lambda p: Image.open(p).convert("RGB"), "image,RGB,RGB", "PIL.open ..> .convert('RGB')", 1),])  #200:        return [


def rule_format(state):  #209: def rule_format(state):
    if hasattr(state, "__neighbors__"):  #210:     if hasattr(state,"__neighbors__"):
        ngs = state.__neighbors__()  #211:         ngs = state.__neighbors__()
        if not isinstance(ngs, list):  #212:         if not isinstance(ngs,list):
            ngs = [ngs,]  #213:             ngs = [ngs]
        return (ngs)  #214:         return ngs


def to_spectral_img(img: '"PIL.Image.Image"'):  #216: def to_spectral_img(img:"PIL.Image.Image"):
#gray_img = img.convert('L')
# NumPy 配列にする
    f_xy = np.asarray(img)  #219:     f_xy = np.asarray(img)

# 2 次元高速フーリエ変換で周波数領域の情報を取り出す
    f_uv = np.fft.fft2(f_xy)  #222:     f_uv = np.fft.fft2(f_xy)
# 画像の中心に低周波数の成分がくるように並べかえる
    shifted_f_uv = np.fft.fftshift(f_uv)  #224:     shifted_f_uv = np.fft.fftshift(f_uv)

# パワースペクトルに変換する
    magnitude_spectrum2d = 20 * np.log(np.absolute(shifted_f_uv))  #227:     magnitude_spectrum2d = 20 * np.log(np.absolute(shifted_f_uv))
    return (magnitude_spectrum2d)  #228:     return magnitude_spectrum2d
#return auto("numpy,float64,HW,L,None")(magnitude_spectrum2d)


def rule_to_spectrum(state):  #231: def rule_to_spectrum(state):
    if state == "image,L,L":  #232:     if state == "image,L,L":
        return ([(to_spectral_img, "spectrum", "image,L,L => spectrum", 1),])  #233:         return [(


ms_img2L = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], s[1])))  #240: ms_img2L = (s->(s[0],s[1])) |> ss_to_ms$
ms_img2LA = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (s[0], s[1], 2)))  #241: ms_img2LA = (s->(s[0],s[1],2)) |> ss_to_ms$
def rule_image2gray(state):  #242: def rule_image2gray(state):
    _coconut_case_match_to_11 = state  #243:     case state:
    _coconut_case_match_check_11 = False  #243:     case state:
    _coconut_match_temp_144 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #243:     case state:
    _coconut_case_match_check_11 = True  #243:     case state:
    if _coconut_case_match_check_11:  #243:     case state:
        _coconut_case_match_check_11 = False  #243:     case state:
        if not _coconut_case_match_check_11:  #243:     case state:
            _coconut_match_set_name_meta = _coconut_sentinel  #243:     case state:
            if (_coconut_match_temp_144) and (_coconut.isinstance(_coconut_case_match_to_11, ImageDef)) and (_coconut.len(_coconut_case_match_to_11) >= 2):  #243:     case state:
                _coconut_match_temp_145 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #243:     case state:
                _coconut_match_set_name_meta = _coconut_case_match_to_11[1]  #243:     case state:
                _coconut_match_temp_150 = _coconut.len(_coconut_case_match_to_11) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_11.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_11, "_coconut_data_defaults", {}) and _coconut_case_match_to_11[i] == _coconut.getattr(_coconut_case_match_to_11, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_11.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_11, "__match_args__") else _coconut.len(_coconut_case_match_to_11) == 2  # type: ignore  #243:     case state:
                if _coconut_match_temp_150:  #243:     case state:
                    _coconut_case_match_check_11 = True  #243:     case state:
            if _coconut_case_match_check_11:  #243:     case state:
                _coconut_case_match_check_11 = False  #243:     case state:
                if not _coconut_case_match_check_11:  #243:     case state:
                    _coconut_match_set_name_ch_rpr = _coconut_sentinel  #243:     case state:
                    _coconut_match_set_name_ch_rpr2 = _coconut_sentinel  #243:     case state:
                    if (_coconut_match_temp_145) and (_coconut.isinstance(_coconut_case_match_to_11[0], PILImage)) and (_coconut.len(_coconut_case_match_to_11[0]) >= 2):  #243:     case state:
                        _coconut_match_set_name_ch_rpr = _coconut_case_match_to_11[0][0]  #243:     case state:
                        _coconut_match_set_name_ch_rpr2 = _coconut_case_match_to_11[0][1]  #243:     case state:
                        _coconut_match_temp_146 = _coconut.len(_coconut_case_match_to_11[0]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_11[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_11[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_11[0][i] == _coconut.getattr(_coconut_case_match_to_11[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_11[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_11[0], "__match_args__") else _coconut.len(_coconut_case_match_to_11[0]) == 2  # type: ignore  #243:     case state:
                        if _coconut_match_temp_146:  #243:     case state:
                            _coconut_case_match_check_11 = True  #243:     case state:
                    if _coconut_case_match_check_11:  #243:     case state:
                        if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #243:     case state:
                            ch_rpr = _coconut_match_set_name_ch_rpr  #243:     case state:
                        if _coconut_match_set_name_ch_rpr2 is not _coconut_sentinel:  #243:     case state:
                            ch_rpr2 = _coconut_match_set_name_ch_rpr2  #243:     case state:

                if not _coconut_case_match_check_11:  #243:     case state:
                    if (not _coconut_match_temp_145) and (_coconut.isinstance(_coconut_case_match_to_11[0], PILImage)):  #243:     case state:
                        _coconut_case_match_check_11 = True  #243:     case state:
                    if _coconut_case_match_check_11:  #243:     case state:
                        _coconut_case_match_check_11 = False  #243:     case state:
                        if not _coconut_case_match_check_11:  #243:     case state:
                            if _coconut.type(_coconut_case_match_to_11[0]) in _coconut_self_match_types:  #243:     case state:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #243:     case state:
                                _coconut_case_match_check_11 = True  #243:     case state:

                        if not _coconut_case_match_check_11:  #243:     case state:
                            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #243:     case state:
                            _coconut_match_set_name_ch_rpr2 = _coconut_sentinel  #243:     case state:
                            if not _coconut.type(_coconut_case_match_to_11[0]) in _coconut_self_match_types:  #243:     case state:
                                _coconut_match_temp_147 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #243:     case state:
                                if not _coconut.isinstance(_coconut_match_temp_147, _coconut.tuple):  #243:     case state:
                                    raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #243:     case state:
                                if _coconut.len(_coconut_match_temp_147) < 2:  #243:     case state:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_147),))  #243:     case state:
                                _coconut_match_temp_148 = _coconut.getattr(_coconut_case_match_to_11[0], _coconut_match_temp_147[0], _coconut_sentinel)  #243:     case state:
                                _coconut_match_temp_149 = _coconut.getattr(_coconut_case_match_to_11[0], _coconut_match_temp_147[1], _coconut_sentinel)  #243:     case state:
                                if (_coconut_match_temp_148 is not _coconut_sentinel) and (_coconut_match_temp_149 is not _coconut_sentinel):  #243:     case state:
                                    _coconut_match_set_name_ch_rpr = _coconut_match_temp_148  #243:     case state:
                                    _coconut_match_set_name_ch_rpr2 = _coconut_match_temp_149  #243:     case state:
                                    _coconut_case_match_check_11 = True  #243:     case state:
                            if _coconut_case_match_check_11:  #243:     case state:
                                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #243:     case state:
                                    ch_rpr = _coconut_match_set_name_ch_rpr  #243:     case state:
                                if _coconut_match_set_name_ch_rpr2 is not _coconut_sentinel:  #243:     case state:
                                    ch_rpr2 = _coconut_match_set_name_ch_rpr2  #243:     case state:




            if _coconut_case_match_check_11:  #243:     case state:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #243:     case state:
                    meta = _coconut_match_set_name_meta  #243:     case state:

        if not _coconut_case_match_check_11:  #243:     case state:
            if (not _coconut_match_temp_144) and (_coconut.isinstance(_coconut_case_match_to_11, ImageDef)):  #243:     case state:
                _coconut_case_match_check_11 = True  #243:     case state:
            if _coconut_case_match_check_11:  #243:     case state:
                _coconut_case_match_check_11 = False  #243:     case state:
                if not _coconut_case_match_check_11:  #243:     case state:
                    if _coconut.type(_coconut_case_match_to_11) in _coconut_self_match_types:  #243:     case state:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #243:     case state:
                        _coconut_case_match_check_11 = True  #243:     case state:

                if not _coconut_case_match_check_11:  #243:     case state:
                    _coconut_match_set_name_meta = _coconut_sentinel  #243:     case state:
                    if not _coconut.type(_coconut_case_match_to_11) in _coconut_self_match_types:  #243:     case state:
                        _coconut_match_temp_151 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #243:     case state:
                        if not _coconut.isinstance(_coconut_match_temp_151, _coconut.tuple):  #243:     case state:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #243:     case state:
                        if _coconut.len(_coconut_match_temp_151) < 2:  #243:     case state:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_151),))  #243:     case state:
                        _coconut_match_temp_152 = _coconut.getattr(_coconut_case_match_to_11, _coconut_match_temp_151[0], _coconut_sentinel)  #243:     case state:
                        _coconut_match_temp_158 = _coconut.getattr(_coconut_case_match_to_11, _coconut_match_temp_151[1], _coconut_sentinel)  #243:     case state:
                        if (_coconut_match_temp_152 is not _coconut_sentinel) and (_coconut_match_temp_158 is not _coconut_sentinel):  #243:     case state:
                            _coconut_match_temp_153 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #243:     case state:
                            _coconut_match_set_name_meta = _coconut_match_temp_158  #243:     case state:
                            _coconut_case_match_check_11 = True  #243:     case state:
                    if _coconut_case_match_check_11:  #243:     case state:
                        _coconut_case_match_check_11 = False  #243:     case state:
                        if not _coconut_case_match_check_11:  #243:     case state:
                            _coconut_match_set_name_ch_rpr = _coconut_sentinel  #243:     case state:
                            _coconut_match_set_name_ch_rpr2 = _coconut_sentinel  #243:     case state:
                            if (_coconut_match_temp_153) and (_coconut.isinstance(_coconut_match_temp_152, PILImage)) and (_coconut.len(_coconut_match_temp_152) >= 2):  #243:     case state:
                                _coconut_match_set_name_ch_rpr = _coconut_match_temp_152[0]  #243:     case state:
                                _coconut_match_set_name_ch_rpr2 = _coconut_match_temp_152[1]  #243:     case state:
                                _coconut_match_temp_154 = _coconut.len(_coconut_match_temp_152) <= _coconut.max(2, _coconut.len(_coconut_match_temp_152.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_152, "_coconut_data_defaults", {}) and _coconut_match_temp_152[i] == _coconut.getattr(_coconut_match_temp_152, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_match_temp_152.__match_args__))) if _coconut.hasattr(_coconut_match_temp_152, "__match_args__") else _coconut.len(_coconut_match_temp_152) == 2  # type: ignore  #243:     case state:
                                if _coconut_match_temp_154:  #243:     case state:
                                    _coconut_case_match_check_11 = True  #243:     case state:
                            if _coconut_case_match_check_11:  #243:     case state:
                                if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #243:     case state:
                                    ch_rpr = _coconut_match_set_name_ch_rpr  #243:     case state:
                                if _coconut_match_set_name_ch_rpr2 is not _coconut_sentinel:  #243:     case state:
                                    ch_rpr2 = _coconut_match_set_name_ch_rpr2  #243:     case state:

                        if not _coconut_case_match_check_11:  #243:     case state:
                            if (not _coconut_match_temp_153) and (_coconut.isinstance(_coconut_match_temp_152, PILImage)):  #243:     case state:
                                _coconut_case_match_check_11 = True  #243:     case state:
                            if _coconut_case_match_check_11:  #243:     case state:
                                _coconut_case_match_check_11 = False  #243:     case state:
                                if not _coconut_case_match_check_11:  #243:     case state:
                                    if _coconut.type(_coconut_match_temp_152) in _coconut_self_match_types:  #243:     case state:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #243:     case state:
                                        _coconut_case_match_check_11 = True  #243:     case state:

                                if not _coconut_case_match_check_11:  #243:     case state:
                                    _coconut_match_set_name_ch_rpr = _coconut_sentinel  #243:     case state:
                                    _coconut_match_set_name_ch_rpr2 = _coconut_sentinel  #243:     case state:
                                    if not _coconut.type(_coconut_match_temp_152) in _coconut_self_match_types:  #243:     case state:
                                        _coconut_match_temp_155 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #243:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_155, _coconut.tuple):  #243:     case state:
                                            raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #243:     case state:
                                        if _coconut.len(_coconut_match_temp_155) < 2:  #243:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_155),))  #243:     case state:
                                        _coconut_match_temp_156 = _coconut.getattr(_coconut_match_temp_152, _coconut_match_temp_155[0], _coconut_sentinel)  #243:     case state:
                                        _coconut_match_temp_157 = _coconut.getattr(_coconut_match_temp_152, _coconut_match_temp_155[1], _coconut_sentinel)  #243:     case state:
                                        if (_coconut_match_temp_156 is not _coconut_sentinel) and (_coconut_match_temp_157 is not _coconut_sentinel):  #243:     case state:
                                            _coconut_match_set_name_ch_rpr = _coconut_match_temp_156  #243:     case state:
                                            _coconut_match_set_name_ch_rpr2 = _coconut_match_temp_157  #243:     case state:
                                            _coconut_case_match_check_11 = True  #243:     case state:
                                    if _coconut_case_match_check_11:  #243:     case state:
                                        if _coconut_match_set_name_ch_rpr is not _coconut_sentinel:  #243:     case state:
                                            ch_rpr = _coconut_match_set_name_ch_rpr  #243:     case state:
                                        if _coconut_match_set_name_ch_rpr2 is not _coconut_sentinel:  #243:     case state:
                                            ch_rpr2 = _coconut_match_set_name_ch_rpr2  #243:     case state:




                    if _coconut_case_match_check_11:  #243:     case state:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #243:     case state:
                            meta = _coconut_match_set_name_meta  #243:     case state:




    if _coconut_case_match_check_11:  #243:     case state:
        return ([(_coconut.operator.methodcaller("convert", "L"), ImageDef(PILImage("L", "L"), (ms_img2L)(meta)), "image2gray", 10), (_coconut.operator.methodcaller("convert", "LA"), ImageDef(PILImage("LA", "LA"), (ms_img2LA)(meta)), "image2gray-alpha", 10)])  #245:             return [


def rule_image2lab(state):  #250: def rule_image2lab(state):
    from skimage import color  #251:     from skimage import color
    _coconut_case_match_to_12 = state  #252:     case state:
    _coconut_case_match_check_12 = False  #252:     case state:
    _coconut_match_temp_159 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #252:     case state:
    _coconut_case_match_check_12 = True  #252:     case state:
    if _coconut_case_match_check_12:  #252:     case state:
        _coconut_case_match_check_12 = False  #252:     case state:
        if not _coconut_case_match_check_12:  #252:     case state:
            _coconut_match_set_name_meta = _coconut_sentinel  #252:     case state:
            if (_coconut_match_temp_159) and (_coconut.isinstance(_coconut_case_match_to_12, ImageDef)) and (_coconut.len(_coconut_case_match_to_12) >= 2):  #252:     case state:
                _coconut_match_temp_160 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #252:     case state:
                _coconut_match_set_name_meta = _coconut_case_match_to_12[1]  #252:     case state:
                _coconut_match_temp_167 = _coconut.len(_coconut_case_match_to_12) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_12.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_12, "_coconut_data_defaults", {}) and _coconut_case_match_to_12[i] == _coconut.getattr(_coconut_case_match_to_12, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_12.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_12, "__match_args__") else _coconut.len(_coconut_case_match_to_12) == 2  # type: ignore  #252:     case state:
                if _coconut_match_temp_167:  #252:     case state:
                    _coconut_case_match_check_12 = True  #252:     case state:
            if _coconut_case_match_check_12:  #252:     case state:
                _coconut_case_match_check_12 = False  #252:     case state:
                if not _coconut_case_match_check_12:  #252:     case state:
                    if (_coconut_match_temp_160) and (_coconut.isinstance(_coconut_case_match_to_12[0], Numpy)) and (_coconut.len(_coconut_case_match_to_12[0]) >= 4) and (_coconut_case_match_to_12[0][0] == "float64") and (_coconut_case_match_to_12[0][1] == "HWC") and (_coconut_case_match_to_12[0][2] == "RGB") and (_coconut_case_match_to_12[0][3] == "0_1"):  #252:     case state:
                        _coconut_match_temp_161 = _coconut.len(_coconut_case_match_to_12[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_12[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_12[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_12[0][i] == _coconut.getattr(_coconut_case_match_to_12[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_12[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_12[0], "__match_args__") else _coconut.len(_coconut_case_match_to_12[0]) == 4  # type: ignore  #252:     case state:
                        if _coconut_match_temp_161:  #252:     case state:
                            _coconut_case_match_check_12 = True  #252:     case state:

                if not _coconut_case_match_check_12:  #252:     case state:
                    if (not _coconut_match_temp_160) and (_coconut.isinstance(_coconut_case_match_to_12[0], Numpy)):  #252:     case state:
                        _coconut_case_match_check_12 = True  #252:     case state:
                    if _coconut_case_match_check_12:  #252:     case state:
                        _coconut_case_match_check_12 = False  #252:     case state:
                        if not _coconut_case_match_check_12:  #252:     case state:
                            if _coconut.type(_coconut_case_match_to_12[0]) in _coconut_self_match_types:  #252:     case state:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #252:     case state:
                                _coconut_case_match_check_12 = True  #252:     case state:

                        if not _coconut_case_match_check_12:  #252:     case state:
                            if not _coconut.type(_coconut_case_match_to_12[0]) in _coconut_self_match_types:  #252:     case state:
                                _coconut_match_temp_162 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #252:     case state:
                                if not _coconut.isinstance(_coconut_match_temp_162, _coconut.tuple):  #252:     case state:
                                    raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #252:     case state:
                                if _coconut.len(_coconut_match_temp_162) < 4:  #252:     case state:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_162),))  #252:     case state:
                                _coconut_match_temp_163 = _coconut.getattr(_coconut_case_match_to_12[0], _coconut_match_temp_162[0], _coconut_sentinel)  #252:     case state:
                                _coconut_match_temp_164 = _coconut.getattr(_coconut_case_match_to_12[0], _coconut_match_temp_162[1], _coconut_sentinel)  #252:     case state:
                                _coconut_match_temp_165 = _coconut.getattr(_coconut_case_match_to_12[0], _coconut_match_temp_162[2], _coconut_sentinel)  #252:     case state:
                                _coconut_match_temp_166 = _coconut.getattr(_coconut_case_match_to_12[0], _coconut_match_temp_162[3], _coconut_sentinel)  #252:     case state:
                                if (_coconut_match_temp_163 is not _coconut_sentinel) and (_coconut_match_temp_163 == "float64") and (_coconut_match_temp_164 is not _coconut_sentinel) and (_coconut_match_temp_164 == "HWC") and (_coconut_match_temp_165 is not _coconut_sentinel) and (_coconut_match_temp_165 == "RGB") and (_coconut_match_temp_166 is not _coconut_sentinel) and (_coconut_match_temp_166 == "0_1"):  #252:     case state:
                                    _coconut_case_match_check_12 = True  #252:     case state:




            if _coconut_case_match_check_12:  #252:     case state:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #252:     case state:
                    meta = _coconut_match_set_name_meta  #252:     case state:

        if not _coconut_case_match_check_12:  #252:     case state:
            if (not _coconut_match_temp_159) and (_coconut.isinstance(_coconut_case_match_to_12, ImageDef)):  #252:     case state:
                _coconut_case_match_check_12 = True  #252:     case state:
            if _coconut_case_match_check_12:  #252:     case state:
                _coconut_case_match_check_12 = False  #252:     case state:
                if not _coconut_case_match_check_12:  #252:     case state:
                    if _coconut.type(_coconut_case_match_to_12) in _coconut_self_match_types:  #252:     case state:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #252:     case state:
                        _coconut_case_match_check_12 = True  #252:     case state:

                if not _coconut_case_match_check_12:  #252:     case state:
                    _coconut_match_set_name_meta = _coconut_sentinel  #252:     case state:
                    if not _coconut.type(_coconut_case_match_to_12) in _coconut_self_match_types:  #252:     case state:
                        _coconut_match_temp_168 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #252:     case state:
                        if not _coconut.isinstance(_coconut_match_temp_168, _coconut.tuple):  #252:     case state:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #252:     case state:
                        if _coconut.len(_coconut_match_temp_168) < 2:  #252:     case state:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_168),))  #252:     case state:
                        _coconut_match_temp_169 = _coconut.getattr(_coconut_case_match_to_12, _coconut_match_temp_168[0], _coconut_sentinel)  #252:     case state:
                        _coconut_match_temp_177 = _coconut.getattr(_coconut_case_match_to_12, _coconut_match_temp_168[1], _coconut_sentinel)  #252:     case state:
                        if (_coconut_match_temp_169 is not _coconut_sentinel) and (_coconut_match_temp_177 is not _coconut_sentinel):  #252:     case state:
                            _coconut_match_temp_170 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #252:     case state:
                            _coconut_match_set_name_meta = _coconut_match_temp_177  #252:     case state:
                            _coconut_case_match_check_12 = True  #252:     case state:
                    if _coconut_case_match_check_12:  #252:     case state:
                        _coconut_case_match_check_12 = False  #252:     case state:
                        if not _coconut_case_match_check_12:  #252:     case state:
                            if (_coconut_match_temp_170) and (_coconut.isinstance(_coconut_match_temp_169, Numpy)) and (_coconut.len(_coconut_match_temp_169) >= 4) and (_coconut_match_temp_169[0] == "float64") and (_coconut_match_temp_169[1] == "HWC") and (_coconut_match_temp_169[2] == "RGB") and (_coconut_match_temp_169[3] == "0_1"):  #252:     case state:
                                _coconut_match_temp_171 = _coconut.len(_coconut_match_temp_169) <= _coconut.max(4, _coconut.len(_coconut_match_temp_169.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_169, "_coconut_data_defaults", {}) and _coconut_match_temp_169[i] == _coconut.getattr(_coconut_match_temp_169, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_169.__match_args__))) if _coconut.hasattr(_coconut_match_temp_169, "__match_args__") else _coconut.len(_coconut_match_temp_169) == 4  # type: ignore  #252:     case state:
                                if _coconut_match_temp_171:  #252:     case state:
                                    _coconut_case_match_check_12 = True  #252:     case state:

                        if not _coconut_case_match_check_12:  #252:     case state:
                            if (not _coconut_match_temp_170) and (_coconut.isinstance(_coconut_match_temp_169, Numpy)):  #252:     case state:
                                _coconut_case_match_check_12 = True  #252:     case state:
                            if _coconut_case_match_check_12:  #252:     case state:
                                _coconut_case_match_check_12 = False  #252:     case state:
                                if not _coconut_case_match_check_12:  #252:     case state:
                                    if _coconut.type(_coconut_match_temp_169) in _coconut_self_match_types:  #252:     case state:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #252:     case state:
                                        _coconut_case_match_check_12 = True  #252:     case state:

                                if not _coconut_case_match_check_12:  #252:     case state:
                                    if not _coconut.type(_coconut_match_temp_169) in _coconut_self_match_types:  #252:     case state:
                                        _coconut_match_temp_172 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #252:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_172, _coconut.tuple):  #252:     case state:
                                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #252:     case state:
                                        if _coconut.len(_coconut_match_temp_172) < 4:  #252:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_172),))  #252:     case state:
                                        _coconut_match_temp_173 = _coconut.getattr(_coconut_match_temp_169, _coconut_match_temp_172[0], _coconut_sentinel)  #252:     case state:
                                        _coconut_match_temp_174 = _coconut.getattr(_coconut_match_temp_169, _coconut_match_temp_172[1], _coconut_sentinel)  #252:     case state:
                                        _coconut_match_temp_175 = _coconut.getattr(_coconut_match_temp_169, _coconut_match_temp_172[2], _coconut_sentinel)  #252:     case state:
                                        _coconut_match_temp_176 = _coconut.getattr(_coconut_match_temp_169, _coconut_match_temp_172[3], _coconut_sentinel)  #252:     case state:
                                        if (_coconut_match_temp_173 is not _coconut_sentinel) and (_coconut_match_temp_173 == "float64") and (_coconut_match_temp_174 is not _coconut_sentinel) and (_coconut_match_temp_174 == "HWC") and (_coconut_match_temp_175 is not _coconut_sentinel) and (_coconut_match_temp_175 == "RGB") and (_coconut_match_temp_176 is not _coconut_sentinel) and (_coconut_match_temp_176 == "0_1"):  #252:     case state:
                                            _coconut_case_match_check_12 = True  #252:     case state:




                    if _coconut_case_match_check_12:  #252:     case state:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #252:     case state:
                            meta = _coconut_match_set_name_meta  #252:     case state:




    if _coconut_case_match_check_12:  #252:     case state:
        return ([(color.rgb2lab, ImageDef(Numpy("float64", "HWC", "LAB", "LAB"), meta), "sklearn.color.rgb2lab"),])  #254:             return [
    if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
        _coconut_match_temp_178 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
        _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
        if _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
            _coconut_case_match_check_12 = False  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
            if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                if (_coconut_match_temp_178) and (_coconut.isinstance(_coconut_case_match_to_12, ImageDef)) and (_coconut.len(_coconut_case_match_to_12) >= 2):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                    _coconut_match_temp_179 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_12[1]  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                    _coconut_match_temp_186 = _coconut.len(_coconut_case_match_to_12) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_12.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_12, "_coconut_data_defaults", {}) and _coconut_case_match_to_12[i] == _coconut.getattr(_coconut_case_match_to_12, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_12.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_12, "__match_args__") else _coconut.len(_coconut_case_match_to_12) == 2  # type: ignore  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                    if _coconut_match_temp_186:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                        _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                if _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                    _coconut_case_match_check_12 = False  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                    if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                        if (_coconut_match_temp_179) and (_coconut.isinstance(_coconut_case_match_to_12[0], Numpy)) and (_coconut.len(_coconut_case_match_to_12[0]) >= 4) and (_coconut_case_match_to_12[0][0] == "float64") and (_coconut_case_match_to_12[0][1] == "HWC") and (_coconut_case_match_to_12[0][2] == "LAB") and (_coconut_case_match_to_12[0][3] == "LAB"):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            _coconut_match_temp_180 = _coconut.len(_coconut_case_match_to_12[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_12[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_12[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_12[0][i] == _coconut.getattr(_coconut_case_match_to_12[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_12[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_12[0], "__match_args__") else _coconut.len(_coconut_case_match_to_12[0]) == 4  # type: ignore  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            if _coconut_match_temp_180:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):

                    if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                        if (not _coconut_match_temp_179) and (_coconut.isinstance(_coconut_case_match_to_12[0], Numpy)):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                        if _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            _coconut_case_match_check_12 = False  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                if _coconut.type(_coconut_case_match_to_12[0]) in _coconut_self_match_types:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):

                            if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                if not _coconut.type(_coconut_case_match_to_12[0]) in _coconut_self_match_types:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    _coconut_match_temp_181 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_181, _coconut.tuple):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    if _coconut.len(_coconut_match_temp_181) < 4:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_181),))  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    _coconut_match_temp_182 = _coconut.getattr(_coconut_case_match_to_12[0], _coconut_match_temp_181[0], _coconut_sentinel)  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    _coconut_match_temp_183 = _coconut.getattr(_coconut_case_match_to_12[0], _coconut_match_temp_181[1], _coconut_sentinel)  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    _coconut_match_temp_184 = _coconut.getattr(_coconut_case_match_to_12[0], _coconut_match_temp_181[2], _coconut_sentinel)  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    _coconut_match_temp_185 = _coconut.getattr(_coconut_case_match_to_12[0], _coconut_match_temp_181[3], _coconut_sentinel)  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    if (_coconut_match_temp_182 is not _coconut_sentinel) and (_coconut_match_temp_182 == "float64") and (_coconut_match_temp_183 is not _coconut_sentinel) and (_coconut_match_temp_183 == "HWC") and (_coconut_match_temp_184 is not _coconut_sentinel) and (_coconut_match_temp_184 == "LAB") and (_coconut_match_temp_185 is not _coconut_sentinel) and (_coconut_match_temp_185 == "LAB"):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                        _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):




                if _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                        meta = _coconut_match_set_name_meta  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):

            if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                if (not _coconut_match_temp_178) and (_coconut.isinstance(_coconut_case_match_to_12, ImageDef)):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                    _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                if _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                    _coconut_case_match_check_12 = False  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                    if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                        if _coconut.type(_coconut_case_match_to_12) in _coconut_self_match_types:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):

                    if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                        if not _coconut.type(_coconut_case_match_to_12) in _coconut_self_match_types:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            _coconut_match_temp_187 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            if not _coconut.isinstance(_coconut_match_temp_187, _coconut.tuple):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            if _coconut.len(_coconut_match_temp_187) < 2:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_187),))  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            _coconut_match_temp_188 = _coconut.getattr(_coconut_case_match_to_12, _coconut_match_temp_187[0], _coconut_sentinel)  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            _coconut_match_temp_196 = _coconut.getattr(_coconut_case_match_to_12, _coconut_match_temp_187[1], _coconut_sentinel)  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            if (_coconut_match_temp_188 is not _coconut_sentinel) and (_coconut_match_temp_196 is not _coconut_sentinel):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                _coconut_match_temp_189 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_196  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                        if _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            _coconut_case_match_check_12 = False  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                if (_coconut_match_temp_189) and (_coconut.isinstance(_coconut_match_temp_188, Numpy)) and (_coconut.len(_coconut_match_temp_188) >= 4) and (_coconut_match_temp_188[0] == "float64") and (_coconut_match_temp_188[1] == "HWC") and (_coconut_match_temp_188[2] == "LAB") and (_coconut_match_temp_188[3] == "LAB"):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    _coconut_match_temp_190 = _coconut.len(_coconut_match_temp_188) <= _coconut.max(4, _coconut.len(_coconut_match_temp_188.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_188, "_coconut_data_defaults", {}) and _coconut_match_temp_188[i] == _coconut.getattr(_coconut_match_temp_188, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_188.__match_args__))) if _coconut.hasattr(_coconut_match_temp_188, "__match_args__") else _coconut.len(_coconut_match_temp_188) == 4  # type: ignore  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    if _coconut_match_temp_190:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                        _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):

                            if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                if (not _coconut_match_temp_189) and (_coconut.isinstance(_coconut_match_temp_188, Numpy)):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                if _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    _coconut_case_match_check_12 = False  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                    if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                        if _coconut.type(_coconut_match_temp_188) in _coconut_self_match_types:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                            _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):

                                    if not _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                        if not _coconut.type(_coconut_match_temp_188) in _coconut_self_match_types:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                            _coconut_match_temp_191 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_191, _coconut.tuple):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                            if _coconut.len(_coconut_match_temp_191) < 4:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_191),))  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                            _coconut_match_temp_192 = _coconut.getattr(_coconut_match_temp_188, _coconut_match_temp_191[0], _coconut_sentinel)  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                            _coconut_match_temp_193 = _coconut.getattr(_coconut_match_temp_188, _coconut_match_temp_191[1], _coconut_sentinel)  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                            _coconut_match_temp_194 = _coconut.getattr(_coconut_match_temp_188, _coconut_match_temp_191[2], _coconut_sentinel)  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                            _coconut_match_temp_195 = _coconut.getattr(_coconut_match_temp_188, _coconut_match_temp_191[3], _coconut_sentinel)  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                            if (_coconut_match_temp_192 is not _coconut_sentinel) and (_coconut_match_temp_192 == "float64") and (_coconut_match_temp_193 is not _coconut_sentinel) and (_coconut_match_temp_193 == "HWC") and (_coconut_match_temp_194 is not _coconut_sentinel) and (_coconut_match_temp_194 == "LAB") and (_coconut_match_temp_195 is not _coconut_sentinel) and (_coconut_match_temp_195 == "LAB"):  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                                _coconut_case_match_check_12 = True  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):




                        if _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
                                meta = _coconut_match_set_name_meta  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):




        if _coconut_case_match_check_12:  #257:         match ImageDef(Numpy("float64","HWC","LAB","LAB"),meta):
            return ([(color.lab2rgb, ImageDef(Numpy("float64", "HWC", "RGB", "0_1"), meta), "sklearn.color.lab2rgb"),])  #258:             return [


def convert_ignore_channel(ary, f):  #262: def convert_ignore_channel(ary,f):
    """
    shape:(H,W,C)
    """  #265:     """
    ignored = ary[:, :, [-1,]]  #266:     ignored = ary[:,:,[-1]]
    tgt = ary[:, :, :-1]  #267:     tgt = ary[:,:,:-1]
    converted = f(tgt)  #268:     converted = f(tgt)
    result = np.concatenate((tgt, ignored), axis=-1)  #269:     result = np.concatenate((tgt,ignored),axis=-1)
    return (result)  #270:     return result


def rule_rgba2laba(state):  #272: def rule_rgba2laba(state):
    from skimage import color  #273:     from skimage import color
    _coconut_case_match_to_13 = state  #274:     case state:
    _coconut_case_match_check_13 = False  #274:     case state:
    _coconut_match_temp_197 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #274:     case state:
    _coconut_case_match_check_13 = True  #274:     case state:
    if _coconut_case_match_check_13:  #274:     case state:
        _coconut_case_match_check_13 = False  #274:     case state:
        if not _coconut_case_match_check_13:  #274:     case state:
            _coconut_match_set_name_meta = _coconut_sentinel  #274:     case state:
            if (_coconut_match_temp_197) and (_coconut.isinstance(_coconut_case_match_to_13, ImageDef)) and (_coconut.len(_coconut_case_match_to_13) >= 2):  #274:     case state:
                _coconut_match_temp_198 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #274:     case state:
                _coconut_match_set_name_meta = _coconut_case_match_to_13[1]  #274:     case state:
                _coconut_match_temp_205 = _coconut.len(_coconut_case_match_to_13) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_13.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_13, "_coconut_data_defaults", {}) and _coconut_case_match_to_13[i] == _coconut.getattr(_coconut_case_match_to_13, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_13.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_13, "__match_args__") else _coconut.len(_coconut_case_match_to_13) == 2  # type: ignore  #274:     case state:
                if _coconut_match_temp_205:  #274:     case state:
                    _coconut_case_match_check_13 = True  #274:     case state:
            if _coconut_case_match_check_13:  #274:     case state:
                _coconut_case_match_check_13 = False  #274:     case state:
                if not _coconut_case_match_check_13:  #274:     case state:
                    if (_coconut_match_temp_198) and (_coconut.isinstance(_coconut_case_match_to_13[0], Numpy)) and (_coconut.len(_coconut_case_match_to_13[0]) >= 4) and (_coconut_case_match_to_13[0][0] == "float64") and (_coconut_case_match_to_13[0][1] == "HWC") and (_coconut_case_match_to_13[0][2] == "RGBA") and (_coconut_case_match_to_13[0][3] == "0_1"):  #274:     case state:
                        _coconut_match_temp_199 = _coconut.len(_coconut_case_match_to_13[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_13[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_13[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_13[0][i] == _coconut.getattr(_coconut_case_match_to_13[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_13[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_13[0], "__match_args__") else _coconut.len(_coconut_case_match_to_13[0]) == 4  # type: ignore  #274:     case state:
                        if _coconut_match_temp_199:  #274:     case state:
                            _coconut_case_match_check_13 = True  #274:     case state:

                if not _coconut_case_match_check_13:  #274:     case state:
                    if (not _coconut_match_temp_198) and (_coconut.isinstance(_coconut_case_match_to_13[0], Numpy)):  #274:     case state:
                        _coconut_case_match_check_13 = True  #274:     case state:
                    if _coconut_case_match_check_13:  #274:     case state:
                        _coconut_case_match_check_13 = False  #274:     case state:
                        if not _coconut_case_match_check_13:  #274:     case state:
                            if _coconut.type(_coconut_case_match_to_13[0]) in _coconut_self_match_types:  #274:     case state:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #274:     case state:
                                _coconut_case_match_check_13 = True  #274:     case state:

                        if not _coconut_case_match_check_13:  #274:     case state:
                            if not _coconut.type(_coconut_case_match_to_13[0]) in _coconut_self_match_types:  #274:     case state:
                                _coconut_match_temp_200 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #274:     case state:
                                if not _coconut.isinstance(_coconut_match_temp_200, _coconut.tuple):  #274:     case state:
                                    raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #274:     case state:
                                if _coconut.len(_coconut_match_temp_200) < 4:  #274:     case state:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_200),))  #274:     case state:
                                _coconut_match_temp_201 = _coconut.getattr(_coconut_case_match_to_13[0], _coconut_match_temp_200[0], _coconut_sentinel)  #274:     case state:
                                _coconut_match_temp_202 = _coconut.getattr(_coconut_case_match_to_13[0], _coconut_match_temp_200[1], _coconut_sentinel)  #274:     case state:
                                _coconut_match_temp_203 = _coconut.getattr(_coconut_case_match_to_13[0], _coconut_match_temp_200[2], _coconut_sentinel)  #274:     case state:
                                _coconut_match_temp_204 = _coconut.getattr(_coconut_case_match_to_13[0], _coconut_match_temp_200[3], _coconut_sentinel)  #274:     case state:
                                if (_coconut_match_temp_201 is not _coconut_sentinel) and (_coconut_match_temp_201 == "float64") and (_coconut_match_temp_202 is not _coconut_sentinel) and (_coconut_match_temp_202 == "HWC") and (_coconut_match_temp_203 is not _coconut_sentinel) and (_coconut_match_temp_203 == "RGBA") and (_coconut_match_temp_204 is not _coconut_sentinel) and (_coconut_match_temp_204 == "0_1"):  #274:     case state:
                                    _coconut_case_match_check_13 = True  #274:     case state:




            if _coconut_case_match_check_13:  #274:     case state:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #274:     case state:
                    meta = _coconut_match_set_name_meta  #274:     case state:

        if not _coconut_case_match_check_13:  #274:     case state:
            if (not _coconut_match_temp_197) and (_coconut.isinstance(_coconut_case_match_to_13, ImageDef)):  #274:     case state:
                _coconut_case_match_check_13 = True  #274:     case state:
            if _coconut_case_match_check_13:  #274:     case state:
                _coconut_case_match_check_13 = False  #274:     case state:
                if not _coconut_case_match_check_13:  #274:     case state:
                    if _coconut.type(_coconut_case_match_to_13) in _coconut_self_match_types:  #274:     case state:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #274:     case state:
                        _coconut_case_match_check_13 = True  #274:     case state:

                if not _coconut_case_match_check_13:  #274:     case state:
                    _coconut_match_set_name_meta = _coconut_sentinel  #274:     case state:
                    if not _coconut.type(_coconut_case_match_to_13) in _coconut_self_match_types:  #274:     case state:
                        _coconut_match_temp_206 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #274:     case state:
                        if not _coconut.isinstance(_coconut_match_temp_206, _coconut.tuple):  #274:     case state:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #274:     case state:
                        if _coconut.len(_coconut_match_temp_206) < 2:  #274:     case state:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_206),))  #274:     case state:
                        _coconut_match_temp_207 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_206[0], _coconut_sentinel)  #274:     case state:
                        _coconut_match_temp_215 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_206[1], _coconut_sentinel)  #274:     case state:
                        if (_coconut_match_temp_207 is not _coconut_sentinel) and (_coconut_match_temp_215 is not _coconut_sentinel):  #274:     case state:
                            _coconut_match_temp_208 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #274:     case state:
                            _coconut_match_set_name_meta = _coconut_match_temp_215  #274:     case state:
                            _coconut_case_match_check_13 = True  #274:     case state:
                    if _coconut_case_match_check_13:  #274:     case state:
                        _coconut_case_match_check_13 = False  #274:     case state:
                        if not _coconut_case_match_check_13:  #274:     case state:
                            if (_coconut_match_temp_208) and (_coconut.isinstance(_coconut_match_temp_207, Numpy)) and (_coconut.len(_coconut_match_temp_207) >= 4) and (_coconut_match_temp_207[0] == "float64") and (_coconut_match_temp_207[1] == "HWC") and (_coconut_match_temp_207[2] == "RGBA") and (_coconut_match_temp_207[3] == "0_1"):  #274:     case state:
                                _coconut_match_temp_209 = _coconut.len(_coconut_match_temp_207) <= _coconut.max(4, _coconut.len(_coconut_match_temp_207.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_207, "_coconut_data_defaults", {}) and _coconut_match_temp_207[i] == _coconut.getattr(_coconut_match_temp_207, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_207.__match_args__))) if _coconut.hasattr(_coconut_match_temp_207, "__match_args__") else _coconut.len(_coconut_match_temp_207) == 4  # type: ignore  #274:     case state:
                                if _coconut_match_temp_209:  #274:     case state:
                                    _coconut_case_match_check_13 = True  #274:     case state:

                        if not _coconut_case_match_check_13:  #274:     case state:
                            if (not _coconut_match_temp_208) and (_coconut.isinstance(_coconut_match_temp_207, Numpy)):  #274:     case state:
                                _coconut_case_match_check_13 = True  #274:     case state:
                            if _coconut_case_match_check_13:  #274:     case state:
                                _coconut_case_match_check_13 = False  #274:     case state:
                                if not _coconut_case_match_check_13:  #274:     case state:
                                    if _coconut.type(_coconut_match_temp_207) in _coconut_self_match_types:  #274:     case state:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #274:     case state:
                                        _coconut_case_match_check_13 = True  #274:     case state:

                                if not _coconut_case_match_check_13:  #274:     case state:
                                    if not _coconut.type(_coconut_match_temp_207) in _coconut_self_match_types:  #274:     case state:
                                        _coconut_match_temp_210 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #274:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_210, _coconut.tuple):  #274:     case state:
                                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #274:     case state:
                                        if _coconut.len(_coconut_match_temp_210) < 4:  #274:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_210),))  #274:     case state:
                                        _coconut_match_temp_211 = _coconut.getattr(_coconut_match_temp_207, _coconut_match_temp_210[0], _coconut_sentinel)  #274:     case state:
                                        _coconut_match_temp_212 = _coconut.getattr(_coconut_match_temp_207, _coconut_match_temp_210[1], _coconut_sentinel)  #274:     case state:
                                        _coconut_match_temp_213 = _coconut.getattr(_coconut_match_temp_207, _coconut_match_temp_210[2], _coconut_sentinel)  #274:     case state:
                                        _coconut_match_temp_214 = _coconut.getattr(_coconut_match_temp_207, _coconut_match_temp_210[3], _coconut_sentinel)  #274:     case state:
                                        if (_coconut_match_temp_211 is not _coconut_sentinel) and (_coconut_match_temp_211 == "float64") and (_coconut_match_temp_212 is not _coconut_sentinel) and (_coconut_match_temp_212 == "HWC") and (_coconut_match_temp_213 is not _coconut_sentinel) and (_coconut_match_temp_213 == "RGBA") and (_coconut_match_temp_214 is not _coconut_sentinel) and (_coconut_match_temp_214 == "0_1"):  #274:     case state:
                                            _coconut_case_match_check_13 = True  #274:     case state:




                    if _coconut_case_match_check_13:  #274:     case state:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #274:     case state:
                            meta = _coconut_match_set_name_meta  #274:     case state:




    if _coconut_case_match_check_13:  #274:     case state:
        return ([(lambda a: convert_ignore_channel(a, color.rgb2lab), ImageDef(Numpy("float64", "HWC", "LABA", "LABA"), meta), "rgba2laba (ignores alpha)"),])  #276:             return [
    if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
        _coconut_match_temp_216 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
        _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
        if _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
            _coconut_case_match_check_13 = False  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
            if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                if (_coconut_match_temp_216) and (_coconut.isinstance(_coconut_case_match_to_13, ImageDef)) and (_coconut.len(_coconut_case_match_to_13) >= 2):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_match_temp_217 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_13[1]  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_match_temp_224 = _coconut.len(_coconut_case_match_to_13) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_13.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_13, "_coconut_data_defaults", {}) and _coconut_case_match_to_13[i] == _coconut.getattr(_coconut_case_match_to_13, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_13.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_13, "__match_args__") else _coconut.len(_coconut_case_match_to_13) == 2  # type: ignore  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    if _coconut_match_temp_224:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                if _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_case_match_check_13 = False  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if (_coconut_match_temp_217) and (_coconut.isinstance(_coconut_case_match_to_13[0], Numpy)) and (_coconut.len(_coconut_case_match_to_13[0]) >= 4) and (_coconut_case_match_to_13[0][0] == "float64") and (_coconut_case_match_to_13[0][1] == "HWC") and (_coconut_case_match_to_13[0][2] == "LABA") and (_coconut_case_match_to_13[0][3] == "LABA"):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_match_temp_218 = _coconut.len(_coconut_case_match_to_13[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_13[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_13[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_13[0][i] == _coconut.getattr(_coconut_case_match_to_13[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_13[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_13[0], "__match_args__") else _coconut.len(_coconut_case_match_to_13[0]) == 4  # type: ignore  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if _coconut_match_temp_218:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

                    if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if (not _coconut_match_temp_217) and (_coconut.isinstance(_coconut_case_match_to_13[0], Numpy)):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_case_match_check_13 = False  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                if _coconut.type(_coconut_case_match_to_13[0]) in _coconut_self_match_types:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

                            if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                if not _coconut.type(_coconut_case_match_to_13[0]) in _coconut_self_match_types:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_219 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_219, _coconut.tuple):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    if _coconut.len(_coconut_match_temp_219) < 4:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_219),))  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_220 = _coconut.getattr(_coconut_case_match_to_13[0], _coconut_match_temp_219[0], _coconut_sentinel)  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_221 = _coconut.getattr(_coconut_case_match_to_13[0], _coconut_match_temp_219[1], _coconut_sentinel)  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_222 = _coconut.getattr(_coconut_case_match_to_13[0], _coconut_match_temp_219[2], _coconut_sentinel)  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_223 = _coconut.getattr(_coconut_case_match_to_13[0], _coconut_match_temp_219[3], _coconut_sentinel)  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    if (_coconut_match_temp_220 is not _coconut_sentinel) and (_coconut_match_temp_220 == "float64") and (_coconut_match_temp_221 is not _coconut_sentinel) and (_coconut_match_temp_221 == "HWC") and (_coconut_match_temp_222 is not _coconut_sentinel) and (_coconut_match_temp_222 == "LABA") and (_coconut_match_temp_223 is not _coconut_sentinel) and (_coconut_match_temp_223 == "LABA"):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):




                if _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        meta = _coconut_match_set_name_meta  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

            if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                if (not _coconut_match_temp_216) and (_coconut.isinstance(_coconut_case_match_to_13, ImageDef)):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                if _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_case_match_check_13 = False  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if _coconut.type(_coconut_case_match_to_13) in _coconut_self_match_types:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

                    if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if not _coconut.type(_coconut_case_match_to_13) in _coconut_self_match_types:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_match_temp_225 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if not _coconut.isinstance(_coconut_match_temp_225, _coconut.tuple):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if _coconut.len(_coconut_match_temp_225) < 2:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_225),))  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_match_temp_226 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_225[0], _coconut_sentinel)  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_match_temp_234 = _coconut.getattr(_coconut_case_match_to_13, _coconut_match_temp_225[1], _coconut_sentinel)  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if (_coconut_match_temp_226 is not _coconut_sentinel) and (_coconut_match_temp_234 is not _coconut_sentinel):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                _coconut_match_temp_227 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_234  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_case_match_check_13 = False  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                if (_coconut_match_temp_227) and (_coconut.isinstance(_coconut_match_temp_226, Numpy)) and (_coconut.len(_coconut_match_temp_226) >= 4) and (_coconut_match_temp_226[0] == "float64") and (_coconut_match_temp_226[1] == "HWC") and (_coconut_match_temp_226[2] == "LABA") and (_coconut_match_temp_226[3] == "LABA"):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_228 = _coconut.len(_coconut_match_temp_226) <= _coconut.max(4, _coconut.len(_coconut_match_temp_226.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_226, "_coconut_data_defaults", {}) and _coconut_match_temp_226[i] == _coconut.getattr(_coconut_match_temp_226, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_226.__match_args__))) if _coconut.hasattr(_coconut_match_temp_226, "__match_args__") else _coconut.len(_coconut_match_temp_226) == 4  # type: ignore  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    if _coconut_match_temp_228:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

                            if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                if (not _coconut_match_temp_227) and (_coconut.isinstance(_coconut_match_temp_226, Numpy)):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                if _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_case_match_check_13 = False  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        if _coconut.type(_coconut_match_temp_226) in _coconut_self_match_types:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

                                    if not _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        if not _coconut.type(_coconut_match_temp_226) in _coconut_self_match_types:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_match_temp_229 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_229, _coconut.tuple):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            if _coconut.len(_coconut_match_temp_229) < 4:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_229),))  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_match_temp_230 = _coconut.getattr(_coconut_match_temp_226, _coconut_match_temp_229[0], _coconut_sentinel)  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_match_temp_231 = _coconut.getattr(_coconut_match_temp_226, _coconut_match_temp_229[1], _coconut_sentinel)  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_match_temp_232 = _coconut.getattr(_coconut_match_temp_226, _coconut_match_temp_229[2], _coconut_sentinel)  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_match_temp_233 = _coconut.getattr(_coconut_match_temp_226, _coconut_match_temp_229[3], _coconut_sentinel)  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            if (_coconut_match_temp_230 is not _coconut_sentinel) and (_coconut_match_temp_230 == "float64") and (_coconut_match_temp_231 is not _coconut_sentinel) and (_coconut_match_temp_231 == "HWC") and (_coconut_match_temp_232 is not _coconut_sentinel) and (_coconut_match_temp_232 == "LABA") and (_coconut_match_temp_233 is not _coconut_sentinel) and (_coconut_match_temp_233 == "LABA"):  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                                _coconut_case_match_check_13 = True  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):




                        if _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                meta = _coconut_match_set_name_meta  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):




        if _coconut_case_match_check_13:  #279:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
            return ([(lambda a: convert_ignore_channel(a, color.lab2rgb), ImageDef(Numpy("float64", "HWC", "RGBA", "0_1"), meta), "laba2rgba (ignores alpha)"),])  #280:             return [



def rule_lab_value_conversion(state):  #285: def rule_lab_value_conversion(state):
    _coconut_case_match_to_14 = state  #286:     case state:
    _coconut_case_match_check_14 = False  #286:     case state:
    _coconut_match_temp_235 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #286:     case state:
    _coconut_case_match_check_14 = True  #286:     case state:
    if _coconut_case_match_check_14:  #286:     case state:
        _coconut_case_match_check_14 = False  #286:     case state:
        if not _coconut_case_match_check_14:  #286:     case state:
            _coconut_match_set_name_meta = _coconut_sentinel  #286:     case state:
            if (_coconut_match_temp_235) and (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)) and (_coconut.len(_coconut_case_match_to_14) >= 2):  #286:     case state:
                _coconut_match_temp_236 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #286:     case state:
                _coconut_match_set_name_meta = _coconut_case_match_to_14[1]  #286:     case state:
                _coconut_match_temp_243 = _coconut.len(_coconut_case_match_to_14) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_14.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {}) and _coconut_case_match_to_14[i] == _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_14.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_14, "__match_args__") else _coconut.len(_coconut_case_match_to_14) == 2  # type: ignore  #286:     case state:
                if _coconut_match_temp_243:  #286:     case state:
                    _coconut_case_match_check_14 = True  #286:     case state:
            if _coconut_case_match_check_14:  #286:     case state:
                _coconut_case_match_check_14 = False  #286:     case state:
                if not _coconut_case_match_check_14:  #286:     case state:
                    if (_coconut_match_temp_236) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)) and (_coconut.len(_coconut_case_match_to_14[0]) >= 4) and (_coconut_case_match_to_14[0][0] == "float64") and (_coconut_case_match_to_14[0][1] == "HWC") and (_coconut_case_match_to_14[0][2] == "LAB") and (_coconut_case_match_to_14[0][3] == "LAB"):  #286:     case state:
                        _coconut_match_temp_237 = _coconut.len(_coconut_case_match_to_14[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_14[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_14[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_14[0][i] == _coconut.getattr(_coconut_case_match_to_14[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_14[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_14[0], "__match_args__") else _coconut.len(_coconut_case_match_to_14[0]) == 4  # type: ignore  #286:     case state:
                        if _coconut_match_temp_237:  #286:     case state:
                            _coconut_case_match_check_14 = True  #286:     case state:

                if not _coconut_case_match_check_14:  #286:     case state:
                    if (not _coconut_match_temp_236) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)):  #286:     case state:
                        _coconut_case_match_check_14 = True  #286:     case state:
                    if _coconut_case_match_check_14:  #286:     case state:
                        _coconut_case_match_check_14 = False  #286:     case state:
                        if not _coconut_case_match_check_14:  #286:     case state:
                            if _coconut.type(_coconut_case_match_to_14[0]) in _coconut_self_match_types:  #286:     case state:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #286:     case state:
                                _coconut_case_match_check_14 = True  #286:     case state:

                        if not _coconut_case_match_check_14:  #286:     case state:
                            if not _coconut.type(_coconut_case_match_to_14[0]) in _coconut_self_match_types:  #286:     case state:
                                _coconut_match_temp_238 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #286:     case state:
                                if not _coconut.isinstance(_coconut_match_temp_238, _coconut.tuple):  #286:     case state:
                                    raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #286:     case state:
                                if _coconut.len(_coconut_match_temp_238) < 4:  #286:     case state:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_238),))  #286:     case state:
                                _coconut_match_temp_239 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_238[0], _coconut_sentinel)  #286:     case state:
                                _coconut_match_temp_240 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_238[1], _coconut_sentinel)  #286:     case state:
                                _coconut_match_temp_241 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_238[2], _coconut_sentinel)  #286:     case state:
                                _coconut_match_temp_242 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_238[3], _coconut_sentinel)  #286:     case state:
                                if (_coconut_match_temp_239 is not _coconut_sentinel) and (_coconut_match_temp_239 == "float64") and (_coconut_match_temp_240 is not _coconut_sentinel) and (_coconut_match_temp_240 == "HWC") and (_coconut_match_temp_241 is not _coconut_sentinel) and (_coconut_match_temp_241 == "LAB") and (_coconut_match_temp_242 is not _coconut_sentinel) and (_coconut_match_temp_242 == "LAB"):  #286:     case state:
                                    _coconut_case_match_check_14 = True  #286:     case state:




            if _coconut_case_match_check_14:  #286:     case state:
                if _coconut_match_set_name_meta is not _coconut_sentinel:  #286:     case state:
                    meta = _coconut_match_set_name_meta  #286:     case state:

        if not _coconut_case_match_check_14:  #286:     case state:
            if (not _coconut_match_temp_235) and (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)):  #286:     case state:
                _coconut_case_match_check_14 = True  #286:     case state:
            if _coconut_case_match_check_14:  #286:     case state:
                _coconut_case_match_check_14 = False  #286:     case state:
                if not _coconut_case_match_check_14:  #286:     case state:
                    if _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #286:     case state:
                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #286:     case state:
                        _coconut_case_match_check_14 = True  #286:     case state:

                if not _coconut_case_match_check_14:  #286:     case state:
                    _coconut_match_set_name_meta = _coconut_sentinel  #286:     case state:
                    if not _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #286:     case state:
                        _coconut_match_temp_244 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #286:     case state:
                        if not _coconut.isinstance(_coconut_match_temp_244, _coconut.tuple):  #286:     case state:
                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #286:     case state:
                        if _coconut.len(_coconut_match_temp_244) < 2:  #286:     case state:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_244),))  #286:     case state:
                        _coconut_match_temp_245 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_244[0], _coconut_sentinel)  #286:     case state:
                        _coconut_match_temp_253 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_244[1], _coconut_sentinel)  #286:     case state:
                        if (_coconut_match_temp_245 is not _coconut_sentinel) and (_coconut_match_temp_253 is not _coconut_sentinel):  #286:     case state:
                            _coconut_match_temp_246 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #286:     case state:
                            _coconut_match_set_name_meta = _coconut_match_temp_253  #286:     case state:
                            _coconut_case_match_check_14 = True  #286:     case state:
                    if _coconut_case_match_check_14:  #286:     case state:
                        _coconut_case_match_check_14 = False  #286:     case state:
                        if not _coconut_case_match_check_14:  #286:     case state:
                            if (_coconut_match_temp_246) and (_coconut.isinstance(_coconut_match_temp_245, Numpy)) and (_coconut.len(_coconut_match_temp_245) >= 4) and (_coconut_match_temp_245[0] == "float64") and (_coconut_match_temp_245[1] == "HWC") and (_coconut_match_temp_245[2] == "LAB") and (_coconut_match_temp_245[3] == "LAB"):  #286:     case state:
                                _coconut_match_temp_247 = _coconut.len(_coconut_match_temp_245) <= _coconut.max(4, _coconut.len(_coconut_match_temp_245.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_245, "_coconut_data_defaults", {}) and _coconut_match_temp_245[i] == _coconut.getattr(_coconut_match_temp_245, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_245.__match_args__))) if _coconut.hasattr(_coconut_match_temp_245, "__match_args__") else _coconut.len(_coconut_match_temp_245) == 4  # type: ignore  #286:     case state:
                                if _coconut_match_temp_247:  #286:     case state:
                                    _coconut_case_match_check_14 = True  #286:     case state:

                        if not _coconut_case_match_check_14:  #286:     case state:
                            if (not _coconut_match_temp_246) and (_coconut.isinstance(_coconut_match_temp_245, Numpy)):  #286:     case state:
                                _coconut_case_match_check_14 = True  #286:     case state:
                            if _coconut_case_match_check_14:  #286:     case state:
                                _coconut_case_match_check_14 = False  #286:     case state:
                                if not _coconut_case_match_check_14:  #286:     case state:
                                    if _coconut.type(_coconut_match_temp_245) in _coconut_self_match_types:  #286:     case state:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #286:     case state:
                                        _coconut_case_match_check_14 = True  #286:     case state:

                                if not _coconut_case_match_check_14:  #286:     case state:
                                    if not _coconut.type(_coconut_match_temp_245) in _coconut_self_match_types:  #286:     case state:
                                        _coconut_match_temp_248 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #286:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_248, _coconut.tuple):  #286:     case state:
                                            raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #286:     case state:
                                        if _coconut.len(_coconut_match_temp_248) < 4:  #286:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_248),))  #286:     case state:
                                        _coconut_match_temp_249 = _coconut.getattr(_coconut_match_temp_245, _coconut_match_temp_248[0], _coconut_sentinel)  #286:     case state:
                                        _coconut_match_temp_250 = _coconut.getattr(_coconut_match_temp_245, _coconut_match_temp_248[1], _coconut_sentinel)  #286:     case state:
                                        _coconut_match_temp_251 = _coconut.getattr(_coconut_match_temp_245, _coconut_match_temp_248[2], _coconut_sentinel)  #286:     case state:
                                        _coconut_match_temp_252 = _coconut.getattr(_coconut_match_temp_245, _coconut_match_temp_248[3], _coconut_sentinel)  #286:     case state:
                                        if (_coconut_match_temp_249 is not _coconut_sentinel) and (_coconut_match_temp_249 == "float64") and (_coconut_match_temp_250 is not _coconut_sentinel) and (_coconut_match_temp_250 == "HWC") and (_coconut_match_temp_251 is not _coconut_sentinel) and (_coconut_match_temp_251 == "LAB") and (_coconut_match_temp_252 is not _coconut_sentinel) and (_coconut_match_temp_252 == "LAB"):  #286:     case state:
                                            _coconut_case_match_check_14 = True  #286:     case state:




                    if _coconut_case_match_check_14:  #286:     case state:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #286:     case state:
                            meta = _coconut_match_set_name_meta  #286:     case state:




    if _coconut_case_match_check_14:  #286:     case state:
        return ([((_vr_lab_to_0_1, ImageDef(Numpy("float64", "HWC", "LAB", "0_1"), meta), "vr_lab_to_0_1")),])  #288:             return [((_vr_lab_to_0_1,ImageDef(Numpy("float64","HWC","LAB","0_1"),meta),"vr_lab_to_0_1"))]
    if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
        _coconut_match_temp_254 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
        _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
        if _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
            _coconut_case_match_check_14 = False  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
            if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                if (_coconut_match_temp_254) and (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)) and (_coconut.len(_coconut_case_match_to_14) >= 2):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_match_temp_255 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_14[1]  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_match_temp_262 = _coconut.len(_coconut_case_match_to_14) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_14.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {}) and _coconut_case_match_to_14[i] == _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_14.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_14, "__match_args__") else _coconut.len(_coconut_case_match_to_14) == 2  # type: ignore  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    if _coconut_match_temp_262:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                if _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_case_match_check_14 = False  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if (_coconut_match_temp_255) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)) and (_coconut.len(_coconut_case_match_to_14[0]) >= 4) and (_coconut_case_match_to_14[0][0] == "float64") and (_coconut_case_match_to_14[0][1] == "HWC") and (_coconut_case_match_to_14[0][2] == "LABA") and (_coconut_case_match_to_14[0][3] == "LABA"):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_match_temp_256 = _coconut.len(_coconut_case_match_to_14[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_14[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_14[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_14[0][i] == _coconut.getattr(_coconut_case_match_to_14[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_14[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_14[0], "__match_args__") else _coconut.len(_coconut_case_match_to_14[0]) == 4  # type: ignore  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if _coconut_match_temp_256:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

                    if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if (not _coconut_match_temp_255) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_case_match_check_14 = False  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                if _coconut.type(_coconut_case_match_to_14[0]) in _coconut_self_match_types:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

                            if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                if not _coconut.type(_coconut_case_match_to_14[0]) in _coconut_self_match_types:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_257 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_257, _coconut.tuple):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    if _coconut.len(_coconut_match_temp_257) < 4:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_257),))  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_258 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_257[0], _coconut_sentinel)  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_259 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_257[1], _coconut_sentinel)  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_260 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_257[2], _coconut_sentinel)  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_261 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_257[3], _coconut_sentinel)  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    if (_coconut_match_temp_258 is not _coconut_sentinel) and (_coconut_match_temp_258 == "float64") and (_coconut_match_temp_259 is not _coconut_sentinel) and (_coconut_match_temp_259 == "HWC") and (_coconut_match_temp_260 is not _coconut_sentinel) and (_coconut_match_temp_260 == "LABA") and (_coconut_match_temp_261 is not _coconut_sentinel) and (_coconut_match_temp_261 == "LABA"):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):




                if _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        meta = _coconut_match_set_name_meta  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

            if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                if (not _coconut_match_temp_254) and (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                if _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    _coconut_case_match_check_14 = False  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                    if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

                    if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if not _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_match_temp_263 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if not _coconut.isinstance(_coconut_match_temp_263, _coconut.tuple):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if _coconut.len(_coconut_match_temp_263) < 2:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_263),))  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_match_temp_264 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_263[0], _coconut_sentinel)  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_match_temp_272 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_263[1], _coconut_sentinel)  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if (_coconut_match_temp_264 is not _coconut_sentinel) and (_coconut_match_temp_272 is not _coconut_sentinel):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                _coconut_match_temp_265 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_272  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                        if _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            _coconut_case_match_check_14 = False  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                if (_coconut_match_temp_265) and (_coconut.isinstance(_coconut_match_temp_264, Numpy)) and (_coconut.len(_coconut_match_temp_264) >= 4) and (_coconut_match_temp_264[0] == "float64") and (_coconut_match_temp_264[1] == "HWC") and (_coconut_match_temp_264[2] == "LABA") and (_coconut_match_temp_264[3] == "LABA"):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_match_temp_266 = _coconut.len(_coconut_match_temp_264) <= _coconut.max(4, _coconut.len(_coconut_match_temp_264.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_264, "_coconut_data_defaults", {}) and _coconut_match_temp_264[i] == _coconut.getattr(_coconut_match_temp_264, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_264.__match_args__))) if _coconut.hasattr(_coconut_match_temp_264, "__match_args__") else _coconut.len(_coconut_match_temp_264) == 4  # type: ignore  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    if _coconut_match_temp_266:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

                            if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                if (not _coconut_match_temp_265) and (_coconut.isinstance(_coconut_match_temp_264, Numpy)):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                if _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    _coconut_case_match_check_14 = False  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                    if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        if _coconut.type(_coconut_match_temp_264) in _coconut_self_match_types:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):

                                    if not _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                        if not _coconut.type(_coconut_match_temp_264) in _coconut_self_match_types:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_match_temp_267 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_267, _coconut.tuple):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            if _coconut.len(_coconut_match_temp_267) < 4:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_267),))  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_match_temp_268 = _coconut.getattr(_coconut_match_temp_264, _coconut_match_temp_267[0], _coconut_sentinel)  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_match_temp_269 = _coconut.getattr(_coconut_match_temp_264, _coconut_match_temp_267[1], _coconut_sentinel)  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_match_temp_270 = _coconut.getattr(_coconut_match_temp_264, _coconut_match_temp_267[2], _coconut_sentinel)  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            _coconut_match_temp_271 = _coconut.getattr(_coconut_match_temp_264, _coconut_match_temp_267[3], _coconut_sentinel)  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                            if (_coconut_match_temp_268 is not _coconut_sentinel) and (_coconut_match_temp_268 == "float64") and (_coconut_match_temp_269 is not _coconut_sentinel) and (_coconut_match_temp_269 == "HWC") and (_coconut_match_temp_270 is not _coconut_sentinel) and (_coconut_match_temp_270 == "LABA") and (_coconut_match_temp_271 is not _coconut_sentinel) and (_coconut_match_temp_271 == "LABA"):  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                                _coconut_case_match_check_14 = True  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):




                        if _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
                                meta = _coconut_match_set_name_meta  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):




        if _coconut_case_match_check_14:  #289:         match ImageDef(Numpy("float64","HWC","LABA","LABA"),meta):
            return ([((lambda a: convert_ignore_channel(a, _vr_lab_to_0_1), ImageDef(Numpy("float64", "HWC", "LABA", "0_1"), meta), "vr_laba_to_0_1")),])  #290:             return [((a->convert_ignore_channel(a,_vr_lab_to_0_1),ImageDef(Numpy("float64","HWC","LABA","0_1"),meta),"vr_laba_to_0_1"))]
    if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
        _coconut_match_temp_273 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
        _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
        if _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
            _coconut_case_match_check_14 = False  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
            if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                if (_coconut_match_temp_273) and (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)) and (_coconut.len(_coconut_case_match_to_14) >= 2):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                    _coconut_match_temp_274 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_14[1]  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                    _coconut_match_temp_281 = _coconut.len(_coconut_case_match_to_14) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_14.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {}) and _coconut_case_match_to_14[i] == _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_14.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_14, "__match_args__") else _coconut.len(_coconut_case_match_to_14) == 2  # type: ignore  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                    if _coconut_match_temp_281:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                        _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                if _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                    _coconut_case_match_check_14 = False  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                    if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                        if (_coconut_match_temp_274) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)) and (_coconut.len(_coconut_case_match_to_14[0]) >= 4) and (_coconut_case_match_to_14[0][0] == "float64") and (_coconut_case_match_to_14[0][1] == "HWC") and (_coconut_case_match_to_14[0][2] == "LAB") and (_coconut_case_match_to_14[0][3] == "0_1"):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            _coconut_match_temp_275 = _coconut.len(_coconut_case_match_to_14[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_14[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_14[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_14[0][i] == _coconut.getattr(_coconut_case_match_to_14[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_14[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_14[0], "__match_args__") else _coconut.len(_coconut_case_match_to_14[0]) == 4  # type: ignore  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            if _coconut_match_temp_275:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):

                    if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                        if (not _coconut_match_temp_274) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                        if _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            _coconut_case_match_check_14 = False  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                if _coconut.type(_coconut_case_match_to_14[0]) in _coconut_self_match_types:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):

                            if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                if not _coconut.type(_coconut_case_match_to_14[0]) in _coconut_self_match_types:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    _coconut_match_temp_276 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_276, _coconut.tuple):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    if _coconut.len(_coconut_match_temp_276) < 4:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_276),))  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    _coconut_match_temp_277 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_276[0], _coconut_sentinel)  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    _coconut_match_temp_278 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_276[1], _coconut_sentinel)  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    _coconut_match_temp_279 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_276[2], _coconut_sentinel)  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    _coconut_match_temp_280 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_276[3], _coconut_sentinel)  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    if (_coconut_match_temp_277 is not _coconut_sentinel) and (_coconut_match_temp_277 == "float64") and (_coconut_match_temp_278 is not _coconut_sentinel) and (_coconut_match_temp_278 == "HWC") and (_coconut_match_temp_279 is not _coconut_sentinel) and (_coconut_match_temp_279 == "LAB") and (_coconut_match_temp_280 is not _coconut_sentinel) and (_coconut_match_temp_280 == "0_1"):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                        _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):




                if _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                        meta = _coconut_match_set_name_meta  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):

            if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                if (not _coconut_match_temp_273) and (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                    _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                if _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                    _coconut_case_match_check_14 = False  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                    if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                        if _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):

                    if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                        if not _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            _coconut_match_temp_282 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            if not _coconut.isinstance(_coconut_match_temp_282, _coconut.tuple):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            if _coconut.len(_coconut_match_temp_282) < 2:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_282),))  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            _coconut_match_temp_283 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_282[0], _coconut_sentinel)  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            _coconut_match_temp_291 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_282[1], _coconut_sentinel)  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            if (_coconut_match_temp_283 is not _coconut_sentinel) and (_coconut_match_temp_291 is not _coconut_sentinel):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                _coconut_match_temp_284 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_291  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                        if _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            _coconut_case_match_check_14 = False  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                if (_coconut_match_temp_284) and (_coconut.isinstance(_coconut_match_temp_283, Numpy)) and (_coconut.len(_coconut_match_temp_283) >= 4) and (_coconut_match_temp_283[0] == "float64") and (_coconut_match_temp_283[1] == "HWC") and (_coconut_match_temp_283[2] == "LAB") and (_coconut_match_temp_283[3] == "0_1"):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    _coconut_match_temp_285 = _coconut.len(_coconut_match_temp_283) <= _coconut.max(4, _coconut.len(_coconut_match_temp_283.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_283, "_coconut_data_defaults", {}) and _coconut_match_temp_283[i] == _coconut.getattr(_coconut_match_temp_283, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_283.__match_args__))) if _coconut.hasattr(_coconut_match_temp_283, "__match_args__") else _coconut.len(_coconut_match_temp_283) == 4  # type: ignore  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    if _coconut_match_temp_285:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                        _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):

                            if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                if (not _coconut_match_temp_284) and (_coconut.isinstance(_coconut_match_temp_283, Numpy)):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                if _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    _coconut_case_match_check_14 = False  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                    if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                        if _coconut.type(_coconut_match_temp_283) in _coconut_self_match_types:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                            _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):

                                    if not _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                        if not _coconut.type(_coconut_match_temp_283) in _coconut_self_match_types:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                            _coconut_match_temp_286 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_286, _coconut.tuple):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                            if _coconut.len(_coconut_match_temp_286) < 4:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_286),))  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                            _coconut_match_temp_287 = _coconut.getattr(_coconut_match_temp_283, _coconut_match_temp_286[0], _coconut_sentinel)  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                            _coconut_match_temp_288 = _coconut.getattr(_coconut_match_temp_283, _coconut_match_temp_286[1], _coconut_sentinel)  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                            _coconut_match_temp_289 = _coconut.getattr(_coconut_match_temp_283, _coconut_match_temp_286[2], _coconut_sentinel)  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                            _coconut_match_temp_290 = _coconut.getattr(_coconut_match_temp_283, _coconut_match_temp_286[3], _coconut_sentinel)  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                            if (_coconut_match_temp_287 is not _coconut_sentinel) and (_coconut_match_temp_287 == "float64") and (_coconut_match_temp_288 is not _coconut_sentinel) and (_coconut_match_temp_288 == "HWC") and (_coconut_match_temp_289 is not _coconut_sentinel) and (_coconut_match_temp_289 == "LAB") and (_coconut_match_temp_290 is not _coconut_sentinel) and (_coconut_match_temp_290 == "0_1"):  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                                _coconut_case_match_check_14 = True  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):




                        if _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
                                meta = _coconut_match_set_name_meta  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):




        if _coconut_case_match_check_14:  #291:         match ImageDef(Numpy("float64","HWC","LAB","0_1"),meta):
            return ([((_0_1_to_vr_lab, ImageDef(Numpy("float64", "HWC", "LAB", "LAB"), meta), "0_1_to_vr_lab")),])  #292:             return [((_0_1_to_vr_lab,ImageDef(Numpy("float64","HWC","LAB","LAB"),meta),"0_1_to_vr_lab"))]
    if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
        _coconut_match_temp_292 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
        _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
        if _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
            _coconut_case_match_check_14 = False  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
            if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                if (_coconut_match_temp_292) and (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)) and (_coconut.len(_coconut_case_match_to_14) >= 2):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                    _coconut_match_temp_293 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_14[1]  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                    _coconut_match_temp_300 = _coconut.len(_coconut_case_match_to_14) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_14.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {}) and _coconut_case_match_to_14[i] == _coconut.getattr(_coconut_case_match_to_14, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_14.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_14, "__match_args__") else _coconut.len(_coconut_case_match_to_14) == 2  # type: ignore  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                    if _coconut_match_temp_300:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                        _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                if _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                    _coconut_case_match_check_14 = False  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                    if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                        if (_coconut_match_temp_293) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)) and (_coconut.len(_coconut_case_match_to_14[0]) >= 4) and (_coconut_case_match_to_14[0][0] == "float64") and (_coconut_case_match_to_14[0][1] == "HWC") and (_coconut_case_match_to_14[0][2] == "LABA") and (_coconut_case_match_to_14[0][3] == "0_1"):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            _coconut_match_temp_294 = _coconut.len(_coconut_case_match_to_14[0]) <= _coconut.max(4, _coconut.len(_coconut_case_match_to_14[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_14[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_14[0][i] == _coconut.getattr(_coconut_case_match_to_14[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_case_match_to_14[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_14[0], "__match_args__") else _coconut.len(_coconut_case_match_to_14[0]) == 4  # type: ignore  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            if _coconut_match_temp_294:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):

                    if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                        if (not _coconut_match_temp_293) and (_coconut.isinstance(_coconut_case_match_to_14[0], Numpy)):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                        if _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            _coconut_case_match_check_14 = False  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                if _coconut.type(_coconut_case_match_to_14[0]) in _coconut_self_match_types:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):

                            if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                if not _coconut.type(_coconut_case_match_to_14[0]) in _coconut_self_match_types:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    _coconut_match_temp_295 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_295, _coconut.tuple):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                        raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    if _coconut.len(_coconut_match_temp_295) < 4:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_295),))  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    _coconut_match_temp_296 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_295[0], _coconut_sentinel)  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    _coconut_match_temp_297 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_295[1], _coconut_sentinel)  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    _coconut_match_temp_298 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_295[2], _coconut_sentinel)  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    _coconut_match_temp_299 = _coconut.getattr(_coconut_case_match_to_14[0], _coconut_match_temp_295[3], _coconut_sentinel)  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    if (_coconut_match_temp_296 is not _coconut_sentinel) and (_coconut_match_temp_296 == "float64") and (_coconut_match_temp_297 is not _coconut_sentinel) and (_coconut_match_temp_297 == "HWC") and (_coconut_match_temp_298 is not _coconut_sentinel) and (_coconut_match_temp_298 == "LABA") and (_coconut_match_temp_299 is not _coconut_sentinel) and (_coconut_match_temp_299 == "0_1"):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                        _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):




                if _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                        meta = _coconut_match_set_name_meta  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):

            if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                if (not _coconut_match_temp_292) and (_coconut.isinstance(_coconut_case_match_to_14, ImageDef)):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                    _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                if _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                    _coconut_case_match_check_14 = False  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                    if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                        if _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):

                    if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                        if not _coconut.type(_coconut_case_match_to_14) in _coconut_self_match_types:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            _coconut_match_temp_301 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            if not _coconut.isinstance(_coconut_match_temp_301, _coconut.tuple):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            if _coconut.len(_coconut_match_temp_301) < 2:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_301),))  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            _coconut_match_temp_302 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_301[0], _coconut_sentinel)  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            _coconut_match_temp_310 = _coconut.getattr(_coconut_case_match_to_14, _coconut_match_temp_301[1], _coconut_sentinel)  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            if (_coconut_match_temp_302 is not _coconut_sentinel) and (_coconut_match_temp_310 is not _coconut_sentinel):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                _coconut_match_temp_303 = _coconut.getattr(Numpy, "_coconut_is_data", False) or _coconut.isinstance(Numpy, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Numpy)  # type: ignore  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_310  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                        if _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            _coconut_case_match_check_14 = False  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                if (_coconut_match_temp_303) and (_coconut.isinstance(_coconut_match_temp_302, Numpy)) and (_coconut.len(_coconut_match_temp_302) >= 4) and (_coconut_match_temp_302[0] == "float64") and (_coconut_match_temp_302[1] == "HWC") and (_coconut_match_temp_302[2] == "LABA") and (_coconut_match_temp_302[3] == "0_1"):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    _coconut_match_temp_304 = _coconut.len(_coconut_match_temp_302) <= _coconut.max(4, _coconut.len(_coconut_match_temp_302.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_302, "_coconut_data_defaults", {}) and _coconut_match_temp_302[i] == _coconut.getattr(_coconut_match_temp_302, "_coconut_data_defaults", {})[i] for i in _coconut.range(4, _coconut.len(_coconut_match_temp_302.__match_args__))) if _coconut.hasattr(_coconut_match_temp_302, "__match_args__") else _coconut.len(_coconut_match_temp_302) == 4  # type: ignore  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    if _coconut_match_temp_304:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                        _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):

                            if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                if (not _coconut_match_temp_303) and (_coconut.isinstance(_coconut_match_temp_302, Numpy)):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                if _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    _coconut_case_match_check_14 = False  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                    if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                        if _coconut.type(_coconut_match_temp_302) in _coconut_self_match_types:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports 1)")  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                            _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):

                                    if not _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                        if not _coconut.type(_coconut_match_temp_302) in _coconut_self_match_types:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                            _coconut_match_temp_305 = _coconut.getattr(Numpy, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_305, _coconut.tuple):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                                raise _coconut.TypeError("Numpy.__match_args__ must be a tuple")  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                            if _coconut.len(_coconut_match_temp_305) < 4:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 4; 'Numpy' only supports %s)" % (_coconut.len(_coconut_match_temp_305),))  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                            _coconut_match_temp_306 = _coconut.getattr(_coconut_match_temp_302, _coconut_match_temp_305[0], _coconut_sentinel)  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                            _coconut_match_temp_307 = _coconut.getattr(_coconut_match_temp_302, _coconut_match_temp_305[1], _coconut_sentinel)  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                            _coconut_match_temp_308 = _coconut.getattr(_coconut_match_temp_302, _coconut_match_temp_305[2], _coconut_sentinel)  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                            _coconut_match_temp_309 = _coconut.getattr(_coconut_match_temp_302, _coconut_match_temp_305[3], _coconut_sentinel)  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                            if (_coconut_match_temp_306 is not _coconut_sentinel) and (_coconut_match_temp_306 == "float64") and (_coconut_match_temp_307 is not _coconut_sentinel) and (_coconut_match_temp_307 == "HWC") and (_coconut_match_temp_308 is not _coconut_sentinel) and (_coconut_match_temp_308 == "LABA") and (_coconut_match_temp_309 is not _coconut_sentinel) and (_coconut_match_temp_309 == "0_1"):  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                                _coconut_case_match_check_14 = True  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):




                        if _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
                                meta = _coconut_match_set_name_meta  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):




        if _coconut_case_match_check_14:  #293:         match ImageDef(Numpy("float64","HWC","LABA","0_1"),meta):
            return ([((lambda a: convert_ignore_channel(a, _0_1_to_vr_lab), ImageDef(Numpy("float64", "HWC", "LABA", "LABA"), meta), "vr_0_1_to_laba")),])  #294:             return [((a->convert_ignore_channel(a,_0_1_to_vr_lab),ImageDef(Numpy("float64","HWC","LABA","LABA"),meta),"vr_0_1_to_laba"))]


def _vr_lab_to_0_1(ary):  #296: def _vr_lab_to_0_1(ary):
    r = ary.copy()  #297:     r = ary.copy()
    r[:, :, 0] = ary[:, :, 0] * 0.01  #298:     r[:,:,0] = ary[:,:,0] * 0.01
    r[:, :, 1] = (ary[:, :, 1] + 128.0) / 255.0  #299:     r[:,:,1] = (ary[:,:,1] + 128.0) / 255.0
    r[:, :, 2] = (ary[:, :, 2] + 128.0) / 255.0  #300:     r[:,:,2] = (ary[:,:,2] + 128.0) / 255.0
    return (r)  #301:     return r


def _0_1_to_vr_lab(ary):  #303: def _0_1_to_vr_lab(ary):
    r = ary.copy()  #304:     r = ary.copy()
    r[:, :, 0] = ary[:, :, 0] * 100  #305:     r[:,:,0] = ary[:,:,0] * 100
    r[:, :, 1] = (ary[:, :, 1] * 255) - 128.0  #306:     r[:,:,1] = (ary[:,:,1] * 255) - 128.0
    r[:, :, 2] = (ary[:, :, 2] * 255) - 128.0  #307:     r[:,:,2] = (ary[:,:,2] * 255) - 128.0
    return (r)  #308:     return r


class AutoTuple(_coconut.collections.namedtuple("AutoTuple", ('formats',))):  #310: data AutoTuple(formats is tuple)
    __slots__ = ()  #310: data AutoTuple(formats is tuple)
    _coconut_is_data = True  #310: data AutoTuple(formats is tuple)
    __match_args__ = ('formats',)  #310: data AutoTuple(formats is tuple)
    def __add__(self, other): return _coconut.NotImplemented  #310: data AutoTuple(formats is tuple)
    def __mul__(self, other): return _coconut.NotImplemented  #310: data AutoTuple(formats is tuple)
    def __rmul__(self, other): return _coconut.NotImplemented  #310: data AutoTuple(formats is tuple)
    __ne__ = _coconut.object.__ne__  #310: data AutoTuple(formats is tuple)
    def __eq__(self, other):  #310: data AutoTuple(formats is tuple)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #310: data AutoTuple(formats is tuple)
    def __hash__(self):  #310: data AutoTuple(formats is tuple)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #310: data AutoTuple(formats is tuple)
    def __new__(_coconut_cls, _coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #310: data AutoTuple(formats is tuple)
        _coconut_match_check_0 = False  #310: data AutoTuple(formats is tuple)
        _coconut_match_set_name_formats = _coconut_sentinel  #310: data AutoTuple(formats is tuple)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #310: data AutoTuple(formats is tuple)
        if _coconut_match_first_arg is not _coconut_sentinel:  #310: data AutoTuple(formats is tuple)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #310: data AutoTuple(formats is tuple)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "formats" in _coconut_match_kwargs)) == 1):  #310: data AutoTuple(formats is tuple)
            _coconut_match_temp_311 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("formats")  #310: data AutoTuple(formats is tuple)
            if _coconut.isinstance(_coconut_match_temp_311, tuple):  #310: data AutoTuple(formats is tuple)
                _coconut_match_set_name_formats = _coconut_match_temp_311  #310: data AutoTuple(formats is tuple)
                if not _coconut_match_kwargs:  #310: data AutoTuple(formats is tuple)
                    _coconut_match_check_0 = True  #310: data AutoTuple(formats is tuple)
        if _coconut_match_check_0:  #310: data AutoTuple(formats is tuple)
            if _coconut_match_set_name_formats is not _coconut_sentinel:  #310: data AutoTuple(formats is tuple)
                formats = _coconut_match_set_name_formats  #310: data AutoTuple(formats is tuple)

        if not _coconut_match_check_0:  #310: data AutoTuple(formats is tuple)
            raise _coconut_FunctionMatchError('data AutoTuple(formats is tuple)', _coconut_match_args)  #310: data AutoTuple(formats is tuple)

        return _coconut.tuple.__new__(_coconut_cls, (formats,))  #310: data AutoTuple(formats is tuple)



_coconut_call_set_names(AutoTuple)  #313: def isnamedtuple(x):
def isnamedtuple(x):  #313: def isnamedtuple(x):
    t = type(x)  #314:     t = type(x)
    b = t.__bases__  #315:     b = t.__bases__
    if hasattr(x, "__slots__"):  #316:     if hasattr(x,"__slots__"): return True
        return (True)  #316:     if hasattr(x,"__slots__"): return True
    if len(b) != 1 or b[0] != tuple:  #317:     if len(b) != 1 or b[0] != tuple: return False
        return (False)  #317:     if len(b) != 1 or b[0] != tuple: return False
    f = getattr(t, '_fields', None)  #318:     f = getattr(t, '_fields', None)
    if not isinstance(f, tuple):  #319:     if not isinstance(f, tuple): return False
        return (False)  #319:     if not isinstance(f, tuple): return False
    return (all((type(n) == str for n in f)))  #320:     return all(type(n)==str for n in f)


def cast_tuple2auto_tuple(state):  #322: def cast_tuple2auto_tuple(state):
    if isinstance(state, str):  #323:     if isinstance(state,str):
        return (None)  #324:         return None
    if isinstance(state, AutoTuple):  #325:     if isinstance(state,AutoTuple):
        res = [state.formats,]  #326:         res = [state.formats]
        return (res)  #327:         return res
    elif type(state) == tuple:  #328:     elif type(state) == tuple:
        res = [AutoTuple(state),]  #329:         res = [AutoTuple(state)]
        return (res)  #330:         return res


def map_tuple_i(t, i, f):  #332: def map_tuple_i(t,i,f):
    res = list(t)  #333:     res = list(t)
    res[i] = f(res[i])  #334:     res[i] = f(res[i])
    return (tuple(res))  #335:     return tuple(res)


def map_state(states, i, new_state):  #337: def map_state(states,i,new_state):
    res = list(states)  #338:     res = list(states)
    res[i] = new_state  #339:     res[i] = new_state
    return (tuple(res))  #340:     return tuple(res)



def map_each(t, mappers):  #343: def map_each(t,mappers):
#logger.warning(f"items:{t}")
#logger.warning(f"mappers:{mappers}")
    return (tuple([f(item) for f, item in zip(mappers, t)]))  #346:     return tuple([f(item) for f,item in zip(mappers,t)])



class AutoList(_coconut.collections.namedtuple("AutoList", ('state',))):  #349: data AutoList(state):
    __slots__ = ()  #349: data AutoList(state):
    _coconut_is_data = True  #349: data AutoList(state):
    __match_args__ = ('state',)  #349: data AutoList(state):
    def __add__(self, other): return _coconut.NotImplemented  #349: data AutoList(state):
    def __mul__(self, other): return _coconut.NotImplemented  #349: data AutoList(state):
    def __rmul__(self, other): return _coconut.NotImplemented  #349: data AutoList(state):
    __ne__ = _coconut.object.__ne__  #349: data AutoList(state):
    def __eq__(self, other):  #349: data AutoList(state):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #349: data AutoList(state):
    def __hash__(self):  #349: data AutoList(state):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #349: data AutoList(state):
    def __repr__(self):  #350:     def __repr__(self):
        return ("[{_coconut_format_0}]".format(_coconut_format_0=(self.state)))  #351:         return f"[{self.state}]"




_coconut_call_set_names(AutoList)  #355: def cast_ary_str_to_ary_type(state):
def cast_ary_str_to_ary_type(state):  #355: def cast_ary_str_to_ary_type(state):
    _coconut_case_match_to_15 = state  #356:     case state:
    _coconut_case_match_check_15 = False  #356:     case state:
    _coconut_match_set_name_element_state = _coconut_sentinel  #356:     case state:
    if (_coconut.isinstance(_coconut_case_match_to_15, _coconut.str)) and (_coconut.len(_coconut_case_match_to_15) >= 2) and (_coconut_case_match_to_15.startswith("[")) and (_coconut_case_match_to_15.endswith("]")):  #356:     case state:
        _coconut_match_temp_312 = _coconut_case_match_to_15[1:-1]  #356:     case state:
        _coconut_match_set_name_element_state = _coconut_match_temp_312  #356:     case state:
        _coconut_case_match_check_15 = True  #356:     case state:
    if _coconut_case_match_check_15:  #356:     case state:
        if _coconut_match_set_name_element_state is not _coconut_sentinel:  #356:     case state:
            element_state = _coconut_match_set_name_element_state  #356:     case state:
    if _coconut_case_match_check_15:  #356:     case state:
        return ([AutoList(element_state),])  #358:             return [AutoList(element_state)]
    if not _coconut_case_match_check_15:  #359:         match AutoList(es is str):
        _coconut_match_temp_313 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #359:         match AutoList(es is str):
        _coconut_case_match_check_15 = True  #359:         match AutoList(es is str):
        if _coconut_case_match_check_15:  #359:         match AutoList(es is str):
            _coconut_case_match_check_15 = False  #359:         match AutoList(es is str):
            if not _coconut_case_match_check_15:  #359:         match AutoList(es is str):
                _coconut_match_set_name_es = _coconut_sentinel  #359:         match AutoList(es is str):
                if (_coconut_match_temp_313) and (_coconut.isinstance(_coconut_case_match_to_15, AutoList)) and (_coconut.len(_coconut_case_match_to_15) >= 1) and (_coconut.isinstance(_coconut_case_match_to_15[0], str)):  #359:         match AutoList(es is str):
                    _coconut_match_set_name_es = _coconut_case_match_to_15[0]  #359:         match AutoList(es is str):
                    _coconut_match_temp_314 = _coconut.len(_coconut_case_match_to_15) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_15.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_15, "_coconut_data_defaults", {}) and _coconut_case_match_to_15[i] == _coconut.getattr(_coconut_case_match_to_15, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_15.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_15, "__match_args__") else _coconut.len(_coconut_case_match_to_15) == 1  # type: ignore  #359:         match AutoList(es is str):
                    if _coconut_match_temp_314:  #359:         match AutoList(es is str):
                        _coconut_case_match_check_15 = True  #359:         match AutoList(es is str):
                if _coconut_case_match_check_15:  #359:         match AutoList(es is str):
                    if _coconut_match_set_name_es is not _coconut_sentinel:  #359:         match AutoList(es is str):
                        es = _coconut_match_set_name_es  #359:         match AutoList(es is str):

            if not _coconut_case_match_check_15:  #359:         match AutoList(es is str):
                if (not _coconut_match_temp_313) and (_coconut.isinstance(_coconut_case_match_to_15, AutoList)):  #359:         match AutoList(es is str):
                    _coconut_case_match_check_15 = True  #359:         match AutoList(es is str):
                if _coconut_case_match_check_15:  #359:         match AutoList(es is str):
                    _coconut_case_match_check_15 = False  #359:         match AutoList(es is str):
                    if not _coconut_case_match_check_15:  #359:         match AutoList(es is str):
                        _coconut_match_set_name_es = _coconut_sentinel  #359:         match AutoList(es is str):
                        if (_coconut.type(_coconut_case_match_to_15) in _coconut_self_match_types) and (_coconut.isinstance(_coconut_case_match_to_15, str)):  #359:         match AutoList(es is str):
                            _coconut_match_set_name_es = _coconut_case_match_to_15  #359:         match AutoList(es is str):
                            _coconut_case_match_check_15 = True  #359:         match AutoList(es is str):
                        if _coconut_case_match_check_15:  #359:         match AutoList(es is str):
                            if _coconut_match_set_name_es is not _coconut_sentinel:  #359:         match AutoList(es is str):
                                es = _coconut_match_set_name_es  #359:         match AutoList(es is str):

                    if not _coconut_case_match_check_15:  #359:         match AutoList(es is str):
                        _coconut_match_set_name_es = _coconut_sentinel  #359:         match AutoList(es is str):
                        if not _coconut.type(_coconut_case_match_to_15) in _coconut_self_match_types:  #359:         match AutoList(es is str):
                            _coconut_match_temp_315 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #359:         match AutoList(es is str):
                            if not _coconut.isinstance(_coconut_match_temp_315, _coconut.tuple):  #359:         match AutoList(es is str):
                                raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #359:         match AutoList(es is str):
                            if _coconut.len(_coconut_match_temp_315) < 1:  #359:         match AutoList(es is str):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_315),))  #359:         match AutoList(es is str):
                            _coconut_match_temp_316 = _coconut.getattr(_coconut_case_match_to_15, _coconut_match_temp_315[0], _coconut_sentinel)  #359:         match AutoList(es is str):
                            if (_coconut_match_temp_316 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_316, str)):  #359:         match AutoList(es is str):
                                _coconut_match_set_name_es = _coconut_match_temp_316  #359:         match AutoList(es is str):
                                _coconut_case_match_check_15 = True  #359:         match AutoList(es is str):
                        if _coconut_case_match_check_15:  #359:         match AutoList(es is str):
                            if _coconut_match_set_name_es is not _coconut_sentinel:  #359:         match AutoList(es is str):
                                es = _coconut_match_set_name_es  #359:         match AutoList(es is str):




        if _coconut_case_match_check_15:  #359:         match AutoList(es is str):
            return (["[{_coconut_format_0}]".format(_coconut_format_0=(es)),])  #360:             return [f"[{es}]"]

#shape change!

ms_add_None_b_ch = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: (None, *s)))  #363: ms_add_None_b_ch = (s->(None,*s)) |> ss_to_ms$
"adds 1 as batch shape"  #364: "adds 1 as batch shape"
ms_del_b_ch = (_coconut_partial(_coconut_partial, ss_to_ms))((lambda s: s[1:]))  #365: ms_del_b_ch = (s->s[1:])  |> ss_to_ms$
# TODO preserve length in AutoList
def img_list_is_imgs(state):  #367: def img_list_is_imgs(state):
    _coconut_case_match_to_16 = state  #368:     case state:
    _coconut_case_match_check_16 = False  #368:     case state:
    _coconut_match_temp_317 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #368:     case state:
    _coconut_case_match_check_16 = True  #368:     case state:
    if _coconut_case_match_check_16:  #368:     case state:
        _coconut_case_match_check_16 = False  #368:     case state:
        if not _coconut_case_match_check_16:  #368:     case state:
            if (_coconut_match_temp_317) and (_coconut.isinstance(_coconut_case_match_to_16, AutoList)) and (_coconut.len(_coconut_case_match_to_16) >= 1):  #368:     case state:
                _coconut_match_temp_318 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #368:     case state:
                _coconut_match_temp_333 = _coconut.len(_coconut_case_match_to_16) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_16.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {}) and _coconut_case_match_to_16[i] == _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_16.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16, "__match_args__") else _coconut.len(_coconut_case_match_to_16) == 1  # type: ignore  #368:     case state:
                if _coconut_match_temp_333:  #368:     case state:
                    _coconut_case_match_check_16 = True  #368:     case state:
            if _coconut_case_match_check_16:  #368:     case state:
                _coconut_case_match_check_16 = False  #368:     case state:
                if not _coconut_case_match_check_16:  #368:     case state:
                    _coconut_match_set_name_meta = _coconut_sentinel  #368:     case state:
                    if (_coconut_match_temp_318) and (_coconut.isinstance(_coconut_case_match_to_16[0], ImageDef)) and (_coconut.len(_coconut_case_match_to_16[0]) >= 2):  #368:     case state:
                        _coconut_match_temp_319 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #368:     case state:
                        _coconut_match_set_name_meta = _coconut_case_match_to_16[0][1]  #368:     case state:
                        _coconut_match_temp_324 = _coconut.len(_coconut_case_match_to_16[0]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_16[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_16[0][i] == _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_16[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16[0], "__match_args__") else _coconut.len(_coconut_case_match_to_16[0]) == 2  # type: ignore  #368:     case state:
                        if _coconut_match_temp_324:  #368:     case state:
                            _coconut_case_match_check_16 = True  #368:     case state:
                    if _coconut_case_match_check_16:  #368:     case state:
                        _coconut_case_match_check_16 = False  #368:     case state:
                        if not _coconut_case_match_check_16:  #368:     case state:
                            _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                            _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                            if (_coconut_match_temp_319) and (_coconut.isinstance(_coconut_case_match_to_16[0][0], PILImage)) and (_coconut.len(_coconut_case_match_to_16[0][0]) >= 2):  #368:     case state:
                                _coconut_match_set_name_m1 = _coconut_case_match_to_16[0][0][0]  #368:     case state:
                                _coconut_match_set_name_m2 = _coconut_case_match_to_16[0][0][1]  #368:     case state:
                                _coconut_match_temp_320 = _coconut.len(_coconut_case_match_to_16[0][0]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_16[0][0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16[0][0], "_coconut_data_defaults", {}) and _coconut_case_match_to_16[0][0][i] == _coconut.getattr(_coconut_case_match_to_16[0][0], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_16[0][0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16[0][0], "__match_args__") else _coconut.len(_coconut_case_match_to_16[0][0]) == 2  # type: ignore  #368:     case state:
                                if _coconut_match_temp_320:  #368:     case state:
                                    _coconut_case_match_check_16 = True  #368:     case state:
                            if _coconut_case_match_check_16:  #368:     case state:
                                if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                    m1 = _coconut_match_set_name_m1  #368:     case state:
                                if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                    m2 = _coconut_match_set_name_m2  #368:     case state:

                        if not _coconut_case_match_check_16:  #368:     case state:
                            if (not _coconut_match_temp_319) and (_coconut.isinstance(_coconut_case_match_to_16[0][0], PILImage)):  #368:     case state:
                                _coconut_case_match_check_16 = True  #368:     case state:
                            if _coconut_case_match_check_16:  #368:     case state:
                                _coconut_case_match_check_16 = False  #368:     case state:
                                if not _coconut_case_match_check_16:  #368:     case state:
                                    if _coconut.type(_coconut_case_match_to_16[0][0]) in _coconut_self_match_types:  #368:     case state:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #368:     case state:
                                        _coconut_case_match_check_16 = True  #368:     case state:

                                if not _coconut_case_match_check_16:  #368:     case state:
                                    _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                                    _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                                    if not _coconut.type(_coconut_case_match_to_16[0][0]) in _coconut_self_match_types:  #368:     case state:
                                        _coconut_match_temp_321 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #368:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_321, _coconut.tuple):  #368:     case state:
                                            raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #368:     case state:
                                        if _coconut.len(_coconut_match_temp_321) < 2:  #368:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_321),))  #368:     case state:
                                        _coconut_match_temp_322 = _coconut.getattr(_coconut_case_match_to_16[0][0], _coconut_match_temp_321[0], _coconut_sentinel)  #368:     case state:
                                        _coconut_match_temp_323 = _coconut.getattr(_coconut_case_match_to_16[0][0], _coconut_match_temp_321[1], _coconut_sentinel)  #368:     case state:
                                        if (_coconut_match_temp_322 is not _coconut_sentinel) and (_coconut_match_temp_323 is not _coconut_sentinel):  #368:     case state:
                                            _coconut_match_set_name_m1 = _coconut_match_temp_322  #368:     case state:
                                            _coconut_match_set_name_m2 = _coconut_match_temp_323  #368:     case state:
                                            _coconut_case_match_check_16 = True  #368:     case state:
                                    if _coconut_case_match_check_16:  #368:     case state:
                                        if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                            m1 = _coconut_match_set_name_m1  #368:     case state:
                                        if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                            m2 = _coconut_match_set_name_m2  #368:     case state:




                    if _coconut_case_match_check_16:  #368:     case state:
                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #368:     case state:
                            meta = _coconut_match_set_name_meta  #368:     case state:

                if not _coconut_case_match_check_16:  #368:     case state:
                    if (not _coconut_match_temp_318) and (_coconut.isinstance(_coconut_case_match_to_16[0], ImageDef)):  #368:     case state:
                        _coconut_case_match_check_16 = True  #368:     case state:
                    if _coconut_case_match_check_16:  #368:     case state:
                        _coconut_case_match_check_16 = False  #368:     case state:
                        if not _coconut_case_match_check_16:  #368:     case state:
                            if _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #368:     case state:
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #368:     case state:
                                _coconut_case_match_check_16 = True  #368:     case state:

                        if not _coconut_case_match_check_16:  #368:     case state:
                            _coconut_match_set_name_meta = _coconut_sentinel  #368:     case state:
                            if not _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #368:     case state:
                                _coconut_match_temp_325 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #368:     case state:
                                if not _coconut.isinstance(_coconut_match_temp_325, _coconut.tuple):  #368:     case state:
                                    raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #368:     case state:
                                if _coconut.len(_coconut_match_temp_325) < 2:  #368:     case state:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_325),))  #368:     case state:
                                _coconut_match_temp_326 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_325[0], _coconut_sentinel)  #368:     case state:
                                _coconut_match_temp_332 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_325[1], _coconut_sentinel)  #368:     case state:
                                if (_coconut_match_temp_326 is not _coconut_sentinel) and (_coconut_match_temp_332 is not _coconut_sentinel):  #368:     case state:
                                    _coconut_match_temp_327 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #368:     case state:
                                    _coconut_match_set_name_meta = _coconut_match_temp_332  #368:     case state:
                                    _coconut_case_match_check_16 = True  #368:     case state:
                            if _coconut_case_match_check_16:  #368:     case state:
                                _coconut_case_match_check_16 = False  #368:     case state:
                                if not _coconut_case_match_check_16:  #368:     case state:
                                    _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                                    _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                                    if (_coconut_match_temp_327) and (_coconut.isinstance(_coconut_match_temp_326, PILImage)) and (_coconut.len(_coconut_match_temp_326) >= 2):  #368:     case state:
                                        _coconut_match_set_name_m1 = _coconut_match_temp_326[0]  #368:     case state:
                                        _coconut_match_set_name_m2 = _coconut_match_temp_326[1]  #368:     case state:
                                        _coconut_match_temp_328 = _coconut.len(_coconut_match_temp_326) <= _coconut.max(2, _coconut.len(_coconut_match_temp_326.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_326, "_coconut_data_defaults", {}) and _coconut_match_temp_326[i] == _coconut.getattr(_coconut_match_temp_326, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_match_temp_326.__match_args__))) if _coconut.hasattr(_coconut_match_temp_326, "__match_args__") else _coconut.len(_coconut_match_temp_326) == 2  # type: ignore  #368:     case state:
                                        if _coconut_match_temp_328:  #368:     case state:
                                            _coconut_case_match_check_16 = True  #368:     case state:
                                    if _coconut_case_match_check_16:  #368:     case state:
                                        if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                            m1 = _coconut_match_set_name_m1  #368:     case state:
                                        if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                            m2 = _coconut_match_set_name_m2  #368:     case state:

                                if not _coconut_case_match_check_16:  #368:     case state:
                                    if (not _coconut_match_temp_327) and (_coconut.isinstance(_coconut_match_temp_326, PILImage)):  #368:     case state:
                                        _coconut_case_match_check_16 = True  #368:     case state:
                                    if _coconut_case_match_check_16:  #368:     case state:
                                        _coconut_case_match_check_16 = False  #368:     case state:
                                        if not _coconut_case_match_check_16:  #368:     case state:
                                            if _coconut.type(_coconut_match_temp_326) in _coconut_self_match_types:  #368:     case state:
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #368:     case state:
                                                _coconut_case_match_check_16 = True  #368:     case state:

                                        if not _coconut_case_match_check_16:  #368:     case state:
                                            _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                                            _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                                            if not _coconut.type(_coconut_match_temp_326) in _coconut_self_match_types:  #368:     case state:
                                                _coconut_match_temp_329 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #368:     case state:
                                                if not _coconut.isinstance(_coconut_match_temp_329, _coconut.tuple):  #368:     case state:
                                                    raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #368:     case state:
                                                if _coconut.len(_coconut_match_temp_329) < 2:  #368:     case state:
                                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_329),))  #368:     case state:
                                                _coconut_match_temp_330 = _coconut.getattr(_coconut_match_temp_326, _coconut_match_temp_329[0], _coconut_sentinel)  #368:     case state:
                                                _coconut_match_temp_331 = _coconut.getattr(_coconut_match_temp_326, _coconut_match_temp_329[1], _coconut_sentinel)  #368:     case state:
                                                if (_coconut_match_temp_330 is not _coconut_sentinel) and (_coconut_match_temp_331 is not _coconut_sentinel):  #368:     case state:
                                                    _coconut_match_set_name_m1 = _coconut_match_temp_330  #368:     case state:
                                                    _coconut_match_set_name_m2 = _coconut_match_temp_331  #368:     case state:
                                                    _coconut_case_match_check_16 = True  #368:     case state:
                                            if _coconut_case_match_check_16:  #368:     case state:
                                                if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                                    m1 = _coconut_match_set_name_m1  #368:     case state:
                                                if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                                    m2 = _coconut_match_set_name_m2  #368:     case state:




                            if _coconut_case_match_check_16:  #368:     case state:
                                if _coconut_match_set_name_meta is not _coconut_sentinel:  #368:     case state:
                                    meta = _coconut_match_set_name_meta  #368:     case state:





        if not _coconut_case_match_check_16:  #368:     case state:
            if (not _coconut_match_temp_317) and (_coconut.isinstance(_coconut_case_match_to_16, AutoList)):  #368:     case state:
                _coconut_case_match_check_16 = True  #368:     case state:
            if _coconut_case_match_check_16:  #368:     case state:
                _coconut_case_match_check_16 = False  #368:     case state:
                if not _coconut_case_match_check_16:  #368:     case state:
                    if _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #368:     case state:
                        _coconut_match_temp_334 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #368:     case state:
                        _coconut_case_match_check_16 = True  #368:     case state:
                    if _coconut_case_match_check_16:  #368:     case state:
                        _coconut_case_match_check_16 = False  #368:     case state:
                        if not _coconut_case_match_check_16:  #368:     case state:
                            _coconut_match_set_name_meta = _coconut_sentinel  #368:     case state:
                            if (_coconut_match_temp_334) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)) and (_coconut.len(_coconut_case_match_to_16) >= 2):  #368:     case state:
                                _coconut_match_temp_335 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #368:     case state:
                                _coconut_match_set_name_meta = _coconut_case_match_to_16[1]  #368:     case state:
                                _coconut_match_temp_340 = _coconut.len(_coconut_case_match_to_16) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_16.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {}) and _coconut_case_match_to_16[i] == _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_16.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16, "__match_args__") else _coconut.len(_coconut_case_match_to_16) == 2  # type: ignore  #368:     case state:
                                if _coconut_match_temp_340:  #368:     case state:
                                    _coconut_case_match_check_16 = True  #368:     case state:
                            if _coconut_case_match_check_16:  #368:     case state:
                                _coconut_case_match_check_16 = False  #368:     case state:
                                if not _coconut_case_match_check_16:  #368:     case state:
                                    _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                                    _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                                    if (_coconut_match_temp_335) and (_coconut.isinstance(_coconut_case_match_to_16[0], PILImage)) and (_coconut.len(_coconut_case_match_to_16[0]) >= 2):  #368:     case state:
                                        _coconut_match_set_name_m1 = _coconut_case_match_to_16[0][0]  #368:     case state:
                                        _coconut_match_set_name_m2 = _coconut_case_match_to_16[0][1]  #368:     case state:
                                        _coconut_match_temp_336 = _coconut.len(_coconut_case_match_to_16[0]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_16[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_16[0][i] == _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_16[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16[0], "__match_args__") else _coconut.len(_coconut_case_match_to_16[0]) == 2  # type: ignore  #368:     case state:
                                        if _coconut_match_temp_336:  #368:     case state:
                                            _coconut_case_match_check_16 = True  #368:     case state:
                                    if _coconut_case_match_check_16:  #368:     case state:
                                        if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                            m1 = _coconut_match_set_name_m1  #368:     case state:
                                        if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                            m2 = _coconut_match_set_name_m2  #368:     case state:

                                if not _coconut_case_match_check_16:  #368:     case state:
                                    if (not _coconut_match_temp_335) and (_coconut.isinstance(_coconut_case_match_to_16[0], PILImage)):  #368:     case state:
                                        _coconut_case_match_check_16 = True  #368:     case state:
                                    if _coconut_case_match_check_16:  #368:     case state:
                                        _coconut_case_match_check_16 = False  #368:     case state:
                                        if not _coconut_case_match_check_16:  #368:     case state:
                                            if _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #368:     case state:
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #368:     case state:
                                                _coconut_case_match_check_16 = True  #368:     case state:

                                        if not _coconut_case_match_check_16:  #368:     case state:
                                            _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                                            _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                                            if not _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #368:     case state:
                                                _coconut_match_temp_337 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #368:     case state:
                                                if not _coconut.isinstance(_coconut_match_temp_337, _coconut.tuple):  #368:     case state:
                                                    raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #368:     case state:
                                                if _coconut.len(_coconut_match_temp_337) < 2:  #368:     case state:
                                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_337),))  #368:     case state:
                                                _coconut_match_temp_338 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_337[0], _coconut_sentinel)  #368:     case state:
                                                _coconut_match_temp_339 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_337[1], _coconut_sentinel)  #368:     case state:
                                                if (_coconut_match_temp_338 is not _coconut_sentinel) and (_coconut_match_temp_339 is not _coconut_sentinel):  #368:     case state:
                                                    _coconut_match_set_name_m1 = _coconut_match_temp_338  #368:     case state:
                                                    _coconut_match_set_name_m2 = _coconut_match_temp_339  #368:     case state:
                                                    _coconut_case_match_check_16 = True  #368:     case state:
                                            if _coconut_case_match_check_16:  #368:     case state:
                                                if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                                    m1 = _coconut_match_set_name_m1  #368:     case state:
                                                if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                                    m2 = _coconut_match_set_name_m2  #368:     case state:




                            if _coconut_case_match_check_16:  #368:     case state:
                                if _coconut_match_set_name_meta is not _coconut_sentinel:  #368:     case state:
                                    meta = _coconut_match_set_name_meta  #368:     case state:

                        if not _coconut_case_match_check_16:  #368:     case state:
                            if (not _coconut_match_temp_334) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)):  #368:     case state:
                                _coconut_case_match_check_16 = True  #368:     case state:
                            if _coconut_case_match_check_16:  #368:     case state:
                                _coconut_case_match_check_16 = False  #368:     case state:
                                if not _coconut_case_match_check_16:  #368:     case state:
                                    if _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #368:     case state:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #368:     case state:
                                        _coconut_case_match_check_16 = True  #368:     case state:

                                if not _coconut_case_match_check_16:  #368:     case state:
                                    _coconut_match_set_name_meta = _coconut_sentinel  #368:     case state:
                                    if not _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #368:     case state:
                                        _coconut_match_temp_341 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #368:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_341, _coconut.tuple):  #368:     case state:
                                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #368:     case state:
                                        if _coconut.len(_coconut_match_temp_341) < 2:  #368:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_341),))  #368:     case state:
                                        _coconut_match_temp_342 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_341[0], _coconut_sentinel)  #368:     case state:
                                        _coconut_match_temp_348 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_341[1], _coconut_sentinel)  #368:     case state:
                                        if (_coconut_match_temp_342 is not _coconut_sentinel) and (_coconut_match_temp_348 is not _coconut_sentinel):  #368:     case state:
                                            _coconut_match_temp_343 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #368:     case state:
                                            _coconut_match_set_name_meta = _coconut_match_temp_348  #368:     case state:
                                            _coconut_case_match_check_16 = True  #368:     case state:
                                    if _coconut_case_match_check_16:  #368:     case state:
                                        _coconut_case_match_check_16 = False  #368:     case state:
                                        if not _coconut_case_match_check_16:  #368:     case state:
                                            _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                                            _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                                            if (_coconut_match_temp_343) and (_coconut.isinstance(_coconut_match_temp_342, PILImage)) and (_coconut.len(_coconut_match_temp_342) >= 2):  #368:     case state:
                                                _coconut_match_set_name_m1 = _coconut_match_temp_342[0]  #368:     case state:
                                                _coconut_match_set_name_m2 = _coconut_match_temp_342[1]  #368:     case state:
                                                _coconut_match_temp_344 = _coconut.len(_coconut_match_temp_342) <= _coconut.max(2, _coconut.len(_coconut_match_temp_342.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_342, "_coconut_data_defaults", {}) and _coconut_match_temp_342[i] == _coconut.getattr(_coconut_match_temp_342, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_match_temp_342.__match_args__))) if _coconut.hasattr(_coconut_match_temp_342, "__match_args__") else _coconut.len(_coconut_match_temp_342) == 2  # type: ignore  #368:     case state:
                                                if _coconut_match_temp_344:  #368:     case state:
                                                    _coconut_case_match_check_16 = True  #368:     case state:
                                            if _coconut_case_match_check_16:  #368:     case state:
                                                if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                                    m1 = _coconut_match_set_name_m1  #368:     case state:
                                                if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                                    m2 = _coconut_match_set_name_m2  #368:     case state:

                                        if not _coconut_case_match_check_16:  #368:     case state:
                                            if (not _coconut_match_temp_343) and (_coconut.isinstance(_coconut_match_temp_342, PILImage)):  #368:     case state:
                                                _coconut_case_match_check_16 = True  #368:     case state:
                                            if _coconut_case_match_check_16:  #368:     case state:
                                                _coconut_case_match_check_16 = False  #368:     case state:
                                                if not _coconut_case_match_check_16:  #368:     case state:
                                                    if _coconut.type(_coconut_match_temp_342) in _coconut_self_match_types:  #368:     case state:
                                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #368:     case state:
                                                        _coconut_case_match_check_16 = True  #368:     case state:

                                                if not _coconut_case_match_check_16:  #368:     case state:
                                                    _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                                                    _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                                                    if not _coconut.type(_coconut_match_temp_342) in _coconut_self_match_types:  #368:     case state:
                                                        _coconut_match_temp_345 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #368:     case state:
                                                        if not _coconut.isinstance(_coconut_match_temp_345, _coconut.tuple):  #368:     case state:
                                                            raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #368:     case state:
                                                        if _coconut.len(_coconut_match_temp_345) < 2:  #368:     case state:
                                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_345),))  #368:     case state:
                                                        _coconut_match_temp_346 = _coconut.getattr(_coconut_match_temp_342, _coconut_match_temp_345[0], _coconut_sentinel)  #368:     case state:
                                                        _coconut_match_temp_347 = _coconut.getattr(_coconut_match_temp_342, _coconut_match_temp_345[1], _coconut_sentinel)  #368:     case state:
                                                        if (_coconut_match_temp_346 is not _coconut_sentinel) and (_coconut_match_temp_347 is not _coconut_sentinel):  #368:     case state:
                                                            _coconut_match_set_name_m1 = _coconut_match_temp_346  #368:     case state:
                                                            _coconut_match_set_name_m2 = _coconut_match_temp_347  #368:     case state:
                                                            _coconut_case_match_check_16 = True  #368:     case state:
                                                    if _coconut_case_match_check_16:  #368:     case state:
                                                        if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                                            m1 = _coconut_match_set_name_m1  #368:     case state:
                                                        if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                                            m2 = _coconut_match_set_name_m2  #368:     case state:




                                    if _coconut_case_match_check_16:  #368:     case state:
                                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #368:     case state:
                                            meta = _coconut_match_set_name_meta  #368:     case state:





                if not _coconut_case_match_check_16:  #368:     case state:
                    if not _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #368:     case state:
                        _coconut_match_temp_349 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #368:     case state:
                        if not _coconut.isinstance(_coconut_match_temp_349, _coconut.tuple):  #368:     case state:
                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #368:     case state:
                        if _coconut.len(_coconut_match_temp_349) < 1:  #368:     case state:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_349),))  #368:     case state:
                        _coconut_match_temp_350 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_349[0], _coconut_sentinel)  #368:     case state:
                        if _coconut_match_temp_350 is not _coconut_sentinel:  #368:     case state:
                            _coconut_match_temp_351 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #368:     case state:
                            _coconut_case_match_check_16 = True  #368:     case state:
                    if _coconut_case_match_check_16:  #368:     case state:
                        _coconut_case_match_check_16 = False  #368:     case state:
                        if not _coconut_case_match_check_16:  #368:     case state:
                            _coconut_match_set_name_meta = _coconut_sentinel  #368:     case state:
                            if (_coconut_match_temp_351) and (_coconut.isinstance(_coconut_match_temp_350, ImageDef)) and (_coconut.len(_coconut_match_temp_350) >= 2):  #368:     case state:
                                _coconut_match_temp_352 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #368:     case state:
                                _coconut_match_set_name_meta = _coconut_match_temp_350[1]  #368:     case state:
                                _coconut_match_temp_357 = _coconut.len(_coconut_match_temp_350) <= _coconut.max(2, _coconut.len(_coconut_match_temp_350.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_350, "_coconut_data_defaults", {}) and _coconut_match_temp_350[i] == _coconut.getattr(_coconut_match_temp_350, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_match_temp_350.__match_args__))) if _coconut.hasattr(_coconut_match_temp_350, "__match_args__") else _coconut.len(_coconut_match_temp_350) == 2  # type: ignore  #368:     case state:
                                if _coconut_match_temp_357:  #368:     case state:
                                    _coconut_case_match_check_16 = True  #368:     case state:
                            if _coconut_case_match_check_16:  #368:     case state:
                                _coconut_case_match_check_16 = False  #368:     case state:
                                if not _coconut_case_match_check_16:  #368:     case state:
                                    _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                                    _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                                    if (_coconut_match_temp_352) and (_coconut.isinstance(_coconut_match_temp_350[0], PILImage)) and (_coconut.len(_coconut_match_temp_350[0]) >= 2):  #368:     case state:
                                        _coconut_match_set_name_m1 = _coconut_match_temp_350[0][0]  #368:     case state:
                                        _coconut_match_set_name_m2 = _coconut_match_temp_350[0][1]  #368:     case state:
                                        _coconut_match_temp_353 = _coconut.len(_coconut_match_temp_350[0]) <= _coconut.max(2, _coconut.len(_coconut_match_temp_350[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_350[0], "_coconut_data_defaults", {}) and _coconut_match_temp_350[0][i] == _coconut.getattr(_coconut_match_temp_350[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_match_temp_350[0].__match_args__))) if _coconut.hasattr(_coconut_match_temp_350[0], "__match_args__") else _coconut.len(_coconut_match_temp_350[0]) == 2  # type: ignore  #368:     case state:
                                        if _coconut_match_temp_353:  #368:     case state:
                                            _coconut_case_match_check_16 = True  #368:     case state:
                                    if _coconut_case_match_check_16:  #368:     case state:
                                        if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                            m1 = _coconut_match_set_name_m1  #368:     case state:
                                        if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                            m2 = _coconut_match_set_name_m2  #368:     case state:

                                if not _coconut_case_match_check_16:  #368:     case state:
                                    if (not _coconut_match_temp_352) and (_coconut.isinstance(_coconut_match_temp_350[0], PILImage)):  #368:     case state:
                                        _coconut_case_match_check_16 = True  #368:     case state:
                                    if _coconut_case_match_check_16:  #368:     case state:
                                        _coconut_case_match_check_16 = False  #368:     case state:
                                        if not _coconut_case_match_check_16:  #368:     case state:
                                            if _coconut.type(_coconut_match_temp_350[0]) in _coconut_self_match_types:  #368:     case state:
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #368:     case state:
                                                _coconut_case_match_check_16 = True  #368:     case state:

                                        if not _coconut_case_match_check_16:  #368:     case state:
                                            _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                                            _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                                            if not _coconut.type(_coconut_match_temp_350[0]) in _coconut_self_match_types:  #368:     case state:
                                                _coconut_match_temp_354 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #368:     case state:
                                                if not _coconut.isinstance(_coconut_match_temp_354, _coconut.tuple):  #368:     case state:
                                                    raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #368:     case state:
                                                if _coconut.len(_coconut_match_temp_354) < 2:  #368:     case state:
                                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_354),))  #368:     case state:
                                                _coconut_match_temp_355 = _coconut.getattr(_coconut_match_temp_350[0], _coconut_match_temp_354[0], _coconut_sentinel)  #368:     case state:
                                                _coconut_match_temp_356 = _coconut.getattr(_coconut_match_temp_350[0], _coconut_match_temp_354[1], _coconut_sentinel)  #368:     case state:
                                                if (_coconut_match_temp_355 is not _coconut_sentinel) and (_coconut_match_temp_356 is not _coconut_sentinel):  #368:     case state:
                                                    _coconut_match_set_name_m1 = _coconut_match_temp_355  #368:     case state:
                                                    _coconut_match_set_name_m2 = _coconut_match_temp_356  #368:     case state:
                                                    _coconut_case_match_check_16 = True  #368:     case state:
                                            if _coconut_case_match_check_16:  #368:     case state:
                                                if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                                    m1 = _coconut_match_set_name_m1  #368:     case state:
                                                if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                                    m2 = _coconut_match_set_name_m2  #368:     case state:




                            if _coconut_case_match_check_16:  #368:     case state:
                                if _coconut_match_set_name_meta is not _coconut_sentinel:  #368:     case state:
                                    meta = _coconut_match_set_name_meta  #368:     case state:

                        if not _coconut_case_match_check_16:  #368:     case state:
                            if (not _coconut_match_temp_351) and (_coconut.isinstance(_coconut_match_temp_350, ImageDef)):  #368:     case state:
                                _coconut_case_match_check_16 = True  #368:     case state:
                            if _coconut_case_match_check_16:  #368:     case state:
                                _coconut_case_match_check_16 = False  #368:     case state:
                                if not _coconut_case_match_check_16:  #368:     case state:
                                    if _coconut.type(_coconut_match_temp_350) in _coconut_self_match_types:  #368:     case state:
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #368:     case state:
                                        _coconut_case_match_check_16 = True  #368:     case state:

                                if not _coconut_case_match_check_16:  #368:     case state:
                                    _coconut_match_set_name_meta = _coconut_sentinel  #368:     case state:
                                    if not _coconut.type(_coconut_match_temp_350) in _coconut_self_match_types:  #368:     case state:
                                        _coconut_match_temp_358 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #368:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_358, _coconut.tuple):  #368:     case state:
                                            raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #368:     case state:
                                        if _coconut.len(_coconut_match_temp_358) < 2:  #368:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_358),))  #368:     case state:
                                        _coconut_match_temp_359 = _coconut.getattr(_coconut_match_temp_350, _coconut_match_temp_358[0], _coconut_sentinel)  #368:     case state:
                                        _coconut_match_temp_365 = _coconut.getattr(_coconut_match_temp_350, _coconut_match_temp_358[1], _coconut_sentinel)  #368:     case state:
                                        if (_coconut_match_temp_359 is not _coconut_sentinel) and (_coconut_match_temp_365 is not _coconut_sentinel):  #368:     case state:
                                            _coconut_match_temp_360 = _coconut.getattr(PILImage, "_coconut_is_data", False) or _coconut.isinstance(PILImage, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImage)  # type: ignore  #368:     case state:
                                            _coconut_match_set_name_meta = _coconut_match_temp_365  #368:     case state:
                                            _coconut_case_match_check_16 = True  #368:     case state:
                                    if _coconut_case_match_check_16:  #368:     case state:
                                        _coconut_case_match_check_16 = False  #368:     case state:
                                        if not _coconut_case_match_check_16:  #368:     case state:
                                            _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                                            _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                                            if (_coconut_match_temp_360) and (_coconut.isinstance(_coconut_match_temp_359, PILImage)) and (_coconut.len(_coconut_match_temp_359) >= 2):  #368:     case state:
                                                _coconut_match_set_name_m1 = _coconut_match_temp_359[0]  #368:     case state:
                                                _coconut_match_set_name_m2 = _coconut_match_temp_359[1]  #368:     case state:
                                                _coconut_match_temp_361 = _coconut.len(_coconut_match_temp_359) <= _coconut.max(2, _coconut.len(_coconut_match_temp_359.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_359, "_coconut_data_defaults", {}) and _coconut_match_temp_359[i] == _coconut.getattr(_coconut_match_temp_359, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_match_temp_359.__match_args__))) if _coconut.hasattr(_coconut_match_temp_359, "__match_args__") else _coconut.len(_coconut_match_temp_359) == 2  # type: ignore  #368:     case state:
                                                if _coconut_match_temp_361:  #368:     case state:
                                                    _coconut_case_match_check_16 = True  #368:     case state:
                                            if _coconut_case_match_check_16:  #368:     case state:
                                                if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                                    m1 = _coconut_match_set_name_m1  #368:     case state:
                                                if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                                    m2 = _coconut_match_set_name_m2  #368:     case state:

                                        if not _coconut_case_match_check_16:  #368:     case state:
                                            if (not _coconut_match_temp_360) and (_coconut.isinstance(_coconut_match_temp_359, PILImage)):  #368:     case state:
                                                _coconut_case_match_check_16 = True  #368:     case state:
                                            if _coconut_case_match_check_16:  #368:     case state:
                                                _coconut_case_match_check_16 = False  #368:     case state:
                                                if not _coconut_case_match_check_16:  #368:     case state:
                                                    if _coconut.type(_coconut_match_temp_359) in _coconut_self_match_types:  #368:     case state:
                                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports 1)")  #368:     case state:
                                                        _coconut_case_match_check_16 = True  #368:     case state:

                                                if not _coconut_case_match_check_16:  #368:     case state:
                                                    _coconut_match_set_name_m1 = _coconut_sentinel  #368:     case state:
                                                    _coconut_match_set_name_m2 = _coconut_sentinel  #368:     case state:
                                                    if not _coconut.type(_coconut_match_temp_359) in _coconut_self_match_types:  #368:     case state:
                                                        _coconut_match_temp_362 = _coconut.getattr(PILImage, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #368:     case state:
                                                        if not _coconut.isinstance(_coconut_match_temp_362, _coconut.tuple):  #368:     case state:
                                                            raise _coconut.TypeError("PILImage.__match_args__ must be a tuple")  #368:     case state:
                                                        if _coconut.len(_coconut_match_temp_362) < 2:  #368:     case state:
                                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImage' only supports %s)" % (_coconut.len(_coconut_match_temp_362),))  #368:     case state:
                                                        _coconut_match_temp_363 = _coconut.getattr(_coconut_match_temp_359, _coconut_match_temp_362[0], _coconut_sentinel)  #368:     case state:
                                                        _coconut_match_temp_364 = _coconut.getattr(_coconut_match_temp_359, _coconut_match_temp_362[1], _coconut_sentinel)  #368:     case state:
                                                        if (_coconut_match_temp_363 is not _coconut_sentinel) and (_coconut_match_temp_364 is not _coconut_sentinel):  #368:     case state:
                                                            _coconut_match_set_name_m1 = _coconut_match_temp_363  #368:     case state:
                                                            _coconut_match_set_name_m2 = _coconut_match_temp_364  #368:     case state:
                                                            _coconut_case_match_check_16 = True  #368:     case state:
                                                    if _coconut_case_match_check_16:  #368:     case state:
                                                        if _coconut_match_set_name_m1 is not _coconut_sentinel:  #368:     case state:
                                                            m1 = _coconut_match_set_name_m1  #368:     case state:
                                                        if _coconut_match_set_name_m2 is not _coconut_sentinel:  #368:     case state:
                                                            m2 = _coconut_match_set_name_m2  #368:     case state:




                                    if _coconut_case_match_check_16:  #368:     case state:
                                        if _coconut_match_set_name_meta is not _coconut_sentinel:  #368:     case state:
                                            meta = _coconut_match_set_name_meta  #368:     case state:








    if _coconut_case_match_check_16:  #368:     case state:
        return ([ImageDef(PILImages(m1, m2), (ms_add_None_b_ch)(meta)),])  #370:             return [ImageDef(PILImages(m1,m2),meta |> ms_add_None_b_ch)]
    if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
        _coconut_match_temp_366 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #371:         match ImageDef(PILImages(m1,m2),meta):
        _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):
        if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
            _coconut_case_match_check_16 = False  #371:         match ImageDef(PILImages(m1,m2),meta):
            if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                _coconut_match_set_name_meta = _coconut_sentinel  #371:         match ImageDef(PILImages(m1,m2),meta):
                if (_coconut_match_temp_366) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)) and (_coconut.len(_coconut_case_match_to_16) >= 2):  #371:         match ImageDef(PILImages(m1,m2),meta):
                    _coconut_match_temp_367 = _coconut.getattr(PILImages, "_coconut_is_data", False) or _coconut.isinstance(PILImages, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImages)  # type: ignore  #371:         match ImageDef(PILImages(m1,m2),meta):
                    _coconut_match_set_name_meta = _coconut_case_match_to_16[1]  #371:         match ImageDef(PILImages(m1,m2),meta):
                    _coconut_match_temp_372 = _coconut.len(_coconut_case_match_to_16) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_16.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {}) and _coconut_case_match_to_16[i] == _coconut.getattr(_coconut_case_match_to_16, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_16.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16, "__match_args__") else _coconut.len(_coconut_case_match_to_16) == 2  # type: ignore  #371:         match ImageDef(PILImages(m1,m2),meta):
                    if _coconut_match_temp_372:  #371:         match ImageDef(PILImages(m1,m2),meta):
                        _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):
                if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                    _coconut_case_match_check_16 = False  #371:         match ImageDef(PILImages(m1,m2),meta):
                    if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                        _coconut_match_set_name_m1 = _coconut_sentinel  #371:         match ImageDef(PILImages(m1,m2),meta):
                        _coconut_match_set_name_m2 = _coconut_sentinel  #371:         match ImageDef(PILImages(m1,m2),meta):
                        if (_coconut_match_temp_367) and (_coconut.isinstance(_coconut_case_match_to_16[0], PILImages)) and (_coconut.len(_coconut_case_match_to_16[0]) >= 2):  #371:         match ImageDef(PILImages(m1,m2),meta):
                            _coconut_match_set_name_m1 = _coconut_case_match_to_16[0][0]  #371:         match ImageDef(PILImages(m1,m2),meta):
                            _coconut_match_set_name_m2 = _coconut_case_match_to_16[0][1]  #371:         match ImageDef(PILImages(m1,m2),meta):
                            _coconut_match_temp_368 = _coconut.len(_coconut_case_match_to_16[0]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_16[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_16[0][i] == _coconut.getattr(_coconut_case_match_to_16[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_16[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_16[0], "__match_args__") else _coconut.len(_coconut_case_match_to_16[0]) == 2  # type: ignore  #371:         match ImageDef(PILImages(m1,m2),meta):
                            if _coconut_match_temp_368:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):
                        if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                            if _coconut_match_set_name_m1 is not _coconut_sentinel:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                m1 = _coconut_match_set_name_m1  #371:         match ImageDef(PILImages(m1,m2),meta):
                            if _coconut_match_set_name_m2 is not _coconut_sentinel:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                m2 = _coconut_match_set_name_m2  #371:         match ImageDef(PILImages(m1,m2),meta):

                    if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                        if (not _coconut_match_temp_367) and (_coconut.isinstance(_coconut_case_match_to_16[0], PILImages)):  #371:         match ImageDef(PILImages(m1,m2),meta):
                            _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):
                        if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                            _coconut_case_match_check_16 = False  #371:         match ImageDef(PILImages(m1,m2),meta):
                            if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                if _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports 1)")  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):

                            if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                _coconut_match_set_name_m1 = _coconut_sentinel  #371:         match ImageDef(PILImages(m1,m2),meta):
                                _coconut_match_set_name_m2 = _coconut_sentinel  #371:         match ImageDef(PILImages(m1,m2),meta):
                                if not _coconut.type(_coconut_case_match_to_16[0]) in _coconut_self_match_types:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    _coconut_match_temp_369 = _coconut.getattr(PILImages, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    if not _coconut.isinstance(_coconut_match_temp_369, _coconut.tuple):  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        raise _coconut.TypeError("PILImages.__match_args__ must be a tuple")  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    if _coconut.len(_coconut_match_temp_369) < 2:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports %s)" % (_coconut.len(_coconut_match_temp_369),))  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    _coconut_match_temp_370 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_369[0], _coconut_sentinel)  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    _coconut_match_temp_371 = _coconut.getattr(_coconut_case_match_to_16[0], _coconut_match_temp_369[1], _coconut_sentinel)  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    if (_coconut_match_temp_370 is not _coconut_sentinel) and (_coconut_match_temp_371 is not _coconut_sentinel):  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        _coconut_match_set_name_m1 = _coconut_match_temp_370  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        _coconut_match_set_name_m2 = _coconut_match_temp_371  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):
                                if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    if _coconut_match_set_name_m1 is not _coconut_sentinel:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        m1 = _coconut_match_set_name_m1  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    if _coconut_match_set_name_m2 is not _coconut_sentinel:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        m2 = _coconut_match_set_name_m2  #371:         match ImageDef(PILImages(m1,m2),meta):




                if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                    if _coconut_match_set_name_meta is not _coconut_sentinel:  #371:         match ImageDef(PILImages(m1,m2),meta):
                        meta = _coconut_match_set_name_meta  #371:         match ImageDef(PILImages(m1,m2),meta):

            if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                if (not _coconut_match_temp_366) and (_coconut.isinstance(_coconut_case_match_to_16, ImageDef)):  #371:         match ImageDef(PILImages(m1,m2),meta):
                    _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):
                if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                    _coconut_case_match_check_16 = False  #371:         match ImageDef(PILImages(m1,m2),meta):
                    if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                        if _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #371:         match ImageDef(PILImages(m1,m2),meta):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #371:         match ImageDef(PILImages(m1,m2),meta):
                            _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):

                    if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                        _coconut_match_set_name_meta = _coconut_sentinel  #371:         match ImageDef(PILImages(m1,m2),meta):
                        if not _coconut.type(_coconut_case_match_to_16) in _coconut_self_match_types:  #371:         match ImageDef(PILImages(m1,m2),meta):
                            _coconut_match_temp_373 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #371:         match ImageDef(PILImages(m1,m2),meta):
                            if not _coconut.isinstance(_coconut_match_temp_373, _coconut.tuple):  #371:         match ImageDef(PILImages(m1,m2),meta):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #371:         match ImageDef(PILImages(m1,m2),meta):
                            if _coconut.len(_coconut_match_temp_373) < 2:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_373),))  #371:         match ImageDef(PILImages(m1,m2),meta):
                            _coconut_match_temp_374 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_373[0], _coconut_sentinel)  #371:         match ImageDef(PILImages(m1,m2),meta):
                            _coconut_match_temp_380 = _coconut.getattr(_coconut_case_match_to_16, _coconut_match_temp_373[1], _coconut_sentinel)  #371:         match ImageDef(PILImages(m1,m2),meta):
                            if (_coconut_match_temp_374 is not _coconut_sentinel) and (_coconut_match_temp_380 is not _coconut_sentinel):  #371:         match ImageDef(PILImages(m1,m2),meta):
                                _coconut_match_temp_375 = _coconut.getattr(PILImages, "_coconut_is_data", False) or _coconut.isinstance(PILImages, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in PILImages)  # type: ignore  #371:         match ImageDef(PILImages(m1,m2),meta):
                                _coconut_match_set_name_meta = _coconut_match_temp_380  #371:         match ImageDef(PILImages(m1,m2),meta):
                                _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):
                        if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                            _coconut_case_match_check_16 = False  #371:         match ImageDef(PILImages(m1,m2),meta):
                            if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                _coconut_match_set_name_m1 = _coconut_sentinel  #371:         match ImageDef(PILImages(m1,m2),meta):
                                _coconut_match_set_name_m2 = _coconut_sentinel  #371:         match ImageDef(PILImages(m1,m2),meta):
                                if (_coconut_match_temp_375) and (_coconut.isinstance(_coconut_match_temp_374, PILImages)) and (_coconut.len(_coconut_match_temp_374) >= 2):  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    _coconut_match_set_name_m1 = _coconut_match_temp_374[0]  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    _coconut_match_set_name_m2 = _coconut_match_temp_374[1]  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    _coconut_match_temp_376 = _coconut.len(_coconut_match_temp_374) <= _coconut.max(2, _coconut.len(_coconut_match_temp_374.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_374, "_coconut_data_defaults", {}) and _coconut_match_temp_374[i] == _coconut.getattr(_coconut_match_temp_374, "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_match_temp_374.__match_args__))) if _coconut.hasattr(_coconut_match_temp_374, "__match_args__") else _coconut.len(_coconut_match_temp_374) == 2  # type: ignore  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    if _coconut_match_temp_376:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):
                                if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    if _coconut_match_set_name_m1 is not _coconut_sentinel:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        m1 = _coconut_match_set_name_m1  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    if _coconut_match_set_name_m2 is not _coconut_sentinel:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        m2 = _coconut_match_set_name_m2  #371:         match ImageDef(PILImages(m1,m2),meta):

                            if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                if (not _coconut_match_temp_375) and (_coconut.isinstance(_coconut_match_temp_374, PILImages)):  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):
                                if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    _coconut_case_match_check_16 = False  #371:         match ImageDef(PILImages(m1,m2),meta):
                                    if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        if _coconut.type(_coconut_match_temp_374) in _coconut_self_match_types:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports 1)")  #371:         match ImageDef(PILImages(m1,m2),meta):
                                            _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):

                                    if not _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        _coconut_match_set_name_m1 = _coconut_sentinel  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        _coconut_match_set_name_m2 = _coconut_sentinel  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        if not _coconut.type(_coconut_match_temp_374) in _coconut_self_match_types:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                            _coconut_match_temp_377 = _coconut.getattr(PILImages, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #371:         match ImageDef(PILImages(m1,m2),meta):
                                            if not _coconut.isinstance(_coconut_match_temp_377, _coconut.tuple):  #371:         match ImageDef(PILImages(m1,m2),meta):
                                                raise _coconut.TypeError("PILImages.__match_args__ must be a tuple")  #371:         match ImageDef(PILImages(m1,m2),meta):
                                            if _coconut.len(_coconut_match_temp_377) < 2:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'PILImages' only supports %s)" % (_coconut.len(_coconut_match_temp_377),))  #371:         match ImageDef(PILImages(m1,m2),meta):
                                            _coconut_match_temp_378 = _coconut.getattr(_coconut_match_temp_374, _coconut_match_temp_377[0], _coconut_sentinel)  #371:         match ImageDef(PILImages(m1,m2),meta):
                                            _coconut_match_temp_379 = _coconut.getattr(_coconut_match_temp_374, _coconut_match_temp_377[1], _coconut_sentinel)  #371:         match ImageDef(PILImages(m1,m2),meta):
                                            if (_coconut_match_temp_378 is not _coconut_sentinel) and (_coconut_match_temp_379 is not _coconut_sentinel):  #371:         match ImageDef(PILImages(m1,m2),meta):
                                                _coconut_match_set_name_m1 = _coconut_match_temp_378  #371:         match ImageDef(PILImages(m1,m2),meta):
                                                _coconut_match_set_name_m2 = _coconut_match_temp_379  #371:         match ImageDef(PILImages(m1,m2),meta):
                                                _coconut_case_match_check_16 = True  #371:         match ImageDef(PILImages(m1,m2),meta):
                                        if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                            if _coconut_match_set_name_m1 is not _coconut_sentinel:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                                m1 = _coconut_match_set_name_m1  #371:         match ImageDef(PILImages(m1,m2),meta):
                                            if _coconut_match_set_name_m2 is not _coconut_sentinel:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                                m2 = _coconut_match_set_name_m2  #371:         match ImageDef(PILImages(m1,m2),meta):




                        if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
                            if _coconut_match_set_name_meta is not _coconut_sentinel:  #371:         match ImageDef(PILImages(m1,m2),meta):
                                meta = _coconut_match_set_name_meta  #371:         match ImageDef(PILImages(m1,m2),meta):




        if _coconut_case_match_check_16:  #371:         match ImageDef(PILImages(m1,m2),meta):
            return ([AutoList(ImageDef(PILImage(m1, m2), (ms_del_b_ch)(meta))),])  #372:             return [AutoList(ImageDef(PILImage(m1,m2),meta |> ms_del_b_ch))]

def numpys_to_numpy(state):  #373: def numpys_to_numpy(state):
    _coconut_case_match_to_17 = state  #374:     case state:
    _coconut_case_match_check_17 = False  #374:     case state:
    _coconut_match_temp_381 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #374:     case state:
    _coconut_case_match_check_17 = True  #374:     case state:
    if _coconut_case_match_check_17:  #374:     case state:
        _coconut_case_match_check_17 = False  #374:     case state:
        if not _coconut_case_match_check_17:  #374:     case state:
            _coconut_match_set_name_arng = _coconut_sentinel  #374:     case state:
            _coconut_match_set_name_shape = _coconut_sentinel  #374:     case state:
            _coconut_match_set_name_other_meta = _coconut_sentinel  #374:     case state:
            _coconut_match_set_name_kwargs = _coconut_sentinel  #374:     case state:
            if (_coconut_match_temp_381) and (_coconut.isinstance(_coconut_case_match_to_17, AutoList)) and (_coconut.len(_coconut_case_match_to_17) >= 1) and (_coconut.isinstance(_coconut_case_match_to_17[0], _coconut.abc.Mapping)):  #374:     case state:
                _coconut_match_temp_382 = _coconut_case_match_to_17[0].get("type", _coconut_sentinel)  #374:     case state:
                _coconut_match_temp_383 = _coconut_case_match_to_17[0].get("arrange", _coconut_sentinel)  #374:     case state:
                _coconut_match_temp_384 = _coconut_case_match_to_17[0].get("meta", _coconut_sentinel)  #374:     case state:
                _coconut_match_temp_386 = _coconut.len(_coconut_case_match_to_17) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_17.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_17, "_coconut_data_defaults", {}) and _coconut_case_match_to_17[i] == _coconut.getattr(_coconut_case_match_to_17, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_17.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_17, "__match_args__") else _coconut.len(_coconut_case_match_to_17) == 1  # type: ignore  #374:     case state:
                if (_coconut_match_temp_382 is not _coconut_sentinel) and (_coconut_match_temp_382 == "numpy") and (_coconut_match_temp_383 is not _coconut_sentinel) and (_coconut_match_temp_384 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_384, _coconut.abc.Mapping)) and (_coconut_match_temp_386):  #374:     case state:
                    _coconut_match_set_name_arng = _coconut_match_temp_383  #374:     case state:
                    _coconut_match_temp_385 = _coconut_match_temp_384.get("shape", _coconut_sentinel)  #374:     case state:
                    _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_17[0].items() if k not in _coconut.set(("type", "arrange", "meta")))  #374:     case state:
                    if _coconut_match_temp_385 is not _coconut_sentinel:  #374:     case state:
                        _coconut_match_set_name_shape = _coconut_match_temp_385  #374:     case state:
                        _coconut_match_set_name_other_meta = _coconut.dict((k, v) for k, v in _coconut_match_temp_384.items() if k not in _coconut.set(("shape",)))  #374:     case state:
                        _coconut_case_match_check_17 = True  #374:     case state:
            if _coconut_case_match_check_17:  #374:     case state:
                if _coconut_match_set_name_arng is not _coconut_sentinel:  #374:     case state:
                    arng = _coconut_match_set_name_arng  #374:     case state:
                if _coconut_match_set_name_shape is not _coconut_sentinel:  #374:     case state:
                    shape = _coconut_match_set_name_shape  #374:     case state:
                if _coconut_match_set_name_other_meta is not _coconut_sentinel:  #374:     case state:
                    other_meta = _coconut_match_set_name_other_meta  #374:     case state:
                if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #374:     case state:
                    kwargs = _coconut_match_set_name_kwargs  #374:     case state:

        if not _coconut_case_match_check_17:  #374:     case state:
            if (not _coconut_match_temp_381) and (_coconut.isinstance(_coconut_case_match_to_17, AutoList)):  #374:     case state:
                _coconut_case_match_check_17 = True  #374:     case state:
            if _coconut_case_match_check_17:  #374:     case state:
                _coconut_case_match_check_17 = False  #374:     case state:
                if not _coconut_case_match_check_17:  #374:     case state:
                    _coconut_match_set_name_arng = _coconut_sentinel  #374:     case state:
                    _coconut_match_set_name_shape = _coconut_sentinel  #374:     case state:
                    _coconut_match_set_name_other_meta = _coconut_sentinel  #374:     case state:
                    _coconut_match_set_name_kwargs = _coconut_sentinel  #374:     case state:
                    if (_coconut.type(_coconut_case_match_to_17) in _coconut_self_match_types) and (_coconut.isinstance(_coconut_case_match_to_17, _coconut.abc.Mapping)):  #374:     case state:
                        _coconut_match_temp_387 = _coconut_case_match_to_17.get("type", _coconut_sentinel)  #374:     case state:
                        _coconut_match_temp_388 = _coconut_case_match_to_17.get("arrange", _coconut_sentinel)  #374:     case state:
                        _coconut_match_temp_389 = _coconut_case_match_to_17.get("meta", _coconut_sentinel)  #374:     case state:
                        if (_coconut_match_temp_387 is not _coconut_sentinel) and (_coconut_match_temp_387 == "numpy") and (_coconut_match_temp_388 is not _coconut_sentinel) and (_coconut_match_temp_389 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_389, _coconut.abc.Mapping)):  #374:     case state:
                            _coconut_match_set_name_arng = _coconut_match_temp_388  #374:     case state:
                            _coconut_match_temp_390 = _coconut_match_temp_389.get("shape", _coconut_sentinel)  #374:     case state:
                            _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_17.items() if k not in _coconut.set(("type", "arrange", "meta")))  #374:     case state:
                            if _coconut_match_temp_390 is not _coconut_sentinel:  #374:     case state:
                                _coconut_match_set_name_shape = _coconut_match_temp_390  #374:     case state:
                                _coconut_match_set_name_other_meta = _coconut.dict((k, v) for k, v in _coconut_match_temp_389.items() if k not in _coconut.set(("shape",)))  #374:     case state:
                                _coconut_case_match_check_17 = True  #374:     case state:
                    if _coconut_case_match_check_17:  #374:     case state:
                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #374:     case state:
                            arng = _coconut_match_set_name_arng  #374:     case state:
                        if _coconut_match_set_name_shape is not _coconut_sentinel:  #374:     case state:
                            shape = _coconut_match_set_name_shape  #374:     case state:
                        if _coconut_match_set_name_other_meta is not _coconut_sentinel:  #374:     case state:
                            other_meta = _coconut_match_set_name_other_meta  #374:     case state:
                        if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #374:     case state:
                            kwargs = _coconut_match_set_name_kwargs  #374:     case state:

                if not _coconut_case_match_check_17:  #374:     case state:
                    _coconut_match_set_name_arng = _coconut_sentinel  #374:     case state:
                    _coconut_match_set_name_shape = _coconut_sentinel  #374:     case state:
                    _coconut_match_set_name_other_meta = _coconut_sentinel  #374:     case state:
                    _coconut_match_set_name_kwargs = _coconut_sentinel  #374:     case state:
                    if not _coconut.type(_coconut_case_match_to_17) in _coconut_self_match_types:  #374:     case state:
                        _coconut_match_temp_391 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #374:     case state:
                        if not _coconut.isinstance(_coconut_match_temp_391, _coconut.tuple):  #374:     case state:
                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #374:     case state:
                        if _coconut.len(_coconut_match_temp_391) < 1:  #374:     case state:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_391),))  #374:     case state:
                        _coconut_match_temp_392 = _coconut.getattr(_coconut_case_match_to_17, _coconut_match_temp_391[0], _coconut_sentinel)  #374:     case state:
                        if (_coconut_match_temp_392 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_392, _coconut.abc.Mapping)):  #374:     case state:
                            _coconut_match_temp_393 = _coconut_match_temp_392.get("type", _coconut_sentinel)  #374:     case state:
                            _coconut_match_temp_394 = _coconut_match_temp_392.get("arrange", _coconut_sentinel)  #374:     case state:
                            _coconut_match_temp_395 = _coconut_match_temp_392.get("meta", _coconut_sentinel)  #374:     case state:
                            if (_coconut_match_temp_393 is not _coconut_sentinel) and (_coconut_match_temp_393 == "numpy") and (_coconut_match_temp_394 is not _coconut_sentinel) and (_coconut_match_temp_395 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_395, _coconut.abc.Mapping)):  #374:     case state:
                                _coconut_match_set_name_arng = _coconut_match_temp_394  #374:     case state:
                                _coconut_match_temp_396 = _coconut_match_temp_395.get("shape", _coconut_sentinel)  #374:     case state:
                                _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_match_temp_392.items() if k not in _coconut.set(("type", "arrange", "meta")))  #374:     case state:
                                if _coconut_match_temp_396 is not _coconut_sentinel:  #374:     case state:
                                    _coconut_match_set_name_shape = _coconut_match_temp_396  #374:     case state:
                                    _coconut_match_set_name_other_meta = _coconut.dict((k, v) for k, v in _coconut_match_temp_395.items() if k not in _coconut.set(("shape",)))  #374:     case state:
                                    _coconut_case_match_check_17 = True  #374:     case state:
                    if _coconut_case_match_check_17:  #374:     case state:
                        if _coconut_match_set_name_arng is not _coconut_sentinel:  #374:     case state:
                            arng = _coconut_match_set_name_arng  #374:     case state:
                        if _coconut_match_set_name_shape is not _coconut_sentinel:  #374:     case state:
                            shape = _coconut_match_set_name_shape  #374:     case state:
                        if _coconut_match_set_name_other_meta is not _coconut_sentinel:  #374:     case state:
                            other_meta = _coconut_match_set_name_other_meta  #374:     case state:
                        if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #374:     case state:
                            kwargs = _coconut_match_set_name_kwargs  #374:     case state:




    if _coconut_case_match_check_17 and not ("B" not in arng):  #374:     case state:
        _coconut_case_match_check_17 = False  #374:     case state:
    if _coconut_case_match_check_17:  #374:     case state:
        return ([(lambda numpys: np.array(numpys), frozendict(_coconut_dict_merge(_coconut.dict((("type", "numpy"), ("arrange", "B" + arng), ("meta", fdict(_coconut_dict_merge(_coconut.dict((("shape", (None,) + shape),)), other_meta))))), kwargs)), "merge arrays to array".format(), 10),])  #376:             return [

def tensor_to_list(state):  #382: def tensor_to_list(state):
    _coconut_case_match_to_18 = state  #383:     case state:
    _coconut_case_match_check_18 = False  #383:     case state:
    _coconut_match_set_name_arng = _coconut_sentinel  #383:     case state:
    _coconut_match_set_name_shape = _coconut_sentinel  #383:     case state:
    _coconut_match_set_name_other_meta = _coconut_sentinel  #383:     case state:
    _coconut_match_set_name_kwargs = _coconut_sentinel  #383:     case state:
    if _coconut.isinstance(_coconut_case_match_to_18, _coconut.abc.Mapping):  #383:     case state:
        _coconut_match_temp_397 = _coconut_case_match_to_18.get("arrange", _coconut_sentinel)  #383:     case state:
        _coconut_match_temp_399 = _coconut_case_match_to_18.get("meta", _coconut_sentinel)  #383:     case state:
        if (_coconut_match_temp_397 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_397, _coconut.str)) and (_coconut.len(_coconut_match_temp_397) >= 1) and (_coconut_match_temp_397.startswith("B")) and (_coconut_match_temp_399 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_399, _coconut.abc.Mapping)):  #383:     case state:
            _coconut_match_temp_400 = _coconut_match_temp_399.get("shape", _coconut_sentinel)  #383:     case state:
            _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_18.items() if k not in _coconut.set(("arrange", "meta")))  #383:     case state:
            if _coconut_match_temp_400 is not _coconut_sentinel:  #383:     case state:
                _coconut_match_temp_398 = _coconut_match_temp_397[1:]  #383:     case state:
                _coconut_match_set_name_shape = _coconut_match_temp_400  #383:     case state:
                _coconut_match_set_name_other_meta = _coconut.dict((k, v) for k, v in _coconut_match_temp_399.items() if k not in _coconut.set(("shape",)))  #383:     case state:
                _coconut_match_set_name_arng = _coconut_match_temp_398  #383:     case state:
                _coconut_case_match_check_18 = True  #383:     case state:
    if _coconut_case_match_check_18:  #383:     case state:
        if _coconut_match_set_name_arng is not _coconut_sentinel:  #383:     case state:
            arng = _coconut_match_set_name_arng  #383:     case state:
        if _coconut_match_set_name_shape is not _coconut_sentinel:  #383:     case state:
            shape = _coconut_match_set_name_shape  #383:     case state:
        if _coconut_match_set_name_other_meta is not _coconut_sentinel:  #383:     case state:
            other_meta = _coconut_match_set_name_other_meta  #383:     case state:
        if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #383:     case state:
            kwargs = _coconut_match_set_name_kwargs  #383:     case state:
    if _coconut_case_match_check_18 and not (len(arng) > 1):  #383:     case state:
        _coconut_case_match_check_18 = False  #383:     case state:
    if _coconut_case_match_check_18:  #383:     case state:
        return ([(lambda tensor: [t for t in tensor], AutoList(fdict(arrange=arng, meta=fdict(_coconut_dict_merge(_coconut.dict((("shape", shape[1:]),)), other_meta)), **kwargs)), "tensor to list of tensor".format(), 2),])  #385:             return [
    if not _coconut_case_match_check_18:  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
        _coconut_match_set_name_arng = _coconut_sentinel  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
        _coconut_match_set_name_shape = _coconut_sentinel  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
        _coconut_match_set_name_other_meta = _coconut_sentinel  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
        _coconut_match_set_name_cr = _coconut_sentinel  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
        _coconut_match_set_name_kwargs = _coconut_sentinel  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
        if _coconut.isinstance(_coconut_case_match_to_18, _coconut.abc.Mapping):  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
            _coconut_match_temp_401 = _coconut_case_match_to_18.get("arrange", _coconut_sentinel)  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
            _coconut_match_temp_403 = _coconut_case_match_to_18.get("meta", _coconut_sentinel)  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
            _coconut_match_temp_405 = _coconut_case_match_to_18.get("ch_rpr", _coconut_sentinel)  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
            if (_coconut_match_temp_401 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_401, _coconut.str)) and (_coconut.len(_coconut_match_temp_401) >= 1) and (_coconut_match_temp_401.startswith("C")) and (_coconut_match_temp_403 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_403, _coconut.abc.Mapping)) and (_coconut_match_temp_405 is not _coconut_sentinel):  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                _coconut_match_temp_404 = _coconut_match_temp_403.get("shape", _coconut_sentinel)  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                _coconut_match_set_name_cr = _coconut_match_temp_405  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_18.items() if k not in _coconut.set(("arrange", "meta", "ch_rpr")))  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                if _coconut_match_temp_404 is not _coconut_sentinel:  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                    _coconut_match_temp_402 = _coconut_match_temp_401[1:]  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                    _coconut_match_set_name_shape = _coconut_match_temp_404  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                    _coconut_match_set_name_other_meta = _coconut.dict((k, v) for k, v in _coconut_match_temp_403.items() if k not in _coconut.set(("shape",)))  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                    _coconut_match_set_name_arng = _coconut_match_temp_402  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                    _coconut_case_match_check_18 = True  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
        if _coconut_case_match_check_18:  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
            if _coconut_match_set_name_arng is not _coconut_sentinel:  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                arng = _coconut_match_set_name_arng  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
            if _coconut_match_set_name_shape is not _coconut_sentinel:  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                shape = _coconut_match_set_name_shape  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
            if _coconut_match_set_name_other_meta is not _coconut_sentinel:  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                other_meta = _coconut_match_set_name_other_meta  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
            if _coconut_match_set_name_cr is not _coconut_sentinel:  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                cr = _coconut_match_set_name_cr  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
            if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
                kwargs = _coconut_match_set_name_kwargs  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
        if _coconut_case_match_check_18 and not (len(arng) > 1):  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
            _coconut_case_match_check_18 = False  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
        if _coconut_case_match_check_18:  #391:         match {"arrange":"C"+arng,"meta":{"shape":shape,**other_meta},"ch_rpr":cr,**kwargs} if len(arng) > 1:
            return ([(lambda tensor: [t for t in tensor], AutoList(fdict(arrange=arng, meta=fdict(_coconut_dict_merge(_coconut.dict((("shape", shape[1:]),)), other_meta)), ch_rpr="L", **kwargs)), "split CHW to [HW]".format(), 2),])  #392:             return [



def rgb_to_rgba(state):  #403: def rgb_to_rgba(state):
    if state == "numpy,uint8,HWC,RGB,0_255":  #404:     if state == "numpy,uint8,HWC,RGB,0_255":
        return ([(lambda a: np.concatenate((a, np.ones((*a.shape[:2], 1), dtype="uint8") * 255), axis=2), "numpy,uint8,HWC,RGBA,0_255", "add 255 as alpha channel", 10),])  #405:         return [(
    elif state == "numpy,uint8,BHWC,RGB,0_255":  #411:     elif state == "numpy,uint8,BHWC,RGB,0_255":
        return ([(lambda a: np.concatenate((a, np.ones((*a.shape[:3], 1), dtype="uint8") * 255), axis=3), "numpy,uint8,BHWC,RGBA,0_255", "add 255 as alpha channel to batch", 10),])  #412:         return [(


@memoize()  #419: @memoize()
def pix2pix_normalizer(nc):  #420: def pix2pix_normalizer(nc):
    from torchvision import transforms  #421:     import torchvision.transforms as transforms
    return (transforms.Normalize((0.5,) * nc, (0.5,) * nc))  #422:     return transforms.Normalize((0.5,)*nc,(0.5,)*nc)



def torch_img_to_pixpix_input(state):  #425: def torch_img_to_pixpix_input(state):
    _coconut_case_match_to_19 = state  #426:     case state:
    _coconut_case_match_check_19 = False  #426:     case state:
    _coconut_match_set_name_rpr = _coconut_sentinel  #426:     case state:
    _coconut_match_set_name_kwargs = _coconut_sentinel  #426:     case state:
    if _coconut.isinstance(_coconut_case_match_to_19, _coconut.abc.Mapping):  #426:     case state:
        _coconut_match_temp_406 = _coconut_case_match_to_19.get("type", _coconut_sentinel)  #426:     case state:
        _coconut_match_temp_407 = _coconut_case_match_to_19.get("dtype", _coconut_sentinel)  #426:     case state:
        _coconut_match_temp_408 = _coconut_case_match_to_19.get("arrange", _coconut_sentinel)  #426:     case state:
        _coconut_match_temp_409 = _coconut_case_match_to_19.get("v_range", _coconut_sentinel)  #426:     case state:
        _coconut_match_temp_410 = _coconut_case_match_to_19.get("ch_rpr", _coconut_sentinel)  #426:     case state:
        if (_coconut_match_temp_406 is not _coconut_sentinel) and (_coconut_match_temp_406 == "torch") and (_coconut_match_temp_407 is not _coconut_sentinel) and (_coconut_match_temp_407 == "float32") and (_coconut_match_temp_408 is not _coconut_sentinel) and (_coconut_match_temp_408 == "CHW") and (_coconut_match_temp_409 is not _coconut_sentinel) and (_coconut_match_temp_409 == "0_1") and (_coconut_match_temp_410 is not _coconut_sentinel):  #426:     case state:
            _coconut_match_set_name_rpr = _coconut_match_temp_410  #426:     case state:
            _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_19.items() if k not in _coconut.set(("type", "dtype", "arrange", "v_range", "ch_rpr")))  #426:     case state:
            _coconut_case_match_check_19 = True  #426:     case state:
    if _coconut_case_match_check_19:  #426:     case state:
        _coconut_case_match_check_19 = False  #426:     case state:
        if not _coconut_case_match_check_19:  #426:     case state:
            if _coconut_match_temp_410 == "RGB":  #426:     case state:
                _coconut_case_match_check_19 = True  #426:     case state:

        if not _coconut_case_match_check_19:  #426:     case state:
            if _coconut_match_temp_410 == "RGBA":  #426:     case state:
                _coconut_case_match_check_19 = True  #426:     case state:

        if not _coconut_case_match_check_19:  #426:     case state:
            if _coconut_match_temp_410 == "L":  #426:     case state:
                _coconut_case_match_check_19 = True  #426:     case state:


    if _coconut_case_match_check_19:  #426:     case state:
        if _coconut_match_set_name_rpr is not _coconut_sentinel:  #426:     case state:
            rpr = _coconut_match_set_name_rpr  #426:     case state:
        if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #426:     case state:
            kwargs = _coconut_match_set_name_kwargs  #426:     case state:
    if _coconut_case_match_check_19:  #426:     case state:
        return ([(pix2pix_normalizer(len(rpr)), "pix2pix,nc={_coconut_format_0}".format(_coconut_format_0=(len(rpr))), "to pixpix normalized", 1),])  #428:             return [(
    if not _coconut_case_match_check_19:  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
        _coconut_match_set_name_rpr = _coconut_sentinel  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
        _coconut_match_set_name_kwargs = _coconut_sentinel  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
        if _coconut.isinstance(_coconut_case_match_to_19, _coconut.abc.Mapping):  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
            _coconut_match_temp_411 = _coconut_case_match_to_19.get("type", _coconut_sentinel)  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
            _coconut_match_temp_412 = _coconut_case_match_to_19.get("dtype", _coconut_sentinel)  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
            _coconut_match_temp_413 = _coconut_case_match_to_19.get("arrange", _coconut_sentinel)  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
            _coconut_match_temp_414 = _coconut_case_match_to_19.get("v_range", _coconut_sentinel)  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
            _coconut_match_temp_415 = _coconut_case_match_to_19.get("ch_rpr", _coconut_sentinel)  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
            if (_coconut_match_temp_411 is not _coconut_sentinel) and (_coconut_match_temp_411 == "torch") and (_coconut_match_temp_412 is not _coconut_sentinel) and (_coconut_match_temp_412 == "float32") and (_coconut_match_temp_413 is not _coconut_sentinel) and (_coconut_match_temp_413 == "BCHW") and (_coconut_match_temp_414 is not _coconut_sentinel) and (_coconut_match_temp_414 == "0_1") and (_coconut_match_temp_415 is not _coconut_sentinel):  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
                _coconut_match_set_name_rpr = _coconut_match_temp_415  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
                _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_19.items() if k not in _coconut.set(("type", "dtype", "arrange", "v_range", "ch_rpr")))  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
                _coconut_case_match_check_19 = True  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
        if _coconut_case_match_check_19:  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
            _coconut_case_match_check_19 = False  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
            if not _coconut_case_match_check_19:  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
                if _coconut_match_temp_415 == "RGB":  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
                    _coconut_case_match_check_19 = True  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:

            if not _coconut_case_match_check_19:  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
                if _coconut_match_temp_415 == "RGBA":  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
                    _coconut_case_match_check_19 = True  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:

            if not _coconut_case_match_check_19:  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
                if _coconut_match_temp_415 == "L":  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
                    _coconut_case_match_check_19 = True  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:


        if _coconut_case_match_check_19:  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
            if _coconut_match_set_name_rpr is not _coconut_sentinel:  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
                rpr = _coconut_match_set_name_rpr  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
            if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
                kwargs = _coconut_match_set_name_kwargs  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
        if _coconut_case_match_check_19:  #434:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":("RGB" or "RGBA" or "L") as rpr,**kwargs}:
            return ([(lambda t: torch.cat([pix2pix_normalizer(len(rpr))(i)[None] for i in t], dim=0), "pix2pix_batch,nc={_coconut_format_0}".format(_coconut_format_0=(len(rpr))), "to pixpix normalized", 1),])  #435:             return [(
    if not _coconut_case_match_check_19:  #441:         match "pix2pix_laba":
        if _coconut_case_match_to_19 == "pix2pix_laba":  #441:         match "pix2pix_laba":
            _coconut_case_match_check_19 = True  #441:         match "pix2pix_laba":
        if _coconut_case_match_check_19:  #441:         match "pix2pix_laba":
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,CHW,LABA,0_1".format(), "inverse pix2pix_laba to img ", 1),])  #442:             return [(
    if not _coconut_case_match_check_19:  #448:         match "pix2pix_lab":
        if _coconut_case_match_to_19 == "pix2pix_lab":  #448:         match "pix2pix_lab":
            _coconut_case_match_check_19 = True  #448:         match "pix2pix_lab":
        if _coconut_case_match_check_19:  #448:         match "pix2pix_lab":
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,CHW,LAB,0_1".format(), "inverse pix2pix_lab to img ", 1),])  #449:             return [(
    if not _coconut_case_match_check_19:  #455:         match "pix2pix_laba_batch":
        if _coconut_case_match_to_19 == "pix2pix_laba_batch":  #455:         match "pix2pix_laba_batch":
            _coconut_case_match_check_19 = True  #455:         match "pix2pix_laba_batch":
        if _coconut_case_match_check_19:  #455:         match "pix2pix_laba_batch":
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,BCHW,LABA,0_1".format(), "inverse pix2pix_laba batch to img", 1),])  #456:             return [(
    if not _coconut_case_match_check_19:  #462:         match "pix2pix_lab_batch":
        if _coconut_case_match_to_19 == "pix2pix_lab_batch":  #462:         match "pix2pix_lab_batch":
            _coconut_case_match_check_19 = True  #462:         match "pix2pix_lab_batch":
        if _coconut_case_match_check_19:  #462:         match "pix2pix_lab_batch":
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,BCHW,LAB,0_1".format(), "inverse pix2pix_laba batch to img", 1),])  #463:             return [(
    if not _coconut_case_match_check_19:  #469:         match "pix2pix,nc=4":
        if _coconut_case_match_to_19 == "pix2pix,nc=4":  #469:         match "pix2pix,nc=4":
            _coconut_case_match_check_19 = True  #469:         match "pix2pix,nc=4":
        if _coconut_case_match_check_19:  #469:         match "pix2pix,nc=4":
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,CHW,RGBA,0_1".format(), "inverse pix2pix to img", 1),])  #470:             return [(
    if not _coconut_case_match_check_19:  #476:         match "pix2pix_batch,nc=4":
        if _coconut_case_match_to_19 == "pix2pix_batch,nc=4":  #476:         match "pix2pix_batch,nc=4":
            _coconut_case_match_check_19 = True  #476:         match "pix2pix_batch,nc=4":
        if _coconut_case_match_check_19:  #476:         match "pix2pix_batch,nc=4":
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,BCHW,RGBA,0_1".format(), "inverse pix2pix batch nc=4 to img", 1),])  #477:             return [(
    if not _coconut_case_match_check_19:  #483:         match "pix2pix_batch,nc=3":
        if _coconut_case_match_to_19 == "pix2pix_batch,nc=3":  #483:         match "pix2pix_batch,nc=3":
            _coconut_case_match_check_19 = True  #483:         match "pix2pix_batch,nc=3":
        if _coconut_case_match_check_19:  #483:         match "pix2pix_batch,nc=3":
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,BCHW,RGB,0_1".format(), "inverse pix2pix batch nc=3 to img", 1),])  #484:             return [(
    if not _coconut_case_match_check_19:  #490:         match "pix2pix,nc=3":
        if _coconut_case_match_to_19 == "pix2pix,nc=3":  #490:         match "pix2pix,nc=3":
            _coconut_case_match_check_19 = True  #490:         match "pix2pix,nc=3":
        if _coconut_case_match_check_19:  #490:         match "pix2pix,nc=3":
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,CHW,RGB,0_1".format(), "inverse pix2pix to img", 1),])  #491:             return [(
    if not _coconut_case_match_check_19:  #497:         match "pix2pix_batch,nc=1":
        if _coconut_case_match_to_19 == "pix2pix_batch,nc=1":  #497:         match "pix2pix_batch,nc=1":
            _coconut_case_match_check_19 = True  #497:         match "pix2pix_batch,nc=1":
        if _coconut_case_match_check_19:  #497:         match "pix2pix_batch,nc=1":
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,BCHW,L,0_1".format(), "inverse pix2pix_batch,nc=1 to img", 1),])  #498:             return [(
    if not _coconut_case_match_check_19:  #504:         match "pix2pix,nc=1":
        if _coconut_case_match_to_19 == "pix2pix,nc=1":  #504:         match "pix2pix,nc=1":
            _coconut_case_match_check_19 = True  #504:         match "pix2pix,nc=1":
        if _coconut_case_match_check_19:  #504:         match "pix2pix,nc=1":
            return ([(lambda a: a * 0.5 + 0.5, "torch,float32,CHW,L,0_1".format(), "inverse pix2pix,nc=1 to img", 1),])  #505:             return [(


@memoize()  #512: @memoize()
def _VGG_NORMALIZER():  #513: def _VGG_NORMALIZER():
    from torchvision import transforms  #514:     import torchvision.transforms as transforms
    nrm = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  #515:     nrm = transforms.Normalize(mean=[0.485,0.456,0.406],std=[0.229,0.224,0.225])
    return (nrm)  #516:     return nrm

def inverse_vgg_prep(tensor):  #517: def inverse_vgg_prep(tensor):
    return (tensor.cpu() * torch.tensor([0.229, 0.224, 0.225])[:, None, None] + torch.tensor([0.485, 0.456, 0.406])[:, None, None])  #518:     return tensor.cpu() * torch.tensor([0.229,0.224,0.225])[:,None,None] + torch.tensor([0.485,0.456,0.406])[:,None,None]

def inverse_vgg_prep_batch(tensor):  #519: def inverse_vgg_prep_batch(tensor):
    return (tensor.cpu() * torch.tensor([0.229, 0.224, 0.225])[None, :, None, None] + torch.tensor([0.485, 0.456, 0.406])[None, :, None, None])  #520:     return tensor.cpu() * torch.tensor([0.229,0.224,0.225])[None,:,None,None] + torch.tensor([0.485,0.456,0.406])[None,:,None,None]

def torch_img_to_vgg_prep(state):  #521: def torch_img_to_vgg_prep(state):
    VGG_NORMALIZER = _VGG_NORMALIZER()  #522:     VGG_NORMALIZER = _VGG_NORMALIZER()
    _coconut_case_match_to_20 = state  #523:     case state:
    _coconut_case_match_check_20 = False  #523:     case state:
    if _coconut_case_match_to_20 == "vgg_prep":  #523:     case state:
        _coconut_case_match_check_20 = True  #523:     case state:
    if _coconut_case_match_check_20:  #523:     case state:
        return ([(inverse_vgg_prep, "torch,float32,CHW,RGB,0_1", "inverse from vgg_prep", 1),])  #525:             return [(
    if not _coconut_case_match_check_20:  #531:         match "vgg_prep_batch":
        if _coconut_case_match_to_20 == "vgg_prep_batch":  #531:         match "vgg_prep_batch":
            _coconut_case_match_check_20 = True  #531:         match "vgg_prep_batch":
        if _coconut_case_match_check_20:  #531:         match "vgg_prep_batch":
            return ([(inverse_vgg_prep_batch, "torch,float32,BCHW,RGB,0_1", "inverse from vgg_prep_batch", 1),])  #532:             return [(
    if not _coconut_case_match_check_20:  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
        _coconut_match_set_name_kwargs = _coconut_sentinel  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
        if _coconut.isinstance(_coconut_case_match_to_20, _coconut.abc.Mapping):  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            _coconut_match_temp_416 = _coconut_case_match_to_20.get("type", _coconut_sentinel)  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            _coconut_match_temp_417 = _coconut_case_match_to_20.get("dtype", _coconut_sentinel)  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            _coconut_match_temp_418 = _coconut_case_match_to_20.get("arrange", _coconut_sentinel)  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            _coconut_match_temp_419 = _coconut_case_match_to_20.get("v_range", _coconut_sentinel)  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            _coconut_match_temp_420 = _coconut_case_match_to_20.get("ch_rpr", _coconut_sentinel)  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            if (_coconut_match_temp_416 is not _coconut_sentinel) and (_coconut_match_temp_416 == "torch") and (_coconut_match_temp_417 is not _coconut_sentinel) and (_coconut_match_temp_417 == "float32") and (_coconut_match_temp_418 is not _coconut_sentinel) and (_coconut_match_temp_418 == "CHW") and (_coconut_match_temp_419 is not _coconut_sentinel) and (_coconut_match_temp_419 == "0_1") and (_coconut_match_temp_420 is not _coconut_sentinel) and (_coconut_match_temp_420 == "RGB"):  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
                _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_20.items() if k not in _coconut.set(("type", "dtype", "arrange", "v_range", "ch_rpr")))  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
                _coconut_case_match_check_20 = True  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
        if _coconut_case_match_check_20:  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
                kwargs = _coconut_match_set_name_kwargs  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
        if _coconut_case_match_check_20:  #538:         match {"type":"torch","dtype":"float32","arrange":"CHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            return ([(VGG_NORMALIZER, "vgg_prep".format(), "to vgg normalized", 1),])  #539:             return [(
    if not _coconut_case_match_check_20:  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
        _coconut_match_set_name_kwargs = _coconut_sentinel  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
        if _coconut.isinstance(_coconut_case_match_to_20, _coconut.abc.Mapping):  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            _coconut_match_temp_421 = _coconut_case_match_to_20.get("type", _coconut_sentinel)  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            _coconut_match_temp_422 = _coconut_case_match_to_20.get("dtype", _coconut_sentinel)  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            _coconut_match_temp_423 = _coconut_case_match_to_20.get("arrange", _coconut_sentinel)  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            _coconut_match_temp_424 = _coconut_case_match_to_20.get("v_range", _coconut_sentinel)  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            _coconut_match_temp_425 = _coconut_case_match_to_20.get("ch_rpr", _coconut_sentinel)  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            if (_coconut_match_temp_421 is not _coconut_sentinel) and (_coconut_match_temp_421 == "torch") and (_coconut_match_temp_422 is not _coconut_sentinel) and (_coconut_match_temp_422 == "float32") and (_coconut_match_temp_423 is not _coconut_sentinel) and (_coconut_match_temp_423 == "BCHW") and (_coconut_match_temp_424 is not _coconut_sentinel) and (_coconut_match_temp_424 == "0_1") and (_coconut_match_temp_425 is not _coconut_sentinel) and (_coconut_match_temp_425 == "RGB"):  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
                _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_20.items() if k not in _coconut.set(("type", "dtype", "arrange", "v_range", "ch_rpr")))  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
                _coconut_case_match_check_20 = True  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
        if _coconut_case_match_check_20:  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
                kwargs = _coconut_match_set_name_kwargs  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
        if _coconut_case_match_check_20:  #545:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGB",**kwargs}:
            return ([(lambda t: torch.cat([VGG_NORMALIZER(i)[None] for i in t], dim=0), "vgg_prep_batch".format(), "to vgg normalized batch", 1),])  #546:             return [(
    if not _coconut_case_match_check_20:  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
        _coconut_match_set_name_kwargs = _coconut_sentinel  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
        if _coconut.isinstance(_coconut_case_match_to_20, _coconut.abc.Mapping):  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
            _coconut_match_temp_426 = _coconut_case_match_to_20.get("type", _coconut_sentinel)  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
            _coconut_match_temp_427 = _coconut_case_match_to_20.get("dtype", _coconut_sentinel)  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
            _coconut_match_temp_428 = _coconut_case_match_to_20.get("arrange", _coconut_sentinel)  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
            _coconut_match_temp_429 = _coconut_case_match_to_20.get("v_range", _coconut_sentinel)  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
            _coconut_match_temp_430 = _coconut_case_match_to_20.get("ch_rpr", _coconut_sentinel)  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
            if (_coconut_match_temp_426 is not _coconut_sentinel) and (_coconut_match_temp_426 == "torch") and (_coconut_match_temp_427 is not _coconut_sentinel) and (_coconut_match_temp_427 == "float32") and (_coconut_match_temp_428 is not _coconut_sentinel) and (_coconut_match_temp_428 == "BCHW") and (_coconut_match_temp_429 is not _coconut_sentinel) and (_coconut_match_temp_429 == "0_1") and (_coconut_match_temp_430 is not _coconut_sentinel) and (_coconut_match_temp_430 == "RGBA"):  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
                _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_20.items() if k not in _coconut.set(("type", "dtype", "arrange", "v_range", "ch_rpr")))  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
                _coconut_case_match_check_20 = True  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
        if _coconut_case_match_check_20:  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
            if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
                kwargs = _coconut_match_set_name_kwargs  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
        if _coconut_case_match_check_20:  #552:         match {"type":"torch","dtype":"float32","arrange":"BCHW","v_range":"0_1","ch_rpr":"RGBA",**kwargs}:
            return ([(lambda t: torch.cat([torch.cat((VGG_NORMALIZER(i[:3])[None], i[[3,]][None]), dim=1) for i in t], dim=0), "vgg_prep_batch_masked".format(), "to vgg normalized batch", 1),])  #553:             return [(

def repeat_ch(state):  #561: def repeat_ch(state):
    _coconut_case_match_to_21 = state  #562:     case state:
    _coconut_case_match_check_21 = False  #562:     case state:
    _coconut_match_set_name_ch = _coconut_sentinel  #562:     case state:
    _coconut_match_set_name_shape = _coconut_sentinel  #562:     case state:
    _coconut_match_set_name_other = _coconut_sentinel  #562:     case state:
    _coconut_match_set_name_kwargs = _coconut_sentinel  #562:     case state:
    if _coconut.isinstance(_coconut_case_match_to_21, _coconut.abc.Mapping):  #562:     case state:
        _coconut_match_temp_431 = _coconut_case_match_to_21.get("type", _coconut_sentinel)  #562:     case state:
        _coconut_match_temp_432 = _coconut_case_match_to_21.get("mode", _coconut_sentinel)  #562:     case state:
        _coconut_match_temp_433 = _coconut_case_match_to_21.get("ch_rpr", _coconut_sentinel)  #562:     case state:
        _coconut_match_temp_434 = _coconut_case_match_to_21.get("meta", _coconut_sentinel)  #562:     case state:
        if (_coconut_match_temp_431 is not _coconut_sentinel) and (_coconut_match_temp_431 == "image") and (_coconut_match_temp_432 is not _coconut_sentinel) and (_coconut_match_temp_432 == "L") and (_coconut_match_temp_433 is not _coconut_sentinel) and (_coconut_match_temp_434 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_434, _coconut.abc.Mapping)):  #562:     case state:
            _coconut_match_set_name_ch = _coconut_match_temp_433  #562:     case state:
            _coconut_match_temp_435 = _coconut_match_temp_434.get("shape", _coconut_sentinel)  #562:     case state:
            _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_21.items() if k not in _coconut.set(("type", "mode", "ch_rpr", "meta")))  #562:     case state:
            if _coconut_match_temp_435 is not _coconut_sentinel:  #562:     case state:
                _coconut_match_set_name_shape = _coconut_match_temp_435  #562:     case state:
                _coconut_match_set_name_other = _coconut.dict((k, v) for k, v in _coconut_match_temp_434.items() if k not in _coconut.set(("shape",)))  #562:     case state:
                _coconut_case_match_check_21 = True  #562:     case state:
    if _coconut_case_match_check_21:  #562:     case state:
        if _coconut_match_set_name_ch is not _coconut_sentinel:  #562:     case state:
            ch = _coconut_match_set_name_ch  #562:     case state:
        if _coconut_match_set_name_shape is not _coconut_sentinel:  #562:     case state:
            shape = _coconut_match_set_name_shape  #562:     case state:
        if _coconut_match_set_name_other is not _coconut_sentinel:  #562:     case state:
            other = _coconut_match_set_name_other  #562:     case state:
        if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #562:     case state:
            kwargs = _coconut_match_set_name_kwargs  #562:     case state:
    if _coconut_case_match_check_21 and not (len(ch_splitter(ch)) == 1):  #562:     case state:
        _coconut_case_match_check_21 = False  #562:     case state:
    if _coconut_case_match_check_21:  #562:     case state:
        return ([(lambda a: np.repeat(np.array(a)[:, :, None], 3, axis=2), fdict(type="numpy", dtype="uint8", arrange="HWC", ch_rpr=ch * 3, v_range="0_255", meta=fdict(_coconut_dict_merge(_coconut.dict((("shape", (shape[0], shape[1], 3)),)), other)), **kwargs), "repeat_channel_3", 10),])  #564:             return [
    if not _coconut_case_match_check_21:  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
        _coconut_match_set_name_ch = _coconut_sentinel  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
        _coconut_match_set_name_shape = _coconut_sentinel  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
        _coconut_match_set_name_other = _coconut_sentinel  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
        _coconut_match_set_name_kwargs = _coconut_sentinel  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
        if _coconut.isinstance(_coconut_case_match_to_21, _coconut.abc.Mapping):  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
            _coconut_match_temp_436 = _coconut_case_match_to_21.get("type", _coconut_sentinel)  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
            _coconut_match_temp_437 = _coconut_case_match_to_21.get("arrange", _coconut_sentinel)  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
            _coconut_match_temp_438 = _coconut_case_match_to_21.get("ch_rpr", _coconut_sentinel)  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
            _coconut_match_temp_439 = _coconut_case_match_to_21.get("meta", _coconut_sentinel)  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
            if (_coconut_match_temp_436 is not _coconut_sentinel) and (_coconut_match_temp_436 == "numpy") and (_coconut_match_temp_437 is not _coconut_sentinel) and (_coconut_match_temp_437 == "HWC") and (_coconut_match_temp_438 is not _coconut_sentinel) and (_coconut_match_temp_439 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_439, _coconut.abc.Mapping)):  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
                _coconut_match_set_name_ch = _coconut_match_temp_438  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
                _coconut_match_temp_440 = _coconut_match_temp_439.get("shape", _coconut_sentinel)  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
                _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_21.items() if k not in _coconut.set(("type", "arrange", "ch_rpr", "meta")))  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
                if _coconut_match_temp_440 is not _coconut_sentinel:  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
                    _coconut_match_set_name_shape = _coconut_match_temp_440  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
                    _coconut_match_set_name_other = _coconut.dict((k, v) for k, v in _coconut_match_temp_439.items() if k not in _coconut.set(("shape",)))  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
                    _coconut_case_match_check_21 = True  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
        if _coconut_case_match_check_21:  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
            if _coconut_match_set_name_ch is not _coconut_sentinel:  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
                ch = _coconut_match_set_name_ch  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
            if _coconut_match_set_name_shape is not _coconut_sentinel:  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
                shape = _coconut_match_set_name_shape  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
            if _coconut_match_set_name_other is not _coconut_sentinel:  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
                other = _coconut_match_set_name_other  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
            if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
                kwargs = _coconut_match_set_name_kwargs  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
        if _coconut_case_match_check_21 and not (len(ch_splitter(ch)) == 1):  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
            _coconut_case_match_check_21 = False  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
        if _coconut_case_match_check_21:  #577:         match {"type":"numpy","arrange":"HWC","ch_rpr":ch,"meta":{"shape":shape,**other},**kwargs} if len(ch_splitter(ch)) == 1:
            return ([(lambda a: a[:, :, [0, 0, 0]], fdict(type="numpy", arrange="HWC", ch_rpr=ch * 3, meta=fdict(_coconut_dict_merge(_coconut.dict((("shape", (shape[0], shape[1], 3)),)), other)), **kwargs), "numpy_repeat_channel_3", 10),])  #578:             return [




def lll_is_rgb(state):  #593: def lll_is_rgb(state):
    _coconut_case_match_to_22 = state  #594:     case state:
    _coconut_case_match_check_22 = False  #594:     case state:
    _coconut_match_set_name_kwargs = _coconut_sentinel  #594:     case state:
    if _coconut.isinstance(_coconut_case_match_to_22, _coconut.abc.Mapping):  #594:     case state:
        _coconut_match_temp_441 = _coconut_case_match_to_22.get("ch_rpr", _coconut_sentinel)  #594:     case state:
        if (_coconut_match_temp_441 is not _coconut_sentinel) and (_coconut_match_temp_441 == "LLL"):  #594:     case state:
            _coconut_match_set_name_kwargs = _coconut.dict((k, v) for k, v in _coconut_case_match_to_22.items() if k not in _coconut.set(("ch_rpr",)))  #594:     case state:
            _coconut_case_match_check_22 = True  #594:     case state:
    if _coconut_case_match_check_22:  #594:     case state:
        if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #594:     case state:
            kwargs = _coconut_match_set_name_kwargs  #594:     case state:
    if _coconut_case_match_check_22:  #594:     case state:
        return ([frozendict(ch_rpr="RGB", **kwargs),])  #596:             return [frozendict(ch_rpr="RGB",**kwargs)]




def debug(conv):  #600: def debug(conv):
    from IPython import embed  #601:     from IPython import embed
    n = conv.edges[-1]  #602:     n = conv.edges[-1]
    matched = False  #603:     matched = False
    _coconut_case_match_to_23 = (n.src, n.dst)  #604:     case (n.src,n.dst):
    _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
    if (_coconut.isinstance(_coconut_case_match_to_23, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_23) == 2):  #604:     case (n.src,n.dst):
        _coconut_match_temp_442 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
            if (_coconut_match_temp_442) and (_coconut.isinstance(_coconut_case_match_to_23[1], AutoList)) and (_coconut.len(_coconut_case_match_to_23[1]) >= 1):  #604:     case (n.src,n.dst):
                _coconut_match_temp_443 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                _coconut_match_temp_459 = _coconut.len(_coconut_case_match_to_23[1]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_23[1].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_23[1], "_coconut_data_defaults", {}) and _coconut_case_match_to_23[1][i] == _coconut.getattr(_coconut_case_match_to_23[1], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_23[1].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_23[1], "__match_args__") else _coconut.len(_coconut_case_match_to_23[1]) == 1  # type: ignore  #604:     case (n.src,n.dst):
                if _coconut_match_temp_459:  #604:     case (n.src,n.dst):
                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                    if (_coconut_match_temp_443) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], AutoList)) and (_coconut.len(_coconut_case_match_to_23[1][0]) >= 1):  #604:     case (n.src,n.dst):
                        _coconut_match_temp_444 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                        _coconut_match_temp_448 = _coconut.len(_coconut_case_match_to_23[1][0]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_23[1][0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_23[1][0], "_coconut_data_defaults", {}) and _coconut_case_match_to_23[1][0][i] == _coconut.getattr(_coconut_case_match_to_23[1][0], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_23[1][0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_23[1][0], "__match_args__") else _coconut.len(_coconut_case_match_to_23[1][0]) == 1  # type: ignore  #604:     case (n.src,n.dst):
                        if _coconut_match_temp_448:  #604:     case (n.src,n.dst):
                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                            if (_coconut_match_temp_444) and (_coconut.isinstance(_coconut_case_match_to_23[1][0][0], AutoList)) and (_coconut.len(_coconut_case_match_to_23[1][0][0]) >= 1):  #604:     case (n.src,n.dst):
                                _coconut_match_temp_445 = _coconut.len(_coconut_case_match_to_23[1][0][0]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_23[1][0][0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_23[1][0][0], "_coconut_data_defaults", {}) and _coconut_case_match_to_23[1][0][0][i] == _coconut.getattr(_coconut_case_match_to_23[1][0][0], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_23[1][0][0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_23[1][0][0], "__match_args__") else _coconut.len(_coconut_case_match_to_23[1][0][0]) == 1  # type: ignore  #604:     case (n.src,n.dst):
                                if _coconut_match_temp_445:  #604:     case (n.src,n.dst):
                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                            if (not _coconut_match_temp_444) and (_coconut.isinstance(_coconut_case_match_to_23[1][0][0], AutoList)):  #604:     case (n.src,n.dst):
                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if _coconut.type(_coconut_case_match_to_23[1][0][0]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if not _coconut.type(_coconut_case_match_to_23[1][0][0]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_446 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                        if not _coconut.isinstance(_coconut_match_temp_446, _coconut.tuple):  #604:     case (n.src,n.dst):
                                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                        if _coconut.len(_coconut_match_temp_446) < 1:  #604:     case (n.src,n.dst):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_446),))  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_447 = _coconut.getattr(_coconut_case_match_to_23[1][0][0], _coconut_match_temp_446[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                        if _coconut_match_temp_447 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):





                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                    if (not _coconut_match_temp_443) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], AutoList)):  #604:     case (n.src,n.dst):
                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                            if _coconut.type(_coconut_case_match_to_23[1][0]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                _coconut_match_temp_449 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if (_coconut_match_temp_449) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], AutoList)) and (_coconut.len(_coconut_case_match_to_23[1][0]) >= 1):  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_450 = _coconut.len(_coconut_case_match_to_23[1][0]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_23[1][0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_23[1][0], "_coconut_data_defaults", {}) and _coconut_case_match_to_23[1][0][i] == _coconut.getattr(_coconut_case_match_to_23[1][0], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_23[1][0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_23[1][0], "__match_args__") else _coconut.len(_coconut_case_match_to_23[1][0]) == 1  # type: ignore  #604:     case (n.src,n.dst):
                                        if _coconut_match_temp_450:  #604:     case (n.src,n.dst):
                                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if (not _coconut_match_temp_449) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], AutoList)):  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if _coconut.type(_coconut_case_match_to_23[1][0]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if not _coconut.type(_coconut_case_match_to_23[1][0]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_451 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                                if not _coconut.isinstance(_coconut_match_temp_451, _coconut.tuple):  #604:     case (n.src,n.dst):
                                                    raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                                if _coconut.len(_coconut_match_temp_451) < 1:  #604:     case (n.src,n.dst):
                                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_451),))  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_452 = _coconut.getattr(_coconut_case_match_to_23[1][0], _coconut_match_temp_451[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                                if _coconut_match_temp_452 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):





                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                            if not _coconut.type(_coconut_case_match_to_23[1][0]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                _coconut_match_temp_453 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                if not _coconut.isinstance(_coconut_match_temp_453, _coconut.tuple):  #604:     case (n.src,n.dst):
                                    raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                if _coconut.len(_coconut_match_temp_453) < 1:  #604:     case (n.src,n.dst):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_453),))  #604:     case (n.src,n.dst):
                                _coconut_match_temp_454 = _coconut.getattr(_coconut_case_match_to_23[1][0], _coconut_match_temp_453[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                if _coconut_match_temp_454 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                    _coconut_match_temp_455 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if (_coconut_match_temp_455) and (_coconut.isinstance(_coconut_match_temp_454, AutoList)) and (_coconut.len(_coconut_match_temp_454) >= 1):  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_456 = _coconut.len(_coconut_match_temp_454) <= _coconut.max(1, _coconut.len(_coconut_match_temp_454.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_454, "_coconut_data_defaults", {}) and _coconut_match_temp_454[i] == _coconut.getattr(_coconut_match_temp_454, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_454.__match_args__))) if _coconut.hasattr(_coconut_match_temp_454, "__match_args__") else _coconut.len(_coconut_match_temp_454) == 1  # type: ignore  #604:     case (n.src,n.dst):
                                        if _coconut_match_temp_456:  #604:     case (n.src,n.dst):
                                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if (not _coconut_match_temp_455) and (_coconut.isinstance(_coconut_match_temp_454, AutoList)):  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if _coconut.type(_coconut_match_temp_454) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if not _coconut.type(_coconut_match_temp_454) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_457 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                                if not _coconut.isinstance(_coconut_match_temp_457, _coconut.tuple):  #604:     case (n.src,n.dst):
                                                    raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                                if _coconut.len(_coconut_match_temp_457) < 1:  #604:     case (n.src,n.dst):
                                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_457),))  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_458 = _coconut.getattr(_coconut_match_temp_454, _coconut_match_temp_457[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                                if _coconut_match_temp_458 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):









        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
            if (not _coconut_match_temp_442) and (_coconut.isinstance(_coconut_case_match_to_23[1], AutoList)):  #604:     case (n.src,n.dst):
                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                    if _coconut.type(_coconut_case_match_to_23[1]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                        _coconut_match_temp_460 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                            if (_coconut_match_temp_460) and (_coconut.isinstance(_coconut_case_match_to_23[1], AutoList)) and (_coconut.len(_coconut_case_match_to_23[1]) >= 1):  #604:     case (n.src,n.dst):
                                _coconut_match_temp_461 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                                _coconut_match_temp_465 = _coconut.len(_coconut_case_match_to_23[1]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_23[1].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_23[1], "_coconut_data_defaults", {}) and _coconut_case_match_to_23[1][i] == _coconut.getattr(_coconut_case_match_to_23[1], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_23[1].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_23[1], "__match_args__") else _coconut.len(_coconut_case_match_to_23[1]) == 1  # type: ignore  #604:     case (n.src,n.dst):
                                if _coconut_match_temp_465:  #604:     case (n.src,n.dst):
                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if (_coconut_match_temp_461) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], AutoList)) and (_coconut.len(_coconut_case_match_to_23[1][0]) >= 1):  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_462 = _coconut.len(_coconut_case_match_to_23[1][0]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_23[1][0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_23[1][0], "_coconut_data_defaults", {}) and _coconut_case_match_to_23[1][0][i] == _coconut.getattr(_coconut_case_match_to_23[1][0], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_23[1][0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_23[1][0], "__match_args__") else _coconut.len(_coconut_case_match_to_23[1][0]) == 1  # type: ignore  #604:     case (n.src,n.dst):
                                        if _coconut_match_temp_462:  #604:     case (n.src,n.dst):
                                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if (not _coconut_match_temp_461) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], AutoList)):  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if _coconut.type(_coconut_case_match_to_23[1][0]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if not _coconut.type(_coconut_case_match_to_23[1][0]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_463 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                                if not _coconut.isinstance(_coconut_match_temp_463, _coconut.tuple):  #604:     case (n.src,n.dst):
                                                    raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                                if _coconut.len(_coconut_match_temp_463) < 1:  #604:     case (n.src,n.dst):
                                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_463),))  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_464 = _coconut.getattr(_coconut_case_match_to_23[1][0], _coconut_match_temp_463[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                                if _coconut_match_temp_464 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):





                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                            if (not _coconut_match_temp_460) and (_coconut.isinstance(_coconut_case_match_to_23[1], AutoList)):  #604:     case (n.src,n.dst):
                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if _coconut.type(_coconut_case_match_to_23[1]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_466 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if (_coconut_match_temp_466) and (_coconut.isinstance(_coconut_case_match_to_23[1], AutoList)) and (_coconut.len(_coconut_case_match_to_23[1]) >= 1):  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_467 = _coconut.len(_coconut_case_match_to_23[1]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_23[1].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_23[1], "_coconut_data_defaults", {}) and _coconut_case_match_to_23[1][i] == _coconut.getattr(_coconut_case_match_to_23[1], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_23[1].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_23[1], "__match_args__") else _coconut.len(_coconut_case_match_to_23[1]) == 1  # type: ignore  #604:     case (n.src,n.dst):
                                                if _coconut_match_temp_467:  #604:     case (n.src,n.dst):
                                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if (not _coconut_match_temp_466) and (_coconut.isinstance(_coconut_case_match_to_23[1], AutoList)):  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                    if _coconut.type(_coconut_case_match_to_23[1]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                    if not _coconut.type(_coconut_case_match_to_23[1]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                        _coconut_match_temp_468 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                                        if not _coconut.isinstance(_coconut_match_temp_468, _coconut.tuple):  #604:     case (n.src,n.dst):
                                                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                                        if _coconut.len(_coconut_match_temp_468) < 1:  #604:     case (n.src,n.dst):
                                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_468),))  #604:     case (n.src,n.dst):
                                                        _coconut_match_temp_469 = _coconut.getattr(_coconut_case_match_to_23[1], _coconut_match_temp_468[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                                        if _coconut_match_temp_469 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):





                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if not _coconut.type(_coconut_case_match_to_23[1]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_470 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                        if not _coconut.isinstance(_coconut_match_temp_470, _coconut.tuple):  #604:     case (n.src,n.dst):
                                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                        if _coconut.len(_coconut_match_temp_470) < 1:  #604:     case (n.src,n.dst):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_470),))  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_471 = _coconut.getattr(_coconut_case_match_to_23[1], _coconut_match_temp_470[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                        if _coconut_match_temp_471 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                            _coconut_match_temp_472 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if (_coconut_match_temp_472) and (_coconut.isinstance(_coconut_match_temp_471, AutoList)) and (_coconut.len(_coconut_match_temp_471) >= 1):  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_473 = _coconut.len(_coconut_match_temp_471) <= _coconut.max(1, _coconut.len(_coconut_match_temp_471.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_471, "_coconut_data_defaults", {}) and _coconut_match_temp_471[i] == _coconut.getattr(_coconut_match_temp_471, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_471.__match_args__))) if _coconut.hasattr(_coconut_match_temp_471, "__match_args__") else _coconut.len(_coconut_match_temp_471) == 1  # type: ignore  #604:     case (n.src,n.dst):
                                                if _coconut_match_temp_473:  #604:     case (n.src,n.dst):
                                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if (not _coconut_match_temp_472) and (_coconut.isinstance(_coconut_match_temp_471, AutoList)):  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                    if _coconut.type(_coconut_match_temp_471) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                    if not _coconut.type(_coconut_match_temp_471) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                        _coconut_match_temp_474 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                                        if not _coconut.isinstance(_coconut_match_temp_474, _coconut.tuple):  #604:     case (n.src,n.dst):
                                                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                                        if _coconut.len(_coconut_match_temp_474) < 1:  #604:     case (n.src,n.dst):
                                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_474),))  #604:     case (n.src,n.dst):
                                                        _coconut_match_temp_475 = _coconut.getattr(_coconut_match_temp_471, _coconut_match_temp_474[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                                        if _coconut_match_temp_475 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):









                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                    if not _coconut.type(_coconut_case_match_to_23[1]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                        _coconut_match_temp_476 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                        if not _coconut.isinstance(_coconut_match_temp_476, _coconut.tuple):  #604:     case (n.src,n.dst):
                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                        if _coconut.len(_coconut_match_temp_476) < 1:  #604:     case (n.src,n.dst):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_476),))  #604:     case (n.src,n.dst):
                        _coconut_match_temp_477 = _coconut.getattr(_coconut_case_match_to_23[1], _coconut_match_temp_476[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                        if _coconut_match_temp_477 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                            _coconut_match_temp_478 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                            if (_coconut_match_temp_478) and (_coconut.isinstance(_coconut_match_temp_477, AutoList)) and (_coconut.len(_coconut_match_temp_477) >= 1):  #604:     case (n.src,n.dst):
                                _coconut_match_temp_479 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                                _coconut_match_temp_483 = _coconut.len(_coconut_match_temp_477) <= _coconut.max(1, _coconut.len(_coconut_match_temp_477.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_477, "_coconut_data_defaults", {}) and _coconut_match_temp_477[i] == _coconut.getattr(_coconut_match_temp_477, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_477.__match_args__))) if _coconut.hasattr(_coconut_match_temp_477, "__match_args__") else _coconut.len(_coconut_match_temp_477) == 1  # type: ignore  #604:     case (n.src,n.dst):
                                if _coconut_match_temp_483:  #604:     case (n.src,n.dst):
                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if (_coconut_match_temp_479) and (_coconut.isinstance(_coconut_match_temp_477[0], AutoList)) and (_coconut.len(_coconut_match_temp_477[0]) >= 1):  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_480 = _coconut.len(_coconut_match_temp_477[0]) <= _coconut.max(1, _coconut.len(_coconut_match_temp_477[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_477[0], "_coconut_data_defaults", {}) and _coconut_match_temp_477[0][i] == _coconut.getattr(_coconut_match_temp_477[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_477[0].__match_args__))) if _coconut.hasattr(_coconut_match_temp_477[0], "__match_args__") else _coconut.len(_coconut_match_temp_477[0]) == 1  # type: ignore  #604:     case (n.src,n.dst):
                                        if _coconut_match_temp_480:  #604:     case (n.src,n.dst):
                                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if (not _coconut_match_temp_479) and (_coconut.isinstance(_coconut_match_temp_477[0], AutoList)):  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if _coconut.type(_coconut_match_temp_477[0]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if not _coconut.type(_coconut_match_temp_477[0]) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_481 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                                if not _coconut.isinstance(_coconut_match_temp_481, _coconut.tuple):  #604:     case (n.src,n.dst):
                                                    raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                                if _coconut.len(_coconut_match_temp_481) < 1:  #604:     case (n.src,n.dst):
                                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_481),))  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_482 = _coconut.getattr(_coconut_match_temp_477[0], _coconut_match_temp_481[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                                if _coconut_match_temp_482 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):





                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                            if (not _coconut_match_temp_478) and (_coconut.isinstance(_coconut_match_temp_477, AutoList)):  #604:     case (n.src,n.dst):
                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if _coconut.type(_coconut_match_temp_477) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_484 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if (_coconut_match_temp_484) and (_coconut.isinstance(_coconut_match_temp_477, AutoList)) and (_coconut.len(_coconut_match_temp_477) >= 1):  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_485 = _coconut.len(_coconut_match_temp_477) <= _coconut.max(1, _coconut.len(_coconut_match_temp_477.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_477, "_coconut_data_defaults", {}) and _coconut_match_temp_477[i] == _coconut.getattr(_coconut_match_temp_477, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_477.__match_args__))) if _coconut.hasattr(_coconut_match_temp_477, "__match_args__") else _coconut.len(_coconut_match_temp_477) == 1  # type: ignore  #604:     case (n.src,n.dst):
                                                if _coconut_match_temp_485:  #604:     case (n.src,n.dst):
                                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if (not _coconut_match_temp_484) and (_coconut.isinstance(_coconut_match_temp_477, AutoList)):  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                    if _coconut.type(_coconut_match_temp_477) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                    if not _coconut.type(_coconut_match_temp_477) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                        _coconut_match_temp_486 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                                        if not _coconut.isinstance(_coconut_match_temp_486, _coconut.tuple):  #604:     case (n.src,n.dst):
                                                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                                        if _coconut.len(_coconut_match_temp_486) < 1:  #604:     case (n.src,n.dst):
                                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_486),))  #604:     case (n.src,n.dst):
                                                        _coconut_match_temp_487 = _coconut.getattr(_coconut_match_temp_477, _coconut_match_temp_486[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                                        if _coconut_match_temp_487 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):





                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                    if not _coconut.type(_coconut_match_temp_477) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_488 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                        if not _coconut.isinstance(_coconut_match_temp_488, _coconut.tuple):  #604:     case (n.src,n.dst):
                                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                        if _coconut.len(_coconut_match_temp_488) < 1:  #604:     case (n.src,n.dst):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_488),))  #604:     case (n.src,n.dst):
                                        _coconut_match_temp_489 = _coconut.getattr(_coconut_match_temp_477, _coconut_match_temp_488[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                        if _coconut_match_temp_489 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                            _coconut_match_temp_490 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #604:     case (n.src,n.dst):
                                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                        _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if (_coconut_match_temp_490) and (_coconut.isinstance(_coconut_match_temp_489, AutoList)) and (_coconut.len(_coconut_match_temp_489) >= 1):  #604:     case (n.src,n.dst):
                                                _coconut_match_temp_491 = _coconut.len(_coconut_match_temp_489) <= _coconut.max(1, _coconut.len(_coconut_match_temp_489.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_489, "_coconut_data_defaults", {}) and _coconut_match_temp_489[i] == _coconut.getattr(_coconut_match_temp_489, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_489.__match_args__))) if _coconut.hasattr(_coconut_match_temp_489, "__match_args__") else _coconut.len(_coconut_match_temp_489) == 1  # type: ignore  #604:     case (n.src,n.dst):
                                                if _coconut_match_temp_491:  #604:     case (n.src,n.dst):
                                                    _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                        if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                            if (not _coconut_match_temp_490) and (_coconut.isinstance(_coconut_match_temp_489, AutoList)):  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):
                                            if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                _coconut_case_match_check_23 = False  #604:     case (n.src,n.dst):
                                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                    if _coconut.type(_coconut_match_temp_489) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                        _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):

                                                if not _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
                                                    if not _coconut.type(_coconut_match_temp_489) in _coconut_self_match_types:  #604:     case (n.src,n.dst):
                                                        _coconut_match_temp_492 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #604:     case (n.src,n.dst):
                                                        if not _coconut.isinstance(_coconut_match_temp_492, _coconut.tuple):  #604:     case (n.src,n.dst):
                                                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #604:     case (n.src,n.dst):
                                                        if _coconut.len(_coconut_match_temp_492) < 1:  #604:     case (n.src,n.dst):
                                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_492),))  #604:     case (n.src,n.dst):
                                                        _coconut_match_temp_493 = _coconut.getattr(_coconut_match_temp_489, _coconut_match_temp_492[0], _coconut_sentinel)  #604:     case (n.src,n.dst):
                                                        if _coconut_match_temp_493 is not _coconut_sentinel:  #604:     case (n.src,n.dst):
                                                            _coconut_case_match_check_23 = True  #604:     case (n.src,n.dst):












    if _coconut_case_match_check_23:  #604:     case (n.src,n.dst):
        logger.warning("debugging nested autolist".format())  #606:             logger.warning(f"debugging nested autolist")
        matched = True  #607:             matched = True
    if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
        if (_coconut.isinstance(_coconut_case_match_to_23, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_23) == 2):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
            _coconut_match_temp_494 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
            _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
        if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
            _coconut_case_match_check_23 = False  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
            if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                _coconut_match_set_name_s = _coconut_sentinel  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                if (_coconut_match_temp_494) and (_coconut.isinstance(_coconut_case_match_to_23[1], ImageDef)) and (_coconut.len(_coconut_case_match_to_23[1]) >= 2) and (_coconut.isinstance(_coconut_case_match_to_23[1][1], _coconut.abc.Mapping)):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                    _coconut_match_temp_495 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                    _coconut_match_temp_501 = _coconut_case_match_to_23[1][1].get("shape", _coconut_sentinel)  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                    _coconut_match_temp_502 = _coconut.len(_coconut_case_match_to_23[1]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_23[1].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_23[1], "_coconut_data_defaults", {}) and _coconut_case_match_to_23[1][i] == _coconut.getattr(_coconut_case_match_to_23[1], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_23[1].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_23[1], "__match_args__") else _coconut.len(_coconut_case_match_to_23[1]) == 2  # type: ignore  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                    if (_coconut_match_temp_501 is not _coconut_sentinel) and (_coconut_match_temp_502):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        _coconut_match_set_name_s = _coconut_match_temp_501  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                    _coconut_case_match_check_23 = False  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                    if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        _coconut_match_set_name_arng = _coconut_sentinel  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        if (_coconut_match_temp_495) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], TensorLike)) and (_coconut.len(_coconut_case_match_to_23[1][0]) >= 2):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            _coconut_match_set_name_arng = _coconut_case_match_to_23[1][0][1]  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            if _coconut_match_set_name_arng is not _coconut_sentinel:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                arng = _coconut_match_set_name_arng  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):

                    if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        if (not _coconut_match_temp_495) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], TensorLike)):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            _coconut_match_temp_500 = _coconut.getattr(TensorLike, '__match_args__', ())  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            _coconut_match_temp_499 = _coconut.tuple(_coconut.getattr(_coconut_case_match_to_23[1][0], _coconut_match_temp_500[i]) for i in _coconut.range(2, _coconut.len(_coconut_match_temp_500)))  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            _coconut_case_match_check_23 = False  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                if _coconut.type(_coconut_case_match_to_23[1][0]) in _coconut_self_match_types:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports 1)")  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):

                            if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                _coconut_match_set_name_arng = _coconut_sentinel  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                if not _coconut.type(_coconut_case_match_to_23[1][0]) in _coconut_self_match_types:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_match_temp_496 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    if not _coconut.isinstance(_coconut_match_temp_496, _coconut.tuple):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                        raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    if _coconut.len(_coconut_match_temp_496) < 2:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_496),))  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_match_temp_497 = _coconut.getattr(_coconut_case_match_to_23[1][0], _coconut_match_temp_496[0], _coconut_sentinel)  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_match_temp_498 = _coconut.getattr(_coconut_case_match_to_23[1][0], _coconut_match_temp_496[1], _coconut_sentinel)  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    if (_coconut_match_temp_497 is not _coconut_sentinel) and (_coconut_match_temp_498 is not _coconut_sentinel):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                        _coconut_match_set_name_arng = _coconut_match_temp_498  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                        _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    if _coconut_match_set_name_arng is not _coconut_sentinel:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                        arng = _coconut_match_set_name_arng  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):




                if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                    if _coconut_match_set_name_s is not _coconut_sentinel:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        s = _coconut_match_set_name_s  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):

            if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                if (not _coconut_match_temp_494) and (_coconut.isinstance(_coconut_case_match_to_23[1], ImageDef)):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                    _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                    _coconut_case_match_check_23 = False  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                    if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        if _coconut.type(_coconut_case_match_to_23[1]) in _coconut_self_match_types:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):

                    if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        _coconut_match_set_name_s = _coconut_sentinel  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        if not _coconut.type(_coconut_case_match_to_23[1]) in _coconut_self_match_types:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            _coconut_match_temp_503 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            if not _coconut.isinstance(_coconut_match_temp_503, _coconut.tuple):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            if _coconut.len(_coconut_match_temp_503) < 2:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_503),))  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            _coconut_match_temp_504 = _coconut.getattr(_coconut_case_match_to_23[1], _coconut_match_temp_503[0], _coconut_sentinel)  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            _coconut_match_temp_511 = _coconut.getattr(_coconut_case_match_to_23[1], _coconut_match_temp_503[1], _coconut_sentinel)  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            if (_coconut_match_temp_504 is not _coconut_sentinel) and (_coconut_match_temp_511 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_511, _coconut.abc.Mapping)):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                _coconut_match_temp_505 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                _coconut_match_temp_512 = _coconut_match_temp_511.get("shape", _coconut_sentinel)  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                if _coconut_match_temp_512 is not _coconut_sentinel:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_match_set_name_s = _coconut_match_temp_512  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                        if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            _coconut_case_match_check_23 = False  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                _coconut_match_set_name_arng = _coconut_sentinel  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                if (_coconut_match_temp_505) and (_coconut.isinstance(_coconut_match_temp_504, TensorLike)) and (_coconut.len(_coconut_match_temp_504) >= 2):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_match_set_name_arng = _coconut_match_temp_504[1]  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    if _coconut_match_set_name_arng is not _coconut_sentinel:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                        arng = _coconut_match_set_name_arng  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):

                            if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                if (not _coconut_match_temp_505) and (_coconut.isinstance(_coconut_match_temp_504, TensorLike)):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_match_temp_510 = _coconut.getattr(TensorLike, '__match_args__', ())  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_match_temp_509 = _coconut.tuple(_coconut.getattr(_coconut_match_temp_504, _coconut_match_temp_510[i]) for i in _coconut.range(2, _coconut.len(_coconut_match_temp_510)))  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    _coconut_case_match_check_23 = False  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                    if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                        if _coconut.type(_coconut_match_temp_504) in _coconut_self_match_types:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports 1)")  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                            _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):

                                    if not _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                        _coconut_match_set_name_arng = _coconut_sentinel  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                        if not _coconut.type(_coconut_match_temp_504) in _coconut_self_match_types:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                            _coconut_match_temp_506 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                            if not _coconut.isinstance(_coconut_match_temp_506, _coconut.tuple):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                                raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                            if _coconut.len(_coconut_match_temp_506) < 2:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_506),))  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                            _coconut_match_temp_507 = _coconut.getattr(_coconut_match_temp_504, _coconut_match_temp_506[0], _coconut_sentinel)  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                            _coconut_match_temp_508 = _coconut.getattr(_coconut_match_temp_504, _coconut_match_temp_506[1], _coconut_sentinel)  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                            if (_coconut_match_temp_507 is not _coconut_sentinel) and (_coconut_match_temp_508 is not _coconut_sentinel):  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                                _coconut_match_set_name_arng = _coconut_match_temp_508  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                                _coconut_case_match_check_23 = True  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                        if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                            if _coconut_match_set_name_arng is not _coconut_sentinel:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                                arng = _coconut_match_set_name_arng  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):




                        if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                            if _coconut_match_set_name_s is not _coconut_sentinel:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
                                s = _coconut_match_set_name_s  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):




        if _coconut_case_match_check_23:  #608:         match (_,ImageDef(TensorLike(_,arng,*_),{"shape":s,**_})):
            if len(arng) != len(s):  #609:             if len(arng) != len(s):
                logger.warning("debug console for omni_converter".format())  #610:                 logger.warning(f"debug console for omni_converter")
                matched = True  #611:                 matched =True
    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
        if (_coconut.isinstance(_coconut_case_match_to_23, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_23) == 2):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            _coconut_match_temp_513 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            _coconut_match_temp_532 = _coconut.getattr(ImageDef, "_coconut_is_data", False) or _coconut.isinstance(ImageDef, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in ImageDef)  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                _coconut_match_set_name_s1 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                if (_coconut_match_temp_513) and (_coconut.isinstance(_coconut_case_match_to_23[0], ImageDef)) and (_coconut.len(_coconut_case_match_to_23[0]) >= 2) and (_coconut.isinstance(_coconut_case_match_to_23[0][1], _coconut.abc.Mapping)):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_match_temp_514 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_match_temp_520 = _coconut_case_match_to_23[0][1].get("shape", _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_match_temp_521 = _coconut.len(_coconut_case_match_to_23[0]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_23[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_23[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_23[0][i] == _coconut.getattr(_coconut_case_match_to_23[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_23[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_23[0], "__match_args__") else _coconut.len(_coconut_case_match_to_23[0]) == 2  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    if (_coconut_match_temp_520 is not _coconut_sentinel) and (_coconut_match_temp_521):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        _coconut_match_set_name_s1 = _coconut_match_temp_520  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        _coconut_match_set_name_arng1 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if (_coconut_match_temp_514) and (_coconut.isinstance(_coconut_case_match_to_23[0][0], TensorLike)) and (_coconut.len(_coconut_case_match_to_23[0][0]) >= 2):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_set_name_arng1 = _coconut_case_match_to_23[0][0][1]  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if _coconut_match_set_name_arng1 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                arng1 = _coconut_match_set_name_arng1  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if (not _coconut_match_temp_514) and (_coconut.isinstance(_coconut_case_match_to_23[0][0], TensorLike)):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_temp_519 = _coconut.getattr(TensorLike, '__match_args__', ())  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_temp_518 = _coconut.tuple(_coconut.getattr(_coconut_case_match_to_23[0][0], _coconut_match_temp_519[i]) for i in _coconut.range(2, _coconut.len(_coconut_match_temp_519)))  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if _coconut.type(_coconut_case_match_to_23[0][0]) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports 1)")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

                            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                _coconut_match_set_name_arng1 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if not _coconut.type(_coconut_case_match_to_23[0][0]) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_temp_515 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if not _coconut.isinstance(_coconut_match_temp_515, _coconut.tuple):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if _coconut.len(_coconut_match_temp_515) < 2:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_515),))  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_temp_516 = _coconut.getattr(_coconut_case_match_to_23[0][0], _coconut_match_temp_515[0], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_temp_517 = _coconut.getattr(_coconut_case_match_to_23[0][0], _coconut_match_temp_515[1], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if (_coconut_match_temp_516 is not _coconut_sentinel) and (_coconut_match_temp_517 is not _coconut_sentinel):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        _coconut_match_set_name_arng1 = _coconut_match_temp_517  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if _coconut_match_set_name_arng1 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        arng1 = _coconut_match_set_name_arng1  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):




                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    if _coconut_match_set_name_s1 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        s1 = _coconut_match_set_name_s1  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                if (not _coconut_match_temp_513) and (_coconut.isinstance(_coconut_case_match_to_23[0], ImageDef)):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if _coconut.type(_coconut_case_match_to_23[0]) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        _coconut_match_set_name_s1 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if not _coconut.type(_coconut_case_match_to_23[0]) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_temp_522 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if not _coconut.isinstance(_coconut_match_temp_522, _coconut.tuple):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if _coconut.len(_coconut_match_temp_522) < 2:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_522),))  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_temp_523 = _coconut.getattr(_coconut_case_match_to_23[0], _coconut_match_temp_522[0], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_temp_530 = _coconut.getattr(_coconut_case_match_to_23[0], _coconut_match_temp_522[1], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if (_coconut_match_temp_523 is not _coconut_sentinel) and (_coconut_match_temp_530 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_530, _coconut.abc.Mapping)):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                _coconut_match_temp_524 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                _coconut_match_temp_531 = _coconut_match_temp_530.get("shape", _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if _coconut_match_temp_531 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_set_name_s1 = _coconut_match_temp_531  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                _coconut_match_set_name_arng1 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if (_coconut_match_temp_524) and (_coconut.isinstance(_coconut_match_temp_523, TensorLike)) and (_coconut.len(_coconut_match_temp_523) >= 2):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_set_name_arng1 = _coconut_match_temp_523[1]  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if _coconut_match_set_name_arng1 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        arng1 = _coconut_match_set_name_arng1  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

                            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if (not _coconut_match_temp_524) and (_coconut.isinstance(_coconut_match_temp_523, TensorLike)):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_temp_529 = _coconut.getattr(TensorLike, '__match_args__', ())  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_temp_528 = _coconut.tuple(_coconut.getattr(_coconut_match_temp_523, _coconut_match_temp_529[i]) for i in _coconut.range(2, _coconut.len(_coconut_match_temp_529)))  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        if _coconut.type(_coconut_match_temp_523) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports 1)")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

                                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        _coconut_match_set_name_arng1 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        if not _coconut.type(_coconut_match_temp_523) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            _coconut_match_temp_525 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            if not _coconut.isinstance(_coconut_match_temp_525, _coconut.tuple):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                                raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            if _coconut.len(_coconut_match_temp_525) < 2:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_525),))  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            _coconut_match_temp_526 = _coconut.getattr(_coconut_match_temp_523, _coconut_match_temp_525[0], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            _coconut_match_temp_527 = _coconut.getattr(_coconut_match_temp_523, _coconut_match_temp_525[1], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            if (_coconut_match_temp_526 is not _coconut_sentinel) and (_coconut_match_temp_527 is not _coconut_sentinel):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                                _coconut_match_set_name_arng1 = _coconut_match_temp_527  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                                _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            if _coconut_match_set_name_arng1 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                                arng1 = _coconut_match_set_name_arng1  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):




                        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if _coconut_match_set_name_s1 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                s1 = _coconut_match_set_name_s1  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):




        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                _coconut_match_set_name_s2 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                if (_coconut_match_temp_532) and (_coconut.isinstance(_coconut_case_match_to_23[1], ImageDef)) and (_coconut.len(_coconut_case_match_to_23[1]) >= 2) and (_coconut.isinstance(_coconut_case_match_to_23[1][1], _coconut.abc.Mapping)):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_match_temp_533 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_match_temp_539 = _coconut_case_match_to_23[1][1].get("shape", _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_match_temp_540 = _coconut.len(_coconut_case_match_to_23[1]) <= _coconut.max(2, _coconut.len(_coconut_case_match_to_23[1].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_23[1], "_coconut_data_defaults", {}) and _coconut_case_match_to_23[1][i] == _coconut.getattr(_coconut_case_match_to_23[1], "_coconut_data_defaults", {})[i] for i in _coconut.range(2, _coconut.len(_coconut_case_match_to_23[1].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_23[1], "__match_args__") else _coconut.len(_coconut_case_match_to_23[1]) == 2  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    if (_coconut_match_temp_539 is not _coconut_sentinel) and (_coconut_match_temp_540):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        _coconut_match_set_name_s2 = _coconut_match_temp_539  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        _coconut_match_set_name_arng2 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if (_coconut_match_temp_533) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], TensorLike)) and (_coconut.len(_coconut_case_match_to_23[1][0]) >= 2):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_set_name_arng2 = _coconut_case_match_to_23[1][0][1]  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if _coconut_match_set_name_arng2 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                arng2 = _coconut_match_set_name_arng2  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if (not _coconut_match_temp_533) and (_coconut.isinstance(_coconut_case_match_to_23[1][0], TensorLike)):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_temp_538 = _coconut.getattr(TensorLike, '__match_args__', ())  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_temp_537 = _coconut.tuple(_coconut.getattr(_coconut_case_match_to_23[1][0], _coconut_match_temp_538[i]) for i in _coconut.range(2, _coconut.len(_coconut_match_temp_538)))  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if _coconut.type(_coconut_case_match_to_23[1][0]) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports 1)")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

                            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                _coconut_match_set_name_arng2 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if not _coconut.type(_coconut_case_match_to_23[1][0]) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_temp_534 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if not _coconut.isinstance(_coconut_match_temp_534, _coconut.tuple):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if _coconut.len(_coconut_match_temp_534) < 2:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_534),))  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_temp_535 = _coconut.getattr(_coconut_case_match_to_23[1][0], _coconut_match_temp_534[0], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_temp_536 = _coconut.getattr(_coconut_case_match_to_23[1][0], _coconut_match_temp_534[1], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if (_coconut_match_temp_535 is not _coconut_sentinel) and (_coconut_match_temp_536 is not _coconut_sentinel):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        _coconut_match_set_name_arng2 = _coconut_match_temp_536  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if _coconut_match_set_name_arng2 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        arng2 = _coconut_match_set_name_arng2  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):




                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    if _coconut_match_set_name_s2 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        s2 = _coconut_match_set_name_s2  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                if (not _coconut_match_temp_532) and (_coconut.isinstance(_coconut_case_match_to_23[1], ImageDef)):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if _coconut.type(_coconut_case_match_to_23[1]) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports 1)")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        _coconut_match_set_name_s2 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if not _coconut.type(_coconut_case_match_to_23[1]) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_temp_541 = _coconut.getattr(ImageDef, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if not _coconut.isinstance(_coconut_match_temp_541, _coconut.tuple):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                raise _coconut.TypeError("ImageDef.__match_args__ must be a tuple")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if _coconut.len(_coconut_match_temp_541) < 2:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'ImageDef' only supports %s)" % (_coconut.len(_coconut_match_temp_541),))  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_temp_542 = _coconut.getattr(_coconut_case_match_to_23[1], _coconut_match_temp_541[0], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_match_temp_549 = _coconut.getattr(_coconut_case_match_to_23[1], _coconut_match_temp_541[1], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if (_coconut_match_temp_542 is not _coconut_sentinel) and (_coconut_match_temp_549 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_549, _coconut.abc.Mapping)):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                _coconut_match_temp_543 = _coconut.getattr(TensorLike, "_coconut_is_data", False) or _coconut.isinstance(TensorLike, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in TensorLike)  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                _coconut_match_temp_550 = _coconut_match_temp_549.get("shape", _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if _coconut_match_temp_550 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_set_name_s2 = _coconut_match_temp_550  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                _coconut_match_set_name_arng2 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if (_coconut_match_temp_543) and (_coconut.isinstance(_coconut_match_temp_542, TensorLike)) and (_coconut.len(_coconut_match_temp_542) >= 2):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_set_name_arng2 = _coconut_match_temp_542[1]  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if _coconut_match_set_name_arng2 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        arng2 = _coconut_match_set_name_arng2  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

                            if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if (not _coconut_match_temp_543) and (_coconut.isinstance(_coconut_match_temp_542, TensorLike)):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_temp_548 = _coconut.getattr(TensorLike, '__match_args__', ())  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_match_temp_547 = _coconut.tuple(_coconut.getattr(_coconut_match_temp_542, _coconut_match_temp_548[i]) for i in _coconut.range(2, _coconut.len(_coconut_match_temp_548)))  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    _coconut_case_match_check_23 = False  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        if _coconut.type(_coconut_match_temp_542) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports 1)")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):

                                    if not _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        _coconut_match_set_name_arng2 = _coconut_sentinel  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        if not _coconut.type(_coconut_match_temp_542) in _coconut_self_match_types:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            _coconut_match_temp_544 = _coconut.getattr(TensorLike, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            if not _coconut.isinstance(_coconut_match_temp_544, _coconut.tuple):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                                raise _coconut.TypeError("TensorLike.__match_args__ must be a tuple")  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            if _coconut.len(_coconut_match_temp_544) < 2:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                                raise _coconut.TypeError("too many positional args in class match (pattern requires 2; 'TensorLike' only supports %s)" % (_coconut.len(_coconut_match_temp_544),))  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            _coconut_match_temp_545 = _coconut.getattr(_coconut_match_temp_542, _coconut_match_temp_544[0], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            _coconut_match_temp_546 = _coconut.getattr(_coconut_match_temp_542, _coconut_match_temp_544[1], _coconut_sentinel)  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            if (_coconut_match_temp_545 is not _coconut_sentinel) and (_coconut_match_temp_546 is not _coconut_sentinel):  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                                _coconut_match_set_name_arng2 = _coconut_match_temp_546  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                                _coconut_case_match_check_23 = True  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                            if _coconut_match_set_name_arng2 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                                arng2 = _coconut_match_set_name_arng2  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):




                        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                            if _coconut_match_set_name_s2 is not _coconut_sentinel:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
                                s2 = _coconut_match_set_name_s2  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):




        if _coconut_case_match_check_23:  #612:         match (ImageDef(TensorLike(_,arng1,*_),{"shape":s1,**_}),ImageDef(TensorLike(_,arng2,*_),{"shape":s2})):
            if (len(arng2) != len(s2)) or (len(arng1) != len(s1)):  #613:             if (len(arng2) != len(s2)) or (len(arng1) != len(s1)):
                logger.warning("debug console for omni_converter".format())  #614:                 logger.warning(f"debug console for omni_converter")
                matched = True  #615:                 matched = True
    if matched:  #616:     if matched:
        embed()  #617:         embed()
        raise RuntimeError("exit")  #618:         raise RuntimeError("exit")
