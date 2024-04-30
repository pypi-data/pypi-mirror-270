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
import atexit
import datetime
import inspect
import logging
import os
import signal
import sys
import threading
from uuid import uuid4
from bstack_utils.percy_sdk import PercySDK
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1111l1l1l_opy_, bstack1lll111ll1_opy_, update, bstack11l1l1ll_opy_,
                                       bstack11l111lll_opy_, bstack11l1ll111_opy_, bstack1lll1l11ll_opy_, bstack1111l1l11_opy_,
                                       bstack1lll1l11l_opy_, bstack111l111ll_opy_, bstack1l111l1l_opy_, bstack11ll111ll_opy_,
                                       bstack111ll1111_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1ll1lllll_opy_)
from browserstack_sdk.bstack11ll111l1_opy_ import bstack1l1ll111l_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack11ll11l1l_opy_
from bstack_utils.capture import bstack1l1111l11l_opy_
from bstack_utils.config import Config
from bstack_utils.constants import bstack1ll11l11l_opy_, bstack1lll11lll_opy_, bstack1llll1l1l_opy_, \
    bstack11ll1lll1_opy_
from bstack_utils.helper import bstack1111lll1l_opy_, bstack1llll11111_opy_, bstack11l11111ll_opy_, bstack1l11llll11_opy_, \
    bstack11l11l11l1_opy_, \
    bstack111lll1l1l_opy_, bstack1ll1ll1l11_opy_, bstack1l111l11l_opy_, bstack11l1111lll_opy_, bstack111l11lll_opy_, Notset, \
    bstack1lllll1l1l_opy_, bstack111llllll1_opy_, bstack111ll11l11_opy_, Result, bstack111lll11ll_opy_, bstack111lllll11_opy_, bstack11lll11l1l_opy_, \
    bstack1l11l11ll_opy_, bstack1llll11l1l_opy_, bstack1llll1lll1_opy_, bstack111lllll1l_opy_
from bstack_utils.bstack111l1l1l1l_opy_ import bstack111l1ll11l_opy_
from bstack_utils.messages import bstack1llll1ll1_opy_, bstack1l1ll11l1l_opy_, bstack1llll1l1_opy_, bstack1l11lllll_opy_, bstack11l1l1l1_opy_, \
    bstack111lllll_opy_, bstack1l1ll1ll_opy_, bstack1111l1ll1_opy_, bstack1l1l1lll1_opy_, bstack11ll1111l_opy_, \
    bstack1l111ll1_opy_, bstack1l1l1ll11_opy_
from bstack_utils.proxy import bstack1ll1l1l11l_opy_, bstack1ll11lll11_opy_
from bstack_utils.bstack1lll11l1_opy_ import bstack1llllll1l1l_opy_, bstack1lllll1ll1l_opy_, bstack1llllll11ll_opy_, bstack1lllll1l1l1_opy_, \
    bstack1lllll1llll_opy_, bstack1lllll1ll11_opy_, bstack1llllll1111_opy_, bstack1llll11lll_opy_, bstack1llllll1ll1_opy_
from bstack_utils.bstack1l11l1llll_opy_ import bstack1l1l1ll1l_opy_
from bstack_utils.bstack1l1l11l1l1_opy_ import bstack1l1l1lll1l_opy_, bstack11l111l1_opy_, bstack1l1l11l1ll_opy_, \
    bstack1lll1111ll_opy_, bstack1lll1llll_opy_
