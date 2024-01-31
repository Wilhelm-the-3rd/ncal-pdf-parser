import os
import fitz

"""
This file is intended to parse PDF files containing NCAL questions into a format.
These questions are outputted into the file question.txt. organize.py is intended
to be used to organize the questions into separate question files for category.
"""

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


def file_exists(file_path: str) -> bool:
    """
        @return     True if file exists, False otherwise
        @rtype      bool
    """
    return os.path.exists(file_path)


def write(file_path: str, new_line: str) -> None:
    """
        Writes new line to file
        @return     None
    """

    with open(file_path) as file:
        file.write(new_line + "\n")


def text_from_pdf(file_path: str) -> list[str]:
    """
        Extracts text from a pdf file
        @return     Text as a string
        @rtype      str
    """
    out = []

    for page in fitz.open(file_path):
        out.append(page.get_text())

    return out


def process_text(pages: list[str], output_path: str) -> None:
    """
        Processes text into question format and outputs to file
        @return     None
    """
    for page in
