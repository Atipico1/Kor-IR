<h1 align="center">Kor-IR: 한국어 검색을 위한 임베딩 벤치마크</h1>

## Intro

한국어 임베딩 모델의 검색 (Information Retrieval) 성능 비교를 위한 리더보드입니다.
현재 [Ko-StrategyQA](https://huggingface.co/datasets/taeminlee/Ko-StrategyQA) 데이터셋을 사용해 IR 성능을 측정했습니다.

## Leader Board

| Rank | Model                                                      | nDCG@10 | MRR@10 | MAP@10 | Recall@10 | Average |
|------|------------------------------------------------------------|---------|--------|--------|-----------|---------|
| 1    | [intfloat/multilingual-e5-large-instruct](https://huggingface.co/intfloat/multilingual-e5-large-instruct)                    | 80.68   | 82.52  | 76.61  | 85.74     | 81.39   |
| 2    | [intfloat/multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large)                             | 80.35   | 82.01  | 76.37  | 85.4      | 81.03   |
| 3    | [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3)                                                | 79.4    | 81.12  | 75.07  | 85.2      | 80.2    |
| 4    | [intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base)                              | 76.35   | 79.04  | 71.6   | 82.06     | 77.26   |
| 5    | [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small)                             | 75.16   | 77.55  | 69.78  | 82.17     | 76.16   |
| 6    | OpenAI/text-embedding-3-large                                     | 73.74   | 75.7   | 68.47  | 80.99     | 74.73   |
| 7    | [upskyy/kf-deberta-multitask](https://huggingface.co/upskyy/kf-deberta-multitask)                                | 68.42   | 70.14  | 61.64  | 78.71     | 69.73   |
| 8    | [cateto/longformer-ko-sroberta-multitask-23040](https://huggingface.co/cateto/longformer-ko-sroberta-multitask-23040)              | 66.31   | 68.51  | 59.34  | 76.62     | 67.69   |
| 9    | [jhgan/ko-sroberta-multitask](https://huggingface.co/jhgan/ko-sroberta-multitask)                                | 65.1    | 67.46  | 58.03  | 75.41     | 66.5    |
| 10   | [jhgan/ko-sroberta-nli](https://huggingface.co/jhgan/ko-sroberta-nli)                                      | 63.9    | 66.56  | 56.84  | 74.09     | 65.35   |
| 11   | [jhgan/ko-sbert-multitask](https://huggingface.co/jhgan/ko-sbert-multitask)                                   | 62.86   | 65.6   | 55.61  | 73.34     | 64.35   |
| 12   | [BM-K/KoSimCSE-bert-multitask](BM-K/KoSimCSE-bert-multitask)                               | 56.93   | 59.17  | 49.21  | 69.03     | 58.59   |
| 13   | [BM-K/KoSimCSE-roberta-multitask](https://huggingface.co/BM-K/KoSimCSE-roberta-multitask)                            | 56.32   | 58.31  | 48.47  | 68.66     | 57.94   |
| 14   | OpenAI/text-embedding-3-small                                     | 56.33   | 59.75  | 49.64  | 65.53     | 57.81   |
| 15   | [sentence-transformers/paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2) | 53.03   | 54.49  | 46.52  | 63.25     | 54.32   |
| 16   | [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) | 45.9    | 46.9   | 39.26  | 57.04     | 47.28   |
| 17   | [kakaobank/kf-deberta-base](https://huggingface.co/kakaobank/kf-deberta-base)                                  | 41.25   | 43.82  | 33.45  | 53.42     | 42.99   |

## Todo
- Website 제작
- PR 가이드라인 제작
- Cohere, Upstage, Voyage 결과 추가
- 벤치마크용 데이터셋 추가


