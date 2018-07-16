
import re

def convert_to_binary(n):
    return bin(n)[2:]

def solution(n):
    bin = convert_to_binary(n)
    matchers = re.findall(r"(?=(1(0+)1))", bin)
    num_of_zeros = 0
    if matchers:
        for match in matchers:
            num_of_zeros = len(match[1]) if len(match[1]) > num_of_zeros else num_of_zeros
    return num_of_zeros
        
print(solution(32))