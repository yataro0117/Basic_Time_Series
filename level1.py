import os
import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

# ファイル読み込み
def load_dat(filepath):
    try:
        data = np.loadtxt(filepath)

        # 万全を期して完全に 1 次元にする
        if data.ndim == 0:
            data = np.array([data])         # スカラーを1要素の配列に
        elif data.ndim == 2:
            data = data[:, 0]               # 2次元 → 1列目だけ取り出す
        elif data.ndim > 2:
            raise ValueError(f"データが多次元すぎます: {filepath}")
        return data.flatten()               # 念のためflattenで1次元化
    except Exception as e:
        print(f"読み込み失敗: {filepath}")
        raise e



# DTWによる分類
def to_sequence(x):
    return [(v,) for v in x]

def classify(test_series, ref1, ref2):
    test_seq = to_sequence(test_series)
    ref1_seq = to_sequence(ref1)
    ref2_seq = to_sequence(ref2)

    dist1, _ = fastdtw(test_seq, ref1_seq, dist=euclidean)
    dist2, _ = fastdtw(test_seq, ref2_seq, dist=euclidean)
    return 1 if dist1 < dist2 else 2


# ディレクトリ内の全テストデータを分類
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
    level_path = "dataset/level1"
    results = classify_all(level_path)
    print("▼ level1 の分類結果 ▼")
    for fname, pred in results:
        print(f"{fname} → class {pred}")

