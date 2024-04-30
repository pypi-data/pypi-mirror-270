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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.bstack11l11l11l_opy_ as bstack1l11ll1l1_opy_
from browserstack_sdk.bstack1ll1llllll_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1l1l1_opy_
class bstack1l1ll111l_opy_:
    def __init__(self, args, logger, bstack11ll1l1lll_opy_, bstack11ll1ll1l1_opy_):
        self.args = args
        self.logger = logger
        self.bstack11ll1l1lll_opy_ = bstack11ll1l1lll_opy_
        self.bstack11ll1ll1l1_opy_ = bstack11ll1ll1l1_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack11ll1l1l_opy_ = []
        self.bstack11lll111l1_opy_ = None
        self.bstack1ll111llll_opy_ = []
        self.bstack11ll1lll1l_opy_ = self.bstack1lll1l1l1l_opy_()
        self.bstack1l1lllll1l_opy_ = -1
    def bstack1ll111lll_opy_(self, bstack11ll1lllll_opy_):
        self.parse_args()
        self.bstack11ll1ll11l_opy_()
        self.bstack11lll111ll_opy_(bstack11ll1lllll_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack11lll11111_opy_():
        import importlib
        if getattr(importlib, bstack11ll111_opy_ (u"ࠨࡨ࡬ࡲࡩࡥ࡬ࡰࡣࡧࡩࡷ࠭ฏ"), False):
            bstack11lll1111l_opy_ = importlib.find_loader(bstack11ll111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫฐ"))
        else:
            bstack11lll1111l_opy_ = importlib.util.find_spec(bstack11ll111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬฑ"))
    def bstack11ll1l1l1l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1l1lllll1l_opy_ = -1
        if bstack11ll111_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫฒ") in self.bstack11ll1l1lll_opy_:
            self.bstack1l1lllll1l_opy_ = int(self.bstack11ll1l1lll_opy_[bstack11ll111_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬณ")])
        try:
            bstack11ll1ll111_opy_ = [bstack11ll111_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨด"), bstack11ll111_opy_ (u"ࠧ࠮࠯ࡳࡰࡺ࡭ࡩ࡯ࡵࠪต"), bstack11ll111_opy_ (u"ࠨ࠯ࡳࠫถ")]
            if self.bstack1l1lllll1l_opy_ >= 0:
                bstack11ll1ll111_opy_.extend([bstack11ll111_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪท"), bstack11ll111_opy_ (u"ࠪ࠱ࡳ࠭ธ")])
            for arg in bstack11ll1ll111_opy_:
                self.bstack11ll1l1l1l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11ll1ll11l_opy_(self):
        bstack11lll111l1_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11lll111l1_opy_ = bstack11lll111l1_opy_
        return bstack11lll111l1_opy_
    def bstack1l111ll1l_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack11lll11111_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11l1l1l1_opy_)
    def bstack11lll111ll_opy_(self, bstack11ll1lllll_opy_):
        bstack1111l1111_opy_ = Config.bstack1ll111l11_opy_()
        if bstack11ll1lllll_opy_:
            self.bstack11lll111l1_opy_.append(bstack11ll111_opy_ (u"ࠫ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨน"))
            self.bstack11lll111l1_opy_.append(bstack11ll111_opy_ (u"࡚ࠬࡲࡶࡧࠪบ"))
        if bstack1111l1111_opy_.bstack11ll1l1ll1_opy_():
            self.bstack11lll111l1_opy_.append(bstack11ll111_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬป"))
            self.bstack11lll111l1_opy_.append(bstack11ll111_opy_ (u"ࠧࡕࡴࡸࡩࠬผ"))
        self.bstack11lll111l1_opy_.append(bstack11ll111_opy_ (u"ࠨ࠯ࡳࠫฝ"))
        self.bstack11lll111l1_opy_.append(bstack11ll111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠧพ"))
        self.bstack11lll111l1_opy_.append(bstack11ll111_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶࠬฟ"))
        self.bstack11lll111l1_opy_.append(bstack11ll111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫภ"))
        if self.bstack1l1lllll1l_opy_ > 1:
            self.bstack11lll111l1_opy_.append(bstack11ll111_opy_ (u"ࠬ࠳࡮ࠨม"))
            self.bstack11lll111l1_opy_.append(str(self.bstack1l1lllll1l_opy_))
    def bstack11ll1llll1_opy_(self):
        bstack1ll111llll_opy_ = []
        for spec in self.bstack11ll1l1l_opy_:
            bstack1l1lll1l1_opy_ = [spec]
            bstack1l1lll1l1_opy_ += self.bstack11lll111l1_opy_
            bstack1ll111llll_opy_.append(bstack1l1lll1l1_opy_)
        self.bstack1ll111llll_opy_ = bstack1ll111llll_opy_
        return bstack1ll111llll_opy_
    def bstack1lll1l1l1l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack11ll1lll1l_opy_ = True
            return True
        except Exception as e:
            self.bstack11ll1lll1l_opy_ = False
        return self.bstack11ll1lll1l_opy_
    def bstack1ll11lll_opy_(self, bstack11lll11l11_opy_, bstack1ll111lll_opy_):
        bstack1ll111lll_opy_[bstack11ll111_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ย")] = self.bstack11ll1l1lll_opy_
        multiprocessing.set_start_method(bstack11ll111_opy_ (u"ࠧࡴࡲࡤࡻࡳ࠭ร"))
        if bstack11ll111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫฤ") in self.bstack11ll1l1lll_opy_:
            bstack1l1ll1ll11_opy_ = []
            manager = multiprocessing.Manager()
            bstack1lll11llll_opy_ = manager.list()
            for index, platform in enumerate(self.bstack11ll1l1lll_opy_[bstack11ll111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬล")]):
                bstack1l1ll1ll11_opy_.append(multiprocessing.Process(name=str(index),
                                                           target=bstack11lll11l11_opy_,
                                                           args=(self.bstack11lll111l1_opy_, bstack1ll111lll_opy_, bstack1lll11llll_opy_)))
            i = 0
            bstack11ll1lll11_opy_ = len(self.bstack11ll1l1lll_opy_[bstack11ll111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ฦ")])
            for t in bstack1l1ll1ll11_opy_:
                os.environ[bstack11ll111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫว")] = str(i)
                os.environ[bstack11ll111_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭ศ")] = json.dumps(self.bstack11ll1l1lll_opy_[bstack11ll111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩษ")][i % bstack11ll1lll11_opy_])
                i += 1
                t.start()
            for t in bstack1l1ll1ll11_opy_:
                t.join()
            return list(bstack1lll11llll_opy_)
    @staticmethod
    def bstack1l111111_opy_(driver, bstack1l11111ll_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11ll111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫส"), None)
        if item and getattr(item, bstack11ll111_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࠪห"), None) and not getattr(item, bstack11ll111_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡳࡵࡥࡤࡰࡰࡨࠫฬ"), False):
            logger.info(
                bstack11ll111_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠤอ"))
            bstack11ll1ll1ll_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1l11ll1l1_opy_.bstack1lllll11l_opy_(driver, bstack11ll1ll1ll_opy_, item.name, item.module.__name__, item.path, bstack1l11111ll_opy_)
            item._a11y_stop_done = True
            if wait:
                sleep(2)