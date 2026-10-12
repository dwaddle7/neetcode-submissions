class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []
        # for asteroid in asteroids:
        #     stack.append(asteroid)
        #     while (stack):
        #         if(len(stack)) == 1: break
        #         right = stack[-1]
        #         left = stack[-2]
        #         if right * left > 0: break # same direction
        #         if left < 0: break # left asteroid going left, right asteroid going right
        #         if abs(left) > abs(right): stack.pop(-1)
        #         elif abs(left) < abs(right): stack.pop(-2)
        #         else:
        #             stack.pop(-2)
        #             stack.pop(-1)
        # return stack


















            

            stack = []
            for asteroid in asteroids:
                stack.append(asteroid)
                while(stack):
                    if len(stack) == 1:
                        break
                    else:
                        left = stack[-2]
                        right = stack[-1]
                        if left < 0 and right > 0:
                            break
                        elif left * right > 0:
                            break
                        else: # left * right < 0 means different signs and left is moving right and right is moving left so collision will happen
                            if abs(left) > abs(right):
                                stack.pop(-1)
                            elif abs(left) < abs(right):
                                stack.pop(-2)
                            else: # both have same abs value
                                stack.pop(-2)
                                stack.pop(-1)
            return stack