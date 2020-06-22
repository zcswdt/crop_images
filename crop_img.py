# coding=utf-8

import os
import cv2
import numpy as np
import codecs
from math import *


def dumpRotateImage(img,degree,pt1,pt2,pt3,pt4):
    # if fabs(degree) > 50:
        # return np.array([])
        
    try:
        height,width=im.shape[:2]
        print("checked for shape".format(im.shape))
    except AttributeError:
        print("shape not found")    
        
        
    #height,width=img.shape[:2]
    heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
    widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))
    matRotation=cv2.getRotationMatrix2D((width/2,height/2),degree,1)
    matRotation[0, 2] += (widthNew - width) / 2
    matRotation[1, 2] += (heightNew - height) / 2
    imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))
    pt1 = list(pt1)
    pt3 = list(pt3)
    
    [[pt1[0]], [pt1[1]]] = np.dot(matRotation, np.array([[pt1[0]], [pt1[1]], [1]]))
    [[pt3[0]], [pt3[1]]] = np.dot(matRotation, np.array([[pt3[0]], [pt3[1]], [1]]))
    imgOut=imgRotation[int(pt1[1]):int(pt3[1]),int(pt1[0]):int(pt3[0])]
    height,width=imgOut.shape[:2]
    return imgOut

#判断是否是纯英文
def is_all_eng(strs):
    import string
    for i in strs:
        if i not in string.ascii_lowercase+string.ascii_uppercase:
            return False
    return True

#判断字符串是中文还是英文,只要有一个中文就算中文
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False



# f=open('D:\\codes\\crop_img\\txt\\1.txt', mode='r', encoding='utf-8')
    # #lines = f.read()
# lines = f.readlines()
# print('lines',lines)


''' 
input_path = "/home/zhoucs/changshi/data/crop_img/input"
txt_path = "/home/zhoucs/changshi/data/crop_img/txt"
save_path = "/home/zhoucs/changshi/data/crop_img/save"
'''

input_path = "D:\\codes\\crop_img\\icdar2019\\images"
txt_path = "D:\\codes\\crop_img\\icdar2019\\gt"
save_path = "D:\\codes\\crop_img\\icdar2019\\save"
#save_txt_path=

#print('input_path',input_path)
filelist = os.listdir(input_path)
for item in filelist:
     
    img_path = os.path.join(input_path, item)
    im=cv2.imread(img_path)
    try:     
        im.shape 
    except:
        print('fail to read item')
        continue
    im_height,im_width=im.shape[:2]

    new_name = item.replace(".jpg", ".txt")
    #new_txt_path = txt_path + os.sep + new_name
    new_txt_path = os.path.join(txt_path, new_name)

    
    new_save_path = os.path.join(save_path, item)
    pre_img_fn = new_save_path.split(".")[0]
    
    # #保存图片txt
    # new_save_path = os.path.join(save_txt_path, item)
    # pre_txt_fn = new_save_path.split(".")[0]
 
    f=open(new_txt_path, mode='r', encoding='utf-8')
    #f=open('new_txt_path')
    #lines = f.read()
    lines = f.readlines()
    #print('lines',lines)
 
    #im_width = im.shape[1]
    #im_height = im.shape[0]
    
 
 
    try:
        im_height,im_width=im.shape[:2]
        print("checked for shape".format(im.shape))
    except AttributeError:
        print("shape not found")
    
 
 
    # for i,rec in enumerate(lines):
    
        # rec=[float(item) for item in rec]
        # if rec[0]<0:
            # lines[i][0] = 0
        # if rec[1]<0:
            # lines[i][1] = 0
        # if rec[6]>=im_width:
            # lines[i][6] = im_width-1
        # if rec[7]<0:
            # lines[i][7] = 0
        # if rec[4]<0:
            # lines[i][4] = 0
        # if rec[5] >=im_height:
            # lines[i][5] = im_height-1
        # if (rec[2]+5)>=im_width:
            # lines[i][2] = im_width-1
        # else:
            # lines[i][2] = rec[2] + 5
        # if rec[3]>=im_height:
            # lines[i][3] = im_height-1
 
 
 

    index=0    
    for line in lines:
        rec=line.split(',')[:8]       
        #print('rec',rec)
        
        label=line.split(',')[-1]
        print('label',label)
        
        judge_img = is_all_eng(label)
        print('judge_img',judge_img)
        
        judge_chn = is_contains_chinese(label)
        
        
        i=0
        if judge_chn==True:
        #if judge_img==False and label !='###' and label !=' ':
            
        
            rec=[float(item) for item in rec]
            print('rec1',rec)
            
                
            
            if rec[0]<0:
                rec[0] = 0
            if rec[1]<0:
                rec[1] = 0
            if rec[6]>=im_width:
                rec[6] = im_width-1
            if rec[7]<0:
                rec[7] = 0
            if rec[4]<0:
                rec[4] = 0
            if rec[5] >=im_height:
                rec[5] = im_height-1
            if (rec[2]+5)>=im_width:
                rec[2] = im_width-1
            else:
                rec[2] = rec[2] + 5
            if rec[3]>=im_height:
                rec[3] = im_height-1
            
            
            
            
            #print('int(rec[0])',int(rec[0]))
            pt1 = (rec[0],rec[1])           
            pt2 = (rec[2],rec[3])
            pt3 = (rec[4],rec[5])
            pt4 = (rec[6],rec[7])
            
            box_width = pt2[0]-pt1[0]
            box_height = pt4[1]-pt1[1]
            if  box_height <= 10 or box_height > 1.1*box_width:
                continue
            
            
            
            partImg = dumpRotateImage(im,degrees(atan2(pt2[1]-pt1[1],pt2[0]-pt1[0])),pt1,pt2,pt3,pt4)
            #print('partImg',partImg)
            
            index += 1
            img_name = pre_img_fn + "_p" + str(index) + ".jpg"
            print(img_name)
            cv2.imwrite(img_name,partImg)
            
            txt_name = pre_img_fn + "_p" + str(index) + '.txt'
            
            f=open(txt_name, mode='w', encoding='utf-8')
            
            txt_new_name = os.path.basename(img_name)
            print("txt_new_name",txt_new_name)
            f.write(txt_new_name+ ' ' + label)
            
        else:
            i+=1
            print(i)
            continue

