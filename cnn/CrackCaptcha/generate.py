# -*- coding: utf-8 -*-
from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
from PIL import Image
import random
import cv2
import os
 
# 验证码中的字符
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
# ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
#             'V', 'W', 'X', 'Y', 'Z']
 
# 验证码长度为4个字符
def random_captcha_text(char_set=number, captcha_size=4):
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text
 
 
# 生成字符对应的验证码
def gen_captcha_text_and_image():
    image = ImageCaptcha()
 
    captcha_text = random_captcha_text()
    captcha_text = ''.join(captcha_text)
 
    captcha = image.generate(captcha_text)
 
    captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image
 
 
if __name__ == '__main__':
 
    # 训练集和测试集数量
    train_num = 10000
    valid_num = 3000
 
    #保存路径
    path_train = './trainImage'
    path_valid = './validImage'
    if not os.path.exists(path_train):
        os.mkdir(path_train)
    if not os.path.exists(path_valid):
        os.mkdir(path_valid)
 
    for i in range(train_num):
        text, image = gen_captcha_text_and_image()
        fullPath = os.path.join(path_train, text + ".jpg")
        cv2.imwrite(fullPath, image)
        print ("Creating train data: {0}/{1}".format(i,train_num))
    for i in range(valid_num):
        text, image = gen_captcha_text_and_image()
        fullPath = os.path.join(path_valid, text + ".jpg")
        cv2.imwrite(fullPath, image)
        print ("Creating valid data: {0}/{1}".format(i, valid_num))
    print ("Done!")
