from pathlib import Path
import subprocess

ruta = Path.home()/"Downloads"/"cex"/"cex2_1_original_py"
not_uncompyle = []
for el in ruta.rglob("*.pyc"):
    if el.suffix == ".pyc":
        res= subprocess.call(f"uncompyle6 -o {str(el.parent)} {str(el)}",shell=False)
        if res == 0:
            el.unlink()
        else:
            el.with_suffix(".py").unlink()
            not_uncompyle.append(el)

print("\n"*5)
print("Archivos NO descomprimidos")
for x in not_uncompyle:
    print(x)