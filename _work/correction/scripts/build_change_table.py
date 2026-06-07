from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "_work" / "correction" / "change_table.md"


ROWS = [
    {
        "dosya": "README.md",
        "eklenen_metin_ozeti": "Repo'nun kişisel gözlem/yeniden kurulum dosyası olduğu netleştirildi; kişi adı sansürü bağlamı eklendi.",
        "eklenen_gorseller": "-",
        "uygulanan_sansur": "Kişi adlarının public metinde `[SANSÜR]` kalacağı açıklandı.",
        "render_durumu": "Görsel yok; docs linkleri çözümleniyor.",
    },
    {
        "dosya": "docs/tarih-olcek-ve-bakim.md",
        "eklenen_metin_ozeti": "Şirket yapısı, tarihsel izler, Silahtarağa, Eskişehir/Turhal, kalite sapması, finansal ölçek ve gaz türbini bakım notları geri yüklendi.",
        "eklenen_gorseller": "9 görsel: şirket yapısı, Silahtarağa, santral yaşı, ölçek analojileri, finansal ölçek, şeker fabrikası ve bakım.",
        "uygulanan_sansur": "Public metinde gerçek kişi adı bırakılmadı.",
        "render_durumu": "`../assets/...` yolları ve alt metinler doğrulandı.",
    },
    {
        "dosya": "docs/hidrojen-ve-enerji-depolama.md",
        "eklenen_metin_ozeti": "Hidrojen üretim türleri, araç/altypı tartışması, ülke/kurum teşvikleri, NREL teknoloji eğrisi, verimlilik itirazı ve depolama akışı genişletildi.",
        "eklenen_gorseller": "9 görsel: üretim yolları, AB/NREL, NREL PV çizelgeleri, verimlilik zinciri, kayıp karşılaştırması, istasyon ve depolama.",
        "uygulanan_sansur": "Kişisel anlatım kaynakları public metinde isimsiz bırakıldı.",
        "render_durumu": "`../assets/...` yolları ve alt metinler doğrulandı.",
    },
    {
        "dosya": "docs/verimlilik-hipotez-ve-insan-makine.md",
        "eklenen_metin_ozeti": "Thermoflow notu, insan/çeki hayvanı hipotezi, kalori hesabı, T3000, operatör rolü ve Lorentz/model güncelleme akışı güçlendirildi.",
        "eklenen_gorseller": "4 görsel: Thermoflow, at kalori kaynağı, T3000 kontrol odası ve Lorentz/yük devresi.",
        "uygulanan_sansur": "Stajdaki konuşma kişileri `[SANSÜR]` biçiminde bırakıldı.",
        "render_durumu": "`../assets/...` yolları ve alt metinler doğrulandı.",
    },
    {
        "dosya": "docs/kaynakca-ve-sekil-notlari.md",
        "eklenen_metin_ozeti": "Kaynakça ve final görsel eşleştirme tablosu güncellendi; belirsiz kaynaklar açık notlandı.",
        "eklenen_gorseller": "Görsel eklenmedi; 22 final görselin izleme tablosu eklendi.",
        "uygulanan_sansur": "Kaynakça ve kişisel görüşme/soru-cevap satırlarındaki hedef kişi adları sansürlendi.",
        "render_durumu": "Şekil tablosu gerçek public görsel referanslarıyla eşleşiyor.",
    },
]


def commits_for(path: str) -> str:
    result = subprocess.run(
        ["git", "log", "--oneline", "--", path],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=True,
    )
    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return "<br>".join(lines[:5]) if lines else "-"


def main() -> int:
    lines = [
        "# Change Table",
        "",
        "| dosya | eklenen_metin_ozeti | eklenen_gorseller | uygulanan_sansur | render_durumu | ilgili_commitler |",
        "|---|---|---|---|---|---|",
    ]
    for row in ROWS:
        commits = commits_for(row["dosya"])
        lines.append(
            "| {dosya} | {eklenen_metin_ozeti} | {eklenen_gorseller} | {uygulanan_sansur} | {render_durumu} | {commits} |".format(
                commits=commits,
                **row,
            )
        )
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"BUILD_CHANGE_TABLE_OK path={OUT.relative_to(ROOT).as_posix()} rows={len(ROWS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
