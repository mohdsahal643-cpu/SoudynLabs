"""Phase 0: preserve source artwork and prepare self-hosted Latin fonts.

Run with Pillow, fontTools and Brotli available on PYTHONPATH.
"""

from io import BytesIO
from pathlib import Path
import math
import re
import urllib.request

from PIL import Image
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent


def prepare_logo():
    source = Image.open(ROOT / "assets/img/soudyn-logo-source.webp").convert("RGBA")
    alpha = source.getchannel("A")
    bounds = alpha.getbbox()
    print("Source artwork bounds:", bounds)
    # The mark is separate from the wordmark. Find the first empty column
    # after the mark, retaining every original non-transparent pixel.
    left, top, right, bottom = bounds
    split = next(x for x in range(left + 40, right)
                 if alpha.crop((x, top, x + 1, bottom)).getbbox() is None)
    mark_bounds = alpha.crop((left, top, split, bottom)).getbbox()
    mark = source.crop((left + mark_bounds[0], top + mark_bounds[1],
                        left + mark_bounds[2], top + mark_bounds[3]))
    padding = math.ceil(mark.height / 2)
    for name, artwork in (("soudyn-logo", source.crop(bounds)), ("soudyn-mark", mark)):
        padded = Image.new("RGBA", (artwork.width + 2 * padding,
                                    artwork.height + 2 * padding))
        padded.paste(artwork, (padding, padding))
        # Source-resolution pixels support display at half the exported size.
        padded.save(ROOT / f"assets/img/{name}-2x.webp", lossless=True, exact=True)
        print(name, padded.size, "artwork:", artwork.size, "padding:", padding)


def prepare_fonts():
    css_url = ("https://fonts.googleapis.com/css2?family=Outfit:wght@600;700"
               "&family=Source+Sans+3:wght@400;600&display=swap")
    request = urllib.request.Request(css_url, headers={"User-Agent": "Mozilla/5.0"})
    css = urllib.request.urlopen(request).read().decode("utf-8")
    fallback_rules = []
    for block in re.findall(r"@font-face\s*\{([^}]+)\}", css):
        family = re.search(r"font-family:\s*'([^']+)'", block)[1]
        weight = re.search(r"font-weight:\s*(\d+)", block)[1]
        url = re.search(r"url\(([^)]+)\)", block)[1]
        font = TTFont(BytesIO(urllib.request.urlopen(url).read()))
        opts = subset.Options()
        opts.flavor = "woff2"
        sub = subset.Subsetter(options=opts)
        sub.populate(unicodes=list(range(0x20, 0x100)) + [0x131, 0x152, 0x153,
                     0x2BB, 0x2BC, 0x2C6, 0x2DA, 0x2DC, *range(0x2000, 0x2070),
                     0x20AC, 0x2122, 0x2191, 0x2193, 0x2212, 0x2215, 0xFEFF, 0xFFFD])
        sub.subset(font)
        font.flavor = "woff2"
        slug = family.lower().replace(" ", "-")
        output = ROOT / f"assets/fonts/{slug}-latin-{weight}.woff2"
        font.save(output)
        print(output.name, output.stat().st_size)
        local_font = "Segoe UI" if weight == "400" else "Segoe UI Semibold" if weight == "600" else "Segoe UI Bold"
        local_path = "segoeui.ttf" if weight == "400" else "seguisb.ttf" if weight == "600" else "segoeuib.ttf"
        fallback = TTFont(Path("C:/Windows/Fonts") / local_path)
        # Match average advance width, then compensate vertical metrics.
        sample = "Software that takes repetitive work off your team."
        def average_width(f):
            cmap = f.getBestCmap()
            return sum(f["hmtx"][cmap[ord(c)]][0] for c in sample) / len(sample) / f["head"].unitsPerEm
        adjustment = average_width(font) / average_width(fallback)
        upm = font["head"].unitsPerEm
        metrics = font["hhea"]
        fallback_rules.append(
            '@font-face {\n'
            f'  font-family: "{family} fallback";\n'
            f'  src: local("{local_font}");\n'
            f'  font-style: normal;\n  font-weight: {weight};\n'
            f'  size-adjust: {adjustment * 100:.4f}%;\n'
            f'  ascent-override: {metrics.ascent / upm / adjustment * 100:.4f}%;\n'
            f'  descent-override: {abs(metrics.descent) / upm / adjustment * 100:.4f}%;\n'
            f'  line-gap-override: {metrics.lineGap / upm / adjustment * 100:.4f}%;\n'
            '}\n')
    (ROOT / "assets/css/font-fallbacks.css").write_text("\n".join(fallback_rules), encoding="ascii")
    for family, folder in (("Outfit", "outfit"), ("Source Sans 3", "sourcesans3")):
        url = f"https://raw.githubusercontent.com/google/fonts/main/ofl/{folder}/OFL.txt"
        (ROOT / f"assets/fonts/{folder}-OFL.txt").write_bytes(urllib.request.urlopen(url).read())


if __name__ == "__main__":
    prepare_logo()
    prepare_fonts()
