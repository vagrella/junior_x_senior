# Júnior:
import contextlib

try:
    print(x)
except NameError:
    pass

# Senior:
with contextlib.suppress(NameError):
    print(x)
