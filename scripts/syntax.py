import json
import spacy
from collections import defaultdict, Counter
import time


# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def get_content(file_path):
    article_content = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            article = json.loads(line)
            text = article.get('text', '')  
            if text: 
                article_content.append(nlp(text))

    return article_content

def pos_tag_frequency(article_content):
    #pos tag frequency 
    pos_tag_frequency = defaultdict(int)
    
    for doc in article_content:
        for token in doc:
            pos_tag_frequency[token.pos_] += 1
    
    counter = Counter(pos_tag_frequency)
    
    return counter.most_common()

def pos_seq_freq_chunks(article_content):
    pos_seq_freq = defaultdict(int)

    for doc in article_content:
        for chunk in doc.noun_chunks:
            pos_sequence = []
            for token in chunk:
                pos_sequence.append(token.pos_)
            pos_seq_freq[" ".join(pos_sequence)] += 1
    
    counter = Counter(pos_seq_freq)
    
    return counter.most_common(10)

def pos_seq_freq_sents(article_content):
    pos_seq_freq_sents = defaultdict(int)

    for doc in article_content:
        for sent in doc.sents:
            pos_seq = []
            for token in sent:
                pos_seq.append(token.pos_)
            pos_seq_freq_sents[" ".join(pos_seq)] += 1
    
    counter = Counter(pos_seq_freq_sents)

    return counter.most_common(10)

def main():
    start_time = time.time()
    file_path_human = "../data/human.jsonl"
    file_path_ai = "../data/group6.jsonl"
    human_article_content = (get_content(file_path_human))
    ai_article_content = (get_content(file_path_ai))

    print('POS Tag frequency - human content:')
    print(pos_tag_frequency(human_article_content))

    
    print('\nPOS Tag frequency - ai content:')
    print(pos_tag_frequency(ai_article_content))

    human_pos_seq_freq = pos_seq_freq_chunks(human_article_content)
    print("\nHuman POS tag sequences in chunks:")
    print(human_pos_seq_freq)

    ai_pos_seq_freq = pos_seq_freq_chunks(ai_article_content)
    print("\nAI POS tag sequences in chunks:")
    print(ai_pos_seq_freq)

    human_pos_seq_freq_sents = pos_seq_freq_sents(human_article_content)
    print("\nmost common Human POS tag sequences in sentences:")
    print(human_pos_seq_freq_sents)

    ai_pos_seq_freq_sents = pos_seq_freq_sents(ai_article_content)
    print("\nMost commong AI POS tag sequences in sentences:")
    print(ai_pos_seq_freq_sents)

    end_time = time.time()
    print(f"total time taken: {end_time - start_time}")

if __name__ == "__main__":
    main()