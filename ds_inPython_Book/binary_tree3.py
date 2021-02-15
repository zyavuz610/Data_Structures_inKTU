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
        #print(self.data),
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


    """     method 1 """

    #verilen düğümün altındaki en küçük değere sahip düğümü döndüren method
    def findMinvalueData(node):
        current = node
 
        # yaprak düğüme kadar git en küçüğü en sol yaprak düğümde zaten
        while(current.left is not None):
            current = current.left
 
        return current
            

        
    """ üç tane durum söz konusu
    1- eğer silinecek değer yaprak düğümse direk silinir. bunu tutan değere null atanır.
    2- eğer silinecek değer bir tane çocuk tutuyorsa --> çocuk kopyalanır kendi değeriyle yer değiştirilir.
    3- eğer iki çocuğu da var çocukları arasında en küçük değere sahip düğüm bulunur ve bu düğümle silicek düğüm
     yer değiştirilir böylece ağacın yapısı bozulmamış olur.
    """
    # verilen düğümden verilen değeri içeren düğümü silen ve silinmiş halini döndüren method
    def DeleteValue(node, value):

        #eğer düğümde silinecek değer kalmamışsa 
        if node is None:
            return node

        if value < node.data:
            node.left =Node.DeleteValue(node.left, value)

        elif value > node.data:
            node.right = Node.DeleteValue(node.right, value)

        #silinecek değer düğümdeki değere eşit olduğu zaman
        else:
            #sol tarafı boşsa yani tek düğümlü ise kendisin değeri ile 
            #sol tarafın değerini değiştirip sol tarafı siler 
            if node.left is None:
                temp = node.right
                node = None
                return temp
            #sağ tarafı boşsa yani tek düğümlü ise kendisin değeri ile 
            #sağ tarafın değerini değiştirip sol tarafı siler 
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            #çocuklarından en küçük düğümü bulum kendisi ile değiştirecek.
            temp = Node.findMinvalueData(node.left)
            node.data = temp.data
            node.left = Node.DeleteValue(node.left, temp.data)
            
        return node


"""         Method 2    """
# bu fonksiyon verilen ağaçta en derindeki ve sağ düğümü öncelikli siler. 
# burada silinecek node verilen en derin node tur.
def delete_deep_node(root,silinecek_node): 
    que = [] 
    que.append(root) 
    while(len(que)):        # queue me ekleyerek ağaçta dolanıyorum 
        temp = que.pop(0) 
        if temp is silinecek_node: 
            temp = None
            return
        if temp.right: 
            if temp.right is silinecek_node: 
                temp.right = None
                return
            else: 
                que.append(temp.right) 
        if temp.left: 
            if temp.left is silinecek_node: 
                temp.left = None
                return
            else: 
                que.append(temp.left) 
   
# burada en derindeki   
def deleteKey(root, key): 
    if root == None : 
        return None
    if root.left == None and root.right == None: 
        if root.key == key :  
            return None
        else : 
            return root 
    key_node = None
    que = [] 
    que.append(root) 
    while(len(que)): 
        temp = que.pop(0) 
        #silinecek değeri bulana kadar ağçta geziniyoruz
        #sürekli queue mize önce sol sonra sağ düğümleri atıyoruz böylece en üste sağ öncelikli duruyor
        if temp.data == key: 
            key_node = temp 
        if temp.left: 
            que.append(temp.left) 
        if temp.right: 
            que.append(temp.right) 
    #silinecek değeri tutan node bulunduysa temp yani sağdaki en derin düğümle yer değiştir
    if key_node :  
        x = temp.data 
        delete_deep_node(root,temp) # en derin nodu sil
        key_node.data = x 
    return root 

def test1():
# Use the insert method to add nodes
    print("test 1")
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(18)
    root.insert(10)
    root.insert(19)
    root.insert(13)
    root.insert(20)
    root.insert(7)
    root.insert(11)

    root.PrintTree()
    print()
    root = Node.DeleteValue(root, 10)
    
##    root = Node.DeleteValue(root, 19)
##
    root.PrintTree()
    return root

def test2():
    print("\ntest 2")
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(18)
    root.insert(10)
    root.insert(19)
    root.insert(13)
    root.insert(20)
    root.insert(7)
    root.insert(11)

    root.PrintTree()
    print()

    root = deleteKey (root, 6)
    root = deleteKey (root, 14)

    root.PrintTree()
    return root


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


if __name__ == "__main__":
    root= test1() #1. methodu dene
    test2() #2. methodu dene