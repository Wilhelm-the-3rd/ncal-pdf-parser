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

from .parse import *
from .organize import *

input = "input.pdf"
output = "question.txt"

def main() -> None:
    """
        This function runs the rest of the file.
        @return     None
    """

    print_lines(["The default file for parsing is input.pdf",
                 "Please ensure that this exists."," ",
                 "Press any key to continue...",])
    input()

    if not file_exists(input):
        raise(FileNotFoundError)
        exit(1)

    pdf_text = textract.process(input, method='pdftotext')

def print_lines(lines: list[str]) -> None:
    for line in lines:
        print(line)