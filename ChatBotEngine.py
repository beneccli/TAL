from people import People
import re

class ChatBotEngine:

    def normalise(str):
        str = re.sub("\'\'", '"', str)  # two single quotes = double quotes
        str = re.sub("[`‘’]+", r"'", str)  # normalise apostrophes/single quotes
        str = re.sub("[≪≫“”]", '"', str)  # normalise double quotes
        replacements = [("cb", "combien"), ("slt", "salut"), ("bcp", "beaucoup"), ("cmt", "comment"), ("cc", "coucou")]
        for (original, replacement) in replacements:
            str = re.sub("(^| )" + original + "( |$)", r"\1" + replacement + r"\2", str)
        return str


    # Va lire une phrase et en sortir les tokens
    def tokenize(str):
        str = str.lower()
        str = ChatBotEngine.normalise(str)
        str = re.sub("([^ ])\'", r"\1 '", str)  # separate apostrophe from preceding word by a space if no space to left
        str = re.sub(" \'", r" ' ", str)  # separate apostrophe from following word if a space to left

        # separate on punctuation
        cannot_precede = ["M", "Prof", "Sgt", "Lt", "Ltd", "co", "etc", "[A-Z]", "[Ii].e", "[eE].g"]  # non-exhaustive list
        regex_cannot_precede = "(?:(?<!" + ")(?<!".join(cannot_precede) + "))"
        str = re.sub(regex_cannot_precede + "([\.\,\;\:\)\(\"\?\!]( |$))", r" \1", str)
        str = re.sub("((^| )[\.\?\!]) ([\.\?\!]( |$))", r"\1\2", str)  # then restick several fullstops ... or several ?? or !!
        str = str.split()  # split on whitespace
        return str

    @staticmethod
    def talk(str):
        tokens = ChatBotEngine.tokenize(str)
        return tokens