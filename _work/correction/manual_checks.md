# Manual Checks

Bu fazda public markdown dosyaları notebook'a daha sadık hale getirildi. Aşağıdaki noktalar bilinçli olarak ihtiyatla bırakıldı; bir sonraki turda gerekiyorsa tek tek doğrulanmalı.

## Kaynak / Doğrulama Gerektirenler

- Siemens'in Osmanlı telgraf sistemi için defterde geçen `1856` yılı: metinde kesin tarih iddiası gibi büyütülmedi.
- Enerji Bakanlığı raporunun yılı: metinde yıl yazılmadı.
- Ambarlı Termik Santrali için `%51`, Samsun Doğalgaz Çevrim Santrali için `%61` rekor notu: dış doğrulama yapılmadan yalnızca notebook izi olarak geçti.
- Eskişehir/Turhal türbinleri ve yaklaşık 70 yıllık çalışma anlatısı: kişisel tanıklık düzeyinde bırakıldı.
- 2. Dünya Savaşı kalite/üretim hızı örneği: kaynak izi zayıf, ama notebook düşünce hattını korumak için kısa metin olarak tutuldu; askeri görseller public yazıya eklenmedi.
- Hidrojen teşvikleri ve AB/NREL haber ekran görüntüleri: haber/ekran görüntüsü olarak kullanıldı; politika iddiasının tek dayanağı yapılmadı.
- H2Stations grafiğindeki 2021 ve 685 istasyon bilgisi: altyapı ihtiyacını göstermek için kullanıldı, kesin pazar verisi gibi sunulmadı.
- T3000 bölümündeki `%42` insan hatası oranı: notebook sadakati için geri getirildi, ama doğrulanmış dış veri gibi kullanılmadı.
- Afşin Termik Santrali kazası anlatısı: `[SANSÜR]` aktarımı olarak bırakıldı; kaza raporu gibi sunulmadı.
- İnsan/çeki hayvanı kalori hesabı: kesin biyoloji/veterinerlik sonucu değil, düşünce deneyi girdisi olarak kaldı.

## Yerleşim Güveni Düşük Olan Görseller

- `assets/figures/tarih-olcek/03-siemens-sirket-yapisi.jpg`: başlık eşleşmesi düşük; dosyanın girişine harita işleviyle yerleştirildi.
- `assets/figures/tarih-olcek/07-finansal-olcek-denklemi.JPG`: notebook'taki finansal ölçek bölümüne ait; public metinde argüman görseli olarak dikkatli kullanılmalı.
- `assets/figures/hidrojen/02-ab-yesil-anlasma-hidrojen.JPG`: haber ekran görüntüsü olduğu için kaynakça notu güçlü tutulmalı.
- `assets/figures/hidrojen/08-hidrojen-istasyonlari.jpg`: sayısal grafik var; kaynak durumu kısmen net.
- `assets/figures/verimlilik/02-at-kalori-kaynagi.jpg`: kaba kalori hesabı girdisi; kesin veri gibi okunmamalı.

## Bilerek Taşınmayan Görseller

- İdari kapak/form/üniversite görselleri.
- Şirket logo/sıralama ekranları içinde argümana zayıf katkı yapan tekrarlar.
- 2. Dünya Savaşı askeri görselleri: metindeki kalite sapması korundu, ama görsel olarak ana repo akışını gereksiz sertleştireceği için kullanılmadı.
- Nükleer mikroreaktör kamyon/araç görselleri: hidrojen araç bölümündeki yan düşünce metin olarak korundu, ama ana enerji depolama argümanını dağıtmamak için görsel eklenmedi.
## Missing Text Assertion Register

Bu tablo `mismatch_matrix.csv` içindeki `missing_text` kayıtlarının son durumunu gösterir.
Public metne taşınmayan kayıtlar ya idari/filler kabul edildi ya da manuel karar olarak bırakıldı.

