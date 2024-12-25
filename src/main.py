# 必要なライブラリをインポート
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def main():
    # .envファイルから環境変数を読み込む
    load_dotenv()

    # OpenAIの埋め込みモデルをインスタンス化
    embeddings = OpenAIEmbeddings()

    # ドキュメント群（6件）
    documents = [
        "昨日の天気予報は晴れでした。",
        "サッカーの試合結果：日本が勝利！",
        "AI技術が進化している理由について。",
        "株式市場の最新ニュースをお届けします。",
        "猫が可愛くて好きです。",
        "焼肉が食べたいです。"
    ]

    # FAISSベクトルデータベースを作成
    faiss_db = FAISS.from_texts(documents, embeddings)

    # 検索クエリ
    query = "AIに関する最新ニュースを教えて"
    query_vector = embeddings.embed_query(query)

    # 類似度検索とスコア取得（結果件数を6に設定）
    results_with_scores = faiss_db.similarity_search_with_relevance_scores(query, k=len(documents))

    # 検索結果とスコアを表示
    print("検索結果:")
    for result, score in results_with_scores:
        print(f"ドキュメント: {result}, 類似度スコア: {score:.4f}")

# スクリプトが直接実行された場合にのみmain()を実行
if __name__ == "__main__":
    main()
