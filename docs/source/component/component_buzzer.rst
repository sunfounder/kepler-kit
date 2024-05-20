.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _cpn_buzzer:

ブザー
=======

DC電源で駆動されるブザーは、一体型の電子ブザーとして、コンピュータ、プリンタ、コピー機、アラーム、電子玩具、自動車用電子機器、電話、タイマーなど、さまざまな電子製品や音声機器で広く使用されています。

ブザーは、アクティブ型とパッシブ型に分類されます（以下の画像を参照）。ブザーをピンが上を向くように回転させると、緑色の基板を持つブザーはパッシブ型で、黒いテープで覆われたものはアクティブ型です。

|img_buzzer|

アクティブ型とパッシブ型のブザーの違い：

アクティブ型ブザーは内蔵の振動源を持っているため、通電すると音を出します。一方で、パッシブ型ブザーはそのような振動源を持っていないので、DC信号を使用しても音は出ません。代わりに、2Kから5Kの周波数の矩形波を使用して駆動する必要があります。アクティブ型ブザーは、多くの内蔵振動回路があるため、パッシブ型よりも高価なことがよくあります。

以下はブザーの電気記号です。プラスとマイナスの極性を持つ2つのピンがあります。表面に+が表示されている方が陽極で、もう一方は陰極です。

|img_buzzer_symbol|

ブザーのピンを確認すると、長い方が陽極で短い方が陰極です。接続する際にそれらを混同しないでください。そうしないと、ブザーは音を出さなくなります。

`Buzzer - Wikipedia <https://en.wikipedia.org/wiki/Buzzer>`_

.. 例
.. -------------------

.. :ref:`Intruder Alarm`

.. :ref:`Custom Tone`

**例**

* :ref:`py_ac_buz` (MicroPythonユーザー向け)
* :ref:`py_pa_buz` (MicroPythonユーザー向け)
* :ref:`py_light_theremin` (MicroPythonユーザー向け)
* :ref:`py_alarm_lamp` (MicroPythonユーザー向け)
* :ref:`py_music_player` (MicroPythonユーザー向け)
* :ref:`py_fruit_piano` (MicroPythonユーザー向け)
* :ref:`py_reversing_aid` (MicroPythonユーザー向け)
* :ref:`ar_ac_buz` (Arduinoユーザー向け)
* :ref:`ar_pa_buz` (Arduinoユーザー向け)
* :ref:`per_service_bell` (Piper Makeユーザー向け)
* :ref:`per_reversing_system` (Piper Makeユーザー向け)
* :ref:`per_reaction_game` (Piper Makeユーザー向け)

