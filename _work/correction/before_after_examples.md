# Before / After Examples

Başlangıç commit'i: `f1f245e9cd11378a80a00200cc2b95505431f4c6`

Örnekler gerçek `git diff` çıktılarından üretildi. Kişi adı riski taşıyan görünen metinler bu raporda da `[SANSÜR]` olarak bırakıldı.

## README.md

README'in staj defteri özeti değil, kişisel gözlem/yeniden kurulum çerçevesine çekilmesi.

### Önce

```markdown
[base commit'te bu blok yoktu]
```

### Sonra

```markdown
Kamuya açık hale getirirken kişi adlarını `[SANSÜR]` biçiminde bıraktım. Buradaki amaç kişisel öğrenme izini korumak; konuşmalara dahil olmuş kişileri açık kaynak repo içinde görünür yapmak değil.

```

## docs/tarih-olcek-ve-bakim.md

Tarih, ölçek, finansal karşılaştırma ve bakım mantığının notebook'tan geri yüklenmesi.

### Önce

```markdown
![Silahtarağa Santrali](../assets/figures/tarih-silahtaraga-santrali.jpeg)
![Santral yaşı ve verim ilişkisi](../assets/figures/tarih-santral-yasi-kullanilabilirlik.jpg)
![GPS cihazı ve bozuk para ile ölçek kurma](../assets/figures/olcek-gps-bozuk-para.jpeg)
![Dinozor ve insan ölçeği](../assets/figures/olcek-dinozor-insan.jpg)
```

### Sonra

```markdown
![Silahtarağa Santrali'nin teknoloji ömrü ve endüstriyel miras sorusunu açan görseli](../assets/figures/tarih-olcek/01-silahtaraga-santrali.jpeg)
![Santral yaşının verim ve işletme kararıyla ilişkisini düşündüren grafik](../assets/figures/tarih-olcek/02-santral-yasi-verim.jpg)
![Silahtarağa Santrali'nin tarihsel görünümünü ölçek ve altyapı hissiyle gösteren görsel](../assets/figures/tarih-olcek/04-silahtaraga-tarihsel-gorunum.jpeg)

*Şekil — Notebook'ta Silahtarağa'nın eski görünümü, santrali yalnızca bugün müze olarak değil, bir dönem İstanbul'un enerji altyapısı olarak düşünmemi sağlıyordu.*

![Şeker fabrikası ve buhar türbini anlatısını tarihsel üretim altyapısına bağlayan görsel](../assets/figures/tarih-olcek/08-seker-fabrikasi-buhar-turbini.jpg)

*Şekil — Notebook'taki bu küçük görsel, anlatının raporlanmış teknik kanıt değil; eski üretim altyapısı, bakım kültürü ve tanıklık karışımı bir iz olduğunu hatırlatıyor.*

Defterde burada biraz yan yola sapıp Alman kalite anlayışıyla ilgili, sevimli olmayan bir 2. Dünya Savaşı örneği de yazmıştım. Savaş sanayisindeki bazı ürünlerin, kullanım ömrü çok kısa olacakken gereğinden fazla dayanıklı tasarlanmaya çalışıldığı; bunun da üretim hızını ve kapasitesini olumsuz etkileyebildiği türünden bir nottu. Bu pasajı bugün aynen büyütmek istemem; hem kaynak izi zayıf hem de enerji sistemleri yazısının ana hattını dağıtabilir. Ama tamamen atınca da defterdeki düşünce kayboluyor.

Buradan bana kalan soru şuydu: Kalite her zaman "daha dayanıklı yap" demek mi? Yoksa kullanılacağı bağlam, üretim hızı, bakım imkanı ve gerçek ihtiyaç da kalite tanımının parçası mı? Eskişehir/Turhal örneğinde uzun ömür olumlu bir şey gibi duruyor. Ama başka bir bağlamda aşırı kalite, sistemin ihtiyacıyla uyumsuz bile olabilir. Bu yüzden kaliteyi tek başına ahlaki bir övgü gibi değil, bağlama bağlı bir mühendislik tercihi gibi düşünmek daha doğru geliyor.

Defterde Ambarlı Termik Santrali için `%51`, Samsun Doğalgaz Çevrim Enerji Santrali için de `%61` etkinlik/verimlilik rekoru diye notlar vardı. Bu sayıları burada dışarıdan doğrulanmış kesin iddia gibi büyütmüyorum. Ama Silahtarağa'dan modern çevrim santrallerine geçerken, "eski santral" sorusunun karşısına modern santraldeki başarım ölçütlerinin çıktığını göstermesi açısından önemli. Bir tarafta yaşlanan altyapı, diğer tarafta verim rekoru diye anılan yeni tasarımlar var.

![Soyut büyüklüğü bilinen bir nesneyle kurmayı gösteren GPS ve bozuk para görseli](../assets/figures/tarih-olcek/05-gps-bozuk-para.jpeg)
![Sayısal ölçeğin insan siluetiyle nasıl sezilir hale geldiğini gösteren dinozor karşılaştırması](../assets/figures/tarih-olcek/06-dinozor-insan-olcek.jpg)
```

