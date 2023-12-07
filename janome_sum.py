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
text = """かつて海と山に囲まれた小さな町、青葉町は、緑豊かな自然と歴史的な建造物で知られています。町の中心には、古くからの商店街が広がり、地元の人々と観光客でにぎわっています。店々は伝統的な和菓子、地元産の新鮮な野菜、手作りの陶器など、多様な商品を提供しており、訪れる人々を楽しませています。

町の北部には、美しい青葉山がそびえ立ち、春には桜が咲き乱れ、秋には紅葉が山を彩ります。山頂には、古い城跡があり、そこからは町全体を一望できる絶景が広がっています。かつてこの地を治めていた武士の歴史に思いをはせながら、多くのハイキング愛好家や歴史愛好家が訪れます。

また、町の南部には、青葉町を代表する美しい海岸線があります。夏には、透明度の高い海水と白い砂浜が人々を引きつけ、海水浴やサーフィンを楽しむ人々で賑わいます。海岸近くの小さな漁港では、新鮮な魚介類が豊富に水揚げされ、町の食文化を支えています。

青葉町のもう一つの魅力は、年間を通じて開催される伝統的な祭りです。春には、花見を楽しむ「青葉祭り」が開催され、夏には海岸での「灯籠祭り」が人々を魅了します。秋には収穫を祝う「秋祭り」、冬には雪を楽しむ「雪まつり」があり、それぞれの季節の風物詩となっています。

このように青葉町は、四季折々の自然美と伝統文化が息づく場所です。訪れる人々には、町の歴史を感じることができ、また地元の人々の温かなもてなしに触れることができます。青葉町は、忙しい日常を離れ、心を癒す特別な場所として多くの人々に愛されています。"""

# 要約の実行
summary = summarize_text_japanese(text)
print(summary)

### 出力：青葉町は、忙しい日常を離れ、心を癒す特別な場所として多くの人々に愛されています。かつて海と山に囲まれた小さな町、青葉町は、緑豊かな自然と歴史的な建造物で知られています。店々は伝統的な和菓子、地元産の新鮮な野菜、手作りの陶器など、多様な商品を提供しており、訪れる人々を楽しませています
