class MinStack:
# 初始化兩個陣列，一個用來儲存一般的element的stack，一個用來把每次加入stack後的所有的當下最小值同步儲存下來，叫做min_stack
# 這樣就會有兩個stack，而每次要針對一般的stack進行pop或push的時候，也會同步pop或push min_stack
# 這樣設計的原因是因為題目有針對時間複雜度 O(1)的要求

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_tmp = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_tmp)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]