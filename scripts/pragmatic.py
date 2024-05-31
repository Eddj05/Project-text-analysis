import json
import spacy
import asent
from spacytextblob.spacytextblob import SpacyTextBlob

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')


def get_content(file_path):
    article_content = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            article = json.loads(line)
            text = article.get('text', '')  
            if text: 
                article_content.append(nlp(text))

    return article_content

def get_content_asent(file_path):
    article_content = []
    
    nlp = spacy.blank('en')
    nlp.add_pipe('sentencizer')
    nlp.add_pipe('asent_en_v1')

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            article = json.loads(line)
            text = article.get('text', '')  
            if text: 
                article_content.append(nlp(text))
    return article_content

def get_asent_polarity(article_content):
    return [doc._.polarity for doc in article_content]

def get_blob_polarity(article_content):
    for doc in article_content:
        return doc._.blob.polarity

def get_subjectivity(article_content):
    for doc in article_content:
        return doc._.blob.subjectivity

def get_assesments(article_content):
    for doc in article_content:
        return doc._.blob.sentiment_assessments.assessments

def main():
    file_path_human = "../data/human.jsonl"
    file_path_ai = "../data/group6.jsonl"

    human_article_content = (get_content(file_path_human))
    ai_article_content = (get_content(file_path_ai))

    human_article_content_asent = (get_content_asent(file_path_human))
    ai_article_content_asent = (get_content_asent(file_path_ai))

    human_polarity_asent = get_asent_polarity(human_article_content_asent)
    ai_polarity_asent = get_asent_polarity(ai_article_content_asent)

    print("Human Article Sentiment Polarity:", human_polarity_asent)
    print("AI Article Sentiment Polarity:", ai_polarity_asent)

    human_polarity = get_blob_polarity(human_article_content)
    ai_polarity = get_blob_polarity(ai_article_content)

    print("Human Article Sentiment Polarity:", human_polarity)
    print("AI Article Sentiment Polarity:", ai_polarity)
    
    human_subjectivity = get_subjectivity(human_article_content)
    ai_subjectivity = get_subjectivity(ai_article_content)

    print("Human Article Sentiment subjectivity:", human_subjectivity)
    print("AI Article Sentiment subjectivity:", ai_subjectivity)

    human_assesments = get_assesments(human_article_content)
    ai_assesments = get_assesments(ai_article_content)

    print("Human Article Sentiment assesments:", human_assesments)
    print("AI Article Sentiment assesments:", ai_assesments)

if __name__ == "__main__":
    main()