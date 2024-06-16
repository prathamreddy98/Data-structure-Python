class BST:
    def __init__(self, key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self, data):
        if self.key is None:#root is empty
            self.key=data
            return 
        if data<self.key:
            if self.lchild: # if there is already left child then this condition is true and we need to recusrsively call insert method
                self.lchild.insert(data)
            else:
                self.lchild=BST(data) # Root node does not have any child so we insert a new node
        else:
            if self.rchild: #since data is bigger than key adding to right part
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
                







        
root=BST(10)
root.insert(20)