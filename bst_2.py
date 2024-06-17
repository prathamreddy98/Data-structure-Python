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
        if data<self.key:
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



           

        
root=BST(10)
list1=[6,3,1,6,98,3,7]

for i in list1:
    root.insert(i)
root.inorder()