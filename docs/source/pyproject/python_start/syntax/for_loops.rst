.. _syntax_forloop:

For ループ
============

``for`` ループは、リストや文字列など、任意の項目のシーケンスを走査することができます。

for ループの文法形式は以下の通りです：

.. code-block:: python

    for val in sequence:
        Body of for

ここで、 ``val`` は各イテレーションでシーケンス内の項目の値を取得する変数です。

ループは、シーケンス内の最後の項目に到達するまで続きます。 ``for`` ループの本体と残りのコードを区別するためにインデントを使用します。

**for ループのフローチャート**

.. image:: img/for_loop.png




.. code-block:: python

    numbers = [1, 2, 3, 4]
    sum = 0

    for val in numbers:
        sum = sum + val

    print("The sum is", sum)

>>> %Run -c $EDITOR_CONTENT
The sum is 10

break 文
-------------------------

break 文を使用すると、すべての項目をループ処理する前にループを停止することができます。



.. code-block:: python

    numbers = [1, 2, 3, 4]
    sum = 0

    for val in numbers:
        sum = sum + val
        if sum == 6:
            break
    print("The sum is", sum)

>>> %Run -c $EDITOR_CONTENT
The sum is 6

continue 文
--------------------------------------------

``continue`` 文を使用すると、ループの現在のイテレーションを停止し、次のイテレーションで続行することができます。



.. code-block:: python

    numbers = [1, 2, 3, 4]

    for val in numbers:
        if val == 3:
            continue
        print(val)

>>> %Run -c $EDITOR_CONTENT
1
2
4


range() 関数
--------------------------------------------

range() 関数を使用して数値のシーケンスを生成することができます。range(6)は、0から5まで（6つの数値）を生成します。

また、開始値、終了値、ステップサイズをrange(start, stop, step_size)として定義することもできます。step_sizeが指定されていない場合、デフォルトは1になります。

rangeオブジェクトは「遅延評価される」（lazy）と言えます。オブジェクトを生成した時点で、その中に「含まれる」すべての数値は生成されていません。ただし、これはイテレータではありません。なぜなら、in、len、そして ``__getitem__`` 操作がサポートされているからです。

この関数はすべての値をメモリに保持していません。そうすると非効率的になります。したがって、開始値、終了値、ステップサイズを覚えておき、進行中に次の数値を生成します。

この関数がすべての項目を出力するように強制するには、list()関数を使用することができます。



.. code-block:: python

    print(range(6))

    print(list(range(6)))

    print(list(range(2, 6)))

    print(list(range(2, 10, 2)))

>>> %Run -c $EDITOR_CONTENT
range(0, 6)
[0, 1, 2, 3, 4, 5]
[2, 3, 4, 5]
[2, 4, 6, 8]


``for`` ループの中で ``range()`` を使用して数値のシーケンスを反復処理することができます。これはlen()関数と組み合わせて、インデックスを使用してシーケンスを走査することもできます。



.. code-block:: python

    fruits = ['pear', 'apple', 'grape']

    for i in range(len(fruits)):
        print("I like", fruits[i])
        
>>> %Run -c $EDITOR_CONTENT
I like pear
I like apple
I like grape

For ループにおけるElse
--------------------------------

``for`` ループには、オプションで ``else`` ブロックも追加することができます。ループで使用されるシーケンスの項目がすべて使い切られた場合、 ``else`` 部分が実行されます。

``break`` キーワードを使用して ``for`` ループを停止することができます。この場合、 ``else`` 部分は無視されます。

したがって、何らかの中断が発生しない場合、 ``for`` ループの ``else`` 部分が実行されます。



.. code-block:: python

    for val in range(5):
        print(val)
    else:
        print("Finished")

>>> %Run -c $EDITOR_CONTENT
0
1
2
3
4
Finished

break文によってループが停止された場合、elseブロックは実行されません。



.. code-block:: python

    for val in range(5):
        if val == 2: break
        print(val)
    else:
        print("Finished")

>>> %Run -c $EDITOR_CONTENT
0
1

