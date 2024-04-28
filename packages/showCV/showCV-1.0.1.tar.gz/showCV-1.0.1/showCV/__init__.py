import cv2


def show(name,img,function=None, param=None):
    cv2.namedWindow('{0}'.format(name),cv2.WINDOW_NORMAL)#窗口名，调节类型
    cv2.resizeWindow('{0}'.format(name), img.shape[1], img.shape[0])
    cv2.imshow('{0}'.format(name),img)
    if function:
        cv2.setMouseCallback('{0}'.format(name), function, param)
    else:
        pass
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return