class Node:
    def __init__(self, data):
        self.left   = None
        self.right  = None
        self.parent = None  
        self.data   = data
		
    def insert(self, data):
        if self.data:                       
            if data < self.data:              
                if self.left is None:           
                    self.left = Node(data)
                    self.left.parent = self     
                else:
                    self.left.insert(data)      
            elif data > self.data:          
                if self.right is None:          
                    self.right = Node(data)
                    self.right.parent = self   
                else:                           
                    self.right.insert(data)
        else:
            self.data = data      

	# Sürekli ağacın soluna dogru giderek en kücük dugumu bulan fonksiyondur.
    def minimumValueNode(self, node):
        current = node	# Basta node'un ilk degeri current'a setlenir. 
        while(current.left is not None): # Agacın soluna dogru bitene kadar gidilir.
            current = current.left # Bir alttaki dugumle current yeniden setlenir.
        return current	# En alttaki soldaki dugum en kucuk degeri belirtir.

	# 
    def delete(self, data):
        if self is None: # Agacta hic node yoksa silinecek dugumde yoktur.
            return None # Bos deger doner.
        if data < self.data: # Eger silmek istenilen node'un degeri kucukse sola dogru gidilerek bulunur.
            self.left = self.left.delete(data)
        elif data > self.data: # Eger silmek istenilen node'un degeri buyukse saga dogru gidilerek bulunur.
            self.right = self.right.delete(data)
        else: # Tek cocuklu dugumu siliyor.
            if self.left is None: 
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
				
			# Ikı cocuklu dugumu silen kod satırı
            temp = self.minimumValueNode(self.right)
            self.data = temp.data
            self.right = self.right.delete(temp.data)
			
        return self


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data,end='-')
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

root = Node(25)
root.insert(12)
root.insert(10)
root.insert(22)
root.insert(5)
root.insert(36)
root.insert(30)
root.insert(40)
root.insert(28)
root.insert(38)
root.insert(48)
root.PrintTree()

# Use the delete method to delete nodes

root.delete(25)
print("\n25 is deleted")
root.PrintTree()
root.delete(30)
print("\n30 is deleted")
root.delete(38)
print("38 is deleted")
root.PrintTree()