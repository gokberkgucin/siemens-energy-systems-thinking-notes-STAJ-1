# Render Audit

Bu denetimin amacı GitHub markdown render kalitesini kontrol etmekti: görsel yolları, alt metinler, linkler, başlık hiyerarşisi ve uzun paragraf blokları.

## Kapsam

- `README.md`
- `docs/tarih-olcek-ve-bakim.md`
- `docs/hidrojen-ve-enerji-depolama.md`
- `docs/verimlilik-hipotez-ve-insan-makine.md`
- `docs/kaynakca-ve-sekil-notlari.md`

## Sonuçlar

| Kontrol | Sonuç |
|---|---:|
| Public markdown dosyası | 5 |
| Görsel referansı | 22 |
| Normal markdown linki | 32 |
| Kırık görsel/link | 0 |
| Boş alt metin | 0 |
| Yanlış görsel path prefix'i | 0 |
| Başlık hiyerarşisi sorunu | 0 |
| Çok uzun tek-paragraf bloğu | 0 |
| Gereksiz HTML kullanımı | 0 |

## Path Normalizasyonu

- `README.md` içinde görsel kullanılmıyor; bu yüzden `./assets/...` düzeltmesi gerektiren bir referans yok.
- `docs/*.md` içindeki tüm görsel yolları `../assets/...` ile başlıyor.
- Görseller `assets/figures/tarih-olcek/`, `assets/figures/hidrojen/`, `assets/figures/verimlilik/` altında duruyor.

## Alt Metin Revizyonu

Bazı görsel alt metinleri yalnızca nesneyi adlandırıyordu. Bunlar, görselin argümana nasıl hizmet ettiğini anlatacak şekilde kısaltılarak düzeltildi.

- `docs/tarih-olcek-ve-bakim.md`: Silahtarağa, santral yaşı, GPS/ölçek, dinozor/insan ölçeği ve gaz türbini bakım görselleri.
- `docs/hidrojen-ve-enerji-depolama.md`: hidrojen üretim yolları, NREL çizelgeleri, hidrojen verimlilik zinciri, enerji kaybı karşılaştırması ve depolama grafiği.
- `docs/verimlilik-hipotez-ve-insan-makine.md`: T3000 kontrol odası ve Lorentz/yük devresi görselleri.

## Not

Görsel dosyaları yeniden sıkıştırılmadı, crop edilmedi, OCR ile yeniden çizilmedi. Değişiklik markdown seviyesinde kaldı.

