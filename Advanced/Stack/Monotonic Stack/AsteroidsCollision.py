class Solution:
    def asteroidCollision(self, asteroids):
        stk = []
        for i in asteroids:
            while stk and i*stk[-1]<0 and stk[-1]>0:
                if abs(i)>abs(stk[-1]):
                    stk.pop()
                elif abs(i)<abs(stk[-1]):
                    break
                else:
                    stk.pop()
                    break
            else:
                stk.append(i)
        return stk
  
