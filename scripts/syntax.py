import json
import spacy
from collections import defaultdict, Counter


# Load spaCy model
nlp = spacy.load("en_core_web_sm")


def get_content(file_path):
    """
    This function reads a json file where each line is an object. The function extracts
    the 'text' field to get the content of each article. The function returns a list of
    all the collected texts.

    By Edwin
    """

    # initialize a list to store the articles
    article_content = []
    # open the file
    with open(file_path, "r", encoding="utf-8") as file:
        # iterate over the lines
        for line in file:
            # parse the json object for each line
            article = json.loads(line)
            # extract the text field from the file
            text = article.get('text', '')
            # check if the field is not empty
            if text:
                # process the text using nlp
                article_content.append(nlp(text))

    return article_content


def pos_tag_frequency(article_content):
    """
    This function takes a list of processed texts. Each token in this text will
    receive a pos tag. The function return a default dictionary with the frequency
    of each pos tag across all the texts

    By Edwin
    """

    # initialize a defaultdict to count the pos tags
    pos_tag_frequency = defaultdict(int)

    for doc in article_content:
        for token in doc:
            # count the token's POS tags
            pos_tag_frequency[token.pos_] += 1

    # convert the defaultdict into a counter
    counter = Counter(pos_tag_frequency)

    # return a sorted counter
    return counter.most_common()


def pos_seq_freq_chunks(article_content):
    """
    This function takes a list of processed texts. Each token in this text will
    receive a pos tag. The function return a default dictionary with the frequency
    of each pos tag across all noun chunks within the texts

    By Kennie
    """

    # initialize a defaultdict to count pos tag sequences
    pos_seq_freq = defaultdict(int)

    for doc in article_content:
        for chunk in doc.noun_chunks:
            # initialize a list to store the sequences
            pos_sequence = []
            # iterate over the tokens in the chunks
            for token in chunk:
                # add the pos tags to the sequence
                pos_sequence.append(token.pos_)
            # join the pos tags into a string and count
            pos_seq_freq[" ".join(pos_sequence)] += 1

    # convert the defaultdict into a counter
    counter = Counter(pos_seq_freq)

    # return a sorted counter
    return counter.most_common()


def pos_seq_freq_sents(article_content):
    """
    This function takes a list of processed texts. Each token in this text will
    receive a pos tag. The function return a default dictionary with the frequency
    of each pos tag across all sentences within the texts

    By Kennie
    """

    # initialize a defaultdict to count pos tag sequences
    pos_seq_freq_sents = defaultdict(int)

    for doc in article_content:
        for sent in doc.sents:
            # initialize a list to store the sequences
            pos_seq = []
            for token in sent:
                # add the pos tags to the sequence
                pos_seq.append(token.pos_)
            # join the pos tags into a string and count
            pos_seq_freq_sents[" ".join(pos_seq)] += 1

    # convert the defaultdict into a counter
    counter = Counter(pos_seq_freq_sents)

    # return a sorted counter
    return counter.most_common()


def display_sentences(article_content):
    """
    This function takes a list of processed texts. It extracts each sentence
    from each text, collects the tokens for each sentence. the function
    returns a list of sentences where each sentence is represented as a list
    of tokens.

    by Edwin
    """

    # initialize a list to store all the sentences.
    all_sentences = []

    for doc in article_content:
        for sent in doc.sents:
            # initialize a list to store the tokens
            tokens = []
            for token in sent:
                # add the tokens
                tokens.append(token)
            # add a list of tokens to the sentences list
            all_sentences.append(tokens)

    return all_sentences


