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
    valid_scores = [score for score in score_list if score is not None]
    test_score = sum(valid_scores)

    # if the testscore is positive the label is 'Human', if the testscore is negative the label will be 'AI Generated'
    if test_score < 0:
        label = "AI Generated"
    else:
        label = "Human"

    return label, test_score


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


def test_pos_tags(test_text, percentage_pos_tag_human, percentage_pos_tag_ai):
    """
    Returns a test score based on whether the test text is more likely to be AI or Human generated
    based on the frequency of POS tags and checking it with average human frequency of POS tags and 
    average AI frequency of POS tags

    Parameters:
    test_text (list): a list of doc variable containing the test_text
    percentage_pos_tag_human (list): list of tuples with pos tags and a percentage of how frequent they 
    occur in the text

    percentage_pos_tag_ai (list): list of tuples with pos tags and a percentage of how frequent they 
    occur in the text

    Returns:
    test_score (int): returns a test score whether frequency of pos tags is more likely to be
    AI or human generated

    Made by: Edwin
    """
    test_score = 0
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


def test_3_beginning_pos(test_text, percentage_3_pos_beginning_human, percentage_3_pos_beginning_ai):
    """
    Returns a test score number based on whether the test text where the 3 beginning POS tags of sentences
    are more likely to be human or AI.

    Parameters:
    test_text (list): a list containing doc variable with the test text
    percentage_3_pos_beginning_human (list): list of tuples with 3 pos tags that occur at the beginning of a sentence
    and a percentage of how frequent they occur in the text

    percentage_3_pos_beginning_ai (list): list of tuples with 3 pos tags that occur at the beginning of a sentence
    and a percentage of how frequent they occur in the text

    Returns:
    test_score (int): a test score whether it is more likely to be human or AI generated

    Made by: Kennie
    """
    percentage_3_pos_beginning_test = sorted(find_percentage(begin_POS_tags(display_sentences(test_text))))

    test_score = 0
    for test_percentage in percentage_3_pos_beginning_test:
        # prevents UnboundLocalError
        test_percentage_human = float('inf')
        test_percentage_ai = float('inf')
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


def test_3_end_pos(test_text, percentage_3_pos_end_human, percentage_3_pos_end_ai):
    """
    Returns a test score based on whether the test text is more likely to be human or AI generated
    based on the frequency of the three ending POS tags of sentences and comparing them with the 
    frequency of the three ending POS tags of sentences in human and AI generated texts

    Parameters:
    test_text (list): a list with one doc variable containing the test text
    percentage_3_pos_end_human (list): list of tuples with 3 pos tags that occur at the end of a sentence
    and a percentage of how frequent they occur in the text

    percentage_3_pos_end_ai (list): list of tuples with 3 pos tags that occur at the end of a sentence
    and a percentage of how frequent they occur in the text

    Returns:
    test_score (int): returns an integer telling whether the test text is more likely to be
    human or AI generated

    Made by: Kennie
    """
    percentage_3_pos_end_test = sorted(find_percentage(end_POS_tags(display_sentences(test_text))))

    test_score = 0
    for test_percentage in percentage_3_pos_end_test:
        test_percentage_human = float('inf')
        test_percentage_ai = float('inf')
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


def test_dep_freq(test_text, percentage_dep_freq_human, percentage_dep_freq_ai):
    """
    Returns a test score based on whether the test text is more likely to be human or AI generated
    based on the frequency of dependecy and comparing that with the frequency of dependency in human 
    and AI generated texts

    Parameters:
    test_text (list): a list with one doc variable containing the test text
    percentage_dep_freq_human (list): list of tuples with dependecy tag and a percentage of how frequent they
    occur in the human texts

    percentage_3_pos_beginning_ai (list): list of tuples with dependecy tag and a percentage of how frequent they
    occur in the ai texts


    Returns:
    test_score (int): returns an integer telling whether the test text is more likely to be
    human or AI generated

    Made by: Kennie
    """
    percentage_dep_freq_test = sorted(find_percentage(dep_tag_frequency(test_text)))

    test_score = 0
    
    for test_percentage in percentage_dep_freq_test:
        test_percentage_human = float('inf')
        test_percentage_ai = float('inf')
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


def test_asent_polarity(test_text, human_asent_polarity, ai_asent_polarity):
    """
    Returns a test score based on whether the test text is more likely to be human or AI generated
    based on asent polarity of the text and comparing that with the asent polarity of human
    and AI generated texts

    Parameters:
    test_text (str): a string containing the test text
    humnan_asent_polarity (float): a float containing asent polarity
    ai_asent_polarity (float): a float containing asent polarity

    Returns:
    integer indicating whether it is more likely to be AI or human generated

    Made by: Carlijn
    """
    nlp = spacy.blank('en')
    nlp.add_pipe('sentencizer')
    nlp.add_pipe('asent_en_v1')

    test_text_asent = [nlp(test_text)]
    test_text_polarity = get_asent_polarity(test_text_asent)

    test_human_polarity = abs(test_text_polarity - human_asent_polarity)
    test_ai_polarity = abs(test_text_polarity - ai_asent_polarity)

    if test_human_polarity < test_ai_polarity:
        return 5
    else:
        return -5