## docs/hidrojen-ve-enerji-depolama.md

Hidrojen anlatısının üretim, altyapı, verimlilik itirazı ve depolama ekseninde genişletilmesi.

### Önce

```markdown
![Hidrojen üretim yolları](../assets/figures/hidrojen-uretim-yollari.jpeg)
Kahverengi ve gri hidrojen için defterde kurduğum benzetme hala işe yarıyor gibi geliyor: Çevrecilik açısından bu durum, dizel jeneratörle şarj edilen elektrikli arabaya benziyor sanki. Son kullanıcı tarafında elektrikli araba temiz görünebilir; ama elektriği nasıl ürettiğimiz sorusunu dışarıda bırakırsak resmi eksik okuruz.
```

### Sonra

```markdown
![Temiz hidrojen iddiasının üretim yoluna bağlı olduğunu gösteren üretim şeması](../assets/figures/hidrojen/01-hidrojen-uretim-yollari.jpeg)
Kahverengi ve gri hidrojen için defterde kurduğum benzetme hala işe yarıyor gibi geliyor: Çevrecilik açısından bu durum, dizel jeneratörle şarj edilen elektrikli arabaya benziyor sanki. Bu benzetmeyi stajdaki bir anlatımdan esinlenerek kurmuştum. Son kullanıcı tarafında elektrikli araba temiz görünebilir; ama elektriği nasıl ürettiğimiz sorusunu dışarıda bırakırsak resmi eksik okuruz.
```

## docs/verimlilik-hipotez-ve-insan-makine.md

Hipotez kurma, T3000 ve Lorentz/model güncelleme akışının güçlendirilmesi.

### Önce

```markdown
Staj notlarımda T3000, güç santrali kontrol sistemi olarak geçiyordu. Modern bir santralde kontrol sistemi çok fazla şeyi izliyor, düzenliyor ve operatörün önüne anlamlı hale getiriyor. Bu tür sistemlerde insan müdahalesi eskiye göre azalmış olabilir. Hatta notlarımda, planlanmamış yavaşlama veya kesintilerde insan hatasının kayda değer bir payı olabildiğine dair bir oran da vardı. Bu oranı bu turda güç santrali özelinde yeterince netleştiremediğim için burada kesin sayı gibi kullanmıyorum.
![T3000 kontrol odası](../assets/figures/t3000-kontrol-odasi.jpeg)
```

### Sonra

```markdown
Staj notlarımda T3000, güç santrali kontrol sistemi olarak geçiyordu. Modern bir santralde kontrol sistemi çok fazla şeyi izliyor, düzenliyor ve operatörün önüne anlamlı hale getiriyor. Bu tür sistemlerde insan müdahalesi eskiye göre azalmış olabilir. Hatta notlarımda, planlanmamış yavaşlama veya kesintilerin `%42` gibi kayda değer bir kısmının insan hatası kaynaklı olduğuna dair bir oran vardı. Bu oranı bu turda güç santrali özelinde yeterince netleştiremediğim için burada kesin sayı gibi kullanmıyorum; ama o gün bende şu soruyu başlattığı için notebook izini siliyor da değilim.
![Operatör rolünün soyut değil gerçek bir kontrol ortamında düşünülmesini sağlayan T3000 görseli](../assets/figures/verimlilik/03-t3000-kontrol-odasi.jpeg)
```

