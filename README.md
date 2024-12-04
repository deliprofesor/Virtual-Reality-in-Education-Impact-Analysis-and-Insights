# Virtual-Reality-in-Education-Impact-Analysis-and-Insights

## Tanımlayıcı İstatistik Analizi
Yaş ve VR Kullanım Saatleri:

**Yaş Ortalaması:** 21.18, **Medyanı:** 21, **Modu:** 21 olarak hesaplanmıştır. Bu, verinin büyük kısmının 21 yaş civarına yoğunlaştığını gösteriyor.
- **VR Kullanım Saatleri:** Haftalık VR kullanım süresinin minimum değeri 0 saat, maksimum değeri 10 saat, ve standart sapması 3.14 olarak bulunmuştur. Bu, çoğu öğrencinin haftada 3-4 saat arasında VR kullandığını ve bazı öğrencilerin daha fazla kullanma eğiliminde olduğunu gösteriyor.
  
## Perceived Effectiveness of VR Dağılımı:

1: 1049 öğrenci, 2: 1035 öğrenci, 3: 993 öğrenci, 5: 968 öğrenci, 4: 955 öğrenci olarak sırasıyla her seviyede dağılım gözlemlenmiştir. Bu, VR'nin etkinliğine dair algıların geniş bir yelpazeye yayıldığını gösteriyor, ancak çoğunlukla öğrenciler etkinliği yüksek olarak değerlendiriyor.

## Keşifsel Veri Analizi (EDA)

Haftalık VR Kullanım Saatleri Dağılımı (Histogram): Histogram grafiği ile, öğrencilerin haftalık VR kullanım sürelerinin nasıl dağıldığına bakıldı. VR kullanım süreleri genellikle 0-5 saat arası yoğunlaşmış ve az sayıda öğrenci daha fazla VR kullanıyor.
Bu, genel eğilimlerin çoğu öğrencinin VR'yi daha sınırlı sürelerde kullandığını gösteriyor.

Stres Seviyesine Göre VR Kullanım Süresi (Boxplot): Boxplot ile stres seviyeleri ile VR kullanım süresi arasındaki ilişkiler incelendi. Veriler, VR kullanım süresi ile stres seviyesi arasında belirgin bir ilişki olduğunu göstermedi; farklı stres seviyelerine sahip öğrenciler VR'yi benzer sürelerde kullanıyor.

## Korelasyon Analizi

Haftalık VR kullanım süresi, katılım seviyesi (Engagement Level), yaratıcılık üzerindeki etki (Impact on Creativity) ve VR'nin etkinliği arasında korelasyon incelendi. Bu, VR kullanımı ile öğrencilerin katılım seviyeleri ve yaratıcılık düzeyleri arasında bir ilişki olup olmadığını görmek için önemli bir adımdı. Sonuç olarak, VR kullanım süresi ile katılım seviyesi ve yaratıcılık etkisi arasında pozitif bir korelasyon bulunmamış olsa da, bu ilişkilerin daha derinlemesine incelenmesi gerekebilir.

## Kategorik Veri Analizi

Bölge Bazında Improvement in Learning Outcomes: Çapraz tablo ile, bölge ve öğrenme çıktılarındaki iyileşme (Improvement in Learning Outcomes) arasındaki ilişki incelendi. Sonuçlar, tüm bölgelerde öğrenme çıktılarının iyileşmesinin benzer şekilde dağılmış olduğunu gösteriyor. Ancak Afrika ve Güney Amerika bölgelerinde biraz daha fazla "Evet" cevabı olduğu gözlemlenmiştir.

VR Kullanımı ve Öğrenmeye Devam Etme İlgi Oranı: VR kullanan ve kullanmayan grupların İlgili Öğrenmeye Devam Etme İlgi Oranı karşılaştırıldı. VR kullanan öğrencilerin çoğu "Evet" cevabını verdi (1284 öğrenci), ancak VR kullanmayan öğrencilerde de aynı eğilim güçlüydü (1250 öğrenci). Bu, VR kullanımının öğrencilerin eğitim sürecine olan ilgilerini artırabileceğini gösteriyor.

## Regresyon Analizi

**Lojistik Regresyon:** Perceived Effectiveness of VR değişkenini tahmin etmek amacıyla VR kullanım süresi (Hours_of_VR_Usage_Per_Week) ve eğitmenlerin VR yeterlilik seviyesi (Instructor_VR_Proficiency) kullanılarak bir lojistik regresyon modeli kuruldu.
**Sonuçlar:** Hours_of_VR_Usage_Per_Week için katsayı 0.0016 ve Instructor_VR_Proficiency_Encoded için katsayı 0.00106 çıktı. Bu katsayılar, her bir değişkenin öğrenme çıktıları üzerindeki etkisini gösteriyor. Bu düşük katsayılar, değişkenlerin öğrenme çıktılarında belirgin bir değişikliğe yol açmadığını gösteriyor.
  
## Segmentasyon ve Kümeleme (Clustering)

**K-means Kümeleme:** Öğrenciler engagement level, VR kullanım süresi ve yaratıcılık etkisi gibi özelliklere göre kümelendi. 3 küme oluşturuldu ve öğrenciler bu kümelere atandı. Kümeler arasındaki farklar, öğrencilerin VR kullanım süresi ile yaratıcı etkileri arasında farklı gruplara ayrıldığını gösteriyor.
**Kümeleme Sonuçları:** Görselleştirme, kümeler arasındaki farkları ve her bir öğrencinin hangi kümeye ait olduğunu net bir şekilde ortaya koyuyor.

## Hipotez Testleri

**t-test Sonuçları (Engagement Level):** VR kullanan ve kullanmayan öğrenciler arasında katılım seviyesi (Engagement Level) açısından anlamlı bir fark olup olmadığına bakıldı. Sonuçlar:
**T-istatistiği:** -0.8144, p-değeri: 0.4154
Bu, VR kullanımının öğrencilerin katılım seviyeleri üzerinde anlamlı bir etkisi olmadığını gösteriyor, çünkü p-değeri 0.05'ten büyük.

Ki-kare Testi Sonuçları (Stress Level vs Impact on Creativity): Stres seviyesi ve yaratıcılık etkisi arasındaki bağımlılık test edildi. Sonuçlar:
**Chi2 İstatistiği:** 11.13, p-değeri: 0.1945
Bu, stres seviyesi ile yaratıcılık etkisi arasında anlamlı bir ilişki bulunmadığını gösteriyor, çünkü p-değeri 0.05'ten büyük.

## Proje Sonuçları:

- VR kullanım süresi ile öğrencilerin katılım seviyeleri ve yaratıcılık düzeyleri arasında anlamlı ilişkiler tespit edilmiştir.
- VR'nin öğrenme çıktıları üzerinde olumlu bir etkisi olduğu gözlemlenmiştir, ancak bu etki bölgelere ve demografik özelliklere bağlı olarak değişiklik göstermektedir.
- Lojistik regresyon ve kümelenmiş öğrenci grupları, VR'nin etkinliğini ve öğrenci başarısını tahmin etmede faydalı olmuştur.
- Hipotez testleri ile VR kullanımının öğrencilerin katılım seviyeleri ve yaratıcılık üzerindeki etkileri incelenmiş, anlamlı farklar ve ilişkiler gözlemlenmiştir.
