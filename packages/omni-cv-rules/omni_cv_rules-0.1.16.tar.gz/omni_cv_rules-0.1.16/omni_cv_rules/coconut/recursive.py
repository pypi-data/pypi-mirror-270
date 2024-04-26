#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x3f0b27c7

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

from omni_cv_rules.coconut.omni_converter import AutoList  #1: from omni_cv_rules.coconut.omni_converter import AutoList


def intra_list_conversions(state, neighbors):  #4: def intra_list_conversions(state,neighbors):
    _coconut_case_match_to_0 = state  #5:     case state:
    _coconut_case_match_check_0 = False  #5:     case state:
    _coconut_match_temp_0 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #5:     case state:
    _coconut_case_match_check_0 = True  #5:     case state:
    if _coconut_case_match_check_0:  #5:     case state:
        _coconut_case_match_check_0 = False  #5:     case state:
        if not _coconut_case_match_check_0:  #5:     case state:
            if (_coconut_match_temp_0) and (_coconut.isinstance(_coconut_case_match_to_0, AutoList)) and (_coconut.len(_coconut_case_match_to_0) >= 1):  #5:     case state:
                _coconut_match_temp_1 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #5:     case state:
                _coconut_match_temp_5 = _coconut.len(_coconut_case_match_to_0) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {}) and _coconut_case_match_to_0[i] == _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_0.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0, "__match_args__") else _coconut.len(_coconut_case_match_to_0) == 1  # type: ignore  #5:     case state:
                if _coconut_match_temp_5:  #5:     case state:
                    _coconut_case_match_check_0 = True  #5:     case state:
            if _coconut_case_match_check_0:  #5:     case state:
                _coconut_case_match_check_0 = False  #5:     case state:
                if not _coconut_case_match_check_0:  #5:     case state:
                    if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_case_match_to_0[0], AutoList)) and (_coconut.len(_coconut_case_match_to_0[0]) >= 1):  #5:     case state:
                        _coconut_match_temp_2 = _coconut.len(_coconut_case_match_to_0[0]) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_0[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0[0], "_coconut_data_defaults", {}) and _coconut_case_match_to_0[0][i] == _coconut.getattr(_coconut_case_match_to_0[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_0[0].__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0[0], "__match_args__") else _coconut.len(_coconut_case_match_to_0[0]) == 1  # type: ignore  #5:     case state:
                        if _coconut_match_temp_2:  #5:     case state:
                            _coconut_case_match_check_0 = True  #5:     case state:

                if not _coconut_case_match_check_0:  #5:     case state:
                    if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_case_match_to_0[0], AutoList)):  #5:     case state:
                        _coconut_case_match_check_0 = True  #5:     case state:
                    if _coconut_case_match_check_0:  #5:     case state:
                        _coconut_case_match_check_0 = False  #5:     case state:
                        if not _coconut_case_match_check_0:  #5:     case state:
                            if _coconut.type(_coconut_case_match_to_0[0]) in _coconut_self_match_types:  #5:     case state:
                                _coconut_case_match_check_0 = True  #5:     case state:

                        if not _coconut_case_match_check_0:  #5:     case state:
                            if not _coconut.type(_coconut_case_match_to_0[0]) in _coconut_self_match_types:  #5:     case state:
                                _coconut_match_temp_3 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #5:     case state:
                                if not _coconut.isinstance(_coconut_match_temp_3, _coconut.tuple):  #5:     case state:
                                    raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #5:     case state:
                                if _coconut.len(_coconut_match_temp_3) < 1:  #5:     case state:
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_3),))  #5:     case state:
                                _coconut_match_temp_4 = _coconut.getattr(_coconut_case_match_to_0[0], _coconut_match_temp_3[0], _coconut_sentinel)  #5:     case state:
                                if _coconut_match_temp_4 is not _coconut_sentinel:  #5:     case state:
                                    _coconut_case_match_check_0 = True  #5:     case state:





        if not _coconut_case_match_check_0:  #5:     case state:
            if (not _coconut_match_temp_0) and (_coconut.isinstance(_coconut_case_match_to_0, AutoList)):  #5:     case state:
                _coconut_case_match_check_0 = True  #5:     case state:
            if _coconut_case_match_check_0:  #5:     case state:
                _coconut_case_match_check_0 = False  #5:     case state:
                if not _coconut_case_match_check_0:  #5:     case state:
                    if _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #5:     case state:
                        _coconut_match_temp_6 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #5:     case state:
                        _coconut_case_match_check_0 = True  #5:     case state:
                    if _coconut_case_match_check_0:  #5:     case state:
                        _coconut_case_match_check_0 = False  #5:     case state:
                        if not _coconut_case_match_check_0:  #5:     case state:
                            if (_coconut_match_temp_6) and (_coconut.isinstance(_coconut_case_match_to_0, AutoList)) and (_coconut.len(_coconut_case_match_to_0) >= 1):  #5:     case state:
                                _coconut_match_temp_7 = _coconut.len(_coconut_case_match_to_0) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {}) and _coconut_case_match_to_0[i] == _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_0.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0, "__match_args__") else _coconut.len(_coconut_case_match_to_0) == 1  # type: ignore  #5:     case state:
                                if _coconut_match_temp_7:  #5:     case state:
                                    _coconut_case_match_check_0 = True  #5:     case state:

                        if not _coconut_case_match_check_0:  #5:     case state:
                            if (not _coconut_match_temp_6) and (_coconut.isinstance(_coconut_case_match_to_0, AutoList)):  #5:     case state:
                                _coconut_case_match_check_0 = True  #5:     case state:
                            if _coconut_case_match_check_0:  #5:     case state:
                                _coconut_case_match_check_0 = False  #5:     case state:
                                if not _coconut_case_match_check_0:  #5:     case state:
                                    if _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #5:     case state:
                                        _coconut_case_match_check_0 = True  #5:     case state:

                                if not _coconut_case_match_check_0:  #5:     case state:
                                    if not _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #5:     case state:
                                        _coconut_match_temp_8 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #5:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_8, _coconut.tuple):  #5:     case state:
                                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #5:     case state:
                                        if _coconut.len(_coconut_match_temp_8) < 1:  #5:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_8),))  #5:     case state:
                                        _coconut_match_temp_9 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_8[0], _coconut_sentinel)  #5:     case state:
                                        if _coconut_match_temp_9 is not _coconut_sentinel:  #5:     case state:
                                            _coconut_case_match_check_0 = True  #5:     case state:





                if not _coconut_case_match_check_0:  #5:     case state:
                    if not _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #5:     case state:
                        _coconut_match_temp_10 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #5:     case state:
                        if not _coconut.isinstance(_coconut_match_temp_10, _coconut.tuple):  #5:     case state:
                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #5:     case state:
                        if _coconut.len(_coconut_match_temp_10) < 1:  #5:     case state:
                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_10),))  #5:     case state:
                        _coconut_match_temp_11 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_10[0], _coconut_sentinel)  #5:     case state:
                        if _coconut_match_temp_11 is not _coconut_sentinel:  #5:     case state:
                            _coconut_match_temp_12 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #5:     case state:
                            _coconut_case_match_check_0 = True  #5:     case state:
                    if _coconut_case_match_check_0:  #5:     case state:
                        _coconut_case_match_check_0 = False  #5:     case state:
                        if not _coconut_case_match_check_0:  #5:     case state:
                            if (_coconut_match_temp_12) and (_coconut.isinstance(_coconut_match_temp_11, AutoList)) and (_coconut.len(_coconut_match_temp_11) >= 1):  #5:     case state:
                                _coconut_match_temp_13 = _coconut.len(_coconut_match_temp_11) <= _coconut.max(1, _coconut.len(_coconut_match_temp_11.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_11, "_coconut_data_defaults", {}) and _coconut_match_temp_11[i] == _coconut.getattr(_coconut_match_temp_11, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_11.__match_args__))) if _coconut.hasattr(_coconut_match_temp_11, "__match_args__") else _coconut.len(_coconut_match_temp_11) == 1  # type: ignore  #5:     case state:
                                if _coconut_match_temp_13:  #5:     case state:
                                    _coconut_case_match_check_0 = True  #5:     case state:

                        if not _coconut_case_match_check_0:  #5:     case state:
                            if (not _coconut_match_temp_12) and (_coconut.isinstance(_coconut_match_temp_11, AutoList)):  #5:     case state:
                                _coconut_case_match_check_0 = True  #5:     case state:
                            if _coconut_case_match_check_0:  #5:     case state:
                                _coconut_case_match_check_0 = False  #5:     case state:
                                if not _coconut_case_match_check_0:  #5:     case state:
                                    if _coconut.type(_coconut_match_temp_11) in _coconut_self_match_types:  #5:     case state:
                                        _coconut_case_match_check_0 = True  #5:     case state:

                                if not _coconut_case_match_check_0:  #5:     case state:
                                    if not _coconut.type(_coconut_match_temp_11) in _coconut_self_match_types:  #5:     case state:
                                        _coconut_match_temp_14 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #5:     case state:
                                        if not _coconut.isinstance(_coconut_match_temp_14, _coconut.tuple):  #5:     case state:
                                            raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #5:     case state:
                                        if _coconut.len(_coconut_match_temp_14) < 1:  #5:     case state:
                                            raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_14),))  #5:     case state:
                                        _coconut_match_temp_15 = _coconut.getattr(_coconut_match_temp_11, _coconut_match_temp_14[0], _coconut_sentinel)  #5:     case state:
                                        if _coconut_match_temp_15 is not _coconut_sentinel:  #5:     case state:
                                            _coconut_case_match_check_0 = True  #5:     case state:








    if _coconut_case_match_check_0:  #5:     case state:
        return ([])  # dont dive into nested list too much  #7:             return [] # dont dive into nested list too much
    if not _coconut_case_match_check_0:  #8:         match AutoList(es):
        _coconut_match_temp_16 = _coconut.getattr(AutoList, "_coconut_is_data", False) or _coconut.isinstance(AutoList, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in AutoList)  # type: ignore  #8:         match AutoList(es):
        _coconut_case_match_check_0 = True  #8:         match AutoList(es):
        if _coconut_case_match_check_0:  #8:         match AutoList(es):
            _coconut_case_match_check_0 = False  #8:         match AutoList(es):
            if not _coconut_case_match_check_0:  #8:         match AutoList(es):
                _coconut_match_set_name_es = _coconut_sentinel  #8:         match AutoList(es):
                if (_coconut_match_temp_16) and (_coconut.isinstance(_coconut_case_match_to_0, AutoList)) and (_coconut.len(_coconut_case_match_to_0) >= 1):  #8:         match AutoList(es):
                    _coconut_match_set_name_es = _coconut_case_match_to_0[0]  #8:         match AutoList(es):
                    _coconut_match_temp_17 = _coconut.len(_coconut_case_match_to_0) <= _coconut.max(1, _coconut.len(_coconut_case_match_to_0.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {}) and _coconut_case_match_to_0[i] == _coconut.getattr(_coconut_case_match_to_0, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_case_match_to_0.__match_args__))) if _coconut.hasattr(_coconut_case_match_to_0, "__match_args__") else _coconut.len(_coconut_case_match_to_0) == 1  # type: ignore  #8:         match AutoList(es):
                    if _coconut_match_temp_17:  #8:         match AutoList(es):
                        _coconut_case_match_check_0 = True  #8:         match AutoList(es):
                if _coconut_case_match_check_0:  #8:         match AutoList(es):
                    if _coconut_match_set_name_es is not _coconut_sentinel:  #8:         match AutoList(es):
                        es = _coconut_match_set_name_es  #8:         match AutoList(es):

            if not _coconut_case_match_check_0:  #8:         match AutoList(es):
                if (not _coconut_match_temp_16) and (_coconut.isinstance(_coconut_case_match_to_0, AutoList)):  #8:         match AutoList(es):
                    _coconut_case_match_check_0 = True  #8:         match AutoList(es):
                if _coconut_case_match_check_0:  #8:         match AutoList(es):
                    _coconut_case_match_check_0 = False  #8:         match AutoList(es):
                    if not _coconut_case_match_check_0:  #8:         match AutoList(es):
                        _coconut_match_set_name_es = _coconut_sentinel  #8:         match AutoList(es):
                        if _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #8:         match AutoList(es):
                            _coconut_match_set_name_es = _coconut_case_match_to_0  #8:         match AutoList(es):
                            _coconut_case_match_check_0 = True  #8:         match AutoList(es):
                        if _coconut_case_match_check_0:  #8:         match AutoList(es):
                            if _coconut_match_set_name_es is not _coconut_sentinel:  #8:         match AutoList(es):
                                es = _coconut_match_set_name_es  #8:         match AutoList(es):

                    if not _coconut_case_match_check_0:  #8:         match AutoList(es):
                        _coconut_match_set_name_es = _coconut_sentinel  #8:         match AutoList(es):
                        if not _coconut.type(_coconut_case_match_to_0) in _coconut_self_match_types:  #8:         match AutoList(es):
                            _coconut_match_temp_18 = _coconut.getattr(AutoList, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #8:         match AutoList(es):
                            if not _coconut.isinstance(_coconut_match_temp_18, _coconut.tuple):  #8:         match AutoList(es):
                                raise _coconut.TypeError("AutoList.__match_args__ must be a tuple")  #8:         match AutoList(es):
                            if _coconut.len(_coconut_match_temp_18) < 1:  #8:         match AutoList(es):
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'AutoList' only supports %s)" % (_coconut.len(_coconut_match_temp_18),))  #8:         match AutoList(es):
                            _coconut_match_temp_19 = _coconut.getattr(_coconut_case_match_to_0, _coconut_match_temp_18[0], _coconut_sentinel)  #8:         match AutoList(es):
                            if _coconut_match_temp_19 is not _coconut_sentinel:  #8:         match AutoList(es):
                                _coconut_match_set_name_es = _coconut_match_temp_19  #8:         match AutoList(es):
                                _coconut_case_match_check_0 = True  #8:         match AutoList(es):
                        if _coconut_case_match_check_0:  #8:         match AutoList(es):
                            if _coconut_match_set_name_es is not _coconut_sentinel:  #8:         match AutoList(es):
                                es = _coconut_match_set_name_es  #8:         match AutoList(es):




        if _coconut_case_match_check_0:  #8:         match AutoList(es):
            return ([(lambda f, new_state, cost, name: (lambda items: [f(i) for i in items], AutoList(new_state), "[{_coconut_format_0}]".format(_coconut_format_0=(name)), cost + 1))(re.converter, re.new_format, re.cost, re.name) for re in neighbors(es)])  #9:             return [((f,new_state,cost,name)->(
