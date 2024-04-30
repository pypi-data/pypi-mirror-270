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
class bstack1l1l1ll1l_opy_:
    def __init__(self, handler):
        self._1llll1ll1l1_opy_ = None
        self.handler = handler
        self._1llll1ll1ll_opy_ = self.bstack1llll1ll11l_opy_()
        self.patch()
    def patch(self):
        self._1llll1ll1l1_opy_ = self._1llll1ll1ll_opy_.execute
        self._1llll1ll1ll_opy_.execute = self.bstack1llll1lll11_opy_()
    def bstack1llll1lll11_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11ll111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࠥᑾ"), driver_command, None, this, args)
            response = self._1llll1ll1l1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11ll111_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࠥᑿ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1llll1ll1ll_opy_.execute = self._1llll1ll1l1_opy_
    @staticmethod
    def bstack1llll1ll11l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver