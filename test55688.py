import cv2
import os

def main():
    # 用户输入图像文件名
    filename = input("请输入图像文件名: ")

    # 构建完整的文件路径
    base_path = os.getcwd()  # 获取当前工作目录
    image_path = os.path.join(base_path, filename)
    absolute_path = os.path.abspath(image_path)

    print("完整路径:", absolute_path)

    # 加载图像
    image = cv2.imread(absolute_path)
    if image is None:
        print("图像加载失败，请检查路径。")
        return
    
    # 使用OpenCV显示原始图像
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)  # 等待用户按键
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()