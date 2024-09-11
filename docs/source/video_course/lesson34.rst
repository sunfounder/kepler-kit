.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 34: MicroPythonでHSVをRGBに変換する
=============================================================================
このチュートリアルでは、HSV（色相、彩度、明度）カラー値をRGB（赤、緑、青）に変換し、Raspberry Pi Pico Wを使用してRGB LEDに表示する方法を説明します。

* **HSVカラーホイールの紹介**: HSVカラーホイールの概要と、特に温度データの視覚化における滑らかな色の変化に役立つことを説明します。
* **プロジェクトのセットアップと目標**: 天気ステーションプロジェクトの復習と、温度を表現するRGB LEDカラーの追加目標を説明します。
* **HSVからRGBへの変換の理解**: HSVカラーホイールの数学的な表現、ゾーン、そしてRGBへの変換方法を解説します。
* **アルゴリズムの開発**: HSVをRGBに変換する関数を作成し、PWMを使用してRGB LEDを設定します。
* **コードの実装**: PWM制御とHSVからRGBへの変換のPythonコードを解説し、ライブラリ関数を含めます。
* **実践的なデモンストレーション**: HSVに基づくRGB LEDの色変化を示し、LEDを天気ステーションプロジェクトに統合する課題を提示します。



**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/gg_hYPiCn_U?si=V32plkV0jGdV-4qV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