from bstack_utils.bstack1l111llll1_opy_ import bstack1l111111l1_opy_
from bstack_utils.bstack1l1l1l1ll1_opy_ import bstack11lll1l1_opy_
import bstack_utils.bstack11l11l11l_opy_ as bstack1l11ll1l1_opy_
from bstack_utils.bstack111111lll_opy_ import bstack111111lll_opy_
bstack1ll1111ll1_opy_ = None
bstack1l1l11ll_opy_ = None
bstack1l1l1ll1ll_opy_ = None
bstack111llll1l_opy_ = None
bstack1lllllll1l_opy_ = None
bstack1ll111l111_opy_ = None
bstack11llll1l_opy_ = None
bstack1lll111l1l_opy_ = None
bstack1llll1ll_opy_ = None
bstack1ll1l11ll_opy_ = None
bstack11l11llll_opy_ = None
bstack11l1l11ll_opy_ = None
bstack11l1l111_opy_ = None
bstack1lll11l11_opy_ = bstack11ll111_opy_ (u"ࠫࠬᗖ")
CONFIG = {}
bstack1l11ll11_opy_ = False
bstack1l1ll1111_opy_ = bstack11ll111_opy_ (u"ࠬ࠭ᗗ")
bstack1l1ll111_opy_ = bstack11ll111_opy_ (u"࠭ࠧᗘ")
bstack1lll11l11l_opy_ = False
bstack1ll1ll111l_opy_ = []
bstack1111111l_opy_ = bstack1ll11l11l_opy_
bstack1lll1l1ll11_opy_ = bstack11ll111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᗙ")
bstack1lll111ll1l_opy_ = False
bstack11l1llll1_opy_ = {}
bstack11l1ll1l1_opy_ = False
logger = bstack11ll11l1l_opy_.get_logger(__name__, bstack1111111l_opy_)
store = {
    bstack11ll111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᗚ"): []
}
bstack1lll1l1ll1l_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1l111l11ll_opy_ = {}
current_test_uuid = None
def bstack1ll1lll111_opy_(page, bstack11ll1l111_opy_):
    try:
        page.evaluate(bstack11ll111_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᗛ"),
                      bstack11ll111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠧᗜ") + json.dumps(
                          bstack11ll1l111_opy_) + bstack11ll111_opy_ (u"ࠦࢂࢃࠢᗝ"))
    except Exception as e:
        print(bstack11ll111_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡼࡿࠥᗞ"), e)
def bstack1l1111111_opy_(page, message, level):
    try:
        page.evaluate(bstack11ll111_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᗟ"), bstack11ll111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬᗠ") + json.dumps(
            message) + bstack11ll111_opy_ (u"ࠨ࠮ࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠫᗡ") + json.dumps(level) + bstack11ll111_opy_ (u"ࠩࢀࢁࠬᗢ"))
    except Exception as e:
        print(bstack11ll111_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡿࢂࠨᗣ"), e)
def pytest_configure(config):
    bstack1111l1111_opy_ = Config.bstack1ll111l11_opy_()
    config.args = bstack11lll1l1_opy_.bstack1lll1l1llll_opy_(config.args)
    bstack1111l1111_opy_.bstack1l11ll11ll_opy_(bstack1llll1lll1_opy_(config.getoption(bstack11ll111_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᗤ"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1lll1l111l1_opy_ = item.config.getoption(bstack11ll111_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᗥ"))
    plugins = item.config.getoption(bstack11ll111_opy_ (u"ࠨࡰ࡭ࡷࡪ࡭ࡳࡹࠢᗦ"))
    report = outcome.get_result()
    bstack1lll1l11111_opy_(item, call, report)
    if bstack11ll111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡶ࡬ࡶࡩ࡬ࡲࠧᗧ") not in plugins or bstack111l11lll_opy_():
        return
    summary = []
    driver = getattr(item, bstack11ll111_opy_ (u"ࠣࡡࡧࡶ࡮ࡼࡥࡳࠤᗨ"), None)
    page = getattr(item, bstack11ll111_opy_ (u"ࠤࡢࡴࡦ࡭ࡥࠣᗩ"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1lll11lll1l_opy_(item, report, summary, bstack1lll1l111l1_opy_)
    if (page is not None):
        bstack1lll11ll111_opy_(item, report, summary, bstack1lll1l111l1_opy_)
def bstack1lll11lll1l_opy_(item, report, summary, bstack1lll1l111l1_opy_):
    if report.when == bstack11ll111_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᗪ") and report.skipped:
        bstack1llllll1ll1_opy_(report)
    if report.when in [bstack11ll111_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥᗫ"), bstack11ll111_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢᗬ")]:
        return
    if not bstack11l11111ll_opy_():
        return
    try:
        if (str(bstack1lll1l111l1_opy_).lower() != bstack11ll111_opy_ (u"࠭ࡴࡳࡷࡨࠫᗭ")):
            item._driver.execute_script(
                bstack11ll111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬᗮ") + json.dumps(
                    report.nodeid) + bstack11ll111_opy_ (u"ࠨࡿࢀࠫᗯ"))
        os.environ[bstack11ll111_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬᗰ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11ll111_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩ࠿ࠦࡻ࠱ࡿࠥᗱ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11ll111_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᗲ")))
    bstack1ll11l1ll_opy_ = bstack11ll111_opy_ (u"ࠧࠨᗳ")
    bstack1llllll1ll1_opy_(report)
    if not passed:
        try:
            bstack1ll11l1ll_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11ll111_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨᗴ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll11l1ll_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11ll111_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤᗵ")))
        bstack1ll11l1ll_opy_ = bstack11ll111_opy_ (u"ࠣࠤᗶ")
        if not passed:
            try:
                bstack1ll11l1ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11ll111_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤᗷ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll11l1ll_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11ll111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡤࡢࡶࡤࠦ࠿ࠦࠧᗸ")
                    + json.dumps(bstack11ll111_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠥࠧᗹ"))
                    + bstack11ll111_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣᗺ")
                )
            else:
                item._driver.execute_script(
                    bstack11ll111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫᗻ")
                    + json.dumps(str(bstack1ll11l1ll_opy_))
                    + bstack11ll111_opy_ (u"ࠢ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠥᗼ")
                )
        except Exception as e:
            summary.append(bstack11ll111_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡡ࡯ࡰࡲࡸࡦࡺࡥ࠻ࠢࡾ࠴ࢂࠨᗽ").format(e))
def bstack1lll111l1ll_opy_(test_name, error_message):
    try:
        bstack1lll11l1ll1_opy_ = []
        bstack1l1l111lll_opy_ = os.environ.get(bstack11ll111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᗾ"), bstack11ll111_opy_ (u"ࠪ࠴ࠬᗿ"))
        bstack1l11ll1l11_opy_ = {bstack11ll111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᘀ"): test_name, bstack11ll111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᘁ"): error_message, bstack11ll111_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᘂ"): bstack1l1l111lll_opy_}
        bstack1lll11llll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll111_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬᘃ"))
        if os.path.exists(bstack1lll11llll1_opy_):
            with open(bstack1lll11llll1_opy_) as f:
                bstack1lll11l1ll1_opy_ = json.load(f)
        bstack1lll11l1ll1_opy_.append(bstack1l11ll1l11_opy_)
        with open(bstack1lll11llll1_opy_, bstack11ll111_opy_ (u"ࠨࡹࠪᘄ")) as f:
            json.dump(bstack1lll11l1ll1_opy_, f)
    except Exception as e:
        logger.debug(bstack11ll111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵ࡫ࡲࡴ࡫ࡶࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡶࡹࡵࡧࡶࡸࠥ࡫ࡲࡳࡱࡵࡷ࠿ࠦࠧᘅ") + str(e))
def bstack1lll11ll111_opy_(item, report, summary, bstack1lll1l111l1_opy_):
    if report.when in [bstack11ll111_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤᘆ"), bstack11ll111_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᘇ")]:
        return
    if (str(bstack1lll1l111l1_opy_).lower() != bstack11ll111_opy_ (u"ࠬࡺࡲࡶࡧࠪᘈ")):
        bstack1ll1lll111_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11ll111_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣᘉ")))
    bstack1ll11l1ll_opy_ = bstack11ll111_opy_ (u"ࠢࠣᘊ")
    bstack1llllll1ll1_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1ll11l1ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11ll111_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣᘋ").format(e)
                )
        try:
            if passed:
                bstack1lll1llll_opy_(getattr(item, bstack11ll111_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨᘌ"), None), bstack11ll111_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥᘍ"))
            else:
                error_message = bstack11ll111_opy_ (u"ࠫࠬᘎ")
                if bstack1ll11l1ll_opy_:
                    bstack1l1111111_opy_(item._page, str(bstack1ll11l1ll_opy_), bstack11ll111_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦᘏ"))
                    bstack1lll1llll_opy_(getattr(item, bstack11ll111_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬᘐ"), None), bstack11ll111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢᘑ"), str(bstack1ll11l1ll_opy_))
                    error_message = str(bstack1ll11l1ll_opy_)
                else:
                    bstack1lll1llll_opy_(getattr(item, bstack11ll111_opy_ (u"ࠨࡡࡳࡥ࡬࡫ࠧᘒ"), None), bstack11ll111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤᘓ"))
                bstack1lll111l1ll_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11ll111_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡷࡳࡨࡦࡺࡥࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿ࠵ࢃࠢᘔ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack11ll111_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣᘕ"), default=bstack11ll111_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦᘖ"), help=bstack11ll111_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧᘗ"))
    parser.addoption(bstack11ll111_opy_ (u"ࠢ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᘘ"), default=bstack11ll111_opy_ (u"ࠣࡈࡤࡰࡸ࡫ࠢᘙ"), help=bstack11ll111_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡧࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠣᘚ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11ll111_opy_ (u"ࠥ࠱࠲ࡪࡲࡪࡸࡨࡶࠧᘛ"), action=bstack11ll111_opy_ (u"ࠦࡸࡺ࡯ࡳࡧࠥᘜ"), default=bstack11ll111_opy_ (u"ࠧࡩࡨࡳࡱࡰࡩࠧᘝ"),
                         help=bstack11ll111_opy_ (u"ࠨࡄࡳ࡫ࡹࡩࡷࠦࡴࡰࠢࡵࡹࡳࠦࡴࡦࡵࡷࡷࠧᘞ"))
def bstack1l111ll111_opy_(log):
    if not (log[bstack11ll111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᘟ")] and log[bstack11ll111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᘠ")].strip()):
        return
    active = bstack1l111l11l1_opy_()
    log = {
        bstack11ll111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᘡ"): log[bstack11ll111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᘢ")],
        bstack11ll111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᘣ"): datetime.datetime.utcnow().isoformat() + bstack11ll111_opy_ (u"ࠬࡠࠧᘤ"),
        bstack11ll111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᘥ"): log[bstack11ll111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᘦ")],
    }
    if active:
        if active[bstack11ll111_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᘧ")] == bstack11ll111_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᘨ"):
            log[bstack11ll111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᘩ")] = active[bstack11ll111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᘪ")]
        elif active[bstack11ll111_opy_ (u"ࠬࡺࡹࡱࡧࠪᘫ")] == bstack11ll111_opy_ (u"࠭ࡴࡦࡵࡷࠫᘬ"):
            log[bstack11ll111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᘭ")] = active[bstack11ll111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᘮ")]
    bstack11lll1l1_opy_.bstack1ll1lll11l_opy_([log])
def bstack1l111l11l1_opy_():
    if len(store[bstack11ll111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᘯ")]) > 0 and store[bstack11ll111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᘰ")][-1]:
        return {
            bstack11ll111_opy_ (u"ࠫࡹࡿࡰࡦࠩᘱ"): bstack11ll111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᘲ"),
            bstack11ll111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᘳ"): store[bstack11ll111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᘴ")][-1]
        }
    if store.get(bstack11ll111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᘵ"), None):
        return {
            bstack11ll111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᘶ"): bstack11ll111_opy_ (u"ࠪࡸࡪࡹࡴࠨᘷ"),
            bstack11ll111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᘸ"): store[bstack11ll111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᘹ")]
        }
    return None
