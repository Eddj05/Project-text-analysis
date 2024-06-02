import json
import spacy
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from fastcoref import spacy_component
from collections import defaultdict, Counter

nltk.download('wordnet')
nltk.download('punkt')

# Load SpaCy model and add fastcoref
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("fastcoref")

def get_content(file_path):
    article_content = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            article = json.loads(line)
            text = article.get('text', '')  
            if text: 
                article_content.append(text)
    return article_content

def wordnet_synsets(article_content, num_words=20):
    word_count = 0
    for text in article_content:
        doc = nlp(text)
        for token in doc:
            if token.is_alpha:  
                if word_count < num_words:
                    synsets = wn.synsets(token.text)
                    if synsets:
                        synset = synsets[0]  
                        print(f"Word: {token.text}")
                        print(f"Synset: {synset.name()}")
                        print(f"Definition: {synset.definition()}")
                        print("----")
                    word_count += 1
                else:
                    break
        if word_count >= num_words:
            break

def lesk(context_sentence, ambiguous_word, pos=None):
    tokens = word_tokenize(context_sentence)
    
    if pos is None:
        synsets = wn.synsets(ambiguous_word)
    else:
        synsets = wn.synsets(ambiguous_word, pos)
    
    max_overlap_score = -1
    best_synset = None
    
    for synset in synsets:
        overlap_score = 0
        synset_signature = set(word_tokenize(synset.definition()))
        for example in synset.examples():
            synset_signature.update(word_tokenize(example))
        
        context = set(tokens)
        overlap = len(context.intersection(synset_signature))
        
        if overlap > max_overlap_score:
            max_overlap_score = overlap
            best_synset = synset

    return best_synset

def count_ambiguous_words(article_content):
    lemma_counts_list = []

    for doc in article_content:
        lemma_counts = defaultdict(int)
        for token in doc:
            if not token.is_stop and not token.is_punct:
                lemma_counts[token.lemma_] += 1
        lemma_counts_list.append(lemma_counts)

    return lemma_counts_list

def named_entity_rec(article_content):
    entity_freq = defaultdict(int)

    for doc in article_content:
        for entity in doc.ents:
            entity_freq[entity.label_] += 1

    counter = Counter(entity_freq)

    return counter.most_common()

def named_entity_recognition(article_content, num_entities=20):
    entity_count = 0
    for text in article_content:
        doc = nlp(text)
        for entity in doc.ents:
            if entity_count < num_entities:
                print(f"Entity: {entity.text}")
                print(f"Label: {entity.label_}")
                print("----")
                entity_count += 1
            else:
                break
        if entity_count >= num_entities:
            break

def co_reference_resolution(article_content, num_co_references=20):
    co_reference_count = 0
    for text in article_content:
        doc = nlp(text)
        if hasattr(doc._, 'coref_clusters'):
            for cluster in doc._.coref_clusters:
                if co_reference_count < num_co_references:
                    mentions = [(text[span[0]:span[1]], span) for span in cluster]
                    print(f"Main: {mentions[0][0]}")
                    print(f"Mentions: {[mention[0] for mention in mentions[1:]]}")
                    print("----")
                    co_reference_count += 1
                else:
                    break
        if co_reference_count >= num_co_references:
            break

def main():
    file_path_human = "../data/human.jsonl"
    file_path_ai = "../data/group6.jsonl"
    human_article_content = get_content(file_path_human)
    ai_article_content = get_content(file_path_ai)

    print("\nWordnet synsets human texts:")
    wordnet_synsets(human_article_content)

    print("\nWordnet synsets ai texts:")
    wordnet_synsets(ai_article_content)

    print("\nNamed Entity Recognition human texts:")
    named_entity_recognition(human_article_content)

    print("\nNamed Entity Recognition ai texts:")
    named_entity_recognition(ai_article_content)

    print("\nCo-reference resolution human texts:")
    co_reference_resolution(human_article_content)
    
    print("\nCo-reference resolution ai texts:")
    co_reference_resolution(ai_article_content)

    print(named_entity_rec(human_article_content))
    print(named_entity_rec(ai_article_content))

if __name__ == "__main__":
    main()
