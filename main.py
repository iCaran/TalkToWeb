import colorama
from colorama import Fore
from bardcode import bardSesh
from urlTest import is_url

def prettyColor():
    global info_color, main_output_color, error_color, next_input, divider_color, cont_color, title_color
    colorama.init()
    info_color = Fore.CYAN
    main_output_color = Fore.WHITE
    error_color = Fore.LIGHTRED_EX
    next_input = Fore.GREEN
    divider_color = Fore.LIGHTBLACK_EX
    cont_color = Fore.LIGHTWHITE_EX
    title_color = Fore.LIGHTYELLOW_EX

def main():
    prettyColor()
    b = bardSesh()
    b.bardSession(error_color = error_color)

    while(1):
        query = input(next_input + "Query or URL (Enter to Exit): ")
        if query=='':
            exit()
        elif is_url(query):
            print()
            title, summary = b.on_submit(query)
            if summary == "":
                print(error_color + "Couldn't get site content :(")
            else:
                print()
                print(title_color + title)
                print()
                print(main_output_color + summary)
                print(cont_color + "Continue this convo!?")
                print()
        else:
            print()
            print(main_output_color + b.getResponse(query))
            print(divider_color + "---")
            print()
            print(cont_color + "Continue this convo!?")
            print()

if __name__ == '__main__':
    main()