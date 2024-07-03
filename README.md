<h1 align="center">Kor-IR: 한국어 검색을 위한 임베딩 벤치마크</h1>

## Intro

한국어 임베딩 모델의 검색 (Information Retrieval) 성능 비교를 위한 리더보드입니다.
현재 [Ko-StrategyQA](https://huggingface.co/datasets/taeminlee/Ko-StrategyQA) 데이터셋을 사용해 IR 성능을 측정했습니다.

## Leader Board (last updated on July 3, 2024)

|     | Model                                                  | NDCG@10 | MRR@10 | MAP@10 | Recall@10 | Average | Link                                                                                                |
|-----|--------------------------------------------------------|---------|--------|--------|-----------|---------|-----------------------------------------------------------------------------------------------------|
| 1   | **Upstage/solar-embedding-1-large**                    | 83.61   | 84.14  | 80.35  | 88.35     | 84.11   | [:paperclip:](https://developers.upstage.ai/docs/apis/embeddings)                                    |
| 2   | **Cohere/embed-multilingual-v3.0**                     | 80.79   | 82.33  | 76.80  | 85.96     | 81.47   | [:paperclip:](https://docs.cohere.com/reference/embed)                                               |
| 3   | **intfloat/multilingual-e5-large-instruct**       | 80.68   | 82.52  | 76.61  | 85.74     | 81.39   | [:paperclip:](https://huggingface.co/intfloat/multilingual-e5-large-instruct)                        |
| 4   | **intfloat/multilingual-e5-large**                     | 80.35   | 82.01  | 76.37  | 85.40     | 81.03   | [:paperclip:](https://huggingface.co/intfloat/multilingual-e5-large)                                 |
| 5   | **Voyage/voyage-multilingual-2**                       | 79.69   | 80.53  | 75.24  | 86.43     | 80.47   | [:paperclip:](https://docs.voyageai.com/docs/embeddings)                                             |
| 6   | **BAAI/bge-m3**                                        | 79.40   | 81.12  | 75.07  | 85.20     | 80.20   | [:paperclip:](https://huggingface.co/BAAI/bge-m3)                                                    |
| 7   | **intfloat/multilingual-e5-base**                      | 76.35   | 79.04  | 71.60  | 82.06     | 77.26   | [:paperclip:](https://huggingface.co/intfloat/multilingual-e5-base)                                  |
| 8   | **intfloat/multilingual-e5-small**                     | 75.16   | 77.55  | 69.78  | 82.17     | 76.16   | [:paperclip:](https://huggingface.co/intfloat/multilingual-e5-small)                                 |
| 9   | **Cohere/embed-multilingual-light-v3.0**               | 74.22   | 76.31  | 68.91  | 81.26     | 75.17   | [:paperclip:](https://docs.cohere.com/reference/embed)                                               |
| 10  | **OpenAI/text-embedding-3-large**                      | 73.74   | 75.70  | 68.47  | 80.99     | 74.73   | [:paperclip:](https://platform.openai.com/docs/guides/embeddings/embedding-models)                   |
| 11  | **upskyy/kf-deberta-multitask**                        | 68.42   | 70.14  | 61.64  | 78.71     | 69.73   | [:paperclip:](https://huggingface.co/upskyy/kf-deberta-multitask)                                    |
| 12  | **cateto/longformer-ko-sroberta-multitask-23040**      | 66.31   | 68.51  | 59.34  | 76.62     | 67.69   | [:paperclip:](https://huggingface.co/cateto/longformer-ko-sroberta-multitask-23040)                  |
| 13  | **jhgan/ko-sroberta-multitask**                        | 65.10   | 67.46  | 58.03  | 75.41     | 66.50   | [:paperclip:](https://huggingface.co/jhgan/ko-sroberta-multitask)                                    |
| 14  | **jhgan/ko-sroberta-nli**                              | 63.90   | 66.56  | 56.84  | 74.09     | 65.35   | [:paperclip:](https://huggingface.co/jhgan/ko-sroberta-nli)                                          |
| 15  | **jhgan/ko-sbert-multitask**                           | 62.86   | 65.60  | 55.61  | 73.34     | 64.35   | [:paperclip:](https://huggingface.co/jhgan/ko-sbert-multitask)                                       |
| 16  | **BM-K/KoSimCSE-bert-multitask**                       | 56.93   | 59.17  | 49.21  | 69.03     | 58.59   | [:paperclip:](https://huggingface.co/BM-K/KoSimCSE-bert-multitask)                                   |
| 17  | **BM-K/KoSimCSE-roberta-multitask**                    | 56.32   | 58.31  | 48.47  | 68.66     | 57.94   | [:paperclip:](https://huggingface.co/BM-K/KoSimCSE-roberta-multitask)                                |
| 18  | **OpenAI/text-embedding-3-small**                      | 56.33   | 59.75  | 49.64  | 65.53     | 57.81   | [:paperclip:](https://platform.openai.com/docs/guides/embeddings/embedding-models)                   |
| 19  | **sentence-transformers/paraphrase-multilingual-mpnet-base-v2** | 53.03   | 54.49  | 46.52  | 63.25     | 54.32   | [:paperclip:](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2)    |
| 20  | **sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2** | 45.90   | 46.90  | 39.26  | 57.04     | 47.28   | [:paperclip:](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)    |
| 21  | **kakaobank/kf-deberta-base**                          | 41.25   | 43.82  | 33.45  | 53.42     | 42.99   | [:paperclip:](https://huggingface.co/kakaobank/kf-deberta-base)                                      |

## Todo
- Website 제작
- PR 가이드라인 제작
- ~~Cohere, Upstage, Voyage 결과 추가~~
- 벤치마크용 데이터셋 추가


