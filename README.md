# 時系列識別

時系列（時間とともに変化する波形）の識別をする。

## データ
level1~level4の4種類のデータ。
各levelにはreferenceとtestの2種類フォルダがある。
reference:基準データとして異なる二種類のデータが入ってる。(クラス１、クラス２）
test:ランダムな順番でクラス1かクラス2どちらかに属するデータが入ってる。

referenceフォルダ内の波形を基準にtestフォルダ内の各波形との距離をDPで計算し、testフォルダ内の各データファイルがどちらのクラスか当てるゲーム。

## デモ（Optional）

[脳波のクラス分類(level4)]![Screenshot from 2025-05-22 14-35-37](https://github.com/user-attachments/assets/9c1ea79a-67f9-4cb2-8f6b-9ecd177a5488)