| source_anchor | hedef | durum | gerekçe |
|---|---|---|---|
| `notebook_block_0012` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0032` | `README.md` | ignored_admin_or_filler | İdari şablon, form, imza/kaşe veya açık filler olduğu için public metne taşınmadı. |
| `notebook_block_0038` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0044` | `README.md` | ignored_admin_or_filler | İdari şablon, form, imza/kaşe veya açık filler olduğu için public metne taşınmadı. |
| `notebook_block_0050` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.57. |
| `notebook_block_0051` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.65. |
| `notebook_block_0052` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0053` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0054` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.86. |
| `notebook_block_0055` | `docs/tarih-olcek-ve-bakim.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0057` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.63. |
| `notebook_block_0060` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.91. |
| `notebook_block_0061` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.80. |
| `notebook_block_0071` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0081` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0082` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.81. |
| `notebook_block_0083` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.62. |
| `notebook_block_0084` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.60. |
| `notebook_block_0086` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0087` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0094` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0098` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.62. |
| `notebook_block_0099` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.78. |
| `notebook_block_0100` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.90. |
| `notebook_block_0101` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0102` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.57. |
| `notebook_block_0108` | `docs/tarih-olcek-ve-bakim.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0113` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.72. |
| `notebook_block_0114` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.57. |
| `notebook_block_0122` | `docs/tarih-olcek-ve-bakim.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0126` | `docs/tarih-olcek-ve-bakim.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0127` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.55. |
| `notebook_block_0138` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.71. |
| `notebook_block_0139` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.92. |
| `notebook_block_0140` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.86. |
| `notebook_block_0142` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.81. |
| `notebook_block_0152` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0156` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.60. |
| `notebook_block_0157` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0159` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0162` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.81. |
| `notebook_block_0163` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0174` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0175` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.57. |
| `notebook_block_0176` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.60. |
| `notebook_block_0177` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.81. |
| `notebook_block_0187` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0188` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0195` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.83. |
| `notebook_block_0199` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0204` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0205` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0206` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0207` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.64. |
| `notebook_block_0214` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0218` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.67. |
| `notebook_block_0219` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.60. |
| `notebook_block_0220` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.60. |
| `notebook_block_0221` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0223` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.56. |
| `notebook_block_0233` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0234` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.60. |
| `notebook_block_0236` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.67. |
| `notebook_block_0237` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0238` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.67. |
| `notebook_block_0249` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.72. |
| `notebook_block_0250` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0251` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0252` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0253` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0254` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0255` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0256` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0257` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0258` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0269` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.68. |
| `notebook_block_0270` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0271` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0272` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0273` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0279` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.62. |
| `notebook_block_0283` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.57. |
| `notebook_block_0284` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0285` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0286` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.68. |
| `notebook_block_0287` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.56. |
| `notebook_block_0288` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.70. |
| `notebook_block_0295` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.80. |
| `notebook_block_0300` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0302` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0303` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0305` | `docs/hidrojen-ve-enerji-depolama.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.78. |
| `notebook_block_0306` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0307` | `docs/hidrojen-ve-enerji-depolama.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0315` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0319` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0320` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0321` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0322` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0323` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.57. |
| `notebook_block_0324` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0326` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0338` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0339` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0340` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0341` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.71. |
| `notebook_block_0342` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.80. |
| `notebook_block_0343` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0346` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.83. |
| `notebook_block_0349` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.71. |
| `notebook_block_0350` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0352` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0353` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0364` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0378` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.60. |
| `notebook_block_0379` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.80. |
| `notebook_block_0380` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.57. |
| `notebook_block_0382` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.89. |
| `notebook_block_0383` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0385` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0387` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0388` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0389` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.80. |
| `notebook_block_0390` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.72. |
| `notebook_block_0401` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0402` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.71. |
| `notebook_block_0403` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.64. |
| `notebook_block_0404` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0406` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.77. |
| `notebook_block_0408` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.67. |
| `notebook_block_0414` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0419` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0420` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0421` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0422` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0423` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0424` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0425` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.67. |
| `notebook_block_0432` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0436` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0437` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0438` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.73. |
| `notebook_block_0439` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.56. |
| `notebook_block_0440` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.86. |
| `notebook_block_0441` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0442` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0443` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0444` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0445` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0446` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.70. |
| `notebook_block_0447` | `docs/tarih-olcek-ve-bakim.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.56. |
| `notebook_block_0448` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 1.00. |
| `notebook_block_0449` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.59. |
| `notebook_block_0460` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0461` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.59. |
| `notebook_block_0462` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.77. |
| `notebook_block_0464` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0465` | `README.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0466` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.75. |
| `notebook_block_0467` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0469` | `README.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.71. |
| `notebook_block_0470` | `docs/verimlilik-hipotez-ve-insan-makine.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
| `notebook_block_0472` | `docs/verimlilik-hipotez-ve-insan-makine.md` | resolved_or_transformed | Public metinde dönüştürülerek karşılandı; kelime kapsama skoru 0.80. |
| `notebook_block_0473` | `docs/tarih-olcek-ve-bakim.md` | manual_check | Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı. |
