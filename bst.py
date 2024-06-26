class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data=data
        self.left=None
        self.right=None

    def add_child(self, data):
        if data==self.data: #if an element already exists then we can't add it again since it is BST
            return
        if data<self.data: # add in left subtree
            #check if it's not leaf node
            if self.left:
                self.left.add_child(data)#recursively call add child method since it's another left subtree
                
            else:
                self.left=BinarySearchTreeNode(data)

            
        else:  # Add in right subtree
            if self.right:
                self.right.add_child(data)
            else:#it's a leaf node
                self.right=BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements=[]
        #visit left
        if self.left:
            elements+=self.left.in_order_traversal()
         #visit root
        elements.append(self.data)

        #visit right
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    
    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val.self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.right
        return self.right.find_max()
    
    def delete(self, val):
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            max_val=self.left.find_max()
            self.data=max_val
            self.left=self.left.delete(max_val)
        return self
    
  





                    
                    
                
                 
            


    
def build_tree(elements):
        root=BinarySearchTreeNode(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i])
        return root
        
           
    
if __name__=='__main__':
    numbers=[17,4,1,20,9,23,18,34]
    t=build_tree(numbers)
    print(t.in_order_traversal())
    t.delete(9)
    print(t.in_order_traversal())

    


