#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xde45ca28

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

import ipywidgets as widgets  #1: import ipywidgets as widgets
from pprintpp import pformat  #2: from pprintpp import pformat,pprint
from pprintpp import pprint  #2: from pprintpp import pformat,pprint
from PIL import Image  #3: from PIL import Image
import PIL  #4: import PIL
from loguru import logger  #5: from loguru import logger
import numpy as np  #6: import numpy as np
import pandas as pd  #7: import pandas as pd
if _coconut.typing.TYPE_CHECKING:  #8: from typing import Iterable
    from typing import Iterable  #8: from typing import Iterable
else:  #8: from typing import Iterable
    try:  #8: from typing import Iterable
        Iterable = _coconut.typing.Iterable  #8: from typing import Iterable
    except _coconut.AttributeError as _coconut_imp_err:  #8: from typing import Iterable
        raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #8: from typing import Iterable
nn = lambda none, func: func(none) if none is not None else None  #9: nn = (none,func) -> func(none) if none is not None else None
L = _coconut_partial(Image.fromarray, mode="L")  #10: L = Image.fromarray$(mode="L")
RGB = _coconut_partial(Image.fromarray, mode="RGB")  #11: RGB = Image.fromarray$(mode="RGB")
RGBA = _coconut_partial(Image.fromarray, mode="RGBA")  #12: RGBA = Image.fromarray$(mode="RGBA")
batch_image_to_image = lambda ary: ary.transpose((1, 0, 2, 3)).reshape((ary.shape[2], -1, ary.shape[3]))  #13: batch_image_to_image = ary->ary.transpose((1, 0, 2, 3)).reshape((ary.shape[2], -1, ary.shape[3]))
batch_L_to_img = lambda ary: ary  #14: batch_L_to_img = ary->ary
def img_to_widget(value):  #15: def img_to_widget(value):
    img_widget = widgets.Image(value=value._repr_png_(), format="png")  #16:     img_widget = widgets.Image(value=value._repr_png_(),format="png")
#img_widget.layout.object_fit = "contain"
    return (img_widget)  #18:     return img_widget
#img_to_widget = value ->widgets.Box([widgets.Image(value=value._repr_png_(),format="png")])


from bqplot import pyplot as blt  #21: from bqplot import pyplot as blt
from loguru import logger  #22: from loguru import logger

class DummyType(_coconut.collections.namedtuple("DummyType", ())):  #24: data DummyType
    __slots__ = ()  #24: data DummyType
    _coconut_is_data = True  #24: data DummyType
    __match_args__ = ()  #24: data DummyType
    def __add__(self, other): return _coconut.NotImplemented  #24: data DummyType
    def __mul__(self, other): return _coconut.NotImplemented  #24: data DummyType
    def __rmul__(self, other): return _coconut.NotImplemented  #24: data DummyType
    __ne__ = _coconut.object.__ne__  #24: data DummyType
    def __eq__(self, other):  #24: data DummyType
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #24: data DummyType
    def __hash__(self):  #24: data DummyType
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #24: data DummyType


_coconut_call_set_names(DummyType)  #26: try:
try:  #26: try:
    import torch  #27:     import torch
    TensorType = torch.Tensor  #28:     TensorType = torch.Tensor
except Exception as e:  #29: except Exception as e:
    logger.warning("failed to load torch. no visualization for torch tensor.".format())  #30:     logger.warning(f"failed to load torch. no visualization for torch tensor.")
    TensorType = DummyType  #31:     TensorType = DummyType

def bqplot_hist(ary, title="histogram", bins=50):  #33: def bqplot_hist(ary, title="histogram", bins=50):
    fig = blt.figure(title=title)  #34:     fig = blt.figure(title=title)
    blt.hist(ary.flatten(), bins=bins)  #35:     blt.hist(ary.flatten(), bins=bins)
    fig.layout.width = "400px"  #36:     fig.layout.width = "400px"
    fig.layout.height = "300px"  #37:     fig.layout.height = "300px"
    return (fig)  #38:     return fig



def ary_to_image(value):  #41: def ary_to_image(value):
    if not (isinstance)(value, np.ndarray):  #42:     if not value `isinstance` np.ndarray:
        return (None)  #43:         return None
    if value.dtype is not np.uint8:  #44:     if value.dtype is not np.uint8:
        if value.max() <= 1:  #45:         if value.max() <= 1:
            value = value * 255  #46:             value = value * 255
