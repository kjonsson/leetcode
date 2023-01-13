#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
from collections import deque

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack2) == 0:
            self._move_between_stacks()
            
        val = self.stack2.pop()
        return val
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack2) == 0:
            self._move_between_stacks()
            
        return self.stack2[-1]
        
        
    def _move_between_stacks(self):
        while len(self.stack1):
            val = self.stack1.pop()
            self.stack2.append(val)
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

