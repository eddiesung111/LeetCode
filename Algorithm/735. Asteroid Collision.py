class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Time = O(n)
        # Space = O(n)
        val = asteroids[0]
        stack = [val]
        prev_pos = (val > 0)
        for i in range(1,len(asteroids)):
            curr_val = asteroids[i]
            if curr_val > 0:
                stack.append(curr_val)
                prev_pos = True
            else:
                if prev_pos == True:
                    while stack and 0 < stack[-1] < -curr_val:
                        stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(curr_val)
                        prev_pos = False
                    if stack and stack[-1] == -curr_val:
                        stack.pop()
                else:
                    stack.append(curr_val)
        return stack