bstack11lll1ll1l_opy_ = bstack1l1111l11l_opy_(bstack1l111ll111_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        global bstack1lll111ll1l_opy_
        item._1lll1l1l111_opy_ = True
        bstack11111l11l_opy_ = bstack1l11ll1l1_opy_.bstack1ll111l1l_opy_(CONFIG, bstack111lll1l1l_opy_(item.own_markers))
        item._a11y_test_case = bstack11111l11l_opy_
        if bstack1lll111ll1l_opy_:
            driver = getattr(item, bstack11ll111_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᘺ"), None)
            item._a11y_started = bstack1l11ll1l1_opy_.bstack1ll111ll1_opy_(driver, bstack11111l11l_opy_)
        if not bstack11lll1l1_opy_.on() or bstack1lll1l1ll11_opy_ != bstack11ll111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᘻ"):
            return
        global current_test_uuid, bstack11lll1ll1l_opy_
        bstack11lll1ll1l_opy_.start()
        bstack1l1111l1ll_opy_ = {
            bstack11ll111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᘼ"): uuid4().__str__(),
            bstack11ll111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᘽ"): datetime.datetime.utcnow().isoformat() + bstack11ll111_opy_ (u"ࠪ࡞ࠬᘾ")
        }
        current_test_uuid = bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠫࡺࡻࡩࡥࠩᘿ")]
        store[bstack11ll111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᙀ")] = bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᙁ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1l111l11ll_opy_[item.nodeid] = {**_1l111l11ll_opy_[item.nodeid], **bstack1l1111l1ll_opy_}
        bstack1lll11ll1ll_opy_(item, _1l111l11ll_opy_[item.nodeid], bstack11ll111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᙂ"))
    except Exception as err:
        print(bstack11ll111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡳࡷࡱࡸࡪࡹࡴࡠࡥࡤࡰࡱࡀࠠࡼࡿࠪᙃ"), str(err))
def pytest_runtest_setup(item):
    global bstack1lll1l1ll1l_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack11l1111lll_opy_():
        atexit.register(bstack1l11111l_opy_)
        if not bstack1lll1l1ll1l_opy_:
            try:
                bstack1lll11lll11_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack111lllll1l_opy_():
                    bstack1lll11lll11_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll11lll11_opy_:
                    signal.signal(s, bstack1lll1l1l11l_opy_)
                bstack1lll1l1ll1l_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11ll111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡷ࡫ࡧࡪࡵࡷࡩࡷࠦࡳࡪࡩࡱࡥࡱࠦࡨࡢࡰࡧࡰࡪࡸࡳ࠻ࠢࠥᙄ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1llllll1l1l_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11ll111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᙅ")
    try:
        if not bstack11lll1l1_opy_.on():
            return
        bstack11lll1ll1l_opy_.start()
        uuid = uuid4().__str__()
        bstack1l1111l1ll_opy_ = {
            bstack11ll111_opy_ (u"ࠫࡺࡻࡩࡥࠩᙆ"): uuid,
            bstack11ll111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᙇ"): datetime.datetime.utcnow().isoformat() + bstack11ll111_opy_ (u"࡚࠭ࠨᙈ"),
            bstack11ll111_opy_ (u"ࠧࡵࡻࡳࡩࠬᙉ"): bstack11ll111_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᙊ"),
            bstack11ll111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᙋ"): bstack11ll111_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᙌ"),
            bstack11ll111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧᙍ"): bstack11ll111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᙎ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11ll111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪᙏ")] = item
        store[bstack11ll111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᙐ")] = [uuid]
        if not _1l111l11ll_opy_.get(item.nodeid, None):
            _1l111l11ll_opy_[item.nodeid] = {bstack11ll111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᙑ"): [], bstack11ll111_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫᙒ"): []}
        _1l111l11ll_opy_[item.nodeid][bstack11ll111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᙓ")].append(bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠫࡺࡻࡩࡥࠩᙔ")])
        _1l111l11ll_opy_[item.nodeid + bstack11ll111_opy_ (u"ࠬ࠳ࡳࡦࡶࡸࡴࠬᙕ")] = bstack1l1111l1ll_opy_
        bstack1lll11l1l11_opy_(item, bstack1l1111l1ll_opy_, bstack11ll111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᙖ"))
    except Exception as err:
        print(bstack11ll111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡴࡧࡷࡹࡵࡀࠠࡼࡿࠪᙗ"), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack11l1llll1_opy_
        if CONFIG.get(bstack11ll111_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᙘ"), False):
            if CONFIG.get(bstack11ll111_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩࠬᙙ"), bstack11ll111_opy_ (u"ࠥࡥࡺࡺ࡯ࠣᙚ")) == bstack11ll111_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᙛ"):
                bstack1lll111ll11_opy_ = bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠬࡶࡥࡳࡥࡼࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᙜ"), None)
                bstack1111ll1l_opy_ = bstack1lll111ll11_opy_ + bstack11ll111_opy_ (u"ࠨ࠭ࡵࡧࡶࡸࡨࡧࡳࡦࠤᙝ")
                driver = getattr(item, bstack11ll111_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨᙞ"), None)
                PercySDK.screenshot(driver, bstack1111ll1l_opy_)
        if getattr(item, bstack11ll111_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠨᙟ"), False):
            bstack1l1ll111l_opy_.bstack1l111111_opy_(getattr(item, bstack11ll111_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪᙠ"), None), bstack11l1llll1_opy_, logger, item)
        if not bstack11lll1l1_opy_.on():
            return
        bstack1l1111l1ll_opy_ = {
            bstack11ll111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᙡ"): uuid4().__str__(),
            bstack11ll111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᙢ"): datetime.datetime.utcnow().isoformat() + bstack11ll111_opy_ (u"ࠬࡠࠧᙣ"),
            bstack11ll111_opy_ (u"࠭ࡴࡺࡲࡨࠫᙤ"): bstack11ll111_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᙥ"),
            bstack11ll111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫᙦ"): bstack11ll111_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᙧ"),
            bstack11ll111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭ᙨ"): bstack11ll111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ᙩ")
        }
        _1l111l11ll_opy_[item.nodeid + bstack11ll111_opy_ (u"ࠬ࠳ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᙪ")] = bstack1l1111l1ll_opy_
        bstack1lll11l1l11_opy_(item, bstack1l1111l1ll_opy_, bstack11ll111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᙫ"))
    except Exception as err:
        print(bstack11ll111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯࠼ࠣࡿࢂ࠭ᙬ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack11lll1l1_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1lllll1l1l1_opy_(fixturedef.argname):
        store[bstack11ll111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡰࡳࡩࡻ࡬ࡦࡡ࡬ࡸࡪࡳࠧ᙭")] = request.node
    elif bstack1lllll1llll_opy_(fixturedef.argname):
        store[bstack11ll111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡧࡱࡧࡳࡴࡡ࡬ࡸࡪࡳࠧ᙮")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack11ll111_opy_ (u"ࠪࡲࡦࡳࡥࠨᙯ"): fixturedef.argname,
            bstack11ll111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᙰ"): bstack11l11l11l1_opy_(outcome),
            bstack11ll111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧᙱ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11ll111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪᙲ")]
        if not _1l111l11ll_opy_.get(current_test_item.nodeid, None):
            _1l111l11ll_opy_[current_test_item.nodeid] = {bstack11ll111_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᙳ"): []}
        _1l111l11ll_opy_[current_test_item.nodeid][bstack11ll111_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪᙴ")].append(fixture)
    except Exception as err:
        logger.debug(bstack11ll111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡶࡩࡹࡻࡰ࠻ࠢࡾࢁࠬᙵ"), str(err))
if bstack111l11lll_opy_() and bstack11lll1l1_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _1l111l11ll_opy_[request.node.nodeid][bstack11ll111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ᙶ")].bstack1llll11lll1_opy_(id(step))
        except Exception as err:
            print(bstack11ll111_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴ࠿ࠦࡻࡾࠩᙷ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _1l111l11ll_opy_[request.node.nodeid][bstack11ll111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨᙸ")].bstack1l11111l11_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11ll111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡶࡸࡪࡶ࡟ࡦࡴࡵࡳࡷࡀࠠࡼࡿࠪᙹ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack1l111llll1_opy_: bstack1l111111l1_opy_ = _1l111l11ll_opy_[request.node.nodeid][bstack11ll111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᙺ")]
            bstack1l111llll1_opy_.bstack1l11111l11_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11ll111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡸࡺࡥࡱࡡࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠬᙻ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1lll1l1ll11_opy_
        try:
            if not bstack11lll1l1_opy_.on() or bstack1lll1l1ll11_opy_ != bstack11ll111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᙼ"):
                return
            global bstack11lll1ll1l_opy_
            bstack11lll1ll1l_opy_.start()
            driver = bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩᙽ"), None)
            if not _1l111l11ll_opy_.get(request.node.nodeid, None):
                _1l111l11ll_opy_[request.node.nodeid] = {}
            bstack1l111llll1_opy_ = bstack1l111111l1_opy_.bstack1llll111l1l_opy_(
                scenario, feature, request.node,
                name=bstack1lllll1ll11_opy_(request.node, scenario),
                bstack11lllll11l_opy_=bstack1l11llll11_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11ll111_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭ᙾ"),
                tags=bstack1llllll1111_opy_(feature, scenario),
                bstack1l11l111l1_opy_=bstack11lll1l1_opy_.bstack11llll1l1l_opy_(driver) if driver and driver.session_id else {}
            )
            _1l111l11ll_opy_[request.node.nodeid][bstack11ll111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨᙿ")] = bstack1l111llll1_opy_
            bstack1lll11l11l1_opy_(bstack1l111llll1_opy_.uuid)
            bstack11lll1l1_opy_.bstack1l111l1111_opy_(bstack11ll111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ "), bstack1l111llll1_opy_)
        except Exception as err:
            print(bstack11ll111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳ࠿ࠦࡻࡾࠩᚁ"), str(err))
def bstack1lll1l11l11_opy_(bstack1lll1l11lll_opy_):
    if bstack1lll1l11lll_opy_ in store[bstack11ll111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᚂ")]:
        store[bstack11ll111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᚃ")].remove(bstack1lll1l11lll_opy_)
def bstack1lll11l11l1_opy_(bstack1lll11l11ll_opy_):
    store[bstack11ll111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᚄ")] = bstack1lll11l11ll_opy_
    threading.current_thread().current_test_uuid = bstack1lll11l11ll_opy_
@bstack11lll1l1_opy_.bstack1lll1lll111_opy_
def bstack1lll1l11111_opy_(item, call, report):
    global bstack1lll1l1ll11_opy_
    bstack111ll1l1_opy_ = bstack1l11llll11_opy_()
    if hasattr(report, bstack11ll111_opy_ (u"ࠫࡸࡺ࡯ࡱࠩᚅ")):
        bstack111ll1l1_opy_ = bstack111lll11ll_opy_(report.stop)
    elif hasattr(report, bstack11ll111_opy_ (u"ࠬࡹࡴࡢࡴࡷࠫᚆ")):
        bstack111ll1l1_opy_ = bstack111lll11ll_opy_(report.start)
    try:
        if getattr(report, bstack11ll111_opy_ (u"࠭ࡷࡩࡧࡱࠫᚇ"), bstack11ll111_opy_ (u"ࠧࠨᚈ")) == bstack11ll111_opy_ (u"ࠨࡥࡤࡰࡱ࠭ᚉ"):
            bstack11lll1ll1l_opy_.reset()
        if getattr(report, bstack11ll111_opy_ (u"ࠩࡺ࡬ࡪࡴࠧᚊ"), bstack11ll111_opy_ (u"ࠪࠫᚋ")) == bstack11ll111_opy_ (u"ࠫࡨࡧ࡬࡭ࠩᚌ"):
            if bstack1lll1l1ll11_opy_ == bstack11ll111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᚍ"):
                _1l111l11ll_opy_[item.nodeid][bstack11ll111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᚎ")] = bstack111ll1l1_opy_
                bstack1lll11ll1ll_opy_(item, _1l111l11ll_opy_[item.nodeid], bstack11ll111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᚏ"), report, call)
                store[bstack11ll111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᚐ")] = None
            elif bstack1lll1l1ll11_opy_ == bstack11ll111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨᚑ"):
                bstack1l111llll1_opy_ = _1l111l11ll_opy_[item.nodeid][bstack11ll111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ᚒ")]
                bstack1l111llll1_opy_.set(hooks=_1l111l11ll_opy_[item.nodeid].get(bstack11ll111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᚓ"), []))
                exception, bstack1l1111111l_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l1111111l_opy_ = [call.excinfo.exconly(), getattr(report, bstack11ll111_opy_ (u"ࠬࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠫᚔ"), bstack11ll111_opy_ (u"࠭ࠧᚕ"))]
                bstack1l111llll1_opy_.stop(time=bstack111ll1l1_opy_, result=Result(result=getattr(report, bstack11ll111_opy_ (u"ࠧࡰࡷࡷࡧࡴࡳࡥࠨᚖ"), bstack11ll111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᚗ")), exception=exception, bstack1l1111111l_opy_=bstack1l1111111l_opy_))
                bstack11lll1l1_opy_.bstack1l111l1111_opy_(bstack11ll111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᚘ"), _1l111l11ll_opy_[item.nodeid][bstack11ll111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ᚙ")])
        elif getattr(report, bstack11ll111_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩᚚ"), bstack11ll111_opy_ (u"ࠬ࠭᚛")) in [bstack11ll111_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ᚜"), bstack11ll111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ᚝")]:
            bstack11llll1lll_opy_ = item.nodeid + bstack11ll111_opy_ (u"ࠨ࠯ࠪ᚞") + getattr(report, bstack11ll111_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ᚟"), bstack11ll111_opy_ (u"ࠪࠫᚠ"))
            if getattr(report, bstack11ll111_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᚡ"), False):
                hook_type = bstack11ll111_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᚢ") if getattr(report, bstack11ll111_opy_ (u"࠭ࡷࡩࡧࡱࠫᚣ"), bstack11ll111_opy_ (u"ࠧࠨᚤ")) == bstack11ll111_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧᚥ") else bstack11ll111_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᚦ")
                _1l111l11ll_opy_[bstack11llll1lll_opy_] = {
                    bstack11ll111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᚧ"): uuid4().__str__(),
                    bstack11ll111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᚨ"): bstack111ll1l1_opy_,
                    bstack11ll111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨᚩ"): hook_type
                }
            _1l111l11ll_opy_[bstack11llll1lll_opy_][bstack11ll111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᚪ")] = bstack111ll1l1_opy_
            bstack1lll1l11l11_opy_(_1l111l11ll_opy_[bstack11llll1lll_opy_][bstack11ll111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᚫ")])
            bstack1lll11l1l11_opy_(item, _1l111l11ll_opy_[bstack11llll1lll_opy_], bstack11ll111_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᚬ"), report, call)
            if getattr(report, bstack11ll111_opy_ (u"ࠩࡺ࡬ࡪࡴࠧᚭ"), bstack11ll111_opy_ (u"ࠪࠫᚮ")) == bstack11ll111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᚯ"):
                if getattr(report, bstack11ll111_opy_ (u"ࠬࡵࡵࡵࡥࡲࡱࡪ࠭ᚰ"), bstack11ll111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᚱ")) == bstack11ll111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᚲ"):
                    bstack1l1111l1ll_opy_ = {
                        bstack11ll111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᚳ"): uuid4().__str__(),
                        bstack11ll111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᚴ"): bstack1l11llll11_opy_(),
                        bstack11ll111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᚵ"): bstack1l11llll11_opy_()
                    }
                    _1l111l11ll_opy_[item.nodeid] = {**_1l111l11ll_opy_[item.nodeid], **bstack1l1111l1ll_opy_}
                    bstack1lll11ll1ll_opy_(item, _1l111l11ll_opy_[item.nodeid], bstack11ll111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᚶ"))
                    bstack1lll11ll1ll_opy_(item, _1l111l11ll_opy_[item.nodeid], bstack11ll111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᚷ"), report, call)
    except Exception as err:
        print(bstack11ll111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡤࡵ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡽࢀࠫᚸ"), str(err))
def bstack1lll11l111l_opy_(test, bstack1l1111l1ll_opy_, result=None, call=None, bstack1l11ll11l1_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l111llll1_opy_ = {
        bstack11ll111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᚹ"): bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᚺ")],
        bstack11ll111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᚻ"): bstack11ll111_opy_ (u"ࠪࡸࡪࡹࡴࠨᚼ"),
        bstack11ll111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᚽ"): test.name,
        bstack11ll111_opy_ (u"ࠬࡨ࡯ࡥࡻࠪᚾ"): {
            bstack11ll111_opy_ (u"࠭࡬ࡢࡰࡪࠫᚿ"): bstack11ll111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧᛀ"),
            bstack11ll111_opy_ (u"ࠨࡥࡲࡨࡪ࠭ᛁ"): inspect.getsource(test.obj)
        },
        bstack11ll111_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᛂ"): test.name,
        bstack11ll111_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩᛃ"): test.name,
        bstack11ll111_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫᛄ"): bstack11lll1l1_opy_.bstack1l1111l111_opy_(test),
        bstack11ll111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨᛅ"): file_path,
        bstack11ll111_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨᛆ"): file_path,
        bstack11ll111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᛇ"): bstack11ll111_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩᛈ"),
        bstack11ll111_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧᛉ"): file_path,
        bstack11ll111_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᛊ"): bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᛋ")],
        bstack11ll111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᛌ"): bstack11ll111_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭ᛍ"),
        bstack11ll111_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪᛎ"): {
            bstack11ll111_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬᛏ"): test.nodeid
        },
        bstack11ll111_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᛐ"): bstack111lll1l1l_opy_(test.own_markers)
    }
    if bstack1l11ll11l1_opy_ in [bstack11ll111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫᛑ"), bstack11ll111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᛒ")]:
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠬࡳࡥࡵࡣࠪᛓ")] = {
            bstack11ll111_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨᛔ"): bstack1l1111l1ll_opy_.get(bstack11ll111_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᛕ"), [])
        }
    if bstack1l11ll11l1_opy_ == bstack11ll111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᛖ"):
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᛗ")] = bstack11ll111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᛘ")
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᛙ")] = bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᛚ")]
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᛛ")] = bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᛜ")]
    if result:
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᛝ")] = result.outcome
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪᛞ")] = result.duration * 1000
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᛟ")] = bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᛠ")]
        if result.failed:
            bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫᛡ")] = bstack11lll1l1_opy_.bstack11ll1l11ll_opy_(call.excinfo.typename)
            bstack1l111llll1_opy_[bstack11ll111_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᛢ")] = bstack11lll1l1_opy_.bstack1lll1lll1l1_opy_(call.excinfo, result)
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᛣ")] = bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᛤ")]
    if outcome:
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᛥ")] = bstack11l11l11l1_opy_(outcome)
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫᛦ")] = 0
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᛧ")] = bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᛨ")]
        if bstack1l111llll1_opy_[bstack11ll111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᛩ")] == bstack11ll111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᛪ"):
            bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ᛫")] = bstack11ll111_opy_ (u"ࠩࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠪ᛬")  # bstack1lll11ll1l1_opy_
            bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ᛭")] = [{bstack11ll111_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᛮ"): [bstack11ll111_opy_ (u"ࠬࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠩᛯ")]}]
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᛰ")] = bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᛱ")]
    return bstack1l111llll1_opy_
def bstack1lll1l111ll_opy_(test, bstack1l11l11111_opy_, bstack1l11ll11l1_opy_, result, call, outcome, bstack1lll11lllll_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1l11l11111_opy_[bstack11ll111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫᛲ")]
    hook_name = bstack1l11l11111_opy_[bstack11ll111_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᛳ")]
    hook_data = {
        bstack11ll111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᛴ"): bstack1l11l11111_opy_[bstack11ll111_opy_ (u"ࠫࡺࡻࡩࡥࠩᛵ")],
        bstack11ll111_opy_ (u"ࠬࡺࡹࡱࡧࠪᛶ"): bstack11ll111_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᛷ"),
        bstack11ll111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᛸ"): bstack11ll111_opy_ (u"ࠨࡽࢀࠫ᛹").format(bstack1lllll1ll1l_opy_(hook_name)),
        bstack11ll111_opy_ (u"ࠩࡥࡳࡩࡿࠧ᛺"): {
            bstack11ll111_opy_ (u"ࠪࡰࡦࡴࡧࠨ᛻"): bstack11ll111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ᛼"),
            bstack11ll111_opy_ (u"ࠬࡩ࡯ࡥࡧࠪ᛽"): None
        },
        bstack11ll111_opy_ (u"࠭ࡳࡤࡱࡳࡩࠬ᛾"): test.name,
        bstack11ll111_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧ᛿"): bstack11lll1l1_opy_.bstack1l1111l111_opy_(test, hook_name),
        bstack11ll111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫᜀ"): file_path,
        bstack11ll111_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫᜁ"): file_path,
        bstack11ll111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᜂ"): bstack11ll111_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬᜃ"),
        bstack11ll111_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪᜄ"): file_path,
        bstack11ll111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᜅ"): bstack1l11l11111_opy_[bstack11ll111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᜆ")],
        bstack11ll111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᜇ"): bstack11ll111_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫᜈ") if bstack1lll1l1ll11_opy_ == bstack11ll111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧᜉ") else bstack11ll111_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫᜊ"),
        bstack11ll111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨᜋ"): hook_type
    }
    bstack1lll1l1l1ll_opy_ = bstack11lllll1l1_opy_(_1l111l11ll_opy_.get(test.nodeid, None))
    if bstack1lll1l1l1ll_opy_:
        hook_data[bstack11ll111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠ࡫ࡧࠫᜌ")] = bstack1lll1l1l1ll_opy_
    if result:
        hook_data[bstack11ll111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᜍ")] = result.outcome
        hook_data[bstack11ll111_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᜎ")] = result.duration * 1000
        hook_data[bstack11ll111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᜏ")] = bstack1l11l11111_opy_[bstack11ll111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᜐ")]
        if result.failed:
            hook_data[bstack11ll111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᜑ")] = bstack11lll1l1_opy_.bstack11ll1l11ll_opy_(call.excinfo.typename)
            hook_data[bstack11ll111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᜒ")] = bstack11lll1l1_opy_.bstack1lll1lll1l1_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11ll111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᜓ")] = bstack11l11l11l1_opy_(outcome)
        hook_data[bstack11ll111_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ᜔")] = 100
        hook_data[bstack11ll111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ᜕࠭")] = bstack1l11l11111_opy_[bstack11ll111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ᜖")]
        if hook_data[bstack11ll111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ᜗")] == bstack11ll111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᜘"):
            hook_data[bstack11ll111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ᜙")] = bstack11ll111_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧ᜚")  # bstack1lll11ll1l1_opy_
            hook_data[bstack11ll111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ᜛")] = [{bstack11ll111_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ᜜"): [bstack11ll111_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭᜝")]}]
    if bstack1lll11lllll_opy_:
        hook_data[bstack11ll111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ᜞")] = bstack1lll11lllll_opy_.result
        hook_data[bstack11ll111_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬᜟ")] = bstack111llllll1_opy_(bstack1l11l11111_opy_[bstack11ll111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᜠ")], bstack1l11l11111_opy_[bstack11ll111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᜡ")])
        hook_data[bstack11ll111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᜢ")] = bstack1l11l11111_opy_[bstack11ll111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᜣ")]
        if hook_data[bstack11ll111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᜤ")] == bstack11ll111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᜥ"):
            hook_data[bstack11ll111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᜦ")] = bstack11lll1l1_opy_.bstack11ll1l11ll_opy_(bstack1lll11lllll_opy_.exception_type)
            hook_data[bstack11ll111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᜧ")] = [{bstack11ll111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᜨ"): bstack111ll11l11_opy_(bstack1lll11lllll_opy_.exception)}]
    return hook_data
def bstack1lll11ll1ll_opy_(test, bstack1l1111l1ll_opy_, bstack1l11ll11l1_opy_, result=None, call=None, outcome=None):
    bstack1l111llll1_opy_ = bstack1lll11l111l_opy_(test, bstack1l1111l1ll_opy_, result, call, bstack1l11ll11l1_opy_, outcome)
    driver = getattr(test, bstack11ll111_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨᜩ"), None)
    if bstack1l11ll11l1_opy_ == bstack11ll111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᜪ") and driver:
        bstack1l111llll1_opy_[bstack11ll111_opy_ (u"ࠩ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳࠨᜫ")] = bstack11lll1l1_opy_.bstack11llll1l1l_opy_(driver)
    if bstack1l11ll11l1_opy_ == bstack11ll111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫᜬ"):
        bstack1l11ll11l1_opy_ = bstack11ll111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᜭ")
    bstack11llll1l11_opy_ = {
        bstack11ll111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᜮ"): bstack1l11ll11l1_opy_,
        bstack11ll111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨᜯ"): bstack1l111llll1_opy_
    }
    bstack11lll1l1_opy_.bstack1l111l1lll_opy_(bstack11llll1l11_opy_)
def bstack1lll11l1l11_opy_(test, bstack1l1111l1ll_opy_, bstack1l11ll11l1_opy_, result=None, call=None, outcome=None, bstack1lll11lllll_opy_=None):
    hook_data = bstack1lll1l111ll_opy_(test, bstack1l1111l1ll_opy_, bstack1l11ll11l1_opy_, result, call, outcome, bstack1lll11lllll_opy_)
    bstack11llll1l11_opy_ = {
        bstack11ll111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᜰ"): bstack1l11ll11l1_opy_,
        bstack11ll111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࠪᜱ"): hook_data
    }
    bstack11lll1l1_opy_.bstack1l111l1lll_opy_(bstack11llll1l11_opy_)
def bstack11lllll1l1_opy_(bstack1l1111l1ll_opy_):
    if not bstack1l1111l1ll_opy_:
        return None
    if bstack1l1111l1ll_opy_.get(bstack11ll111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᜲ"), None):
        return getattr(bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ᜳ")], bstack11ll111_opy_ (u"ࠫࡺࡻࡩࡥ᜴ࠩ"), None)
    return bstack1l1111l1ll_opy_.get(bstack11ll111_opy_ (u"ࠬࡻࡵࡪࡦࠪ᜵"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack11lll1l1_opy_.on():
            return
        places = [bstack11ll111_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ᜶"), bstack11ll111_opy_ (u"ࠧࡤࡣ࡯ࡰࠬ᜷"), bstack11ll111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪ᜸")]
        bstack11llll1111_opy_ = []
        for bstack1lll1l11l1l_opy_ in places:
            records = caplog.get_records(bstack1lll1l11l1l_opy_)
            bstack1lll1l11ll1_opy_ = bstack11ll111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᜹") if bstack1lll1l11l1l_opy_ == bstack11ll111_opy_ (u"ࠪࡧࡦࡲ࡬ࠨ᜺") else bstack11ll111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ᜻")
            bstack1lll11ll11l_opy_ = request.node.nodeid + (bstack11ll111_opy_ (u"ࠬ࠭᜼") if bstack1lll1l11l1l_opy_ == bstack11ll111_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ᜽") else bstack11ll111_opy_ (u"ࠧ࠮ࠩ᜾") + bstack1lll1l11l1l_opy_)
            bstack1lll11l11ll_opy_ = bstack11lllll1l1_opy_(_1l111l11ll_opy_.get(bstack1lll11ll11l_opy_, None))
            if not bstack1lll11l11ll_opy_:
                continue
            for record in records:
                if bstack111lllll11_opy_(record.message):
                    continue
                bstack11llll1111_opy_.append({
                    bstack11ll111_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ᜿"): datetime.datetime.utcfromtimestamp(record.created).isoformat() + bstack11ll111_opy_ (u"ࠩ࡝ࠫᝀ"),
                    bstack11ll111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᝁ"): record.levelname,
                    bstack11ll111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᝂ"): record.message,
                    bstack1lll1l11ll1_opy_: bstack1lll11l11ll_opy_
                })
        if len(bstack11llll1111_opy_) > 0:
            bstack11lll1l1_opy_.bstack1ll1lll11l_opy_(bstack11llll1111_opy_)
    except Exception as err:
        print(bstack11ll111_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸ࡫ࡣࡰࡰࡧࡣ࡫࡯ࡸࡵࡷࡵࡩ࠿ࠦࡻࡾࠩᝃ"), str(err))
def bstack1llll1lll_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack11l1ll1l1_opy_
    bstack1111111l1_opy_ = bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪᝄ"), None) and bstack1111lll1l_opy_(
            threading.current_thread(), bstack11ll111_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ᝅ"), None)
    bstack1l1l1111l_opy_ = getattr(driver, bstack11ll111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨᝆ"), None) != None and getattr(driver, bstack11ll111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩᝇ"), None) == True
    if sequence == bstack11ll111_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪᝈ") and driver != None:
      if not bstack11l1ll1l1_opy_ and bstack11l11111ll_opy_() and bstack11ll111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᝉ") in CONFIG and CONFIG[bstack11ll111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᝊ")] == True and bstack111111lll_opy_.bstack1ll11ll1ll_opy_(driver_command) and (bstack1l1l1111l_opy_ or bstack1111111l1_opy_) and not bstack1ll1lllll_opy_(args):
        try:
          bstack11l1ll1l1_opy_ = True
          logger.debug(bstack11ll111_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࢁࡽࠨᝋ").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11ll111_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡪࡸࡦࡰࡴࡰࠤࡸࡩࡡ࡯ࠢࡾࢁࠬᝌ").format(str(err)))
        bstack11l1ll1l1_opy_ = False
    if sequence == bstack11ll111_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧᝍ"):
        if driver_command == bstack11ll111_opy_ (u"ࠩࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭ᝎ"):
            bstack11lll1l1_opy_.bstack1l11llllll_opy_({
                bstack11ll111_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩᝏ"): response[bstack11ll111_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪᝐ")],
                bstack11ll111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᝑ"): store[bstack11ll111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᝒ")]
            })
def bstack1l11111l_opy_():
    global bstack1ll1ll111l_opy_
    bstack11ll11l1l_opy_.bstack1lll1l1111_opy_()
    logging.shutdown()
    bstack11lll1l1_opy_.bstack1l111ll1l1_opy_()
    for driver in bstack1ll1ll111l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll1l1l11l_opy_(*args):
    global bstack1ll1ll111l_opy_
    bstack11lll1l1_opy_.bstack1l111ll1l1_opy_()
    for driver in bstack1ll1ll111l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l11l1l1l_opy_(self, *args, **kwargs):
    bstack1l11l11l_opy_ = bstack1ll1111ll1_opy_(self, *args, **kwargs)
    bstack11lll1l1_opy_.bstack1llllll1l_opy_(self)
    return bstack1l11l11l_opy_
def bstack111l1l11l_opy_(framework_name):
    global bstack1lll11l11_opy_
    global bstack1l11l1l1l1_opy_
    bstack1lll11l11_opy_ = framework_name
    logger.info(bstack1l1l1ll11_opy_.format(bstack1lll11l11_opy_.split(bstack11ll111_opy_ (u"ࠧ࠮ࠩᝓ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack11l11111ll_opy_():
            Service.start = bstack1lll1l11ll_opy_
            Service.stop = bstack1111l1l11_opy_
            webdriver.Remote.__init__ = bstack1lllll1111_opy_
            webdriver.Remote.get = bstack111lll11l_opy_
            if not isinstance(os.getenv(bstack11ll111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡃࡕࡅࡑࡒࡅࡍࠩ᝔")), str):
                return
            WebDriver.close = bstack1lll1l11l_opy_
            WebDriver.quit = bstack1lll1l1l1_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        if not bstack11l11111ll_opy_() and bstack11lll1l1_opy_.on():
            webdriver.Remote.__init__ = bstack1l11l1l1l_opy_
        bstack1l11l1l1l1_opy_ = True
    except Exception as e:
        pass
    bstack1l111l1ll_opy_()
    if os.environ.get(bstack11ll111_opy_ (u"ࠩࡖࡉࡑࡋࡎࡊࡗࡐࡣࡔࡘ࡟ࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡎࡔࡓࡕࡃࡏࡐࡊࡊࠧ᝕")):
        bstack1l11l1l1l1_opy_ = eval(os.environ.get(bstack11ll111_opy_ (u"ࠪࡗࡊࡒࡅࡏࡋࡘࡑࡤࡕࡒࡠࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡏࡎࡔࡖࡄࡐࡑࡋࡄࠨ᝖")))
    if not bstack1l11l1l1l1_opy_:
        bstack1l111l1l_opy_(bstack11ll111_opy_ (u"ࠦࡕࡧࡣ࡬ࡣࡪࡩࡸࠦ࡮ࡰࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠨ᝗"), bstack1l111ll1_opy_)
    if bstack1ll1ll11l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack1lll1l1ll_opy_
        except Exception as e:
            logger.error(bstack111lllll_opy_.format(str(e)))
    if bstack11ll111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ᝘") in str(framework_name).lower():
        if not bstack11l11111ll_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack11l111lll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack11l1ll111_opy_
            Config.getoption = bstack11llll11_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack11llll11l_opy_
        except Exception as e:
            pass
def bstack1lll1l1l1_opy_(self):
    global bstack1lll11l11_opy_
    global bstack1ll1l1llll_opy_
    global bstack1l1l11ll_opy_
    try:
        if bstack11ll111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭᝙") in bstack1lll11l11_opy_ and self.session_id != None and bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫ᝚"), bstack11ll111_opy_ (u"ࠨࠩ᝛")) != bstack11ll111_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ᝜"):
            bstack1lll1l1lll_opy_ = bstack11ll111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ᝝") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11ll111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᝞")
            bstack1llll11l1l_opy_(logger, True)
            if self != None:
                bstack1lll1111ll_opy_(self, bstack1lll1l1lll_opy_, bstack11ll111_opy_ (u"ࠬ࠲ࠠࠨ᝟").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack11ll111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪᝠ"), None)
        if item is not None and bstack1lll111ll1l_opy_:
            bstack1l1ll111l_opy_.bstack1l111111_opy_(self, bstack11l1llll1_opy_, logger, item)
        threading.current_thread().testStatus = bstack11ll111_opy_ (u"ࠧࠨᝡ")
    except Exception as e:
        logger.debug(bstack11ll111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࠤᝢ") + str(e))
    bstack1l1l11ll_opy_(self)
    self.session_id = None
def bstack1lllll1111_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1ll1l1llll_opy_
    global bstack1l11lll11l_opy_
    global bstack1lll11l11l_opy_
    global bstack1lll11l11_opy_
    global bstack1ll1111ll1_opy_
    global bstack1ll1ll111l_opy_
    global bstack1l1ll1111_opy_
    global bstack1l1ll111_opy_
    global bstack1lll111ll1l_opy_
    global bstack11l1llll1_opy_
    CONFIG[bstack11ll111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᝣ")] = str(bstack1lll11l11_opy_) + str(__version__)
    command_executor = bstack1l111l11l_opy_(bstack1l1ll1111_opy_)
    logger.debug(bstack1l11lllll_opy_.format(command_executor))
    proxy = bstack111ll1111_opy_(CONFIG, proxy)
    bstack1l1l111lll_opy_ = 0
    try:
        if bstack1lll11l11l_opy_ is True:
            bstack1l1l111lll_opy_ = int(os.environ.get(bstack11ll111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᝤ")))
    except:
        bstack1l1l111lll_opy_ = 0
    bstack1ll11111l_opy_ = bstack1111l1l1l_opy_(CONFIG, bstack1l1l111lll_opy_)
    logger.debug(bstack1111l1ll1_opy_.format(str(bstack1ll11111l_opy_)))
    bstack11l1llll1_opy_ = CONFIG.get(bstack11ll111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᝥ"))[bstack1l1l111lll_opy_]
    if bstack11ll111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᝦ") in CONFIG and CONFIG[bstack11ll111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᝧ")]:
        bstack1l1l11l1ll_opy_(bstack1ll11111l_opy_, bstack1l1ll111_opy_)
    if bstack1l11ll1l1_opy_.bstack1l1l1l1l1_opy_(CONFIG, bstack1l1l111lll_opy_) and bstack1l11ll1l1_opy_.bstack11l1lll1_opy_(bstack1ll11111l_opy_, options):
        bstack1lll111ll1l_opy_ = True
        bstack1l11ll1l1_opy_.set_capabilities(bstack1ll11111l_opy_, CONFIG)
    if desired_capabilities:
        bstack1l11lll1l1_opy_ = bstack1lll111ll1_opy_(desired_capabilities)
        bstack1l11lll1l1_opy_[bstack11ll111_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᝨ")] = bstack1lllll1l1l_opy_(CONFIG)
        bstack11l1l1111_opy_ = bstack1111l1l1l_opy_(bstack1l11lll1l1_opy_)
        if bstack11l1l1111_opy_:
            bstack1ll11111l_opy_ = update(bstack11l1l1111_opy_, bstack1ll11111l_opy_)
        desired_capabilities = None
    if options:
        bstack111l111ll_opy_(options, bstack1ll11111l_opy_)
    if not options:
        options = bstack11l1l1ll_opy_(bstack1ll11111l_opy_)
    if proxy and bstack1ll1ll1l11_opy_() >= version.parse(bstack11ll111_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨᝩ")):
        options.proxy(proxy)
    if options and bstack1ll1ll1l11_opy_() >= version.parse(bstack11ll111_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨᝪ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1ll1ll1l11_opy_() < version.parse(bstack11ll111_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩᝫ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1ll11111l_opy_)
    logger.info(bstack1llll1l1_opy_)
    if bstack1ll1ll1l11_opy_() >= version.parse(bstack11ll111_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫᝬ")):
        bstack1ll1111ll1_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1ll1ll1l11_opy_() >= version.parse(bstack11ll111_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ᝭")):
        bstack1ll1111ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1ll1ll1l11_opy_() >= version.parse(bstack11ll111_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭ᝮ")):
        bstack1ll1111ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack1ll1111ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1l11111l1_opy_ = bstack11ll111_opy_ (u"ࠧࠨᝯ")
        if bstack1ll1ll1l11_opy_() >= version.parse(bstack11ll111_opy_ (u"ࠨ࠶࠱࠴࠳࠶ࡢ࠲ࠩᝰ")):
            bstack1l11111l1_opy_ = self.caps.get(bstack11ll111_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤ᝱"))
        else:
            bstack1l11111l1_opy_ = self.capabilities.get(bstack11ll111_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥᝲ"))
        if bstack1l11111l1_opy_:
            bstack1l11l11ll_opy_(bstack1l11111l1_opy_)
            if bstack1ll1ll1l11_opy_() <= version.parse(bstack11ll111_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫᝳ")):
                self.command_executor._url = bstack11ll111_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨ᝴") + bstack1l1ll1111_opy_ + bstack11ll111_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥ᝵")
            else:
                self.command_executor._url = bstack11ll111_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤ᝶") + bstack1l11111l1_opy_ + bstack11ll111_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤ᝷")
            logger.debug(bstack1l1ll11l1l_opy_.format(bstack1l11111l1_opy_))
        else:
            logger.debug(bstack1llll1ll1_opy_.format(bstack11ll111_opy_ (u"ࠤࡒࡴࡹ࡯࡭ࡢ࡮ࠣࡌࡺࡨࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠥ᝸")))
    except Exception as e:
        logger.debug(bstack1llll1ll1_opy_.format(e))
    bstack1ll1l1llll_opy_ = self.session_id
    if bstack11ll111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ᝹") in bstack1lll11l11_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11ll111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ᝺"), None)
        if item:
            bstack1lll11l1l1l_opy_ = getattr(item, bstack11ll111_opy_ (u"ࠬࡥࡴࡦࡵࡷࡣࡨࡧࡳࡦࡡࡶࡸࡦࡸࡴࡦࡦࠪ᝻"), False)
            if not getattr(item, bstack11ll111_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧ᝼"), None) and bstack1lll11l1l1l_opy_:
                setattr(store[bstack11ll111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ᝽")], bstack11ll111_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩ᝾"), self)
        bstack11lll1l1_opy_.bstack1llllll1l_opy_(self)
    bstack1ll1ll111l_opy_.append(self)
    if bstack11ll111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ᝿") in CONFIG and bstack11ll111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨក") in CONFIG[bstack11ll111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧខ")][bstack1l1l111lll_opy_]:
        bstack1l11lll11l_opy_ = CONFIG[bstack11ll111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨគ")][bstack1l1l111lll_opy_][bstack11ll111_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫឃ")]
    logger.debug(bstack11ll1111l_opy_.format(bstack1ll1l1llll_opy_))
def bstack111lll11l_opy_(self, url):
    global bstack1llll1ll_opy_
    global CONFIG
    try:
        bstack11l111l1_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1l1l1lll1_opy_.format(str(err)))
    try:
        bstack1llll1ll_opy_(self, url)
    except Exception as e:
        try:
            bstack111lll111_opy_ = str(e)
            if any(err_msg in bstack111lll111_opy_ for err_msg in bstack1llll1l1l_opy_):
                bstack11l111l1_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1l1l1lll1_opy_.format(str(err)))
        raise e
def bstack11l11lll1_opy_(item, when):
    global bstack11l1l11ll_opy_
    try:
        bstack11l1l11ll_opy_(item, when)
    except Exception as e:
        pass
def bstack11llll11l_opy_(item, call, rep):
    global bstack11l1l111_opy_
    global bstack1ll1ll111l_opy_
    name = bstack11ll111_opy_ (u"ࠧࠨង")
    try:
        if rep.when == bstack11ll111_opy_ (u"ࠨࡥࡤࡰࡱ࠭ច"):
            bstack1ll1l1llll_opy_ = threading.current_thread().bstackSessionId
            bstack1lll1l111l1_opy_ = item.config.getoption(bstack11ll111_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫឆ"))
            try:
                if (str(bstack1lll1l111l1_opy_).lower() != bstack11ll111_opy_ (u"ࠪࡸࡷࡻࡥࠨជ")):
                    name = str(rep.nodeid)
                    bstack1111l111_opy_ = bstack1l1l1lll1l_opy_(bstack11ll111_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬឈ"), name, bstack11ll111_opy_ (u"ࠬ࠭ញ"), bstack11ll111_opy_ (u"࠭ࠧដ"), bstack11ll111_opy_ (u"ࠧࠨឋ"), bstack11ll111_opy_ (u"ࠨࠩឌ"))
                    os.environ[bstack11ll111_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬឍ")] = name
                    for driver in bstack1ll1ll111l_opy_:
                        if bstack1ll1l1llll_opy_ == driver.session_id:
                            driver.execute_script(bstack1111l111_opy_)
            except Exception as e:
                logger.debug(bstack11ll111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪណ").format(str(e)))
            try:
                bstack1llll11lll_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11ll111_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬត"):
                    status = bstack11ll111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬថ") if rep.outcome.lower() == bstack11ll111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ទ") else bstack11ll111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧធ")
                    reason = bstack11ll111_opy_ (u"ࠨࠩន")
                    if status == bstack11ll111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩប"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11ll111_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨផ") if status == bstack11ll111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫព") else bstack11ll111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫភ")
                    data = name + bstack11ll111_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨម") if status == bstack11ll111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧយ") else name + bstack11ll111_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠣࠣࠫរ") + reason
                    bstack1ll111ll_opy_ = bstack1l1l1lll1l_opy_(bstack11ll111_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫល"), bstack11ll111_opy_ (u"ࠪࠫវ"), bstack11ll111_opy_ (u"ࠫࠬឝ"), bstack11ll111_opy_ (u"ࠬ࠭ឞ"), level, data)
                    for driver in bstack1ll1ll111l_opy_:
                        if bstack1ll1l1llll_opy_ == driver.session_id:
                            driver.execute_script(bstack1ll111ll_opy_)
            except Exception as e:
                logger.debug(bstack11ll111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡴࡴࡴࡦࡺࡷࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪស").format(str(e)))
    except Exception as e:
        logger.debug(bstack11ll111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽࢀࠫហ").format(str(e)))
    bstack11l1l111_opy_(item, call, rep)
notset = Notset()
def bstack11llll11_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack11l11llll_opy_
    if str(name).lower() == bstack11ll111_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨឡ"):
        return bstack11ll111_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣអ")
    else:
        return bstack11l11llll_opy_(self, name, default, skip)
def bstack1lll1l1ll_opy_(self):
    global CONFIG
    global bstack11llll1l_opy_
    try:
        proxy = bstack1ll1l1l11l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11ll111_opy_ (u"ࠪ࠲ࡵࡧࡣࠨឣ")):
                proxies = bstack1ll11lll11_opy_(proxy, bstack1l111l11l_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l11llll1_opy_ = proxies.popitem()
                    if bstack11ll111_opy_ (u"ࠦ࠿࠵࠯ࠣឤ") in bstack1l11llll1_opy_:
                        return bstack1l11llll1_opy_
                    else:
                        return bstack11ll111_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨឥ") + bstack1l11llll1_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11ll111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡳࡶࡴࡾࡹࠡࡷࡵࡰࠥࡀࠠࡼࡿࠥឦ").format(str(e)))
    return bstack11llll1l_opy_(self)
def bstack1ll1ll11l_opy_():
    return (bstack11ll111_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪឧ") in CONFIG or bstack11ll111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬឨ") in CONFIG) and bstack1llll11111_opy_() and bstack1ll1ll1l11_opy_() >= version.parse(
        bstack1lll11lll_opy_)
def bstack1l1l1l1l_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1l11lll11l_opy_
    global bstack1lll11l11l_opy_
    global bstack1lll11l11_opy_
    CONFIG[bstack11ll111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫឩ")] = str(bstack1lll11l11_opy_) + str(__version__)
    bstack1l1l111lll_opy_ = 0
    try:
        if bstack1lll11l11l_opy_ is True:
            bstack1l1l111lll_opy_ = int(os.environ.get(bstack11ll111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪឪ")))
    except:
        bstack1l1l111lll_opy_ = 0
    CONFIG[bstack11ll111_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥឫ")] = True
    bstack1ll11111l_opy_ = bstack1111l1l1l_opy_(CONFIG, bstack1l1l111lll_opy_)
    logger.debug(bstack1111l1ll1_opy_.format(str(bstack1ll11111l_opy_)))
    if CONFIG.get(bstack11ll111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩឬ")):
        bstack1l1l11l1ll_opy_(bstack1ll11111l_opy_, bstack1l1ll111_opy_)
    if bstack11ll111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩឭ") in CONFIG and bstack11ll111_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬឮ") in CONFIG[bstack11ll111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫឯ")][bstack1l1l111lll_opy_]:
        bstack1l11lll11l_opy_ = CONFIG[bstack11ll111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬឰ")][bstack1l1l111lll_opy_][bstack11ll111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨឱ")]
    import urllib
    import json
    bstack111l1l111_opy_ = bstack11ll111_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭ឲ") + urllib.parse.quote(json.dumps(bstack1ll11111l_opy_))
    browser = self.connect(bstack111l1l111_opy_)
    return browser
def bstack1l111l1ll_opy_():
    global bstack1l11l1l1l1_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1l1l1l1l_opy_
        bstack1l11l1l1l1_opy_ = True
    except Exception as e:
        pass
def bstack1lll1l1111l_opy_():
    global CONFIG
    global bstack1l11ll11_opy_
    global bstack1l1ll1111_opy_
    global bstack1l1ll111_opy_
    global bstack1lll11l11l_opy_
    global bstack1111111l_opy_
    CONFIG = json.loads(os.environ.get(bstack11ll111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࠫឳ")))
    bstack1l11ll11_opy_ = eval(os.environ.get(bstack11ll111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ឴")))
    bstack1l1ll1111_opy_ = os.environ.get(bstack11ll111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡈࡖࡄࡢ࡙ࡗࡒࠧ឵"))
    bstack11ll111ll_opy_(CONFIG, bstack1l11ll11_opy_)
    bstack1111111l_opy_ = bstack11ll11l1l_opy_.bstack111lll1l1_opy_(CONFIG, bstack1111111l_opy_)
    global bstack1ll1111ll1_opy_
    global bstack1l1l11ll_opy_
    global bstack1l1l1ll1ll_opy_
    global bstack111llll1l_opy_
    global bstack1lllllll1l_opy_
    global bstack1ll111l111_opy_
    global bstack1lll111l1l_opy_
    global bstack1llll1ll_opy_
    global bstack11llll1l_opy_
    global bstack11l11llll_opy_
    global bstack11l1l11ll_opy_
    global bstack11l1l111_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1ll1111ll1_opy_ = webdriver.Remote.__init__
        bstack1l1l11ll_opy_ = WebDriver.quit
        bstack1lll111l1l_opy_ = WebDriver.close
        bstack1llll1ll_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack11ll111_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫា") in CONFIG or bstack11ll111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ិ") in CONFIG) and bstack1llll11111_opy_():
        if bstack1ll1ll1l11_opy_() < version.parse(bstack1lll11lll_opy_):
            logger.error(bstack1l1ll1ll_opy_.format(bstack1ll1ll1l11_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack11llll1l_opy_ = RemoteConnection._get_proxy_url
            except Exception as e:
                logger.error(bstack111lllll_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack11l11llll_opy_ = Config.getoption
        from _pytest import runner
        bstack11l1l11ll_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack11l1l1l1_opy_)
    try:
        from pytest_bdd import reporting
        bstack11l1l111_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack11ll111_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫី"))
    bstack1l1ll111_opy_ = CONFIG.get(bstack11ll111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨឹ"), {}).get(bstack11ll111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧឺ"))
    bstack1lll11l11l_opy_ = True
    bstack111l1l11l_opy_(bstack11ll1lll1_opy_)
if (bstack11l1111lll_opy_()):
    bstack1lll1l1111l_opy_()
@bstack11lll11l1l_opy_(class_method=False)
def bstack1lll11l1111_opy_(hook_name, event, bstack1lll1l1l1l1_opy_=None):
    if hook_name not in [bstack11ll111_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧុ"), bstack11ll111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫូ"), bstack11ll111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧួ"), bstack11ll111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫើ"), bstack11ll111_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨឿ"), bstack11ll111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬៀ"), bstack11ll111_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫេ"), bstack11ll111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨែ")]:
        return
    node = store[bstack11ll111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫៃ")]
    if hook_name in [bstack11ll111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧោ"), bstack11ll111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫៅ")]:
        node = store[bstack11ll111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡲࡵࡤࡶ࡮ࡨࡣ࡮ࡺࡥ࡮ࠩំ")]
    elif hook_name in [bstack11ll111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩះ"), bstack11ll111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭ៈ")]:
        node = store[bstack11ll111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡤ࡮ࡤࡷࡸࡥࡩࡵࡧࡰࠫ៉")]
    if event == bstack11ll111_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧ៊"):
        hook_type = bstack1llllll11ll_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack1l11l11111_opy_ = {
            bstack11ll111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭់"): uuid,
            bstack11ll111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭៌"): bstack1l11llll11_opy_(),
            bstack11ll111_opy_ (u"ࠪࡸࡾࡶࡥࠨ៍"): bstack11ll111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩ៎"),
            bstack11ll111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ៏"): hook_type,
            bstack11ll111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩ័"): hook_name
        }
        store[bstack11ll111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ៑")].append(uuid)
        bstack1lll11l1lll_opy_ = node.nodeid
        if hook_type == bstack11ll111_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ្࠭"):
            if not _1l111l11ll_opy_.get(bstack1lll11l1lll_opy_, None):
                _1l111l11ll_opy_[bstack1lll11l1lll_opy_] = {bstack11ll111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ៓"): []}
            _1l111l11ll_opy_[bstack1lll11l1lll_opy_][bstack11ll111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ។")].append(bstack1l11l11111_opy_[bstack11ll111_opy_ (u"ࠫࡺࡻࡩࡥࠩ៕")])
        _1l111l11ll_opy_[bstack1lll11l1lll_opy_ + bstack11ll111_opy_ (u"ࠬ࠳ࠧ៖") + hook_name] = bstack1l11l11111_opy_
        bstack1lll11l1l11_opy_(node, bstack1l11l11111_opy_, bstack11ll111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧៗ"))
    elif event == bstack11ll111_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭៘"):
        bstack11llll1lll_opy_ = node.nodeid + bstack11ll111_opy_ (u"ࠨ࠯ࠪ៙") + hook_name
        _1l111l11ll_opy_[bstack11llll1lll_opy_][bstack11ll111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ៚")] = bstack1l11llll11_opy_()
        bstack1lll1l11l11_opy_(_1l111l11ll_opy_[bstack11llll1lll_opy_][bstack11ll111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ៛")])
        bstack1lll11l1l11_opy_(node, _1l111l11ll_opy_[bstack11llll1lll_opy_], bstack11ll111_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ៜ"), bstack1lll11lllll_opy_=bstack1lll1l1l1l1_opy_)
def bstack1lll111llll_opy_():
    global bstack1lll1l1ll11_opy_
    if bstack111l11lll_opy_():
        bstack1lll1l1ll11_opy_ = bstack11ll111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩ៝")
    else:
        bstack1lll1l1ll11_opy_ = bstack11ll111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭៞")
@bstack11lll1l1_opy_.bstack1lll1lll111_opy_
def bstack1lll111lll1_opy_():
    bstack1lll111llll_opy_()
    if bstack1llll11111_opy_():
        bstack1l1l1ll1l_opy_(bstack1llll1lll_opy_)
    try:
        bstack111l1ll11l_opy_(bstack1lll11l1111_opy_)
    except Exception as e:
        logger.debug(bstack11ll111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࡷࠥࡶࡡࡵࡥ࡫࠾ࠥࢁࡽࠣ៟").format(e))
bstack1lll111lll1_opy_()