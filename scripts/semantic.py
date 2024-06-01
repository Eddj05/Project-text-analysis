import json
import spacy
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('punkt')

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

def wordnet_synsets(article_content):
    for text in article_content:
        doc = nlp(text)
        for token in doc:
            synsets = wn.synsets(token.text)
            for synset in synsets:
                print(f"Word: {token.text}")
                print(f"Synset: {synset.name()}")
                print(f"Definition: {synset.definition()}")
                print("----")

def lesk(context_sentence, ambiguous_word, pos=None):
    """
    Returns the most likely sense of an ambiguous word in a given context sentence.

    Parameters:
    context_sentence (str): The sentence containing the ambiguous word.
    ambiguous_word (str): The word to disambiguate.
    pos (str, optional): The part of speech of the ambiguous word. If not provided, all senses will be considered.

    Returns:
    synset: The most likely sense of the ambiguous word in the given context.
    """
    
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

def named_entity_recognition(sentence):
    doc = nlp(sentence)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

def co_reference_resolution(text):
    # Process the text using spaCy
    doc = nlp(text)
    # Extract the co-references
    co_references = []
    for cluster in doc._.coref_clusters:
        co_references.append((cluster.main.text, [mention.text for mention in cluster.mentions]))
    return co_references

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
    for sentence in human_article_content:
        entities_human = named_entity_recognition(sentence)
        print(entities_human)

    print("\nNamed Entity Recognition ai texts:")
    for sentence in ai_article_content:
        entities_ai = named_entity_recognition(sentence)
        print(entities_ai)

    print("\nCo-reference resolution human texts:")
    for text in human_article_content:
        co_references_human = co_reference_resolution(text)
        print(co_references_human)
    
    print("\nCo-reference resolution ai texts:")
    for text in ai_article_content:
        co_references_ai = co_reference_resolution(text)
        print(co_references_ai)

if __name__ == "__main__":
    main()
