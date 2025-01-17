import cv2

def main():
    # 加載圖像
    image = cv2.imread("請輸入圖像路徑: ")
    if image is None:
        print("圖像加載失敗，請檢查路徑。")
        return
    
    # 使用OpenCV顯示原始圖像
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)  # 等待用戶按鍵

    # 定義不同的壓縮質量
    quality_levels = [90, 50, 10]
    for quality in quality_levels:
        # 壓縮並保存圖像為JPEG
        compressed_image_path = f"compressed_image_{quality}.jpg"
        cv2.imwrite(compressed_image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        
        # 讀取並使用OpenCV顯示壓縮後的圖像
        compressed_image = cv2.imread(compressed_image_path)
        cv2.imshow(f"Compressed Image - Quality {quality}", compressed_image)
        cv2.waitKey(0)  # 等待用戶按鍵
    
    cv2.destroyAllWindows()  # 關閉所有窗口

if __name__ == "__main__":
    main()