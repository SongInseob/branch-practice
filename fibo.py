def fibo(n):
    """
    피보나치 수열의 n번째 항을 계산합니다.

    Args:
        n: 계산할 항의 번호 (1 이상의 정수)

    Returns:
        n번째 피보나치 수
    """
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == '__main__':
    print(fibo(4))
