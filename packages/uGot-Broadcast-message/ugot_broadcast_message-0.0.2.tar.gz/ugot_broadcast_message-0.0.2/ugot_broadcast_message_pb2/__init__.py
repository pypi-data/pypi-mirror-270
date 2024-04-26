import re
import google.protobuf

try:
    ret = re.search(r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)", google.protobuf.__version__)
    if ret:
        major = int(ret.group('major'))
        minor = int(ret.group('minor'))
        patch = int(ret.group('patch'))
        if (major > 3) or (major == 3 and minor > 20):
            # protobuf > 3.20.x, Use _pb2_gen2.py generated with protoc >= 3.19.0
            from .ugot_broadcast_message_pb2_gen2 import *
        else:
            # protobuf <= 3.20.x, Use _pb2_gen1.py generated with protoc < 3.19.0
            from .ugot_broadcast_message_pb2_gen1 import *
    else:
        raise RuntimeError('parse version format fail')
except:
    # Use _pb2_gen2.py generated with protoc >= 3.19.0 by default
    from .ugot_broadcast_message_pb2_gen2 import *
