# 9.3
def test(func):
    '''
    함수 func을 호출되면 start, 끝나면 end를 출력하는 함수
    :param func: 함수 이름
    :return:
    '''
    def inner(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")
    return inner


# 9.4
class OopsException(Exception):
    pass


try:
    raise OopsException("oops")
except OopsException as other:
    print(f"Caught an {other}")
