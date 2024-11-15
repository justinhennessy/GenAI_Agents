from supervisor import get_response
import sys

def chat_loop():
    print("\nWelcome to the Database Chat Interface!")
    print("Type 'exit' or 'quit' to end the session")
    print("Type 'help' for example questions")
    print("-" * 50)

    def show_help():
        print("\nExample questions you can ask:")
        print("- How many tables are in the database?")
        print("- What information is in the albums table?")
        print("- How many albums do we have in total?")
        print("- Who are the top selling artists?")
        print("- Show me the longest tracks in the database")
        print("-" * 50)

    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()

            # Check for exit commands
            if user_input.lower() in ['exit', 'quit']:
                print("\nGoodbye!")
                sys.exit(0)

            # Check for help command
            if user_input.lower() == 'help':
                show_help()
                continue

            # Skip empty inputs
            if not user_input:
                continue

            # Process the question through the supervisor
            print("\nProcessing your question...")
            result = get_response(user_input)

            # Display the response
            print("\nAssistant:")
            print(result['response'])

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again or type 'exit' to quit.")

if __name__ == "__main__":
    try:
        chat_loop()
    except Exception as e:
        print(f"\nApplication error: {str(e)}")
        sys.exit(1)