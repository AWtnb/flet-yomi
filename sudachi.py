import re

import sudachidict_core
from sudachipy import Tokenizer, Dictionary, Morpheme


class SudachiToken:
    def __init__(self, morpheme: Morpheme) -> None:
        self.surface = morpheme.surface()
        self.pos = morpheme.part_of_speech()[0]
        self.reading = morpheme.reading_form()

    def get_katakana_surface(self) -> str:
        return "".join([chr(ord(c) + 96) if (0x3041 <= ord(c) <= 0x3094) else c for c in self.surface])


class TokenParser:
    def __init__(self, token:SudachiToken) -> None:
        surface = token.surface
        reg = re.compile(r"^([ぁ-んァ-ヴ・ー]|[a-zA-Z\uff41-\uff5a\uff21-\uff3a]|[0-9\uff10-\uff19]|[\W\s])+$")
        if "記号" in token.pos or "空白" in token.pos or reg.match(surface) :
            if re.match(r"[ぁ-ん]", surface):
                self.reading = token.get_katakana_surface()
            else:
                self.reading = surface
            self.detail = surface
            return
        if len(token.reading) < 1:
            self.reading = surface
            self.detail = surface + "(?)"
            return
        self.reading = token.reading
        self.detail = "{}({})".format(surface, self.reading)

class TokensReader:
    def __init__(self, raw_tokens:list[SudachiToken]) -> None:
        self.tokens = [TokenParser(token) for token in raw_tokens]

    def get_reading(self) -> str:
        return "".join([token.reading for token in self.tokens])

    def get_detail(self) -> str:
        return " / ".join([token.detail for token in self.tokens])

class ParsedLine:
    def __init__(self) -> None:
        self.line = ""
        self.tokens = []

def tokenize(lines:list[str], ignore_paren:bool=False) -> list[ParsedLine]:
    reg = re.compile(r"\(.+?\)|\[.+?\]|\uff08.+?\uff09|\uff3b.+?\uff3d")
    tknzr = Dictionary().create()
    out = []
    for line in lines:
        pl = ParsedLine()
        if line:
            if ignore_paren:
                pl.line = reg.sub("", line)
            else:
                pl.line = line
            for morpheme in tknzr.tokenize(pl.line, Tokenizer.SplitMode.C):
                st = SudachiToken(morpheme)
                pl.tokens.append(st)
        out.append(pl)
    return out


