# 9.3
# 모르겠다 ! !


# 9.4
class OopsException(Exception):
    pass


try:
    raise OopsException("oops")
except OopsException as other:
    print(f"Caught an {other}")
