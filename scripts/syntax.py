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
    
    return counter.most_common()


def pos_seq_freq_sents(article_content):
    pos_seq_freq_sents = defaultdict(int)

    for doc in article_content:
        for sent in doc.sents:
            pos_seq = []
            for token in sent:
                pos_seq.append(token.pos_)
            pos_seq_freq_sents[" ".join(pos_seq)] += 1
    
    counter = Counter(pos_seq_freq_sents)

    return counter.most_common()


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

    return counter.most_common()


def end_POS_tags(all_sentences):
    end_pos_dict = defaultdict(int)

    for sentence in all_sentences:
        last_words = sentence[-4:-1]
        last_words_pos_tags = tuple([word.pos_ for word in last_words])

        end_pos_dict[last_words_pos_tags] += 1

        counter = Counter(end_pos_dict)

    return counter.most_common()


def sentence_lengths(article_content):
    sentence_lengths_dict = defaultdict(int)

    for doc in article_content:
        for sent in doc.sents:
            sentence_length = len(sent)
            sentence_lengths_dict[sentence_length] += 1
    
    
    counter = Counter(sentence_lengths_dict)

    return counter.most_common()


def average_sentence_length(article_content):
    sentences_lengths = []
    
    for doc in article_content:
        for sent in doc.sents:
            sentences_lengths.append(len(sent))

    average_sentence_length = sum(sentences_lengths) / len(sentences_lengths)

    return average_sentence_length


def dep_tag_frequency(article_content):
    #dep tag frequency 
    dep_tag_frequency = defaultdict(int)
    
    for doc in article_content:
        for token in doc:
            dep_tag_frequency[token.dep_] += 1
    
    counter = Counter(dep_tag_frequency)
    
    return counter.most_common()


def find_percentage(freq_list):
    total_tokens = 0
    percentage_dict = {}

    for key, value in freq_list:
        total_tokens += value

    for key, value in freq_list:
        percentage_dict[key] = value / total_tokens
    
    counter = Counter(percentage_dict)

    return counter.most_common()


def main():
    file_path_human = "../data/human.jsonl"
    file_path_ai = "../data/group6.jsonl"
    human_article_content = (get_content(file_path_human))
    ai_article_content = (get_content(file_path_ai))

    print("\n Percentages of POS tag frequency in Human texts:")
    percentage_pos_tag_human = (find_percentage(pos_tag_frequency(human_article_content)))
    print(percentage_pos_tag_human)

    print("\n percentages of POS tag frequency in AI texts:")
    percentage_pos_tag_ai = (find_percentage(pos_tag_frequency(ai_article_content)))
    print(percentage_pos_tag_ai)

    print("\n percentages of DEP tag frequency in human texts:")
    percentage_dep_freq_human = (find_percentage(dep_tag_frequency(human_article_content)))
    print(percentage_dep_freq_human)

    print("\n percentages of DEP tag frequency in AI texts:")
    percentage_dep_freq_ai = (find_percentage(dep_tag_frequency(ai_article_content)))
    print(percentage_dep_freq_ai)

    print("\n percentages of the first 3 beginning POS tags in human texts:")
    percentage_3_pos_beginning_human = find_percentage(begin_POS_tags(display_sentences(human_article_content)))
    print(percentage_3_pos_beginning_human[0:10])

    print("\n percentages of the first 3 beginning POS tags in human texts:")
    percentage_3_pos_beginning_ai = find_percentage(begin_POS_tags(display_sentences(ai_article_content)))
    print(percentage_3_pos_beginning_ai[0:10])

    print("\n percentages of the first 3 beginning POS tags in human texts:")
    percentage_3_pos_end_human = find_percentage(begin_POS_tags(display_sentences(human_article_content)))
    print(percentage_3_pos_end_human[0:10])
    
    print("\n percentages of the first 3 beginning POS tags in AI texts:")
    percentage_3_pos_end_ai = find_percentage(begin_POS_tags(display_sentences(human_article_content)))
    print(percentage_3_pos_end_ai[0:10])


if __name__ == "__main__":
    main()