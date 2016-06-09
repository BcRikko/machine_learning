機械学習（Machine Learning）の学習用リポジトリ
=====


Dependencies
----

* Python (3.5.1)
* scikit-learn (0.17.1)
* scipy (0.17.1)
* NumPy (1.11.0)
* Seaborn (0.7.1)
  Seabornをインストールすると一緒に幾つかのパッケージがインストールされる


Documents
----

機械学習で学んだことは[contents](./docs/0_contents.md)にまとめていく


Question
----

機械学習の練習問題については、各フォルダにある`readme.md`を参照


Caution
-------

Seabornで`RuntimeError: Python is not installed as a framework.`というエラーがでた場合

1. `$ python -c "import matplotlib;print(matplotlib.matplotlib_fname())"`で`matplotlibrc`の場所を確認
2. 38行目の`backend: macos`を`backend: Tkagg`に変更する