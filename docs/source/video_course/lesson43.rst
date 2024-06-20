.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 43 : 3軸加速度計を使用してピッチとロールを測定する方法
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してMPU6050センサーでピッチとロールの角度を測定する方法を紹介します。

* **セットアップ**:
   - 提供された回路図とコードを使用して、MPU6050をRaspberry Pi Pico Wに接続します。
* **傾斜測定のための三角法**:
   - 加速度計のデータからピッチとロールを計算するための三角関数を使用します。
* **コーディング**:
   - Pythonで計算を実装してテストし、ピッチとロールの正確な測定を確認します。
* **宿題**:
   - X、Y、Zの加速度が同時に0Gを示す位置を見つけ、その解決策を共有します。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/5f7fL9G8VsE?si=S8zbOFPDIA3dG8jt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

