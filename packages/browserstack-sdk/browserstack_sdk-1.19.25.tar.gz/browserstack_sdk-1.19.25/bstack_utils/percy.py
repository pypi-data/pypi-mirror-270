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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1l1llllll_opy_, bstack11lllll11_opy_
class bstack1lllllll11_opy_:
  working_dir = os.getcwd()
  bstack1lllllll1_opy_ = False
  config = {}
  binary_path = bstack11ll111_opy_ (u"ࠪࠫᏁ")
  bstack1111l111l1_opy_ = bstack11ll111_opy_ (u"ࠫࠬᏂ")
  bstack11ll11ll1_opy_ = False
  bstack1111l11l1l_opy_ = None
  bstack1111l11111_opy_ = {}
  bstack11111l1111_opy_ = 300
  bstack1111l1l11l_opy_ = False
  logger = None
  bstack1111l1ll1l_opy_ = False
  bstack11111lll1l_opy_ = bstack11ll111_opy_ (u"ࠬ࠭Ꮓ")
  bstack1111lllll1_opy_ = {
    bstack11ll111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭Ꮔ") : 1,
    bstack11ll111_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨᏅ") : 2,
    bstack11ll111_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭Ꮖ") : 3,
    bstack11ll111_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩᏇ") : 4
  }
  def __init__(self) -> None: pass
  def bstack11111ll111_opy_(self):
    bstack1111l1ll11_opy_ = bstack11ll111_opy_ (u"ࠪࠫᏈ")
    bstack1111llll1l_opy_ = sys.platform
    bstack111l111111_opy_ = bstack11ll111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᏉ")
    if re.match(bstack11ll111_opy_ (u"ࠧࡪࡡࡳࡹ࡬ࡲࢁࡳࡡࡤࠢࡲࡷࠧᏊ"), bstack1111llll1l_opy_) != None:
      bstack1111l1ll11_opy_ = bstack11l1l111ll_opy_ + bstack11ll111_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡯ࡴࡺ࠱ࡾ࡮ࡶࠢᏋ")
      self.bstack11111lll1l_opy_ = bstack11ll111_opy_ (u"ࠧ࡮ࡣࡦࠫᏌ")
    elif re.match(bstack11ll111_opy_ (u"ࠣ࡯ࡶࡻ࡮ࡴࡼ࡮ࡵࡼࡷࢁࡳࡩ࡯ࡩࡺࢀࡨࡿࡧࡸ࡫ࡱࢀࡧࡩࡣࡸ࡫ࡱࢀࡼ࡯࡮ࡤࡧࡿࡩࡲࡩࡼࡸ࡫ࡱ࠷࠷ࠨᏍ"), bstack1111llll1l_opy_) != None:
      bstack1111l1ll11_opy_ = bstack11l1l111ll_opy_ + bstack11ll111_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯ࡺ࡭ࡳ࠴ࡺࡪࡲࠥᏎ")
      bstack111l111111_opy_ = bstack11ll111_opy_ (u"ࠥࡴࡪࡸࡣࡺ࠰ࡨࡼࡪࠨᏏ")
      self.bstack11111lll1l_opy_ = bstack11ll111_opy_ (u"ࠫࡼ࡯࡮ࠨᏐ")
    else:
      bstack1111l1ll11_opy_ = bstack11l1l111ll_opy_ + bstack11ll111_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡲࡩ࡯ࡷࡻ࠲ࡿ࡯ࡰࠣᏑ")
      self.bstack11111lll1l_opy_ = bstack11ll111_opy_ (u"࠭࡬ࡪࡰࡸࡼࠬᏒ")
    return bstack1111l1ll11_opy_, bstack111l111111_opy_
  def bstack11111ll11l_opy_(self):
    try:
      bstack1111ll1lll_opy_ = [os.path.join(expanduser(bstack11ll111_opy_ (u"ࠢࡿࠤᏓ")), bstack11ll111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᏔ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1111ll1lll_opy_:
        if(self.bstack1111lll1ll_opy_(path)):
          return path
      raise bstack11ll111_opy_ (u"ࠤࡘࡲࡦࡲࡢࡦࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨᏕ")
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡪࡰࡧࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡹࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠ࠮ࠢࡾࢁࠧᏖ").format(e))
  def bstack1111lll1ll_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack11111ll1l1_opy_(self, bstack1111l1ll11_opy_, bstack111l111111_opy_):
    try:
      bstack1111lll1l1_opy_ = self.bstack11111ll11l_opy_()
      bstack11111llll1_opy_ = os.path.join(bstack1111lll1l1_opy_, bstack11ll111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡾ࡮ࡶࠧᏗ"))
      bstack1111lll11l_opy_ = os.path.join(bstack1111lll1l1_opy_, bstack111l111111_opy_)
      if os.path.exists(bstack1111lll11l_opy_):
        self.logger.info(bstack11ll111_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡻࡾ࠮ࠣࡷࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢᏘ").format(bstack1111lll11l_opy_))
        return bstack1111lll11l_opy_
      if os.path.exists(bstack11111llll1_opy_):
        self.logger.info(bstack11ll111_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࢀࡩࡱࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡷࡱࡾ࡮ࡶࡰࡪࡰࡪࠦᏙ").format(bstack11111llll1_opy_))
        return self.bstack111111lll1_opy_(bstack11111llll1_opy_, bstack111l111111_opy_)
      self.logger.info(bstack11ll111_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠧᏚ").format(bstack1111l1ll11_opy_))
      response = bstack11lllll11_opy_(bstack11ll111_opy_ (u"ࠨࡉࡈࡘࠬᏛ"), bstack1111l1ll11_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack11111llll1_opy_, bstack11ll111_opy_ (u"ࠩࡺࡦࠬᏜ")) as file:
          file.write(response.content)
        self.logger.info(bstack11ll111_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡡ࡯ࡦࠣࡷࡦࡼࡥࡥࠢࡤࡸࠥࢁࡽࠣᏝ").format(bstack11111llll1_opy_))
        return self.bstack111111lll1_opy_(bstack11111llll1_opy_, bstack111l111111_opy_)
      else:
        raise(bstack11ll111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨ࠲࡙ࠥࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠽ࠤࢀࢃࠢᏞ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺ࠼ࠣࡿࢂࠨᏟ").format(e))
  def bstack1111l11l11_opy_(self, bstack1111l1ll11_opy_, bstack111l111111_opy_):
    try:
      retry = 2
      bstack1111lll11l_opy_ = None
      bstack11111l111l_opy_ = False
      while retry > 0:
        bstack1111lll11l_opy_ = self.bstack11111ll1l1_opy_(bstack1111l1ll11_opy_, bstack111l111111_opy_)
        bstack11111l111l_opy_ = self.bstack1111lll111_opy_(bstack1111l1ll11_opy_, bstack111l111111_opy_, bstack1111lll11l_opy_)
        if bstack11111l111l_opy_:
          break
        retry -= 1
      return bstack1111lll11l_opy_, bstack11111l111l_opy_
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡶࡡࡵࡪࠥᏠ").format(e))
    return bstack1111lll11l_opy_, False
  def bstack1111lll111_opy_(self, bstack1111l1ll11_opy_, bstack111l111111_opy_, bstack1111lll11l_opy_, bstack11111l11l1_opy_ = 0):
    if bstack11111l11l1_opy_ > 1:
      return False
    if bstack1111lll11l_opy_ == None or os.path.exists(bstack1111lll11l_opy_) == False:
      self.logger.warn(bstack11ll111_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡴࡨࡸࡷࡿࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧᏡ"))
      return False
    bstack1111l1l1l1_opy_ = bstack11ll111_opy_ (u"ࠣࡠ࠱࠮ࡅࡶࡥࡳࡥࡼࡠ࠴ࡩ࡬ࡪࠢ࡟ࡨ࠳ࡢࡤࠬ࠰࡟ࡨ࠰ࠨᏢ")
    command = bstack11ll111_opy_ (u"ࠩࡾࢁࠥ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᏣ").format(bstack1111lll11l_opy_)
    bstack1111l1llll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1111l1l1l1_opy_, bstack1111l1llll_opy_) != None:
      return True
    else:
      self.logger.error(bstack11ll111_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡹࡩࡷࡹࡩࡰࡰࠣࡧ࡭࡫ࡣ࡬ࠢࡩࡥ࡮ࡲࡥࡥࠤᏤ"))
      return False
  def bstack111111lll1_opy_(self, bstack11111llll1_opy_, bstack111l111111_opy_):
    try:
      working_dir = os.path.dirname(bstack11111llll1_opy_)
      shutil.unpack_archive(bstack11111llll1_opy_, working_dir)
      bstack1111lll11l_opy_ = os.path.join(working_dir, bstack111l111111_opy_)
      os.chmod(bstack1111lll11l_opy_, 0o755)
      return bstack1111lll11l_opy_
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡶࡰࡽ࡭ࡵࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧᏥ"))
  def bstack1111l1111l_opy_(self):
    try:
      percy = str(self.config.get(bstack11ll111_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᏦ"), bstack11ll111_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧᏧ"))).lower()
      if percy != bstack11ll111_opy_ (u"ࠢࡵࡴࡸࡩࠧᏨ"):
        return False
      self.bstack11ll11ll1_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᏩ").format(e))
  def bstack1111ll11l1_opy_(self):
    try:
      bstack1111ll11l1_opy_ = str(self.config.get(bstack11ll111_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩࠬᏪ"), bstack11ll111_opy_ (u"ࠥࡥࡺࡺ࡯ࠣᏫ"))).lower()
      return bstack1111ll11l1_opy_
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡨࡺࠠࡱࡧࡵࡧࡾࠦࡣࡢࡲࡷࡹࡷ࡫ࠠ࡮ࡱࡧࡩ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᏬ").format(e))
  def init(self, bstack1lllllll1_opy_, config, logger):
    self.bstack1lllllll1_opy_ = bstack1lllllll1_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1111l1111l_opy_():
      return
    self.bstack1111l11111_opy_ = config.get(bstack11ll111_opy_ (u"ࠬࡶࡥࡳࡥࡼࡓࡵࡺࡩࡰࡰࡶࠫᏭ"), {})
    self.bstack1111ll1ll1_opy_ = config.get(bstack11ll111_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩᏮ"), bstack11ll111_opy_ (u"ࠢࡢࡷࡷࡳࠧᏯ"))
    try:
      bstack1111l1ll11_opy_, bstack111l111111_opy_ = self.bstack11111ll111_opy_()
      bstack1111lll11l_opy_, bstack11111l111l_opy_ = self.bstack1111l11l11_opy_(bstack1111l1ll11_opy_, bstack111l111111_opy_)
      if bstack11111l111l_opy_:
        self.binary_path = bstack1111lll11l_opy_
        thread = Thread(target=self.bstack1111llll11_opy_)
        thread.start()
      else:
        self.bstack1111l1ll1l_opy_ = True
        self.logger.error(bstack11ll111_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡳࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦࡦࡰࡷࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤ࡚ࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡐࡦࡴࡦࡽࠧᏰ").format(bstack1111lll11l_opy_))
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᏱ").format(e))
  def bstack1111ll111l_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11ll111_opy_ (u"ࠪࡰࡴ࡭ࠧᏲ"), bstack11ll111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡰࡴ࡭ࠧᏳ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11ll111_opy_ (u"ࠧࡖࡵࡴࡪ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࡵࠣࡥࡹࠦࡻࡾࠤᏴ").format(logfile))
      self.bstack1111l111l1_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࠢࡳࡥࡹ࡮ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᏵ").format(e))
  def bstack1111llll11_opy_(self):
    bstack11111l11ll_opy_ = self.bstack11111l1lll_opy_()
    if bstack11111l11ll_opy_ == None:
      self.bstack1111l1ll1l_opy_ = True
      self.logger.error(bstack11ll111_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻࠥ᏶"))
      return False
    command_args = [bstack11ll111_opy_ (u"ࠣࡣࡳࡴ࠿࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠤ᏷") if self.bstack1lllllll1_opy_ else bstack11ll111_opy_ (u"ࠩࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹ࠭ᏸ")]
    bstack11111lll11_opy_ = self.bstack11111l1ll1_opy_()
    if bstack11111lll11_opy_ != None:
      command_args.append(bstack11ll111_opy_ (u"ࠥ࠱ࡨࠦࡻࡾࠤᏹ").format(bstack11111lll11_opy_))
    env = os.environ.copy()
    env[bstack11ll111_opy_ (u"ࠦࡕࡋࡒࡄ࡛ࡢࡘࡔࡑࡅࡏࠤᏺ")] = bstack11111l11ll_opy_
    bstack11111lllll_opy_ = [self.binary_path]
    self.bstack1111ll111l_opy_()
    self.bstack1111l11l1l_opy_ = self.bstack111111llll_opy_(bstack11111lllll_opy_ + command_args, env)
    self.logger.debug(bstack11ll111_opy_ (u"࡙ࠧࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠨᏻ"))
    bstack11111l11l1_opy_ = 0
    while self.bstack1111l11l1l_opy_.poll() == None:
      bstack1111ll1l1l_opy_ = self.bstack11111l1l11_opy_()
      if bstack1111ll1l1l_opy_:
        self.logger.debug(bstack11ll111_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠤᏼ"))
        self.bstack1111l1l11l_opy_ = True
        return True
      bstack11111l11l1_opy_ += 1
      self.logger.debug(bstack11ll111_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡒࡦࡶࡵࡽࠥ࠳ࠠࡼࡿࠥᏽ").format(bstack11111l11l1_opy_))
      time.sleep(2)
    self.logger.error(bstack11ll111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡉࡥ࡮ࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡽࢀࠤࡦࡺࡴࡦ࡯ࡳࡸࡸࠨ᏾").format(bstack11111l11l1_opy_))
    self.bstack1111l1ll1l_opy_ = True
    return False
  def bstack11111l1l11_opy_(self, bstack11111l11l1_opy_ = 0):
    try:
      if bstack11111l11l1_opy_ > 10:
        return False
      bstack11111l1l1l_opy_ = os.environ.get(bstack11ll111_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡕࡈࡖ࡛ࡋࡒࡠࡃࡇࡈࡗࡋࡓࡔࠩ᏿"), bstack11ll111_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡰࡴࡩࡡ࡭ࡪࡲࡷࡹࡀ࠵࠴࠵࠻ࠫ᐀"))
      bstack1111l11ll1_opy_ = bstack11111l1l1l_opy_ + bstack11l1l11ll1_opy_
      response = requests.get(bstack1111l11ll1_opy_)
      return True if response.json() else False
    except:
      return False
  def bstack11111l1lll_opy_(self):
    bstack1111ll11ll_opy_ = bstack11ll111_opy_ (u"ࠫࡦࡶࡰࠨᐁ") if self.bstack1lllllll1_opy_ else bstack11ll111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᐂ")
    bstack111llll11l_opy_ = bstack11ll111_opy_ (u"ࠨࡡࡱ࡫࠲ࡥࡵࡶ࡟ࡱࡧࡵࡧࡾ࠵ࡧࡦࡶࡢࡴࡷࡵࡪࡦࡥࡷࡣࡹࡵ࡫ࡦࡰࡂࡲࡦࡳࡥ࠾ࡽࢀࠪࡹࡿࡰࡦ࠿ࡾࢁࠧᐃ").format(self.config[bstack11ll111_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᐄ")], bstack1111ll11ll_opy_)
    uri = bstack1l1llllll_opy_(bstack111llll11l_opy_)
    try:
      response = bstack11lllll11_opy_(bstack11ll111_opy_ (u"ࠨࡉࡈࡘࠬᐅ"), uri, {}, {bstack11ll111_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᐆ"): (self.config[bstack11ll111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᐇ")], self.config[bstack11ll111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᐈ")])})
      if response.status_code == 200:
        bstack1111l11lll_opy_ = response.json()
        if bstack11ll111_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᐉ") in bstack1111l11lll_opy_:
          return bstack1111l11lll_opy_[bstack11ll111_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧᐊ")]
        else:
          raise bstack11ll111_opy_ (u"ࠧࡕࡱ࡮ࡩࡳࠦࡎࡰࡶࠣࡊࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠧᐋ").format(bstack1111l11lll_opy_)
      else:
        raise bstack11ll111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡴࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡸࡺࡡࡵࡷࡶࠤ࠲ࠦࡻࡾ࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡈ࡯ࡥࡻࠣ࠱ࠥࢁࡽࠣᐌ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡳࡶࡴࡰࡥࡤࡶࠥᐍ").format(e))
  def bstack11111l1ll1_opy_(self):
    bstack1111ll1111_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll111_opy_ (u"ࠥࡴࡪࡸࡣࡺࡅࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳࠨᐎ"))
    try:
      if bstack11ll111_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᐏ") not in self.bstack1111l11111_opy_:
        self.bstack1111l11111_opy_[bstack11ll111_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ᐐ")] = 2
      with open(bstack1111ll1111_opy_, bstack11ll111_opy_ (u"࠭ࡷࠨᐑ")) as fp:
        json.dump(self.bstack1111l11111_opy_, fp)
      return bstack1111ll1111_opy_
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡧࡷ࡫ࡡࡵࡧࠣࡴࡪࡸࡣࡺࠢࡦࡳࡳ࡬ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᐒ").format(e))
  def bstack111111llll_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack11111lll1l_opy_ == bstack11ll111_opy_ (u"ࠨࡹ࡬ࡲࠬᐓ"):
        bstack1111l1lll1_opy_ = [bstack11ll111_opy_ (u"ࠩࡦࡱࡩ࠴ࡥࡹࡧࠪᐔ"), bstack11ll111_opy_ (u"ࠪ࠳ࡨ࠭ᐕ")]
        cmd = bstack1111l1lll1_opy_ + cmd
      cmd = bstack11ll111_opy_ (u"ࠫࠥ࠭ᐖ").join(cmd)
      self.logger.debug(bstack11ll111_opy_ (u"ࠧࡘࡵ࡯ࡰ࡬ࡲ࡬ࠦࡻࡾࠤᐗ").format(cmd))
      with open(self.bstack1111l111l1_opy_, bstack11ll111_opy_ (u"ࠨࡡࠣᐘ")) as bstack11111ll1ll_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack11111ll1ll_opy_, text=True, stderr=bstack11111ll1ll_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1111l1ll1l_opy_ = True
      self.logger.error(bstack11ll111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠡࡹ࡬ࡸ࡭ࠦࡣ࡮ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᐙ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1111l1l11l_opy_:
        self.logger.info(bstack11ll111_opy_ (u"ࠣࡕࡷࡳࡵࡶࡩ࡯ࡩࠣࡔࡪࡸࡣࡺࠤᐚ"))
        cmd = [self.binary_path, bstack11ll111_opy_ (u"ࠤࡨࡼࡪࡩ࠺ࡴࡶࡲࡴࠧᐛ")]
        self.bstack111111llll_opy_(cmd)
        self.bstack1111l1l11l_opy_ = False
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡱࡳࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡧࡴࡳ࡭ࡢࡰࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᐜ").format(cmd, e))
  def bstack1l1lllll11_opy_(self):
    if not self.bstack11ll11ll1_opy_:
      return
    try:
      bstack1111llllll_opy_ = 0
      while not self.bstack1111l1l11l_opy_ and bstack1111llllll_opy_ < self.bstack11111l1111_opy_:
        if self.bstack1111l1ll1l_opy_:
          self.logger.info(bstack11ll111_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡩࡥ࡮ࡲࡥࡥࠤᐝ"))
          return
        time.sleep(1)
        bstack1111llllll_opy_ += 1
      os.environ[bstack11ll111_opy_ (u"ࠬࡖࡅࡓࡅ࡜ࡣࡇࡋࡓࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࠫᐞ")] = str(self.bstack1111ll1l11_opy_())
      self.logger.info(bstack11ll111_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡹࡥࡵࡷࡳࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠢᐟ"))
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᐠ").format(e))
  def bstack1111ll1l11_opy_(self):
    if self.bstack1lllllll1_opy_:
      return
    try:
      bstack1111l1l111_opy_ = [platform[bstack11ll111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᐡ")].lower() for platform in self.config.get(bstack11ll111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᐢ"), [])]
      bstack1111l111ll_opy_ = sys.maxsize
      bstack111111ll1l_opy_ = bstack11ll111_opy_ (u"ࠪࠫᐣ")
      for browser in bstack1111l1l111_opy_:
        if browser in self.bstack1111lllll1_opy_:
          bstack1111l1l1ll_opy_ = self.bstack1111lllll1_opy_[browser]
        if bstack1111l1l1ll_opy_ < bstack1111l111ll_opy_:
          bstack1111l111ll_opy_ = bstack1111l1l1ll_opy_
          bstack111111ll1l_opy_ = browser
      return bstack111111ll1l_opy_
    except Exception as e:
      self.logger.error(bstack11ll111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡨࡥࡴࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᐤ").format(e))