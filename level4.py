import os
import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

# 64次元ベクトルの時系列読み込み
def load_dat(filepath):
    try:
        data = np.loadtxt(filepath)
        if data.ndim != 2 or data.shape[1] != 64:
            raise ValueError(f"形式が (T, 64) ではありません: {filepath}, shape={data.shape}")
        return [vec for vec in data]
    except Exception as e:
        print(f"読み込み失敗: {filepath}")
        raise e

# クラス内の複数ファイルを平均して代表系列を作成
def compute_average_series(folder_path):
    all_series = []
    for fname in sorted(os.listdir(folder_path)):
        if fname.endswith(".dat"):
            path = os.path.join(folder_path, fname)
            series = np.loadtxt(path)
            all_series.append(series)
    if not all_series:
        raise ValueError(f"{folder_path} にデータがありません")
    avg_series = np.mean(np.stack(all_series), axis=0)
    return [vec for vec in avg_series]  # fastdtw用に list of vectors に変換

# DTWによる分類
def classify(test_series, ref1, ref2):
    dist1, _ = fastdtw(test_series, ref1, dist=euclidean)
    dist2, _ = fastdtw(test_series, ref2, dist=euclidean)
    return 1 if dist1 < dist2 else 2

# 全 test データを分類
def classify_all(level_path):
    ref1 = compute_average_series(os.path.join(level_path, "reference", "1"))
    ref2 = compute_average_series(os.path.join(level_path, "reference", "2"))
    test_dir = os.path.join(level_path, "test")

    results = []
    for file in sorted(os.listdir(test_dir)):
        if file.endswith(".dat"):
            test_path = os.path.join(test_dir, file)
            test_series = load_dat(test_path)
            pred = classify(test_series, ref1, ref2)
            results.append((file, pred))
    return results

# 実行
if __name__ == "__main__":
    level_path = "dataset/level4"
    results = classify_all(level_path)
    print("▼ level4 の分類結果 ▼")
    for fname, pred in results:
        print(f"{fname} → class {pred}")
