class Solution:

    def encode(self, strs: List[str]) -> str:
        str = ""
        if not strs:
            return "§"

        for el in strs:
            str += el + ":;"

        return str[:-2]


    def decode(self, s: str) -> List[str]:

        if s == "§":
            return []

        return s.split(":;")