## docs/kaynakca-ve-sekil-notlari.md

Şekil kaynak notlarının gerçek public görsel kullanımıyla eşleştirilmesi.

### Önce

```markdown
| 33 | "[SANSÜR], başlıpınnbu bilmi. çorum, 1992..." | Kaynakça içinde kalmış ama anlamlı kaynak değil. Final yazılarda kullanılmadı. |
| 34 | [SANSÜR], "avusturyalıler", 1999. | Kayıt eksik ve doğrulanmamış. Final yazılarda kullanılmadı. |
| - | [SANSÜR], kişisel görüşme, Eylül 2022. | Eskişehir/Turhal buhar türbinleri bağlamında defterde geçti. Yazıda tanıklık gibi ele alındı; teknik kanıt gibi kullanılmadı. |
| - | [SANSÜR]'in aktardığı bilgi. | Footnote içinde geçti. Notebook içinde geçti, doğrulama gerekebilir. |
| - | [SANSÜR] ile soru-cevap. | T3000, jeneratör dönüş hızı, Lorentz ve yük değişimleri bağlamında defterde geçti. Kişisel öğrenme anı olarak kullanıldı; kaynak iddiası gibi sunulmadı. |
| - | Afşin Termik Santrali kazası anlatısı. | [SANSÜR]'in aktarımı olarak defterde geçti. Notebook içinde geçti, doğrulama gerekebilir. Final yazıda kaza ayrıntısı kanıt gibi büyütülmedi. |
| Görsel adı | Kullanıldığı dosya | Kısa açıklama | Kaynak notu |
|---|---|---|---|
| `tarih-silahtaraga-santrali.jpeg` | `docs/tarih-olcek-ve-bakim.md` | Silahtarağa Santrali'ni tarihsel iz ve teknolojik ömür sorusuna bağlamak için kullanıldı. | Ham görsel: `ek09_img_07_silahtaraga_santrali_dis_gorunum.jpeg`. Kaynakça [1] ile ilişkili kabul edildi; özgün görsel kaynağı kısmen net. |
| `tarih-santral-yasi-kullanilabilirlik.jpg` | `docs/tarih-olcek-ve-bakim.md` | Santral yaşı ile verim ilişkisini düşünmek için kullanıldı. | Ham görsel: `ek09_img_05_santral_yasi_kullanilabilirlik_grafigi.jpg`. Kaynakça [2] ile ilişkili; rapor adı doğrulandı, yıl bilgisi net olmadığı için metinde tarih yazılmadı. |
| `olcek-gps-bozuk-para.jpeg` | `docs/tarih-olcek-ve-bakim.md` | Soyut büyüklüğü bilinen nesneyle kıyaslama fikrini gösteriyor. | Ham görsel: `ek09_img_21_gps_cihazi_bozuk_para_olcek.jpeg`. Notebook içinde geçti; özgün kaynak doğrulama gerektirebilir. Kanıt değil, anlatım yöntemi görseli. |
| `olcek-dinozor-insan.jpg` | `docs/tarih-olcek-ve-bakim.md` | Ölçek hissini insan siluetiyle kurma fikrini taşıyor. | Ham görsel: `ek09_img_22_dinozor_insan_olcek_karsilastirma.jpg`. Kaynakça [3] ile ilişkili kabul edildi; doğrulama gerekebilir. |
| `operasyon-gaz-turbini-bakim.jpeg` | `docs/tarih-olcek-ve-bakim.md` | Gaz türbini bakımının fiziksel ve operasyonel ölçeğini sezdiriyor. | Ham görsel: `ek09_img_12_gaz_turbini_montaj_sahasi.jpeg`. Notebook içinde geçti; özgün kaynak kısmen net. Bakım süresi bilgisinin kanıtı değil. |
| `hidrojen-uretim-yollari.jpeg` | `docs/hidrojen-ve-enerji-depolama.md` | Kahverengi/gri/mavi/yeşil hidrojen üretim yollarını hızlıca ayırmak için kullanıldı. | Ham görsel: `ek09_img_29_hidrojen_renkleri_uretim_yollari.jpeg`. Kaynak durumu kısmen net; doğrulama gerekebilir. |
```

### Sonra

