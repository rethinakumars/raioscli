import typer
from raioscli.core.commands import handle_storageo, handle_storageb

app = typer.Typer(help="RAIOSCLI — Unified Multi‑Cloud + Hypervisor CLI")

@app.command()
def storageo(action: str, name: str, sync: str = ""):
    """
    Object storage operations (S3 / GCS / Blob / RAIOS StorageO)
    """
    handle_storageo(action, name, sync)

@app.command()
def storageb(action: str, name: str, size: str = "20GB", sync: str = ""):
    """
    Block storage operations (EBS / PD / Managed Disk / RAIOS StorageB)
    """
    handle_storageb(action, name, size, sync)

if __name__ == "__main__":
    app()

