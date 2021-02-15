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

    def delete_(self,data):
        while self is not None: 
          if self.data == data: #sileceğim data o andaki data ise sileceğim datayı bulmuşum demektir.
            break
          else:
            if data<self.data: #eğer silinecek data self.datadan küçükse onu bulmak için yerimi sola kaydırırım.
              self=self.left #artık sol kısıma geçtim.
            else:
              self=self.right  #değilse artık sağ dalı gösteriyorum.

        if self is None:
          print("bole bir agac yok")

        else: #Ağaç boş değilse 
          
          if self.right is not None:
            temp = self.right  #geçici bir değer oluşturup sayımın sağını göstermesini sağladım.
            if temp.left is not None:
              while temp.left is not None:
                temp=temp.left
                self.data=temp.data
                if temp.right is not None:
                  temp.parent.left = temp.right
                  temp.right.parent = temp.parent
                else: 
                  temp.parent.left=None
            else:#geçici değerin soluda boşsa
              self.data=temp.data #silinecek sayımı geçici değerimize(ki o da silinecek sayının solunugösteriyordu)atıyyoruz   40=48
              if temp.right is not None:#48=48
                temp.parent.right=temp.right#sağımın parentı sağımdaki sayı olmuş oldu.
                temp.right.parent=temp.parent#yukarda olan sayımınn parentı yerine koyduğum sayımın parentı olmuş oldu.#bağ kopuş oldu
              else:
                temp.parent.right=None
            temp=None#bağı kopan düğüm silinir.
            return  
          elif self.left is not None:#sayımın solu boş değilse
            if self.parent is not None:#sayımın parentı varsa yani kök değilse
              if self == self.parent.left:#sayım solundaki dalın parentı ise
                self.parent.left=self.left#parentı yani sayımı solundaki dal yap
                self.left.parent=self.parent #yeni parentımın parentıda sileceğim sasyımın parentı olmuş olur.
              else:
                self.parent.right=self.left
                self.left.parent=self.parent
            else:
              self.left.parent =None#düğüm ise parentı silinir
              a=self.left  #düğümde sayının sol kısmını göstermiş olur.
            self=None #bağlantısı kopan düğüm silinir.
            return
          else: #Silinecek düğümümün sağı ve solu boş ise buraya girilir.
            if self.parent is not None: #sayının parentı var ise
              if self.parent.left == self:#sayımın parentı sayımmı gösteriyorsa(yani kopacak düğüm parentın sağındamı solundamı bunu anlar.)
                self.parent.left = None#Ve aralarındaki bağlantıyı koparırım
              else:
                self.parent.right = None
              self=None#bağlantısı kopan sayımı silerim

            else:
              a =None #zaten parentı yoksa tek bir düğümdür ve o düğümü direk silerim
              return                 

               
                      

            
# Ağacı yazdır
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
root.insert(25)
root.insert(28)
root.insert(38)
root.insert(48)
root.PrintTree()

print("/n")

root.delete_(5)
root.PrintTree()
print("/n")

root.delete_(25)
root.PrintTree()