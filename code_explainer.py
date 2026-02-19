import google.generativeai as genai

# Configure API
API_KEY = "AIzaSyA29Y164lp8KZGksWkzrUE6LCrh-_kf5Xo"
genai.configure(api_key=API_KEY)

def explain_code(code, language=""):
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
    Explain the following {language} code in simple terms:
    
    ```{language}
    {code}
    ```
    
    Provide:
    1. What the code does (overview)
    2. Line-by-line explanation
    3. Key concepts used
    4. Potential improvements
    """
    
    response = model.generate_content(prompt)
    return response.text

def main():
    print("=" * 60)
    print("CODE EXPLAINER - Powered by Gemini AI")
    print("=" * 60)
    
    while True:
        print("\n1. Explain Code")
        print("2. Exit")
        choice = input("\nChoice: ").strip()
        
        if choice == "2":
            print("Goodbye!")
            break
        
        if choice == "1":
            language = input("Language (Python/Java/JavaScript/etc): ").strip()
            print("\nPaste your code (type 'END' on new line when done):")
            
            lines = []
            while True:
                line = input()
                if line == "END":
                    break
                lines.append(line)
            
            code = "\n".join(lines)
            
            if code.strip():
                print("\n" + "=" * 60)
                print("EXPLANATION:")
                print("=" * 60)
                explanation = explain_code(code, language)
                print(explanation)
            else:
                print("No code provided!")

if __name__ == "__main__":
    main()
