.. _cpn_led:

LED
==========

|img_led|

半導体発光ダイオードは、PN接合を通じて電気エネルギーを光エネルギーに変換する部品です。波長によっては、レーザーダイオード、赤外発光ダイオード、および一般的には発光ダイオード（LED）として知られている可視光発光ダイオードに分類できます。

ダイオードは単方向の導電性があり、回路記号の矢印が示すように電流が流れます。アノードに正の電源、カソードに負の電源を供給することで、LEDは点灯します。

|img_led_symbol|

LEDには二つのピンがあります。長い方がアノードで、短い方がカソードです。逆に接続しないように注意してください。LEDには固定された順方向電圧降下があり、この降下を上回る供給電圧があるとLEDが焼けるため、回路に直接接続することはできません。赤、黄、緑のLEDの順方向電圧は1.8V、白のLEDは2.6Vです。ほとんどのLEDは最大電流20mAまで耐えられるため、直列に電流制限抵抗を接続する必要があります。

抵抗値の計算式は以下の通りです：

    R = (Vsupply – VD)/I

**R** は電流制限抵抗の抵抗値、 **Vsupply** は供給電圧、 **VD** は電圧降下、 **I** はLEDの動作電流を表します。

詳しいLEDの紹介はこちら： `LED - Wikipedia <https://en.wikipedia.org/wiki/Light-emitting_diode>`_。

**例**

* :ref:`py_led` （MicroPythonユーザー向け）
* :ref:`py_fade` （MicroPythonユーザー向け）
* :ref:`py_alarm_lamp` （MicroPythonユーザー向け）
* :ref:`py_traffic_light` （MicroPythonユーザー向け）
* :ref:`py_reversing_aid` （MicroPythonユーザー向け）
* :ref:`ar_led` （Arduinoユーザー向け）
* :ref:`ar_fade` （Arduinoユーザー向け）
* :ref:`per_blink` （Piper Makeユーザー向け）
* :ref:`per_button` （Piper Makeユーザー向け）
* :ref:`per_service_bell` （Piper Makeユーザー向け）
* :ref:`per_reversing_system` （Piper Makeユーザー向け）
* :ref:`per_reaction_game` （Piper Makeユーザー向け）