def test_polarity_blob(test_text, human_polarity_blob, ai_polarity_blob):
    """
    Returns a test score based on whether the test text is more likely to be human or AI generated
    based on the blob polarity of the test text and comparing that with the blob polarity of 
    human and AI generated texts

    Parameters:
    test_text (list): a list with one doc variable containing the test text
    human_polarity_blob (float): a float containing the blob polarity score
    ai_polarity_blob (float): a float containing the blob polarity score

    Returns:
    integer indicating whether it is more likely to be AI or human generated

    Made by: Carlijn
    """
    test_text_polarity_blob = get_blob_polarity(test_text)

    test_human_polarity = abs(test_text_polarity_blob - human_polarity_blob)
    test_ai_polarity = abs(test_text_polarity_blob - ai_polarity_blob)

    if test_human_polarity < test_ai_polarity:
        return 5
    else:
        return -5


def test_subjectivity(test_text, human_subjectivity, ai_subjectivity):
    """
    Returns a test score based on whether the test text is more likely to be human or AI generated
    based on the the subjectivity score of the test text and comparing that to human and AI
    generated texts

    Parameters:
    test_text (list): a list with one doc variable containing the test text
    human_subjectivity (float): a float containing subjectivity score
    ai_subjectivity (float): a float containing subjectivity score

    Returns:
    test_score (int): returns an integer telling whether the test text is more likely to be
    human or AI generated

    Made by: Anouk
    """
    test_text_subjectivity = get_subjectivity(test_text)

    test_human_subjectivity = abs(test_text_subjectivity - human_subjectivity)
    test_ai_subjectivity = abs(test_text_subjectivity - ai_subjectivity)

    if test_human_subjectivity < test_ai_subjectivity:
        return 5
    else:
        return -5


def test_named_entity_recognition(test_text, percentage_human_entity, percentage_ai_entity):
    """
    Returns a test score based on the percentage of entity labels comparing that of the test
    text with the percentage of entity lables of human and AI generated texts

    Parameters:
    test_text (list): a list with one doc variable containing the test text
    percentage_human_entity (list): a list containing tuples with entity label and percentage 
    of how much they occur in the text

    percentage_ai_entity (list): a list containing tuples with entity label and percentage 
    of how much they occur in the text

    Returns:
    test_score (int): returns an integer telling whether the test text is more likely to be
    human or AI generated

    Made by: Kennie
    """
    test_score = 0
    percentage_test_text = sorted(find_percentage(named_entity_rec(test_text)))

    for test_percentage in percentage_test_text:
        test_human_percentage = float('inf')
        test_ai_percentage = float('inf')
        for human_percentage in percentage_human_entity:
            if test_percentage[0] == human_percentage[0]:
                test_human_percentage = abs(test_percentage[1] - human_percentage[1])
                break
        for ai_percentage in percentage_ai_entity:
            if test_percentage[0] == ai_percentage[0]:
                test_ai_percentage = abs(test_percentage[1] - ai_percentage[1])
                break
        if test_human_percentage < test_ai_percentage:
            test_score += 1
        else:
            test_score -= 1
        
        return test_score


def test_ambiguity(test_text, human_percentage_ambiguity, ai_percentage_ambiguity):
    """
    Returns a test score based on the percentage of how many of the words are ambiguous
    and comparing that to the average percentage of ambiguous words of human and AI
    generated texts
    
    Parameters:
    test_text (list): a list with one doc variable containing the test text
    human_percentage_ambiguity (float): a float containing a percentage of how much of the words 
    in the text are ambiguous

    ai_percentage_ambiguity (float): a float containing a percentage of how much of the words 
    in the text are ambiguous

    Returns:
    Integer that indicates whether it is more human-like or AI-like

    Made by: Kennie
    """
    test_text_percentage = find_percentage_ambiguity(count_ambiguous_words(test_text))

    test_human_percentage = abs(test_text_percentage - human_percentage_ambiguity)
    test_ai_percentage = abs(test_text_percentage - ai_percentage_ambiguity)

    if test_human_percentage < test_ai_percentage:
        return 5
    else:
        return -5

