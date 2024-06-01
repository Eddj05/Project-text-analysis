from syntax import *
from semantic import *
from pragmatic import *

def test_data(test_text):
    test_score = 0
    
    average_sent_length = average_sentence_length(test_text)
    if average_sent_length > 27.55:
        test_score -= 1
    else:
        test_score += 1

    print(test_score)

    if test_score < 0:
        label = "AI Generated"
    else:
        label = "Human"

    print(f"label = {label}")
        

def main():
    # Chat-GPT 3.5 generated text
    ai_test_text = "In a quiet village, a legend spoke of an ancient tree with golden leaves holding time's secrets. One evening, curious Elara ventured into the forest, finding a glowing path to a clearing with a crystal pond and a stone pedestal holding an ancient book. Opening the book, Elara discovered stories of her village's past and future. As dawn broke, she realized she had become the keeper of her village's history and destiny. Returning home, she felt a profound connection to generations past and future, understanding the true magic of the tree lay in its timeless stories."
    # Human made text from the bbc
    human_test_text = "Twenty-five years after bursting on to the scene, it appears rapper Eminem's provocative alter ego Slim Shady may finally be silenced. The antagonistic Slim Shady, with his peroxide-blond hair and everyman blue jeans, stemmed from Eminem's self-described 'white trash' upbringing. In a surprise April announcement teased as a mock murder news report, Eminem revealed that his new album, The Death of Slim Shady (Coup de Grâce), will be released this summer."
    file_path_human = "../data/human.jsonl"
    file_path_ai = "../data/group6.jsonl"

    # test data still needs to be given
    file_path_test = None

    human_article_content = get_content(file_path_human)
    ai_article_content = get_content(file_path_ai)

    # loading all the percentages lists
    percentage_pos_tag_human = (find_percentage(pos_tag_frequency(human_article_content)))
    percentage_pos_tag_ai = (find_percentage(pos_tag_frequency(ai_article_content)))
    
    percentage_3_pos_beginning_human = find_percentage(begin_POS_tags(display_sentences(human_article_content)))
    percentage_3_pos_beginning_ai = find_percentage(begin_POS_tags(display_sentences(ai_article_content)))
    
    percentage_3_pos_end_human = find_percentage(begin_POS_tags(display_sentences(human_article_content)))
    percentage_3_pos_end_ai = find_percentage(begin_POS_tags(display_sentences(human_article_content)))
    
    percentage_dep_freq_human = (find_percentage(dep_tag_frequency(human_article_content)))
    percentage_dep_freq_ai = (find_percentage(dep_tag_frequency(ai_article_content)))

    #human_article_content should be replaced with test_data
    test_data(ai_article_content)

    
if __name__ == "__main__":
    main()