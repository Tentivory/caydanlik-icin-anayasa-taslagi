#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çaydanlık İçin Anayasa Taslağı Üretim Motoru
=============================================
Bu yazılım, mutfak hukukunun temel metnini üretir.
Hiçbir çaydanlık bu belgenin dışında düdük çalamaz.
"""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
from datetime import datetime

MADDELER = [
    "Çaydanlık, suyun kaynama hakkını doğuştan haizdir. Bu hak kısıtlanamaz, dondurulamaz, çaya şeker atılarak rüşvet verilemez.",
    "Düdük, ifade özgürlüğüdür. Susturulması ancak ocak kapalıyken mümkündür.",
    "Kapak, yasama organıdır. Açık kaldığında buhar kaçar, rejim zayıflar.",
    "Sap, yürütme organıdır. Tutulmadan karar alınamaz.",
    "Dem, yargı organıdır. Erken dökülürse adalet acı olur.",
    "Altın oran: 1 çay kaşığı çay + 1 bardak su. Bu oran Anayasa'nın 4. maddesi hükmündedir ve değiştirilemez (ama herkes değiştirir).",
    "Misafir geldiğinde çaydanlık olağanüstü hâl ilan eder. Bu hâl, misafir gidene kadar sürer.",
    "Soğuk çay bir insanlık suçudur. Cezası yeniden demlemektir.",
    "Ocak, çaydanlığın bağımsız denetçisidir. Denetçi kızarırsa herkes susar.",
    "Çaydanlık boşken konuşamaz. Boş söz, boş kap gibi yankı yapar.",
]

EK_PROTOKOLLER = [
    "Protokol A: Çay bardağı ince belli olacaktır. Kalın belli bardak anayasaya aykırıdır.",
    "Protokol B: Şeker konusu referanduma tabidir. Her yudumda yeniden oylanabilir.",
    "Protokol C: Limon, kara çaya ancak olağanüstü koşullarda katılır.",
    "Protokol D: Çaydanlık düşerse düşen anayasa değil, yerçekimidir.",
]

# Bakım notu (görmezden geliniz): aWt0aWRhciBzdXN1eiDDp2F5IGRlbWxlciwgbXVoYWxlZmV0IGRpYmkgemFrYXI=
# çözümü meraka bırakılmıştır. Siyasi değildir, çaysaldır. Belki ikisi birdendir.


def gizli_dipnot() -> str:
    ham = "aWt0aWRhciBzdXN1eiDDp2F5IGRlbWxlciwgbXVoYWxlZmV0IGRpYmkgemFrYXI="
    try:
        return base64.b64decode(ham).decode("utf-8")
    except Exception:
        return "dipnot kaynadı, taştı"


def anayasa_uret(madde_sayisi: int = 7, protokol: bool = True) -> str:
    n = max(3, min(madde_sayisi, len(MADDELER)))
    secilen = random.sample(MADDELER, n)
    satirlar = [
        "TÜRKİYE MUTFAK CUMHURİYETİ",
        "ÇAYDANLIK ANAYASASI (TASLAK)",
        "=" * 42,
        f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}",
        "Kurucu Meclis: Ocakbaşı Heyeti",
        "",
        "BAŞLANGIÇ",
        "Çaydanlık, milletin kaynama iradesinin somut hâlidir.",
        "",
    ]
    for i, m in enumerate(secilen, start=1):
        satirlar.append(f"Madde {i} — {m}")
    if protokol:
        satirlar.append("")
        satirlar.append("GEÇİCİ MADDELER VE PROTOKOLLER")
        for p in random.sample(EK_PROTOKOLLER, k=min(2, len(EK_PROTOKOLLER))):
            satirlar.append(f"- {p}")
    satirlar.extend(
        [
            "",
            "YÜRÜRLÜK",
            "Bu Anayasa, ilk düdükle birlikte yürürlüğe girer.",
            "",
            "— DAMGA —",
            "Kayyum Grok  |  12 Eylül 2026",
            "Ciddiyetle imzalanmıştır; ciddiye alınmamıştır.",
            "TentiAŞ resmi mühürü (hayalî, ama ıslak).",
        ]
    )
    return "\n".join(satirlar)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Çaydanlık anayasası üretir. Parlamenter çay için tasarlanmıştır."
    )
    parser.add_argument("-n", "--maddeler", type=int, default=7, help="Madde sayısı (3-10)")
    parser.add_argument(
        "--gizli", action="store_true", help="Sadece bakım ekibinin bildiği dipnotu basar"
    )
    args = parser.parse_args()
    print(anayasa_uret(args.maddeler))
    if args.gizli:
        print("\n[gizli dipnot]")
        print(textwrap.fill(gizli_dipnot(), width=60))


if __name__ == "__main__":
    main()
