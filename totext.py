import sys
import time
import cv2 as cv

table = '@w$#*%842+!/=c-;.      '  # 填充字符


def img_txt(img):
    w, h = img.shape[:2][::-1]
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    f = open("out.txt", 'a+')
    line = ''

    for i in range(1, h, 2):  
        for j in range(w):
            index = int((float(img_gray[i, j]) / 256.0) * len(table))
            line += table[index]  
        line += "\n" 

    line += "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print(line)
    f.write(line)
    f.close()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("请输入视频文件名")
        exit()
    cap = cv.VideoCapture(str(sys.argv[1]))
    ret = True
    num = 0
    run_t = 0

    while cap.isOpened() & ret:
        ret, frame = cap.read()
        if ret:
            num = num + 1
            cv.imshow('frame', frame)
            frame = cv.resize(frame, (50, 50))
            img_txt(frame)

        cv.waitKey(30)
