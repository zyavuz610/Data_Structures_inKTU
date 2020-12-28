class Node:
    def __init__(self, data):
        self.left   = None
        self.right  = None
        self.parent = None  # yeni
        self.data   = data
    def insert(self, data):
        if self.data:                       # karılaştırma yaparak ekle
            if data < self.data:            # küçükse sola       
                if self.left is None:           # sol boşsa sola ekle
                    self.left = Node(data)
                    self.left.parent = self     # yeni
                else:
                    self.left.insert(data)      # sol boş değilse sol alt-ağaca ekle
            elif data > self.data:          # büyükse sağa
                if self.right is None:          # sağ boşsa sağa ekle
                    self.right = Node(data)
                    self.right.parent = self    # yeni
                else:                           # sağ boş değilse sağ alt-ağaca ekle
                    self.right.insert(data)
        else:
            self.data = data        # ağacın ilk düşümü
            
# Ağacı yazdır
    def PrintTree(self):
        print( self.data,end='-')
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
        
    def sizeTree(self): 
        if self.left and self.right:
            return 1 + self.left.sizeTree() + self.right.sizeTree()
        elif self.left:
            return 1 + self.left.sizeTree()
        elif self.right:
            return 1 + self.right.sizeTree()
        else:
            return 1
    
    def depth(self):
        if self.left and self.right:
            l = self.left.depth()
            r = self.right.depth()
            return 1 + max(l,r)
        elif self.left:
            return 1 + self.left.depth()
        elif self.right:
            return 1 + self.right.depth()
        else:
            return 1

# Use the insert method to add nodes

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(5)
root.insert(8)
root.insert(13)
root.insert(23)
root.PrintTree()


"""
# 25,36,20,10,5,22,40,48,38,30,22,12,28
root = Node(25)
root.insert(36)
root.insert(20)
root.insert(10)
root.insert(5)
root.insert(22)
root.insert(40)
root.insert(48)
root.insert(38)
root.insert(30)
root.insert(12)
root.insert(28)

print(root.sizeTree(),root.depth())

"""