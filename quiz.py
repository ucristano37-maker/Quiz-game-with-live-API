import requests
import html
import random

# Get questions from API
def get_questions():
    url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["results"]
    else:
        print("Failed to fetch data")
        return []

# Present question
def present_question(question, index):
    print(f"\nQuestion {index + 1}: {html.unescape(question['question'])}")

    choices = question["incorrect_answers"] + [question["correct_answer"]]
    random.shuffle(choices)

    for i, choice in enumerate(choices):
        print(f"{i + 1}. {html.unescape(choice)}")

    user_choice = int(input("Enter your choice: "))

    if choices[user_choice - 1] == question["correct_answer"]:
        print("✅ Correct Answer")
        return 1
    else:
        print("❌ Wrong Answer")
        print("Correct Answer:", html.unescape(question["correct_answer"]))
        return 0

# Main quiz function
def main():
    print("Welcome to the Quiz!\n")

    questions = get_questions()
    if not questions:
        print("No questions available")
        return

    score = 0

    for i, question in enumerate(questions):
        score += present_question(question, i)

    print("\nQuiz Finished")
    print(f"Marks: {score}/10")

    if score >= 5:
        print("🎉 PASS")
    else:
        print("❌ FAIL Try again !")
print("Thank you for playing!")    
main()
