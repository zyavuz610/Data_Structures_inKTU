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
       visited = []                                 #ziyaret edilen düğümleri tutacak bir dizi oluşturduk
       
       if self:
           visited.append(self)                     #diziyi ilk düğümle birlikte arttırdık
           print(self.data, end='-')                #ilk düğümün içeriğini yazdık
       current = self                               #current adlı değişkene self i atadık ve replikasyon yapmış olduk
       while current :                              
            if current.left:                        #self in soldaki ilk düğümü iken:
                print(current.left.data, end='-')   #self in soldaki ilk düğümünün datasını yazdık
                visited.append(current.left)        #visited adlı dizimize soldaki ilk düğümü geçirdik
            if current.right:                       #self in sağdaki ilk düğümü iken:
                print(current.right.data, end='-')  #self in sağdaki ilk düğümünün datasını yazdık
                visited.append(current.right)       #visited adlı dizimize soldaki ilk düğümü geçirdik      
            visited.pop(0)                          #.pop(0) ile visited adlı dizinin ilk elemanını patlattık(döngünün her seferinde kök düğümü yazmaması için)
            if not visited:                         #tüm düğümler ziyaret edildiyse aşağıdaki break ile döngüyü kırdık
                break
            current = visited[0]                    #listenin ilk elemanı kök düğümden sonraki ilk düğüm oldu
            
        
  

        
    def sizeTree(self): 
        if self.left and self.right:
            return 1 + self.left.sizeTree() + self.right.sizeTree()
        elif self.left:
            return 1 + self.left.sizeTree()
        elif self.right:
            return 1 + self.right.sizeTree()
        else:
            return 1
    
    def breadth(self):
        if self.left and self.right:
            l = self.left.breadh()
            r = self.right.breadth()
            return 1 + max(l,r)
        elif self.left:
            return 1 + self.left.breadth()
        elif self.right:
            return 1 + self.right.breadth()
        else:
            return 1

# Use the insert method to add nodes

root = Node(25)
root.insert(20)
root.insert(36)
root.insert(10)
root.insert(12)
root.insert(5)
root.insert(22)
root.insert(30)
root.insert(40)
root.insert(28)
root.insert(38)
root.insert(48)
root.PrintTree()
