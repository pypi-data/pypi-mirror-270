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
import requests
import logging
from urllib.parse import urlparse
from datetime import datetime
from bstack_utils.constants import bstack11ll1111l1_opy_ as bstack11ll11l111_opy_
from bstack_utils.bstack111111lll_opy_ import bstack111111lll_opy_
from bstack_utils.helper import bstack1l11llll11_opy_, bstack1llll11ll_opy_, bstack11l1lll1ll_opy_, bstack11ll11ll1l_opy_, bstack11ll1l1l1_opy_, get_host_info, bstack11l1lllll1_opy_, bstack11lllll11_opy_, bstack11lll11l1l_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack11lll11l1l_opy_(class_method=False)
def _11l1lll111_opy_(driver, bstack1l11111ll_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11ll111_opy_ (u"ࠩࡲࡷࡤࡴࡡ࡮ࡧࠪำ"): caps.get(bstack11ll111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩิ"), None),
        bstack11ll111_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨี"): bstack1l11111ll_opy_.get(bstack11ll111_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨึ"), None),
        bstack11ll111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬื"): caps.get(bstack11ll111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩุࠬ"), None),
        bstack11ll111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰูࠪ"): caps.get(bstack11ll111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰฺࠪ"), None)
    }
  except Exception as error:
    logger.debug(bstack11ll111_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤ࠿ࠦࠧ฻") + str(error))
  return response
def bstack111ll1lll_opy_(config):
  return config.get(bstack11ll111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ฼"), False) or any([p.get(bstack11ll111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ฽"), False) == True for p in config.get(bstack11ll111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ฾"), [])])
def bstack1l1l1l1l1_opy_(config, bstack1l1l111lll_opy_):
  try:
    if not bstack1llll11ll_opy_(config):
      return False
    bstack11l1ll1l1l_opy_ = config.get(bstack11ll111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ฿"), False)
    bstack11l1llllll_opy_ = config[bstack11ll111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫเ")][bstack1l1l111lll_opy_].get(bstack11ll111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩแ"), None)
    if bstack11l1llllll_opy_ != None:
      bstack11l1ll1l1l_opy_ = bstack11l1llllll_opy_
    bstack11l1ll1ll1_opy_ = os.getenv(bstack11ll111_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨโ")) is not None and len(os.getenv(bstack11ll111_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩใ"))) > 0 and os.getenv(bstack11ll111_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪไ")) != bstack11ll111_opy_ (u"࠭࡮ࡶ࡮࡯ࠫๅ")
    return bstack11l1ll1l1l_opy_ and bstack11l1ll1ll1_opy_
  except Exception as error:
    logger.debug(bstack11ll111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡶࡦࡴ࡬ࡪࡾ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤ࠿ࠦࠧๆ") + str(error))
  return False
def bstack1ll111l1l_opy_(bstack11ll111l1l_opy_, test_tags):
  bstack11ll111l1l_opy_ = os.getenv(bstack11ll111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ็"))
  if bstack11ll111l1l_opy_ is None:
    return True
  bstack11ll111l1l_opy_ = json.loads(bstack11ll111l1l_opy_)
  try:
    include_tags = bstack11ll111l1l_opy_[bstack11ll111_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫่ࠧ")] if bstack11ll111_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ้") in bstack11ll111l1l_opy_ and isinstance(bstack11ll111l1l_opy_[bstack11ll111_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦ๊ࠩ")], list) else []
    exclude_tags = bstack11ll111l1l_opy_[bstack11ll111_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧ๋ࠪ")] if bstack11ll111_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ์") in bstack11ll111l1l_opy_ and isinstance(bstack11ll111l1l_opy_[bstack11ll111_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬํ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11ll111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡶࡢ࡮࡬ࡨࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡨࡧ࡮࡯࡫ࡱ࡫࠳ࠦࡅࡳࡴࡲࡶࠥࡀࠠࠣ๎") + str(error))
  return False
def bstack1ll11l1ll1_opy_(config, bstack11ll111lll_opy_, bstack11ll11l1l1_opy_, bstack11ll11lll1_opy_):
  bstack11ll11111l_opy_ = bstack11l1lll1ll_opy_(config)
  bstack11ll11l11l_opy_ = bstack11ll11ll1l_opy_(config)
  if bstack11ll11111l_opy_ is None or bstack11ll11l11l_opy_ is None:
    logger.error(bstack11ll111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡷࡻ࡮ࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࡐ࡭ࡸࡹࡩ࡯ࡩࠣࡥࡺࡺࡨࡦࡰࡷ࡭ࡨࡧࡴࡪࡱࡱࠤࡹࡵ࡫ࡦࡰࠪ๏"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11ll111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ๐"), bstack11ll111_opy_ (u"ࠫࢀࢃࠧ๑")))
    data = {
        bstack11ll111_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ๒"): config[bstack11ll111_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ๓")],
        bstack11ll111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ๔"): config.get(bstack11ll111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ๕"), os.path.basename(os.getcwd())),
        bstack11ll111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡕ࡫ࡰࡩࠬ๖"): bstack1l11llll11_opy_(),
        bstack11ll111_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨ๗"): config.get(bstack11ll111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ๘"), bstack11ll111_opy_ (u"ࠬ࠭๙")),
        bstack11ll111_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭๚"): {
            bstack11ll111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡑࡥࡲ࡫ࠧ๛"): bstack11ll111lll_opy_,
            bstack11ll111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ๜"): bstack11ll11l1l1_opy_,
            bstack11ll111_opy_ (u"ࠩࡶࡨࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭๝"): __version__,
            bstack11ll111_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬ๞"): bstack11ll111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ๟"),
            bstack11ll111_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ๠"): bstack11ll111_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨ๡"),
            bstack11ll111_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ๢"): bstack11ll11lll1_opy_
        },
        bstack11ll111_opy_ (u"ࠨࡵࡨࡸࡹ࡯࡮ࡨࡵࠪ๣"): settings,
        bstack11ll111_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࡆࡳࡳࡺࡲࡰ࡮ࠪ๤"): bstack11l1lllll1_opy_(),
        bstack11ll111_opy_ (u"ࠪࡧ࡮ࡏ࡮ࡧࡱࠪ๥"): bstack11ll1l1l1_opy_(),
        bstack11ll111_opy_ (u"ࠫ࡭ࡵࡳࡵࡋࡱࡪࡴ࠭๦"): get_host_info(),
        bstack11ll111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧ๧"): bstack1llll11ll_opy_(config)
    }
    headers = {
        bstack11ll111_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ๨"): bstack11ll111_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ๩"),
    }
    config = {
        bstack11ll111_opy_ (u"ࠨࡣࡸࡸ࡭࠭๪"): (bstack11ll11111l_opy_, bstack11ll11l11l_opy_),
        bstack11ll111_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ๫"): headers
    }
    response = bstack11lllll11_opy_(bstack11ll111_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ๬"), bstack11ll11l111_opy_ + bstack11ll111_opy_ (u"ࠫ࠴ࡼ࠲࠰ࡶࡨࡷࡹࡥࡲࡶࡰࡶࠫ๭"), data, config)
    bstack11l1ll1lll_opy_ = response.json()
    if bstack11l1ll1lll_opy_[bstack11ll111_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭๮")]:
      parsed = json.loads(os.getenv(bstack11ll111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ๯"), bstack11ll111_opy_ (u"ࠧࡼࡿࠪ๰")))
      parsed[bstack11ll111_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ๱")] = bstack11l1ll1lll_opy_[bstack11ll111_opy_ (u"ࠩࡧࡥࡹࡧࠧ๲")][bstack11ll111_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ๳")]
      os.environ[bstack11ll111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ๴")] = json.dumps(parsed)
      bstack111111lll_opy_.bstack11l1lll1l1_opy_(bstack11l1ll1lll_opy_[bstack11ll111_opy_ (u"ࠬࡪࡡࡵࡣࠪ๵")][bstack11ll111_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧ๶")])
      bstack111111lll_opy_.bstack11ll1111ll_opy_(bstack11l1ll1lll_opy_[bstack11ll111_opy_ (u"ࠧࡥࡣࡷࡥࠬ๷")][bstack11ll111_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪ๸")])
      bstack111111lll_opy_.store()
      return bstack11l1ll1lll_opy_[bstack11ll111_opy_ (u"ࠩࡧࡥࡹࡧࠧ๹")][bstack11ll111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡗࡳࡰ࡫࡮ࠨ๺")], bstack11l1ll1lll_opy_[bstack11ll111_opy_ (u"ࠫࡩࡧࡴࡢࠩ๻")][bstack11ll111_opy_ (u"ࠬ࡯ࡤࠨ๼")]
    else:
      logger.error(bstack11ll111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࠧ๽") + bstack11l1ll1lll_opy_[bstack11ll111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ๾")])
      if bstack11l1ll1lll_opy_[bstack11ll111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ๿")] == bstack11ll111_opy_ (u"ࠩࡌࡲࡻࡧ࡬ࡪࡦࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡴࡦࡹࡳࡦࡦ࠱ࠫ຀"):
        for bstack11l1lll11l_opy_ in bstack11l1ll1lll_opy_[bstack11ll111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡵࠪກ")]:
          logger.error(bstack11l1lll11l_opy_[bstack11ll111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬຂ")])
      return None, None
  except Exception as error:
    logger.error(bstack11ll111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥࠨ຃") +  str(error))
    return None, None
def bstack1l11llll_opy_():
  if os.getenv(bstack11ll111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫຄ")) is None:
    return {
        bstack11ll111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ຅"): bstack11ll111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧຆ"),
        bstack11ll111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪງ"): bstack11ll111_opy_ (u"ࠪࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤ࡭ࡧࡤࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠩຈ")
    }
  data = {bstack11ll111_opy_ (u"ࠫࡪࡴࡤࡕ࡫ࡰࡩࠬຉ"): bstack1l11llll11_opy_()}
  headers = {
      bstack11ll111_opy_ (u"ࠬࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬຊ"): bstack11ll111_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࠧ຋") + os.getenv(bstack11ll111_opy_ (u"ࠢࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠧຌ")),
      bstack11ll111_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧຍ"): bstack11ll111_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬຎ")
  }
  response = bstack11lllll11_opy_(bstack11ll111_opy_ (u"ࠪࡔ࡚࡚ࠧຏ"), bstack11ll11l111_opy_ + bstack11ll111_opy_ (u"ࠫ࠴ࡺࡥࡴࡶࡢࡶࡺࡴࡳ࠰ࡵࡷࡳࡵ࠭ຐ"), data, { bstack11ll111_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ຑ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11ll111_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡗࡩࡸࡺࠠࡓࡷࡱࠤࡲࡧࡲ࡬ࡧࡧࠤࡦࡹࠠࡤࡱࡰࡴࡱ࡫ࡴࡦࡦࠣࡥࡹࠦࠢຒ") + datetime.utcnow().isoformat() + bstack11ll111_opy_ (u"࡛ࠧࠩຓ"))
      return {bstack11ll111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨດ"): bstack11ll111_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪຕ"), bstack11ll111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫຖ"): bstack11ll111_opy_ (u"ࠫࠬທ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11ll111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡࡥࡲࡱࡵࡲࡥࡵ࡫ࡲࡲࠥࡵࡦࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡙࡫ࡳࡵࠢࡕࡹࡳࡀࠠࠣຘ") + str(error))
    return {
        bstack11ll111_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ນ"): bstack11ll111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ບ"),
        bstack11ll111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩປ"): str(error)
    }
def bstack11l1lll1_opy_(caps, options):
  try:
    bstack11ll11ll11_opy_ = caps.get(bstack11ll111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪຜ"), {}).get(bstack11ll111_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧຝ"), caps.get(bstack11ll111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫພ"), bstack11ll111_opy_ (u"ࠬ࠭ຟ")))
    if bstack11ll11ll11_opy_:
      logger.warn(bstack11ll111_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡄࡦࡵ࡮ࡸࡴࡶࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥຠ"))
      return False
    browser = caps.get(bstack11ll111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬມ"), bstack11ll111_opy_ (u"ࠨࠩຢ")).lower()
    if browser != bstack11ll111_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩຣ"):
      logger.warn(bstack11ll111_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ຤"))
      return False
    browser_version = caps.get(bstack11ll111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬລ"), caps.get(bstack11ll111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ຦")))
    if browser_version and browser_version != bstack11ll111_opy_ (u"࠭࡬ࡢࡶࡨࡷࡹ࠭ວ") and int(browser_version.split(bstack11ll111_opy_ (u"ࠧ࠯ࠩຨ"))[0]) <= 94:
      logger.warn(bstack11ll111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰࠣ࡫ࡷ࡫ࡡࡵࡧࡵࠤࡹ࡮ࡡ࡯ࠢ࠼࠸࠳ࠨຩ"))
      return False
    if not options is None:
      bstack11l1llll1l_opy_ = options.to_capabilities().get(bstack11ll111_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧສ"), {})
      if bstack11ll111_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹࠧຫ") in bstack11l1llll1l_opy_.get(bstack11ll111_opy_ (u"ࠫࡦࡸࡧࡴࠩຬ"), []):
        logger.warn(bstack11ll111_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡷࠤࡷࡻ࡮ࠡࡱࡱࠤࡱ࡫ࡧࡢࡥࡼࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲࡙ࠥࡷࡪࡶࡦ࡬ࠥࡺ࡯ࠡࡰࡨࡻࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩࠥࡵࡲࠡࡣࡹࡳ࡮ࡪࠠࡶࡵ࡬ࡲ࡬ࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠢອ"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack11ll111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡡ࡭࡫ࡧࡥࡹ࡫ࠠࡢ࠳࠴ࡽࠥࡹࡵࡱࡲࡲࡶࡹࠦ࠺ࠣຮ") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack11ll11l1ll_opy_ = config.get(bstack11ll111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧຯ"), {})
    bstack11ll11l1ll_opy_[bstack11ll111_opy_ (u"ࠨࡣࡸࡸ࡭࡚࡯࡬ࡧࡱࠫະ")] = os.getenv(bstack11ll111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧັ"))
    bstack11ll111l11_opy_ = json.loads(os.getenv(bstack11ll111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫາ"), bstack11ll111_opy_ (u"ࠫࢀࢃࠧຳ"))).get(bstack11ll111_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ິ"))
    caps[bstack11ll111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ີ")] = True
    if bstack11ll111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨຶ") in caps:
      caps[bstack11ll111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩື")][bstack11ll111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴຸࠩ")] = bstack11ll11l1ll_opy_
      caps[bstack11ll111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶູࠫ")][bstack11ll111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶ຺ࠫ")][bstack11ll111_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ົ")] = bstack11ll111l11_opy_
    else:
      caps[bstack11ll111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬຼ")] = bstack11ll11l1ll_opy_
      caps[bstack11ll111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ຽ")][bstack11ll111_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ຾")] = bstack11ll111l11_opy_
  except Exception as error:
    logger.debug(bstack11ll111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠯ࠢࡈࡶࡷࡵࡲ࠻ࠢࠥ຿") +  str(error))
def bstack1ll111ll1_opy_(driver, bstack11ll11llll_opy_):
  try:
    setattr(driver, bstack11ll111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪເ"), True)
    session = driver.session_id
    if session:
      bstack11l1llll11_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack11l1llll11_opy_ = False
      bstack11l1llll11_opy_ = url.scheme in [bstack11ll111_opy_ (u"ࠦ࡭ࡺࡴࡱࠤແ"), bstack11ll111_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦໂ")]
      if bstack11l1llll11_opy_:
        if bstack11ll11llll_opy_:
          logger.info(bstack11ll111_opy_ (u"ࠨࡓࡦࡶࡸࡴࠥ࡬࡯ࡳࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡬ࡦࡹࠠࡴࡶࡤࡶࡹ࡫ࡤ࠯ࠢࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡤࡨ࡫࡮ࡴࠠ࡮ࡱࡰࡩࡳࡺࡡࡳ࡫࡯ࡽ࠳ࠨໃ"))
      return bstack11ll11llll_opy_
  except Exception as e:
    logger.error(bstack11ll111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡣࡵࡸ࡮ࡴࡧࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥໄ") + str(e))
    return False
def bstack1lllll11l_opy_(driver, class_name, name, module_name, path, bstack1l11111ll_opy_):
  try:
    bstack11ll1ll1ll_opy_ = [class_name] if not class_name is None else []
    bstack11ll111111_opy_ = {
        bstack11ll111_opy_ (u"ࠣࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸࠨ໅"): True,
        bstack11ll111_opy_ (u"ࠤࡷࡩࡸࡺࡄࡦࡶࡤ࡭ࡱࡹࠢໆ"): {
            bstack11ll111_opy_ (u"ࠥࡲࡦࡳࡥࠣ໇"): name,
            bstack11ll111_opy_ (u"ࠦࡹ࡫ࡳࡵࡔࡸࡲࡎࡪ່ࠢ"): os.environ.get(bstack11ll111_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡔࡆࡕࡗࡣࡗ࡛ࡎࡠࡋࡇ້ࠫ")),
            bstack11ll111_opy_ (u"ࠨࡦࡪ࡮ࡨࡔࡦࡺࡨ໊ࠣ"): str(path),
            bstack11ll111_opy_ (u"ࠢࡴࡥࡲࡴࡪࡒࡩࡴࡶ໋ࠥ"): [module_name, *bstack11ll1ll1ll_opy_, name],
        },
        bstack11ll111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥ໌"): _11l1lll111_opy_(driver, bstack1l11111ll_opy_)
    }
    logger.debug(bstack11ll111_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡧࡶࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠬໍ"))
    logger.debug(driver.execute_async_script(bstack111111lll_opy_.perform_scan, {bstack11ll111_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠥ໎"): name}))
    logger.debug(driver.execute_async_script(bstack111111lll_opy_.bstack11ll111ll1_opy_, bstack11ll111111_opy_))
    logger.info(bstack11ll111_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠢ໏"))
  except Exception as bstack11ll1l1111_opy_:
    logger.error(bstack11ll111_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡣࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡨࡲࡶࠥࡺࡨࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢ໐") + str(path) + bstack11ll111_opy_ (u"ࠨࠠࡆࡴࡵࡳࡷࠦ࠺ࠣ໑") + str(bstack11ll1l1111_opy_))