```markdown
| 33 | "[SANSÜR], başlıpınnbu bilmi. çorum, 1992..." | Kaynakça içinde kalmış ama anlamlı kaynak değil. Final yazılarda kullanılmadı. |
| 34 | [SANSÜR], "avusturyalıler", 1999. | Kayıt eksik ve doğrulanmamış. Final yazılarda kullanılmadı. |
| - | `[SANSÜR]`, kişisel görüşme, Eylül 2022. | Eskişehir/Turhal buhar türbinleri bağlamında defterde geçti. Yazıda tanıklık gibi ele alındı; teknik kanıt gibi kullanılmadı. |
| - | `[SANSÜR]` tarafından aktarılan bilgi. | Footnote içinde geçti. Notebook içinde geçti, doğrulama gerekebilir. |
| - | `[SANSÜR]` ile soru-cevap. | T3000, jeneratör dönüş hızı, Lorentz ve yük değişimleri bağlamında defterde geçti. Kişisel öğrenme anı olarak kullanıldı; kaynak iddiası gibi sunulmadı. |
| - | Afşin Termik Santrali kazası anlatısı. | `[SANSÜR]` aktarımı olarak defterde geçti. Notebook içinde geçti, doğrulama gerekebilir. Final yazıda kaza ayrıntısı kanıt gibi büyütülmedi. |
Bu tabloda `source_image_id`, `_work/correction/inventory/image_manifest.csv` içindeki görsel kimliğine karşılık gelir. Görseller orijinal binary dosyalardan taşındı/kopyalandı; crop, OCR veya yeniden çizim yapılmadı.

| final_path | source_image_id | kullanıldığı_dosya | ilgili_bölüm | kaynak_notu |
|---|---|---|---|---|
| `assets/figures/tarih-olcek/01-silahtaraga-santrali.jpeg` | `nb_img_007` | `docs/tarih-olcek-ve-bakim.md` | Silahtarağa | Kaynakça [1] ile ilişkili kabul edildi; özgün görsel kaynağı kısmen net. |
| `assets/figures/tarih-olcek/02-santral-yasi-verim.jpg` | `nb_img_005` | `docs/tarih-olcek-ve-bakim.md` | Santral yaşı/verim | Kaynakça [2] ile ilişkili; rapor yılı net olmadığı için metinde tarih yazılmadı. |
| `assets/figures/tarih-olcek/03-siemens-sirket-yapisi.jpg` | `nb_img_003` | `docs/tarih-olcek-ve-bakim.md` | Şirket yapısı haritası | Şirket tanıtımı değil, notebook başlıklarının hangi iş kollarına bağlandığını göstermek için kullanıldı. |
| `assets/figures/tarih-olcek/04-silahtaraga-tarihsel-gorunum.jpeg` | `nb_img_008` | `docs/tarih-olcek-ve-bakim.md` | Tarihsel altyapı | Silahtarağa'nın tarihsel enerji altyapısı olarak okunmasına hizmet ediyor; kaynak durumu kısmen net. |
| `assets/figures/tarih-olcek/05-gps-bozuk-para.jpeg` | `nb_img_021` | `docs/tarih-olcek-ve-bakim.md` | Ölçek analojisi | Kanıt değil; bilinmeyen büyüklüğü bilinen nesneyle kıyaslama yöntemini gösteriyor. |
| `assets/figures/tarih-olcek/06-dinozor-insan-olcek.jpg` | `nb_img_022` | `docs/tarih-olcek-ve-bakim.md` | Ölçek analojisi | Kaynakça [3] ile ilişkili kabul edildi; doğrulama gerekebilir. |
| `assets/figures/tarih-olcek/07-finansal-olcek-denklemi.JPG` | `nb_img_024` | `docs/tarih-olcek-ve-bakim.md` | Finansal ölçek | Notebook'taki şirket/logolarla ciro eşitleme denemesi; sıralama kanıtı değil, ölçek kurma yöntemi. |
| `assets/figures/tarih-olcek/08-seker-fabrikasi-buhar-turbini.jpg` | `nb_img_014` | `docs/tarih-olcek-ve-bakim.md` | Eskişehir/Turhal | Kişisel tanıklık bağlamındaki tarihsel üretim altyapısı izi; teknik kanıt gibi kullanılmadı. |
```
