.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 35 : RGB LED温度インジケータ付きリモート気象ステーション
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用して温度データを表示する気象ステーションにRGB LEDを統合する方法を説明します。

* **プロジェクト概要**:
 - Raspberry Pi Pico W、OLEDディスプレイ、およびRGB LEDを使用して、温度を視覚的に表示するリモート気象ステーションを構築します。
* **HSVからRGBへの変換**:
 - 温度値をHSVカラーホイールを使用して色に変換します。
 - 温度を-20°F（ディープバイオレット）から120°F（赤）までカラーホイール上の対応する角度にマッピングします。
* **回路セットアップ**:
 - OLEDディスプレイとRGB LEDをRaspberry Pi Pico Wに接続します。
 - RGB LED用にGPIOピンとPWMを構成します。
* **コーディング**:
 - 温度データを取得し、色相角度を計算し、それをRGB値に変換し、RGB LEDに適用します。
 - HSVからRGBへの変換ライブラリを気象ステーションコードに統合します。
* **デモンストレーション**:
 - OLEDとRGB LEDに温度データを表示します。
 - コードを保存して実行し、バッテリ電源でポータブルな設定にします。
* **結論**:
 - 色のマッピングや温度範囲を調整してプロジェクトをカスタマイズします。
 - チュートリアルの購読、コメント、共有を奨励します。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/c9tQHyQWIYk?si=ORHsIXt8eBGeXDdp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

