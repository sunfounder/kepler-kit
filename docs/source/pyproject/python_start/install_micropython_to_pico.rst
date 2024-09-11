.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _install_micropython_on_pico:

1.3 Raspberry Pi PicoにMicroPythonをインストール
=====================================================

Thonny IDEを使って、Raspberry Pi PicoにMicroPythonを簡単に一回でインストールしましょう。

.. note::
    Thonnyをアップグレードしたくない場合、Raspberry Pi公式の |link_micropython_pi| を使って、 ``rp2_pico_xxxx.uf2`` ファイルをRaspberry Pi Picoにドラッグアンドドロップすることもできます。

#. Thonny IDEを開きます。

    .. image:: img/set_pico1.png

#. **BOOTSEL** ボタンを押しながら、Micro USBケーブルでPicoをコンピューターに接続します。Picoが **RPI-RP2** という名前の大容量ストレージデバイスとしてマウントされたら、 **BOOTSEL** ボタンを離します。

    .. image:: img/bootsel_onboard.png

#. 右下隅で、インタープリタ選択ボタンをクリックし、 **MicroPythonをインストール** を選択します。

    .. note::
        もしThonnyにこのオプションがない場合、最新バージョンに更新してください。

    .. image:: img/set_pico2.png

#. **対象のボリューム** で、先ほど挿入したPicoのボリュームが自動的に表示されます。 **MicroPythonのバリアント** で、 **Raspberry Pi.Pico W/Pico WH** を選択します。

    .. image:: img/set_pico3.png

#. **インストール** ボタンをクリックし、インストールが完了するまで待ってからこのページを閉じます。

    .. image:: img/set_pico4.png

おめでとうございます、あなたのRaspberry Pi Picoは使用準備が整いました。
