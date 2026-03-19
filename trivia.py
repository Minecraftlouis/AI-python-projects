                    import requests

                    import random

                    import html

                    # Education-focused categories (General Knowledge, Science, History, etc.)

                    EDUCATION_CATEGORY_ID = 9 # General Knowledge category (most educational)

                    API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"

                    def get_education_questions():
                    response = requests.get(API_URL)

                    if response.status_code == 200:

                    data = response.json()

                    if data['response_code'] == 0 and data['results']:

                    return data['results']

                    return None
                    def run_quiz():

                    questions = get_education_questions()

                    if not questions:

                    print("Failed to fetch educational questions")

                    return

                    score = 0

                    print("Welcome to the Education Quiz!\n")


                    for i, q in enumerate(questions, 1):

                    # Decode HTML entities and prepare options

                    question = html.unescape(q['question'])

                    correct = html.unescape(q['correct_answer'])

                    incorrects = [html.unescape(a) for a in q['incorrect_answers']]


                    # Create and shuffle options

                    options = incorrects + [correct]

                    random.shuffle(options)


                    # Display question

                    print(f"Question {i}: {question}")

                    for idx, option in enumerate(options, 1):

                    print(f" {idx}. {option}")