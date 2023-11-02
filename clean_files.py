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


LAST_CHAR = "\r\n"

class Clean_import_wx(IValidator):
    @staticmethod
    def convert_str(line: str)->str:
        pattern = re.compile(r"(?<=^import\s)(wx,?\s?)")
        if pattern.search(line):
            if "," in line:
                return pattern.sub("",line)
            else:
                return None
        return line

class Clean_UnderScoreUnicode(IValidator):
    @staticmethod
    def convert_str(line: str)->str:
        pattern = re.compile(r"_\(\s*u?('.*?')\)")
        if pattern.search(line):
            line = pattern.sub(r"\1",line)
        return line
    
class CleanWX_StaticText(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r".+wx\.StaticText\(")
        if pattern.search(line):
            return None
        return line

class CleanWX_StaticBox(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r".+wx\.StaticBox\(")
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

class Clean_WX_Panel(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"wx\.Panel\.__init__\(")
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
    pattern = re.compile(r"(.+ =)\s?wx\.TextCtrl\(.+, value=(.+)\)")

    @classmethod
    def convert_str(cls, line: str) -> str:

        text_ctrl = re.compile(r"wx\.TextCtrl\(")
        if text_ctrl.search(line):
            if re.search(r"value=",line):
                line = " ".join(cls.pattern.search(line).group(1,2))+ LAST_CHAR 
            else:
                return None
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
            return pattern.sub(r"",line)
        return line

class Clean_WX_SetValue(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"\.SetValue\((.*?)\)")
        if pattern.search(line):
            line = pattern.sub(r"= \1",line)
        return line

class Clean_WX_RadioButton(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"(wx\.RadioButton\(.+\))")
        if pattern.search(line):
            line = pattern.sub(r"False # or True, era un CheckBox que debia elegir el usuario",line)
        return line

class Clean_WX_CheckBox(IValidator):
    tab= lambda line: re.compile(r"^(\s+)\w").search(line).group(1)
    var_name= lambda line: re.compile(r"\s+(self\.\w+)\s?(?==)").search(line).group(1)
    label= lambda line: re.compile(r"label\s?=\s?'(.+?)'").search(line).group(1)

    @classmethod
    def convert_str(cls, line: str) -> str:
        pattern = re.compile(r"wx\.CheckBox\(")
        if pattern.search(line):
            line = cls.tab(line)+ "# " + cls.var_name(line)+ cls.label(line) + LAST_CHAR
        return line

class Clean_WX_SetBackgroundStyle(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"\.SetBackgroundStyle\(")
        if pattern.search(line):
            return None
        return line

class Clean_WX_MessageBoxAsRaise_print(IValidator):
    is_raise:re.Pattern = re.compile(r",\s?(_\()?'Aviso'\)?")

    @classmethod
    def convert_str(cls, line: str) -> str:
        pattern = re.compile(r"wx\.MessageBox")
        if pattern.search(line):
            if cls.is_raise.search(line) is None:
                return pattern.sub(r"print",line)
            else:
                line = pattern.sub(r"raise Exception",line)
                return cls.is_raise.sub(")",line)
        return line

class Clean_MiChoice(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"MiChoice\(choices=(.+?),.+")
        if pattern.search(line):
            line = pattern.sub(r"MiChoice(choices=\1)",line)
        return line

class Clean_WX_Heritage(IValidator):
    @staticmethod
    def convert_str(line: str) -> str:
        pattern = re.compile(r"(?<=class )(\w+)\b\(wx\.(Dialog|Panel|Frame)\)")
        if pattern.search(line):
           return f"class {pattern.search(line).group(1)}():{LAST_CHAR}"
        return line




class FixLines():
    def __init__(self, line) -> None:
        self._line = line
        self._validator:list[IValidator] = (
            Clean_import_wx,
            Clean_UnderScoreUnicode,
            CleanWX_StaticText,
            CleanWX_StaticBox,
            CleanWX_SetFont,
            CleanWX_SetClientSize,
            CleanWX_SetForegroundColour,
            CleanWX_SetBackgroundColour,
            Clean_WX_Dialog,
            Clean_WX_Panel,
            Clean_WX_Button,
            Clean_WX_TextCtrl,
            Clean_WK_CONST,
            Clean_Show_method,
            Clean_WX_Bind,
            Clean_WX_GetValue,
            Clean_WX_SetValue,
            Clean_WX_RadioButton,
            Clean_WX_CheckBox,
            Clean_WX_SetBackgroundStyle,
            Clean_WX_MessageBoxAsRaise_print,
            Clean_MiChoice,
            Clean_WX_Heritage
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
        old_name.unlink()
        new_name.rename(new_name.with_name(old_name.name))
        count+=1
    return count
        

if __name__ == "__main__":
    ruta= Path.home()/"Downloads"/"cex"/"cex2_1_custom"
    
    rutas = [x for x in ruta.iterdir() if x.is_dir()]
    for x in rutas:
        count = clean_path(x)
        print(f"Se han modificado '{count}' ficheros en {x.stem}")