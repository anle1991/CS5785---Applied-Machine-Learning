#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:08:44 2017

@author: sunran
"""

import numpy as np
from numpy import *
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg
import csv


def pairSimil(test, candidate, mode):
    """
    compute the simiarity between one query and 2000 candidates
    base on different mode, we use different way to compute the similarity
    0: cosin
    1: euclidean 
    """
    res = []
    if(mode == 0):
        # use cosin distance
        for n in candidate:
            cos = dot(test,n)/(linalg.norm(test)*linalg.norm(n))
            res.append(cos)
        
    elif(mode == 1):
        # use euclidean distance
        for n in candidate:
            dist = np.linalg.norm(test - n)
            res.append(dist)
    
    res = np.array(res)    
    return res
    

def visualize(index):
    for n in index:
        s = str(n)+".jpg"
        print (s)
        pic = mpimg.imread('lena.png') 
        plt.imshow(pic)
        plt.axis('off')
        plt.show()

def createcsvfile():
    with open('egg.csv','w+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile,delimiter =',')
        spamwriter.writerow(["shbjh"])
    

    
if __name__  == "__main__":
    #test = [[2,5],[3,2],[6,2],[4,4]]
    test = [[3,2]]
    candidate = [[1,1],[1,3],[1,4],[1,5],[2,1],[4,1],[5,1]]
    test = np.array(test)
    candidate = np.array(candidate)
  
    similarity = pairSimil(test, candidate, 1)
    print (similarity.shape)
    print (similarity)
    
    similarity = pairSimil(test, candidate, 0)
    print (similarity.shape)
    print (similarity)

    index = [1,2,3,4]
    index = np.array(index)
    visualize(index)
    
    createcsvfile()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    