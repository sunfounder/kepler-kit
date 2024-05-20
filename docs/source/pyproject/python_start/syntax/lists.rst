.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _syntax_list:

リスト
===================

リストは複数のアイテムを一つの変数で格納するために使用され、角括弧を使って作成されます。

.. code-block:: python

    B_list = ["Blossom", "Bubbles","Buttercup"]
    print(B_list)


リストのアイテムは変更可能で、順序があり、重複する値を許容します。
リストのアイテムはインデックス付きで、最初のアイテムがインデックス [0]、次のアイテムがインデックス [1]、と続きます。

.. code-block:: python

    C_list = ["Red", "Blue", "Green", "Blue"]
    print(C_list)            # 重複を許容
    print(C_list[0]) 
    print(C_list[1])         # 順序付き
    C_list[2] = "Purple"     # 変更可能
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Blue', 'Green', 'Blue']
Red
Blue
['Red', 'Blue', 'Purple', 'Blue']


リストは異なるデータ型を含むことができます：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
['Banana', 255, False, 3.14]


リストの長さ
------------------
リストにいくつのアイテムが含まれているかを判定するには、len()関数を使用します。

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(len(A_list))

>>> %Run -c $EDITOR_CONTENT
4

リストアイテムの確認
-----------------------

リストの二番目のアイテムを出力します：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list[1])

>>> %Run -c $EDITOR_CONTENT
[255]

リストの最後のアイテムを出力します：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list[-1])

>>> %Run -c $EDITOR_CONTENT
[3.14]

二番目と三番目のアイテムを出力します：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    print(A_list[1:3])

>>> %Run -c $EDITOR_CONTENT
[255, False]


リストアイテムの変更
----------------------
二番目と三番目のアイテムを変更します：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    A_list[1:3] = [True,"Orange"] 
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
['Banana', True, 'Orange', 3.14]

二番目の値を2つの値で置き換えます：

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14]
    A_list[1:2] = [True,"Orange"] 
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
['Banana', True, 'Orange', False, 3.14]


リストアイテムの追加
-----------------------

append()メソッドを使用してアイテムを追加します：

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.append("Orange")
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Blue', 'Green', 'Orange']

二番目の位置にアイテムを挿入します：

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.insert(1, "Orange")
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Orange', 'Blue', 'Green']



リストアイテムの削除
-----------------------

remove()メソッドは指定したアイテムを削除します。

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.remove("Blue")
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Green']

pop()メソッドは指定したインデックスのアイテムを削除します。インデックスを指定しない場合、pop()メソッドは最後のアイテムを削除します。

.. code-block:: python

    A_list = ["Banana", 255, False, 3.14, True,"Orange"]
    A_list.pop(1)
    print(A_list)
    A_list.pop()
    print(A_list)

>>> %Run -c $EDITOR_CONTENT
255
['Banana', False, 3.14, True, 'Orange']
'Orange'
['Banana', False, 3.14, True]

``del`` キーワードも指定したインデックスのアイテムを削除します：

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    del C_list[1]
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
['Red', 'Green']

clear()メソッドはリストを空にします。リスト自体は残りますが、内容はありません。

.. code-block:: python

    C_list = ["Red", "Blue", "Green"]
    C_list.clear()
    print(C_list)

>>> %Run -c $EDITOR_CONTENT
[]
