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
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import bstack11l1l11lll_opy_, bstack11l1ll1ll_opy_, bstack1l1l11l111_opy_, bstack1l11l111_opy_
from bstack_utils.messages import bstack111ll11ll_opy_, bstack111lllll_opy_
from bstack_utils.proxy import bstack1l1l1l11l1_opy_, bstack1ll1l1l11l_opy_
bstack1111l1111_opy_ = Config.bstack1ll111l11_opy_()
def bstack11l1lll1ll_opy_(config):
    return config[bstack11ll111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᆅ")]
def bstack11ll11ll1l_opy_(config):
    return config[bstack11ll111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᆆ")]
def bstack1llll1l1ll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack11l11ll111_opy_(obj):
    values = []
    bstack11l11lll1l_opy_ = re.compile(bstack11ll111_opy_ (u"ࡲࠣࡠࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࡜ࡥ࠭ࠧࠦᆇ"), re.I)
    for key in obj.keys():
        if bstack11l11lll1l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111ll1l1ll_opy_(config):
    tags = []
    tags.extend(bstack11l11ll111_opy_(os.environ))
    tags.extend(bstack11l11ll111_opy_(config))
    return tags
def bstack111lll1l1l_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111lll1l11_opy_(bstack111llll111_opy_):
    if not bstack111llll111_opy_:
        return bstack11ll111_opy_ (u"ࠨࠩᆈ")
    return bstack11ll111_opy_ (u"ࠤࡾࢁࠥ࠮ࡻࡾࠫࠥᆉ").format(bstack111llll111_opy_.name, bstack111llll111_opy_.email)
def bstack11l1lllll1_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack11l1111111_opy_ = repo.common_dir
        info = {
            bstack11ll111_opy_ (u"ࠥࡷ࡭ࡧࠢᆊ"): repo.head.commit.hexsha,
            bstack11ll111_opy_ (u"ࠦࡸ࡮࡯ࡳࡶࡢࡷ࡭ࡧࠢᆋ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11ll111_opy_ (u"ࠧࡨࡲࡢࡰࡦ࡬ࠧᆌ"): repo.active_branch.name,
            bstack11ll111_opy_ (u"ࠨࡴࡢࡩࠥᆍ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11ll111_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࠥᆎ"): bstack111lll1l11_opy_(repo.head.commit.committer),
            bstack11ll111_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࡣࡩࡧࡴࡦࠤᆏ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11ll111_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࠤᆐ"): bstack111lll1l11_opy_(repo.head.commit.author),
            bstack11ll111_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡢࡨࡦࡺࡥࠣᆑ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11ll111_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᆒ"): repo.head.commit.message,
            bstack11ll111_opy_ (u"ࠧࡸ࡯ࡰࡶࠥᆓ"): repo.git.rev_parse(bstack11ll111_opy_ (u"ࠨ࠭࠮ࡵ࡫ࡳࡼ࠳ࡴࡰࡲ࡯ࡩࡻ࡫࡬ࠣᆔ")),
            bstack11ll111_opy_ (u"ࠢࡤࡱࡰࡱࡴࡴ࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᆕ"): bstack11l1111111_opy_,
            bstack11ll111_opy_ (u"ࠣࡹࡲࡶࡰࡺࡲࡦࡧࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵࠦᆖ"): subprocess.check_output([bstack11ll111_opy_ (u"ࠤࡪ࡭ࡹࠨᆗ"), bstack11ll111_opy_ (u"ࠥࡶࡪࡼ࠭ࡱࡣࡵࡷࡪࠨᆘ"), bstack11ll111_opy_ (u"ࠦ࠲࠳ࡧࡪࡶ࠰ࡧࡴࡳ࡭ࡰࡰ࠰ࡨ࡮ࡸࠢᆙ")]).strip().decode(
                bstack11ll111_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᆚ")),
            bstack11ll111_opy_ (u"ࠨ࡬ࡢࡵࡷࡣࡹࡧࡧࠣᆛ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11ll111_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡳࡠࡵ࡬ࡲࡨ࡫࡟࡭ࡣࡶࡸࡤࡺࡡࡨࠤᆜ"): repo.git.rev_list(
                bstack11ll111_opy_ (u"ࠣࡽࢀ࠲࠳ࢁࡽࠣᆝ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack11l111111l_opy_ = []
        for remote in remotes:
            bstack111ll1l11l_opy_ = {
                bstack11ll111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᆞ"): remote.name,
                bstack11ll111_opy_ (u"ࠥࡹࡷࡲࠢᆟ"): remote.url,
            }
            bstack11l111111l_opy_.append(bstack111ll1l11l_opy_)
        return {
            bstack11ll111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᆠ"): bstack11ll111_opy_ (u"ࠧ࡭ࡩࡵࠤᆡ"),
            **info,
            bstack11ll111_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡹࠢᆢ"): bstack11l111111l_opy_
        }
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11ll111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥᆣ").format(err))
        return {}
def bstack11ll1l1l1_opy_():
    env = os.environ
    if (bstack11ll111_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨᆤ") in env and len(env[bstack11ll111_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢᆥ")]) > 0) or (
            bstack11ll111_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤᆦ") in env and len(env[bstack11ll111_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥᆧ")]) > 0):
        return {
            bstack11ll111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᆨ"): bstack11ll111_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹࠢᆩ"),
            bstack11ll111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᆪ"): env.get(bstack11ll111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᆫ")),
            bstack11ll111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᆬ"): env.get(bstack11ll111_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᆭ")),
            bstack11ll111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᆮ"): env.get(bstack11ll111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᆯ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠨࡃࡊࠤᆰ")) == bstack11ll111_opy_ (u"ࠢࡵࡴࡸࡩࠧᆱ") and bstack1llll1lll1_opy_(env.get(bstack11ll111_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥᆲ"))):
        return {
            bstack11ll111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᆳ"): bstack11ll111_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧᆴ"),
            bstack11ll111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᆵ"): env.get(bstack11ll111_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᆶ")),
            bstack11ll111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᆷ"): env.get(bstack11ll111_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦᆸ")),
            bstack11ll111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᆹ"): env.get(bstack11ll111_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧᆺ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠥࡇࡎࠨᆻ")) == bstack11ll111_opy_ (u"ࠦࡹࡸࡵࡦࠤᆼ") and bstack1llll1lll1_opy_(env.get(bstack11ll111_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧᆽ"))):
        return {
            bstack11ll111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᆾ"): bstack11ll111_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥᆿ"),
            bstack11ll111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᇀ"): env.get(bstack11ll111_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤᇁ")),
            bstack11ll111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᇂ"): env.get(bstack11ll111_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᇃ")),
            bstack11ll111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᇄ"): env.get(bstack11ll111_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᇅ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠢࡄࡋࠥᇆ")) == bstack11ll111_opy_ (u"ࠣࡶࡵࡹࡪࠨᇇ") and env.get(bstack11ll111_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥᇈ")) == bstack11ll111_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧᇉ"):
        return {
            bstack11ll111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇊ"): bstack11ll111_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢᇋ"),
            bstack11ll111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇌ"): None,
            bstack11ll111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᇍ"): None,
            bstack11ll111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᇎ"): None
        }
    if env.get(bstack11ll111_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧᇏ")) and env.get(bstack11ll111_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᇐ")):
        return {
            bstack11ll111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇑ"): bstack11ll111_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣᇒ"),
            bstack11ll111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇓ"): env.get(bstack11ll111_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧᇔ")),
            bstack11ll111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᇕ"): None,
            bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᇖ"): env.get(bstack11ll111_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᇗ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠦࡈࡏࠢᇘ")) == bstack11ll111_opy_ (u"ࠧࡺࡲࡶࡧࠥᇙ") and bstack1llll1lll1_opy_(env.get(bstack11ll111_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧᇚ"))):
        return {
            bstack11ll111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᇛ"): bstack11ll111_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢᇜ"),
            bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᇝ"): env.get(bstack11ll111_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨᇞ")),
            bstack11ll111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᇟ"): None,
            bstack11ll111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᇠ"): env.get(bstack11ll111_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᇡ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠢࡄࡋࠥᇢ")) == bstack11ll111_opy_ (u"ࠣࡶࡵࡹࡪࠨᇣ") and bstack1llll1lll1_opy_(env.get(bstack11ll111_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧᇤ"))):
        return {
            bstack11ll111_opy_ (u"ࠥࡲࡦࡳࡥࠣᇥ"): bstack11ll111_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢᇦ"),
            bstack11ll111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᇧ"): env.get(bstack11ll111_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐࠧᇨ")),
            bstack11ll111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᇩ"): env.get(bstack11ll111_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᇪ")),
            bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᇫ"): env.get(bstack11ll111_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨᇬ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠦࡈࡏࠢᇭ")) == bstack11ll111_opy_ (u"ࠧࡺࡲࡶࡧࠥᇮ") and bstack1llll1lll1_opy_(env.get(bstack11ll111_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤᇯ"))):
        return {
            bstack11ll111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᇰ"): bstack11ll111_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣᇱ"),
            bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᇲ"): env.get(bstack11ll111_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢᇳ")),
            bstack11ll111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᇴ"): env.get(bstack11ll111_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᇵ")),
            bstack11ll111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᇶ"): env.get(bstack11ll111_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥᇷ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠣࡅࡌࠦᇸ")) == bstack11ll111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᇹ") and bstack1llll1lll1_opy_(env.get(bstack11ll111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨᇺ"))):
        return {
            bstack11ll111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇻ"): bstack11ll111_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣᇼ"),
            bstack11ll111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇽ"): env.get(bstack11ll111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᇾ")),
            bstack11ll111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᇿ"): env.get(bstack11ll111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦሀ")) or env.get(bstack11ll111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨሁ")),
            bstack11ll111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥሂ"): env.get(bstack11ll111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢሃ"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack11ll111_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣሄ"))):
        return {
            bstack11ll111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧህ"): bstack11ll111_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳࠣሆ"),
            bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧሇ"): bstack11ll111_opy_ (u"ࠥࡿࢂࢁࡽࠣለ").format(env.get(bstack11ll111_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧሉ")), env.get(bstack11ll111_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬሊ"))),
            bstack11ll111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣላ"): env.get(bstack11ll111_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨሌ")),
            bstack11ll111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢል"): env.get(bstack11ll111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤሎ"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack11ll111_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧሏ"))):
        return {
            bstack11ll111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤሐ"): bstack11ll111_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢሑ"),
            bstack11ll111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤሒ"): bstack11ll111_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨሓ").format(env.get(bstack11ll111_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧሔ")), env.get(bstack11ll111_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪሕ")), env.get(bstack11ll111_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫሖ")), env.get(bstack11ll111_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨሗ"))),
            bstack11ll111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢመ"): env.get(bstack11ll111_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥሙ")),
            bstack11ll111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨሚ"): env.get(bstack11ll111_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤማ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥሜ")) and env.get(bstack11ll111_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧም")):
        return {
            bstack11ll111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤሞ"): bstack11ll111_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢሟ"),
            bstack11ll111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤሠ"): bstack11ll111_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥሡ").format(env.get(bstack11ll111_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫሢ")), env.get(bstack11ll111_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࠧሣ")), env.get(bstack11ll111_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪሤ"))),
            bstack11ll111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨሥ"): env.get(bstack11ll111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧሦ")),
            bstack11ll111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧሧ"): env.get(bstack11ll111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢረ"))
        }
    if any([env.get(bstack11ll111_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨሩ")), env.get(bstack11ll111_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣሪ")), env.get(bstack11ll111_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢራ"))]):
        return {
            bstack11ll111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤሬ"): bstack11ll111_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨࠧር"),
            bstack11ll111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤሮ"): env.get(bstack11ll111_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨሯ")),
            bstack11ll111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥሰ"): env.get(bstack11ll111_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢሱ")),
            bstack11ll111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤሲ"): env.get(bstack11ll111_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤሳ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥሴ")):
        return {
            bstack11ll111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦስ"): bstack11ll111_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵࠢሶ"),
            bstack11ll111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦሷ"): env.get(bstack11ll111_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯ࠦሸ")),
            bstack11ll111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧሹ"): env.get(bstack11ll111_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧࠥሺ")),
            bstack11ll111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦሻ"): env.get(bstack11ll111_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦሼ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࠣሽ")) or env.get(bstack11ll111_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥሾ")):
        return {
            bstack11ll111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢሿ"): bstack11ll111_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵࠦቀ"),
            bstack11ll111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢቁ"): env.get(bstack11ll111_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤቂ")),
            bstack11ll111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣቃ"): bstack11ll111_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠢቄ") if env.get(bstack11ll111_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥቅ")) else None,
            bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣቆ"): env.get(bstack11ll111_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔࠣቇ"))
        }
    if any([env.get(bstack11ll111_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤቈ")), env.get(bstack11ll111_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨ቉")), env.get(bstack11ll111_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨቊ"))]):
        return {
            bstack11ll111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧቋ"): bstack11ll111_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪࠢቌ"),
            bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧቍ"): None,
            bstack11ll111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ቎"): env.get(bstack11ll111_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣ቏")),
            bstack11ll111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦቐ"): env.get(bstack11ll111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣቑ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥቒ")):
        return {
            bstack11ll111_opy_ (u"ࠣࡰࡤࡱࡪࠨቓ"): bstack11ll111_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩࠧቔ"),
            bstack11ll111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨቕ"): env.get(bstack11ll111_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥቖ")),
            bstack11ll111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ቗"): bstack11ll111_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃࠢቘ").format(env.get(bstack11ll111_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠪ቙"))) if env.get(bstack11ll111_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦቚ")) else None,
            bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣቛ"): env.get(bstack11ll111_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧቜ"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack11ll111_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝ࠧቝ"))):
        return {
            bstack11ll111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ቞"): bstack11ll111_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿࠢ቟"),
            bstack11ll111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥበ"): env.get(bstack11ll111_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧቡ")),
            bstack11ll111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦቢ"): env.get(bstack11ll111_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨባ")),
            bstack11ll111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥቤ"): env.get(bstack11ll111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢብ"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack11ll111_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ࡙ࠢቦ"))):
        return {
            bstack11ll111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧቧ"): bstack11ll111_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤቨ"),
            bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧቩ"): bstack11ll111_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦቪ").format(env.get(bstack11ll111_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨቫ")), env.get(bstack11ll111_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩቬ")), env.get(bstack11ll111_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ࠭ቭ"))),
            bstack11ll111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤቮ"): env.get(bstack11ll111_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥቯ")),
            bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣተ"): env.get(bstack11ll111_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥቱ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠦࡈࡏࠢቲ")) == bstack11ll111_opy_ (u"ࠧࡺࡲࡶࡧࠥታ") and env.get(bstack11ll111_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨቴ")) == bstack11ll111_opy_ (u"ࠢ࠲ࠤት"):
        return {
            bstack11ll111_opy_ (u"ࠣࡰࡤࡱࡪࠨቶ"): bstack11ll111_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤቷ"),
            bstack11ll111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨቸ"): bstack11ll111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢቹ").format(env.get(bstack11ll111_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩቺ"))),
            bstack11ll111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣቻ"): None,
            bstack11ll111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨቼ"): None,
        }
    if env.get(bstack11ll111_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦች")):
        return {
            bstack11ll111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢቾ"): bstack11ll111_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧቿ"),
            bstack11ll111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢኀ"): None,
            bstack11ll111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢኁ"): env.get(bstack11ll111_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢኂ")),
            bstack11ll111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨኃ"): env.get(bstack11ll111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢኄ"))
        }
    if any([env.get(bstack11ll111_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧኅ")), env.get(bstack11ll111_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥኆ")), env.get(bstack11ll111_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤኇ")), env.get(bstack11ll111_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨኈ"))]):
        return {
            bstack11ll111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ኉"): bstack11ll111_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥኊ"),
            bstack11ll111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦኋ"): None,
            bstack11ll111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦኌ"): env.get(bstack11ll111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦኍ")) or None,
            bstack11ll111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ኎"): env.get(bstack11ll111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢ኏"), 0)
        }
    if env.get(bstack11ll111_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦነ")):
        return {
            bstack11ll111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧኑ"): bstack11ll111_opy_ (u"ࠣࡉࡲࡇࡉࠨኒ"),
            bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧና"): None,
            bstack11ll111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧኔ"): env.get(bstack11ll111_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤን")),
            bstack11ll111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦኖ"): env.get(bstack11ll111_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧኗ"))
        }
    if env.get(bstack11ll111_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧኘ")):
        return {
            bstack11ll111_opy_ (u"ࠣࡰࡤࡱࡪࠨኙ"): bstack11ll111_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧኚ"),
            bstack11ll111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨኛ"): env.get(bstack11ll111_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥኜ")),
            bstack11ll111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢኝ"): env.get(bstack11ll111_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤኞ")),
            bstack11ll111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨኟ"): env.get(bstack11ll111_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨአ"))
        }
    return {bstack11ll111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣኡ"): None}
def get_host_info():
    return {
        bstack11ll111_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧኢ"): platform.node(),
        bstack11ll111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨኣ"): platform.system(),
        bstack11ll111_opy_ (u"ࠧࡺࡹࡱࡧࠥኤ"): platform.machine(),
        bstack11ll111_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢእ"): platform.version(),
        bstack11ll111_opy_ (u"ࠢࡢࡴࡦ࡬ࠧኦ"): platform.architecture()[0]
    }
def bstack1llll11111_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack11l111ll11_opy_():
    if bstack1111l1111_opy_.get_property(bstack11ll111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩኧ")):
        return bstack11ll111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨከ")
    return bstack11ll111_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩኩ")
def bstack111lll1ll1_opy_(driver):
    info = {
        bstack11ll111_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪኪ"): driver.capabilities,
        bstack11ll111_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩካ"): driver.session_id,
        bstack11ll111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧኬ"): driver.capabilities.get(bstack11ll111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬክ"), None),
        bstack11ll111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪኮ"): driver.capabilities.get(bstack11ll111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪኯ"), None),
        bstack11ll111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬኰ"): driver.capabilities.get(bstack11ll111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪ኱"), None),
    }
    if bstack11l111ll11_opy_() == bstack11ll111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫኲ"):
        info[bstack11ll111_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧኳ")] = bstack11ll111_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ኴ") if bstack1lllllll1_opy_() else bstack11ll111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪኵ")
    return info
