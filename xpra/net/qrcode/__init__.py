# This file is part of Xpra.
# Copyright (C) 2022 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

def qrencode(s):
    try:
        from xpra.net.qrcode.qrencode import encode_image
    except ImportError:
        return None
    return encode_image(s)
