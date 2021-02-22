class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        for i in range(len(indexes)):
            if S[indexes[i]:indexes[i]+len(sources[i])] != sources[i]:
                indexes[i] = -1
                sources[i] = ''
                targets[i] = ''
        for i in range(len(indexes)):
            if indexes[i] != -1:
                S = S.replace(sources[i],targets[i],1)
        return S