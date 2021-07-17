import numpy as np
import random as rd
from dataclasses import dataclass
@dataclass
class number:
    t :  float= 3

class block:
    o = number.t
    block_array={1:[[o,0,0],[o,0,0],[o,0,0]],
                2:[[o,0,0],[o,0,0],[o,o,0]],
                3:[[0,o,0],[o,o,0],[o,0,0]],
                4:[[o,o,0],[o,o,0],[0,0,0]],
                5:[[0,o,0],[0,o,0],[o,o,0]],
                6:[[0,o,o],[o,o,0],[0,0,0]],
                7:[[o,o,0],[0,o,o],[0,0,0]]}
    def __init__(self):
        self.newblock = np.array(self.block_array[rd.randint(1,8)])

b = block()
print(b.newblock)
class tetris():
    def __init__(self):
        self.board =np.array([[0 for x in range(13)] for x in range(60)])
        self.board[len(self.board)-3:len(self.board),]=1
        self.board[:,:3]=1
        self.board[:,len(self.board[0])-3:]=1
    def input(self,tet):
        #print(tet,self.board[:3,:3])
        a = rd.randint(3,len(self.board)-5)
        self.board[:3,a:a+3] = tet.newblock
        #print(type(self.board[:3,a:a+3]))
    #def next(self):
    def draw(self):
        print(self.board)
    def find(self):
        for i in self.board:
           for j in i :
               print(type(j))
te = tetris()
te.input(b)
print()
te.draw()
#te.find()


    

