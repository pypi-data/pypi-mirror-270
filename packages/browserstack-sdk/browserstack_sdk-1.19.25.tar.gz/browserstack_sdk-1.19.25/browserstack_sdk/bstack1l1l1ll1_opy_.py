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
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1ll11lllll_opy_ = {}
        bstack1l11l11l1l_opy_ = os.environ.get(bstack11ll111_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫജ"), bstack11ll111_opy_ (u"ࠫࠬഝ"))
        if not bstack1l11l11l1l_opy_:
            return bstack1ll11lllll_opy_
        try:
            bstack1l11l11ll1_opy_ = json.loads(bstack1l11l11l1l_opy_)
            if bstack11ll111_opy_ (u"ࠧࡵࡳࠣഞ") in bstack1l11l11ll1_opy_:
                bstack1ll11lllll_opy_[bstack11ll111_opy_ (u"ࠨ࡯ࡴࠤട")] = bstack1l11l11ll1_opy_[bstack11ll111_opy_ (u"ࠢࡰࡵࠥഠ")]
            if bstack11ll111_opy_ (u"ࠣࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧഡ") in bstack1l11l11ll1_opy_ or bstack11ll111_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧഢ") in bstack1l11l11ll1_opy_:
                bstack1ll11lllll_opy_[bstack11ll111_opy_ (u"ࠥࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳࠨണ")] = bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣത"), bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣഥ")))
            if bstack11ll111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࠢദ") in bstack1l11l11ll1_opy_ or bstack11ll111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧധ") in bstack1l11l11ll1_opy_:
                bstack1ll11lllll_opy_[bstack11ll111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨന")] = bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥഩ"), bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣപ")))
            if bstack11ll111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳࠨഫ") in bstack1l11l11ll1_opy_ or bstack11ll111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨബ") in bstack1l11l11ll1_opy_:
                bstack1ll11lllll_opy_[bstack11ll111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢഭ")] = bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤമ"), bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤയ")))
            if bstack11ll111_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࠤര") in bstack1l11l11ll1_opy_ or bstack11ll111_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢറ") in bstack1l11l11ll1_opy_:
                bstack1ll11lllll_opy_[bstack11ll111_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠣല")] = bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࠧള"), bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥഴ")))
            if bstack11ll111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤവ") in bstack1l11l11ll1_opy_ or bstack11ll111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢശ") in bstack1l11l11ll1_opy_:
                bstack1ll11lllll_opy_[bstack11ll111_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣഷ")] = bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧസ"), bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥഹ")))
            if bstack11ll111_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣഺ") in bstack1l11l11ll1_opy_ or bstack11ll111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮഻ࠣ") in bstack1l11l11ll1_opy_:
                bstack1ll11lllll_opy_[bstack11ll111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤ഼")] = bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠦഽ"), bstack1l11l11ll1_opy_.get(bstack11ll111_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦാ")))
            if bstack11ll111_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧി") in bstack1l11l11ll1_opy_:
                bstack1ll11lllll_opy_[bstack11ll111_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨീ")] = bstack1l11l11ll1_opy_[bstack11ll111_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠢു")]
        except Exception as error:
            logger.error(bstack11ll111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡡࡵࡣ࠽ࠤࠧൂ") +  str(error))
        return bstack1ll11lllll_opy_