# AI文書類似度検索システム

## 概要
このプロジェクトは、OpenAIの埋め込みモデルとFAISSを使用して、テキストドキュメントの類似度検索を行うシステムです。与えられたクエリに対して、最も関連性の高いドキュメントを検索し、類似度スコアと共に結果を表示します。
類似度が高い順に表示されます。

## 機能
- テキストドキュメントの埋め込みベクトル化
- FAISSを使用した高速な類似度検索
- 類似度スコアの計算と表示

## 必要条件
- Python 3.8以上
- OpenAI API キー

## 依存ライブラリ
- langchain
- langchain-openai
- faiss-cpu
- python-dotenv

## セットアップ
1. リポジトリをクローン

git clone <repository-url>

2. 依存ライブラリをインストール

```bash
pip install -r requirements.txt
```

3. 環境変数の設定
`.env`ファイルをプロジェクトのルートディレクトリに作成し、以下の内容を設定：

```
OPENAI_API_KEY=your-api-key-here
```

## 使用方法

python src/main.py

## プロジェクト構造
.
├── README.md
├── requirements.txt
├── .env
└── src/
└── main.py

## ライセンス
MIT

## 作者
[あなたの名前]

## 注意事項
- OpenAI APIの利用には料金が発生する場合があります
- 大量のデータを処理する場合は、APIの利用制限にご注意ください
