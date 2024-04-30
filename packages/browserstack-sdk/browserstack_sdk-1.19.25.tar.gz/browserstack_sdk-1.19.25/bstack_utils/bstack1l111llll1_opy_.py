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
from uuid import uuid4
from bstack_utils.helper import bstack1l11llll11_opy_, bstack111llllll1_opy_
from bstack_utils.bstack1lll11l1_opy_ import bstack1llllll11l1_opy_
class bstack1l111111ll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack11lllll11l_opy_=None, framework=None, tags=[], scope=[], bstack1llll11ll11_opy_=None, bstack1llll1111l1_opy_=True, bstack1llll11l1l1_opy_=None, bstack1l11ll11l1_opy_=None, result=None, duration=None, bstack11lllll111_opy_=None, meta={}):
        self.bstack11lllll111_opy_ = bstack11lllll111_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1llll1111l1_opy_:
            self.uuid = uuid4().__str__()
        self.bstack11lllll11l_opy_ = bstack11lllll11l_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1llll11ll11_opy_ = bstack1llll11ll11_opy_
        self.bstack1llll11l1l1_opy_ = bstack1llll11l1l1_opy_
        self.bstack1l11ll11l1_opy_ = bstack1l11ll11l1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack11llllll11_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack1llll1l11ll_opy_(self):
        bstack1llll1111ll_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11ll111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫᒴ"): bstack1llll1111ll_opy_,
            bstack11ll111_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫᒵ"): bstack1llll1111ll_opy_,
            bstack11ll111_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨᒶ"): bstack1llll1111ll_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11ll111_opy_ (u"࡚ࠦࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡺࡳࡥ࡯ࡶ࠽ࠤࠧᒷ") + key)
            setattr(self, key, val)
    def bstack1llll111l11_opy_(self):
        return {
            bstack11ll111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᒸ"): self.name,
            bstack11ll111_opy_ (u"࠭ࡢࡰࡦࡼࠫᒹ"): {
                bstack11ll111_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬᒺ"): bstack11ll111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨᒻ"),
                bstack11ll111_opy_ (u"ࠩࡦࡳࡩ࡫ࠧᒼ"): self.code
            },
            bstack11ll111_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪᒽ"): self.scope,
            bstack11ll111_opy_ (u"ࠫࡹࡧࡧࡴࠩᒾ"): self.tags,
            bstack11ll111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᒿ"): self.framework,
            bstack11ll111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᓀ"): self.bstack11lllll11l_opy_
        }
    def bstack1llll11l111_opy_(self):
        return {
         bstack11ll111_opy_ (u"ࠧ࡮ࡧࡷࡥࠬᓁ"): self.meta
        }
    def bstack1llll1l1111_opy_(self):
        return {
            bstack11ll111_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡓࡧࡵࡹࡳࡖࡡࡳࡣࡰࠫᓂ"): {
                bstack11ll111_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪ࠭ᓃ"): self.bstack1llll11ll11_opy_
            }
        }
    def bstack1llll11l11l_opy_(self, bstack1llll1l111l_opy_, details):
        step = next(filter(lambda st: st[bstack11ll111_opy_ (u"ࠪ࡭ࡩ࠭ᓄ")] == bstack1llll1l111l_opy_, self.meta[bstack11ll111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᓅ")]), None)
        step.update(details)
    def bstack1llll11lll1_opy_(self, bstack1llll1l111l_opy_):
        step = next(filter(lambda st: st[bstack11ll111_opy_ (u"ࠬ࡯ࡤࠨᓆ")] == bstack1llll1l111l_opy_, self.meta[bstack11ll111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᓇ")]), None)
        step.update({
            bstack11ll111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᓈ"): bstack1l11llll11_opy_()
        })
    def bstack1l11111l11_opy_(self, bstack1llll1l111l_opy_, result, duration=None):
        bstack1llll11l1l1_opy_ = bstack1l11llll11_opy_()
        if bstack1llll1l111l_opy_ is not None and self.meta.get(bstack11ll111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᓉ")):
            step = next(filter(lambda st: st[bstack11ll111_opy_ (u"ࠩ࡬ࡨࠬᓊ")] == bstack1llll1l111l_opy_, self.meta[bstack11ll111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᓋ")]), None)
            step.update({
                bstack11ll111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᓌ"): bstack1llll11l1l1_opy_,
                bstack11ll111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧᓍ"): duration if duration else bstack111llllll1_opy_(step[bstack11ll111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᓎ")], bstack1llll11l1l1_opy_),
                bstack11ll111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᓏ"): result.result,
                bstack11ll111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩᓐ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1llll111ll1_opy_):
        if self.meta.get(bstack11ll111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᓑ")):
            self.meta[bstack11ll111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᓒ")].append(bstack1llll111ll1_opy_)
        else:
            self.meta[bstack11ll111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᓓ")] = [ bstack1llll111ll1_opy_ ]
    def bstack1llll1l11l1_opy_(self):
        return {
            bstack11ll111_opy_ (u"ࠬࡻࡵࡪࡦࠪᓔ"): self.bstack11llllll11_opy_(),
            **self.bstack1llll111l11_opy_(),
            **self.bstack1llll1l11ll_opy_(),
            **self.bstack1llll11l111_opy_()
        }
    def bstack1llll111lll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11ll111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᓕ"): self.bstack1llll11l1l1_opy_,
            bstack11ll111_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨᓖ"): self.duration,
            bstack11ll111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᓗ"): self.result.result
        }
        if data[bstack11ll111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᓘ")] == bstack11ll111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᓙ"):
            data[bstack11ll111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᓚ")] = self.result.bstack11ll1l11ll_opy_()
            data[bstack11ll111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᓛ")] = [{bstack11ll111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᓜ"): self.result.bstack11l111llll_opy_()}]
        return data
    def bstack1llll1l1l11_opy_(self):
        return {
            bstack11ll111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᓝ"): self.bstack11llllll11_opy_(),
            **self.bstack1llll111l11_opy_(),
            **self.bstack1llll1l11ll_opy_(),
            **self.bstack1llll111lll_opy_(),
            **self.bstack1llll11l111_opy_()
        }
    def bstack1l111l1ll1_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11ll111_opy_ (u"ࠨࡕࡷࡥࡷࡺࡥࡥࠩᓞ") in event:
            return self.bstack1llll1l11l1_opy_()
        elif bstack11ll111_opy_ (u"ࠩࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᓟ") in event:
            return self.bstack1llll1l1l11_opy_()
    def bstack11lll1l11l_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1llll11l1l1_opy_ = time if time else bstack1l11llll11_opy_()
        self.duration = duration if duration else bstack111llllll1_opy_(self.bstack11lllll11l_opy_, self.bstack1llll11l1l1_opy_)
        if result:
            self.result = result
class bstack1l111111l1_opy_(bstack1l111111ll_opy_):
    def __init__(self, hooks=[], bstack1l11l111l1_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l11l111l1_opy_ = bstack1l11l111l1_opy_
        super().__init__(*args, **kwargs, bstack1l11ll11l1_opy_=bstack11ll111_opy_ (u"ࠪࡸࡪࡹࡴࠨᓠ"))
    @classmethod
    def bstack1llll111l1l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11ll111_opy_ (u"ࠫ࡮ࡪࠧᓡ"): id(step),
                bstack11ll111_opy_ (u"ࠬࡺࡥࡹࡶࠪᓢ"): step.name,
                bstack11ll111_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧᓣ"): step.keyword,
            })
        return bstack1l111111l1_opy_(
            **kwargs,
            meta={
                bstack11ll111_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨᓤ"): {
                    bstack11ll111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᓥ"): feature.name,
                    bstack11ll111_opy_ (u"ࠩࡳࡥࡹ࡮ࠧᓦ"): feature.filename,
                    bstack11ll111_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨᓧ"): feature.description
                },
                bstack11ll111_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ᓨ"): {
                    bstack11ll111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᓩ"): scenario.name
                },
                bstack11ll111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᓪ"): steps,
                bstack11ll111_opy_ (u"ࠧࡦࡺࡤࡱࡵࡲࡥࡴࠩᓫ"): bstack1llllll11l1_opy_(test)
            }
        )
    def bstack1llll11l1ll_opy_(self):
        return {
            bstack11ll111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᓬ"): self.hooks
        }
    def bstack1llll11llll_opy_(self):
        if self.bstack1l11l111l1_opy_:
            return {
                bstack11ll111_opy_ (u"ࠩ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳࠨᓭ"): self.bstack1l11l111l1_opy_
            }
        return {}
    def bstack1llll1l1l11_opy_(self):
        return {
            **super().bstack1llll1l1l11_opy_(),
            **self.bstack1llll11l1ll_opy_()
        }
    def bstack1llll1l11l1_opy_(self):
        return {
            **super().bstack1llll1l11l1_opy_(),
            **self.bstack1llll11llll_opy_()
        }
    def bstack11lll1l11l_opy_(self):
        return bstack11ll111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬᓮ")
class bstack1l1111lll1_opy_(bstack1l111111ll_opy_):
    def __init__(self, hook_type, *args, **kwargs):
        self.hook_type = hook_type
        super().__init__(*args, **kwargs, bstack1l11ll11l1_opy_=bstack11ll111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᓯ"))
    def bstack11llll1ll1_opy_(self):
        return self.hook_type
    def bstack1llll11ll1l_opy_(self):
        return {
            bstack11ll111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨᓰ"): self.hook_type
        }
    def bstack1llll1l1l11_opy_(self):
        return {
            **super().bstack1llll1l1l11_opy_(),
            **self.bstack1llll11ll1l_opy_()
        }
    def bstack1llll1l11l1_opy_(self):
        return {
            **super().bstack1llll1l11l1_opy_(),
            **self.bstack1llll11ll1l_opy_()
        }
    def bstack11lll1l11l_opy_(self):
        return bstack11ll111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨᓱ")