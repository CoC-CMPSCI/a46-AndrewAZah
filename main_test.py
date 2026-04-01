import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            assert False, f'Expect: {expected}'
    else:
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    # student female cs → factor=3.0, amount=30000.00
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'3\.0.*30000\.00'], lines)


@pytest.mark.T2
def test_main_2():
    # student male cs → factor=2.0, amount=20000.00
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'2\.0.*20000\.00'], lines)


@pytest.mark.T3
def test_main_3():
    # student female other → factor=1.0, amount=10000.00
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'1\.0.*10000\.00'], lines)


@pytest.mark.T4
def test_main_4():
    # nonstudent male other → factor=0.1, amount=1000.00
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'0\.1.*1000\.00'], lines)
