#!/usr/bin/env python
import pyotp
import sys

def code():
    totp = pyotp.TOTP(sys.argv[1])
    return totp.now()

print code()

