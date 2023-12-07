from janome.tokenizer import Tokenizer
from collections import defaultdict
from heapq import nlargest

def summarize_text_japanese(text, num_sentences=3):
    # Janome形態素解析器の初期化
    tokenizer = Tokenizer()

    # 単語の出現頻度をカウント
    freq_table = defaultdict(int)
    for token in tokenizer.tokenize(text):
        if token.part_of_speech.startswith('名詞') or token.part_of_speech.startswith('動詞') or token.part_of_speech.startswith('形容詞'):
            freq_table[token.surface] += 1

    # 文を分割して、各文の重要度をスコアリング
    sentences = text.split('。')
    sentence_value = defaultdict(int)
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence:
                sentence_value[sentence] += freq

    # 最も重要な文を取得
    summary_sentences = nlargest(num_sentences, sentence_value, key=sentence_value.get)

    # 要約を組み立てる
    summary = '。'.join(summary_sentences)
    return summary

# テキストの例
text = """
    Pythonは、解釈型の高水準汎用プログラミング言語である。グイド・ヴァンロッサムによって開発され、
    1991年に初版がリリースされた。Pythonのデザイン哲学は、コードの可読性に重点を置いており、
    その顕著な空白の使用法は注目に値する。言語構造とオブジェクト指向のアプローチは、
    プログラマーが小規模から大規模プロジェクトまで、明瞭で論理的なコードを書くことを目指している。
    """

# 要約の実行
summary = summarize_text_japanese(text)
print(summary)
