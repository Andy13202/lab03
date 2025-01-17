import cv2

def main():
    # 加载图像
    image = cv2.imread("请输入图像路径: ")
    if image is None:
        print("图像加载失败，请检查路径。")
        return
    
    # 使用OpenCV显示原始图像
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)  # 等待用户按键

    # 定义不同的压缩质量
    quality_levels = [90, 50, 10]
    for quality in quality_levels:
        # 压缩并保存图像为JPEG
        compressed_image_path = f"compressed_image_{quality}.jpg"
        cv2.imwrite(compressed_image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        
        # 读取并使用OpenCV显示压缩后的图像
        compressed_image = cv2.imread(compressed_image_path)
        cv2.imshow(f"Compressed Image - Quality {quality}", compressed_image)
        cv2.waitKey(0)  # 等待用户按键
    
    cv2.destroyAllWindows()  # 关闭所有窗口

if __name__ == "__main__":
    main()