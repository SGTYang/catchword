# Catchword
Catchword prints out the matched lowercase words from the file. Search term exists on the last line of the file at all times. If there is no match, "**There is no word that matches with Search Term!**" will be printed out on console.

The search function was implemented by using **"Prefix Tree"**.

I try to follow [this][google/styleguide] style guide for this project. Check my docstrings and comments for detailed explanations. 

[google/styleguide]: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

# Setup
This project uses "setup.py" for packaging project. But since it is not recommened way for packaging the project, [this][packaging] can be followed instead of using "setup.py".

[packaging]: https://packaging.python.org/en/latest/tutorials/packaging-projects/

## Check Python version
This project needs **Python** version that is greater than or equal to **3.10**.
```
python --version
```

## Install
```
pip install catchword
```

## Usage
"FILEPATH" should be absolute path of a file.
```
wordsearch ["FILEPATH"]
```