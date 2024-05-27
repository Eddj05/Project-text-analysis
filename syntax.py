import json
import spacy
from collections import defaultdict, Counter

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def get_content(file_path):
    article_content = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            article = json.loads(line)
            text = article.get('text', '')  
            if text: 
                article_content.append(text)

    return article_content

def pos_tag_frequency(article_content):
    #pos tag frequency 
    pos_tag_frequency = defaultdict(int)
    
    for text in article_content:
        doc = nlp(text)
        for token in doc:
            pos_tag_frequency[token.pos_] += 1
    
    counter = Counter(pos_tag_frequency)
    
    return counter.most_common()

def main():
    file_path_human = "human.jsonl"
    file_path_ai = "group6.jsonl"
    human_article_content = (get_content(file_path_human))
    print('POS Tag frequency - human content:')
    print(pos_tag_frequency(human_article_content))

    ai_article_content = (get_content(file_path_ai))
    print('\nPOS Tag frequency - ai content:')
    print(pos_tag_frequency(ai_article_content))

if __name__ == "__main__":
    main()