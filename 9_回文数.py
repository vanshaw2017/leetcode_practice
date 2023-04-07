def isPalindrome( x: int) -> bool:
    if not x:
        return False
    # 负数不可能是回文数
    if x < 0:
        return False
    if x == 0:
        return True
    s = str(x)
    res = []
    while x > 0:
        # 余数是最低一位
        tail = x % 10
        x = x // 10
        res.append(str(tail))
    print(res)
    s_ = ''.join(res)
    return s == s_

if __name__ == "__main__":
    print(isPalindrome(0))