#logger.warning("automatically converting dtype {value.dtype} to uint8 for visualization")
        value = value.astype("uint8")  #48:         value = value.astype("uint8")


    _coconut_case_match_to_0 = value.shape  #51:     case value.shape:
    _coconut_case_match_check_0 = False  #51:     case value.shape:
    _coconut_match_set_name_bs = _coconut_sentinel  #51:     case value.shape:
    _coconut_match_set_name_h = _coconut_sentinel  #51:     case value.shape:
    _coconut_match_set_name_w = _coconut_sentinel  #51:     case value.shape:
    if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 4) and (_coconut_case_match_to_0[3] == 1):  #51:     case value.shape:
        _coconut_match_set_name_bs = _coconut_case_match_to_0[0]  #51:     case value.shape:
        _coconut_match_set_name_h = _coconut_case_match_to_0[1]  #51:     case value.shape:
        _coconut_match_set_name_w = _coconut_case_match_to_0[2]  #51:     case value.shape:
        _coconut_case_match_check_0 = True  #51:     case value.shape:
    if _coconut_case_match_check_0:  #51:     case value.shape:
        if _coconut_match_set_name_bs is not _coconut_sentinel:  #51:     case value.shape:
            bs = _coconut_match_set_name_bs  #51:     case value.shape:
        if _coconut_match_set_name_h is not _coconut_sentinel:  #51:     case value.shape:
            h = _coconut_match_set_name_h  #51:     case value.shape:
        if _coconut_match_set_name_w is not _coconut_sentinel:  #51:     case value.shape:
            w = _coconut_match_set_name_w  #51:     case value.shape:
    if _coconut_case_match_check_0:  #51:     case value.shape:
        return ((L)(value.transpose(1, 0, 2, 3).reshape(h, bs * w)))  #53:             return value.transpose(1,0,2,3).reshape(h,bs*w) |> L
    if not _coconut_case_match_check_0:  # batch of rgbs  #54:         match (_,_,_,3): # batch of rgbs
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 4) and (_coconut_case_match_to_0[3] == 3):  # batch of rgbs  #54:         match (_,_,_,3): # batch of rgbs
            _coconut_case_match_check_0 = True  # batch of rgbs  #54:         match (_,_,_,3): # batch of rgbs
        if _coconut_case_match_check_0:  # batch of rgbs  #54:         match (_,_,_,3): # batch of rgbs
            return ((RGB)((batch_image_to_image)(value)))  #55:             return value |> batch_image_to_image |> RGB
    if not _coconut_case_match_check_0:  # batch of rgbas  #56:         match (_,_,_,4): # batch of rgbas
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 4) and (_coconut_case_match_to_0[3] == 4):  # batch of rgbas  #56:         match (_,_,_,4): # batch of rgbas
            _coconut_case_match_check_0 = True  # batch of rgbas  #56:         match (_,_,_,4): # batch of rgbas
        if _coconut_case_match_check_0:  # batch of rgbas  #56:         match (_,_,_,4): # batch of rgbas
            return ((RGBA)((batch_image_to_image)(value)))  #57:             return value |> batch_image_to_image |> RGBA
    if not _coconut_case_match_check_0:  # a gray image  #58:         match (_,_,1): # a gray image
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[2] == 1):  # a gray image  #58:         match (_,_,1): # a gray image
            _coconut_case_match_check_0 = True  # a gray image  #58:         match (_,_,1): # a gray image
        if _coconut_case_match_check_0:  # a gray image  #58:         match (_,_,1): # a gray image
            return ((L)(value[:, :, 0]))  #59:             return value[:,:,0] |> L
    if not _coconut_case_match_check_0:  # an RGB image  #60:         match (_,_,3): # an RGB image
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[2] == 3):  # an RGB image  #60:         match (_,_,3): # an RGB image
            _coconut_case_match_check_0 = True  # an RGB image  #60:         match (_,_,3): # an RGB image
        if _coconut_case_match_check_0:  # an RGB image  #60:         match (_,_,3): # an RGB image
            return ((RGB)(value))  #61:             return value |> RGB
    if not _coconut_case_match_check_0:  # an RGBA image  #62:         match (_,_,4): # an RGBA image
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[2] == 4):  # an RGBA image  #62:         match (_,_,4): # an RGBA image
            _coconut_case_match_check_0 = True  # an RGBA image  #62:         match (_,_,4): # an RGBA image
        if _coconut_case_match_check_0:  # an RGBA image  #62:         match (_,_,4): # an RGBA image
            return ((RGBA)(value))  #63:             return value |> RGBA
    if not _coconut_case_match_check_0:  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
        _coconut_match_set_name_bs = _coconut_sentinel  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
        _coconut_match_set_name_h = _coconut_sentinel  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
        _coconut_match_set_name_w = _coconut_sentinel  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3):  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
            _coconut_match_set_name_bs = _coconut_case_match_to_0[0]  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
            _coconut_match_set_name_h = _coconut_case_match_to_0[1]  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
            _coconut_match_set_name_w = _coconut_case_match_to_0[2]  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
            _coconut_case_match_check_0 = True  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
        if _coconut_case_match_check_0:  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
            if _coconut_match_set_name_bs is not _coconut_sentinel:  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
                bs = _coconut_match_set_name_bs  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
            if _coconut_match_set_name_h is not _coconut_sentinel:  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
                h = _coconut_match_set_name_h  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
            if _coconut_match_set_name_w is not _coconut_sentinel:  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
                w = _coconut_match_set_name_w  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
        if _coconut_case_match_check_0 and not (w > 4):  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
            _coconut_case_match_check_0 = False  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
        if _coconut_case_match_check_0:  # batch of gray image  #64:         match (bs,h,w) if w>4: # batch of gray image
            return ((L)(value.transpose(1, 0, 2).reshape(h, bs * w)))  #65:             return value.transpose(1,0,2).reshape(h,bs*w) |> L
    if not _coconut_case_match_check_0:  # gray image  #66:         match (_,_): # gray image
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2):  # gray image  #66:         match (_,_): # gray image
            _coconut_case_match_check_0 = True  # gray image  #66:         match (_,_): # gray image
        if _coconut_case_match_check_0:  # gray image  #66:         match (_,_): # gray image
            return ((L)(value))  #67:             return value |> L
    if not _coconut_case_match_check_0:  #68:     else:
        return (None)  #69:         return None


