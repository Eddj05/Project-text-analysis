from syntax import *
from semantic import *
from pragmatic import *

def test_data(score_list):
    # initialize a variable which keeps track of the amount of the score of the text
    # this score will decide which label the text will be given
    test_score = sum(score_list)
    
    print(test_score)

    # if the testscore is positive the label is 'Human', if the testscore is negative the label will be 'AI Generated'
    if test_score < 0:
        label = "AI Generated"
    else:
        label = "Human"

    print(f"label = {label}")


def test_average_length(test_text):
    length_test_score = 0
    # get the average sentence length from syntax.py
    average_sent_length = average_sentence_length(test_text)
    # decide whether this applies to human made or ai generated text.
    if average_sent_length > 27.55:
        length_test_score -= 1
    else:
        length_test_score += 1

    return length_test_score


def test_pos_tags(test_text, human_article_content, ai_article_content):
    test_score = 0
    percentage_pos_tag_human = sorted((find_percentage(pos_tag_frequency(human_article_content))))
    percentage_pos_tag_ai = sorted((find_percentage(pos_tag_frequency(ai_article_content))))
    percentage_pos_tag_test = sorted((find_percentage(pos_tag_frequency(test_text))))

    for test_percentage in percentage_pos_tag_test:
        for human_percentage in percentage_pos_tag_human:
            if test_percentage[0] == human_percentage[0]:
                test_percentage_human = abs(test_percentage[1] - human_percentage[1])
                break
        for ai_percentage in percentage_pos_tag_ai:
            if test_percentage[0] == ai_percentage[0]:
                test_percentage_ai = abs(test_percentage[1] - ai_percentage[1])
                break
        if test_percentage_human < test_percentage_ai:
            test_score += 1
        else:
            test_score -= 1

    return test_score 


def test_3_beginning_pos(test_text, human_article_content, ai_article_content):
    percentage_3_pos_beginning_human = sorted(find_percentage(begin_POS_tags(display_sentences(human_article_content))))
    percentage_3_pos_beginning_ai = sorted(find_percentage(begin_POS_tags(display_sentences(ai_article_content))))
    percentage_3_pos_beginning_test = sorted(find_percentage(begin_POS_tags(display_sentences(test_text))))

    test_score = 0
    for test_percentage in percentage_3_pos_beginning_test:
        for human_percentage in percentage_3_pos_beginning_human:
            if test_percentage[0] == human_percentage[0]:
                test_percentage_human = abs(test_percentage[1] - human_percentage[1])
                break
        for ai_percentage in percentage_3_pos_beginning_ai:
            if test_percentage[0] == ai_percentage[0]:
                test_percentage_ai = abs(test_percentage[1] - ai_percentage[1])
                break
        if test_percentage_human < test_percentage_ai:
            test_score += 1
        else:
            test_score -= 1
    
    return test_score


def test_3_end_pos(test_text, human_article_content, ai_article_content):
    percentage_3_pos_end_human = sorted(find_percentage(end_POS_tags(display_sentences(human_article_content))))
    percentage_3_pos_end_ai = sorted(find_percentage(end_POS_tags(display_sentences(ai_article_content))))
    percentage_3_pos_end_test = sorted(find_percentage(end_POS_tags(display_sentences(test_text))))

    test_score = 0
    for test_percentage in percentage_3_pos_end_test:
        for human_percentage in percentage_3_pos_end_human:
            if test_percentage[0] == human_percentage[0]:
                test_percentage_human = abs(test_percentage[1] - human_percentage[1])
                break
        for ai_percentage in percentage_3_pos_end_ai:
            if test_percentage[0] == ai_percentage[0]:
                test_percentage_ai = abs(test_percentage[1] - ai_percentage[1])
                break
        if test_percentage_human < test_percentage_ai:
            test_score += 1
        else:
            test_score -= 1
    
    return test_score


