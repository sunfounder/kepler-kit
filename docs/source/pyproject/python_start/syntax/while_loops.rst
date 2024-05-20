.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_syntax_while_loops:

Whileループ
====================

``while`` 文は、特定の条件下で同じタスクを繰り返し処理するためにプログラムをループで実行するために使用されます。

基本的な形式は以下の通りです：

.. code-block:: python

    while テスト式:
        whileの本体


``while`` ループでは、まず ``テスト式`` をチェックします。 ``テスト式`` が ``True`` と評価された場合のみ、whileの本体に入ります。一回の反復後、再び ``テスト式`` をチェックします。このプロセスは、 ``テスト式`` が ``False`` と評価されるまで続きます。

MicroPythonでは、 ``while`` ループの本体はインデントによって決定されます。

本体はインデントで始まり、最初の非インデント行で終わります。

Pythonは、非ゼロの値を ``True`` と解釈します。Noneと0は ``False`` と解釈されます。

**whileループのフローチャート**

.. image:: img/while_loop.png



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        x -= 1

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6
5
4
3
2
1


Break文
--------------------

break文を使って、while条件がtrueであってもループを停止することができます。



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        if x == 6:
            break
        x -= 1

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6

Elseを持つWhileループ
----------------------
``if`` ループと同様に、 ``while`` ループにもオプションで ``else`` ブロックを持たせることができます。

``while`` ループの条件が ``False`` と評価された場合、 ``else`` 部分が実行されます。



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        x -= 1
    else:
        print("Game Over")

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6
5
4
3
2
1
Game Over
