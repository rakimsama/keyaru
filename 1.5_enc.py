#----------------------------------------------
import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))
