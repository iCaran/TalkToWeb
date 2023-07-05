from transformers import BartTokenizer, BartForConditionalGeneration
from extractor import getPost

tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

def summarize_article(url, max_length=512):
    article_text, title = getPost(url)

    # Tokenize the article
    inputs = tokenizer([article_text], max_length=max_length, truncation=True, return_tensors='pt')

    # Generate the summary
    summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=max_length, early_stopping=True)

    # Decode the summary tokens
    summary = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)

    return summary, title
