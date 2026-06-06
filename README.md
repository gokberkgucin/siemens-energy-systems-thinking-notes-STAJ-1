# Siemens Energy Stajından Sistem Düşüncesi Notları

Bu repo, bir staj defterinin kronolojik kopyası değil.

Staj sırasında duyduğum, okuduğum ve gördüğüm bazı şeyleri sonradan tekrar ele alma denemesi. Ölçek, bakım, verimlilik, depolama ve insan-makine işbirliği gibi başlıklar var; ama buradaki dert "stajda şunları yaptım" diye günlük tutmak değil. Daha çok, bir endüstriyel sisteme bakarken aklıma hangi sorular geldi, neyi neye benzettim, nerede itiraz ettim, nerede de ilk hipotezim beklediğim kadar güçlü çıkmadığı için geri adım attım, bunu ayıklamak.

Bu resmi bir Siemens Energy dokümanı değildir. Kişisel gözlem, okuma ve yeniden düşünme dosyasıdır.

## Bu Repo Neden Var?

İlk staj defterimde bazı bölümler sadece bilgi notu gibi kalıyordu. Şirket bölümleri, tarihsel bilgiler, teknik tanımlar, kaynak parçaları... Bunların hepsi tek tek gerekli görünebilir; ama hepsi repo'ya taşınırsa bu defterin daha ilginç tarafı kaybolur.

Bence o taraf, bir bilgiyi duyunca onun arkasındaki ilişkiyi aramamdaydı.

Örneğin bir gaz türbininin bakımında yüzlerce kişinin haftalarca çalıştığını duyunca, bunu sadece bakım bilgisi olarak değil, ürün başarımı ve işletme ekonomisi açısından düşünmek gerekiyor. Ya da hidrojenin verimliliği düşük denildiğinde, "tamam, o zaman kötü" demek yerine, önce sistem sınırını sormak gerekiyor: Neye göre düşük? Hangi alternatifle kıyaslıyoruz? Uzun süreli depolama ihtiyacını hesaba katıyor muyuz?

Bu repo biraz o soruları temizleyip yan yana koymak için var.

## Benim İçin Ne Var?

Burada "her şeyi biliyorum" iddiası yok. Hatta bazı yerlerde özellikle yok.

Bunları okurken öne çıkan şeyler şunlar:

- Soyut büyüklükleri çıplak rakam olarak bırakmayıp bir ölçek arama.
- Teknik bir bilginin işletmede neye mal olduğunu da sorma.
- Hidrojen gibi bir konuya "iyi/kötü" diye değil, kayıp, depolama ve kullanım yeriyle birlikte bakma.
- Kendi hipotezimi kurup, sonuç zayıf çıkarsa onu zorlamama.
- Otomasyon ile insan rolünü birbirinin yerine koymadan düşünmeye çalışma.

Bazı hesaplar veya yorumlar yöntemsel olarak eksik olabilir. Bu repo'nun iddiası "her şeyi doğru hesapladım" değil. Daha çok, düşünürken nereden geçtiğimi saklamamak.

## Neden Klasik Staj Günlüğü Değil?

Çünkü klasik staj günlüğü çoğu zaman sırayla ilerler: bugün şu anlatıldı, sonra bu görüldü, sonra şu not alındı.

Benim burada yapmak istediğim şey o değil. Ham kronoloji yerine, birbirine bağlanan üç ana eksen seçtim. Bazı kısımlar bilerek dışarıda kaldı: staj defteri formları, şirket tanıtımı gibi duran bölümler, ana fikri dağıtan örnekler, yalnızca dekor gibi kalan görseller.

Bu yüzden repo daha az dosyadan oluşuyor. Az olsun, ama her dosyanın bir derdi olsun istedim.

## İçerik Haritası

1. [Tarih, Ölçek, Bakım ve Operasyon Mantığı](docs/tarih-olcek-ve-bakim.md)

   Siemens'in Türkiye'deki tarihsel izlerinden başlayıp santral yaşı, ölçek anlatımı ve gaz türbini bakımının işletme tarafına gidiyor.

2. [Hidrojen, Enerji Dönüşümü ve Depolama](docs/hidrojen-ve-enerji-depolama.md)

   Hidrojeni sadece temiz yakıt etiketiyle değil; üretim yolu, dönüşüm kayıpları, sistem sınırı ve depolama ihtiyacıyla birlikte okuyor.

3. [Verimlilik, Hipotez Kurma ve İnsan-Makine İlişkisi](docs/verimlilik-hipotez-ve-insan-makine.md)

   Etkililik, etkinlik ve verimlilik kavramlarından insan/çeki hayvanı düşünce deneyine; oradan T3000 kontrol sistemi, operatör rolü ve jeneratör-yük ilişkisine geçiyor.

Kaynak ve görsel notları için: [Kaynakça ve Şekil Notları](docs/kaynakca-ve-sekil-notlari.md)

## Okurken Ne Beklemeli?

Bu repo'da büyük ve cilalı sonuç cümleleri beklememek daha doğru olur. Bazı yerlerde soru var, bazı yerlerde itiraz var, bazı yerlerde de "burada çok emin değilim" tavrı var.

Bilinmeyen bir şeyi bilinen bir şeyle kıyaslamaya çalışıyorum. Bazen bir grafikten, bazen bir bakım süresinden, bazen basit bir devre çiziminden, bazen de bir kalori hesabından yola çıkıyorum.

Benim için buradaki mesele biraz şu: Enerji sistemleri sadece türbin, jeneratör, hidrojen veya kontrol yazılımı diye tek tek parçalar halinde durmuyor. Bakım süresi, insan kararı, depolama ihtiyacı, kayıplar, ölçek ve bazen de yanlış kurulmuş ilk hipotezler işin içine girince daha gerçek hale geliyor.

Ben de eldeki staj notlarını bu ilişkileri daha iyi görebilmek için yeniden dizdim.
