from groq import generate_response


def prompt_engineering_activity():
    print("Welcome to the AI Prompt Engineering Tutorial!")

    vague = input("Enter a vague prompt: ")
    print("\nAI's response to vague prompt:")
    print(generate_response(vague))

    specific = input("\nNow, make it more specific: ")
    print("\nAI's response to specific prompt:")
    print(generate_response(specific))

    context = input("\nNow, add context to your specific prompt: ")
    print("\nAI's response to contextual prompt:")
    print(generate_response(context))


    print("\n--- reflection ---")
    print("how did thee ais response change when the prompt was mmade more specific")
    print("how did the ais response improve with thee added context")
    print("which prompt produced the most relevant and tailored response? why?")

if __name__ == "__main__":
    prompt_engineering_activity()