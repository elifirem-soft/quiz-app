# quiz-app
Başlangıç seviye bir quiz uygulaması

Bu proje, Python'da Nesne Yönelimli Programlama (OOP) prensiplerini kullanarak geliştirdiğim dinamik bir bilgi yarışması uygulamasıdır. Kod mimarisini tamamen modüler ve geliştirilebilir bir yapıda kurguladım.

Neler Yaptım?

Sınıf Yapısı ve Modülerlik: Uygulamayı iki ana sınıf üzerine inşa ettim. Question sınıfı ile her bir sorunun metnini, seçeneklerini ve doğru cevabını kapsülledim. Quiz sınıfı ile de oyunun genel akışını, skor takibini ve soru sırasını yönettim.
Dinamik Soru Akışı: random modülünü kullanarak soruların her seferinde farklı bir sırayla gelmesini sağladım (random.sample). Bu sayede tekrar oynanabilirliği artırdım.
İlerleme ve Skor Takibi: Kullanıcının o an kaçıncı soruda olduğunu gösteren bir ilerleme çubuğu (displayProgress) ve test sonunda başarı oranına göre puan hesaplayan bir sistem (displayScore) geliştirdim.
Hata Yönetimi: Kullanıcının seçenekler dışında bir giriş yapması durumunda sistemi korumak adına checkAnswer metodu içerisinde özel hata kontrolleri (ValueError) uyguladım.

Teknik Özellikler

Dil: Python
Kullanılan Modüller: random (Soru karıştırma için)
OOP Konseptleri: Sınıf tanımlama (Class), Örnekleme (Instance), Metotlar ve Kapsülleme.

Nasıl Çalışır?

Uygulama çalıştırıldığında, öncelikle tanımlanmış olan soru havuzu random modülü yardımıyla karıştırılarak her kullanıcıya benzersiz bir deneyim sunulur. Oyun döngüsü boyunca her soru, şıklar ile birlikte sırayla ekrana getirilir ve kullanıcıdan bir cevap girişi beklenir. Girilen cevaplar Question sınıfındaki kontrol mekanizmasından geçerek doğruluğu anlık olarak sorgulanır ve doğru cevap durumunda skor güncellenerek bir sonraki soruya geçilir. Tüm sorular yanıtlandığında ise sistem otomatik olarak bir özet ekranı oluşturur; burada kullanıcının toplam doğru sayısı ve 100 üzerinden hesaplanan nihai başarı puanı estetik bir formatta sunularak test tamamlanır.
