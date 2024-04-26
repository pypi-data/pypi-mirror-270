import io
import json
import os.path
import sys
import threading
from typing import Union

from PIL import Image as pilImage
from airscript.screen import Screen
from airscript.screen import FindColors2 as asFindColors
from airscript.screen import FindImages as asFindImages
from airscript.screen import GetColorNum as asGetColorNum
from airscript.screen import yolo_v5 as asyolov5
from airscript.screen import Ocr as asOcr
from airscript.screen import CompareColors as asCompareColors
from airscript.screen import QRcode as asQRcode
from airscript.screen import TessOcr
from airscript.screen import ASColor
from ascript.android.system import R
from ascript.android.screen import ascv
import aircv
from aircv.isource import Isource
import numpy as np
import cv2
from java import jarray, jint

from .gp import GPTask, Result

IMG_ANDROID_BITMAP = 1
IMG_PYTHON_IMAGE = 2

MODE_FIND = 1
MODE_FIND_ALL = 2
MODE_FIND_SIFT = 3
MODE_FIND_SIFT_ALL = 4
MODE_FIND_TEMPLATE = 5
MODE_FIND_TEMPLATE_ALL = 6


def cache(is_cache: bool = False):
    Screen.cache(is_cache)


def capture(x: int = None, y: int = None, x1: int = None, y1: int = None):
    img = None
    if x is None:
        img = Screen.bitmap()
    else:
        img = Screen.bitmap(x, y, x1, y1)

    return img


def bitmap_to_file(path: str, bitmap=None, quality=100):
    if bitmap is None:
        bitmap = capture()
    Screen.toFile(path, bitmap, quality)


def file_to_bitmap(path: str, sampleSize: int = 1):
    return Screen.file2Bitmap(path, sampleSize)


def bitmap_base64(bitmap=None):
    if bitmap is None:
        bitmap = capture()
    return Screen.base64(bitmap)


def bitmap_maxside(bitmap=None, max_side_len=9999):
    if bitmap is None:
        bitmap = capture()
    return Screen.maxside(bitmap, max_side_len)


def bitmap_to_pilimage(bitmap=None):
    if bitmap is None:
        bitmap = capture()
    cv_img = bitmap_to_cvimage(bitmap)
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    # 将NumPy数组转换为Pillow图像对象
    pil_image = pilImage.fromarray(rgb_image)
    return pil_image


def bitmap_to_cvimage(bitmap=None):
    if bitmap is None:
        bitmap = Screen.bitmap()
    height = bitmap.getHeight()
    width = bitmap.getWidth()
    pixs = jarray(jint)(width * height)
    bitmap.getPixels(pixs, 0, bitmap.getWidth(), 0, 0, width, height)
    argb_values = np.reshape(pixs, (len(pixs), 1))
    # a = (argb_values >> 24) & 0xFF
    red = (argb_values >> 16) & 0xFF  # 取最高8位作为红色通道
    green = (argb_values >> 8) & 0xFF  # 取接下来的8位作为绿色通道
    blue = (argb_values >> 0) & 0xFF  # 取再接下来的8位作为蓝色通道
    bgr_values = np.concatenate((blue, green, red), axis=1)
    # 将二维数组重塑为三维数组，其中第三维是通道数
    bgr_image = np.reshape(bgr_values, (height, width, 3))
    bgr_image = bgr_image.astype(np.uint8)
    return bgr_image

    return bgr_image


def cvimage_to_bitmap(cvimg):
    cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
    pil_image = pilImage.fromarray(cvimg)
    # cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGBA)
    # argb_image = cvimg[:, :, [2, 1, 0, 3]]
    # pil_image = pilImage.fromarray(argb_image)

    with io.BytesIO() as output:
        pil_image.save(output, format='PNG')  # 或者使用'PNG'
        byte_array = output.getvalue()

    bitmap = Screen.toBitmap(byte_array)
    return bitmap