def ary_stat_widget(ary):  #71: def ary_stat_widget(ary):
    return (widgets.VBox([widgets.Label(value=pformat(str(dict(shape=ary.shape, dtype=ary.dtype)))), widgets.HTML(pd.DataFrame(pd.Series(ary.ravel()).describe()).transpose()._repr_html_())]))  #72:     return widgets.VBox([



def ary_to_widget(ary):  #82: def ary_to_widget(ary):
    stat_widget = ary_stat_widget(ary)  #83:     stat_widget = ary_stat_widget(ary)
    viz_widget = (nn)(ary_to_image(ary), img_to_widget)  #84:     viz_widget = ary_to_image(ary) `nn` img_to_widget
    viz_widget = widgets.Label(value=str(ary)[:100]) if viz_widget is None else viz_widget  #85:     viz_widget ??= widgets.Label(value=str(ary)[:100])

    children = [viz_widget, (bqplot_hist)(ary), stat_widget]  #87:     children = [
    return (widgets.VBox(children))  #92:     return widgets.VBox(children)


def output_widget(value):  #94: def output_widget(value):
    out = widgets.Output()  #95:     out = widgets.Output()
    with out:  #96:     with out:
        pprint(repr(value))  #97:         pprint(repr(value))
    return (out)  #98:     return out


