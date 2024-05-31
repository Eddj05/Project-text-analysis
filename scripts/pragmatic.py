import json
import spacy
import asent
from spacytextblob.spacytextblob import SpacyTextBlob

# Load spaCy models
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
    total_compound = 0
    total_docs = 0
    average_compound = 0

    for doc in article_content:
        total_docs += 1
        polarity = doc._.polarity
        total_compound += polarity.compound

    average_compound = total_compound / total_docs
    return average_compound

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

    print("\nAverage human Article Sentiment Polarity (asent):", human_polarity_asent)
    print("Average AI Article Sentiment Polarity (asent):", ai_polarity_asent)

    human_polarity = get_blob_polarity(human_article_content)
    ai_polarity = get_blob_polarity(ai_article_content)

    print("\nHuman Article Sentiment Polarity (blob):", human_polarity)
    print("AI Article Sentiment Polarity (blob):", ai_polarity)
    
    human_subjectivity = get_subjectivity(human_article_content)
    ai_subjectivity = get_subjectivity(ai_article_content)

    print("\nHuman Article Sentiment subjectivity (blob):", human_subjectivity)
    print("AI Article Sentiment subjectivity (blob):", ai_subjectivity)

    human_assesments = get_assesments(human_article_content)
    ai_assesments = get_assesments(ai_article_content)

    print("\nHuman Article Sentiment assesments:", human_assesments)
    print("AI Article Sentiment assesments:", ai_assesments) 

    human_assessment_counts = {}
    for assessment in human_assesments:
        assessment_text = assessment[0][0]
        if assessment_text not in human_assessment_counts:
            human_assessment_counts[assessment_text] = 0
        human_assessment_counts[assessment_text] += 1

    ai_assessment_counts = {}
    for assessment in ai_assesments:
        assessment_text = assessment[0][0]
        if assessment_text not in ai_assessment_counts:
            ai_assessment_counts[assessment_text] = 0
        ai_assessment_counts[assessment_text] += 1

    sorted_human_assessment_counts = dict(sorted(human_assessment_counts.items(), key = lambda item: item[1], reverse=True))
    sorted_ai_assessment_counts = dict(sorted(ai_assessment_counts.items(), key = lambda item: item[1], reverse=True))

    print("\nHuman Article Sentiment Assessment Frequencies:")
    for assessment, count in sorted_human_assessment_counts.items():
        print(assessment, ":", count)

    print("\nAI Article Sentiment Assessment Frequencies:")
    for assessment, count in sorted_ai_assessment_counts.items():
        print(assessment, ":", count)


if __name__ == "__main__":
    main()