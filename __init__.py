"""
All Rights Reserved

Copyright (c) 2024 Wilhelm

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import parse

input_file = "input.pdf"
output_file = "question.txt"


def main() -> None:
    """
        This function runs the rest of the file.
        @return     None
    """

    print_lines(["The default file for parsing is input_file.pdf",
                 "Please ensure that this exists.", " ",
                 "Press any key to continue...", ])
    input()

    if not parse.file_exists(input_file):
        raise FileNotFoundError

    pdf_text = parse.text_from_pdf(input_file)
    parse.process_text(pdf_text, output_file)


def print_lines(lines: list[str]) -> None:
    """
        Prints an array of strings as lines
        @return     None
    """

    for line in lines:
        print(line)
