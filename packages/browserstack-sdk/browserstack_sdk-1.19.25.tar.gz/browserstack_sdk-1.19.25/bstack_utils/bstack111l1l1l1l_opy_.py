# coding: UTF-8
import sys
bstack1llllll1_opy_ = sys.version_info [0] == 2
bstack1l_opy_ = 2048
bstack1l111l1_opy_ = 7
def bstack11ll111_opy_ (bstack1ll111_opy_):
    global bstack1l1l1_opy_
    bstack1lll1ll_opy_ = ord (bstack1ll111_opy_ [-1])
    bstack11l11_opy_ = bstack1ll111_opy_ [:-1]
    bstack11llll1_opy_ = bstack1lll1ll_opy_ % len (bstack11l11_opy_)
    bstack1111l_opy_ = bstack11l11_opy_ [:bstack11llll1_opy_] + bstack11l11_opy_ [bstack11llll1_opy_:]
    if bstack1llllll1_opy_:
        bstack11l1111_opy_ = unicode () .join ([unichr (ord (char) - bstack1l_opy_ - (bstack111l1l_opy_ + bstack1lll1ll_opy_) % bstack1l111l1_opy_) for bstack111l1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l1111_opy_ = str () .join ([chr (ord (char) - bstack1l_opy_ - (bstack111l1l_opy_ + bstack1lll1ll_opy_) % bstack1l111l1_opy_) for bstack111l1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l1111_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l11l1l1l_opy_
from browserstack_sdk.bstack11ll111l1_opy_ import bstack1l1ll111l_opy_
def _111ll111ll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack111l1ll11l_opy_:
    def __init__(self, handler):
        self._111ll1111l_opy_ = {}
        self._111l1l1lll_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1l1ll111l_opy_.version()
        if bstack11l11l1l1l_opy_(pytest_version, bstack11ll111_opy_ (u"ࠤ࠻࠲࠶࠴࠱ࠣጟ")) >= 0:
            self._111ll1111l_opy_[bstack11ll111_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ጠ")] = Module._register_setup_function_fixture
            self._111ll1111l_opy_[bstack11ll111_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬጡ")] = Module._register_setup_module_fixture
            self._111ll1111l_opy_[bstack11ll111_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬጢ")] = Class._register_setup_class_fixture
            self._111ll1111l_opy_[bstack11ll111_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧጣ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack111l1lll1l_opy_(bstack11ll111_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪጤ"))
            Module._register_setup_module_fixture = self.bstack111l1lll1l_opy_(bstack11ll111_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩጥ"))
            Class._register_setup_class_fixture = self.bstack111l1lll1l_opy_(bstack11ll111_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩጦ"))
            Class._register_setup_method_fixture = self.bstack111l1lll1l_opy_(bstack11ll111_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫጧ"))
        else:
            self._111ll1111l_opy_[bstack11ll111_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧጨ")] = Module._inject_setup_function_fixture
            self._111ll1111l_opy_[bstack11ll111_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ጩ")] = Module._inject_setup_module_fixture
            self._111ll1111l_opy_[bstack11ll111_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ጪ")] = Class._inject_setup_class_fixture
            self._111ll1111l_opy_[bstack11ll111_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨጫ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack111l1lll1l_opy_(bstack11ll111_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫጬ"))
            Module._inject_setup_module_fixture = self.bstack111l1lll1l_opy_(bstack11ll111_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪጭ"))
            Class._inject_setup_class_fixture = self.bstack111l1lll1l_opy_(bstack11ll111_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪጮ"))
            Class._inject_setup_method_fixture = self.bstack111l1lll1l_opy_(bstack11ll111_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬጯ"))
    def bstack111l1lll11_opy_(self, bstack111l1l1ll1_opy_, hook_type):
        meth = getattr(bstack111l1l1ll1_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._111l1l1lll_opy_[hook_type] = meth
            setattr(bstack111l1l1ll1_opy_, hook_type, self.bstack111ll111l1_opy_(hook_type))
    def bstack111l1ll1ll_opy_(self, instance, bstack111l1llll1_opy_):
        if bstack111l1llll1_opy_ == bstack11ll111_opy_ (u"ࠧ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣጰ"):
            self.bstack111l1lll11_opy_(instance.obj, bstack11ll111_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠢጱ"))
            self.bstack111l1lll11_opy_(instance.obj, bstack11ll111_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠦጲ"))
        if bstack111l1llll1_opy_ == bstack11ll111_opy_ (u"ࠣ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠤጳ"):
            self.bstack111l1lll11_opy_(instance.obj, bstack11ll111_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠣጴ"))
            self.bstack111l1lll11_opy_(instance.obj, bstack11ll111_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠧጵ"))
        if bstack111l1llll1_opy_ == bstack11ll111_opy_ (u"ࠦࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠦጶ"):
            self.bstack111l1lll11_opy_(instance.obj, bstack11ll111_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠥጷ"))
            self.bstack111l1lll11_opy_(instance.obj, bstack11ll111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠢጸ"))
        if bstack111l1llll1_opy_ == bstack11ll111_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣጹ"):
            self.bstack111l1lll11_opy_(instance.obj, bstack11ll111_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠢጺ"))
            self.bstack111l1lll11_opy_(instance.obj, bstack11ll111_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠦጻ"))
    @staticmethod
    def bstack111l1ll111_opy_(hook_type, func, args):
        if hook_type in [bstack11ll111_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩጼ"), bstack11ll111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ጽ")]:
            _111ll111ll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack111ll111l1_opy_(self, hook_type):
        def bstack111l1lllll_opy_(arg=None):
            self.handler(hook_type, bstack11ll111_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬጾ"))
            result = None
            exception = None
            try:
                self.bstack111l1ll111_opy_(hook_type, self._111l1l1lll_opy_[hook_type], (arg,))
                result = Result(result=bstack11ll111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ጿ"))
            except Exception as e:
                result = Result(result=bstack11ll111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧፀ"), exception=e)
                self.handler(hook_type, bstack11ll111_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧፁ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11ll111_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨፂ"), result)
        def bstack111l1ll1l1_opy_(this, arg=None):
            self.handler(hook_type, bstack11ll111_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪፃ"))
            result = None
            exception = None
            try:
                self.bstack111l1ll111_opy_(hook_type, self._111l1l1lll_opy_[hook_type], (this, arg))
                result = Result(result=bstack11ll111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫፄ"))
            except Exception as e:
                result = Result(result=bstack11ll111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬፅ"), exception=e)
                self.handler(hook_type, bstack11ll111_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬፆ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11ll111_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ፇ"), result)
        if hook_type in [bstack11ll111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧፈ"), bstack11ll111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫፉ")]:
            return bstack111l1ll1l1_opy_
        return bstack111l1lllll_opy_
    def bstack111l1lll1l_opy_(self, bstack111l1llll1_opy_):
        def bstack111ll11111_opy_(this, *args, **kwargs):
            self.bstack111l1ll1ll_opy_(this, bstack111l1llll1_opy_)
            self._111ll1111l_opy_[bstack111l1llll1_opy_](this, *args, **kwargs)
        return bstack111ll11111_opy_