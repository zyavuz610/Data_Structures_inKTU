# Veri Yapıları 5.ödev
# 348403-Hatice Yaşar
# 348399-Merve Zeynep Aygün
# breadth first search with using tree structure

class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

    def insert(self,data):
        if (self.data is None):
            self.data = data
            
        else:
            if( data < self.data ):
                if (self.left is None): 
                    self.left = Node(data)
                    self.left.parent = self
                else:
                    self.left.insert(data)
            elif( data > self.data ):
                if ( self.right is None):
                    self.right = Node(data)
                    self.right.parent = self
                else:
                    self.right.insert(data)
    def depth(self,Root):
        if (Root is None):
            return 0
        else:
            l = self.depth(Root.left)
            r= self.depth(Root.right)
            return max(l,r)+1
    def level_order(self,Root):
        
        height = self.depth(Root)
        for i in range(0,height):
            self.traversal(Root,i)
    def traversal(self,Root,level):
        if Root==None:
            return
        elif level==0:
            print(Root.data,end = '-')
        elif level >0:
            self.traversal(Root.left,level-1)
            self.traversal(Root.right,level-1)
    
Root = Node(25)
Root.insert(20)
Root.insert(10)
Root.insert(12)
Root.insert(22)
Root.insert(5)
Root.insert(36)
Root.insert(30)
Root.insert(40)
Root.insert(28)
Root.insert(38)
Root.insert(48)

Root.level_order(Root)