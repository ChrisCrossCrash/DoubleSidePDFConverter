from pathlib import Path
from pypdf import PdfReader, PdfWriter

IN_FILE = 'sample.pdf'
OUT_FILE = 'output.pdf'

def main():
    reader = PdfReader(IN_FILE)
    number_of_pages = len(reader.pages)
    try:
        assert number_of_pages % 2 == 0
    except AssertionError:
        print("The number of pages is not divisible by 2")
        return 1
    even_pages = reader.pages[:number_of_pages//2]
    odd_pages = reader.pages[number_of_pages//2:]

    # reverse the order of the pages in the second half
    odd_pages = odd_pages[::-1]

    # Merge the even and odd pages in the correct order
    merger = PdfWriter()
    for i in range(number_of_pages//2):
        merger.add_page(even_pages[i])
        merger.add_page(odd_pages[i])
    merger.write(OUT_FILE)


if __name__ == '__main__':
    main()
