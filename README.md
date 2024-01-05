# infosoft_assesment
### Calender Problem Solution 
#### in the given code the problem was in the given insert fucntion where the insert was happening on wrong parameter
#### def insert(self, node: 'Node') -> bool:
####            if not self.right_child:
####                self.right_child = node
####                return True
####            return self.left_child.insert(node)
####        elif node.end >= self.start:
####            if not self.left_child:
####                self.left_child = node
####                return True
####            return self.left_child.insert(node)

if we see above function the comparison between node.start and self.end is wrong since we need not to do double booking we have only two conditions to check
node.end should be <= self.start and node.start >= self.end
so in the above function its opposite and hence it causes double booking and throws error.
so we need to add else condition if the above two condition is not satisfied we can assume that there is a case of double booking and we can return false in the case.
