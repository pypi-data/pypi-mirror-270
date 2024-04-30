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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.helper import bstack11l11l1111_opy_, bstack1lll1l11_opy_, bstack1111lll1l_opy_, bstack111l1l1ll_opy_, \
    bstack11l11ll1l1_opy_
def bstack1l11111l_opy_(bstack1llll1l1lll_opy_):
    for driver in bstack1llll1l1lll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll1111ll_opy_(driver, status, reason=bstack11ll111_opy_ (u"ࠬ࠭ᒀ")):
    bstack1111l1111_opy_ = Config.bstack1ll111l11_opy_()
    if bstack1111l1111_opy_.bstack11ll1l1ll1_opy_():
        return
    bstack1111l111_opy_ = bstack1l1l1lll1l_opy_(bstack11ll111_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᒁ"), bstack11ll111_opy_ (u"ࠧࠨᒂ"), status, reason, bstack11ll111_opy_ (u"ࠨࠩᒃ"), bstack11ll111_opy_ (u"ࠩࠪᒄ"))
    driver.execute_script(bstack1111l111_opy_)
def bstack1lll1llll_opy_(page, status, reason=bstack11ll111_opy_ (u"ࠪࠫᒅ")):
    try:
        if page is None:
            return
        bstack1111l1111_opy_ = Config.bstack1ll111l11_opy_()
        if bstack1111l1111_opy_.bstack11ll1l1ll1_opy_():
            return
        bstack1111l111_opy_ = bstack1l1l1lll1l_opy_(bstack11ll111_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᒆ"), bstack11ll111_opy_ (u"ࠬ࠭ᒇ"), status, reason, bstack11ll111_opy_ (u"࠭ࠧᒈ"), bstack11ll111_opy_ (u"ࠧࠨᒉ"))
        page.evaluate(bstack11ll111_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᒊ"), bstack1111l111_opy_)
    except Exception as e:
        print(bstack11ll111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࢀࢃࠢᒋ"), e)
def bstack1l1l1lll1l_opy_(type, name, status, reason, bstack1ll1lll11_opy_, bstack11l1l1lll_opy_):
    bstack11111lll_opy_ = {
        bstack11ll111_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪᒌ"): type,
        bstack11ll111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᒍ"): {}
    }
    if type == bstack11ll111_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧᒎ"):
        bstack11111lll_opy_[bstack11ll111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᒏ")][bstack11ll111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᒐ")] = bstack1ll1lll11_opy_
        bstack11111lll_opy_[bstack11ll111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᒑ")][bstack11ll111_opy_ (u"ࠩࡧࡥࡹࡧࠧᒒ")] = json.dumps(str(bstack11l1l1lll_opy_))
    if type == bstack11ll111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᒓ"):
        bstack11111lll_opy_[bstack11ll111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᒔ")][bstack11ll111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᒕ")] = name
    if type == bstack11ll111_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᒖ"):
        bstack11111lll_opy_[bstack11ll111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᒗ")][bstack11ll111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᒘ")] = status
        if status == bstack11ll111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᒙ") and str(reason) != bstack11ll111_opy_ (u"ࠥࠦᒚ"):
            bstack11111lll_opy_[bstack11ll111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᒛ")][bstack11ll111_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᒜ")] = json.dumps(str(reason))
    bstack1lll1lllll_opy_ = bstack11ll111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫᒝ").format(json.dumps(bstack11111lll_opy_))
    return bstack1lll1lllll_opy_
def bstack11l111l1_opy_(url, config, logger, bstack11111ll11_opy_=False):
    hostname = bstack1lll1l11_opy_(url)
    is_private = bstack111l1l1ll_opy_(hostname)
    try:
        if is_private or bstack11111ll11_opy_:
            file_path = bstack11l11l1111_opy_(bstack11ll111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᒞ"), bstack11ll111_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧᒟ"), logger)
            if os.environ.get(bstack11ll111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᒠ")) and eval(
                    os.environ.get(bstack11ll111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᒡ"))):
                return
            if (bstack11ll111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᒢ") in config and not config[bstack11ll111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᒣ")]):
                os.environ[bstack11ll111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫᒤ")] = str(True)
                bstack1llll1l1ll1_opy_ = {bstack11ll111_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩᒥ"): hostname}
                bstack11l11ll1l1_opy_(bstack11ll111_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧᒦ"), bstack11ll111_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧᒧ"), bstack1llll1l1ll1_opy_, logger)
    except Exception as e:
        pass
def bstack1l1l11l1ll_opy_(caps, bstack1llll1l1l1l_opy_):
    if bstack11ll111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᒨ") in caps:
        caps[bstack11ll111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᒩ")][bstack11ll111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫᒪ")] = True
        if bstack1llll1l1l1l_opy_:
            caps[bstack11ll111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᒫ")][bstack11ll111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᒬ")] = bstack1llll1l1l1l_opy_
    else:
        caps[bstack11ll111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭ᒭ")] = True
        if bstack1llll1l1l1l_opy_:
            caps[bstack11ll111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᒮ")] = bstack1llll1l1l1l_opy_
def bstack1llllll111l_opy_(bstack11lll11lll_opy_):
    bstack1llll1ll111_opy_ = bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧᒯ"), bstack11ll111_opy_ (u"ࠫࠬᒰ"))
    if bstack1llll1ll111_opy_ == bstack11ll111_opy_ (u"ࠬ࠭ᒱ") or bstack1llll1ll111_opy_ == bstack11ll111_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᒲ"):
        threading.current_thread().testStatus = bstack11lll11lll_opy_
    else:
        if bstack11lll11lll_opy_ == bstack11ll111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᒳ"):
            threading.current_thread().testStatus = bstack11lll11lll_opy_