def begin_POS_tags(all_sentences):
    """
    This function takes a list of sentences. It extracts the POS tags of the first
    three tokens in each sentence, counts the frequency of each unique POS tag sequence.
    The function returns the most common sequences.

    by Edwin
    """

    # initialize a defaultdict to count the frequencies of the sequences
    begin_pos_dict = defaultdict(int)

    # iterate over the sentences
    for sentence in all_sentences:
        # find the first three words
        first_words = sentence[0:3]
        # make a tuple with pos tags for the first three tokens
        first_words_pos_tags = tuple([word.pos_ for word in first_words])
        # count the sequences
        begin_pos_dict[first_words_pos_tags] += 1

        # convert the defaultdict into a counter
        counter = Counter(begin_pos_dict)

    # return a sorted counter
    return counter.most_common()


def end_POS_tags(all_sentences):
    """
    This function takes a list of sentences. It extracts the POS tags of the last
    three tokens in each sentence, counts the frequency of each unique POS tag sequence.
    The function returns the most common sequences.

    by Edwin
    """

    # initialize a defaultdict to count the frequencies of the sequences
    end_pos_dict = defaultdict(int)

    # iterate over the sentences
    for sentence in all_sentences:
        # find the last three words
        last_words = sentence[-4:-1]
        # make a tuple with pos tags for the first three tokens
        last_words_pos_tags = tuple([word.pos_ for word in last_words])
        # count the sequences
        end_pos_dict[last_words_pos_tags] += 1

        # convert the defaultdict into a counter
        counter = Counter(end_pos_dict)

    # return a sorted counter
    return counter.most_common()


def sentence_lengths(article_content):
    """
    This function takes a list of processed text documents. It calculates the length of each
    sentence, counts the frequency of each unique sentence length. It returns the most common
    sentence lengths.

    by Kennie
    """

    # initialize a default dict to count the frequencies of lengths
    sentence_lengths_dict = defaultdict(int)

    for doc in article_content:
        for sent in doc.sents:
            # calculate the length of the sentence
            sentence_length = len(sent)
            # count the length in the dictionary
            sentence_lengths_dict[sentence_length] += 1

    # convert the defaultdict into a counter
    counter = Counter(sentence_lengths_dict)

    # return a sorted counter
    return counter.most_common()


def average_sentence_length(article_content):
    """
    This function takes a list of processed texts. It calculates the length of each
    sentence, computes the average sentence length, and returns this average.

    by Kennie
    """

    # initialize a variable to store the lenghts of the sentences
    sentences_lengths = []

    for doc in article_content:
        for sent in doc.sents:
            # add the lengths to the list
            sentences_lengths.append(len(sent))

    # calculate the average length
    average_sentence_length = sum(sentences_lengths) / len(sentences_lengths)

    return average_sentence_length


def dep_tag_frequency(article_content):
    """
    This function takes a list of processed texts. Each token in this text will
    receive a dep tag. The function return a default dictionary with the frequency
    of each dep tag across all the texts

    By Kennie
    """
    # initialize a defaultdict to count the pos tags
    dep_tag_frequency = defaultdict(int)

    for doc in article_content:
        for token in doc:
            # count the token's POS tags
            dep_tag_frequency[token.dep_] += 1

    # convert the defaultdict into a counter
    counter = Counter(dep_tag_frequency)

    # return a sorted counter
    return counter.most_common()


def find_percentage(freq_list):
    """
    This function takes a list of tuples where each tuple contains an item and its frequency.
    It calculates the percentage of occurrences for each item in the list, and returns a list
    of tuples where each tuple contains an item and its corresponding percentage, sorted by
    percentage.

    by Kennie & Edwin
    """

    # initialize a variable to store the total number of tokens
    total_tokens = 0
    # initialize a dictionary to store percentages for each item
    percentage_dict = {}

    # iterate over each tuple
    for key, value in freq_list:
        # add the frequency value to the total amount of tokens
        total_tokens += value

    # iterate over each tuple again
    for key, value in freq_list:
        # calculate the percentage of occurances for the current item based of the total amount of tokens
        percentage_dict[key] = value / total_tokens

    # convert the dictionary into a counter
    counter = Counter(percentage_dict)

    # return a sorted counter
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
