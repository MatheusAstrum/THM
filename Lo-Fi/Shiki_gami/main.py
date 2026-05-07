import requests
import time
import argparse
import colorama

red = '\033[31m'
green = '\033[32m'

def Requisicao(Url, Tempo):

    palavra_chave = ["root:", "flag", "banana", "euteamo"]#criar um arquivo separado

    try:
        with open("dir.txt", "r") as f:

            url = Url
            tempo = Tempo

            for linha in f:

                dir = linha.strip()
                r = requests.get(f"{url}{dir}")
                html = r.text

                for item in palavra_chave:
                    if item in html:
                        print(f"{green} Conteúdo '{item}' encontrado em: {url}{dir}\n")
                if "does not exist." in html:
                    print(f"{red} Sem resultado em {url}{dir}\n")

                time.sleep(tempo)

    except Exception as error:
        print(f"erro{error}")


def main():

    parser = argparse.ArgumentParser(description="Shiki_Gami LFI Tool", add_help=False)

    parser.add_argument("--url", type=str, help="url")
    parser.add_argument("--tempo", type=int, help="segundos para cada request")

    args = parser.parse_args()

    Requisicao(args.url, args.tempo)

if __name__ == "__main__":
    main()
