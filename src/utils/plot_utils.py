from pathlib import Path
import matplotlib.pyplot as plt

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "reports" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_figure(name: str, dpi: int = 300):
    plt.savefig(
        OUTPUT_DIR / f"{name}.png", dpi=dpi, bbox_inches="tight", facecolor="white"
    )
    print(f"✅ Figure saved to: {OUTPUT_DIR / f'{name}.png'}")
