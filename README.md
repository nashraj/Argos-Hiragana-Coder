[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![](https://img.shields.io/badge/lang-jp-green.svg)](README-JP.md)

![image](https://github.com/user-attachments/assets/3dd8db10-faa7-46ca-a1a1-762a90d4d5a2)

# Argos-Hiragana-Coder
Argos Hiragana Coder is a Python utility that translates Python-like pseudo-code written in Japanese (Hiragana) into executable Python code using English syntax using the Argos Translate Library

Leveraging the open-source Argos Translate library, this tool is designed to assist Japanese speakers in learning Python programming by allowing them to start coding in their native language. It automates the translation of keywords, comments, string literals, and function names from Japanese to English, facilitating a smoother learning curve and bridging language barriers in coding education.

## Features:
Keyword Translation: Automatically converts Japanese Python-like keywords into their English counterparts.
Comment and String Literal Translation: Translates comments and string literals within the code to English.
Function Name Translation: Handles the translation of function names defined in Japanese to English.
Interactive Execution: After translation, the Python code is executed, displaying results immediately for validation and learning purposes.

## Installation:
- Ensure Python is installed on your system.
- Install Argos Translate and necessary language packages via pip
- Download and install the Japanese to English translation package from within the script.

## Running the Script:
- Place your Japanese pseudo-code within the japanese_script variable.
- Run the script to see the translated English Python code and execute it.
- The output will display the translation and any execution results in the console.

## Modifying the Code:
You can add or modify entries in the keyword_mappings dictionary to extend or customize the keyword translations.

## Contributing:
Contributions are welcome! If you have suggestions for improving the translations, adding features, or fixing bugs, please fork the repository and submit a pull request, or open an issue to discuss your ideas.

## Acknowledgements:
This project utilizes Argos Translate, an open-source library for neural machine translation. We are grateful for the hard work and dedication of the Argos Translate team and the broader community that supports it. This library is crucial for our project as it provides the core translation capabilities enabling our script to convert Japanese pseudo-code into executable Python code.