def get_color_num(colors: str, rect: list = None, sim: float = 0.9):
    getcnum = asGetColorNum(colors)
    if rect:
        getcnum.rect(rect[0], rect[1], rect[2], rect[3])
    getcnum.sim(sim)
    return getcnum.find()


class FindColors(GPTask):
    name = "多点找色"
    ui_path = "/website/gpui/find_colors/"

    def __init__(self, colors: str, rect: list = None, space: int = 5, ori: int = 2, diff: float = 0.98,
                 p_max_num: int = 999999):
        self.colors = colors
        self.rect = rect
        self.space = space
        self.ori = ori
        self.diff = diff
        self.p_max_num = p_max_num

    def run(self, cv_image: np.ndarray, offset_x: int = 0, offset_y: int = 0, data=None) -> Result:
        bitmap_image = cvimage_to_bitmap(cv_image)
        # from ascript.android.ui import ImageWindow
        # ImageWindow.show(bitmap_image)
        data = FindColors.find_all(self.colors, self.rect, self.space, self.ori, self.diff, bitmap_image,
                                   self.p_max_num)
        py_data = []
        for p in data:
            py_data.append({
                "x": p.x,
                "y": p.y
            })

        return Result(cv_image, offset_x, offset_y, py_data)

    @staticmethod
    def find(colors: str, rect: list = None, space: int = 5, ori: int = 2, diff: float = 0.98, image=None):
        findc = asFindColors(colors)
        if rect:
            findc.rect(rect[0], rect[1], rect[2], rect[3])

        if image:
            findc.bitmap(image)

        findc.space(space)
        findc.ori(ori)
        hex_diff = str(hex(round((1 - diff) * 255))[2:]).zfill(2)
        findc.diff("#" + hex_diff + hex_diff + hex_diff)
        return findc.find()

    @staticmethod
    def find_all(colors: str, rect: list = None, space: int = 5, ori: int = 2, diff: float = 0.98, image=None,
                 p_max_num: int = 999999):
        findc = asFindColors(colors)
        if rect:
            findc.rect(rect[0], rect[1], rect[2], rect[3])

        if image:
            findc.bitmap(image)

        findc.space(space)
        findc.ori(ori)
        hex_diff = str(hex(round((1 - diff) * 255))[2:]).zfill(2)
        # print(hex_diff)
        findc.diff("#" + hex_diff + hex_diff + hex_diff)
        return findc.find_all(p_max_num)


