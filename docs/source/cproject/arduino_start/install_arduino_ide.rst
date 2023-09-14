.. _install_arduino:

1.1 Arduino IDEのインストール（重要）
======================================

Arduino IDE（Arduino Integrated Development Environment、Arduino統合開発環境）は、Arduinoプロジェクトを完成させるために必要なソフトウェアサポートを全て提供します。これはArduinoチームによって提供される、Arduino専用のプログラミングソフトウェアであり、プログラムの記述とArduinoボードへのアップロードが可能です。

Arduino IDE 2.0はオープンソースプロジェクトであり、堅牢な先代であるArduino IDE 1.xから大きく進化しています。リニューアルされたUI、強化されたボード&ライブラリマネージャー、デバッガー、オートコンプリート機能など多くの新機能が追加されています。

このチュートリアルでは、Windows、Mac、LinuxコンピュータにArduino IDE 2.0をダウンロードしてインストールする方法を説明します。

必要条件
-------------------

* Windows - Win 10以降、64ビット
* Linux - 64ビット
* Mac OS X - バージョン10.14「Mojave」以降、64ビット

Arduino IDE 2.0をダウンロード
-------------------------------

#. |link_download_arduino| ページを訪れてください。

#. お使いのOSバージョンに合わせたIDEをダウンロードしてください。

    .. image:: img/sp_001.png

インストール
------------------------------

Windows
^^^^^^^^^^^^^

#. ダウンロードした ``arduino-ide_xxxx.exe`` ファイルをダブルクリックして実行します。

#. ライセンス契約を読み、同意してください。

    .. image:: img/sp_002.png

#. インストールオプションを選択します。

    .. image:: img/sp_003.png

#. インストール先を選択します。システムドライブ以外にソフトウェアをインストールすることが推奨されています。

    .. image:: img/sp_004.png

#. その後、完了します。

    .. image:: img/sp_005.png

macOS
^^^^^^^^^^^^^^^^

ダウンロードした ``arduino_ide_xxxx.dmg`` ファイルをダブルクリックし、指示に従って **Arduino IDE.app** を **Applications** フォルダにコピーします。数秒後にArduino IDEが正常にインストールされたことが確認できます。

.. image:: img/macos_install_ide.png
    :width: 800

Linux
^^^^^^^^^^^^

LinuxシステムでArduino IDE 2.0をインストールするチュートリアルは、以下のリンクを参照してください：https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing#linux


IDEを開く
--------------

#. Arduino IDE 2.0を初めて開くと、Arduino AVR Boards、組み込みライブラリ、その他必要なファイルが自動的にインストールされます。

    .. image:: img/sp_901.png

#. また、ファイアウォールやセキュリティセンターがデバイスドライバーのインストールを求めるポップアップが数回表示される場合があります。全てインストールしてください。

    .. image:: img/sp_104.png

#. これで、Arduino IDEの準備が完了です！

    .. note::
        ネットワーク問題やその他の理由で一部のインストールが失敗した場合、Arduino IDEを再度開くと残りのインストールが完了します。すべてのインストールが完了した後、VerifyまたはUploadをクリックしない限り、Outputウィンドウは自動的には開きません。

