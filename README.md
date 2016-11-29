# wotmods-saveaccount

World of Tanks (WoT) ASIA クライアント用のいわゆるパスワード保存modというやつです

## インストール

[リリースページ](../../releases/latest) から mod_saveaccount.pyc をダウンロードして、
他の多くの mod と同じように WoT インストールフォルダの
res_mods\XXX\scripts\client\gui\mods にコピーします (XXX はクライアントのバージョン)。

## 従来のパスワード保存 mod との違い

従来のパスワード保存 mod は gui_settings.xml の設定を書き換えたファイルを res_mods\XXX\gui に設置するものでした。
この方式はシンプルで効果的ですが、
gui_settings.xml 内には他の設定項目も数多く含まれており、
クライアントの動作に必要で省略が不可なため、
常に現在のクライアントバージョンの設定と同期させておく必要があります。

この mod は gui_settings.xml の設定のうち、
アカウント情報の保存にかかわる設定のみを変更するので
クライアントのバージョン更新の影響を受けにくいという長所があります (影響がないとは言っていない)。
