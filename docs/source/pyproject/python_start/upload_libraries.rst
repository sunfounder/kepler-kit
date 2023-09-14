.. _add_libraries_py:

1.4 Picoにライブラリをアップロード
===================================

いくつかのプロジェクトでは、追加のライブラリが必要になることがあります。そこで、最初にこれらのライブラリをRaspberry Pi Pico Wにアップロードし、後でコードを直接実行できるように設定します。

#. 下記のリンクから関連するコードをダウンロードします。

   * :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

#. Thonny IDEを開き、マイクロUSBケーブルでPicoをコンピュータに接続します。そして、右下隅にある「MicroPython（Raspberry Pi Pico）.COMXX」インタプリターをクリックします。

    .. image:: img/sec_inter.png

#. 上部ナビゲーションバーで、 **表示** -> **ファイル** を選択します。

    .. image:: img/th_files.png

#. 以前ダウンロードした `コードパッケージ <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`_ が保存されているフォルダへとパスを切り替え、 ``kepler-kit-main/libs`` フォルダに進みます。

    .. image:: img/th_path.png

#. ``libs/`` フォルダ内の全てのファイルまたはフォルダーを選択し、右クリックして **アップロード先** を選択します。アップロードには少し時間がかかります。

    .. image:: img/th_upload.png

#. これで、アップロードしたばかりのファイルがドライブ内の「Raspberry Pi Pico」で確認できるようになります。

    .. image:: img/th_done.png