class FindImages(GPTask):
    name = "找图"
    ui_path = "/website/gpui/find_images/"

    def __init__(self, part_img: Union[str, list], rect: list = None, confidence: float = 0.5, rgb: bool = False,
                 maxcnt: int = 0):
        self.part_img = part_img
        self.rect = rect
        self.confidence = confidence
        self.rgb = rgb
        self.maxcnt = maxcnt

    def run(self, cv_image: np.ndarray, offset_x: int = 0, offset_y: int = 0, data=None) -> Result:

        dims = len(cv_image.shape)
        if dims == 2:
            # 图像是单通道的（可能是灰度或二值）
            channels = 1
        elif dims == 3:
            # 图像是多通道的（可能是BGR等）
            channels = cv_image.shape[2]

        if channels == 1:
            # 图像是单通道的，可能是二值图像或灰度图像
            # 检查像素值范围来区分二值图像和灰度图像
            # if np.all(cv_image >= 0) and np.all(cv_image <= 1):
            #     # 这是二值图像，像素值在0和1之间
            #     # 将其转换为8位无符号整数（0-255）的灰度图像
            #     image = (cv_image * 255).astype('uint8')
            #     # 不论是二值图像还是灰度图像，都转换为RGB图像
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_GRAY2BGR)
        elif channels == 3:
            # 图像已经是RGB图像，无需转换
            pass

        #先进行裁剪,因为 bitmap转换cvimg效率慢
        if self.rect:
            x, y, r, b = self.rect
            # print(x,y,r,b)
            cv_image = cv_image[y:b, x:r]

        py_data = FindImages.find_all_template(self.part_img, self.rect, self.confidence, self.rgb, source_img=cv_image,
                                               maxcnt=self.maxcnt)
        return Result(cv_image, offset_x, offset_y, py_data)

    @staticmethod
    def __makedao(part_img: str, rect: list = None, confidence: int = 0.1):
        if not os.path.exists(part_img):
            part_img = R.img(part_img)
            if not os.path.exists(part_img):
                raise Exception(f"找不到图片文件:{part_img}")

        findi = asFindImages(part_img)

        if rect:
            findi.rect(rect[0], rect[1], rect[2], rect[3])

        findi.confidence(confidence)
        return findi

    @staticmethod
    def search_image(image_path: str):
        if not os.path.exists(image_path):
            image_path = R.img(image_path)
            if not os.path.exists(image_path):
                raise Exception(f"找不到图片文件:{image_path}")

        return image_path

    @staticmethod
    def _get_image_source(rect: list = None):
        # print("2-1")
        if rect:
            source_img = capture(rect[0], rect[1], rect[2], rect[3])
        else:
            source_img = capture()
        # print("2-2")
        source_img = bitmap_to_cvimage(source_img)
        # print("2-3")
        return source_img

    @staticmethod
    def find(part_img: str, rect: list = None, confidence: float = 0.1, rgb: bool = False):
        res = FindImages.find_template(part_img, rect, confidence)
        if res is None:
            return FindImages.find_sift(part_img, rect, confidence)
        return res

    @staticmethod
    def find_all(part_img: str, rect: list = None, confidence: float = 0.1, rgb: bool = False):
        res = FindImages.find_all_template(part_img, rect, confidence)
        if res is None:
            return FindImages.find_all_sift(part_img, rect, confidence)
        return res

    @staticmethod
    def find_sift(part_img: str, rect: list = None, confidence: float = 0.1, min_match_count=4, rgb: bool = False):
        try:
            image_search = aircv.imread(part_img)
            offx = 0
            offy = 0
            if rect:
                offx = rect[0]
                offy = rect[1]

            dao = Isource(FindImages._get_image_source(rect), offx, offy)
            res = dao.find_sift(image_search, min_match_count, confidence)
            return res
        except Exception as e:
            return None

    @staticmethod
    def find_all_sift(part_img: str, rect: list = None, confidence: float = 0.1, min_match_count=4, maxcnt=0,
                      rgb: bool = False):

        try:
            image_search = aircv.imread(part_img)
            offx = 0
            offy = 0
            if rect:
                offx = rect[0]
                offy = rect[1]

            dao = Isource(FindImages._get_image_source(rect), offx, offy)
            res = dao.find_all_sift(image_search, min_match_count, maxcnt, confidence)
            return res
        except Exception as e:
            return None

    @staticmethod
    def find_template(part_img: Union[str, list], rect: list = None, confidence: float = 0.5, rgb: bool = False,
                      source_img=None):

        res = FindImages.find_all_template(part_img, rect=rect, confidence=confidence, rgb=rgb, maxcnt=1,
                                     source_img=source_img)
        if res and len(res)>0:
            return res[0]
        return None

    @staticmethod
    def find_all_template(part_img: Union[str, list], rect: list = None, confidence: float = 0.5, rgb: bool = False,
                          maxcnt: int = 0, source_img=None):

        # print("1")
        if source_img is None:
            # source_img = bitmap_to_cvimage()
            source_img = FindImages._get_image_source(rect)
            # print(source_img)

        return ascv.find_all_template(source_img, part_img, rect=rect, threshold=confidence, rgb=rgb, maxcnt=maxcnt)
        # offx = 0
        # offy = 0
        # if rect:
        #     offx = rect[0]
        #     offy = rect[1]
        #     if source_img is not None:
        #         width = rect[2]-rect[0]
        #         height = rect[3]-rect[1]
        #         x = offx
        #         y = offy
        #         source_img = source_img[y:y+height, x:x+width]
        #
        # if source_img is None:
        #     source_img = FindImages._get_image_source(rect)
        # res = []
        #
        # if isinstance(part_img,list):
        #     for s_img in part_img:
        #         dao = Isource(source_img, offx, offy)
        #         image_search = aircv.imread(FindImages.search_image(s_img))
        #         res =  res + dao.find_all_template(image_search, confidence, rgb=rgb)
        # else:
        #     dao = Isource(source_img, offx, offy)
        #     image_search = aircv.imread(FindImages.search_image(part_img))
        #     res = dao.find_all_template(image_search, confidence, rgb=rgb)
        #
        # part_img = None
        # source_img = None
        #
        # return res


