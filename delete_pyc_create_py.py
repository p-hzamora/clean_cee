from pathlib import Path

def create(ruta:Path)-> None:
    """
    Especificando la ruta raiz, se recorren los ficheros de forma recursiva para cambiar los ".pyc_dis" por ".py" y eliminar los ".pyc"
    """
    for x in ruta.rglob("*"):
        if x.suffix == ".pyc_dis":
            print("rename ",x.name)
            x.rename(x.with_suffix(".py"))
        elif x.suffix ==".pyc":
            print("delete ",x.name)
            x.unlink()
        else:
            print("No se llevó a cabo ninguna modificación")

if __name__ == "__main__":
    
    ruta = Path.home()/"Desktop"/"stc_project"/"stc"/"sos"/"sos_uci"/"scripts"/"cex"/"cex2_1_custom"/"dependencies"
    create(ruta)
