from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager
import arabic_reshaper
from bidi.algorithm import get_display

# ===============================
# Project Color Palette
# ===============================


def fa(text: str) -> str:
    """
    Convert Persian text to a format that Matplotlib can display correctly.
    """
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


"""
| نوع نمودار           | رنگ     | کد                       |
| -------------------- | ------- | ------------------------ |
| 📈 Trend             | آبی     | `COLORS["trend"]`        |
| 📊 Distribution      | نارنجی  | `COLORS["distribution"]` |
| 📉 Comparison        | سبز     | `COLORS["comparison"]`   |
| ⚠️ Outlier / Warning | قرمز    | `COLORS["warning"]`      |
| 🟣 Secondary         | بنفش    | `COLORS["secondary"]`    |
| ⚪ Neutral            | خاکستری | `COLORS["neutral"]`      |


| نوع سؤال            | رنگ                |
| ------------------- | ------------------ |
| Trend               | 🔵 آبی             |
| Histogram           | 🟠 نارنجی          |
| Boxplot             | 🟠 نارنجی          |
| Bar Chart           | 🟢 سبز             |
| Correlation Heatmap | 🟣 بنفش            |
| Geographic Heatmap  | 🔴 طیف داغ (`hot`) |
| Scatter Plot        | 🔵 آبی             |
| Outliers            | 🔴 قرمز            |


"""

COLORS = {
    "trend": "#1f77b4",  # Blue
    "distribution": "#ff7f0e",  # Orange
    "comparison": "#2ca02c",  # Green
    "warning": "#d62728",  # Red
    "secondary": "#9467bd",  # Purple
    "neutral": "#7f7f7f",  # Gray
}


def set_plot_style():
    """
    Configure matplotlib style for the entire project.
    """

    plt.style.use("default")

    # ---------- Figure ----------
    plt.rcParams["figure.figsize"] = (12, 6)
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["savefig.dpi"] = 300

    # ---------- Grid ----------
    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.alpha"] = 0.30
    plt.rcParams["grid.linestyle"] = "--"

    # ---------- Titles ----------
    plt.rcParams["axes.titlesize"] = 16
    plt.rcParams["axes.titleweight"] = "bold"

    # ---------- Labels ----------
    plt.rcParams["axes.labelsize"] = 13

    # ---------- Tick Labels ----------
    plt.rcParams["xtick.labelsize"] = 11
    plt.rcParams["ytick.labelsize"] = 11

    # ---------- Legend ----------
    plt.rcParams["legend.fontsize"] = 11

    # ---------- Lines ----------
    plt.rcParams["lines.linewidth"] = 2.5
    plt.rcParams["lines.markersize"] = 6

    # ---------- Font ----------
    font_path = Path("../assets/fonts/Vazirmatn-Regular.ttf")

    if font_path.exists():

        font_manager.fontManager.addfont(str(font_path))

        font_name = font_manager.FontProperties(fname=str(font_path)).get_name()

        plt.rcParams["font.family"] = font_name

    plt.rcParams["axes.unicode_minus"] = False
