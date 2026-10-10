class Solution:

    def encode(self, strs: List[str]) -> str:
        return str([s[::-1] for s in strs])
    def decode(self, s: str) -> List[str]:
        return [s[::-1] for s in eval(s)]
