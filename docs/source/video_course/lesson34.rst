.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 34 : MicropythonでHSVをRGBに変換する
=============================================================================

このチュートリアルでは、HSV（色相、彩度、明度）カラー値をRGB（赤、緑、青）値に変換し、Raspberry Pi Pico Wを使用してRGB LEDに表示する方法を説明します。

* **HSVカラーホイールの紹介**:
 - HSVカラーホイールの説明と、滑らかな色の移行を表現する際の重要性について。
 - HSVカラーホイールを使用して温度データを視覚的に表現する方法の概要。
* **プロジェクトのセットアップと目標**:
 - 天気ステーションプロジェクトの復習（天気データを取得してOLEDスクリーンに表示）。
 - RGB LEDを使用して温度の視覚的表現を追加するという目標の紹介。
* **HSVからRGBへの変換の理解**:
 - HSVカラーホイールを数学的に表現して変換する方法の説明。
 - カラーホイールの6つのゾーンとそれぞれのRGB値および傾斜の説明。
* **アルゴリズムの開発**:
 - HSV角度をRGB値に変換する関数のステップバイステップの作成。
 - Raspberry Pi Pico WでPWM制御を使用してRGB LED回路を設定する方法の説明。
* **コードの実装**:
 - RGB LEDのPWMを設定し、HSVからRGBへの変換を行うPythonコードの詳細な解説。
 - 変換を簡素化するためのライブラリ関数の作成。
* **実践デモンストレーション**:
 - 実際にコードを動かし、HSVカラーホイールに従って色が変わるRGB LEDを表示。
 - RGB LEDを天気ステーションプロジェクトと統合し、温度データを視覚的に表示する課題の提示。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/gg_hYPiCn_U?si=V32plkV0jGdV-4qV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

