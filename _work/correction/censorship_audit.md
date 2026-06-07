# Censorship Audit

Bu denetimin amacı kişi adlarını public metinden ve `_work/correction` altındaki correction raporlarından temizlemekti. Kurum, yer, ürün ve teknik terimler sansürlenmedi.

## Uygulanan Sansür

- `docs/kaynakca-ve-sekil-notlari.md` içinde kaynakça satırlarında kalan açık kişi adları `[SANSÜR]` biçimine çekildi.
- `_work/correction/extract/notebook_full_text.md` içindeki defterden gelen açık kişi adları `[SANSÜR]` ile değiştirildi.
- `_work/correction/inventory/image_manifest.csv`, `mismatch_matrix.csv`, `repo_markdown_inventory.csv` ve `unused_notebook_images.csv` içindeki aynı kişi adı izleri sansürlendi.
- Eski GitHub API snapshot dosyaları (`github_repo.json`, `github_root_contents.json`, `github_docs_contents.json`, `github_api_status.log`) `_work/correction/inventory` altından kaldırıldı. Bu dosyalar correction için gerekli değildi ve kişisel GitHub slug bilgisini URL/account alanlarında taşıyordu.

## Regex / Denylist Sonucu

- Verilen denylist doğrudan uygulandı.
- `Bey`, `Hoca`, `Hanım`, `Abi`, `Ağabey` gibi unvanlı kişi adı adayları tarandı.
- Verilen ilk-ad ipuçlarına uyan ad-soyad adayları tarandı.
- Son kontrolde denylist ve honorific regex için açık kişi adı eşleşmesi kalmadı.

## Yanlış Pozitif Düzeltmeleri

Otomatik tarama iki başlığı yanlış kişi adı gibi sansürledi. Bunlar geri alındı:

- `Hidrojen Nerelerde Kullanılıyor?`
- `Finalde Kullanılan Görseller`

`repo_markdown_inventory.csv` içindeki eski snapshot satırlarında da aynı başlık izleri düzeltildi.

## Görsel İçi Gizlilik

Finalde kullanılan 22 görsel `tesseract` ile `tur+eng` OCR taramasından geçirildi.

- Açık kişi adı eşleşmesi bulunmadı.
- Bu yüzden `-sansurlu` kopya üretilmedi.
- Orijinal görsel binary dosyalarına dokunulmadı.

## Şüpheli Adaylar

Çözülemeyen şüpheli kişi adı adayı kalmadı.

