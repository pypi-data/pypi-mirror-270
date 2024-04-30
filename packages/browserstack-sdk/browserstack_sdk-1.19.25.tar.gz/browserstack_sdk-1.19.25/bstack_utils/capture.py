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
import sys
class bstack1l1111l11l_opy_:
    def __init__(self, handler):
        self._11l1l1lll1_opy_ = sys.stdout.write
        self._11l1l1ll11_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack11l1l1ll1l_opy_
        sys.stdout.error = self.bstack11l1l1l1ll_opy_
    def bstack11l1l1ll1l_opy_(self, _str):
        self._11l1l1lll1_opy_(_str)
        if self.handler:
            self.handler({bstack11ll111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭໧"): bstack11ll111_opy_ (u"ࠨࡋࡑࡊࡔ࠭໨"), bstack11ll111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ໩"): _str})
    def bstack11l1l1l1ll_opy_(self, _str):
        self._11l1l1ll11_opy_(_str)
        if self.handler:
            self.handler({bstack11ll111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ໪"): bstack11ll111_opy_ (u"ࠫࡊࡘࡒࡐࡔࠪ໫"), bstack11ll111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭໬"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._11l1l1lll1_opy_
        sys.stderr.write = self._11l1l1ll11_opy_