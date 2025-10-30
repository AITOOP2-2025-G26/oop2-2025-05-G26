import numpy as np
import cv2
# フォーマット例に従い K21999 を使用します
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():
    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run() # キー入力(qなど)で終了し、app.frame に画像が格納される

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    
    # capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    # ↑フォーマット通りコメントアウト（または削除）
    
    # capture_img : cv2.Mat = "implement me"
    # ↓ "implement me" の部分を app.frame から取得するように実装
    capture_img : cv2.Mat = app.frame

    # app.frame が None (カメラ取得失敗) の場合、shape 取得でエラーになるのを防ぐ
    if capture_img is None:
        print("警告: カメラ画像の取得に失敗(app.frame is None)。ダミー画像(640x480)を使用します。")
        # 要件の 640x480 に合わせる
        capture_img = np.zeros((480, 640, 3), dtype=np.uint8) 

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    
    print(google_img.shape)
    print(capture_img.shape)
    
    # キャプチャ画像の高さや幅が0の場合、剰余(%)計算でエラーになるのを防ぐ
    if c_hight == 0 or c_width == 0:
        print("エラー: キャプチャ画像のサイズが0です。処理を中断します。")
        return # lecture05_01 関数を終了

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x] # BGR順で取得
            
            # もし白色(255,255,255)だったら置き換える
            # (b, g, r) の順で比較
            if (b, g, r) == (255, 255, 255):
                # pass # pass を削除
                
                #implement me
                # ↓ "implement me" の部分をグリッド状の置換処理で実装
                
                # キャプチャ画像の座標 (y % 高さ, x % 幅) を計算
                capture_y = y % c_hight
                capture_x = x % c_width
                
                # google_img の (y, x) を capture_img のピクセルで上書き
                google_img[y, x] = capture_img[capture_y, capture_x]

    # 書き込み処理
    # implement me
    # ↓ "implement me" の部分を書き込み処理で実装
    
    # フォーマット例の K21999 に合わせてファイル名を決定
    output_filename = "output_images/lecture05_01_k21999.png"
    
    try:
        # os モジュールを使わずに直接書き込み
        cv2.imwrite(output_filename, google_img)
        print(f"処理完了。画像を {output_filename} に保存しました。")
    except Exception as e:
        print(f"エラー: 画像の保存に失敗しました。{e}")
        print("ヒント: 'output_images' フォルダが存在するか確認してください。")

# フォーマット例に従い、このファイル内では lecture05_01() を呼び出しません。
# main.py など、他のスクリプトからこの関数を呼び出して実行してください。