class YoLov5:

    def __init__(self, model_name: str = None, path: str = None):
        super().__init__()
        if model_name:
            self.yolo = asyolov5(model_name)
        elif path:
            self.yolo = asyolov5(path)

    def find_all(self, rect=None):
        if rect:
            return self.yolo.find_all(rect[0], rect[1], rect[2], rect[3])
        return self.yolo.find_all()


class Ocr:
    Tess_ENG = "eng"
    Tess_CHI = "chi"
    Tess_NUM = "num"
    RIL_AUTO = -1
    RIL_BLOCK = 0
    RIL_PARA = 1
    RIL_TEXTLINE = 2
    RIL_WORD = 3
    RIL_SYMBOL = 4
    lock = threading.Lock()

    @staticmethod
    def paddleocr_v2(
            rect: list = None,
            pattern: str = None,
            confidence: int = 0.1,
            max_side_len: int = 1200,
            precision: int = 16,
            bitmap=None,
            file: str = None):
        with Ocr.lock:
            ocr = asOcr()
            ocr.mode(2)

            if rect:
                ocr.rect(rect[0], rect[1], rect[2], rect[3])

            if pattern:
                ocr.pattern(pattern)

            ocr.confidence(confidence)
            ocr.max_side_len(max_side_len)
            ocr.precision(precision)
            if bitmap:
                ocr.bitmap(bitmap)

            if file:
                ocr.file(file)

            return ocr.find_all()

    @staticmethod
    def paddleocr_v3(rect: list = None, pattern: str = None, confidence: int = 0.5, max_side_len: int = 1200,
                     precision: int = 16, bitmap=None,
                     file: str = None):
        with Ocr.lock:
            ocr = asOcr()
            ocr.mode(3)
            if rect:
                ocr.rect(rect[0], rect[1], rect[2], rect[3])
            if pattern:
                ocr.pattern(pattern)

            ocr.confidence(confidence)
            ocr.max_side_len(max_side_len)
            ocr.precision(precision)
            if bitmap:
                ocr.bitmap(bitmap)

            if file:
                ocr.file(file)

            return ocr.find_all()

    @staticmethod
    def tess(data_file=Tess_CHI, rect: list = None, pattern: str = None, split_level=RIL_AUTO, white_list: str = None,
             black_list: str = None):
        tess_core = TessOcr.getInstance(data_file)
        tess_core.split(split_level)
        if rect:
            tess_core.rect(rect)

        if white_list:
            tess_core.writeList(white_list)

        if black_list:
            tess_core.blackList(black_list)

        if pattern:
            tess_core.pattern(pattern)

        return tess_core.find()


class CompareColors:
    @staticmethod
    def compare(colors: str, diff: float = 0.9):
        compare = asCompareColors(colors)
        hex_diff = str(hex(int((1 - diff) * 255))[2:]).zfill(2)
        compare.diff("#" + hex_diff + hex_diff + hex_diff)
        return compare.compare()

    @staticmethod
    def compare_until(colors: str, diff: float = 0.9):
        compare = asCompareColors(colors)
        hex_diff = str(hex(int((1 - diff) * 255))[2:]).zfill(2)
        compare.diff("#" + hex_diff + hex_diff + hex_diff)
        compare.until()
        return compare.compare()


