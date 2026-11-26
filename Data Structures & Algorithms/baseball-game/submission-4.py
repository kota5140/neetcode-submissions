class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for op in operations:
            print(stack)
            if op == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b)
                stack.append(a)
                stack.append(a+b)
                total += a+b
            elif op == "C":
                a = stack.pop()
                total -= int(a)
            elif op == "D":
                a = int(stack.pop())
                stack.append(a)
                stack.append(a*2)
                total += a*2
            else:
                stack.append(op)
                total += int(op)
        return total
