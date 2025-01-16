import cv2
import matplotlib.pyplot as plt

def main():
    # 使用者輸入圖像路徑
    image_path = input("請輸入圖像路徑: ")
    
    # 加載圖像
    image = cv2.imread(image_path)
    if image is None:
        print("圖像加載失敗，請檢查路徑。")
        return
    
    # 將BGR圖像轉換為RGB圖像以適用於matplotlib顯示
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 顯示原始圖像
    plt.imshow(image_rgb)
    plt.title("原始圖像")
    plt.axis('off')  # 不顯示坐標軸
    plt.show()
    
    # 保存並顯示不同壓縮質量的JPEG圖像
    quality_levels = [90, 50, 10]  # 定義不同的壓縮質量
    for quality in quality_levels:
        # 壓縮並保存圖像
        compressed_image_path = f"compressed_image_{quality}.jpg"
        cv2.imwrite(compressed_image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        
        # 讀取並顯示壓縮後的圖像
        compressed_image = cv2.imread(compressed_image_path)
        compressed_image_rgb = cv2.cvtColor(compressed_image, cv2.COLOR_BGR2RGB)
        plt.imshow(compressed_image_rgb)
        plt.title(f"壓縮圖像 - 質量 {quality}")
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    main()