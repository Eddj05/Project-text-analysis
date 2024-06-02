from syntax import *
from semantic import *
from pragmatic import *

def test_data(score_list):
    """
    Returns if the text is AI-Generated text or Human Generated

    Parameters:
    score_list (list): a list of integers with scores of each test function

    Returns:
    label (str): Human Generated or AI-Generated

    Made By: Edwin
    """
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


def find_percentage_ambiguity(ambiguity_list):
    """
    Returns a average percentage of how many of the words are ambiguous in the multiple texts

    Parameters:
    ambiguity_list (list): a list of dictionaries with a value needing to be integers

    Returns:
    average_percentage (float): an average of how many of the words are ambiguous in the texts

    Made by: Kennie
    """
    total_percentages = []

    for dictionary in ambiguity_list:
        total_count = sum([count for count in dictionary.values()])
        ambiguity_count = sum([count for count in dictionary.values() if count > 1])
        ambiguity_percentage = ambiguity_count / total_count
        total_percentages.append(ambiguity_percentage)
    
    average_percentage = sum(total_percentages) / len(total_percentages)

    return average_percentage

def test_average_length(test_text):
    """
    Returns a test score given a test text and checking if the
    average sentence length is more likely to be AI or Human generated

    Parameters:
    test_text (list): a list containing doc variables (doc = nlp(text))

    Returns:
    test_score (int): returning a score based on the test text given whether it is more likely to be 
    AI or Human 
    
    Made by: Edwin
    """
    length_test_score = 0
    # get the average sentence length from syntax.py
    average_sent_length = average_sentence_length(test_text)
    # decide whether this applies to human made or ai generated text.
    if average_sent_length > 27.55:
        # -1 for more likely to be AI
        length_test_score -= 1
    else:
        # +1 for more likely to be human generated
        length_test_score += 1

    return length_test_score


def test_pos_tags(test_text, human_article_content, ai_article_content):
    """
    Returns a test score based on whether the test text is more likely to be AI or Human generated
    based on the frequency of POS tags and checking it with average human frequency of POS tags and 
    average AI frequency of POS tags

    Parameters:
    test_text (list): a list of doc variable containing the test_text
    human_article_content (list): list of doc variables containing human texts
    ai_article_content (list): list of doc variables containing AI generated texts

    Returns:
    test_score (int): returns a test score whether frequency of pos tags is more likely to be
    AI or human generated

    Made by: Edwin
    """
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
        # check whether the test percentage is closer to the percentage of 
        # the percentage of human or ai     
        if test_percentage_human < test_percentage_ai:
            test_score += 1
        else:
            test_score -= 1

    return test_score 


def test_3_beginning_pos(test_text, human_article_content, ai_article_content):
    """
    Returns a test score number based on whether the test text where the 3 beginning POS tags of sentences
    are more likely to be human or AI.

    Parameters:
    test_text (list): a list containing doc variable with the test text
    human_article_content (list): a list containing doc variables containing human generated texts
    ai_article_content (list): a list of doc variables containing AI generated texts

    Returns:
    test_score (int): a test score whether it is more likely to be human or AI generated

    Made by: Kennie
    """
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
    """
    Returns a test score based on whether the test text is more likely to be human or AI generated
    based on the frequency of the three ending POS tags of sentences and comparing them with the 
    frequency of the three ending POS tags of sentences in human and AI generated texts

    Parameters:
    test_text (list): a list with one doc variable containing the test text
    human_article_content (list): a list with doc variables containing human generated texts
    ai_article_content (list): a list with doc variables containing AI generated texts

    Returns:
    test_score (int): returns an integer telling whether the test text is more likely to be
    human or AI generated

    Made by: Kennie
    """
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
    """
    Returns a test score based on whether the test text is more likely to be human or AI generated
    based on the frequency of dependecy and comparing that with the frequency of dependency in human 
    and AI generated texts

    Parameters:
    test_text (list): a list with one doc variable containing the test text
    human_article_content (list): a list with doc variables containing human generated texts
    ai_article_content (list): a list with doc variables containing AI generated texts

    Returns:
    test_score (int): returns an integer telling whether the test text is more likely to be
    human or AI generated

    Made by: Kennie
    """
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
    """
    Returns a test score based on whether the test text is more likely to be human or AI generated
    based on asent polarity of the text and comparing that with the asent polarity of human
    and AI generated texts

    Parameters:
    test_text (str): a string containing the test text
    human_article_content (list): a list with doc variables containing human generated texts
    ai_article_content (list): a list with doc variables containing AI generated texts

    Returns:
    testscore (int): returns an integer telling whether the test text is more likely to be
    human or AI generated

    Made by: Carlijn
    """
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


