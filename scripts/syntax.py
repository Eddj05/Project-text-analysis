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


def display_sentences(article_content):
    all_sentences = []

    for doc in article_content:
        for sent in doc.sents:
            tokens = []
            for token in sent:
                tokens.append(token)
            all_sentences.append(tokens)

    return all_sentences


def begin_POS_tags(all_sentences):
    begin_pos_dict = defaultdict(int)

    for sentence in all_sentences:
        first_words = sentence[0:3]
        first_words_pos_tags = tuple([word.pos_ for word in first_words])

        begin_pos_dict[first_words_pos_tags] += 1

        counter = Counter(begin_pos_dict)

    return counter.most_common(10)


def end_POS_tags(all_sentences):
    end_pos_dict = defaultdict(int)

    for sentence in all_sentences:
        last_words = sentence[-4:-1]
        last_words_pos_tags = tuple([word.pos_ for word in last_words])

        end_pos_dict[last_words_pos_tags] += 1

        counter = Counter(end_pos_dict)

    return counter.most_common(10)


def sentence_lengths(article_content):
    sentence_lengths_dict = defaultdict(int)

    for doc in article_content:
        for sent in doc.sents:
            sentence_length = len(sent)
            sentence_lengths_dict[sentence_length] += 1
    
    
    counter = Counter(sentence_lengths_dict)

    return counter.most_common()


def average_sentence_length(article_content):
    total_words = 0
    total_sentences = 0

    for doc in article_content:
        for sent in doc.sents:
            total_words += len(sent)
            total_sentences += 1

    average_sentence_length = total_words / total_sentences

    return average_sentence_length


def main():
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
    print("\nMost common AI POS tag sequences in sentences:")
    print(ai_pos_seq_freq_sents)

    print("\nMost common first 3 POS tags in human sentences")
    print(begin_POS_tags(display_sentences(human_article_content)))

    print("\nMost common first 3 POS tags in AI sentences")
    print(begin_POS_tags(display_sentences(ai_article_content)))

    print("\nMost common last 3 POS tags in human sentences")
    print(end_POS_tags(display_sentences(human_article_content)))

    print("\nMost common last 3 POS tags in AI sentences")
    print(end_POS_tags(display_sentences(ai_article_content)))

    print("\n Sentence lengths of Humans:")
    print(sentence_lengths(human_article_content))
    print(f"average sentence length: {average_sentence_length(human_article_content)}")

    print("\n Sentence lengths of AI:")
    print(sentence_lengths(ai_article_content))
    print(f"average sentence length: {average_sentence_length(ai_article_content)}")


if __name__ == "__main__":
    main()