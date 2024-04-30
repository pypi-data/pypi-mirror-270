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
from browserstack_sdk.bstack11ll111l1_opy_ import bstack1l1ll111l_opy_
from browserstack_sdk.bstack11lllllll1_opy_ import RobotHandler
def bstack1ll1111111_opy_(framework):
    if framework.lower() == bstack11ll111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᆁ"):
        return bstack1l1ll111l_opy_.version()
    elif framework.lower() == bstack11ll111_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨᆂ"):
        return RobotHandler.version()
    elif framework.lower() == bstack11ll111_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪᆃ"):
        import behave
        return behave.__version__
    else:
        return bstack11ll111_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࠬᆄ")