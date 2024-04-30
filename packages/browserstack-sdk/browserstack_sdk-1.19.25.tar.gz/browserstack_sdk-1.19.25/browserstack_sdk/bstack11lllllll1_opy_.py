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
import os
class RobotHandler():
    def __init__(self, args, logger, bstack11ll1l1lll_opy_, bstack11ll1ll1l1_opy_):
        self.args = args
        self.logger = logger
        self.bstack11ll1l1lll_opy_ = bstack11ll1l1lll_opy_
        self.bstack11ll1ll1l1_opy_ = bstack11ll1ll1l1_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l1111l111_opy_(bstack11ll1l111l_opy_):
        bstack11ll1l11l1_opy_ = []
        if bstack11ll1l111l_opy_:
            tokens = str(os.path.basename(bstack11ll1l111l_opy_)).split(bstack11ll111_opy_ (u"ࠦࡤࠨฮ"))
            camelcase_name = bstack11ll111_opy_ (u"ࠧࠦࠢฯ").join(t.title() for t in tokens)
            suite_name, bstack11ll1l1l11_opy_ = os.path.splitext(camelcase_name)
            bstack11ll1l11l1_opy_.append(suite_name)
        return bstack11ll1l11l1_opy_
    @staticmethod
    def bstack11ll1l11ll_opy_(typename):
        if bstack11ll111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤะ") in typename:
            return bstack11ll111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣั")
        return bstack11ll111_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤา")