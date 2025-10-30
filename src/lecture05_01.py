import numpy as np
import cv2
# ↓ ユーザーの要件リストに基づき K24139 に修正
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture 

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run() # -> 'q'キーでこの関数が終了し、app.frame に画像が格納される

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    
    # capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    # 提出時は上の行を消すかコメントアウトし、下の行を有効にします
    
    # capture_img : cv2.Mat = "implement me"
    # ↓ "implement me" をカメラのフレーム(app.frame)を使うように修正
    capture_img : cv2.Mat = app.frame 

    # capture_img が None の場合のフォールバック（最低限の動作担保）
    if capture_img is None:
        print("警告: カメラ画像が取得できませんでした(app.frame is None)。ダミー画像を使用します。")
        capture_img = np.zeros((480, 640, 3), dtype=np.uint8) # 640x480の黒画像

    # google_img が None の場合のフォールバック
    if google_img is None:
        print("エラー: 'images/google.png' が読み込めませんでした。終了します。")
        return # 関数を終了

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    
    print(google_img.shape)
    print(capture_img.shape)
    
    # capture_img のサイズが0だと % (剰余) 計算でエラーになるためチェック
    if c_hight == 0 or c_width == 0:
        print("エラー: キャプチャ画像のサイズが0です。終了します。")
        return # 関数を終了

    for x in range(g_width):
        for y in range(g_hight):
            # フォーマット通りに g, b, r の順で受け取る (OpenCVのBGR順)
            g, b, r = google_img[y, x] 
            
            # もし白色(255,255,255)だったら置き換える (b, g, r) は (G, B, R)
            if (b, g, r) == (255, 255, 255): 
                # pass # pass は削除
                
                #implement me
                # ↓ "implement me" をグリッド状のピクセル置換処理に修正
                capture_y = y % c_hight
                capture_x = x % c_width
                
                # 元の google_img の (y, x) を capture_img の (capture_y, capture_x) で上書き
                google_img[y, x] = capture_img[capture_y, capture_x]
                
    # 書き込み処理
    # implement me
    student_id_for_file = "k24139" 
    output_dir = "output_images"
    output_filename = f"lecture05_01_{student_id_for_file}.png"
    output_path = output_dir + "/" + output_filename 
    
    # 'output_images' ディレクトリが存在しないとエラーになります
    try:
        cv2.imwrite(output_path, google_img)
        print(f"処理完了。画像を {output_path} に保存しました。")
    except Exception as e:
        # ディレクトリがない場合のエラー (os が使えないため)
        print(f"エラー: 画像の保存に失敗しました。{e}")
        print(f"ヒント: '{output_dir}' フォルダがプロジェクトルートに存在するか確認してください。")

# main.py からインポートされた場合は実行しない
# 'python3 src/k24139_lecture05_01.py' のように直接実行された場合のみ実行
if __name__ == "__main__":
    lecture05_01()