def bstack1lllllll1_opy_():
    if bstack1111l1111_opy_.get_property(bstack11ll111_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ኶")):
        return True
    if bstack1llll1lll1_opy_(os.environ.get(bstack11ll111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ኷"), None)):
        return True
    return False
def bstack11lllll11_opy_(bstack11l11ll11l_opy_, url, data, config):
    headers = config.get(bstack11ll111_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬኸ"), None)
    proxies = bstack1l1l1l11l1_opy_(config, url)
    auth = config.get(bstack11ll111_opy_ (u"ࠬࡧࡵࡵࡪࠪኹ"), None)
    response = requests.request(
            bstack11l11ll11l_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1ll1l111ll_opy_(bstack1lllll111_opy_, size):
    bstack1llll1ll1l_opy_ = []
    while len(bstack1lllll111_opy_) > size:
        bstack1ll11l11l1_opy_ = bstack1lllll111_opy_[:size]
        bstack1llll1ll1l_opy_.append(bstack1ll11l11l1_opy_)
        bstack1lllll111_opy_ = bstack1lllll111_opy_[size:]
    bstack1llll1ll1l_opy_.append(bstack1lllll111_opy_)
    return bstack1llll1ll1l_opy_
def bstack11l11l1ll1_opy_(message, bstack111ll11l1l_opy_=False):
    os.write(1, bytes(message, bstack11ll111_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬኺ")))
    os.write(1, bytes(bstack11ll111_opy_ (u"ࠧ࡝ࡰࠪኻ"), bstack11ll111_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧኼ")))
    if bstack111ll11l1l_opy_:
        with open(bstack11ll111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯ࡲ࠵࠶ࡿ࠭ࠨኽ") + os.environ[bstack11ll111_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩኾ")] + bstack11ll111_opy_ (u"ࠫ࠳ࡲ࡯ࡨࠩ኿"), bstack11ll111_opy_ (u"ࠬࡧࠧዀ")) as f:
            f.write(message + bstack11ll111_opy_ (u"࠭࡜࡯ࠩ዁"))
def bstack11l11111ll_opy_():
    return os.environ[bstack11ll111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪዂ")].lower() == bstack11ll111_opy_ (u"ࠨࡶࡵࡹࡪ࠭ዃ")
def bstack1l1llllll_opy_(bstack111llll11l_opy_):
    return bstack11ll111_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨዄ").format(bstack11l1l11lll_opy_, bstack111llll11l_opy_)
def bstack1l11llll11_opy_():
    return datetime.datetime.utcnow().isoformat() + bstack11ll111_opy_ (u"ࠪ࡞ࠬዅ")
def bstack111llllll1_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11ll111_opy_ (u"ࠫ࡟࠭዆"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11ll111_opy_ (u"ࠬࡠࠧ዇")))).total_seconds() * 1000
def bstack111lll11ll_opy_(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat() + bstack11ll111_opy_ (u"࡚࠭ࠨወ")
def bstack111ll11ll1_opy_(bstack11l11l111l_opy_):
    date_format = bstack11ll111_opy_ (u"࡛ࠧࠦࠨࡱࠪࡪࠠࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪࠬዉ")
    bstack111ll1ll1l_opy_ = datetime.datetime.strptime(bstack11l11l111l_opy_, date_format)
    return bstack111ll1ll1l_opy_.isoformat() + bstack11ll111_opy_ (u"ࠨ࡜ࠪዊ")
def bstack11l11l11l1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11ll111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩዋ")
    else:
        return bstack11ll111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪዌ")
def bstack1llll1lll1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11ll111_opy_ (u"ࠫࡹࡸࡵࡦࠩው")
def bstack11l1111l1l_opy_(val):
    return val.__str__().lower() == bstack11ll111_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫዎ")
def bstack11lll11l1l_opy_(bstack111lll111l_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111lll111l_opy_ as e:
                print(bstack11ll111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨዏ").format(func.__name__, bstack111lll111l_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack11l111ll1l_opy_(bstack111ll1l111_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111ll1l111_opy_(cls, *args, **kwargs)
            except bstack111lll111l_opy_ as e:
                print(bstack11ll111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢዐ").format(bstack111ll1l111_opy_.__name__, bstack111lll111l_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack11l111ll1l_opy_
    else:
        return decorator
def bstack1llll11ll_opy_(bstack11ll1l1lll_opy_):
    if bstack11ll111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬዑ") in bstack11ll1l1lll_opy_ and bstack11l1111l1l_opy_(bstack11ll1l1lll_opy_[bstack11ll111_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ዒ")]):
        return False
    if bstack11ll111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬዓ") in bstack11ll1l1lll_opy_ and bstack11l1111l1l_opy_(bstack11ll1l1lll_opy_[bstack11ll111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ዔ")]):
        return False
    return True
def bstack111l11lll_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack1l111l11l_opy_(hub_url):
    if bstack1ll1ll1l11_opy_() <= version.parse(bstack11ll111_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬዕ")):
        if hub_url != bstack11ll111_opy_ (u"࠭ࠧዖ"):
            return bstack11ll111_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣ዗") + hub_url + bstack11ll111_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧዘ")
        return bstack1l1l11l111_opy_
    if hub_url != bstack11ll111_opy_ (u"ࠩࠪዙ"):
        return bstack11ll111_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧዚ") + hub_url + bstack11ll111_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧዛ")
    return bstack1l11l111_opy_
def bstack11l1111lll_opy_():
    return isinstance(os.getenv(bstack11ll111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫዜ")), str)
def bstack1lll1l11_opy_(url):
    return urlparse(url).hostname
def bstack111l1l1ll_opy_(hostname):
    for bstack1lll11ll1l_opy_ in bstack11l1ll1ll_opy_:
        regex = re.compile(bstack1lll11ll1l_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11l11l1111_opy_(bstack11l1111l11_opy_, file_name, logger):
    bstack1ll11111ll_opy_ = os.path.join(os.path.expanduser(bstack11ll111_opy_ (u"࠭ࡾࠨዝ")), bstack11l1111l11_opy_)
    try:
        if not os.path.exists(bstack1ll11111ll_opy_):
            os.makedirs(bstack1ll11111ll_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11ll111_opy_ (u"ࠧࡿࠩዞ")), bstack11l1111l11_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11ll111_opy_ (u"ࠨࡹࠪዟ")):
                pass
            with open(file_path, bstack11ll111_opy_ (u"ࠤࡺ࠯ࠧዠ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack111ll11ll_opy_.format(str(e)))
def bstack11l11ll1l1_opy_(file_name, key, value, logger):
    file_path = bstack11l11l1111_opy_(bstack11ll111_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪዡ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack111l11111_opy_ = json.load(open(file_path, bstack11ll111_opy_ (u"ࠫࡷࡨࠧዢ")))
        else:
            bstack111l11111_opy_ = {}
        bstack111l11111_opy_[key] = value
        with open(file_path, bstack11ll111_opy_ (u"ࠧࡽࠫࠣዣ")) as outfile:
            json.dump(bstack111l11111_opy_, outfile)
def bstack1l11l1111_opy_(file_name, logger):
    file_path = bstack11l11l1111_opy_(bstack11ll111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ዤ"), file_name, logger)
    bstack111l11111_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11ll111_opy_ (u"ࠧࡳࠩዥ")) as bstack11llll1ll_opy_:
            bstack111l11111_opy_ = json.load(bstack11llll1ll_opy_)
    return bstack111l11111_opy_
def bstack1l1llllll1_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11ll111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬዦ") + file_path + bstack11ll111_opy_ (u"ࠩࠣࠫዧ") + str(e))
def bstack1ll1ll1l11_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11ll111_opy_ (u"ࠥࡀࡓࡕࡔࡔࡇࡗࡂࠧየ")
def bstack1lllll1l1l_opy_(config):
    if bstack11ll111_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪዩ") in config:
        del (config[bstack11ll111_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫዪ")])
        return False
    if bstack1ll1ll1l11_opy_() < version.parse(bstack11ll111_opy_ (u"࠭࠳࠯࠶࠱࠴ࠬያ")):
        return False
    if bstack1ll1ll1l11_opy_() >= version.parse(bstack11ll111_opy_ (u"ࠧ࠵࠰࠴࠲࠺࠭ዬ")):
        return True
    if bstack11ll111_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨይ") in config and config[bstack11ll111_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩዮ")] is False:
        return False
    else:
        return True
def bstack1l1l1l1111_opy_(args_list, bstack111llll1ll_opy_):
    index = -1
    for value in bstack111llll1ll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l1111111l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l1111111l_opy_ = bstack1l1111111l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11ll111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪዯ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11ll111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫደ"), exception=exception)
    def bstack11ll1l11ll_opy_(self):
        if self.result != bstack11ll111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬዱ"):
            return None
        if bstack11ll111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤዲ") in self.exception_type:
            return bstack11ll111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣዳ")
        return bstack11ll111_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤዴ")
    def bstack11l111llll_opy_(self):
        if self.result != bstack11ll111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩድ"):
            return None
        if self.bstack1l1111111l_opy_:
            return self.bstack1l1111111l_opy_
        return bstack111ll11l11_opy_(self.exception)
def bstack111ll11l11_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111lllll11_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1111lll1l_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l1ll1l1_opy_(config, logger):
    try:
        import playwright
        bstack111lll11l1_opy_ = playwright.__file__
        bstack111ll1lll1_opy_ = os.path.split(bstack111lll11l1_opy_)
        bstack111lll1lll_opy_ = bstack111ll1lll1_opy_[0] + bstack11ll111_opy_ (u"ࠪ࠳ࡩࡸࡩࡷࡧࡵ࠳ࡵࡧࡣ࡬ࡣࡪࡩ࠴ࡲࡩࡣ࠱ࡦࡰ࡮࠵ࡣ࡭࡫࠱࡮ࡸ࠭ዶ")
        os.environ[bstack11ll111_opy_ (u"ࠫࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠧዷ")] = bstack1ll1l1l11l_opy_(config)
        with open(bstack111lll1lll_opy_, bstack11ll111_opy_ (u"ࠬࡸࠧዸ")) as f:
            bstack1l1ll11l11_opy_ = f.read()
            bstack11l111l1ll_opy_ = bstack11ll111_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬዹ")
            bstack111lllllll_opy_ = bstack1l1ll11l11_opy_.find(bstack11l111l1ll_opy_)
            if bstack111lllllll_opy_ == -1:
              process = subprocess.Popen(bstack11ll111_opy_ (u"ࠢ࡯ࡲࡰࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠦዺ"), shell=True, cwd=bstack111ll1lll1_opy_[0])
              process.wait()
              bstack11l11lll11_opy_ = bstack11ll111_opy_ (u"ࠨࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࠨ࠻ࠨዻ")
              bstack111lll1111_opy_ = bstack11ll111_opy_ (u"ࠤࠥࠦࠥࡢࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࡠࠧࡁࠠࡤࡱࡱࡷࡹࠦࡻࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠤࢂࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩࠬ࠿ࠥ࡯ࡦࠡࠪࡳࡶࡴࡩࡥࡴࡵ࠱ࡩࡳࡼ࠮ࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠬࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠨࠪ࠽ࠣࠦࠧࠨዼ")
              bstack11l11ll1ll_opy_ = bstack1l1ll11l11_opy_.replace(bstack11l11lll11_opy_, bstack111lll1111_opy_)
              with open(bstack111lll1lll_opy_, bstack11ll111_opy_ (u"ࠪࡻࠬዽ")) as f:
                f.write(bstack11l11ll1ll_opy_)
    except Exception as e:
        logger.error(bstack111lllll_opy_.format(str(e)))
def bstack1ll11ll11l_opy_():
  try:
    bstack11l11l1lll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll111_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫዾ"))
    bstack111ll1llll_opy_ = []
    if os.path.exists(bstack11l11l1lll_opy_):
      with open(bstack11l11l1lll_opy_) as f:
        bstack111ll1llll_opy_ = json.load(f)
      os.remove(bstack11l11l1lll_opy_)
    return bstack111ll1llll_opy_
  except:
    pass
  return []
def bstack1l11l11ll_opy_(bstack1l11111l1_opy_):
  try:
    bstack111ll1llll_opy_ = []
    bstack11l11l1lll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll111_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬዿ"))
    if os.path.exists(bstack11l11l1lll_opy_):
      with open(bstack11l11l1lll_opy_) as f:
        bstack111ll1llll_opy_ = json.load(f)
    bstack111ll1llll_opy_.append(bstack1l11111l1_opy_)
    with open(bstack11l11l1lll_opy_, bstack11ll111_opy_ (u"࠭ࡷࠨጀ")) as f:
        json.dump(bstack111ll1llll_opy_, f)
  except:
    pass
def bstack1llll11l1l_opy_(logger, bstack11l11l11ll_opy_ = False):
  try:
    test_name = os.environ.get(bstack11ll111_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪጁ"), bstack11ll111_opy_ (u"ࠨࠩጂ"))
    if test_name == bstack11ll111_opy_ (u"ࠩࠪጃ"):
        test_name = threading.current_thread().__dict__.get(bstack11ll111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡅࡨࡩࡥࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠩጄ"), bstack11ll111_opy_ (u"ࠫࠬጅ"))
    bstack11l111l111_opy_ = bstack11ll111_opy_ (u"ࠬ࠲ࠠࠨጆ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack11l11l11ll_opy_:
        bstack1l1l111lll_opy_ = os.environ.get(bstack11ll111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ጇ"), bstack11ll111_opy_ (u"ࠧ࠱ࠩገ"))
        bstack1l11ll1l11_opy_ = {bstack11ll111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ጉ"): test_name, bstack11ll111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨጊ"): bstack11l111l111_opy_, bstack11ll111_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩጋ"): bstack1l1l111lll_opy_}
        bstack11l11l1l11_opy_ = []
        bstack11l111lll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡵࡶࡰࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪጌ"))
        if os.path.exists(bstack11l111lll1_opy_):
            with open(bstack11l111lll1_opy_) as f:
                bstack11l11l1l11_opy_ = json.load(f)
        bstack11l11l1l11_opy_.append(bstack1l11ll1l11_opy_)
        with open(bstack11l111lll1_opy_, bstack11ll111_opy_ (u"ࠬࡽࠧግ")) as f:
            json.dump(bstack11l11l1l11_opy_, f)
    else:
        bstack1l11ll1l11_opy_ = {bstack11ll111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫጎ"): test_name, bstack11ll111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ጏ"): bstack11l111l111_opy_, bstack11ll111_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧጐ"): str(multiprocessing.current_process().name)}
        if bstack11ll111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭጑") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1l11ll1l11_opy_)
  except Exception as e:
      logger.warn(bstack11ll111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡶࡹࡵࡧࡶࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢጒ").format(e))
def bstack1ll1ll11_opy_(error_message, test_name, index, logger):
  try:
    bstack11l1111ll1_opy_ = []
    bstack1l11ll1l11_opy_ = {bstack11ll111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩጓ"): test_name, bstack11ll111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫጔ"): error_message, bstack11ll111_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬጕ"): index}
    bstack111ll1ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll111_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨ጖"))
    if os.path.exists(bstack111ll1ll11_opy_):
        with open(bstack111ll1ll11_opy_) as f:
            bstack11l1111ll1_opy_ = json.load(f)
    bstack11l1111ll1_opy_.append(bstack1l11ll1l11_opy_)
    with open(bstack111ll1ll11_opy_, bstack11ll111_opy_ (u"ࠨࡹࠪ጗")) as f:
        json.dump(bstack11l1111ll1_opy_, f)
  except Exception as e:
    logger.warn(bstack11ll111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧጘ").format(e))
def bstack1l1lll111l_opy_(bstack1l1lllll1_opy_, name, logger):
  try:
    bstack1l11ll1l11_opy_ = {bstack11ll111_opy_ (u"ࠪࡲࡦࡳࡥࠨጙ"): name, bstack11ll111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪጚ"): bstack1l1lllll1_opy_, bstack11ll111_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫጛ"): str(threading.current_thread()._name)}
    return bstack1l11ll1l11_opy_
  except Exception as e:
    logger.warn(bstack11ll111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡤࡨ࡬ࡦࡼࡥࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥጜ").format(e))
  return
def bstack111lllll1l_opy_():
    return platform.system() == bstack11ll111_opy_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࠨጝ")
def bstack1ll1111l1l_opy_(bstack111llll1l1_opy_, config, logger):
    bstack11l111l11l_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111llll1l1_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11ll111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡬ࡵࡧࡵࠤࡨࡵ࡮ࡧ࡫ࡪࠤࡰ࡫ࡹࡴࠢࡥࡽࠥࡸࡥࡨࡧࡻࠤࡲࡧࡴࡤࡪ࠽ࠤࢀࢃࠢጞ").format(e))
    return bstack11l111l11l_opy_
def bstack11l11l1l1l_opy_(bstack111ll1l1l1_opy_, bstack11l11111l1_opy_):
    bstack111ll11lll_opy_ = version.parse(bstack111ll1l1l1_opy_)
    bstack11l111l1l1_opy_ = version.parse(bstack11l11111l1_opy_)
    if bstack111ll11lll_opy_ > bstack11l111l1l1_opy_:
        return 1
    elif bstack111ll11lll_opy_ < bstack11l111l1l1_opy_:
        return -1
    else:
        return 0