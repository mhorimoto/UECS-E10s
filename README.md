
# UECS-E10s

UECS E10s用の送信モジュール。

画像撮影時の情報をUECS E10s電文により送信するためのモジュール  
(E10s=文字画像情報通信補足規約(原案) 2011/10/21)

## Install

    $ git clone git@github.com:mhorimoto/UECS-E10s.git
    $ cd UECS-E10s
    $ sudo install e10s.py /usr/local/bin

最終行の /usr/local/bin は撮影プログラムと同じディレクトリで良いのです。

## Usage

### 関数として使う場合
撮影が終了した都度その状況を送出するために適当な場所に以下のコーディングを追加します。

    import e10s
    # 
    # 撮影プログラムを書く
    #
    # time_header=YYYYMMDDhhmmss 書式の日時
    #
      memo="west_bed:{0}".format(time_header+"_0.jpg")
      t='{0}'.format(time_header)
      a='1:1:2' # UECSのRoom:Region:Order
      e10s.send(memo,u=post_url,t=t,a=a) # ここで送信

この方法は、撮影プログラムに自身で手が入れられる場合に有効な方法です。

### シェルスクリプトとして使う場合
撮影プログラムの後に実行します。

    $ /usr/local/bin/picam_withIP.py  # 撮影プログラム
    $ /usr/local/bin/e10s.py 'MEMO' 'URL' 'TIME' 'AT'

撮影プログラムに手を入れられない場合に有効な方法です。


## UECS出力
以下の出力がブロードキャストされます。

    <?xml version="1.0" encode="utf-8"?><UECS ver="1.00-E10s"><MEMO>west_bed:20230903160002_0.jpg</MEMO><URI>https://agri-eye.net/rbtdata_uploader.php</URI><TIME>20230903160002</TIME><AT>1:1:2</AT><IP>192.168.38.103</IP></UECS>

