class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while (stack):
                if(len(stack)) == 1: break
                right = stack[-1]
                left = stack[-2]
                if right * left > 0: break # same direction
                if left < 0: break # left asteroid going left, right asteroid going right
                if abs(left) > abs(right): stack.pop(-1)
                elif abs(left) < abs(right): stack.pop(-2)
                else:
                    stack.pop(-1)
                    stack.pop(-1)
        return stack

            