def test_polarity_blob(test_text, human_article_content, ai_article_content):
    """
    Returns a test score based on whether the test text is more likely to be human or AI generated
    based on the blob polarity of the test text and comparing that with the blob polarity of 
    human and AI generated texts

    Parameters:
    test_text (list): a list with one doc variable containing the test text
    human_article_content (list): a list with doc variables containing human generated texts
    ai_article_content (list): a list with doc variables containing AI generated texts

    Returns:
    test_score (int): returns an integer telling whether the test text is more likely to be
    human or AI generated

    Made by: Carlijn
    """
    human_polarity_blob = get_blob_polarity(human_article_content)
    ai_polarity_blob = get_blob_polarity(ai_article_content)
    test_text_polarity_blob = get_blob_polarity(test_text)

    test_human_polarity = abs(test_text_polarity_blob - human_polarity_blob)
    test_ai_polarity = abs(test_text_polarity_blob - ai_polarity_blob)

    if test_human_polarity < test_ai_polarity:
        return 5
    else:
        return -5


def test_subjectivity(test_text, human_article_content, ai_article_content):
    """
    Returns a test score based on whether the test text is more likely to be human or AI generated
    based on the the subjectivity score of the test text and comparing that to human and AI
    generated texts

    Parameters:
    test_text (list): a list with one doc variable containing the test text
    human_article_content (list): a list with doc variables containing human generated texts
    ai_article_content (list): a list with doc variables containing AI generated texts

    Returns:
    test_score (int): returns an integer telling whether the test text is more likely to be
    human or AI generated

    Made by: Anouk
    """
    human_subjectivity = get_subjectivity(human_article_content)
    ai_subjectivity = get_subjectivity(ai_article_content)
    test_text_subjectivity = get_subjectivity(test_text)

    test_human_subjectivity = abs(test_text_subjectivity - human_subjectivity)
    test_ai_subjectivity = abs(test_text_subjectivity - ai_subjectivity)

    if test_human_subjectivity < test_ai_subjectivity:
        return 5
    else:
        return -5


def test_named_entity_recognition(test_text, human_article_content, ai_article_content):
    """
    Returns a test score based on the percentage of entity labels comparing that of the test
    text with the percentage of entity lables of human and AI generated texts

    Parameters:
    test_text (list): a list with one doc variable containing the test text
    human_article_content (list): a list with doc variables containing human generated texts
    ai_article_content (list): a list with doc variables containing AI generated texts

    Returns:
    test_score (int): returns an integer telling whether the test text is more likely to be
    human or AI generated

    Made by: Kennie
    """
    test_score = 0

    percentage_human = sorted(find_percentage(named_entity_rec(human_article_content)))
    percentage_ai = sorted(find_percentage(named_entity_rec(ai_article_content)))
    percentage_test_text = sorted(find_percentage(named_entity_rec(test_text)))

    for test_percentage in percentage_test_text:
        for human_percentage in percentage_human:
            if test_percentage[0] == human_percentage[0]:
                test_human_percentage = abs(test_percentage[1] - human_percentage[1])
                break
        for ai_percentage in percentage_ai:
            if test_percentage[0] == ai_percentage[0]:
                test_ai_percentage = abs(test_percentage[1] - ai_percentage[1])
                break
        if test_human_percentage < test_ai_percentage:
            test_score += 1
        else:
            test_score -= 1
        
        return test_score


def test_ambiguity(test_text, human_article_content, ai_article_content):
    """
    Returns a test score based on the percentage of how many of the words are ambiguous
    and comparing that to the average percentage of ambiguous words of human and AI
    generated texts
    
    Parameters:
    test_text (list): a list with one doc variable containing the test text
    human_article_content (list): a list with doc variables containing human generated texts
    ai_article_content (list): a list with doc variables containing AI generated texts

    Returns:
    test_score (int): returns an integer telling whether the test text is more likely to be
    human or AI generated

    Made by: Kennie
    """
    human_percentage = find_percentage_ambiguity(count_ambiguous_words(human_article_content))
    ai_percentage = find_percentage_ambiguity(count_ambiguous_words(ai_article_content))
    test_text_percentage = find_percentage_ambiguity(count_ambiguous_words(test_text))

    test_human_percentage = abs(test_text_percentage - human_percentage)
    test_ai_percentage = abs(test_text_percentage - ai_percentage)

    if test_human_percentage < test_ai_percentage:
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
    length_test_score = test_average_length(human_test_text)
    pos_tag_score = test_pos_tags(human_test_text, human_article_content, ai_article_content)
    beginning_3_pos_score = test_3_beginning_pos(human_test_text, human_article_content, ai_article_content)
    end_3_pos_score = test_3_end_pos(human_test_text, human_article_content, ai_article_content)
    dep_frep_score = test_dep_freq(human_test_text, human_article_content, ai_article_content)
    asent_polarity_score = test_asent_polarity(human_test_text[0].text, file_path_human, file_path_ai)
    blob_polarity_score = test_polarity_blob(human_test_text, human_article_content, ai_article_content)
    subjectivity_score = test_subjectivity(human_test_text, human_article_content, ai_article_content)
    named_entity_rec_score = test_named_entity_recognition(human_test_text, human_article_content, ai_article_content)
    ambiguity_score = test_ambiguity(human_test_text, human_article_content, ai_article_content)

    test_list_scores = [length_test_score, pos_tag_score, beginning_3_pos_score, end_3_pos_score, dep_frep_score, asent_polarity_score, blob_polarity_score, subjectivity_score, named_entity_rec_score, ambiguity_score]
    #human_article_content should be replaced with test_data
    test_data(test_list_scores)

    
if __name__ == "__main__":
    main()