from transformers import T5Tokenizer, AutoModelForSeq2SeqLM
import re
from janome.tokenizer import Tokenizer

# 前処理関数
def preprocess_japanese_text(text):
    text = normalize_text(text)
    text = remove_special_characters(text)
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text, wakati=True)
    processed_text = ' '.join(tokens)
    return processed_text

def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[！？。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～]', '', text)
    text = re.sub(r'[!?"#$%&\'()*+,-./:;<=>@[\]^_`{|}~]', '', text)
    return text

def remove_special_characters(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

# 要約関数
def summarize_japanese_text(text, model_name="sonoisa/t5-base-japanese", max_length=150):
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    prefixed_text = "要約: " + text
    inputs = tokenizer.encode(prefixed_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=max_length, num_beams=3, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary

# 例文
text = """かつて海と山に囲まれた小さな町、青葉町は、緑豊かな自然と歴史的な建造物で知られています。町の中心には、古くからの商店街が広がり、地元の人々と観光客でにぎわっています。店々は伝統的な和菓子、地元産の新鮮な野菜、手作りの陶器など、多様な商品を提供しており、訪れる人々を楽しませています。

町の北部には、美しい青葉山がそびえ立ち、春には桜が咲き乱れ、秋には紅葉が山を彩ります。山頂には、古い城跡があり、そこからは町全体を一望できる絶景が広がっています。かつてこの地を治めていた武士の歴史に思いをはせながら、多くのハイキング愛好家や歴史愛好家が訪れます。

また、町の南部には、青葉町を代表する美しい海岸線があります。夏には、透明度の高い海水と白い砂浜が人々を引きつけ、海水浴やサーフィンを楽しむ人々で賑わいます。海岸近くの小さな漁港では、新鮮な魚介類が豊富に水揚げされ、町の食文化を支えています。

青葉町のもう一つの魅力は、年間を通じて開催される伝統的な祭りです。春には、花見を楽しむ「青葉祭り」が開催され、夏には海岸での「灯籠祭り」が人々を魅了します。秋には収穫を祝う「秋祭り」、冬には雪を楽しむ「雪まつり」があり、それぞれの季節の風物詩となっています。

このように青葉町は、四季折々の自然美と伝統文化が息づく場所です。訪れる人々には、町の歴史を感じることができ、また地元の人々の温かなもてなしに触れることができます。青葉町は、忙しい日常を離れ、心を癒す特別な場所として多くの人々に愛されています。"""

# 前処理実行
processed_text = preprocess_japanese_text(text)

# 要約実行
summary = summarize_japanese_text(processed_text)
print(summary)

### 出力：町 の 魅力 は 歴史 を 愛好 家 や ハイキング 愛好 家 や ハイキング 愛好 家 や 歴史 愛好 家 や 歴史 愛好 家 や 歴史 愛好 家 や 歴史 愛好 家 や 歴史 愛好 家 や 歴史 愛好 家 や 愛好 家 や  ます町
