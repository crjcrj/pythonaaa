import time
def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
start=time.time()
print(fib(40))
end=time.time()
dur=end-start
print(dur)


def preorder(self,node):
    stack=[node]
    while len(stack)>0:
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node=stack.pop()
