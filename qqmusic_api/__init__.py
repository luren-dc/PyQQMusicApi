from .api import login, search, song
from .settings import __set_qimei, __set_uid
from .utils.common import random_string
from .utils.credential import Credential
from .utils.qimei import Qimei

# 随机 UID
__set_uid(random_string(10, "0123456789"))
# 随机 QIMEI36
result = Qimei.get()
__set_qimei(result.q36 if result.q36 else "cc8d07a748d4be0a8b91eacd100014a1730e")

__all__ = ["Credential", "exceptions", "login", "search", "song"]