def infer_widget(value):  #100: def infer_widget(value):
    while True:  #101:     from data_tree._series import Series
        from data_tree._series import Series  #101:     from data_tree._series import Series
        _coconut_case_match_to_1 = value  #102:     case value:
        _coconut_case_match_check_1 = False  #102:     case value:
        _coconut_case_match_check_1 = True  #102:     case value:
        if _coconut_case_match_check_1 and not (hasattr(value, "to_widget")):  #102:     case value:
            _coconut_case_match_check_1 = False  #102:     case value:
        if _coconut_case_match_check_1:  #102:     case value:
            return (value.to_widget())  #104:             return value.to_widget()
        if not _coconut_case_match_check_1:  #105:         match _ if hasattr(value, "_ipython_display_"):
            _coconut_case_match_check_1 = True  #105:         match _ if hasattr(value, "_ipython_display_"):
            if _coconut_case_match_check_1 and not (hasattr(value, "_ipython_display_")):  #105:         match _ if hasattr(value, "_ipython_display_"):
                _coconut_case_match_check_1 = False  #105:         match _ if hasattr(value, "_ipython_display_"):
            if _coconut_case_match_check_1:  #105:         match _ if hasattr(value, "_ipython_display_"):
                from ipywidgets import Output  #106:             from ipywidgets import Output
                from IPython.display import display  #107:             from IPython.display import display
                out = Output()  #108:             out = Output()
                with out:  #109:             with out:
                    display(value)  #110:                 display(value)
                return (out)  #111:             return out
        if not _coconut_case_match_check_1:  #112:         match _ is Series:
            if _coconut.isinstance(_coconut_case_match_to_1, Series):  #112:         match _ is Series:
                _coconut_case_match_check_1 = True  #112:         match _ is Series:
            if _coconut_case_match_check_1:  #112:         match _ is Series:
                return (value.widget())  #113:             return value.widget()
        if not _coconut_case_match_check_1:  #114:         match _ is PIL.Image.Image:
            if _coconut.isinstance(_coconut_case_match_to_1, PIL.Image.Image):  #114:         match _ is PIL.Image.Image:
                _coconut_case_match_check_1 = True  #114:         match _ is PIL.Image.Image:
            if _coconut_case_match_check_1:  #114:         match _ is PIL.Image.Image:
                return ((img_to_widget)(value))  #115:             return value |> img_to_widget
        if not _coconut_case_match_check_1:  #116:         match _ is TensorType:
            if _coconut.isinstance(_coconut_case_match_to_1, TensorType):  #116:         match _ is TensorType:
                _coconut_case_match_check_1 = True  #116:         match _ is TensorType:
            if _coconut_case_match_check_1:  #116:         match _ is TensorType:
                try:  #116:         match _ is TensorType:
                    _coconut_tre_check_0 = infer_widget is _coconut_recursive_func_6  # type: ignore  #116:         match _ is TensorType:
                except _coconut.NameError:  #116:         match _ is TensorType:
                    _coconut_tre_check_0 = False  #116:         match _ is TensorType:
                if _coconut_tre_check_0:  #116:         match _ is TensorType:
                    (value,) = (value.detach().cpu().numpy(),)  #116:         match _ is TensorType:
                    continue  #116:         match _ is TensorType:
                else:  #116:         match _ is TensorType:
                    return infer_widget(value.detach().cpu().numpy())  #116:         match _ is TensorType:

        if not _coconut_case_match_check_1:  #118:         match _ is np.ndarray:
            if _coconut.isinstance(_coconut_case_match_to_1, np.ndarray):  #118:         match _ is np.ndarray:
                _coconut_case_match_check_1 = True  #118:         match _ is np.ndarray:
            if _coconut_case_match_check_1:  #118:         match _ is np.ndarray:
                return (ary_to_widget(value))  #119:             return ary_to_widget(value)
        if not _coconut_case_match_check_1:  #120:         match _ is tuple if value `hasattr` "_asdict":
            if _coconut.isinstance(_coconut_case_match_to_1, tuple):  #120:         match _ is tuple if value `hasattr` "_asdict":
                _coconut_case_match_check_1 = True  #120:         match _ is tuple if value `hasattr` "_asdict":
            if _coconut_case_match_check_1 and not ((hasattr)(value, "_asdict")):  #120:         match _ is tuple if value `hasattr` "_asdict":
                _coconut_case_match_check_1 = False  #120:         match _ is tuple if value `hasattr` "_asdict":
            if _coconut_case_match_check_1:  #120:         match _ is tuple if value `hasattr` "_asdict":
                return ((output_widget)(value))  #121:             return value |> output_widget
        if not _coconut_case_match_check_1:  #122:         match _ is dict:
            if _coconut.isinstance(_coconut_case_match_to_1, dict):  #122:         match _ is dict:
                _coconut_case_match_check_1 = True  #122:         match _ is dict:
            if _coconut_case_match_check_1:  #122:         match _ is dict:
                return (widgets.VBox([widgets.VBox([widgets.Text(k), infer_widget(v)]) for k, v in value.items()]))  #123:             return widgets.VBox([
        if not _coconut_case_match_check_1:  #126:         match _ is (tuple,list):
            if _coconut.isinstance(_coconut_case_match_to_1, (tuple, list)):  #126:         match _ is (tuple,list):
                _coconut_case_match_check_1 = True  #126:         match _ is (tuple,list):
            if _coconut_case_match_check_1:  #126:         match _ is (tuple,list):
                items = [infer_widget(item) for item in value]  #127:             items = [infer_widget(item) for item in value]
                return (widgets.VBox([widgets.GridBox(items, layout=widgets.Layout(grid_template_columns="auto auto auto", border="solid 2px")), widgets.Label(value="displaying tuple with {_coconut_format_0} elements".format(_coconut_format_0=(len(value))))]))  #128:             return widgets.VBox([
        if not _coconut_case_match_check_1:  #135:     else:
            return ((output_widget)(value))  #138: 
    return None  #139: 

_coconut_recursive_func_6 = infer_widget  #139:
