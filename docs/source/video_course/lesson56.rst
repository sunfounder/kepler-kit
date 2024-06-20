.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 56 : MicroPythonでジョイスティックを使用する
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wでジョイスティックを使用する方法について説明します。

* **配線設定**:
   - グラウンド、3.3V、VRXをGPIOピン27に、VRYをGPIOピン26に接続します。
* **コードの実装**:
   - 必要なライブラリ（`machine`、`time`、`math`）をインポートします。
   - ジョイスティック軸のADCを設定します。
   - ジョイスティックの値を読み取り、範囲と動作を理解するためにプリントします。
* **キャリブレーション**:
   - 読み取り値を調整し、直感的に理解しやすいように-100から+100のスケールに変換します。
* **宿題**:
   - 中心位置が(0,0)、端が±100と読めるようにジョイスティックをキャリブレーションするプログラムを書きます。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/0W8XSJhGux0?si=DO3JL-oMiMfbXF_e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

