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
import sys
import logging
import tarfile
import io
import os
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l11llll1_opy_
import tempfile
import json
bstack111l1l111l_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠬፊ"))
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11ll111_opy_ (u"ࠫࡡࡴࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩፋ"),
      datefmt=bstack11ll111_opy_ (u"ࠬࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧፌ"),
      stream=sys.stdout
    )
  return logger
def bstack111l1l1l11_opy_():
  global bstack111l1l111l_opy_
  if os.path.exists(bstack111l1l111l_opy_):
    os.remove(bstack111l1l111l_opy_)
def bstack1lll1l1111_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack111lll1l1_opy_(config, log_level):
  bstack111l11l1ll_opy_ = log_level
  if bstack11ll111_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨፍ") in config:
    bstack111l11l1ll_opy_ = bstack11l11llll1_opy_[config[bstack11ll111_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩፎ")]]
  if config.get(bstack11ll111_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪፏ"), False):
    logging.getLogger().setLevel(bstack111l11l1ll_opy_)
    return bstack111l11l1ll_opy_
  global bstack111l1l111l_opy_
  bstack1lll1l1111_opy_()
  bstack111l1l11ll_opy_ = logging.Formatter(
    fmt=bstack11ll111_opy_ (u"ࠩ࡟ࡲࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧፐ"),
    datefmt=bstack11ll111_opy_ (u"ࠪࠩࡍࡀࠥࡎ࠼ࠨࡗࠬፑ")
  )
  bstack111l11ll1l_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack111l1l111l_opy_)
  file_handler.setFormatter(bstack111l1l11ll_opy_)
  bstack111l11ll1l_opy_.setFormatter(bstack111l1l11ll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack111l11ll1l_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11ll111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡵࡩࡲࡵࡴࡦ࠰ࡵࡩࡲࡵࡴࡦࡡࡦࡳࡳࡴࡥࡤࡶ࡬ࡳࡳ࠭ፒ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack111l11ll1l_opy_.setLevel(bstack111l11l1ll_opy_)
  logging.getLogger().addHandler(bstack111l11ll1l_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack111l11l1ll_opy_
def bstack111l11ll11_opy_(config):
  try:
    bstack111l1l1111_opy_ = set([
      bstack11ll111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧፓ"), bstack11ll111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩፔ"), bstack11ll111_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪፕ"), bstack11ll111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬፖ"), bstack11ll111_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠫፗ"),
      bstack11ll111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ፘ"), bstack11ll111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧፙ"), bstack11ll111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡗࡶࡩࡷ࠭ፚ"), bstack11ll111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧ፛")
    ])
    bstack111l1l11l1_opy_ = bstack11ll111_opy_ (u"ࠧࠨ፜")
    with open(bstack11ll111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫ፝")) as bstack111l11lll1_opy_:
      bstack111l11l1l1_opy_ = bstack111l11lll1_opy_.read()
      bstack111l1l11l1_opy_ = re.sub(bstack11ll111_opy_ (u"ࡴࠪࡢ࠭ࡢࡳࠬࠫࡂࠧ࠳࠰ࠤ࡝ࡰࠪ፞"), bstack11ll111_opy_ (u"ࠪࠫ፟"), bstack111l11l1l1_opy_, flags=re.M)
      bstack111l1l11l1_opy_ = re.sub(
        bstack11ll111_opy_ (u"ࡶࠬࡤࠨ࡝ࡵ࠮࠭ࡄ࠮ࠧ፠") + bstack11ll111_opy_ (u"ࠬࢂࠧ፡").join(bstack111l1l1111_opy_) + bstack11ll111_opy_ (u"࠭ࠩ࠯ࠬࠧࠫ።"),
        bstack11ll111_opy_ (u"ࡲࠨ࡞࠵࠾ࠥࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩ፣"),
        bstack111l1l11l1_opy_, flags=re.M | re.I
      )
    def bstack111l11l11l_opy_(dic):
      bstack111l11l111_opy_ = {}
      for key, value in dic.items():
        if key in bstack111l1l1111_opy_:
          bstack111l11l111_opy_[key] = bstack11ll111_opy_ (u"ࠨ࡝ࡕࡉࡉࡇࡃࡕࡇࡇࡡࠬ፤")
        else:
          if isinstance(value, dict):
            bstack111l11l111_opy_[key] = bstack111l11l11l_opy_(value)
          else:
            bstack111l11l111_opy_[key] = value
      return bstack111l11l111_opy_
    bstack111l11l111_opy_ = bstack111l11l11l_opy_(config)
    return {
      bstack11ll111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬ፥"): bstack111l1l11l1_opy_,
      bstack11ll111_opy_ (u"ࠪࡪ࡮ࡴࡡ࡭ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭፦"): json.dumps(bstack111l11l111_opy_)
    }
  except Exception as e:
    return {}
def bstack1ll1lll11l_opy_(config):
  global bstack111l1l111l_opy_
  try:
    if config.get(bstack11ll111_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭፧"), False):
      return
    uuid = os.getenv(bstack11ll111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ፨"))
    if not uuid or uuid == bstack11ll111_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ፩"):
      return
    bstack111l111lll_opy_ = [bstack11ll111_opy_ (u"ࠧࡳࡧࡴࡹ࡮ࡸࡥ࡮ࡧࡱࡸࡸ࠴ࡴࡹࡶࠪ፪"), bstack11ll111_opy_ (u"ࠨࡒ࡬ࡴ࡫࡯࡬ࡦࠩ፫"), bstack11ll111_opy_ (u"ࠩࡳࡽࡵࡸ࡯࡫ࡧࡦࡸ࠳ࡺ࡯࡮࡮ࠪ፬"), bstack111l1l111l_opy_]
    bstack1lll1l1111_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11ll111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠰ࡰࡴ࡭ࡳ࠮ࠩ፭") + uuid + bstack11ll111_opy_ (u"ࠫ࠳ࡺࡡࡳ࠰ࡪࡾࠬ፮"))
    with tarfile.open(output_file, bstack11ll111_opy_ (u"ࠧࡽ࠺ࡨࡼࠥ፯")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack111l111lll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack111l11ll11_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack111l11llll_opy_ = data.encode()
        tarinfo.size = len(bstack111l11llll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack111l11llll_opy_))
    bstack1l1l11ll1_opy_ = MultipartEncoder(
      fields= {
        bstack11ll111_opy_ (u"࠭ࡤࡢࡶࡤࠫ፰"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11ll111_opy_ (u"ࠧࡳࡤࠪ፱")), bstack11ll111_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡸ࠮ࡩࡽ࡭ࡵ࠭፲")),
        bstack11ll111_opy_ (u"ࠩࡦࡰ࡮࡫࡮ࡵࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫ፳"): uuid
      }
    )
    response = requests.post(
      bstack11ll111_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡺࡶ࡬ࡰࡣࡧ࠱ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡤ࡮࡬ࡩࡳࡺ࠭࡭ࡱࡪࡷ࠴ࡻࡰ࡭ࡱࡤࡨࠧ፴"),
      data=bstack1l1l11ll1_opy_,
      headers={bstack11ll111_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ፵"): bstack1l1l11ll1_opy_.content_type},
      auth=(config[bstack11ll111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ፶")], config[bstack11ll111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ፷")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11ll111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡵࡱ࡮ࡲࡥࡩࠦ࡬ࡰࡩࡶ࠾ࠥ࠭፸") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11ll111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡱࡨ࡮ࡴࡧࠡ࡮ࡲ࡫ࡸࡀࠧ፹") + str(e))
  finally:
    try:
      bstack111l1l1l11_opy_()
    except:
      pass