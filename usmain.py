import zlib, base64
exec(zlib.decompress(base64.b64decode(b'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')))
