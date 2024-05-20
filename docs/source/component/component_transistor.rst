.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _cpn_transistor:

トランジスタ
============

|img_NPN&PNP|

トランジスタは電流によって電流を制御する半導体デバイスです。弱い信号を大きな振幅の信号に増幅する機能を持ち、非接触スイッチとしても使用されます。

トランジスタはP型とN型の半導体で構成された3層の構造です。これにより内部には3つの領域が形成されます。中央の薄い部分がベース領域であり、他の2つはいずれもN型かP型です。多数キャリアが豊富な小さい領域がエミッタ領域であり、もう一方がコレクタ領域です。この構造によって、トランジスタは増幅器として機能します。
これら3つの領域からそれぞれ3つの端子が生成され、これがベース(b)、エミッタ(e)、コレクタ(c)です。これらは2つのP-N接合、すなわちエミッタ接合とコレクタ接合を形成します。トランジスタの回路記号の矢印の方向はエミッタ接合の方向を示しています。

* `P–N接合 - Wikipedia <https://ja.wikipedia.org/wiki/Pn%E6%8E%A5%E5%90%88>`_

半導体のタイプに基づいて、トランジスタはNPNとPNPの2つのグループに分けられます。略称から、前者は2つのN型半導体と1つのP型で作られ、後者はその逆です。下の図を参照してください。

.. note::
    s8550はPNPトランジスタで、s8050はNPNです。見た目は非常によく似ているため、ラベルを注意深く確認する必要があります。

|img_transistor_symbol|

NPNトランジスタにハイレベルの信号が通ると、エネルギーが供給されます。しかし、PNPトランジスタはローレベルの信号で制御されます。両方のタイプのトランジスタは非接触スイッチとして頻繁に使用されます。

* `S8050トランジスタのデータシート <https://components101.com/asset/sites/default/files/component_datasheet/S8050%20Transistor%20Datasheet.pdf>`_
* `S8550トランジスタのデータシート <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

ラベル面を自分たちに向け、ピンを下に向けます。左から右に、エミッタ(e)、ベース(b)、コレクタ(c)のピンがあります。

|img_ebc|

.. note::
    * ベースは、より大きな電気供給のゲートコントローラーです。
    * NPNトランジスタでは、コレクタが大きな電気供給であり、エミッタがその供給の出口です。PNPトランジスタはその逆です。

.. Example
.. -------------------

.. :ref:`2種類のトランジスタ`


**例**

* :ref:`py_transistor` (MicroPythonユーザー向け)
* :ref:`py_relay` (MicroPythonユーザー向け)
* :ref:`py_ac_buz` (MicroPythonユーザー向け)
* :ref:`py_pa_buz` (MicroPythonユーザー向け)
* :ref:`py_light_theremin` (MicroPythonユーザー向け)
* :ref:`py_alarm_lamp` (MicroPythonユーザー向け)
* :ref:`py_music_player` (MicroPythonユーザー向け)
* :ref:`py_fruit_piano` (MicroPythonユーザー向け)
* :ref:`py_reversing_aid` (MicroPythonユーザー向け)
* :ref:`ar_ac_buz` (Arduinoユーザー向け)
* :ref:`ar_pa_buz` (Arduinoユーザー向け)
* :ref:`ar_transistor` (Arduinoユーザー向け)
* :ref:`ar_relay` (Arduinoユーザー向け)
* :ref:`per_service_bell` (Piper Makeユーザー向け)
* :ref:`per_reversing_system` (Piper Makeユーザー向け)
* :ref:`per_reaction_game` (Piper Makeユーザー向け)