class QrCode:
    @staticmethod
    def find(rect: list = None, file: str = None, bitmap=None):
        qr = asQRcode()
        if rect:
            qr.rect(rect[0], rect[1], rect[2], rect[3])
        if file:
            qr.file(file)

        if bitmap:
            qr.bitmap(bitmap)

        return qr.find()


class Color:
    def __init__(self, bitmap_color: int):
        self.color = bitmap_color
        self.r = ASColor.r(bitmap_color)
        self.g = ASColor.g(bitmap_color)
        self.b = ASColor.b(bitmap_color)
        self.a = ASColor.a(bitmap_color)
        self.rgb = "#{:02x}{:02x}{:02x}".format(self.r, self.g, self.b)
        self.argb = "#{:02x}{:02x}{:02x}{:02x}".format(self.a, self.r, self.g, self.b)

    def __str__(self):
        c_dict = {
            "r": self.r,
            "g": self.g,
            "b": self.b,
            "rgb": self.rgb,
            "argb": self.argb
        }
        return json.dumps(c_dict)


def get_color(x: int, y: int, bitmap=None):
    if bitmap is None:
        bitmap = capture()
    x = int(x)
    y = int(y)
    a_color = bitmap.getPixel(x, y)
    return Color(a_color)


def get_colors(bitmap):
    if bitmap is None:
        bitmap = capture()
    return ASColor.getPixs(bitmap)


class Eraser(GPTask):
    name = "橡皮擦"
    ui_path = "/website/gpui/eraser/"

    def __init__(self, rect: list, color: str = None):
        self.rect = rect
        if color:
            self.color = (Eraser.rgba_to_tuple(color))
        else:
            self.color = (255,255,255)

    @staticmethod
    def rgba_to_tuple(rgba_str):
        if rgba_str[0] != "#":
            raise ValueError("RGBA string should start with '#'")

        # 去除开头的 '#'
        rgba_str = rgba_str[1:]

        # 检查字符串长度是否为7（包括透明度）或4（不包括透明度）
        if len(rgba_str) not in [7, 4]:
            raise ValueError("Invalid RGBA string length")

        # 将RGBA字符串拆分为R, G, B, 和 A 部分
        if len(rgba_str) == 7:
            r, g, b, a = rgba_str[:2], rgba_str[2:4], rgba_str[4:6], rgba_str[6:]
        else:
            r, g, b = rgba_str[:2], rgba_str[2:4], rgba_str[4:]
            a = "FF"  # 默认完全不透明

        # 将十六进制字符串转换为整数，然后除以255以获取0-1范围内的值
        r, g, b, a = (int(c, 16) / 255.0 for c in [r, g, b, a])

        # 返回包含RGBA值的元组
        return b, g, r

    @staticmethod
    def wipe(rect: list, img_file: str = None, cv_img=None, new_color: str = None):
        if cv_img is not None:
            pass
        elif img_file:
            cv_img = cv2.imread(img_file)
        else:
            pass

        if new_color is None:
            new_color = (255, 255, 255)

        height, width, channels = cv_img.shape

        left = max(0, rect[0])
        top = max(0, rect[1])
        right = min(width - 1, rect[2])
        bottom = min(height - 1, rect[3])

        # 遍历指定区域内的每个像素，并将其设置为新的颜色
        for y in range(top, bottom + 1):
            for x in range(left, right + 1):
                cv_img[y, x] = new_color

        if img_file:
            cv2.imwrite(img_file, cv_img)

        return cv_img

    def run(self, cv_image: np.ndarray, offset_x: int = 0, offset_y: int = 0, data=None) -> Result:
        cv_image = Eraser.wipe(self.rect, cv_img=cv_image, new_color=self.color)
        return Result(cv_image, offset_x, offset_y, data)
