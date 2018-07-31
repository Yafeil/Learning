## 栈

### 栈的压入，弹出序列

**输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）**

~~~python
class Solutuon:
    def IsPopOrder(self,pushV,popV):
        length1 = len(pushV)
        length1 = len(popV)
        
        if length1 != legth2 or length1 == 0:
            return Flase
        
        p1_begin = 0
        p2_begin = 0
        stack = []
        
        while True:
            number = pushV[p1_begin]
            stack.append(number)
            
            while stack and stack[-1] == popV[p2_begin]:
                p2_begin += 1
                stack.pop()
            if p1_begin == length1 -1:
                if stack:
                    return False
                else:
                    return True
            p1_begin += 1
            
             
~~~

注:  	       

​            pushV = [5,4,3,2,1] 

​            popV = [4,5,3,2,1]

### 用两个栈实现队列

**用两个栈来实现一个队列，完成队列的Push和Pop操作。队列中的元素为int类型 **

**思路**

我们通过一个具体的例子分析往该队列插入和删除元素的过程。首先插入一个元素a，不妨先把它插入到stack1，此时stack1中的元素有{a}，stack2为空。再压入两个元素b和c，还是插入到stack1中，此时stack1的元素有{a,b,c}，其中c位于栈顶，而stack2仍然是空的。 

这个时候我们试着从队列中删除一个元素。按照先入先出的规则，由于a比b、c先插入队列中，最先删除的元素应该是a。元素a存储在stack1中，但并不在栈顶，因此不能直接进行删除操作。注意stack2我们一直没有使用过，现在是让stack2发挥作用的时候了。如果我们把stack1中的元素逐个弹出压入stack2，元素在stack2中的顺序正好和原来在stack1中的顺序相反。因此经过3次弹出stack1和要入stack2操作之后，stack1为空，而stack2中的元素是{c,b,a}，这个时候就可以弹出stack2的栈顶a了。此时的stack1为空，而stack2的元素为{b,a}，其中b在栈顶。 

因此我们的思路是：当stack2中不为空时，在stack2中的栈顶元素是最先进入队列的元素，可以弹出。如果stack2为空时，我们把stack1中的元素逐个弹出并压入stack2。由于先进入队列的元素被压倒stack1的栈底，经过弹出和压入之后就处于stack2的栈顶，有可以直接弹出。如果有新元素d插入，我们直接把它压入stack1即可。 

~~~python
class Soluton:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self,node):
        self.stack1.append(node)
    def pop(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
~~~

