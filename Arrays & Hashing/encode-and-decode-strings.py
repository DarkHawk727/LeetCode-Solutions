from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        code = ""

        for elem in strs:
            code += str(len(elem)) + "#" + elem

        return code

    def decode(self, code: str) -> List[str]:
        decoded, i = [], 0

        while i < len(code):
            j = i
            while code[j] != "#":
                j += 1
            length = int(code[i:j])
            decoded.append(code[j + 1 : j + length + 1])
            i = j + length + 1

        return decoded


"""
Algorithm:
For the encoding step we prepend the length and then a # before each word and
concatenate all the words together.
For the decodeing, we look until we find a # and then take that to be the
length. Then we append a slice from the start to the end to the answer.

Time Complexity:
Encoding takes O(n) since we loop through strs.
Decoding take O(n) time as well since we are looping until the end of code.
"""
