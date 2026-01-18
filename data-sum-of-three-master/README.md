Bu alıştırmaların nasıl işleyeceğini anlamak için çok basit bir örnekle başlayalım.

## Bir challenge nasıl çözülür?

Bazı alıştırmalarda bir `Makefile` bulunur.
Bu dosya, challenge’ının doğru olup olmadığını kontrol etmeni sağlar (Le Wagon hocaları tarafından önceden yazılmış testleri kullanan Test-Driven Development (TDD) yaklaşımıyla).
Bu script’i terminalde çalıştırmak için, doğru klasöre cd ile geç (yukarıda açıklandığı gibi ☝️) ve şu komutu çalıştır:

```bash
make
```

Amacın, `sum_of_three.py` dosyasında `sum3` function’ını implement etmektir. İzlemen gereken adımlar şunlardır:

1. Challenge talimatlarının tamamını oku
1. Kod yazacağın sum_of_three.py dosyasını aç ve önce onu oku
1. Run `make` (çalıştır)
1. İlk hata mesajını oku ve anlamaya çalış (gerekirse Google’a sor!)
1.sum_of_three.py dosyasındaki kodu değiştir
1.`make`komutunu tekrar çalıştır 
1. Yeni hata mesajı mı çıktı? Hata sayısı azaldı mı? İlerleme kaydediyorsun!
1. Hata kalmayana kadar tekrarla
1. Kod stilinin doğru olduğundan ve 10.00/10 stil skoruna ulaştığından emin ol
1. Değişikliklerini Workintech’e commit ve push et:
  1. `git status` Son commmit’ten beri hangi dosyaların değiştiğini görmek için
  1. `git diff` Ne değiştiğini görmek için
  1. `git add sum_of_three.py`
  1. `git commit -m "Solve first Python exercise of the day"`
  1. `git push origin master`

## `make` nasıl çalışır?

`make` , `Makefile` içinde tanımladığın komutları çalıştırabilir..

`Makefile` dosyasını text editoründe aç ve incele.

Sana yardımcı olmak için Python ekosisteminden iki önemli aracı kullanıyoruz:

-pytest
-pylint


Varsayılan olarak `make`, hem `pylint` hem de `pytest` çalıştırarak hem kod stilini hem de doğruluğunu kontrol eder.
Sadece stile veya sadece testlere odaklanmak istersen, şu komutlarla ayrı ayrı çalıştırabilirsin:


```bash
make pylint
make pytest
```

## Sonuç

Bu alıştırmanın amacı, testleri çalıştırarak kodunun (hem stil hem doğruluk açısından) otomatik olarak nasıl değerlendirileceğini göstermek ve seni bu hızlı geri bildirim döngüsüyle tanıştırmaktır.