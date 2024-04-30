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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack11l1lllll1_opy_, bstack11ll1l1l1_opy_, get_host_info, bstack11l1lll1ll_opy_, bstack11ll11ll1l_opy_, bstack111ll1l1ll_opy_, \
    bstack111lll1ll1_opy_, bstack11l111ll11_opy_, bstack11lllll11_opy_, bstack11l11l1ll1_opy_, bstack1llll1lll1_opy_, bstack11lll11l1l_opy_
from bstack_utils.bstack1lllll111ll_opy_ import bstack1lllll11l11_opy_
from bstack_utils.bstack1l111llll1_opy_ import bstack1l111111ll_opy_
import bstack_utils.bstack11l11l11l_opy_ as bstack1l11ll1l1_opy_
from bstack_utils.constants import bstack11l1l111l1_opy_
bstack1lll1ll1111_opy_ = [
    bstack11ll111_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫᓲ"), bstack11ll111_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬᓳ"), bstack11ll111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᓴ"), bstack11ll111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫᓵ"),
    bstack11ll111_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᓶ"), bstack11ll111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᓷ"), bstack11ll111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᓸ")
]
bstack1lll1ll11ll_opy_ = bstack11ll111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡥࡲࡰࡱ࡫ࡣࡵࡱࡵ࠱ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧᓹ")
logger = logging.getLogger(__name__)
class bstack11lll1l1_opy_:
    bstack1lllll111ll_opy_ = None
    bs_config = None
    @classmethod
    @bstack11lll11l1l_opy_(class_method=True)
    def launch(cls, bs_config, bstack1llll111111_opy_):
        cls.bs_config = bs_config
        cls.bstack1lll1llllll_opy_()
        bstack11ll11111l_opy_ = bstack11l1lll1ll_opy_(bs_config)
        bstack11ll11l11l_opy_ = bstack11ll11ll1l_opy_(bs_config)
        bstack1l111l1l1_opy_ = False
        bstack1ll1111l_opy_ = False
        if bstack11ll111_opy_ (u"ࠨࡣࡳࡴࠬᓺ") in bs_config:
            bstack1l111l1l1_opy_ = True
        else:
            bstack1ll1111l_opy_ = True
        bstack1l11l1l11l_opy_ = {
            bstack11ll111_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᓻ"): cls.bstack1lllll11l1_opy_() and cls.bstack1lll1l1lll1_opy_(bstack1llll111111_opy_.get(bstack11ll111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫᓼ"), bstack11ll111_opy_ (u"ࠫࠬᓽ"))),
            bstack11ll111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᓾ"): bstack1l11ll1l1_opy_.bstack111ll1lll_opy_(bs_config),
            bstack11ll111_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᓿ"): bs_config.get(bstack11ll111_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ᔀ"), False),
            bstack11ll111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᔁ"): bstack1ll1111l_opy_,
            bstack11ll111_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨᔂ"): bstack1l111l1l1_opy_
        }
        data = {
            bstack11ll111_opy_ (u"ࠪࡪࡴࡸ࡭ࡢࡶࠪᔃ"): bstack11ll111_opy_ (u"ࠫ࡯ࡹ࡯࡯ࠩᔄ"),
            bstack11ll111_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡥ࡮ࡢ࡯ࡨࠫᔅ"): bs_config.get(bstack11ll111_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᔆ"), bstack11ll111_opy_ (u"ࠧࠨᔇ")),
            bstack11ll111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᔈ"): bs_config.get(bstack11ll111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᔉ"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack11ll111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᔊ"): bs_config.get(bstack11ll111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᔋ")),
            bstack11ll111_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪᔌ"): bs_config.get(bstack11ll111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩᔍ"), bstack11ll111_opy_ (u"ࠧࠨᔎ")),
            bstack11ll111_opy_ (u"ࠨࡵࡷࡥࡷࡺ࡟ࡵ࡫ࡰࡩࠬᔏ"): datetime.datetime.now().isoformat(),
            bstack11ll111_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᔐ"): bstack111ll1l1ll_opy_(bs_config),
            bstack11ll111_opy_ (u"ࠪ࡬ࡴࡹࡴࡠ࡫ࡱࡪࡴ࠭ᔑ"): get_host_info(),
            bstack11ll111_opy_ (u"ࠫࡨ࡯࡟ࡪࡰࡩࡳࠬᔒ"): bstack11ll1l1l1_opy_(),
            bstack11ll111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡷࡻ࡮ࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᔓ"): os.environ.get(bstack11ll111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬᔔ")),
            bstack11ll111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࡥࡲࡦࡴࡸࡲࠬᔕ"): os.environ.get(bstack11ll111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓ࠭ᔖ"), False),
            bstack11ll111_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࡢࡧࡴࡴࡴࡳࡱ࡯ࠫᔗ"): bstack11l1lllll1_opy_(),
            bstack11ll111_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࡣࡲࡧࡰࠨᔘ"): bstack1l11l1l11l_opy_,
            bstack11ll111_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᔙ"): {
                bstack11ll111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬᔚ"): bstack1llll111111_opy_.get(bstack11ll111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧᔛ"), bstack11ll111_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧᔜ")),
                bstack11ll111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫᔝ"): bstack1llll111111_opy_.get(bstack11ll111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᔞ")),
                bstack11ll111_opy_ (u"ࠪࡷࡩࡱࡖࡦࡴࡶ࡭ࡴࡴࠧᔟ"): bstack1llll111111_opy_.get(bstack11ll111_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᔠ"))
            }
        }
        config = {
            bstack11ll111_opy_ (u"ࠬࡧࡵࡵࡪࠪᔡ"): (bstack11ll11111l_opy_, bstack11ll11l11l_opy_),
            bstack11ll111_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧᔢ"): cls.default_headers()
        }
        response = bstack11lllll11_opy_(bstack11ll111_opy_ (u"ࠧࡑࡑࡖࡘࠬᔣ"), cls.request_url(bstack11ll111_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳࠨᔤ")), data, config)
        if response.status_code != 200:
            os.environ[bstack11ll111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᔥ")] = bstack11ll111_opy_ (u"ࠪࡲࡺࡲ࡬ࠨᔦ")
            os.environ[bstack11ll111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪᔧ")] = bstack11ll111_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫᔨ")
            os.environ[bstack11ll111_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧᔩ")] = bstack11ll111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬᔪ")
            os.environ[bstack11ll111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᔫ")] = bstack11ll111_opy_ (u"ࠤࡱࡹࡱࡲࠢᔬ")
            os.environ[bstack11ll111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫᔭ")] = bstack11ll111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᔮ")
            bstack1lll1lll1ll_opy_ = response.json()
            if bstack1lll1lll1ll_opy_ and bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᔯ")]:
                error_message = bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᔰ")]
                if bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࡚ࡹࡱࡧࠪᔱ")] == bstack11ll111_opy_ (u"ࠨࡇࡕࡖࡔࡘ࡟ࡊࡐ࡙ࡅࡑࡏࡄࡠࡅࡕࡉࡉࡋࡎࡕࡋࡄࡐࡘ࠭ᔲ"):
                    logger.error(error_message)
                elif bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"ࠩࡨࡶࡷࡵࡲࡕࡻࡳࡩࠬᔳ")] == bstack11ll111_opy_ (u"ࠪࡉࡗࡘࡏࡓࡡࡄࡇࡈࡋࡓࡔࡡࡇࡉࡓࡏࡅࡅࠩᔴ"):
                    logger.info(error_message)
                elif bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"ࠫࡪࡸࡲࡰࡴࡗࡽࡵ࡫ࠧᔵ")] == bstack11ll111_opy_ (u"ࠬࡋࡒࡓࡑࡕࡣࡘࡊࡋࡠࡆࡈࡔࡗࡋࡃࡂࡖࡈࡈࠬᔶ"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11ll111_opy_ (u"ࠨࡄࡢࡶࡤࠤࡺࡶ࡬ࡰࡣࡧࠤࡹࡵࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡔࡦࡵࡷࠤࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡩࡻࡥࠡࡶࡲࠤࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣᔷ"))
            return [None, None, None]
        bstack1lll1lll1ll_opy_ = response.json()
        os.environ[bstack11ll111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᔸ")] = bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪᔹ")]
        if cls.bstack1lllll11l1_opy_() is True and cls.bstack1lll1l1lll1_opy_(bstack1llll111111_opy_.get(bstack11ll111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪᔺ"), bstack11ll111_opy_ (u"ࠪࠫᔻ"))):
            logger.debug(bstack11ll111_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨᔼ"))
            os.environ[bstack11ll111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫᔽ")] = bstack11ll111_opy_ (u"࠭ࡴࡳࡷࡨࠫᔾ")
            if bstack1lll1lll1ll_opy_.get(bstack11ll111_opy_ (u"ࠧ࡫ࡹࡷࠫᔿ")):
                os.environ[bstack11ll111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡐࡗࡕࠩᕀ")] = bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"ࠩ࡭ࡻࡹ࠭ᕁ")]
                os.environ[bstack11ll111_opy_ (u"ࠪࡇࡗࡋࡄࡆࡐࡗࡍࡆࡒࡓࡠࡈࡒࡖࡤࡉࡒࡂࡕࡋࡣࡗࡋࡐࡐࡔࡗࡍࡓࡍࠧᕂ")] = json.dumps({
                    bstack11ll111_opy_ (u"ࠫࡺࡹࡥࡳࡰࡤࡱࡪ࠭ᕃ"): bstack11ll11111l_opy_,
                    bstack11ll111_opy_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧᕄ"): bstack11ll11l11l_opy_
                })
            if bstack1lll1lll1ll_opy_.get(bstack11ll111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨᕅ")):
                os.environ[bstack11ll111_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ᕆ")] = bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪᕇ")]
            if bstack1lll1lll1ll_opy_.get(bstack11ll111_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ᕈ")):
                os.environ[bstack11ll111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫᕉ")] = str(bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨᕊ")])
        return [bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"ࠬࡰࡷࡵࠩᕋ")], bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨᕌ")], bstack1lll1lll1ll_opy_[bstack11ll111_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫᕍ")]]
    @classmethod
    @bstack11lll11l1l_opy_(class_method=True)
    def stop(cls):
        if not cls.on():
            return
        if os.environ[bstack11ll111_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡐࡗࡕࠩᕎ")] == bstack11ll111_opy_ (u"ࠤࡱࡹࡱࡲࠢᕏ") or os.environ[bstack11ll111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᕐ")] == bstack11ll111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᕑ"):
            print(bstack11ll111_opy_ (u"ࠬࡋࡘࡄࡇࡓࡘࡎࡕࡎࠡࡋࡑࠤࡸࡺ࡯ࡱࡄࡸ࡭ࡱࡪࡕࡱࡵࡷࡶࡪࡧ࡭ࠡࡔࡈࡕ࡚ࡋࡓࡕࠢࡗࡓ࡚ࠥࡅࡔࡖࠣࡓࡇ࡙ࡅࡓࡘࡄࡆࡎࡒࡉࡕ࡛ࠣ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭ᕒ"))
            return {
                bstack11ll111_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᕓ"): bstack11ll111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᕔ"),
                bstack11ll111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᕕ"): bstack11ll111_opy_ (u"ࠩࡗࡳࡰ࡫࡮࠰ࡤࡸ࡭ࡱࡪࡉࡅࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡩ࡭ࡳ࡫ࡤ࠭ࠢࡥࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡱ࡮࡭ࡨࡵࠢ࡫ࡥࡻ࡫ࠠࡧࡣ࡬ࡰࡪࡪࠧᕖ")
            }
        else:
            cls.bstack1lllll111ll_opy_.shutdown()
            data = {
                bstack11ll111_opy_ (u"ࠪࡷࡹࡵࡰࡠࡶ࡬ࡱࡪ࠭ᕗ"): datetime.datetime.now().isoformat()
            }
            config = {
                bstack11ll111_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᕘ"): cls.default_headers()
            }
            bstack111llll11l_opy_ = bstack11ll111_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡷࡳࡵ࠭ᕙ").format(os.environ[bstack11ll111_opy_ (u"ࠨࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠧᕚ")])
            bstack1lll1ll1ll1_opy_ = cls.request_url(bstack111llll11l_opy_)
            response = bstack11lllll11_opy_(bstack11ll111_opy_ (u"ࠧࡑࡗࡗࠫᕛ"), bstack1lll1ll1ll1_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11ll111_opy_ (u"ࠣࡕࡷࡳࡵࠦࡲࡦࡳࡸࡩࡸࡺࠠ࡯ࡱࡷࠤࡴࡱࠢᕜ"))
    @classmethod
    def bstack1l111ll1l1_opy_(cls):
        if cls.bstack1lllll111ll_opy_ is None:
            return
        cls.bstack1lllll111ll_opy_.shutdown()
    @classmethod
    def bstack1l1ll1ll1_opy_(cls):
        if cls.on():
            print(
                bstack11ll111_opy_ (u"࡙ࠩ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠬᕝ").format(os.environ[bstack11ll111_opy_ (u"ࠥࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠤᕞ")]))
    @classmethod
    def bstack1lll1llllll_opy_(cls):
        if cls.bstack1lllll111ll_opy_ is not None:
            return
        cls.bstack1lllll111ll_opy_ = bstack1lllll11l11_opy_(cls.bstack1lll1llll1l_opy_)
        cls.bstack1lllll111ll_opy_.start()
    @classmethod
    def bstack1l111l1lll_opy_(cls, bstack1l1111llll_opy_, bstack1lll1ll1lll_opy_=bstack11ll111_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᕟ")):
        if not cls.on():
            return
        bstack1l11ll11l1_opy_ = bstack1l1111llll_opy_[bstack11ll111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᕠ")]
        bstack1lll1ll1l11_opy_ = {
            bstack11ll111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᕡ"): bstack11ll111_opy_ (u"ࠧࡕࡧࡶࡸࡤ࡙ࡴࡢࡴࡷࡣ࡚ࡶ࡬ࡰࡣࡧࠫᕢ"),
            bstack11ll111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᕣ"): bstack11ll111_opy_ (u"ࠩࡗࡩࡸࡺ࡟ࡆࡰࡧࡣ࡚ࡶ࡬ࡰࡣࡧࠫᕤ"),
            bstack11ll111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫᕥ"): bstack11ll111_opy_ (u"࡙ࠫ࡫ࡳࡵࡡࡖ࡯࡮ࡶࡰࡦࡦࡢ࡙ࡵࡲ࡯ࡢࡦࠪᕦ"),
            bstack11ll111_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩᕧ"): bstack11ll111_opy_ (u"࠭ࡌࡰࡩࡢ࡙ࡵࡲ࡯ࡢࡦࠪᕨ"),
            bstack11ll111_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᕩ"): bstack11ll111_opy_ (u"ࠨࡊࡲࡳࡰࡥࡓࡵࡣࡵࡸࡤ࡛ࡰ࡭ࡱࡤࡨࠬᕪ"),
            bstack11ll111_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᕫ"): bstack11ll111_opy_ (u"ࠪࡌࡴࡵ࡫ࡠࡇࡱࡨࡤ࡛ࡰ࡭ࡱࡤࡨࠬᕬ"),
            bstack11ll111_opy_ (u"ࠫࡈࡈࡔࡔࡧࡶࡷ࡮ࡵ࡮ࡄࡴࡨࡥࡹ࡫ࡤࠨᕭ"): bstack11ll111_opy_ (u"ࠬࡉࡂࡕࡡࡘࡴࡱࡵࡡࡥࠩᕮ")
        }.get(bstack1l11ll11l1_opy_)
        if bstack1lll1ll1lll_opy_ == bstack11ll111_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡢࡶࡦ࡬ࠬᕯ"):
            cls.bstack1lll1llllll_opy_()
            cls.bstack1lllll111ll_opy_.add(bstack1l1111llll_opy_)
        elif bstack1lll1ll1lll_opy_ == bstack11ll111_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬᕰ"):
            cls.bstack1lll1llll1l_opy_([bstack1l1111llll_opy_], bstack1lll1ll1lll_opy_)
    @classmethod
    @bstack11lll11l1l_opy_(class_method=True)
    def bstack1lll1llll1l_opy_(cls, bstack1l1111llll_opy_, bstack1lll1ll1lll_opy_=bstack11ll111_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧᕱ")):
        config = {
            bstack11ll111_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᕲ"): cls.default_headers()
        }
        response = bstack11lllll11_opy_(bstack11ll111_opy_ (u"ࠪࡔࡔ࡙ࡔࠨᕳ"), cls.request_url(bstack1lll1ll1lll_opy_), bstack1l1111llll_opy_, config)
        bstack11l1ll1lll_opy_ = response.json()
    @classmethod
    @bstack11lll11l1l_opy_(class_method=True)
    def bstack1ll1lll11l_opy_(cls, bstack11llll1111_opy_):
        bstack1lll1ll111l_opy_ = []
        for log in bstack11llll1111_opy_:
            bstack1lll1lllll1_opy_ = {
                bstack11ll111_opy_ (u"ࠫࡰ࡯࡮ࡥࠩᕴ"): bstack11ll111_opy_ (u"࡚ࠬࡅࡔࡖࡢࡐࡔࡍࠧᕵ"),
                bstack11ll111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᕶ"): log[bstack11ll111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᕷ")],
                bstack11ll111_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᕸ"): log[bstack11ll111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᕹ")],
                bstack11ll111_opy_ (u"ࠪ࡬ࡹࡺࡰࡠࡴࡨࡷࡵࡵ࡮ࡴࡧࠪᕺ"): {},
                bstack11ll111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᕻ"): log[bstack11ll111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᕼ")],
            }
            if bstack11ll111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᕽ") in log:
                bstack1lll1lllll1_opy_[bstack11ll111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᕾ")] = log[bstack11ll111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᕿ")]
            elif bstack11ll111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᖀ") in log:
                bstack1lll1lllll1_opy_[bstack11ll111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᖁ")] = log[bstack11ll111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᖂ")]
            bstack1lll1ll111l_opy_.append(bstack1lll1lllll1_opy_)
        cls.bstack1l111l1lll_opy_({
            bstack11ll111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᖃ"): bstack11ll111_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪᖄ"),
            bstack11ll111_opy_ (u"ࠧ࡭ࡱࡪࡷࠬᖅ"): bstack1lll1ll111l_opy_
        })
    @classmethod
    @bstack11lll11l1l_opy_(class_method=True)
    def bstack1lll1ll1l1l_opy_(cls, steps):
        bstack1llll11111l_opy_ = []
        for step in steps:
            bstack1lll1ll11l1_opy_ = {
                bstack11ll111_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭ᖆ"): bstack11ll111_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡔࡖࡈࡔࠬᖇ"),
                bstack11ll111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᖈ"): step[bstack11ll111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᖉ")],
                bstack11ll111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᖊ"): step[bstack11ll111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᖋ")],
                bstack11ll111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᖌ"): step[bstack11ll111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᖍ")],
                bstack11ll111_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫᖎ"): step[bstack11ll111_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬᖏ")]
            }
            if bstack11ll111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᖐ") in step:
                bstack1lll1ll11l1_opy_[bstack11ll111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᖑ")] = step[bstack11ll111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᖒ")]
            elif bstack11ll111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᖓ") in step:
                bstack1lll1ll11l1_opy_[bstack11ll111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᖔ")] = step[bstack11ll111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᖕ")]
            bstack1llll11111l_opy_.append(bstack1lll1ll11l1_opy_)
        cls.bstack1l111l1lll_opy_({
            bstack11ll111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᖖ"): bstack11ll111_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨᖗ"),
            bstack11ll111_opy_ (u"ࠬࡲ࡯ࡨࡵࠪᖘ"): bstack1llll11111l_opy_
        })
    @classmethod
    @bstack11lll11l1l_opy_(class_method=True)
    def bstack1l11llllll_opy_(cls, screenshot):
        cls.bstack1l111l1lll_opy_({
            bstack11ll111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᖙ"): bstack11ll111_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫᖚ"),
            bstack11ll111_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭ᖛ"): [{
                bstack11ll111_opy_ (u"ࠩ࡮࡭ࡳࡪࠧᖜ"): bstack11ll111_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࠬᖝ"),
                bstack11ll111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᖞ"): datetime.datetime.utcnow().isoformat() + bstack11ll111_opy_ (u"ࠬࡠࠧᖟ"),
                bstack11ll111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᖠ"): screenshot[bstack11ll111_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭ᖡ")],
                bstack11ll111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᖢ"): screenshot[bstack11ll111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᖣ")]
            }]
        }, bstack1lll1ll1lll_opy_=bstack11ll111_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨᖤ"))
    @classmethod
    @bstack11lll11l1l_opy_(class_method=True)
    def bstack1llllll1l_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l111l1lll_opy_({
            bstack11ll111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᖥ"): bstack11ll111_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩᖦ"),
            bstack11ll111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨᖧ"): {
                bstack11ll111_opy_ (u"ࠢࡶࡷ࡬ࡨࠧᖨ"): cls.current_test_uuid(),
                bstack11ll111_opy_ (u"ࠣ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠢᖩ"): cls.bstack11llll1l1l_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack11ll111_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡊࡘࡖࠪᖪ"), None) is None or os.environ[bstack11ll111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠫᖫ")] == bstack11ll111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᖬ"):
            return False
        return True
    @classmethod
    def bstack1lllll11l1_opy_(cls):
        return bstack1llll1lll1_opy_(cls.bs_config.get(bstack11ll111_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᖭ"), False))
    @classmethod
    def bstack1lll1l1lll1_opy_(cls, framework):
        return framework in bstack11l1l111l1_opy_
    @staticmethod
    def request_url(url):
        return bstack11ll111_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬᖮ").format(bstack1lll1ll11ll_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack11ll111_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ᖯ"): bstack11ll111_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫᖰ"),
            bstack11ll111_opy_ (u"࡛ࠩ࠱ࡇ࡙ࡔࡂࡅࡎ࠱࡙ࡋࡓࡕࡑࡓࡗࠬᖱ"): bstack11ll111_opy_ (u"ࠪࡸࡷࡻࡥࠨᖲ")
        }
        if os.environ.get(bstack11ll111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬᖳ"), None):
            headers[bstack11ll111_opy_ (u"ࠬࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬᖴ")] = bstack11ll111_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩᖵ").format(os.environ[bstack11ll111_opy_ (u"ࠢࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠣᖶ")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11ll111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᖷ"), None)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11ll111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᖸ"), None)
    @staticmethod
    def bstack1l111l11l1_opy_():
        if getattr(threading.current_thread(), bstack11ll111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᖹ"), None):
            return {
                bstack11ll111_opy_ (u"ࠫࡹࡿࡰࡦࠩᖺ"): bstack11ll111_opy_ (u"ࠬࡺࡥࡴࡶࠪᖻ"),
                bstack11ll111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᖼ"): getattr(threading.current_thread(), bstack11ll111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᖽ"), None)
            }
        if getattr(threading.current_thread(), bstack11ll111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᖾ"), None):
            return {
                bstack11ll111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᖿ"): bstack11ll111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᗀ"),
                bstack11ll111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᗁ"): getattr(threading.current_thread(), bstack11ll111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᗂ"), None)
            }
        return None
    @staticmethod
    def bstack11llll1l1l_opy_(driver):
        return {
            bstack11l111ll11_opy_(): bstack111lll1ll1_opy_(driver)
        }
    @staticmethod
    def bstack1lll1lll1l1_opy_(exception_info, report):
        return [{bstack11ll111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᗃ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11ll1l11ll_opy_(typename):
        if bstack11ll111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥᗄ") in typename:
            return bstack11ll111_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤᗅ")
        return bstack11ll111_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥᗆ")
    @staticmethod
    def bstack1lll1lll111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack11lll1l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l1111l111_opy_(test, hook_name=None):
        bstack1lll1llll11_opy_ = test.parent
        if hook_name in [bstack11ll111_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᗇ"), bstack11ll111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬᗈ"), bstack11ll111_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᗉ"), bstack11ll111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᗊ")]:
            bstack1lll1llll11_opy_ = test
        scope = []
        while bstack1lll1llll11_opy_ is not None:
            scope.append(bstack1lll1llll11_opy_.name)
            bstack1lll1llll11_opy_ = bstack1lll1llll11_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1lll1lll11l_opy_(hook_type):
        if hook_type == bstack11ll111_opy_ (u"ࠢࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠧᗋ"):
            return bstack11ll111_opy_ (u"ࠣࡕࡨࡸࡺࡶࠠࡩࡱࡲ࡯ࠧᗌ")
        elif hook_type == bstack11ll111_opy_ (u"ࠤࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍࠨᗍ"):
            return bstack11ll111_opy_ (u"ࠥࡘࡪࡧࡲࡥࡱࡺࡲࠥ࡮࡯ࡰ࡭ࠥᗎ")
    @staticmethod
    def bstack1lll1l1llll_opy_(bstack11ll1l1l_opy_):
        try:
            if not bstack11lll1l1_opy_.on():
                return bstack11ll1l1l_opy_
            if os.environ.get(bstack11ll111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠤᗏ"), None) == bstack11ll111_opy_ (u"ࠧࡺࡲࡶࡧࠥᗐ"):
                tests = os.environ.get(bstack11ll111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠥᗑ"), None)
                if tests is None or tests == bstack11ll111_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᗒ"):
                    return bstack11ll1l1l_opy_
                bstack11ll1l1l_opy_ = tests.split(bstack11ll111_opy_ (u"ࠨ࠮ࠪᗓ"))
                return bstack11ll1l1l_opy_
        except Exception as exc:
            print(bstack11ll111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡴࡨࡶࡺࡴࠠࡩࡣࡱࡨࡱ࡫ࡲ࠻ࠢࠥᗔ"), str(exc))
        return bstack11ll1l1l_opy_
    @classmethod
    def bstack1l111l1111_opy_(cls, event: str, bstack1l1111llll_opy_: bstack1l111111ll_opy_):
        bstack11llll1l11_opy_ = {
            bstack11ll111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᗕ"): event,
            bstack1l1111llll_opy_.bstack11lll1l11l_opy_(): bstack1l1111llll_opy_.bstack1l111l1ll1_opy_(event)
        }
        bstack11lll1l1_opy_.bstack1l111l1lll_opy_(bstack11llll1l11_opy_)