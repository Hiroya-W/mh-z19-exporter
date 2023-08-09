# mh-z19-exporter

MH-Z19を使ったCO2のPrometheus exporter

## Setup

依存パッケージをインストールします。

```bash
git clone https://github.com/Hiroya-W/mh-z19-exporter.git
cd mh-z19-exporter
pip insatll .
```

## Run

MH-Z19 をroot権限無しで使えるようにしている場合は以下のようにして実行することが出来ます。

```bash
python main.py
```

root権限が必要な場合は、以下のようにします。

```bash
sudo python main.py
```

詳しくは、[#How to use without root permission.](https://github.com/UedaTakeyuki/mh-z19#how-to-use-without-root-permission)を参照してください。

メトリクスは http://localhost:9000 にアクセスすることで取得することが出来ます。

```
MH_Z19_EXPORTER_CO2 1166.0
```

## サービスとして動かす

リポジトリ内にサービスファイルの例(`mh-z19-exporter.service`)を配置しています。

プログラムは以下のように`/opt`下に配置したときを想定しています。

```bash
cd /opt
git clone https://github.com/Hiroya-W/mh-z19-exporter.git
cd /opt/mh-z19-exporter
pip install .
```

```bash
cd /opt/mh-z19-exporter
sudo cp mh-z19-exporter.service /etc/systemd/system/
sudo systemctl daemon-reload
```

```bash
sudo systemctl enable z19-exporter.service 
sudo systemctl start z19-exporter.service 
```