def test_dep_freq(test_text, human_article_content, ai_article_content):
    percentage_dep_freq_human = sorted((find_percentage(dep_tag_frequency(human_article_content))))
    percentage_dep_freq_ai = sorted((find_percentage(dep_tag_frequency(ai_article_content))))
    percentage_dep_freq_test = sorted(find_percentage(dep_tag_frequency(test_text)))

    test_score = 0
    
    for test_percentage in percentage_dep_freq_test:
        for human_percentage in percentage_dep_freq_human:
            if test_percentage[0] == human_percentage[0]:
                test_percentage_human = abs(test_percentage[1] - human_percentage[1])
                break
        for ai_percentage in percentage_dep_freq_ai:
            if test_percentage[0] == ai_percentage[0]:
                test_percentage_ai = abs(test_percentage[1] - ai_percentage[1])
                break
        if test_percentage_human < test_percentage_ai:
            test_score += 1
        else:
            test_score -= 1 

    return test_score


def test_asent_polarity(test_text, file_path_human, file_path_ai):
    human_article_content_asent = get_content_asent(file_path_human)
    ai_article_content_asent = get_content_asent(file_path_ai)

    nlp = spacy.blank('en')
    nlp.add_pipe('sentencizer')
    nlp.add_pipe('asent_en_v1')

    test_text_asent = [nlp(test_text)]

    human_asent_polarity = get_asent_polarity(human_article_content_asent)
    ai_article_polarity = get_asent_polarity(ai_article_content_asent)
    test_text_polarity = get_asent_polarity(test_text_asent)

    test_human_polarity = abs(test_text_polarity - human_asent_polarity)
    test_ai_polarity = abs(test_text_polarity - ai_article_polarity)

    if test_human_polarity < test_ai_polarity:
        return 5
    else:
        return -5


def main():
    # make a loop to give a label for each independent text in the test data set.
    # Chat-GPT 3.5 generated text
    ai_test_text = [nlp("In a quiet village, a legend spoke of an ancient tree with golden leaves holding time's secrets. One evening, curious Elara ventured into the forest, finding a glowing path to a clearing with a crystal pond and a stone pedestal holding an ancient book. Opening the book, Elara discovered stories of her village's past and future. As dawn broke, she realized she had become the keeper of her village's history and destiny. Returning home, she felt a profound connection to generations past and future, understanding the true magic of the tree lay in its timeless stories.")]
    # Human made text from the bbc
    human_test_text = [nlp("Twenty-five years after bursting on to the scene, it appears rapper Eminem's provocative alter ego Slim Shady may finally be silenced. The antagonistic Slim Shady, with his peroxide-blond hair and everyman blue jeans, stemmed from Eminem's self-described 'white trash' upbringing. In a surprise April announcement teased as a mock murder news report, Eminem revealed that his new album, The Death of Slim Shady (Coup de Grâce), will be released this summer.")]
    file_path_human = "../data/human.jsonl"
    file_path_ai = "../data/group6.jsonl"

    # test data still needs to be given
    file_path_test = None

    human_article_content = get_content(file_path_human)
    ai_article_content = get_content(file_path_ai)

    # testing here with the test texts
    length_test_score = test_average_length(ai_test_text)
    pos_tag_score = test_pos_tags(ai_test_text, human_article_content, ai_article_content)
    beginning_3_pos_score = test_3_beginning_pos(ai_test_text, human_article_content, ai_article_content)
    end_3_pos_score = test_3_end_pos(ai_test_text, human_article_content, ai_article_content)
    dep_frep_score = test_dep_freq(ai_test_text, human_article_content, ai_article_content)
    asent_polarity_score = test_asent_polarity(ai_test_text[0].text, file_path_human, file_path_ai)

    test_list_scores = [length_test_score, pos_tag_score, beginning_3_pos_score, end_3_pos_score, dep_frep_score, asent_polarity_score]
    #human_article_content should be replaced with test_data
    test_data(test_list_scores)

    
if __name__ == "__main__":
    main()