import json
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def process_text(file_path):
    article_content = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            article = json.loads(line)
            text = article.get('text', '')  
            if text: 
                article_content.append(text)

    return article_content

def main():
    file_path = "human.jsonl"
    article_content = (process_text(file_path))
    for text in article_content:
        print(text)

if __name__ == "__main__":
    main()