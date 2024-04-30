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
import re
from bstack_utils.bstack1l1l11l1l1_opy_ import bstack1llllll111l_opy_
def bstack1lllll1l11l_opy_(fixture_name):
    if fixture_name.startswith(bstack11ll111_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᑋ")):
        return bstack11ll111_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᑌ")
    elif fixture_name.startswith(bstack11ll111_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᑍ")):
        return bstack11ll111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪᑎ")
    elif fixture_name.startswith(bstack11ll111_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᑏ")):
        return bstack11ll111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᑐ")
    elif fixture_name.startswith(bstack11ll111_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᑑ")):
        return bstack11ll111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡱࡴࡪࡵ࡭ࡧࠪᑒ")
def bstack1lllll1l1ll_opy_(fixture_name):
    return bool(re.match(bstack11ll111_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥࠨࡧࡷࡱࡧࡹ࡯࡯࡯ࡾࡰࡳࡩࡻ࡬ࡦࠫࡢࡪ࡮ࡾࡴࡶࡴࡨࡣ࠳࠰ࠧᑓ"), fixture_name))
def bstack1lllll1l1l1_opy_(fixture_name):
    return bool(re.match(bstack11ll111_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠ࠰࠭ࠫᑔ"), fixture_name))
def bstack1lllll1llll_opy_(fixture_name):
    return bool(re.match(bstack11ll111_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠ࠰࠭ࠫᑕ"), fixture_name))
def bstack1llllll1l11_opy_(fixture_name):
    if fixture_name.startswith(bstack11ll111_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᑖ")):
        return bstack11ll111_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᑗ"), bstack11ll111_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬᑘ")
    elif fixture_name.startswith(bstack11ll111_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᑙ")):
        return bstack11ll111_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮࡯ࡲࡨࡺࡲࡥࠨᑚ"), bstack11ll111_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧᑛ")
    elif fixture_name.startswith(bstack11ll111_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᑜ")):
        return bstack11ll111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᑝ"), bstack11ll111_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪᑞ")
    elif fixture_name.startswith(bstack11ll111_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᑟ")):
        return bstack11ll111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡱࡴࡪࡵ࡭ࡧࠪᑠ"), bstack11ll111_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡃࡏࡐࠬᑡ")
    return None, None
def bstack1lllll1ll1l_opy_(hook_name):
    if hook_name in [bstack11ll111_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᑢ"), bstack11ll111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ᑣ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1llllll11ll_opy_(hook_name):
    if hook_name in [bstack11ll111_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᑤ"), bstack11ll111_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬᑥ")]:
        return bstack11ll111_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬᑦ")
    elif hook_name in [bstack11ll111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧᑧ"), bstack11ll111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧᑨ")]:
        return bstack11ll111_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧᑩ")
    elif hook_name in [bstack11ll111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᑪ"), bstack11ll111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧᑫ")]:
        return bstack11ll111_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪᑬ")
    elif hook_name in [bstack11ll111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩᑭ"), bstack11ll111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩᑮ")]:
        return bstack11ll111_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡃࡏࡐࠬᑯ")
    return hook_name
def bstack1lllll1ll11_opy_(node, scenario):
    if hasattr(node, bstack11ll111_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬᑰ")):
        parts = node.nodeid.rsplit(bstack11ll111_opy_ (u"ࠦࡠࠨᑱ"))
        params = parts[-1]
        return bstack11ll111_opy_ (u"ࠧࢁࡽࠡ࡝ࡾࢁࠧᑲ").format(scenario.name, params)
    return scenario.name
def bstack1llllll11l1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11ll111_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨᑳ")):
            examples = list(node.callspec.params[bstack11ll111_opy_ (u"ࠧࡠࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤ࡫ࡸࡢ࡯ࡳࡰࡪ࠭ᑴ")].values())
        return examples
    except:
        return []
def bstack1llllll1111_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1llllll1ll1_opy_(report):
    try:
        status = bstack11ll111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᑵ")
        if report.passed or (report.failed and hasattr(report, bstack11ll111_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦᑶ"))):
            status = bstack11ll111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᑷ")
        elif report.skipped:
            status = bstack11ll111_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᑸ")
        bstack1llllll111l_opy_(status)
    except:
        pass
def bstack1llll11lll_opy_(status):
    try:
        bstack1lllll1lll1_opy_ = bstack11ll111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᑹ")
        if status == bstack11ll111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᑺ"):
            bstack1lllll1lll1_opy_ = bstack11ll111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᑻ")
        elif status == bstack11ll111_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᑼ"):
            bstack1lllll1lll1_opy_ = bstack11ll111_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᑽ")
        bstack1llllll111l_opy_(bstack1lllll1lll1_opy_)
    except:
        pass
def bstack1llllll1l1l_opy_(item=None, report=None, summary=None, extra=None):
    return