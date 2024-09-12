# Graph_maker
pythonのmatplotlibを用いたグラフ作成用ライブラリ．
yamlファイルをインプットとして読み込む．

以下，各変数の説明．

- *input*
  - プロットしたいデータが入ったファイル名．複数個のファイルを指定することが可能であり，その場合は["input1.dat","input2.dat"]のように記述する．ファイル数が1個の場合でも["input1.dat"]と配列の様に記述する．ファイルの1列目が横軸，2列目が縦軸に相当する．

- *output*
  - アウトプットとする画像ファイルの名前．

- *legend*
  - 凡例．*input*と同様の記述方法であり，*input*と対応した順番である必要がある．

- *color*
  - プロットする線または点の色．*input*と対応した順番である必要がある．特に指定しない場合はmatplotlibのデフォルトカラーが用いられる．

- *use_legend* (true or false, default:true)
  - 凡例を用いるかどうか．

- *linewidth*
  - プロットする線の太さ．*input*と対応した順番である必要がある．

- *maker*
  - 用いるマーカーのタイプ．*input*と対応した順番である必要がある．デフォルトでは["o","^","s","x","D"]になっている．

- *markersize*
 - プロットする点の大きさ．*input*と対応した順番である必要がある． デフォルトでは0になっており，点はプロットされない．0より大きい値に設定した場合，線に加えて点がプロットされる．点のみをプロットする場合は*linewidth*を0に設定する．

- *marker_only_outline*
 - プロットする点を白抜きにするかどうか．*input*と対応した順番である必要がある． 

- *marker_edge_width*
 - プロットする点の枠線の太さ．*input*と対応した順番である必要がある．

- *xlabel*
  - x軸に用いるラベル．\$\$で囲うことでtexと同様の記述が可能．ただし，通常のmatplotlibにおける場合と同様にバックスラッシュ\\は二重にする必要がある．

- *ylabel*
  - y軸に用いるラベル．*xlabel*と同様．

- *xlabel_size*, *ylabel_size*
  - x軸，y軸のそれぞれのラベルサイズ．

- *xticks_size*, *yticks_size*
  - それぞれ，x軸，y軸ののサイズ．

- *fig_sizex*, *fig_sizey*
 - それぞれ，アウトプットする画像の横と縦の長さ．

- *square* (true or false, default: false)
  - グラフを正方形にするかどうか．

- *xmin*, *xmax*, *ymin*, *ymax*
 - それぞれx軸，y軸の最小値，最大値．

- *plot_colormesh* (true or false, default: false)
  - カラーマップを描画するかどうか．***カラーマップを描画するためのデータはgnuplotで用いられるものと同様の形式で用意する必要がある．***(examples/colormapを参照)

- *plot_contour* (true or false, default: false)
  - contour(等高線)を描画するかどうか．必要なデータ形式については*plot_colormesh*と同様．*plot_colormesh*や*plot_contourf*と同時に用いることが可能．

- *plot_contourf* (true or false, default: false)
  - contourf(塗りつぶした等高線)を描画するかどうか．必要なデータ形式については*plot_colormesh*と同様．
 
- *contour_level*
  - contour(等高線)の本数

- *contourf_level*
  - contourfの本数 

- *cbmin*, *cbmax*
  - カラーバーの範囲の最小値と最大値．

- *cblabel*
  - カラーバーのラベル．  

- *xscale*, *yscale*, *cbscale* (linear or log, default: log)
 - それぞれ，x軸，y軸，カラーバーのスケール． 