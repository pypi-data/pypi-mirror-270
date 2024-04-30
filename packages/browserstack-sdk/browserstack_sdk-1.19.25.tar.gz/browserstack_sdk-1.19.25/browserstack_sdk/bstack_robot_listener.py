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
import datetime
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack11lllllll1_opy_ import RobotHandler
from bstack_utils.capture import bstack1l1111l11l_opy_
from bstack_utils.bstack1l111llll1_opy_ import bstack1l111111ll_opy_, bstack1l1111lll1_opy_, bstack1l111111l1_opy_
from bstack_utils.bstack1l1l1l1ll1_opy_ import bstack11lll1l1_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1111lll1l_opy_, bstack1l11llll11_opy_, Result, \
    bstack11lll11l1l_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack11ll111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫൃ"): [],
        bstack11ll111_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧൄ"): [],
        bstack11ll111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭൅"): []
    }
    bstack11lll1l111_opy_ = []
    bstack1l1111ll1l_opy_ = []
    @staticmethod
    def bstack1l111ll111_opy_(log):
        if not (log[bstack11ll111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫെ")] and log[bstack11ll111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬേ")].strip()):
            return
        active = bstack11lll1l1_opy_.bstack1l111l11l1_opy_()
        log = {
            bstack11ll111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫൈ"): log[bstack11ll111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ൉")],
            bstack11ll111_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪൊ"): datetime.datetime.utcnow().isoformat() + bstack11ll111_opy_ (u"ࠨ࡜ࠪോ"),
            bstack11ll111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪൌ"): log[bstack11ll111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨ്ࠫ")],
        }
        if active:
            if active[bstack11ll111_opy_ (u"ࠫࡹࡿࡰࡦࠩൎ")] == bstack11ll111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ൏"):
                log[bstack11ll111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭൐")] = active[bstack11ll111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ൑")]
            elif active[bstack11ll111_opy_ (u"ࠨࡶࡼࡴࡪ࠭൒")] == bstack11ll111_opy_ (u"ࠩࡷࡩࡸࡺࠧ൓"):
                log[bstack11ll111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪൔ")] = active[bstack11ll111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫൕ")]
        bstack11lll1l1_opy_.bstack1ll1lll11l_opy_([log])
    def __init__(self):
        self.messages = Messages()
        self._1l111l111l_opy_ = None
        self._11lll1lll1_opy_ = None
        self._1l111l11ll_opy_ = OrderedDict()
        self.bstack11lll1ll1l_opy_ = bstack1l1111l11l_opy_(self.bstack1l111ll111_opy_)
    @bstack11lll11l1l_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack11lll11ll1_opy_()
        if not self._1l111l11ll_opy_.get(attrs.get(bstack11ll111_opy_ (u"ࠬ࡯ࡤࠨൖ")), None):
            self._1l111l11ll_opy_[attrs.get(bstack11ll111_opy_ (u"࠭ࡩࡥࠩൗ"))] = {}
        bstack11llllllll_opy_ = bstack1l111111l1_opy_(
                bstack11lllll111_opy_=attrs.get(bstack11ll111_opy_ (u"ࠧࡪࡦࠪ൘")),
                name=name,
                bstack11lllll11l_opy_=bstack1l11llll11_opy_(),
                file_path=os.path.relpath(attrs[bstack11ll111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ൙")], start=os.getcwd()) if attrs.get(bstack11ll111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ൚")) != bstack11ll111_opy_ (u"ࠪࠫ൛") else bstack11ll111_opy_ (u"ࠫࠬ൜"),
                framework=bstack11ll111_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫ൝")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack11ll111_opy_ (u"࠭ࡩࡥࠩ൞"), None)
        self._1l111l11ll_opy_[attrs.get(bstack11ll111_opy_ (u"ࠧࡪࡦࠪൟ"))][bstack11ll111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫൠ")] = bstack11llllllll_opy_
    @bstack11lll11l1l_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack1l111l1l1l_opy_()
        self._1l111l1l11_opy_(messages)
        for bstack1l1111ll11_opy_ in self.bstack11lll1l111_opy_:
            bstack1l1111ll11_opy_[bstack11ll111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫൡ")][bstack11ll111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩൢ")].extend(self.store[bstack11ll111_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪൣ")])
            bstack11lll1l1_opy_.bstack1l111l1lll_opy_(bstack1l1111ll11_opy_)
        self.bstack11lll1l111_opy_ = []
        self.store[bstack11ll111_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰࡤ࡮࡯ࡰ࡭ࡶࠫ൤")] = []
    @bstack11lll11l1l_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack11lll1ll1l_opy_.start()
        if not self._1l111l11ll_opy_.get(attrs.get(bstack11ll111_opy_ (u"࠭ࡩࡥࠩ൥")), None):
            self._1l111l11ll_opy_[attrs.get(bstack11ll111_opy_ (u"ࠧࡪࡦࠪ൦"))] = {}
        driver = bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ൧"), None)
        bstack1l111llll1_opy_ = bstack1l111111l1_opy_(
            bstack11lllll111_opy_=attrs.get(bstack11ll111_opy_ (u"ࠩ࡬ࡨࠬ൨")),
            name=name,
            bstack11lllll11l_opy_=bstack1l11llll11_opy_(),
            file_path=os.path.relpath(attrs[bstack11ll111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ൩")], start=os.getcwd()),
            scope=RobotHandler.bstack1l1111l111_opy_(attrs.get(bstack11ll111_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ൪"), None)),
            framework=bstack11ll111_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫ൫"),
            tags=attrs[bstack11ll111_opy_ (u"࠭ࡴࡢࡩࡶࠫ൬")],
            hooks=self.store[bstack11ll111_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭൭")],
            bstack1l11l111l1_opy_=bstack11lll1l1_opy_.bstack11llll1l1l_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack11ll111_opy_ (u"ࠣࡽࢀࠤࡡࡴࠠࡼࡿࠥ൮").format(bstack11ll111_opy_ (u"ࠤࠣࠦ൯").join(attrs[bstack11ll111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ൰")]), name) if attrs[bstack11ll111_opy_ (u"ࠫࡹࡧࡧࡴࠩ൱")] else name
        )
        self._1l111l11ll_opy_[attrs.get(bstack11ll111_opy_ (u"ࠬ࡯ࡤࠨ൲"))][bstack11ll111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ൳")] = bstack1l111llll1_opy_
        threading.current_thread().current_test_uuid = bstack1l111llll1_opy_.bstack11llllll11_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack11ll111_opy_ (u"ࠧࡪࡦࠪ൴"), None)
        self.bstack1l111l1111_opy_(bstack11ll111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ൵"), bstack1l111llll1_opy_)
    @bstack11lll11l1l_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack11lll1ll1l_opy_.reset()
        bstack11lll11lll_opy_ = bstack11lllll1ll_opy_.get(attrs.get(bstack11ll111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ൶")), bstack11ll111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ൷"))
        self._1l111l11ll_opy_[attrs.get(bstack11ll111_opy_ (u"ࠫ࡮ࡪࠧ൸"))][bstack11ll111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ൹")].stop(time=bstack1l11llll11_opy_(), duration=int(attrs.get(bstack11ll111_opy_ (u"࠭ࡥ࡭ࡣࡳࡷࡪࡪࡴࡪ࡯ࡨࠫൺ"), bstack11ll111_opy_ (u"ࠧ࠱ࠩൻ"))), result=Result(result=bstack11lll11lll_opy_, exception=attrs.get(bstack11ll111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩർ")), bstack1l1111111l_opy_=[attrs.get(bstack11ll111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪൽ"))]))
        self.bstack1l111l1111_opy_(bstack11ll111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬൾ"), self._1l111l11ll_opy_[attrs.get(bstack11ll111_opy_ (u"ࠫ࡮ࡪࠧൿ"))][bstack11ll111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ඀")], True)
        self.store[bstack11ll111_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪඁ")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack11lll11l1l_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack11lll11ll1_opy_()
        current_test_id = bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡥࠩං"), None)
        bstack11lll1ll11_opy_ = current_test_id if bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡦࠪඃ"), None) else bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡺ࡯ࡴࡦࡡ࡬ࡨࠬ඄"), None)
        if attrs.get(bstack11ll111_opy_ (u"ࠪࡸࡾࡶࡥࠨඅ"), bstack11ll111_opy_ (u"ࠫࠬආ")).lower() in [bstack11ll111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫඇ"), bstack11ll111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨඈ")]:
            hook_type = bstack1l11111111_opy_(attrs.get(bstack11ll111_opy_ (u"ࠧࡵࡻࡳࡩࠬඉ")), bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬඊ"), None))
            hook_name = bstack11ll111_opy_ (u"ࠩࡾࢁࠬඋ").format(attrs.get(bstack11ll111_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪඌ"), bstack11ll111_opy_ (u"ࠫࠬඍ")))
            if hook_type in [bstack11ll111_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩඎ"), bstack11ll111_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩඏ")]:
                hook_name = bstack11ll111_opy_ (u"ࠧ࡜ࡽࢀࡡࠥࢁࡽࠨඐ").format(bstack1l111ll1ll_opy_.get(hook_type), attrs.get(bstack11ll111_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨඑ"), bstack11ll111_opy_ (u"ࠩࠪඒ")))
            bstack1l11l11111_opy_ = bstack1l1111lll1_opy_(
                bstack11lllll111_opy_=bstack11lll1ll11_opy_ + bstack11ll111_opy_ (u"ࠪ࠱ࠬඓ") + attrs.get(bstack11ll111_opy_ (u"ࠫࡹࡿࡰࡦࠩඔ"), bstack11ll111_opy_ (u"ࠬ࠭ඕ")).lower(),
                name=hook_name,
                bstack11lllll11l_opy_=bstack1l11llll11_opy_(),
                file_path=os.path.relpath(attrs.get(bstack11ll111_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ඖ")), start=os.getcwd()),
                framework=bstack11ll111_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭඗"),
                tags=attrs[bstack11ll111_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭඘")],
                scope=RobotHandler.bstack1l1111l111_opy_(attrs.get(bstack11ll111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ඙"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack1l11l11111_opy_.bstack11llllll11_opy_()
            threading.current_thread().current_hook_id = bstack11lll1ll11_opy_ + bstack11ll111_opy_ (u"ࠪ࠱ࠬක") + attrs.get(bstack11ll111_opy_ (u"ࠫࡹࡿࡰࡦࠩඛ"), bstack11ll111_opy_ (u"ࠬ࠭ග")).lower()
            self.store[bstack11ll111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪඝ")] = [bstack1l11l11111_opy_.bstack11llllll11_opy_()]
            if bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫඞ"), None):
                self.store[bstack11ll111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬඟ")].append(bstack1l11l11111_opy_.bstack11llllll11_opy_())
            else:
                self.store[bstack11ll111_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡡ࡫ࡳࡴࡱࡳࠨච")].append(bstack1l11l11111_opy_.bstack11llllll11_opy_())
            if bstack11lll1ll11_opy_:
                self._1l111l11ll_opy_[bstack11lll1ll11_opy_ + bstack11ll111_opy_ (u"ࠪ࠱ࠬඡ") + attrs.get(bstack11ll111_opy_ (u"ࠫࡹࡿࡰࡦࠩජ"), bstack11ll111_opy_ (u"ࠬ࠭ඣ")).lower()] = { bstack11ll111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩඤ"): bstack1l11l11111_opy_ }
            bstack11lll1l1_opy_.bstack1l111l1111_opy_(bstack11ll111_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨඥ"), bstack1l11l11111_opy_)
        else:
            bstack11llll111l_opy_ = {
                bstack11ll111_opy_ (u"ࠨ࡫ࡧࠫඦ"): uuid4().__str__(),
                bstack11ll111_opy_ (u"ࠩࡷࡩࡽࡺࠧට"): bstack11ll111_opy_ (u"ࠪࡿࢂࠦࡻࡾࠩඨ").format(attrs.get(bstack11ll111_opy_ (u"ࠫࡰࡽ࡮ࡢ࡯ࡨࠫඩ")), attrs.get(bstack11ll111_opy_ (u"ࠬࡧࡲࡨࡵࠪඪ"), bstack11ll111_opy_ (u"࠭ࠧණ"))) if attrs.get(bstack11ll111_opy_ (u"ࠧࡢࡴࡪࡷࠬඬ"), []) else attrs.get(bstack11ll111_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨත")),
                bstack11ll111_opy_ (u"ࠩࡶࡸࡪࡶ࡟ࡢࡴࡪࡹࡲ࡫࡮ࡵࠩථ"): attrs.get(bstack11ll111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨද"), []),
                bstack11ll111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨධ"): bstack1l11llll11_opy_(),
                bstack11ll111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬන"): bstack11ll111_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ඲"),
                bstack11ll111_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬඳ"): attrs.get(bstack11ll111_opy_ (u"ࠨࡦࡲࡧࠬප"), bstack11ll111_opy_ (u"ࠩࠪඵ"))
            }
            if attrs.get(bstack11ll111_opy_ (u"ࠪࡰ࡮ࡨ࡮ࡢ࡯ࡨࠫබ"), bstack11ll111_opy_ (u"ࠫࠬභ")) != bstack11ll111_opy_ (u"ࠬ࠭ම"):
                bstack11llll111l_opy_[bstack11ll111_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧඹ")] = attrs.get(bstack11ll111_opy_ (u"ࠧ࡭࡫ࡥࡲࡦࡳࡥࠨය"))
            if not self.bstack1l1111ll1l_opy_:
                self._1l111l11ll_opy_[self._1l11l111ll_opy_()][bstack11ll111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫර")].add_step(bstack11llll111l_opy_)
                threading.current_thread().current_step_uuid = bstack11llll111l_opy_[bstack11ll111_opy_ (u"ࠩ࡬ࡨࠬ඼")]
            self.bstack1l1111ll1l_opy_.append(bstack11llll111l_opy_)
    @bstack11lll11l1l_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack1l111l1l1l_opy_()
        self._1l111l1l11_opy_(messages)
        current_test_id = bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡨࠬල"), None)
        bstack11lll1ll11_opy_ = current_test_id if current_test_id else bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡹࡵࡪࡶࡨࡣ࡮ࡪࠧ඾"), None)
        bstack1l11111ll1_opy_ = bstack11lllll1ll_opy_.get(attrs.get(bstack11ll111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ඿")), bstack11ll111_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧව"))
        bstack1l111lll1l_opy_ = attrs.get(bstack11ll111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨශ"))
        if bstack1l11111ll1_opy_ != bstack11ll111_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩෂ") and not attrs.get(bstack11ll111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪස")) and self._1l111l111l_opy_:
            bstack1l111lll1l_opy_ = self._1l111l111l_opy_
        bstack1l111lll11_opy_ = Result(result=bstack1l11111ll1_opy_, exception=bstack1l111lll1l_opy_, bstack1l1111111l_opy_=[bstack1l111lll1l_opy_])
        if attrs.get(bstack11ll111_opy_ (u"ࠪࡸࡾࡶࡥࠨහ"), bstack11ll111_opy_ (u"ࠫࠬළ")).lower() in [bstack11ll111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫෆ"), bstack11ll111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ෇")]:
            bstack11lll1ll11_opy_ = current_test_id if current_test_id else bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡵࡸ࡭ࡹ࡫࡟ࡪࡦࠪ෈"), None)
            if bstack11lll1ll11_opy_:
                bstack11llll1lll_opy_ = bstack11lll1ll11_opy_ + bstack11ll111_opy_ (u"ࠣ࠯ࠥ෉") + attrs.get(bstack11ll111_opy_ (u"ࠩࡷࡽࡵ࡫්ࠧ"), bstack11ll111_opy_ (u"ࠪࠫ෋")).lower()
                self._1l111l11ll_opy_[bstack11llll1lll_opy_][bstack11ll111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ෌")].stop(time=bstack1l11llll11_opy_(), duration=int(attrs.get(bstack11ll111_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪ෍"), bstack11ll111_opy_ (u"࠭࠰ࠨ෎"))), result=bstack1l111lll11_opy_)
                bstack11lll1l1_opy_.bstack1l111l1111_opy_(bstack11ll111_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩා"), self._1l111l11ll_opy_[bstack11llll1lll_opy_][bstack11ll111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫැ")])
        else:
            bstack11lll1ll11_opy_ = current_test_id if current_test_id else bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠ࡫ࡧࠫෑ"), None)
            if bstack11lll1ll11_opy_ and len(self.bstack1l1111ll1l_opy_) == 1:
                current_step_uuid = bstack1111lll1l_opy_(threading.current_thread(), bstack11ll111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡺࡥࡱࡡࡸࡹ࡮ࡪࠧි"), None)
                self._1l111l11ll_opy_[bstack11lll1ll11_opy_][bstack11ll111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧී")].bstack1l11111l11_opy_(current_step_uuid, duration=int(attrs.get(bstack11ll111_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪු"), bstack11ll111_opy_ (u"࠭࠰ࠨ෕"))), result=bstack1l111lll11_opy_)
            else:
                self.bstack1l11111l1l_opy_(attrs)
            self.bstack1l1111ll1l_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack11ll111_opy_ (u"ࠧࡩࡶࡰࡰࠬූ"), bstack11ll111_opy_ (u"ࠨࡰࡲࠫ෗")) == bstack11ll111_opy_ (u"ࠩࡼࡩࡸ࠭ෘ"):
                return
            self.messages.push(message)
            bstack11llll1111_opy_ = []
            if bstack11lll1l1_opy_.bstack1l111l11l1_opy_():
                bstack11llll1111_opy_.append({
                    bstack11ll111_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ෙ"): bstack1l11llll11_opy_(),
                    bstack11ll111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬේ"): message.get(bstack11ll111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ෛ")),
                    bstack11ll111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬො"): message.get(bstack11ll111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ෝ")),
                    **bstack11lll1l1_opy_.bstack1l111l11l1_opy_()
                })
                if len(bstack11llll1111_opy_) > 0:
                    bstack11lll1l1_opy_.bstack1ll1lll11l_opy_(bstack11llll1111_opy_)
        except Exception as err:
            pass
    def close(self):
        bstack11lll1l1_opy_.bstack1l111ll1l1_opy_()
    def bstack1l11111l1l_opy_(self, bstack11lll1llll_opy_):
        if not bstack11lll1l1_opy_.bstack1l111l11l1_opy_():
            return
        kwname = bstack11ll111_opy_ (u"ࠨࡽࢀࠤࢀࢃࠧෞ").format(bstack11lll1llll_opy_.get(bstack11ll111_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩෟ")), bstack11lll1llll_opy_.get(bstack11ll111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ෠"), bstack11ll111_opy_ (u"ࠫࠬ෡"))) if bstack11lll1llll_opy_.get(bstack11ll111_opy_ (u"ࠬࡧࡲࡨࡵࠪ෢"), []) else bstack11lll1llll_opy_.get(bstack11ll111_opy_ (u"࠭࡫ࡸࡰࡤࡱࡪ࠭෣"))
        error_message = bstack11ll111_opy_ (u"ࠢ࡬ࡹࡱࡥࡲ࡫࠺ࠡ࡞ࠥࡿ࠵ࢃ࡜ࠣࠢࡿࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࡢࠢࡼ࠳ࢀࡠࠧࠦࡼࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࡢࠢࡼ࠴ࢀࡠࠧࠨ෤").format(kwname, bstack11lll1llll_opy_.get(bstack11ll111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ෥")), str(bstack11lll1llll_opy_.get(bstack11ll111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ෦"))))
        bstack11llllll1l_opy_ = bstack11ll111_opy_ (u"ࠥ࡯ࡼࡴࡡ࡮ࡧ࠽ࠤࡡࠨࡻ࠱ࡿ࡟ࠦࠥࢂࠠࡴࡶࡤࡸࡺࡹ࠺ࠡ࡞ࠥࡿ࠶ࢃ࡜ࠣࠤ෧").format(kwname, bstack11lll1llll_opy_.get(bstack11ll111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ෨")))
        bstack1l1111l1l1_opy_ = error_message if bstack11lll1llll_opy_.get(bstack11ll111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭෩")) else bstack11llllll1l_opy_
        bstack1l111lllll_opy_ = {
            bstack11ll111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ෪"): self.bstack1l1111ll1l_opy_[-1].get(bstack11ll111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ෫"), bstack1l11llll11_opy_()),
            bstack11ll111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ෬"): bstack1l1111l1l1_opy_,
            bstack11ll111_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ෭"): bstack11ll111_opy_ (u"ࠪࡉࡗࡘࡏࡓࠩ෮") if bstack11lll1llll_opy_.get(bstack11ll111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ෯")) == bstack11ll111_opy_ (u"ࠬࡌࡁࡊࡎࠪ෰") else bstack11ll111_opy_ (u"࠭ࡉࡏࡈࡒࠫ෱"),
            **bstack11lll1l1_opy_.bstack1l111l11l1_opy_()
        }
        bstack11lll1l1_opy_.bstack1ll1lll11l_opy_([bstack1l111lllll_opy_])
    def _1l11l111ll_opy_(self):
        for bstack11lllll111_opy_ in reversed(self._1l111l11ll_opy_):
            bstack1l11l11l11_opy_ = bstack11lllll111_opy_
            data = self._1l111l11ll_opy_[bstack11lllll111_opy_][bstack11ll111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪෲ")]
            if isinstance(data, bstack1l1111lll1_opy_):
                if not bstack11ll111_opy_ (u"ࠨࡇࡄࡇࡍ࠭ෳ") in data.bstack11llll1ll1_opy_():
                    return bstack1l11l11l11_opy_
            else:
                return bstack1l11l11l11_opy_
    def _1l111l1l11_opy_(self, messages):
        try:
            bstack1l111ll11l_opy_ = BuiltIn().get_variable_value(bstack11ll111_opy_ (u"ࠤࠧࡿࡑࡕࡇࠡࡎࡈ࡚ࡊࡒࡽࠣ෴")) in (bstack1l11111lll_opy_.DEBUG, bstack1l11111lll_opy_.TRACE)
            for message, bstack11llll11l1_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack11ll111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ෵"))
                level = message.get(bstack11ll111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ෶"))
                if level == bstack1l11111lll_opy_.FAIL:
                    self._1l111l111l_opy_ = name or self._1l111l111l_opy_
                    self._11lll1lll1_opy_ = bstack11llll11l1_opy_.get(bstack11ll111_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨ෷")) if bstack1l111ll11l_opy_ and bstack11llll11l1_opy_ else self._11lll1lll1_opy_
        except:
            pass
    @classmethod
    def bstack1l111l1111_opy_(self, event: str, bstack1l1111llll_opy_: bstack1l111111ll_opy_, bstack11lll1l1l1_opy_=False):
        if event == bstack11ll111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ෸"):
            bstack1l1111llll_opy_.set(hooks=self.store[bstack11ll111_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫ෹")])
        if event == bstack11ll111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩ෺"):
            event = bstack11ll111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ෻")
        if bstack11lll1l1l1_opy_:
            bstack11llll1l11_opy_ = {
                bstack11ll111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ෼"): event,
                bstack1l1111llll_opy_.bstack11lll1l11l_opy_(): bstack1l1111llll_opy_.bstack1l111l1ll1_opy_(event)
            }
            self.bstack11lll1l111_opy_.append(bstack11llll1l11_opy_)
        else:
            bstack11lll1l1_opy_.bstack1l111l1111_opy_(event, bstack1l1111llll_opy_)
class Messages:
    def __init__(self):
        self._1l11l1111l_opy_ = []
    def bstack11lll11ll1_opy_(self):
        self._1l11l1111l_opy_.append([])
    def bstack1l111l1l1l_opy_(self):
        return self._1l11l1111l_opy_.pop() if self._1l11l1111l_opy_ else list()
    def push(self, message):
        self._1l11l1111l_opy_[-1].append(message) if self._1l11l1111l_opy_ else self._1l11l1111l_opy_.append([message])
class bstack1l11111lll_opy_:
    FAIL = bstack11ll111_opy_ (u"ࠫࡋࡇࡉࡍࠩ෽")
    ERROR = bstack11ll111_opy_ (u"ࠬࡋࡒࡓࡑࡕࠫ෾")
    WARNING = bstack11ll111_opy_ (u"࠭ࡗࡂࡔࡑࠫ෿")
    bstack11lll1l1ll_opy_ = bstack11ll111_opy_ (u"ࠧࡊࡐࡉࡓࠬ฀")
    DEBUG = bstack11ll111_opy_ (u"ࠨࡆࡈࡆ࡚ࡍࠧก")
    TRACE = bstack11ll111_opy_ (u"ࠩࡗࡖࡆࡉࡅࠨข")
    bstack11llll11ll_opy_ = [FAIL, ERROR]
def bstack11lllll1l1_opy_(bstack1l1111l1ll_opy_):
    if not bstack1l1111l1ll_opy_:
        return None
    if bstack1l1111l1ll_opy_.get(bstack11ll111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ฃ"), None):
        return getattr(bstack1l1111l1ll_opy_[bstack11ll111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧค")], bstack11ll111_opy_ (u"ࠬࡻࡵࡪࡦࠪฅ"), None)
    return bstack1l1111l1ll_opy_.get(bstack11ll111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫฆ"), None)
def bstack1l11111111_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack11ll111_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ง"), bstack11ll111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪจ")]:
        return
    if hook_type.lower() == bstack11ll111_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨฉ"):
        if current_test_uuid is None:
            return bstack11ll111_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧช")
        else:
            return bstack11ll111_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩซ")
    elif hook_type.lower() == bstack11ll111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧฌ"):
        if current_test_uuid is None:
            return bstack11ll111_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩญ")
        else:
            return bstack11ll111_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫฎ")