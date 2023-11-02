"""
Elimina todos los strings que tienen la forma _(u'xxxxxx') y los reemplaza por u'xxxxxxx'

"""

import re
import copy
import codecs
from pathlib import Path
from abc import ABC,abstractmethod

class IValidator(ABC):
    @abstractmethod
    def convert_str(line:str)->str: ...



class DeleteUnderScoreUnicode(IValidator):
    @staticmethod
    def convert_str(line: str)->str:
        pattern = re.compile(r"_\(\s*u?('.*?')\)")
        if pattern.search(line):
            line = pattern.sub(r"\1",line)
        return line
    
class CleanWX_StaticText(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        # pattern = re.compile(r"*+wx\.StaticText\(id=.+, label=.+, name=.+, parent=.+, pos=.+, size=.+, style=.+\)")
        pattern = re.compile(r".+wx\.StaticText\(id=.+, label=.+, name=.+, parent=.+, pos=.+, size=.+, style=.+\)")
        if pattern.search(line):
            return None
        return line

class CleanWX_SetFont(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r".+\.SetFont\(wx\.Font")
        if pattern.search(line):
            return None
        return line

class CleanWX_SetClientSize(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r".+\.SetClientSize\(wx\.Size")
        if pattern.search(line):
            return None
        return line

class CleanWX_SetForegroundColour(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r".+\.SetForegroundColour\(wx\.Colour")
        if pattern.search(line):
            return None
        return line

class CleanWX_SetBackgroundColour(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r".+\.SetBackgroundColour\(")
        if pattern.search(line):
            return None
        return line

class Clean_WX_Dialog(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"wx\.Dialog\.__init__\(")
        if pattern.search(line):
            return None
        return line

class Clean_WX_Button(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"wx\.Button\(")
        if pattern.search(line):
            return None
        return line

class Clean_WX_TextCtrl(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        SPACE_CHAR = "\r\n"

        pattern = re.compile(r"(.+ =)\s?wx\.TextCtrl\(.+, value=(.+)\)")
        if pattern.search(line):
            line = " ".join(pattern.search(line).group(1,2))+ SPACE_CHAR 
        return line

class Clean_WK_CONST(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"\[ wx\.NewId\(\) for _init_ctrls in range\(")
        if pattern.search(line):
            return None
        return line

class Clean_Show_method(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"\.Show\((False|True)\)")
        if pattern.search(line):
            return None
        return line

class Clean_WX_Bind(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"\.Bind\(wx\.")
        if pattern.search(line):
            return None
        return line

class Clean_WX_GetValue(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"\.GetValue\(\)")
        if pattern.search(line):
            None
        return line

class Clean_WX_SetValue(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"\.SetValue\((.*?)\)")
        if pattern.search(line):
            line = pattern.sub(r"= \1",line)
        return line


class Clean_WX_CheckBox(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r".+\s?=\s?wx\.CheckBox\(.+(label=\s?.*?,\s?name=.*)\)")
        if pattern.search(line):
            line = pattern.sub(r"# \1",line)
        return line






class FixLines():
    def __init__(self, line) -> None:
        self._line = line
        self._validator:list[IValidator] = (
            DeleteUnderScoreUnicode,
            CleanWX_StaticText,
            CleanWX_SetFont,
            CleanWX_SetClientSize,
            CleanWX_SetForegroundColour,
            CleanWX_SetBackgroundColour,
            Clean_WX_Dialog,
            Clean_WX_Button,
            Clean_WX_TextCtrl,
            Clean_WK_CONST,
            Clean_Show_method,
            Clean_WX_Bind,
            Clean_WX_GetValue,
            Clean_WX_SetValue,
            Clean_WX_CheckBox
        )

    def fix(self)-> str:
        for func in self._validator:
            # si al aplicar los validadores alguno devuelve None, en la siguiente iteracion retornamos None
            if self._line is None:
                return None
            self._line = func.convert_str(self._line)
        return self._line
    


def clean_path(ruta:Path)->int:
    count = 0
    for x in ruta.rglob("*.py"):
        old_name = x
        new_name = x.with_name(f"{x.stem}_modified.py")
        # read old .py file and write new lines on new_name file
        with codecs.open(old_name,"r",encoding="utf-8") as source, codecs.open(new_name,"w",encoding="utf-8") as destination:
            avoid:bool = False
            for line in source:
                if line.strip()== '"""' and avoid is False:
                    avoid = True
                    continue
                elif line.strip()== '"""' and avoid is True:
                    avoid = False
                    continue
                if not avoid:
                    new_line = FixLines(line).fix()
                    if new_line is not None:
                        destination.write(new_line)


        # deleted old file and rename the new one with the old name to avoid concurrency
        # old_name.unlink()
        # new_name.rename(new_name.with_name(old_name.name))
        count+=1
    return count
        

if __name__ == "__main__":
    ruta = Path.home()/"Downloads"/"cex"/"cex2_1_custom"/"MedidasDeMejora"

    total = clean_path(ruta)
    print(f"Se han modificado '{total}' ficheros")