def test(t):
    assert type(t) is int, f"{t}흐음"


lists = [1, 3, 5, 3.13, 3, 3]
try:
    for i in lists:
        test(i)
except AssertionError as errorMsg:
    print(errorMsg)
