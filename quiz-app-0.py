# Quiz App

# Question sınıfı
#   Instance Attributes
#       - text, choices, answer
#   Instance Methods
#       - q1.checkAnswer('python') => True ya da False

q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

sorular = [q1,q2,q3]

# Quiz sınıfı
#   Instance Attributes
#       - questions, questionIndex, score
#   Instance Methods
#       - getQuestion()         => questionIndex' e göre question nesnesi getirir.
#       - displayQuestion()     => getQuestion() ile alınan nesneyi gösterir.
#       - loadQuestion()        => Testi başlatır.
#       - displayScore()        => Score bilgisini gösterir.
#       - displayProgress()     => Testdeki ilerlemeyi gösterir. (5 sorunun 2.sorusundasınız.)


quiz = Quiz(sorular)


# display question içine soruyu yazdırma şıkları getirme(for) cevap alıp cevap doğruysa scoru bir artırma
# soru indeksi artırma ve loadQuestiona yönlendirme var

# loadQuestion içinde ise soru sayısı ve indeksler eşit olunca display score gösterme var (if)
# else kısmı ise display progress ve display quesiton var

# display scoreda ise puan, toplam puan, kaç sorunun kaç tanesini bildiniz ve toplam puanı yazdırma var

# display progress içinde kaç sorunun kaçında olduğunu yazdırma var. total tanımlanacak ve question number