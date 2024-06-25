class BST:
    def __init__(self, key): # Self represents the object 
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self, data):
        if self.key is None:#root is empty
            self.key=data
            return 
        if self.key==data:
            return #Handling duplicate values
        if data<self.key :
            if self.lchild: # if there is already left child then this condition is true and we need to recusrsively call insert method if self.child is equivalent to if self.child is Falsw
                self.lchild.insert(data)
            else:
                self.lchild=BST(data) # Root node does not have any child so we insert a new node
        else:
            if self.rchild: #since data is bigger than key adding to right part
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
                
    def search(self, data): #Here self is representing the object hence self.key. Self is root object self is root here
        if self.key==data:
            print("Node is found")
            return
        if data<self.key: # Searching in left sub tree
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node not found in left subtree")
        else:
            if self.rchild: # if rchild is present recursively search in right sub tree
                self.rchild.search(data)
            else:
                print("Not found in right subtree")

    def preorder(self):
        print(self.key)
        if self.lchild: #if left subtree is present again call preorder
            self.lchild.preorder()
        if self.rchild:# same for right subtree
            self.rchild.preorder()

    def inorder(self):
        if self.lchild: #if left subtree in present call it recursively
            self.lchild.inorder()
        print(self.key) # visit root node
        if self.rchild:
            self.rchild.inorder() # visit right subtree


    def delete(self,data, curr):# curr is root.key. we passed this to delete the root node 
        if self.key is None: #tree is empty
            print("tree is empty")
            return # Once python encounters a return it exits the condition 
        if data<self.key:
            if self.lchild: #check if lchild exists
                 self.lchild=self.lchild.delete(data,curr) #Need to store in lchild since if we delete node then tree has to be updated to point to None 
            else:
                print("Node not present in Left subtree")
        elif data>self.key: #iterating in right subtree
            if self.rchild:
                self.rchild=self.rchild.delete(data,curr)
            else:
                print("not Found")
        else: #Since both of above conditions were false it means the node we want to delete is the root node
            #These if conditions will handle the case where the node to be deleted has 0 or 1 child
            if self.lchild is None:
                temp=self.rchild
                if data ==curr: # to handle case when we have to delete a root node
                    self.key=temp.key
                    self.lchild=temp.lchild # since a root node is to be deleted, we have to make it's L and R pointers none. Since lchild is not there, we replace it with rchild
                    self.rchild=temp.rchild
                    temp=None
                    return 
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            #To delete node having 2 children
            node=self.rchild # Replacing with minimum from right subtree
            while node.lchild: # Since smallest value will be in the left part of right sub tree
                node=node.lchild
            self.key=node.key # Replaces the value with min from right subtree
            self.rchild=self.rchild.delete(node.key,curr)#After replacing the value we delete the node
        return self
      
def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) +count(node.rchild)



        
root=BST(10)
list1=[1,12]

for i in list1:
    root.insert(i)
root.preorder()
print()
if count(root)>1:
    root.delete(10,root.key)
else:
    print("cannot delete")
print("After deleting: ")
root.preorder()