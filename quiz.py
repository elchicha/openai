import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Sample trivia question
question = "What is the capital of France?"
answers = ["London", "Paris", "Berlin"]

# Get user input
user_answer = input("Choose the answer (a, b, or c): ")

# Select answer based on user input
chosen_answer = answers[int(user_answer) - 1]

# Craft prompt for explanation
prompt = f"Explain why '{chosen_answer}' is the answer to the question: '{question}'"

# Use OpenAI to generate explanation
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=150,  # Adjust for desired explanation length
    n=1,
    stop=None,
    temperature=0.7,  # Adjust for creativity vs informativeness
)

explanation = response.choices[0].text.strip()

# Display results
print(f"You chose: {chosen_answer}")
print(f"Explanation: {explanation}")
