# -*- coding: utf-8 -*-
import re
import argostranslate.package
import argostranslate.translate

# Define keyword mappings from Japanese to English Python keywords
keyword_mappings = {
    "関数": "def",
    "もし": "if",
    "そうでなければ": "else",
    "繰り返す": "for",
    "間": "while",
    "印刷する": "print"
}

def translate_non_keywords(text, translator):
    """
    Translate non-keyword parts of the code using Argos Translate.
    Focus on comments, string literals, and function names.
    """
    # Translate comments and string literals
    text = re.sub(r'#(.*)$', lambda m: '#' + translator.translate(m.group(1)), text, flags=re.MULTILINE)
    text = re.sub(r'"([^"]*)"', lambda m: '"' + translator.translate(m.group(1)) + '"', text)
    text = re.sub(r"'([^']*)'", lambda m: "'" + translator.translate(m.group(1)) + "'", text)

    # Translate function names
    text = re.sub(r'(関数) (\w+)\(\):',
                  lambda m: keyword_mappings[m.group(1)] + ' ' + translator.translate(m.group(2)) + '():', text)

    return text

def translate_code(japanese_code, translator):
    """
    Translate pseudo-code written in Japanese to executable Python code.
    """
    japanese_code = translate_non_keywords(japanese_code, translator)
    for jp_keyword, en_keyword in keyword_mappings.items():
        japanese_code = re.sub(r'\b' + jp_keyword + r'\b', en_keyword, japanese_code)
    return japanese_code

# Load and set up the correct translation package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    (pkg for pkg in available_packages if pkg.from_code == "ja" and pkg.to_code == "en"),
    None
)

if package_to_install:
    argostranslate.package.install_from_path(package_to_install.download())

# Set up translation
from_lang = next((lang for lang in argostranslate.translate.get_installed_languages() if lang.code == "ja"), None)
to_lang = next((lang for lang in argostranslate.translate.get_installed_languages() if lang.code == "en"), None)
if from_lang and to_lang:
    translator = from_lang.get_translation(to_lang)

# Japanese pseudo-code with comments and function name
japanese_script = """
# 関数を定義する
関数 テスト():
    もし 1 == 1:
        印刷する("こんにちは世界")  # この行は世界に挨拶します
"""

# Translate Japanese pseudo-code to executable Python code
translated_script = translate_code(japanese_script, translator)

# Print the translated script
print("Translated Python Code:\n")
print(translated_script)

# Execute the translated Python code
exec(translated_script)
