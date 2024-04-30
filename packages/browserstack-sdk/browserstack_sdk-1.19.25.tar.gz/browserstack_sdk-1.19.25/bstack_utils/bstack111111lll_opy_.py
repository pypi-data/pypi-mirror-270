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
class bstack11l1ll111l_opy_(object):
  bstack1ll11111ll_opy_ = os.path.join(os.path.expanduser(bstack11ll111_opy_ (u"ࠧࡿࠩ໒")), bstack11ll111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ໓"))
  bstack11l1ll1111_opy_ = os.path.join(bstack1ll11111ll_opy_, bstack11ll111_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶ࠲࡯ࡹ࡯࡯ࠩ໔"))
  bstack11l1l1llll_opy_ = None
  perform_scan = None
  bstack11ll11ll_opy_ = None
  bstack1lll1l11l1_opy_ = None
  bstack11ll111ll1_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11ll111_opy_ (u"ࠪ࡭ࡳࡹࡴࡢࡰࡦࡩࠬ໕")):
      cls.instance = super(bstack11l1ll111l_opy_, cls).__new__(cls)
      cls.instance.bstack11l1ll11l1_opy_()
    return cls.instance
  def bstack11l1ll11l1_opy_(self):
    try:
      with open(self.bstack11l1ll1111_opy_, bstack11ll111_opy_ (u"ࠫࡷ࠭໖")) as bstack11llll1ll_opy_:
        bstack11l1ll1l11_opy_ = bstack11llll1ll_opy_.read()
        data = json.loads(bstack11l1ll1l11_opy_)
        if bstack11ll111_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ໗") in data:
          self.bstack11ll1111ll_opy_(data[bstack11ll111_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ໘")])
        if bstack11ll111_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ໙") in data:
          self.bstack11l1lll1l1_opy_(data[bstack11ll111_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ໚")])
    except:
      pass
  def bstack11l1lll1l1_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack11ll111_opy_ (u"ࠩࡶࡧࡦࡴࠧ໛")]
      self.bstack11ll11ll_opy_ = scripts[bstack11ll111_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠧໜ")]
      self.bstack1lll1l11l1_opy_ = scripts[bstack11ll111_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨໝ")]
      self.bstack11ll111ll1_opy_ = scripts[bstack11ll111_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪໞ")]
  def bstack11ll1111ll_opy_(self, bstack11l1l1llll_opy_):
    if bstack11l1l1llll_opy_ != None and len(bstack11l1l1llll_opy_) != 0:
      self.bstack11l1l1llll_opy_ = bstack11l1l1llll_opy_
  def store(self):
    try:
      with open(self.bstack11l1ll1111_opy_, bstack11ll111_opy_ (u"࠭ࡷࠨໟ")) as file:
        json.dump({
          bstack11ll111_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࠤ໠"): self.bstack11l1l1llll_opy_,
          bstack11ll111_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࡴࠤ໡"): {
            bstack11ll111_opy_ (u"ࠤࡶࡧࡦࡴࠢ໢"): self.perform_scan,
            bstack11ll111_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢ໣"): self.bstack11ll11ll_opy_,
            bstack11ll111_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠣ໤"): self.bstack1lll1l11l1_opy_,
            bstack11ll111_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥ໥"): self.bstack11ll111ll1_opy_
          }
        }, file)
    except:
      pass
  def bstack1ll11ll1ll_opy_(self, bstack11l1ll11ll_opy_):
    try:
      return any(command.get(bstack11ll111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ໦")) == bstack11l1ll11ll_opy_ for command in self.bstack11l1l1llll_opy_)
    except:
      return False
bstack111111lll_opy_ = bstack11l1ll111l_opy_()