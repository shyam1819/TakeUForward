class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #your code goes here
        freq = self.freqMap(t)
        fkeys = freq.keys()
        required = len(t)
        i,j = 0,0
        n = len(s)
        m = {}
        substr = s
        formed = 0
        has_matched=False
        if len(t)>len(s):
            return ""
        while j<n:
            if s[j] in fkeys:
                m[s[j]] = m.get(s[j],0)+1
                # Loop for moving i
                if m[s[j]]<=freq[s[j]]:
                    formed+=1
                while required==formed:
                    has_matched=True
                    if j-i+1<len(substr):
                        substr = s[i:j+1]
                    if m.get(s[i],None):
                        m[s[i]]=m[s[i]]-1 
                        if m[s[i]]<freq[s[i]]:
                            formed-=1
                    i+=1
            j+=1  
        return substr if has_matched else ""   

    def freqMap(self, s):
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0)+1
        return freq
        
