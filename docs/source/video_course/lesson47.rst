.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 47 : ローパスフィルターを使用したセンサーデータの改善
=============================================================================

このチュートリアルでは、MPU6050センサーとRaspberry Pi Pico Wを使用して、ローパスフィルターを実装することで安定した2軸傾斜計を作成する方法を紹介します。

* **セットアップ**:
   - 提供された回路図を使用して、MPU6050をRaspberry Pi Pico Wに接続します。

* **コンセプト**:
   - MPU6050の加速度データを使用して傾きを測定し、ピッチとロールの角度を計算します。
   - 加速度を傾きとして解釈することによるエラーに対処します。

* **ローパスフィルター**:
   - ローパスフィルターを実装してデータを平滑化し、ノイズを低減します。
   - 方程式: \(\text{new value} = \text{sensor confidence} \times \text{measurement} + (1 - \text{sensor confidence}) \times \text{old value}\)
   - 応答性とノイズ低減のバランスを最適化するために、信頼値を調整します。

* **コード**:
   - MPU6050をセットアップしてX、Y、Z軸の加速度を測定します。
   - ピッチとロールの角度を計算し、フィルターを適用します。
   - フィルター処理された値を表示します。

* **宿題**:
   - ローパスフィルターを実装してテストします。
   - 異なる信頼値で実験します。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3YqGIg4crEk?si=rwiDFcJ98nlj_Sg3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

