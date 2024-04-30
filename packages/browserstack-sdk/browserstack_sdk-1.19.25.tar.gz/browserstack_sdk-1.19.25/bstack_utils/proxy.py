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
from urllib.parse import urlparse
from bstack_utils.messages import bstack111l1111l1_opy_
def bstack1llllllll1l_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1llllllll11_opy_(bstack1lllllll1l1_opy_, bstack1lllllll1ll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1lllllll1l1_opy_):
        with open(bstack1lllllll1l1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1llllllll1l_opy_(bstack1lllllll1l1_opy_):
        pac = get_pac(url=bstack1lllllll1l1_opy_)
    else:
        raise Exception(bstack11ll111_opy_ (u"࠭ࡐࡢࡥࠣࡪ࡮ࡲࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠼ࠣࡿࢂ࠭ᐦ").format(bstack1lllllll1l1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11ll111_opy_ (u"ࠢ࠹࠰࠻࠲࠽࠴࠸ࠣᐧ"), 80))
        bstack1llllll1lll_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1llllll1lll_opy_ = bstack11ll111_opy_ (u"ࠨ࠲࠱࠴࠳࠶࠮࠱ࠩᐨ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1lllllll1ll_opy_, bstack1llllll1lll_opy_)
    return proxy_url
def bstack1l11l1ll_opy_(config):
    return bstack11ll111_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᐩ") in config or bstack11ll111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᐪ") in config
def bstack1ll1l1l11l_opy_(config):
    if not bstack1l11l1ll_opy_(config):
        return
    if config.get(bstack11ll111_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᐫ")):
        return config.get(bstack11ll111_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᐬ"))
    if config.get(bstack11ll111_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᐭ")):
        return config.get(bstack11ll111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᐮ"))
def bstack1l1l1l11l1_opy_(config, bstack1lllllll1ll_opy_):
    proxy = bstack1ll1l1l11l_opy_(config)
    proxies = {}
    if config.get(bstack11ll111_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᐯ")) or config.get(bstack11ll111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᐰ")):
        if proxy.endswith(bstack11ll111_opy_ (u"ࠪ࠲ࡵࡧࡣࠨᐱ")):
            proxies = bstack1ll11lll11_opy_(proxy, bstack1lllllll1ll_opy_)
        else:
            proxies = {
                bstack11ll111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᐲ"): proxy
            }
    return proxies
def bstack1ll11lll11_opy_(bstack1lllllll1l1_opy_, bstack1lllllll1ll_opy_):
    proxies = {}
    global bstack1lllllll11l_opy_
    if bstack11ll111_opy_ (u"ࠬࡖࡁࡄࡡࡓࡖࡔ࡞࡙ࠨᐳ") in globals():
        return bstack1lllllll11l_opy_
    try:
        proxy = bstack1llllllll11_opy_(bstack1lllllll1l1_opy_, bstack1lllllll1ll_opy_)
        if bstack11ll111_opy_ (u"ࠨࡄࡊࡔࡈࡇ࡙ࠨᐴ") in proxy:
            proxies = {}
        elif bstack11ll111_opy_ (u"ࠢࡉࡖࡗࡔࠧᐵ") in proxy or bstack11ll111_opy_ (u"ࠣࡊࡗࡘࡕ࡙ࠢᐶ") in proxy or bstack11ll111_opy_ (u"ࠤࡖࡓࡈࡑࡓࠣᐷ") in proxy:
            bstack1lllllll111_opy_ = proxy.split(bstack11ll111_opy_ (u"ࠥࠤࠧᐸ"))
            if bstack11ll111_opy_ (u"ࠦ࠿࠵࠯ࠣᐹ") in bstack11ll111_opy_ (u"ࠧࠨᐺ").join(bstack1lllllll111_opy_[1:]):
                proxies = {
                    bstack11ll111_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᐻ"): bstack11ll111_opy_ (u"ࠢࠣᐼ").join(bstack1lllllll111_opy_[1:])
                }
            else:
                proxies = {
                    bstack11ll111_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᐽ"): str(bstack1lllllll111_opy_[0]).lower() + bstack11ll111_opy_ (u"ࠤ࠽࠳࠴ࠨᐾ") + bstack11ll111_opy_ (u"ࠥࠦᐿ").join(bstack1lllllll111_opy_[1:])
                }
        elif bstack11ll111_opy_ (u"ࠦࡕࡘࡏ࡙࡛ࠥᑀ") in proxy:
            bstack1lllllll111_opy_ = proxy.split(bstack11ll111_opy_ (u"ࠧࠦࠢᑁ"))
            if bstack11ll111_opy_ (u"ࠨ࠺࠰࠱ࠥᑂ") in bstack11ll111_opy_ (u"ࠢࠣᑃ").join(bstack1lllllll111_opy_[1:]):
                proxies = {
                    bstack11ll111_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᑄ"): bstack11ll111_opy_ (u"ࠤࠥᑅ").join(bstack1lllllll111_opy_[1:])
                }
            else:
                proxies = {
                    bstack11ll111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᑆ"): bstack11ll111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᑇ") + bstack11ll111_opy_ (u"ࠧࠨᑈ").join(bstack1lllllll111_opy_[1:])
                }
        else:
            proxies = {
                bstack11ll111_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᑉ"): proxy
            }
    except Exception as e:
        print(bstack11ll111_opy_ (u"ࠢࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠦᑊ"), bstack111l1111l1_opy_.format(bstack1lllllll1l1_opy_, str(e)))
    bstack1lllllll11l_opy_ = proxies
    return proxies