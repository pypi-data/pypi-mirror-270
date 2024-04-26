import os
import platform
import sys
from groq import Groq



def main():
    endpoint = "https://api.groq.com/openai/v1"

    api_key = os.getenv('GROQ_API_KEY')
    model = os.getenv('GROQ_ModelId')


    if not api_key:
        print("\nAPI key not set. Please set the GROQ_API_KEY environment variable.\n")
        print("Navigate to https://console.groq.com/keys to setup API")
        sys.exit(1)

    if not model:
        print("ModelId is not set. Please set the GROQ_ModelId environment variable.\n")
        print("Navigate to https://console.groq.com/docs/models to setup ModelId")
        sys.exit(1)

    # Configure the API client
    client = Groq(
        api_key=api_key
    )

    def get_system_prompt():
        system_info = f"OS: {platform.system()}, Arch: {platform.machine()}"
        prompt = f"""
            You are CLU, a CLI code generator. Respond with the CLI command to generate the code with only one short sentence description in first line.
            If the user asks for a specific language, respond with the CLI command to generate the code in that language.
            If CLI command is multiple lines, separate each line with a newline character.
            Do not write any markdown. Do not write any code.
            System Info: {system_info}
            First line is the description in one sentence.
            Example output:
            Building and installing a Go binary
            go build main.go
            go install main
            """
        return prompt

    def ask_ai(prompt):
        context_prompt = get_system_prompt()
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": context_prompt},
                    {"role": "user", "content": prompt}
                ]
            )

            first_line = True
            content = response.choices[0].message.content
            lines = content.split('\n')
            print("\n")
            for i, line in enumerate(lines):
                if line:
                    if first_line:
                        print(f"\033[1;35m{line}\033[0m")
                        first_line = False
                    else:
                        print("\033[1;32m$ \033[0m" + line)

        except Exception as e:
            print(e)



    if len(sys.argv) < 2:
        print("Usage: clu <prompt>")
        sys.exit(1)
    phrase = " ".join(sys.argv[1:])
    ask_ai(phrase)


if __name__ == "__main__":
    main()