from medium_to_markdown import MediumParser

url = "https://medium.com/towards-data-science/fine-tune-llama-3-with-orpo-56cfab2f9ada"
filename = ""
is_image_download = True
ssl_verify = True
parser = MediumParser(url, filename, is_image_download, ssl_verify)
if parser.parse_and_savefile():
    print("Parsing is done.")