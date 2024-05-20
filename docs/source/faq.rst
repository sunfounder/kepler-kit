.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

FAQ
=========

Arduino
---------------------

#. Arduino IDEでコードのアップロードに失敗した場合は？

   * Arduino IDEが正しくPicoを認識しているか確認してください。ポートはCOMXX（Raspberry Pi Pico）でなければなりません。詳細は :ref:`setup_pico_arduino` を参照してください。
   * ボード（Raspberry Pi Pico）またはポート（COMXX（Raspberry Pi Pico））が正しく選択されているか確認してください。
   * コードに問題がなく、正しいボードとポートが選択されている場合でも、アップロードが成功しない場合は、 **アップロード** アイコンを再度クリックしてください。進行状況が「アップロード中...」と表示されたら、USBケーブルを抜いて、 **BOOTSEL** ボタンを押しながら再度挿入します。その後、コードのアップロードが成功します。

MicroPython
------------------

#. コードを開いて実行する方法は？
   詳細なチュートリアルは :ref:`open_run_code_py` を参照してください。

#. Raspberry Pi Pico Wにライブラリをアップロードする方法は？
   詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

#. Thonny IDEにMicroPython（Raspberry Pi Pico W）インタープリタオプションがない？

   * Pico WがUSBケーブルでコンピュータに接続されているか確認してください。
   * Pico W用のMicroPythonをインストールしたか確認してください（ :ref:`install_micropython_on_pico` ）。
   * Raspberry Pi Pico Wインタープリタは、Thonnyのバージョン3.3.3以降でのみ利用可能です。古いバージョンを使用している場合は、アップデートしてください（ :ref:`thonny_ide` ）。
   * この時点でLi-poチャージャーモジュールがブレッドボードに接続されている場合は、それを最初に抜いてから、Pico Wをコンピュータに再接続してください。

#. Thonny IDEを経由してPico Wのコードを開いたり保存することができない？

   * Pico WがUSBケーブルでコンピュータに接続されているか確認してください。
   * インタープリタとして **MicroPython（Raspberry Pi Pico）** が選択されているか確認してください。

#. Raspberry Pi Pico WはThonnyとArduinoで同時に使用できるか？
    いいえ、いくつかの異なる操作が必要です。


   * 最初にArduinoで使用していて、今Thonny IDEで使用したい場合は、その上で :ref:`install_micropython_on_pico` が必要です。
   * 最初にThonnyで使用していて、今Arduino IDEで使用したい場合は、 :ref:`setup_pico_arduino` が必要です。

#. お使いのコンピュータがWin7でPico Wが認識されない場合は？

   * USB CDCドライバーを次のURLからダウンロードしてください： `this link <http://aem-origin.microchip.com/en-us/mindi-sw-library?swsearch=Atmel%2520USB%2520CDC%2520Virtual%2520COM%2520Driver>`_
   * ``amtel_devices_cdc.inf`` ファイルを ``pico-serial`` という名前のフォルダに解凍します。
   * ``amtel_devices_cdc.inf`` ファイルの名前を ``pico-serial.inf`` に変更します。
   * ノートパッドのような基本的なエディタで ``pico-serial.inf`` を開き/編集します。
   * 以下の見出しの下にある行を削除して置き換えます：

   .. code-block::

       [DeviceList]
       %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

       [DeviceList.NTAMD64]
       %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

       [DeviceList.NTIA64]
       %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

       [DeviceList.NT]
       %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

       [Strings]
       Manufacturer = "ATMEL, Inc."
       PI_CDC_PICO = "Pi Pico Serial Port"
       Serial.SvcDesc = "Pi Pico Serial Driver"

   #. 閉じて保存し、名前が ``pico-serial.inf`` として保持されていることを確認してください。
   #. PCのデバイスリストに移動し、CDCデバイスとして名前が付けられたpicoをポートで見つけます。黄色い感嘆符がそれを示しています。
   #. CDCデバイスを右クリックして、保存した場所から作成したファイルを選択してドライバーを更新またはインストールします。

Piper Make
------------------

#. Piper MakeでPico Wをセットアップする方法は？

   詳細なチュートリアルは :ref:`per_setup_pico` を参照してください。

#. コードをダウンロードまたはインポートする方法は？

   詳細なチュートリアルは :ref:`per_save_import` を参照してください。

#. Pico Wに接続する方法は？

   詳細なチュートリアルは :ref:`connect_pico_per` を参照してください。

