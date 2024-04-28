import platform, os, sys
from ctypes import (
    CDLL,
    c_int,
    c_void_p,
    c_char_p,
    Structure,
    c_uint,
    c_char,
    POINTER,
    CFUNCTYPE,
    cast,
)
from typing import Callable, Union, Tuple


class webview_t(c_void_p):
    pass


# Window size hints
class webview_hint_t(c_int):
    # Width and height are default size.
    WEBVIEW_HINT_NONE = 0
    # Width and height are minimum bounds.
    WEBVIEW_HINT_MIN = 1
    # Width and height are maximum bounds.
    WEBVIEW_HINT_MAX = 2
    # Window size can not be changed by a user.
    WEBVIEW_HINT_FIXED = 3


class webview_error_t(c_int):
    # Missing dependency.
    WEBVIEW_ERROR_MISSING_DEPENDENCY = -5
    # Operation canceled.
    WEBVIEW_ERROR_CANCELED = -4
    # Invalid state detected.
    WEBVIEW_ERROR_INVALID_STATE = -3
    # One or more invalid arguments have been specified e.g. in a function call.
    WEBVIEW_ERROR_INVALID_ARGUMENT = -2
    # An unspecified error occurred. A more specific error code may be needed.
    WEBVIEW_ERROR_UNSPECIFIED = -1
    # OK/Success. Functions that return error codes will typically return this
    # to signify successful operations.
    WEBVIEW_ERROR_OK = 0
    # Signifies that something already exists.
    WEBVIEW_ERROR_DUPLICATE = 1
    # Signifies that something does not exist.
    WEBVIEW_ERROR_NOT_FOUND = 2


# Native handle kind. The actual type depends on the backend.
class webview_native_handle_kind_t(c_int):

    # Top-level window. @c GtkWindow pointer (GTK), @c NSWindow pointer (Cocoa)
    # or @c HWND (Win32).
    WEBVIEW_NATIVE_HANDLE_KIND_UI_WINDOW = 0
    # Browser widget. @c GtkWidget pointer (GTK), @c NSView pointer (Cocoa) or
    # @c HWND (Win32).
    WEBVIEW_NATIVE_HANDLE_KIND_UI_WIDGET = 1
    # Browser controller. @c WebKitWebView pointer (WebKitGTK), @c WKWebView
    # pointer (Cocoa/WebKit) or @c ICoreWebView2Controller pointer
    # (Win32/WebView2).
    WEBVIEW_NATIVE_HANDLE_KIND_BROWSER_CONTROLLER = 2


class webview_version_t(Structure):
    _fields_ = [("major", c_uint), ("minor", c_uint), ("patch", c_uint)]


class webview_version_info_t(Structure):
    _fields_ = [
        ("version", webview_version_t),
        ("version_number", c_char * 32),
        ("pre_release", c_char * 48),
        ("build_metadata", c_char * 48),
    ]


class webview_version_info_t_ptr_t(POINTER(webview_version_info_t)):
    pass


class _Webview_Version:
    def __init__(self, v: webview_version_t) -> None:
        self.major = v.major
        self.minor = v.minor
        self.patch = v.patch

    def __repr__(self) -> str:
        return "{}.{}.{}".format(self.major, self.minor, self.patch)


class Webview_Version:
    def __repr__(self) -> str:
        return self.version_number

    def __init__(self, lpwv: webview_version_info_t_ptr_t) -> None:
        self.version = _Webview_Version(lpwv.contents.version)
        self.version_number = lpwv.contents.version_number.decode("utf8")
        self.pre_release = lpwv.contents.pre_release.decode("utf8")
        self.build_metadata = lpwv.contents.build_metadata.decode("utf8")


class webview_exception(Exception):
    pass


isbit64 = platform.architecture()[0] == "64bit"
DLL3264path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "platform", sys.platform, ("x86", "x64")[isbit64]
    )
)
webviewdll = os.path.join(DLL3264path, "webview")


webview_dispatch_fn_t = CFUNCTYPE(None, webview_t, c_void_p)
webview_bind_fn_t = CFUNCTYPE(None, c_char_p, c_char_p, c_void_p)