def main():
    # make a loop to give a label for each independent text in the test data set.
    file_path_human = "../data/human.jsonl"
    file_path_ai = "../data/group6.jsonl"
    file_path_test_human = "../test_data/human.jsonl"
    file_path_test_ai = "../test_data/group6.jsonl"

    human_article_content = get_content(file_path_human)
    ai_article_content = get_content(file_path_ai)
    test_human_article_content = get_content(file_path_test_human)
    test_ai_article_content = get_content(file_path_test_ai)
    human_test_analysis = open("human_test_analysis.txt", "w", encoding="utf-8")
    ai_test_analysis = open("ai_test_analysis.txt", "w", encoding="utf-8")

    # loading all the percentages
    percentage_pos_tag_human = sorted((find_percentage(pos_tag_frequency(human_article_content))))
    percentage_pos_tag_ai = sorted((find_percentage(pos_tag_frequency(ai_article_content))))

    percentage_3_pos_beginning_human = sorted(find_percentage(begin_POS_tags(display_sentences(human_article_content))))
    percentage_3_pos_beginning_ai = sorted(find_percentage(begin_POS_tags(display_sentences(ai_article_content))))

    percentage_3_pos_end_human = sorted(find_percentage(end_POS_tags(display_sentences(human_article_content))))
    percentage_3_pos_end_ai = sorted(find_percentage(end_POS_tags(display_sentences(ai_article_content))))

    percentage_dep_freq_human = sorted((find_percentage(dep_tag_frequency(human_article_content))))
    percentage_dep_freq_ai = sorted((find_percentage(dep_tag_frequency(ai_article_content))))

    human_article_content_asent = get_content_asent(file_path_human)
    ai_article_content_asent = get_content_asent(file_path_ai)
    human_asent_polarity = get_asent_polarity(human_article_content_asent)
    ai_asent_polarity = get_asent_polarity(ai_article_content_asent)
    
    human_polarity_blob = get_blob_polarity(human_article_content)
    ai_polarity_blob = get_blob_polarity(ai_article_content)

    human_subjectivity = get_subjectivity(human_article_content)
    ai_subjectivity = get_subjectivity(ai_article_content)

    percentage_human_entity = sorted(find_percentage(named_entity_rec(human_article_content)))
    percentage_ai_entity = sorted(find_percentage(named_entity_rec(ai_article_content)))

    human_percentage_ambiguity = find_percentage_ambiguity(count_ambiguous_words(human_article_content))
    ai_percentage_ambiguity = find_percentage_ambiguity(count_ambiguous_words(ai_article_content))

    # testing our analysis system for human articles
    for index, doc in enumerate(test_human_article_content):
        test_text = [doc]
        length_test_score = test_average_length(test_text)
        pos_tag_score = test_pos_tags(test_text, percentage_pos_tag_human, percentage_pos_tag_ai)
        beginning_3_pos_score = test_3_beginning_pos(test_text, percentage_3_pos_beginning_human, percentage_3_pos_beginning_ai)
        end_3_pos_score = test_3_end_pos(test_text, percentage_3_pos_end_human, percentage_3_pos_end_ai)
        dep_frep_score = test_dep_freq(test_text, percentage_dep_freq_human, percentage_dep_freq_ai)
        asent_polarity_score = test_asent_polarity(test_text[0].text, human_asent_polarity, ai_asent_polarity)
        blob_polarity_score = test_polarity_blob(test_text, human_polarity_blob, ai_polarity_blob)
        subjectivity_score = test_subjectivity(test_text, human_subjectivity, ai_subjectivity)
        named_entity_rec_score = test_named_entity_recognition(test_text, percentage_human_entity, percentage_ai_entity)
        ambiguity_score = test_ambiguity(test_text, human_percentage_ambiguity, ai_percentage_ambiguity)

        test_list_scores = [length_test_score, pos_tag_score, beginning_3_pos_score, end_3_pos_score, dep_frep_score, asent_polarity_score, blob_polarity_score, subjectivity_score, named_entity_rec_score, ambiguity_score]
        label, score = test_data(test_list_scores)
        print(f"Human text {index}. Label: {label} Score: {score}")
        human_test_analysis.write(f"Human text {index}. Label: {label} Score: {score}\n")

    human_test_analysis.close()

    # testing our analysis system for ai articles
    for index, doc in enumerate(test_ai_article_content):
        test_text = [doc]
        length_test_score = test_average_length(test_text)
        pos_tag_score = test_pos_tags(test_text, percentage_pos_tag_human, percentage_pos_tag_ai)
        beginning_3_pos_score = test_3_beginning_pos(test_text, percentage_3_pos_beginning_human, percentage_3_pos_beginning_ai)
        end_3_pos_score = test_3_end_pos(test_text, percentage_3_pos_end_human, percentage_3_pos_end_ai)
        dep_frep_score = test_dep_freq(test_text, percentage_dep_freq_human, percentage_dep_freq_ai)
        asent_polarity_score = test_asent_polarity(test_text[0].text, human_asent_polarity, ai_asent_polarity)
        blob_polarity_score = test_polarity_blob(test_text, human_polarity_blob, ai_polarity_blob)
        subjectivity_score = test_subjectivity(test_text, human_subjectivity, ai_subjectivity)
        named_entity_rec_score = test_named_entity_recognition(test_text, percentage_human_entity, percentage_ai_entity)
        ambiguity_score = test_ambiguity(test_text, human_percentage_ambiguity, ai_percentage_ambiguity)

        test_list_scores = [length_test_score, pos_tag_score, beginning_3_pos_score, end_3_pos_score, dep_frep_score, asent_polarity_score, blob_polarity_score, subjectivity_score, named_entity_rec_score, ambiguity_score]
        label, score = test_data(test_list_scores)
        print(f"AI text {index}. Label: {label} Score: {score}")
        ai_test_analysis.write(f"AI text {index}. Label: {label} Score: {score}\n")

    ai_test_analysis.close()

        
if __name__ == "__main__":
    main()