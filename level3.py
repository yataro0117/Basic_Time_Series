import os
import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

# 3次元ベクトルの時系列を読み込み（長さは可変）
def load_dat(filepath):
    try:
        data = np.loadtxt(filepath)
        if data.ndim != 2 or data.shape[1] != 3:
            raise ValueError(f"形式が (T, 3) ではありません: {filepath}, shape={data.shape}")
        return [vec for vec in data]  # 各行 = 1時点の3次元ベクトル
    except Exception as e:
        print(f"読み込み失敗: {filepath}")
        raise e

# DTWによる分類
def classify(test_series, ref1, ref2):
    dist1, _ = fastdtw(test_series, ref1, dist=euclidean)
    dist2, _ = fastdtw(test_series, ref2, dist=euclidean)
    return 1 if dist1 < dist2 else 2

# test データをすべて分類
def classify_all(level_path):
    ref1 = load_dat(os.path.join(level_path, "reference", "1.dat"))
    ref2 = load_dat(os.path.join(level_path, "reference", "2.dat"))
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
    level_path = "dataset/level3"
    results = classify_all(level_path)
    print("▼ level3 の分類結果 ▼")
    for fname, pred in results:
        print(f"{fname} → class {pred}")
