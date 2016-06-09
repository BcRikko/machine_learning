食べられるキノコはどれだ？
====

問題
----
3種類あるキノコのうち、2種類が毒キノコらしい。  
採ってきたキノコと、食べたキノコのデータから、食用キノコを見分けなさい（教師なし学習）

元ネタ

* [食べられるキノコはどれだ？ | CodeIQ](https://codeiq.jp/q/140)
* [「機械学習基礎」簡単な問題を 解いて理解しよう！前篇 - Tech総研](http://next.rikunabi.com/tech_souken/entry/ct_s03600p002315)


採取したキノコのデータ
----
[data.txt](./data.txt)に96件のキノコのデータが含まれる。  
形式は以下のとおりで、半角スペース区切りで登録されている。

* 柄の長さ(cm)
* 傘の直径(cm)


食べたキノコのデータ
----
[eaten.txt](./eaten.txt)に6件のデータが含まれる。  
形式は以下のとおりで、半角スペース区切りで登録されている。

* 柄の長さ(cm)
* 傘の直径(cm)
* 食べられるかどうか(○:食用キノコ、×:毒キノコ)


予測結果
----
[answer.txt](./answer.txt)に食用キノコのデータ（柄の長さ、傘の直径）を半角スペース区切りで出力される。