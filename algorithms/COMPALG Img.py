import os, re, sys, colorama
from PIL import Image
from colorama import Fore


colorama.init(True)


def _split(values: list, lenght: int) -> list[list[int]]:
    for i in range(0, len(values), lenght):
        yield values[i: i + lenght]



def _count(_pixels: list[int]) -> list[tuple[int]]:
    counted = []
    [counted.append(_pixels.count(number)) for number in _pixels]
    counted = list(dict.fromkeys(counted))
    _pixels = list(dict.fromkeys(_pixels))
    return list(zip(_pixels, counted))



def compression(pixels: list, resolution: tuple[int], cfn: str): 
    LINES = _split(pixels, resolution[1])
    with open(f'{cfn}.py', 'a') as f:
        for line in LINES:
            compressed = _count(line)
            f.write(f'{compressed}\n')
        f.close()
    print(f'{Fore.GREEN}Compression finished. Output file: {cfn}.py')
    


def main(filename: str, compressed_filename: str) -> str:
    os.system('cls')
    try:
        img = Image.open(filename)
        match img.mode:
            case 'L':
                compression(list(img.getdata()), img.size, compressed_filename)
                img.close()
            case _:
                os.system('cls')
                print(f'{Fore.YELLOW} WARNING: converting {filename} from RGB to a W\B.')
                #convert img in wb
    except Exception as e:
        print(f'{Fore.RED}ERROR: {e}')
        
        

def usage(error: str) -> str:
    os.system('cls')
    print(f'{Fore.RED}ERROR: \'{error}\' is not a valid command.')
    print(f'{Fore.YELLOW}USAGE:\n\t- algo.py <filename> <compressed filename> (Compress the file)\n\t- algo.py dec <file to decompress> <output filename>')
    exit(0)



if __name__ == '__main__':
    os.system('cls')
    match len(sys.argv):
        case 3:
            [main(sys.argv[1], re.search('\w+(?=\.)', sys.argv[2]).group()) if '.' in sys.argv[2] else main(sys.argv[1], sys.argv[2])]
        case 4:
            print('Decompression. Work in progress')
        case _:
            usage("".join(sys.argv))
