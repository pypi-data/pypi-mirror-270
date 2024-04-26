import cv2
import numpy as np
from typing import Union


def find_all_sift():
    pass


def find_all_template(image_source, image_search: Union[str, list], rect: list = None, threshold=0.5, rgb=False,
                      maxcnt=0, bgremove=False):
    """模版匹配"""
    # 处理主图 颜色通道
    if not rgb:
        image_source = cv2.cvtColor(image_source, cv2.COLOR_BGR2GRAY)
    else:
        image_source = cv2.cvtColor(image_source, cv2.COLOR_BGR2HSV)
        source_h, source_s, source_v = cv2.split(image_source)
        image_hs = cv2.merge([source_h, source_s])
        # 处理主图 的范围大小
    x, y = [0, 0]
    if rect:
        # 这里只做坐标偏移
        x, y, r, b = rect

    image_search_list = []
    if isinstance(image_search, list):
        image_search_list = image_search
    else:
        image_search_list.append(image_search)
    result = []
    method = cv2.TM_CCOEFF_NORMED
    for image_search_path in image_search_list:
        if not rgb:
            image_search = cv2.imread(image_search_path, cv2.IMREAD_GRAYSCALE)
            res = cv2.matchTemplate(image_source, image_search, method)
        else:
            # 分别计算3通道的rgb值
            image_search = cv2.imread(image_search_path)
            search_hsv = cv2.cvtColor(image_search, cv2.COLOR_BGR2HSV)
            search_h, search_s, search_v = cv2.split(search_hsv)
            search_hs = cv2.merge([search_h, search_s])
            res = cv2.matchTemplate(image_hs, search_hs, cv2.TM_CCOEFF_NORMED)
            # res = resbgr[2]

        w, h = image_search.shape[1], image_search.shape[0]

        # print(res)

        while True:
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            if max_val < threshold:
                break

            # calculator middle point
            # 把 范围 x,y 偏移加进去
            top_left = [a + b for a, b in zip(max_loc, [x, y])]
            middle_point = (top_left[0] + w / 2, top_left[1] + h / 2)
            result.append(dict(
                result=middle_point,
                rectangle=(top_left, (top_left[0], top_left[1] + h), (top_left[0] + w, top_left[1]),
                           (top_left[0] + w, top_left[1] + h)),
                confidence=max_val
            ))
            if maxcnt and len(result) >= maxcnt:
                break
            # floodfill the already found area
            cv2.floodFill(res, None, max_loc, (-1000,), max_val - threshold + 0.1, 1, flags=cv2.FLOODFILL_FIXED_RANGE)
    return result


def find_all_template2(image_source, image_search: Union[str, list], rect: list = None, threshold=0.5, rgb=False,
                       maxcnt=0, bgremove=False):
    """模版匹配"""
    # 处理主图 颜色通道
    if not rgb:
        image_source = cv2.cvtColor(image_source, cv2.COLOR_BGR2GRAY)
        # 处理主图 的范围大小
    x, y = [0, 0]
    if rect:
        x, y, r, b = rect
        # print(x,y,r,b)
        # image_source = image_source[y:b, x:r]
        # image_source = image_source[y:y + h, x:x + w]

    image_search_list = []
    if isinstance(image_search, list):
        image_search_list = image_search
    else:
        image_search_list.append(image_search)
    result = []
    for image_search_path in image_search_list:
        if not rgb:
            image_search = cv2.imread(image_search_path, cv2.IMREAD_GRAYSCALE)
        else:
            # 计算模板和匹配区域的直方图
            image_search = cv2.imread(image_search_path)
            template_hist = calc_histogram(image_search)

        # 关于RGB调试
        #         s_bgr = cv2.split(im_search) # Blue Green Red
        #         i_bgr = cv2.split(im_source)
        #         weight = (0.3, 0.3, 0.4)
        #         resbgr = [0, 0, 0]
        #         for i in range(3): # bgr
        #             resbgr[i] = cv2.matchTemplate(i_bgr[i], s_bgr[i], method)
        #         res = resbgr[0]*weight[0] + resbgr[1]*weight[1] + resbgr[2]*weight[2]

        method = cv2.TM_CCOEFF_NORMED
        res = cv2.matchTemplate(image_source, image_search, method)
        w, h = image_search.shape[1], image_search.shape[0]
        # res = np.where(res >= confidence)
        while True:
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            if max_val < threshold:
                break

            if rgb:

                # 计算直方图
                # 提取匹配区域的图像
                bottom_right = (top_left[0] + w, top_left[1] + h)
                match_region = image_source[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

                # 计算模板和匹配区域的直方图
                # template_hist = calc_histogram(image_search)
                match_hist = calc_histogram(match_region)

                # 比较直方图
                hist_similarity = compare_histograms(template_hist, match_hist, cv2.HISTCMP_CORREL)

                # print(hist_similarity)

                if hist_similarity < threshold:
                    break

            # calculator middle point
            # 把 范围 x,y 偏移加进去
            top_left = [a + b for a, b in zip(max_loc, [x, y])]
            middle_point = (top_left[0] + w / 2, top_left[1] + h / 2)
            result.append(dict(
                result=middle_point,
                rectangle=(top_left, (top_left[0], top_left[1] + h), (top_left[0] + w, top_left[1]),
                           (top_left[0] + w, top_left[1] + h)),
                confidence=max_val
            ))
            if maxcnt and len(result) >= maxcnt:
                break
            # floodfill the already found area
            cv2.floodFill(res, None, max_loc, (-1000,), max_val - threshold + 0.1, 1, flags=cv2.FLOODFILL_FIXED_RANGE)
    return result


def find_all_sift(image_source, image_search: Union[str, list], rect: list = None, threshold=0.5, rgb=False,
                  maxcnt=0, ):
    if not rgb:
        image_source = cv2.cvtColor(image_source, cv2.COLOR_BGR2GRAY)
        # 处理主图 的范围大小
    x, y = [0, 0]
    if rect:
        x, y, w, h = rect
        image_source = image_source[y:y + h, x:x + w]

    image_search_list = []
    if image_search is list:
        image_search_list = image_search
    else:
        image_search_list.append(image_search)

    for image_search_path in image_search_list:
        if not rgb:
            image_search = cv2.imread(image_search_path, cv2.IMREAD_GRAYSCALE)
        else:
            image_search = cv2.imread(image_search_path)

        pass


def compare_histograms(hist1, hist2, method=cv2.HISTCMP_CORREL):
    """比较两个直方图"""
    return cv2.compareHist(hist1, hist2, method)


def calc_histogram(image, mask=None, channels=[0, 1, 2]):
    """计算图像的直方图"""
    # print(image.shape[2])
    hist = cv2.calcHist([image], channels, mask, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    return hist.flatten()
