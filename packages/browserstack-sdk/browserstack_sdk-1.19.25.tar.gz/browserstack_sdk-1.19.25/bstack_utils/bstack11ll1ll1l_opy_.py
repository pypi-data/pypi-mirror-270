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
from collections import deque
from bstack_utils.constants import *
class bstack1lll11111_opy_:
    def __init__(self):
        self._111111l111_opy_ = deque()
        self._11111111ll_opy_ = {}
        self._1111111l1l_opy_ = False
    def bstack1111111ll1_opy_(self, test_name, bstack111111ll11_opy_):
        bstack1111111l11_opy_ = self._11111111ll_opy_.get(test_name, {})
        return bstack1111111l11_opy_.get(bstack111111ll11_opy_, 0)
    def bstack1lllllllll1_opy_(self, test_name, bstack111111ll11_opy_):
        bstack1111111111_opy_ = self.bstack1111111ll1_opy_(test_name, bstack111111ll11_opy_)
        self.bstack111111l1l1_opy_(test_name, bstack111111ll11_opy_)
        return bstack1111111111_opy_
    def bstack111111l1l1_opy_(self, test_name, bstack111111ll11_opy_):
        if test_name not in self._11111111ll_opy_:
            self._11111111ll_opy_[test_name] = {}
        bstack1111111l11_opy_ = self._11111111ll_opy_[test_name]
        bstack1111111111_opy_ = bstack1111111l11_opy_.get(bstack111111ll11_opy_, 0)
        bstack1111111l11_opy_[bstack111111ll11_opy_] = bstack1111111111_opy_ + 1
    def bstack1ll1ll1lll_opy_(self, bstack11111111l1_opy_, bstack1111111lll_opy_):
        bstack111111111l_opy_ = self.bstack1lllllllll1_opy_(bstack11111111l1_opy_, bstack1111111lll_opy_)
        bstack111111l1ll_opy_ = bstack11l1l11l11_opy_[bstack1111111lll_opy_]
        bstack111111l11l_opy_ = bstack11ll111_opy_ (u"ࠧࢁࡽ࠮ࡽࢀ࠱ࢀࢃࠢᐥ").format(bstack11111111l1_opy_, bstack111111l1ll_opy_, bstack111111111l_opy_)
        self._111111l111_opy_.append(bstack111111l11l_opy_)
    def bstack1l11l1ll1_opy_(self):
        return len(self._111111l111_opy_) == 0
    def bstack1111ll1ll_opy_(self):
        bstack1llllllllll_opy_ = self._111111l111_opy_.popleft()
        return bstack1llllllllll_opy_
    def capturing(self):
        return self._1111111l1l_opy_
    def bstack1ll11111l1_opy_(self):
        self._1111111l1l_opy_ = True
    def bstack11ll1lll_opy_(self):
        self._1111111l1l_opy_ = False