def __loadwebviewfunction(ex=False):
    try:
        _webview = CDLL(webviewdll)
        webview_create = _webview.webview_create
        webview_create.argtypes = c_int, c_void_p
        webview_create.restype = webview_t
        webview_set_title = _webview.webview_set_title
        webview_set_title.argtypes = webview_t, c_char_p
        webview_set_title.restype = webview_error_t
        webview_set_size = _webview.webview_set_size
        webview_set_size.argtypes = webview_t, c_int, c_int, webview_hint_t
        webview_set_size.restype = webview_error_t
        webview_set_html = _webview.webview_set_html
        webview_set_html.argtypes = webview_t, c_char_p
        webview_set_html.restype = webview_error_t
        webview_run = _webview.webview_run
        webview_run.argtypes = (webview_t,)
        webview_run.restype = webview_error_t
        webview_destroy = _webview.webview_destroy
        webview_destroy.argtypes = (webview_t,)
        webview_destroy.restype = webview_error_t
        webview_navigate = _webview.webview_navigate
        webview_navigate.argtypes = webview_t, c_char_p
        webview_navigate.restype = webview_error_t
        webview_eval = _webview.webview_eval
        webview_eval.argtypes = webview_t, c_char_p
        webview_eval.restype = webview_error_t
        webview_get_window = _webview.webview_get_window
        webview_get_window.argtypes = (webview_t,)
        webview_get_window.restype = c_void_p
        webview_get_native_handle = _webview.webview_get_native_handle
        webview_get_native_handle.argtypes = webview_t, webview_native_handle_kind_t
        webview_get_native_handle.restype = c_void_p
        webview_init = _webview.webview_init
        webview_init.argtypes = webview_t, c_char_p
        webview_init.restype = webview_error_t
        webview_version = _webview.webview_version
        webview_version.restype = webview_version_info_t_ptr_t
        webview_terminate = _webview.webview_terminate
        webview_terminate.argtypes = (webview_t,)
        webview_terminate.restype = webview_error_t
        webview_unbind = _webview.webview_unbind
        webview_unbind.argtypes = webview_t, c_char_p
        webview_unbind.restype = webview_error_t

        webview_return = _webview.webview_return
        webview_return.argtypes = webview_t, c_char_p, c_int, c_char_p
        webview_return.restype = webview_error_t
        webview_dispatch = _webview.webview_dispatch
        webview_dispatch.argtypes = webview_t, c_void_p, c_void_p
        webview_dispatch.restype = webview_error_t
        webview_bind = _webview.webview_bind
        webview_bind.argtypes = webview_t, c_char_p, c_void_p, c_void_p
        webview_bind.restype = webview_error_t
        variables = locals()  # 获取函数内的所有变量
        globals().update(variables)  # 将所有变量添加到全局命名空间
    except:
        log = 'load module "{}" failed'.format(webviewdll)
        if ex:
            raise Exception(log)


__loadwebviewfunction()


def declare_library_path(path):
    global webviewdll
    webviewdll = path
    __loadwebviewfunction(True)


class Webview:
    def __init__(
        self, debug: bool = False, window: c_void_p = None, init_js: str = None
    ) -> None:
        self.pwebview = 0
        _w = webview_create(debug, window)
        if _w == 0:
            raise Exception()
        self.pwebview = _w
        if init_js:
            self.init(init_js)

    def resolve(self, seq: str, status: int, result: str) -> webview_error_t:
        return webview_return(
            self.pwebview, seq.encode("utf8"), status, result.encode("utf8")
        )

    def bind(
        self, name: str, fn: Callable[[str, str], Union[None, str, Tuple[str, int]]]
    ) -> webview_error_t:

        def wrapped_fn(seq: c_char_p, req: c_char_p, args: c_void_p):
            seq = seq.decode("utf8")
            _result = fn(seq, req.decode("utf8"))

            if _result is None:
                return
            if isinstance(_result, str):
                result, status = _result, 0
            elif isinstance(_result, Tuple[str, int]):
                result, status = _result

            self.resolve(seq, status, result)

        return webview_bind(
            self.pwebview,
            name.encode("utf8"),
            cast(webview_bind_fn_t(wrapped_fn), c_void_p).value,
            None,
        )

    def dispatch(self, fn: Callable[[], None]) -> webview_error_t:
        def wrapped_fn(_w: webview_t, _arg: c_void_p):
            fn()

        return webview_dispatch(
            self.pwebview, cast(webview_dispatch_fn_t(wrapped_fn), c_void_p).value, None
        )

    def unbind(self, name: str) -> webview_error_t:
        return webview_unbind(self.pwebview, name.encode("utf8"))

    def get_window(self) -> c_void_p:
        return webview_get_window(self.pwebview)

    def get_native_handle(self, kind: webview_native_handle_kind_t) -> c_void_p:
        return webview_get_native_handle(self.pwebview, kind)

    def eval(self, js: str) -> webview_error_t:
        return webview_eval(self.pwebview, js.encode("utf8"))

    def navigate(self, url: str) -> webview_error_t:
        return webview_navigate(self.pwebview, url.encode("utf8"))

    def init(self, js: str) -> webview_error_t:
        return webview_init(self.pwebview, js.encode("utf8"))

    def destroy(self) -> webview_error_t:
        if self.pwebview:
            _ = webview_destroy(self.pwebview)
            self.pwebview = None
            return _
        else:
            return webview_error_t.WEBVIEW_ERROR_OK

    def __del__(self) -> None:
        self.destroy()

    def run(self) -> webview_error_t:
        return webview_run(self.pwebview)

    def set_html(self, html: str) -> webview_error_t:
        return webview_set_html(self.pwebview, html.encode("utf8"))

    def set_size(
        self,
        width: int,
        height: int,
        hints: webview_hint_t = webview_hint_t.WEBVIEW_HINT_NONE,
    ) -> webview_error_t:
        return webview_set_size(self.pwebview, width, height, hints)

    def set_title(self, title: str) -> webview_error_t:
        return webview_set_title(self.pwebview, title.encode("utf8"))

    def terminate(self) -> webview_error_t:
        return webview_terminate(self.pwebview)

    @staticmethod
    def version() -> Webview_Version:
        return Webview_Version(webview_version())


__all__ = [
    getattr(_, "__name__")
    for _ in [
        declare_library_path,
        webview_hint_t,
        webview_error_t,
        webview_native_handle_kind_t,
        webview_exception,
        Webview,
    ]
]
