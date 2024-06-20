.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 55 : MicroPythonでNeoPixelsを使ってダイナミックレインボーを作成
=============================================================================

このチュートリアルでは、Raspberry Pi Pico WとMicroPythonを使用してNeoPixelアレイにランニングレインボーパターンを作成する方法について説明します。

* **配線設定**:
   - 5V、GND、およびデータピンをPico WのGPIOピン0に接続します。
* **コンセプトの説明**:
   - HSVカラーバリューをインクリメントし、それぞれのピクセルに適用することで、ランニングレインボーパターンを作成します。
* **コードの実装**:
   - HSVをRGBに変換する関数を使用します。
   - ネストされたループを使用してHSVカラーホイールをサイクルし、NeoPixelアレイを更新します。
* **デモとテスト**:
   - NeoPixelアレイ上にランニングレインボーパターンを表示します。
   - トラブルシューティングのヒントを提供します。
* **宿題**:
   - コードを実験して追加のパターンを作成します。
   - コミュニティと結果を共有します。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/lZYEQLorXMY?si=nj7LHGxmNnCoVfqi" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

