![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

![](_page_0_Picture_2.jpeg)

![](_page_0_Picture_3.jpeg)

# RACHUNEK PRAWDOPODOBIEŃSTWA

### BARTOSZ KOŁODZIEJEK WYDZIAŁ MATEMATYKI I NAUK INFORMACYJNYCH

## Wykład

Projekt "NERW 2 PW. Nauka - Edukacja - Rozwój - Współpraca" współfinansowany ze środków Unii Europejskiej w ramach Europejskiego Funduszu Społecznego.

Zadanie 10 pn. "Modyfikacja programów studiów na kierunkach prowadzonych przez Wydział Matematyki i Nauk Informacyjnych", realizowane w ramach projektu "NERW 2 PW. Nauka - Edukacja - Rozwój - Współpraca", współfinansowanego jest ze środków Unii Europejskiej w ramach Europejskiego Funduszu Społecznego.

#### 29 stycznia 2022

#### Spis treści

| 1. W1 - Aksjomaty i przestrzeń probabilistyczna                                             | 2  |
|---------------------------------------------------------------------------------------------|----|
| Miara Lebesgue'a                                                                            | 4  |
| 2. W2 - Prawdopodobieństwo warunkowe                                                        | 5  |
| <b>♂</b> Konstrukcja zbioru niemierzalnego <b>♂</b>                                         | 6  |
| 3. W3 - Niezależność i Lematy Borela-Cantellego                                             | 7  |
| 4. W4 - Zmienne losowe, rozkłady i dystrybuanty                                             | Ö  |
| Całka względem miary                                                                        | 11 |
| 5. W5 - Wartość oczekiwana                                                                  | 13 |
| 6. W6 - Wariancja, nierówności i wektory losowe                                             | 14 |
| 7. W7 - Wektory losowe ciąg dalszy                                                          | 16 |
| 8. W8 - Wektory losowe dalszy ciąg dalszy                                                   | 18 |
| 9. W9 - Kowariancja, zbieżność według prawdopodobieństwa i SPWL                             | 20 |
| 10. W<br>10 - Zbieżność z prawdopodobieństwem 1 (MPWL), w $\mathcal{L}_p$ i według rozkładu | 22 |
| Dodatek - symulacje                                                                         | 24 |
| 11. W11 - Zbieżność według rozkładu ciąg dalszy                                             | 27 |
| 12. W12 - Centralne Twierdzenie Graniczne                                                   | 29 |
| 13. W13 - Warunkowa wartość oczekiwana                                                      | 31 |
| 14. W14 - Warunkowa wartość oczekiwana ciąg dalszy                                          | 33 |
| 15. W15 - Co warto pamiętać + uzupełnienia                                                  | 36 |

Legenda: 🗐 – Definicja, TW. – Twierdzenie, 📽 – Przykład, 🛕 – Uwaga, LEM. – Lemat, 👁 – Oznaczenie, 🎓 – do samodzielnej rozkminki, — dla chętnych (może być trudne)

#### 1. W1 - Aksjomaty i przestrzeń probabilistyczna

- <span id="page-1-0"></span> $(1.1) \ \ \text{Jeśli} \ \Omega \ \text{jest niepustym zbiorem, to przez} \ 2^{\Omega} \ \text{oznaczamy jego zbiór potęgowy, czyli zbiór wszystkich jego podzbio$ rów. Jeśli  $\Omega$  jest zbiorem skończonym, to mamy  $\#2^{\Omega} = 2^{\#\Omega}$ .
  - lacktriangle Symbol #A oznacza tutaj liczność (moc) zbioru A, często oznaczaną też przez  $\overline{A}$ .
- (1.2)  $\blacksquare$  Rodzinę  $\mathcal{F} \subset 2^{\Omega}$  (podzbiorów zbioru  $\Omega \neq \emptyset$ ) nazywamy  $\sigma$ -ciałem jeśli:
  - (a)  $\Omega \in \mathcal{F}$ .

  - (b)  $A \in \mathcal{F} \implies A^c = \Omega \setminus A \in \mathcal{F},$ (c)  $A_1, A_2, \ldots \in \mathcal{F} \implies \bigcup_{i=1}^{\infty} A_i \in \mathcal{F}.$
- (1.3) **A** Warunek (a) powyżej można zastąpić przez warunek (a')  $\emptyset \in \mathcal{F}$ .
  - A Warunek (c) powyżej można zastapić przez warunek
- (c')  $A_1, A_2, \ldots \in \mathcal{F} \implies \bigcap_{i=1}^{\infty} A_i \in \mathcal{F}$ . (1.4)  $\mathfrak{S}^{\mathfrak{s}}_{\bullet}$  Przykładami  $\sigma$ -ciał są  $\mathcal{F}_0 = \{\emptyset, \Omega\}, \ \mathcal{F}_1 = 2^{\Omega} \text{ oraz } \mathcal{F}_A = \{\emptyset, \Omega, A, A^c\} \text{ o ile } A \subset \Omega$ .
- (1.5)  $\triangle$  Każdą rodzinę  $\mathcal{A}$  podzbiorów zbioru  $\Omega$  można uzupełnić do  $\sigma$ -ciała.
- (1.6)  $\blacksquare$   $\sigma$ -ciało generowane przez rodzinę podzbiorów  $\mathcal{A}$  ( $\odot$   $\sigma(\mathcal{A})$ ) jest to najmniejsze  $\sigma$ -ciało zawierające  $\mathcal{A}$ :

$$\sigma(\mathcal{A}) = \bigcap_{\mathcal{F} - \sigma\text{-cialo: } \mathcal{A} \subset \mathcal{F}} \mathcal{F}.$$

- A Pokazać, że przeciecie dowolnej (być może nieprzeliczalnej) rodziny  $\sigma$ -ciał jest  $\sigma$ -ciałem.
- $\$ Pokazać, że jest tylko jedno najmniejsze  $\sigma$ -ciało zawierającę rodzinę  $\mathcal{A}$ .
- (1.7)  $\bullet_{\bullet}^{\bullet}$  Jeśli  $\mathcal{A} = \{A\}$ , to  $\sigma(\mathcal{A}) = \{\emptyset, \Omega, A, A^c\}$ .
- (1.8)  $\Omega = \{a, b, c, d\}, A = \{\{a, b\}, \{c\}\}\}$ . Pokazać, że  $\#\sigma(A) = 2^3$ .
- (1.9)  $\Omega = [0,1], A = \{(0,1), (1/2,1]\}, \sigma(A) = ?.$
- (1.10)  $\blacksquare \sigma$ -ciało zbiorów borelowskich  $\mathbb{R}$  ( $\bullet$   $\mathcal{B}(\mathbb{R})$ ) jest to  $\sigma$ -ciało generowane przez rodzinę otwartych przedziałów na prostej, tzn.  $\mathcal{B}(\mathbb{R}) = \sigma(\mathcal{A})$ , gdzie  $\mathcal{A} = \{(a, b) \subset \mathbb{R} : a < b\}$ .

 $\blacksquare$  Podobnie definiujemy  $\sigma$ -ciało zbiorów borelowskich  $\mathbb{R}^n$  ( $\bullet$   $\mathcal{B}(\mathbb{R}^n)$ ):  $\mathcal{B}(\mathbb{R}^n) = \sigma(\mathcal{A}_n)$ , gdzie

$$\mathcal{A}_n = \{(a_1, b_1) \times \ldots \times (a_n, b_n) \subset \mathbb{R}^n \colon a_i < b_i, i = 1, \ldots, n\}.$$

**A** Na ćwiczeniach dowiemy się, że  $\sigma$ -ciało zbiorów borelowskich może być zdefiniowane (i w sumie często jest) jako  $\sigma$ -ciało generowane przez rodzinę zbiorów otwartych (a nie tylko przedziałów).

- (1.11)  $\blacksquare$  Funkcję  $\mathbb{P}$  określoną na  $\sigma$ -ciele  $\mathcal{F} \subset 2^{\Omega}$  nazywamy prawdopodobieństwem jeśli
  - (a)  $A \in \mathcal{F} \implies \mathbb{P}(A) > 0$ ,
  - (b)  $\mathbb{P}(\Omega) = 1$ ,

  - (c)  $A_i \in \mathcal{F}, i = 1, 2, ...,$  oraz  $A_i \cap A_j = \emptyset$  dla  $i \neq j \implies \mathbb{P}(\bigcup_{i=1}^{\infty} A_i) = \sum_{i=1}^{\infty} \mathbb{P}(A_i).$ B Jeśli spełnione są tylko (a) i (c), to powiemy, że  $\mathbb{P}$  jest miarą. Jeśli  $\mathbb{P}(\Omega) < \infty$ , to  $\mathbb{P}$  jest miarą skończoną.

#### ▲ Warunek:

$$\forall A_1, A_2 \in \mathcal{F} \ A_1 \cap A_2 = \emptyset \implies \mathbb{P}(A_1 \cup A_2) = \mathbb{P}(A_1) + \mathbb{P}(A_2)$$

poprzez indukcję implikuje tzw. skończoną addytywność,

$$\forall n \ \forall A_1, \dots, A_n \ \forall i \neq j \ A_i \cap A_j = \emptyset \implies \mathbb{P}\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n \mathbb{P}(A_i),$$

która jest warunkiem **istotnie** słabszym niż warunek (c) z definicji prawdopodobieństwa

- (1.12) **TW.** Elementarne własności prawdopodobieństwa.
  - (a)  $\mathbb{P}(\emptyset) = 0$ .
  - (b)  $A_i \in \mathcal{F}, i = 1, ..., n, \text{ oraz } A_i \cap A_j = \emptyset \text{ dla } i \neq j \implies \mathbb{P}(\bigcup_{i=1}^n A_i) = \sum_{i=1}^n \mathbb{P}(A_i).$
  - (c)  $A, B \in \mathcal{F}, A \subset B \implies \mathbb{P}(B \setminus A) = \mathbb{P}(B) \mathbb{P}(A)$ .
  - (d)  $A \in \mathcal{F} \implies \mathbb{P}(A^c) = 1 \mathbb{P}(A)$ .
  - (e)  $A, B \in \mathcal{F}, A \subset B \implies \mathbb{P}(A) < \mathbb{P}(B).$
  - (f)  $A, B \in \mathcal{F} \implies \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) \mathbb{P}(A \cap B)$ .
  - $(g) \ A, B, C \in \mathcal{F} \implies \mathbb{P}(A \cup B \cup C) = \mathbb{P}(A) + \mathbb{P}(B) + \mathbb{P}(C) \mathbb{P}(A \cap B) \mathbb{P}(A \cap C) \mathbb{P}(B \cap C) + \mathbb{P}(A \cap B \cap C).$
  - (h) (Wzór włączeń i wyłączeń)  $A_i \in \mathcal{F}, i = 1, \ldots, n,$

$$\mathbb{P}\left(\bigcup_{i=1}^{n} A_{i}\right) = \sum_{j=1}^{n} (-1)^{j+1} \sum_{1 \leq i_{1} < i_{2} < \dots < i_{j} \leq n} \mathbb{P}\left(A_{i_{1}} \cap A_{i_{2}} \cap \dots \cap A_{i_{j}}\right).$$

Fakt przydatny w zadaniach:

$$\sum_{1 \le i_1 < i_2 < \dots < i_j \le n} 1 = \binom{n}{j}.$$

- (1.13) **TW.** Nieelementarne własności prawdopodobieństwa.
  - (a) (Podaddytywność) Jeśli  $A_1, A_2, \ldots \in \mathcal{F}$ , to

$$\mathbb{P}\left(\bigcup_{i=1}^{\infty} A_i\right) \le \sum_{i=1}^{\infty} \mathbb{P}(A_i)$$

Szkic dowodu:  $B_1 = A_1$ ,  $B_n = A_n \setminus \bigcup_{i=1}^{n-1} A_i$ ,  $n = 2, 3, \ldots$  Mamy  $B_n \in \mathcal{F}$ ,  $B_n \subset A_n$ ,  $(B_n)_{n \geq 1}$  są rozłączne oraz  $\bigcup_{i=1}^n B_i = \bigcup_{i=1}^n A_i$  dla  $n = 1, 2, \ldots, \infty$ . Zatem

$$\mathbb{P}\left(\bigcup_{i=1}^{\infty} A_i\right) = \mathbb{P}\left(\bigcup_{i=1}^{\infty} B_i\right) = \sum_{i=1}^{\infty} \mathbb{P}(B_i) \le \sum_{i=1}^{\infty} \mathbb{P}(A_i).$$

(b) (Ciągłość z dołu) Jeśli  $A_1, A_2, \ldots \in \mathcal{F}$  oraz  $A_i \subset A_{i+1}$  dla  $i = 1, 2, \ldots$ , to

$$\mathbb{P}\left(\bigcup_{i=1}^{\infty} A_i\right) = \lim_{n \to \infty} \mathbb{P}(A_n).$$

Szkic dowodu:  $B_1 = A_1$ ,  $B_n = A_n \setminus A_{n-1}$  dla  $n = 2, 3, \dots$  Zdarzenia  $(B_n)_{n \geq 1}$  sa rozłączne, zatem

$$\mathbb{P}\left(\bigcup_{i=1}^{\infty}A_i\right) = \mathbb{P}\left(\bigcup_{i=1}^{\infty}B_i\right) = \sum_{i=1}^{\infty}\mathbb{P}(B_i) = \lim_{n \to \infty}\sum_{i=1}^{n}\mathbb{P}(B_i) = \lim_{n \to \infty}\mathbb{P}(A_n),$$

ponieważ  $\mathbb{P}(B_i) = \mathbb{P}(A_i) - \mathbb{P}(A_{i-1}) \text{ dla } i \geq 2.$ 

(c) (Ciągłość z góry) Jeśli  $A_1, A_2, \ldots \in \mathcal{F}$  oraz  $A_{i+1} \subset A_i$  dla  $i=1,2,\ldots$ , to

$$\mathbb{P}\left(\bigcap_{i=1}^{\infty} A_i\right) = \lim_{n \to \infty} \mathbb{P}(A_n).$$

Szkic dowodu:  $A_n^c \subset A_{n+1}^c, \ n=1,2,\ldots$  Zatem (prawo de Morgana:  $(\bigcap_n A_n)^c = \bigcup_n A_n^c)$  z ciągłości z dołu

$$\mathbb{P}\left(\bigcap_{i=1}^{\infty} A_i\right) = 1 - \mathbb{P}\left(\bigcup_{i=1}^{\infty} A_i^c\right) = 1 - \lim_{n \to \infty} \mathbb{P}(A_n^c) = \lim_{n \to \infty} \mathbb{P}(A_n).$$

- (1.14)  $\blacksquare$  Przestrzenią probabilistyczną nazywamy trójkę  $(\Omega, \mathcal{F}, \mathbb{P})$ , gdzie
  - $\Omega$  jest niepustym zbiorem,
  - $\mathcal{F}$  jest  $\sigma$ -ciałem podzbiorów  $\Omega$ ,
  - $\mathbb{P}$  jest prawdopodobieństwem na  $\mathcal{F}$ .
  - $\blacksquare$  Parę  $(\Omega, \mathcal{F})$  będziemy nazywali przestrzenią mierzalną.
  - Elementy  $\Omega$  nazywamy zdarzeniami elementarnymi. Elementy  $\mathcal{F}$  to po prostu zdarzenia. W szczególności,  $\emptyset$  zdarzenie niemożliwe,  $\Omega$  zdarzenie pewne.

Jeśli  $A \in \mathcal{F}$  oraz  $\mathbb{P}(A) = 1$ , to powiemy, że zdarzenie A zajdzie <u>prawie na pewno</u>. Jeśli  $A \in \mathcal{F}$  oraz  $\mathbb{P}(A) = 0$ , to powiemy, że zdarzenie A prawie na pewno nie zajdzie.

(1.15) Elementy kombinatoryki.

Twierdzenie o mnożeniu:

$$\#(A_1 \times \ldots \times A_n) = (\#A_1) \cdot \ldots \cdot (\#A_n).$$

Niech dalej #A = n.

• Wybory uporządkowane ze zwracaniem: (wariacje z powtórzeniami)

$$\#\{(a_1,\ldots,a_r): a_j \in A, j=1,\ldots,r\} = n^r$$
.

• Wybory uporządkowane bez zwracania: (wariacje bez powtórzeń)

$$\#\{(a_1,\ldots,a_r): a_j \in A, \ a_j \neq a_k \ \text{dla} \ j \neq k\} = \frac{n!}{(n-r)!}, \quad r \leq n.$$

• Wybory nieuporządkowane bez zwracania: (kombinacje)

$$\#\{\{a_1,\ldots,a_r\}: a_j \in A, \ a_j \neq a_k \ \text{dla} \ j \neq k\} = \binom{n}{r}, \quad r \leq n.$$

- (1.16) 🗱 Przykłady przestrzeni probabilistycznych
  - (a) Schemat klasyczny:  $\#\Omega < \infty$ ,  $\mathcal{F} = 2^{\Omega}$ ,  $\mathbb{P}(A) := \frac{\#A}{\#\Omega}$ .
  - (b) Uogólniony schemat klasyczny:  $\Omega$  zbiór przeliczalny,  $\mathcal{F} = 2^{\Omega}$ ,  $\mathbb{P}(A) = \sum_{\omega \in A} p(\omega)$ , gdzie  $p \colon \Omega \to [0, 1]$  jest funkcją taką, że  $\sum_{\omega \in \Omega} p(\omega) = 1$ .
    - $\Omega = \{0, 1, 2, \ldots\}, p(\omega) = q(1 q)^{\omega} \text{ dla pewnego } q \in (0, 1).$
  - (c) Schemat geometryczny:  $\Omega \subset \mathbb{R}^n$  zbiór ograniczony,  $\mathcal{F} = \mathcal{B}(\Omega) := \{A \cap \Omega \colon A \in \mathcal{B}(\mathbb{R}^n)\}$ ,  $\lambda_n$  tzw. miara Lebesgue'a, czyli naturalne uogólnienie pojęcia długości/pola/objętości,  $\mathbb{P}(A) = \frac{\lambda_n(A)}{\lambda_n(\Omega)}$ . O mierze Lebesgue'a dalei.
    - $\bf A$  Zaskakujący na tym etapie może być wybór  $\sigma$ -ciała. Dlaczego nie wzieliśmy po prostu  ${\cal F}=2^{\Omega}$ ? Okazuje się, że taki wybór jest niemożliwy, ponieważ to  $\sigma$ -ciało jest zbyt bogate i zawiera zbiory którym nie można nadać miary. Szczegóły już niedługo.
    - (Losowe rendez-vous) Asia i Krysia umawiają się na spotkanie między 12 a 13. Ustaliły wcześniej, że każda czeka 15 minut i odchodzi. Obie przychodzą niezależnie od siebie w losowym momencie między 12 i 13. Oblicz prawdopodobieństwo, że się spotkają.

#### <span id="page-3-0"></span>MIARA LEBESGUE'A

Jeśli zbiór  $A \subset \mathbb{R}$  jest domkniętym przedziałem, tzn. A = [a, b] dla pewnych a < b, to definiujemy jego długość poprzez

$$|A| = |[a, b]| = b - a.$$

Chcemy rozszerzyć pojęcie długości na zbiory ogólniejszej klasy niż domknięte przedziały. Dla dowolnego zbioru  $A \subset \mathbb{R}$  definiujemy tzw. miare zewnętrzną Lebesgue'a, tzn.

$$\lambda^*(A) = \inf \left\{ \sum_{B \in \mathcal{C}} |B| \colon \mathcal{C} \text{ jest przeliczalną rodziną przedziałów domkniętych, która pokrywa } A \right\}.$$

Powyższe infimum przebiega wszystkie rodziny przedziałów  $\mathcal{C} = \{B_1, \ldots, B_n\}$  pokrywające zbiór A tzn. takie, że  $A \subset \bigcup_k B_k$  oraz każdy z  $B_k$  jest przedziałem.

 $\blacksquare$  Powiemy, że zbiór  $A \subset \mathbb{R}$  jest mierzalny w sensie miary Lebesgue'a, jeśli zachodzi (warunek Carathéodory'ego)

$$\lambda^*(S) = \lambda^*(S \cap A) + \lambda^*(S \cap A^c), \qquad \forall S \subset \mathbb{R}.$$

 $\triangle$  Okazuje się, że zbiory A spełniające ten warunek tworzą  $\sigma$ -ciało, czasem zwane  $\sigma$ -ciałem Lebesgue'a.

 $\Delta$  To σ-ciało zawiera w sobie σ-ciało zbiorów borelowskich  $\mathcal{B}(\mathbb{R})$ , ale jest istotnie większe (nawet w sensie mocy), tzn. istnieją zbiory mierzalne w sensie miary Lebesgue'a, które nie są borelowskie.

 $\blacksquare$  Miarę Lebesgue'a zbioru A z  $\sigma$ -ciała Lebesgue'a definiujemy jako  $\lambda(A) := \lambda^*(A)$ .

Miara Lebesgue'a jest zupełna w tym sensie, że jeśli zbiór A jest mierzalny w sensie Lebesgue'a oraz  $\lambda(A) = 0$ , to wszystkie podzbiory A również należą do  $\sigma$ -ciała Lebesgue'a i w konsekwencji mają miarę Lebesgue'a zero.

Na potrzeby rachunku prawdopodobieństwa zwykle wystarcza rozważać miarę Lebesgue'a na  $\sigma$ -ciele zbiorów borelowskich.

Miarę Lebesgue'a ( $\otimes \lambda_n$ ) na  $\mathbb{R}^n$  definiuje się podobnie poprzez zadanie miary kostki n-wymiarowej:

$$|[a_1,b_2] \times [a_2,b_2] \times \ldots \times [a_n,b_n]| = \prod_{k=1}^n (b_k - a_k).$$

 $\wedge$  Uzasadnij, że  $\mathbb{Q} \in \mathcal{B}(\mathbb{R})$  oraz oblicz  $\lambda(\mathbb{Q})$ .

#### 2. W2 - Prawdopodobieństwo warunkowe

- <span id="page-4-0"></span>(2.1) CP Przykłady przestrzeni probabilistycznych
  - (a) Schemat klasyczny:  $\#\Omega < \infty$ ,  $\mathcal{F} = 2^{\Omega}$ ,  $\mathbb{P}(A) := \frac{\#A}{\#\Omega}$ .
  - (b) Uogólniony schemat klasyczny:  $\Omega$  zbiór przeliczalny,  $\mathcal{F} = 2^{\Omega}$ ,  $\mathbb{P}(A) = \sum_{\omega \in A} p(\omega)$ , gdzie  $p \colon \Omega \to [0, 1]$  jest funkcją taką, że  $\sum_{\omega \in \Omega} p(\omega) = 1$ .
    - $\Omega = \{0, 1, 2, \ldots\}, \ p(\omega) = q(1-q)^{\omega} \ dla \ pewnego \ q \in (0, 1).$
  - (c) Schemat geometryczny:  $\Omega \subset \mathbb{R}^n$  zbiór ograniczony,  $\mathcal{F} = \mathcal{B}(\Omega) := \{A \cap \Omega \colon A \in \mathcal{B}(\mathbb{R}^n)\}, \lambda_n$  miara Lebesgue'a na  $\mathcal{B}(\mathbb{R}^n)$ ,  $\mathbb{P}(A) = \frac{\lambda_n(A)}{\lambda_n(\Omega)}$ .
    - (Losowe rendez-vous) Asia i Krysia umawiają się na spotkanie między 12 a 13. Ustaliły wcześniej, że każda czeka 15 minut i odchodzi. Obie przychodzą niezależnie od siebie w losowym momencie między 12 i 13. Oblicz prawdopodobieństwo, że się spotkają.
- (2.2)  $\mathbf{A}$  W schemacie geometrycznym  $\Omega$  jest nieprzeliczalna i okazuje się, że nie istnieje prawdopodobieństwo  $\mathbb{P}$  na  $\mathcal{F} = 2^{\Omega}$ . Za pomocą Aksjomatu Wyboru można skonstruować patologiczne zbiory dla których nie można zdefiniować miary. O konstrukcji zbiorów niemierzalnych dalej (dla chętnych).
- (2.3) Raradoks Bertranda. Rzucamy losowo cięciwę na okrąg. Jakie jest prawdopodobieństwo, że jej długość będzie większa od długości boku trójkąta równobocznego wpisanego w ten okrąg?
  - I. Ustalamy punkt na okręgu i rozważamy kąty jakie tworzą cięciwy przechodzące przez ten punkt ze styczną do okręgu w tym punkcie:  $\Omega = [0, \pi], A = [\pi/3, 2\pi/3]$ . Zatem

$$\mathbb{P}(A) = \frac{\lambda(A)}{\lambda(\Omega)} = \frac{\pi/3}{\pi} = \frac{1}{3}.$$

II. Ustalamy kierunek i rozważamy cięciwy równoległe. Wtedy wystarczy badać położenie środka cięciw na średnicy, tzn.  $\Omega = [0, 2r]$ , oraz A = [r/2, 3r/2], gdzie r jest promieniem okręgu. Czyli

$$\mathbb{P}(A) = \frac{\lambda(A)}{\lambda(\Omega)} = \frac{r}{2r} = \frac{1}{2}.$$

III. Bierzemy pod uwagę środki cięciw.  $\Omega = \{(x,y) : x^2 + y^2 < r^2\}$ . Interesuje nas zdarzenie, gdy środek cięciwy leży wewnątrz okręgu wpisanego w trójkąt równoboczny, tzn.  $A = \{(x,y) : x^2 + y^2 < r^2/4\}$ . Wobec tego

$$\mathbb{P}(A) = \frac{\lambda(A)}{\lambda(\Omega)} = \frac{\pi r^2/4}{\pi r^2} = \frac{1}{4}.$$

(2.4)  $\blacksquare$  Niech  $A, B \in \mathcal{F}$  oraz  $\mathbb{P}(B) > 0$ . Prawdopodobieństwem warunkowym zdarzenia A pod warunkiem B nazywamy wielkość

$$\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}.$$

- (2.5) Ciąg zbiorów  $(A_1, A_2, ...)$  nazwiemy <u>przeliczalnym rozbiciem zbioru  $\Omega$ </u>, jeśli  $A_i \in \mathcal{F}$  dla  $i = 1, 2, ..., \bigcup_{i=1}^{\infty} A_i = \Omega$  oraz  $A_i \cap A_j = \emptyset$  dla  $i \neq j$ . Przeliczalne rozbicie  $(A_1, A_2, ...)$  nazwiemy <u>nietrywialnym</u>, jeśli  $\mathbb{P}(A_i) > 0$  dla i = 1, 2, ...
  - lacktriangle Zamiast pisać  $(A_1, A_2, \ldots)$ , będziemy czasem równoważnie pisać  $(A_n)_{n=1}^{\infty}$  lub, jeszcze krócej,  $(A_n)_n$ .
- (2.6) **TW.** (Wzór na prawdopodobieństwo całkowite) Niech  $(A_n)_{n\geq 1}$  będzie nietrywialnym przeliczalnym rozbiciem  $\Omega$ . Dla każdego  $B\in\mathcal{F}$  zachodzi

$$\mathbb{P}(B) = \sum_{n=1}^{\infty} \mathbb{P}(B|A_n)\mathbb{P}(A_n).$$

(2.7) **TW.** (<u>Wzór Bayesa</u>) Przy założeniach wzoru na prawdopodobieństwo całkowite oraz jeśli dodatkowo  $\mathbb{P}(B) > 0$ , to

$$\mathbb{P}(A_k|B) = \frac{\mathbb{P}(B|A_k)\mathbb{P}(A_k)}{\sum_{n=1}^{\infty} \mathbb{P}(B|A_n)\mathbb{P}(A_n)}.$$

- Załóżmy, że przy badaniu narkomana test wypada pozytywnie w 99% przypadków, zaś przy badaniu osoby nie zażywającej narkotyków wypada negatywnie w 99% przypadków. Pewna firma postanowiła przebadać swoich pracowników takim testem, wiedząc, że 0.5% z nich to narkomani. Jakie jest prawdopodobieństwo, że osoba, u której test wypadł pozytywnie, rzeczywiście zażywa narkotyki? ( $\approx 1/3$ )
- Paradoks Monty Halla, "Idź na całość". Zawodnik stoi przed trzema zasłoniętymi bramkami. Za jedną z nich (za którą wie to tylko prowadzący program stary Hajzer) jest nagroda (umieszczana całkowicie losowo), za pozostałymi kot ZONK. Gracz wybiera jedną z bramek. Prowadzący program odsłania inną bramkę (co istotne anonsując, że jest to bramka pusta), po czym proponuje graczowi zmianę wyboru. Co powinien zrobić gracz?

#### <span id="page-5-0"></span>■ Konstrukcja zbioru niemierzalnego

Stosunkowo trudno jest wskazać zbiór, który nie jest borelowski (czyli nie należy do  $\mathcal{B}(\mathbb{R})$ ). Poniżej skonstruujemy zbiór, który nie tylko nie jest borelowski, co nie jest również mierzalny w sensie miary Lebesgue'a. Zbiór ten jest zwany zbiorem Vitalli'ego. Pokażemy, że dla tego zbioru nie można zdefiniować wartości  $\lambda(E)$ . Przypisanie jakiejkolwiek wartości  $\lambda(E)$  prowadzi do sprzeczności. Konstrukcja takich zbiorów jest bardzo delikatna i wymaga przyjęcia tzw. aksjomatu wyboru. Bez tego aksjomatu nie jest możliwe udowodnienie istnienia zbioru niemierzalnego względem miary Lebesgue'a.

- Aksjomat wyboru: istnieje zbiór zawierający dokładnie po jednym elemencie z każdego zbioru należącego do danej rodziny niepustych zbiorów rozłącznych. Aksjomat ten ma zastosowanie gdy rodzina zbiorów jest nieskończona (dla skończonych rodzin własność ta wynika z innych aksjomatów). Aksjomat wyboru nie jest powszechnie przyjęty przez społeczność matematyków. Przy aksjomacie wyboru Banach i Tarski udowodnili twierdzenie o paradoksalnym rozkładzie kuli: kulę z trójwymiarowej przestrzeni euklidesowej można rozłożyć na sześć cześci, a następnie z tych cześci można złożyć, korzystajac wyłącznie z
- Zdefiniujmy relację  $\sim$  na  $\mathbb{R}^2$  w następujący sposób:

$$x \sim y \iff x - y \in \mathbb{Q}.$$

obrotów i przesunięć, dwie kule identyczne jak kula wyjściowa. Te sześć części jest właśnie niemierzalne.

- Relacja ~ jest relacją równoważności (zwrotna, symetryczna, przechodnia).
- Relacja równoważności  $\sim$  dzieli  $\mathbb R$  na klasy abstrakcji: klasa abstrakcji elementu  $a \in \mathbb R$  jest

$$[a] = \{x \in \mathbb{R} : x \sim a\} = \{x \in \mathbb{R} : x - a \in \mathbb{Q}\}.$$

- Niech  $\mathcal{E} = \{[a]: a \in \mathbb{R}\}$  będzie zbiorem takich klas abstrakcji. Jest ich nieprzeliczalnie wiele. Korzystając z aksjomatu wyboru (delikatny punkt!) można skonstruować zbiór E w następujący sposób: do zbioru E wybieramy po jednym punkcie z każdej klasy abstrakcji, tzn. dla każdego  $x \in [0, 1]$  zbiór  $[x] \cap E$  jest jednopunktowy.
- Jeśli  $u, w \in \mathbb{Q}$  i  $u \neq w$ , to  $(E+u) \cap (E+w) = \emptyset$ . W przeciwnym wypadku istniałby  $x \in (E+u) \cap (E+w)$ , tzn.  $x = e_1 + u = e_2 + w$ , gdzie  $e_1, e_2 \in E$ . Ale równość  $e_1 = e_2 + (w-u)$  oznacza, że  $e_1 \sim e_2$ , co stoi w sprzeczności z definicją zbioru E. (e wynikiem działania E + x jest zbiór  $\{e + x : e \in E\}$ ).

- Niech ciąg  $(q_i)_{i=1}^{\infty}$  będzie ciągiem wszystkich liczb wymiernych z odcinka [-1,1]. Wtedy  $[0,1] \subset \bigcup_{i=1}^{\infty} (E+q_i)$ . Rzeczywiście, niech  $x \in [0,1]$  oraz rozważmy klasę abstrakcji [x]. Z definicji zbioru E mamy  $E \cap [x] = \{x_0\}$  dla pewnego  $x_0 \in [0,1] \cap E$ . Oznacza to, że  $x_0 x \in \mathbb{Q} \cap [-1,1]$ , czyli istnieje indeks i taki, że  $x_0 x = q_i$ , czyli  $x \in E + q_i$ .
- Niech  $\mu$  będzie miarą określoną na pewnym  $\sigma$ -ciele  $\mathcal{F}$  z następującymi własnościami: a) przesuwalność, tzn.  $\mu(A) = \mu(x+A)$  dla każdego  $x \in \mathbb{R}$   $(x+A=\{x+a\colon a\in A\})$  oraz b)  $\mu([a,b])=b-a$ . Przykładem takiej miary jest miara Lebesgue'a. Dowód niemierzalności zbioru E jest przeprowadzany nie wprost. Powiedzmy, że E jest mierzalny, czyli  $E \in \mathcal{F}$ . Prawdziwe jest zawieranie

$$[0,1] \subset \bigcup_{i=1}^{\infty} (E+q_i) \subset [-1,2]$$

oraz z wcześniejszych rozważań wiemy, że zbiory  $(E+q_i)_{i=1}^\infty$ są rozłączne. Zatem

$$1 = \mu([0,1]) \le \sum_{k=1}^{\infty} \mu(E+q_i) \le \mu([-1,2]) = 3.$$

Ale z przesuwalności,  $\mu(E+w_i)=\mu(E)$ , zatem pierwsza nierówność wskazuje, że  $\mu(E)=\infty$ , podczas gdy druga daje  $\mu(E)=0$ . Sprzeczność.

• Powyżej skonstruowaliśmy zbiór niemierzalny w sensie miary Lebesgue'a. Ogólnie, przy założeniu hipotezy Continuum, jeśli  $0 < \mu([0,1]) < \infty$  oraz  $\mu(\{x\}) = 0$  dla każdego  $x \in [0,1]$ , to istnieje zbiór niemierzalny względem  $\mu$ . Innymi słowy,  $\mu$  nie może być miarą na  $(\Omega, \mathcal{F}) = ([0,1], 2^{[0,1]})$ .

#### 3. W3 - Niezależność i Lematy Borela-Cantellego

<span id="page-6-0"></span>(3.1)  $\blacksquare$  Niech  $(\Omega, \mathcal{F}, \mathbb{P})$  będzie przestrzenią probabilistyczną. Powiemy, że zdarzenia A i B są niezależne, jeśli

$$\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B).$$

- Rzucamy dwukrotnie monetą. Niech  $A_i$  oznacza zdarzenie, że otrzymaliśmy orła w i-tym rzucie, i=1,2. Zdarzenia  $A_1$  i  $A_2$  są niezależne.
- Schemat geometryczny,  $\Omega = [-1,1]^2$ ,  $A = \{(x,y) \in \Omega \colon x > 0 \land y > 0\}$  oraz  $B = \{(x,y) \in \Omega \colon x^2 + y^2 \le 1/4\}$ . Zdarzenia A i B są niezależne.
- (3.2) A Niech zdarzenia A i B będą niezależne. Pokazać, że wtedy niezależne są również zdarzenia
  - $A i B^c$ ,
  - $A^c$  i B,
  - $A^c$  i  $B^c$ .
- (3.3)  $\blacksquare$  Zdarzenia A, B, C są niezależne, jeśli  $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$ ,  $\mathbb{P}(A \cap C) = \mathbb{P}(A)\mathbb{P}(C)$ ,  $\mathbb{P}(B \cap C) = \mathbb{P}(B)\mathbb{P}(C)$  oraz  $\mathbb{P}(A \cap B \cap C) = \mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C)$ , przy czym nie wystarcza sprawdzać ostatniego lub pierwszych trzech warunków. Sprawdzić zachodzenie powyższych warunków w dwóch poniższych przykładach:
  - Rzucamy dwa razy kostką. Zdefiniuj<br/>my zdarzenia A otrzymaliśmy dublet, B suma należy do  $\{7,8,9,10\}$ ,<br/> C suma należy do  $\{2,7,8\}$ .
  - Rzucamy czworościanem foremnym, który ma jedną ścianę białą, jedną czerwoną, jedną zieloną oraz jedną w pasy biało-czerwono-zielone. Definiujemy zdarzenia A, B, C - wypadła ścianka z kolorem, odpowiednio, zielonym, białym, czerwonym.
- (3.4)  $\blacksquare$  Niech  $A_1, \ldots, A_n \in \mathcal{F}, n \geq 2$ . Powiemy, że zdarzenia  $A_1, \ldots, A_n$  są niezależne, jeśli

$$\forall k \in \{2, \dots, n\} \quad \forall \{i_1, \dots, i_k\} \subset \{1, \dots, n\} \quad \mathbb{P}(A_{i_1} \cap \dots \cap A_{i_k}) = \mathbb{P}(A_{i_1}) \dots \mathbb{P}(A_{i_k}).$$

- (3.5)  $\ \ \,$  Oznaczmy  $A^{(1)}=A$  oraz  $A^{(-1)}=A^c$ . Uzasadnić, że jeśli  $A_1,\ldots,A_n$  są niezależne, to dla każdego  $\underline{\varepsilon}=(\varepsilon_1,\ldots,\varepsilon_n)\in\{-1,1\}^n$ , niezależne są również  $A_1^{(\varepsilon_1)},\ldots,A_n^{(\varepsilon_n)}$ .
- (3.6)  $\bullet$  (Schemat Bernoulliego) Wykonujemy n niezależnych prób pewnego eksperymentu, przy czym p-stwo sukcesu w każdej z prób jest takie samo i wynosi  $p \in (0,1)$ .

Niech  $B_k$  oznacza zdarzenie, że uzyskano dokładnie k sukcesów, k = 0, ..., n, oraz niech  $A_i$  oznacza, że uzyskano sukces w i-tej próbie, i = 1, ..., n. Wtedy

$$\mathbb{P}(B_k) = \sum_{\varepsilon \in \{-1,1\}^n \colon \#\{j \colon \varepsilon_i = 1\} = k} \mathbb{P}(A_1^{(\varepsilon_1)} \cap \ldots \cap A_n^{(\varepsilon_n)}) = \binom{n}{k} p^k (1-p)^{n-k}.$$

Niech  $C_k^r$  oznacza zdarzenie, że r-ty sukces będzie poprzedzony k porażkami,  $r \in \mathbb{N}, k \in \mathbb{N} \cup \{0\}$ . Wtedy

$$\mathbb{P}(C_k^r) = \sum_{\underline{\varepsilon} \in \{-1,1\}^{r+k-1} \colon \#\{j \colon \varepsilon_j = 1\} = r-1} \mathbb{P}(A_1^{(\varepsilon_1)} \cap \ldots \cap A_{r+k-1}^{(\varepsilon_{r+k-1})} \cap A_{r+k}) = \binom{r+k-1}{k} p^r (1-p)^k.$$

(3.7) Niech  $(A_n)_{n\geq 1}$  będzie ciągiem zbiorów. Wtedy

$$\liminf_{n \to \infty} A_n = \bigcup_{n=1}^{\infty} \bigcap_{m=n}^{\infty} A_m$$

oraz

$$\limsup_{n \to \infty} A_n = \bigcap_{m=1}^{\infty} \bigcup_{m=n}^{\infty} A_m.$$

**A** Jeśli  $A_n \in \mathcal{F}$  dla  $n \in \mathbb{N}$ , to  $\liminf_{n \to \infty} A_n \in \mathcal{F}$  oraz  $\limsup_{n \to \infty} A_n \in \mathcal{F}$ .

igotimes W skrócie będziemy czasem pisali  $\liminf_n$  i  $\limsup_n$ .

**A** Z praw de Morgana mamy

$$(\liminf_n A_n)^c = \limsup_n A_n^c$$
 oraz  $(\limsup_n A_n)^c = \liminf_n A_n^c$ .

**A** Niech  $\mathbb{1}_A$  będzie funkcją indykatorową zbioru A, tzn,  $\mathbb{1}_A(\omega) := \begin{cases} 1, & \omega \in A, \\ 0, & \omega \notin A. \end{cases}$ . Wtedy

$$\limsup_{n\to\infty}A_n=\left\{\omega\in\Omega\colon \sum_{n=1}^\infty\mathbbm{1}_{A_n}(\omega)=\infty\right\},\qquad \liminf_{n\to\infty}A_n=\left\{\omega\in\Omega\colon \sum_{n=1}^\infty\mathbbm{1}_{A_n^c}(\omega)<\infty\right\}.$$

Innymi słowy,  $\limsup_{n\to\infty}A_n$  oznacza zdarzenie, że zaszło nieskończenie wiele zdarzeń spośród  $(A_n)_n$ . Z kolei  $\liminf_{n\to\infty}A_n$  oznacza, że zaszło skończenie wiele zdarzeń spośród  $(A_n^c)_n$  (czyli w szczególności zaszło nieskończenie wiele zdarzeń  $(A_n)_n$ ).

 $\triangle$   $\liminf_{n\to\infty} A_n \subset \limsup_{n\to\infty} A_n$ .

(3.8) **TW.** (I Lemat Borela-Cantellego) Niech  $(A_n)_{n\geq 1}$  będzie ciągiem zdarzeń. Jeśli

$$\sum_{n=1}^{\infty} \mathbb{P}(A_n) < \infty,$$

to  $\mathbb{P}(\limsup_{n} A_n) = 0$ .

- Szkic dowodu:  $\mathbb{P}(\limsup_n A_n) \leq \mathbb{P}(\bigcup_{m=n}^{\infty} A_m) \leq \sum_{m=n}^{\infty} \mathbb{P}(A_m) \xrightarrow{n \to \infty} 0.$  (3.9)  $\blacksquare$  Powiemy, że  $(A_n)_{n \geq 1}$  jest (nieskończonym) ciągiem zdarzeń niezależnych, jeśli dla każdego  $k \geq 2$  zdarzenia  $A_1, \ldots, A_k$  są niezależne.
  - $\P$  Uzasadnić, że jeśli zdarzenia  $(A_n)_{n\geq 1}$  są niezależne, to  $\mathbb{P}(\cap_{n\geq 1}A_n)=\prod_{n=1}^{\infty}\mathbb{P}(A_n)$ .
- (3.10) **TW.** (II Lemat Borela-Cantellego) Niech  $(A_n)_{n\geq 1}$  będzie ciągiem zdarzeń niezależnych. Jeśli

$$\sum_{n=1}^{\infty} \mathbb{P}(A_n) = \infty,$$

to  $\mathbb{P}(\limsup_{n} A_n) = 1$ .

Szkic dowodu: Dla każdego  $n \in \mathbb{N}$  zachodzi

$$\mathbb{P}\left(\bigcap_{k=n}^{\infty}A_{k}^{c}\right)\leq \mathbb{P}\left(\bigcap_{k=n}^{n+m}A_{k}^{c}\right)=\prod_{k=n}^{n+m}(1-\mathbb{P}(A_{k}))\leq \prod_{k=n}^{n+m}e^{-\mathbb{P}(A_{k})}=e^{-\sum_{k=n}^{n+m}\mathbb{P}(A_{k})}\overset{m\to\infty}{\longrightarrow}0.$$

[Powyżej skorzystaliśmy z nierówności  $1-x \le e^{-x}$  dla  $x \ge 0$ .] Zatem,

$$0 \le 1 - \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = \mathbb{P}\left(\bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} A_k^c\right) \le \sum_{n=1}^{\infty} \mathbb{P}\left(\bigcap_{k=n}^{\infty} A_k^c\right) = 0.$$

- (3.11)  $\triangle$  Wniosek z Lematów Borela-Cantellego: Jeśli  $(A_n)_{n\geq 1}$  jest ciągiem zdarzeń niezależnych, to zdarzenie lim sup<sub>n</sub>  $A_n$ zachodzi z prawdopodobieństwem 0 lub 1.
  - **A** Skonstruować przykład zdarzeń  $(A_n)_{n\geq 1}$  dla którego zachodzi  $\mathbb{P}(\limsup_n A_n)=3/4$ .

- (3.12) 🗱 Załóżmy, że małpa żyje nieskończenie długo i posadźmy ją przed klawiaturą komputera. Małpa w sposób losowy uderza w klawisze. Po nieskończonym czasie uzyskamy w ten sposób nieskończony ciąg znaków. Jakie jest prawdopodobieństwo, że, poczynając od pewnego miejsca, małpa wiernie odtworzyła Pana Tadeusza? Jakie jest prawdopodobieństwo, że małpa napisała go nieskończenie wiele razy? Przyjmij, że klawiatura ma 101 klawiszy, Pan Tadeusz składa się z 68682 wyrazów oraz średnia liczba znaków w słowie (w języku polskim) to 7.21. https://en.wikipedia.org/wiki/Infinite\_monkey\_theorem
  - 4. W4 Zmienne Losowe, rozkłady i dystrybuanty
- <span id="page-8-0"></span>(4.1) Funkcję  $X: \Omega \to \mathbb{R}$  nazywamy zmienną losową (na przestrzeni mierzalnej  $(\Omega, \mathcal{F})$ ), jeśli jest ona  $\mathcal{F}$ -mierzalna, tzn.

$$\forall B \in \mathcal{B}(\mathbb{R}) \quad X^{-1}(B) := \{ \omega \in \Omega \colon X(\omega) \in B \} \in \mathcal{F}.$$

- $\blacksquare$  Zbiór  $X^{-1}(B)$  nazywamy przeciwobrazem zbioru B przy przekształceniu X.
- ↑ Udowodnij następujące własności przeciwobrazu:

  - $f^{-1}(\bigcap_{i} B_{i}) = \bigcap_{i} f^{-1}(B_{i}),$   $f^{-1}(\bigcup_{i} B_{i}) = \bigcup_{i} f^{-1}(B_{i}),$   $f^{-1}(A^{c}) = (f^{-1}(A))^{c}.$
- (4.2)  $\mathbf{x}^{\mathbf{z}}$  Jeśli  $A \in \mathcal{F}$ , to funkcja  $X : \Omega \to \mathbb{R}$  zdefiniowana przez

$$X(\omega) = \mathbb{1}_A(\omega) = \begin{cases} 1, & \omega \in A, \\ 0, & \omega \notin A, \end{cases}$$

jest zmienna losowa.

- (4.3)  $\blacktriangleleft$  Funkcja  $X: \Omega \to \mathbb{R}$  jest  $\mathcal{F}_0$ -mierzalna, gdzie  $\mathcal{F}_0 = \{\emptyset, \Omega\}$ . Pokazać, że X jest funkcją stałą.
- (4.4)  $\blacksquare$  Rodzinę  $\Pi$  podzbiorów zbioru T nazywamy  $\pi$ -układem, jeśli spełnione są dwa warunki
  - (a)  $T \in \Pi$ ,
  - (b)  $A, B \in \Pi \implies A \cap B \in \Pi$ .
  - $\blacksquare$  Rodzinę  $\Lambda$  podzbiorów zbioru T nazywamy  $\lambda$ -układem, jeśli spełnione są trzy warunki
  - (a)  $T \in \Lambda$ .
  - (b)  $A, B \in \Lambda$  oraz  $A \subset B \implies B \setminus A \in \Lambda$ ,
  - (c)  $A_n \in \Lambda$  oraz  $A_n \subset A_{n+1}, n = 1, 2, ... \implies \bigcup_{n=1}^{\infty} A_n \in \Lambda$ .
  - **TW.** (Lemat o  $\pi \lambda$  układach) Jeśli  $\Pi$  jest  $\pi$ -układem,  $\Lambda$  jest  $\lambda$ -układem oraz  $\Pi \subset \Lambda$ , to  $\sigma(\Pi) \subset \Lambda$ .
- (4.5) **TW.** Następujące warunki są równoważne:
  - (a) X jest zmienną losową,
  - (b)  $\forall t \in \mathbb{R} \quad X^{-1}((-\infty, t]) \in \mathcal{F},$
  - (c)  $\forall t \in \mathbb{R} \quad X^{-1}((-\infty, t)) \in \mathcal{F}.$

Szkic dowodu: z (a) do (c) łatwe. Z (c) do (b) należy zauważyć, że  $(-\infty,t] = \bigcap_{\varepsilon \in \mathbb{O} \cap (0,\infty)} (-\infty,t+\varepsilon)$  oraz skorzystać z własności przeciwobrazu.

Dowód (b)  $\Longrightarrow$  (a) to typowe zastosowanie Lematu o  $\pi - \lambda$  układach: Niech  $\Pi = \{(-\infty, x]: x \in \mathbb{R}\} \cup \mathbb{R}$  oraz  $\Lambda = \{B \in \mathcal{B}(\mathbb{R}) \colon X^{-1}(B) \in \mathcal{F}\}$ . Jeśli  $\Lambda = \mathcal{B}(\mathbb{R})$ , to X jest zmienną losową. Zakładając (b) wiemy z kolei, że  $\Pi \subset \Lambda$ . Rodzina  $\Pi$  jest  $\pi$ -układem podzbiorów  $\mathbb{R}$  (oczywiste) oraz  $\Lambda \subset \mathcal{B}(\mathbb{R})$  jest  $\lambda$ -układem (wynika to szybko z własności przeciwobrazu). Zatem z Lematu o  $\pi - \lambda$  układach mamy, że  $\sigma(\Pi) = \mathcal{B}(\mathbb{R}) \subset \Lambda \subset \mathcal{B}(\mathbb{R})$ , czyli  $\Lambda = \mathcal{B}(\mathbb{R})$ , co jest równoważne (a).

**A** Jeśli X jest zmienną losową, to  $X^{-1}(\{t\}) = \{\omega \in \Omega \colon X(\omega) = t\} \in \mathcal{F}$ , ale w ogólności ten warunek nie implikuje, że X jest zmienną losową. ♠ A kiedy wystarcza?

- (4.6) 🗱 Rzucamy dwukrotnie monetą. Niech X będzie liczbą otrzymanych orłów. Pokazać, że X jest zmienną losową.
- (4.7) Napis  $\{X \in B\}$  jest skrótem  $\{\omega \in \Omega \colon X(\omega) \in B\}$ . Będziemy również pisali  $\mathbb{P}(X \in B)$  zamiast  $\mathbb{P}(\{X \in B\})$ .
- (4.8)  $\blacksquare$  Powiemy, że funkcja  $f: \mathbb{R} \to \mathbb{R}$  jest borelowska, jeśli jest  $\mathcal{B}(\mathbb{R})$ -mierzalna, tzn.

$$\forall B \in \mathcal{B}(\mathbb{R}) \quad f^{-1}(B) \in \mathcal{B}(\mathbb{R}).$$

A Przeciwobrazy zbiorów otwartych przy przekształceniu ciągłym są otwarte, co oznacza, że wszystkie funkcje ciągłe są borelowskie. Funkcje kawałkami ciągłe również są borelowskie.

- (4.9) **TW.** Jeśli  $X_1, \ldots, X_n$  są zmiennymi losowymi, to  $X_1 + \ldots + X_n$  jest zmienną losową. Szkic dowodu: Należy zauważyć, że  $\{X+Y< t\} = \bigcup_{q\in\mathbb{Q}} \{X< q\} \cap \{q< t-Y\}.$
- (4.10) **TW.** Jeśli  $X: \Omega \to \mathbb{R}$  jest zmienną losową, a  $f: \mathbb{R} \to \mathbb{R}$  jest funkcją borelowską, to  $Y(\omega) := f(X(\omega))$  jest zmienną losowa.

(4.11)  $\blacksquare$  Rozkładem prawdopodobieństwa zmiennej losowej X nazywamy funkcję  $\mathbb{P}_X$  na  $\mathcal{B}(\mathbb{R})$  zadaną przez

$$\mathbb{P}_X(B) = \mathbb{P}(X^{-1}(B)) = \mathbb{P}\left(\{\omega \in \Omega \colon X(\omega) \in B\}\right) = \mathbb{P}(X \in B), \qquad B \in \mathcal{B}(\mathbb{R}).$$

- (4.12)  $\mbox{\ensuremath{\mbox{$\alpha$}}}$  Funkcja  $\mathbb{P}_X$  jest prawdopodobieństwem na  $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ . Zatem  $(\mathbb{R},\mathcal{B}(\mathbb{R}),\mathbb{P}_X)$  jest przestrzenią probabilistyczną.
- (4.13)  $\blacksquare$  Niech X będzie zmienną losową. Funkcję  $F_X : \mathbb{R} \to \mathbb{R}$  określoną wzorem

$$F_X(t) = \mathbb{P}_X((-\infty, t]) = \mathbb{P}(X \le t), \qquad t \in \mathbb{R}$$

nazywamy dystrybuantą zmiennej losowej X.

- (4.14) **TW.** (Własności dystrybuanty)
  - (a)  $F_X$  jest niemalejąca,
  - (b)  $F_X$  jest prawostronnie ciągła, tzn.  $F_X(t+) := \lim_{\varepsilon \to 0+} F_X(t+\varepsilon) = F_X(t)$ ,
  - (c)  $\lim_{t\to-\infty} F_X(t) = 0$  oraz  $\lim_{t\to\infty} F_X(t) = 1$ .

Szkic dowodu: (b) Niech  $\varepsilon_n \downarrow 0$ . Wtedy z ciągłości z góry prawdopodobieństwa  $\mathbb{P}_X$  mamy  $\lim_{n\to\infty} F_X(t+\varepsilon_n) = \lim_{n\to\infty} \mathbb{P}_X((-\infty,t+\varepsilon_n]) = \mathbb{P}_X\left(\bigcap_{n=1}^{\infty}(-\infty,t+\varepsilon_n]\right) = F_X(t)$ . Punkt (c) również dowodzimy z ciągłości prawdopodobieństwa.

(4.15) **TW.** Jeśli funkcja  $F: \mathbb{R} \to \mathbb{R}$  spełnia warunki (a), (b), (c) powyżej, to istnieje zmienna losowa X (np. określona na  $(\Omega, \mathcal{F}, \mathbb{P}) = ((0,1), \mathcal{B}((0,1)), \lambda_1))$ , której F jest dystrybuantą, tzn.  $F = F_X$ . Rozważyć  $X(\omega) := \sup\{t \in \mathbb{R}: F(t) < \omega\}$  (jeśli F ma funkcję odwrotną na (0,1), to  $X(\omega) = F^{-1}(\omega)$ ). Szkic dowodu: Należy zauważyć, że

$$X(\omega) > t$$
 wtedy i tylko wtedy, gdy  $F(t) < \omega$ 

dla dowolnych  $t \in \mathbb{R}$  i  $\omega \in (0,1)$ . Dalej, dla dowolnego  $t \in \mathbb{R}$  mamy

$$F_X(t) = \mathbb{P}(X \le t) = 1 - \mathbb{P}(X > t) = 1 - \mathbb{P}(\{\omega \in \Omega : X(\omega) > t\})$$
  
= 1 - \mathbb{P}(\{\omega \in \Omega : F(t) < \omega\}) = 1 - \mathbb{P}((F(t), 1)) = 1 - (1 - F(t)) = F(t).

- (4.16) **TW.** Dystrybuanta  $F_X$  zmiennej losowej X wyznacza rozkład prawdopodobieństwa  $\mathbb{P}_X$  jednoznacznie, tzn. jeśli  $F_X = F_Y$ , to  $\mathbb{P}_X = \mathbb{P}_Y$ .
- (4.17)  $\blacksquare$  Powiemy, że zmienne losowe X i Y mają ten sam rozkład ( $\textcircled{\bullet} X \stackrel{d}{=} Y$ ), jeśli  $\mathbb{P}_X = \mathbb{P}_Y$ .

**LEM.**  $X \stackrel{d}{=} Y$  wtedy i tylko wtedy, gdy  $F_X = F_Y$ .

lack A Jeśli X=Y, to  $X\stackrel{d}{=}Y$ , ale odwrotna implikacja w ogólności nie jest prawdziwa.

(4.18)

$$\mathbb{P}(X \in D) = 1.$$

Równoważnie, nośnik jest zbiorem punktów wzrostu dystrybuanty zmiennej losowej X, tzn.

$$\operatorname{supp}(X) = \{ t \in \mathbb{R} : \forall \varepsilon > 0 \ F_X(t - \varepsilon) < F_X(t + \varepsilon) \}.$$

- (4.19) Typy rozkładow:
  - (a) Ciąg par  $(x_i, p_i)_i$  nazywamy dyskretnym rozkładem prawdopodobnieństwa, jeśli  $\sum_i p_i = 1, p_i > 0$  oraz  $x_i \neq x_j$ , gdy  $i \neq j$ .

 $\blacksquare$  Zmienna losowa X jest typu dyskretnego jeśli istnieje ciąg  $(x_i)_i$  taki, że  $(x_i, \mathbb{P}(X = x_i))_i$  jest dyskretnym rozkładem prawdopodobnieństwa. Wtedy

$$\mathbb{P}_X(B) = \mathbb{P}(X \in B) = \sum_{i: x_i \in B} \mathbb{P}(X = x_i) \quad \text{oraz} \quad F_X(t) = \sum_{i: x_i \le t} \mathbb{P}(X = x_i).$$

Innymi słowy,  $F_X$  jest funkcją schodkową o skokach w punktach  $x_i$  o wysokości  $\mathbb{P}(X=x_i)$ .

**A** supp $(X) := \{x_i : i = 1, 2, \ldots\}.$ 

(b) Zmienna losowa X ma rozkład <u>typu absolutnie ciągłego</u> (względem miary Lebesgue'a), jeśli istnieje funkcja borelowska  $f_X$  taka, że

$$\forall B \in \mathcal{B}(\mathbb{R}) \quad \mathbb{P}_X(B) = \int_B f_X(x) dx.$$

▲ Po prawej mamy całkę względem miary Lebesgue'a, patrz kolejny temat.

Wtedy  $F_X(t) = \int_{(-\infty,t]} f_X(x) dx$  oraz  $F_X$  jest ciągła,  $F_X' = f_X$  prawie wszędzie, tzn.  $\lambda(\{t \in \mathbb{R} : F_X'(t) \neq f_X(t)\}) = 0$ .

● "Prawie wszędzie", to takie "prawie na pewno", tylko że względem miary Lebesgue'a.

 $\blacksquare$ Funkcję  $f_X$ nazywamy gęstością zmiennej losowej X.

LEM. Własności gestości:

- (i)  $f_X \ge 0$  prawie wszędzie, tzn.  $\lambda(\{t \in \mathbb{R}: f_X(t) < 0\}) = 0$ ,
- (ii)  $\int_{\mathbb{R}} f_X(t)dt = 1$  (całka względem miary Lebesgue'a),
- (iii)  $f_X$  jest wyznaczona jednoznacznie z dokładnością do zbiorów miary Lebesgue 0, tzn. jeśli  $f_1, f_2$  gęstości X, to  $\lambda(\{t \in \mathbb{R} : f_1(t) \neq f_2(t)\}) = 0$ .

 $\mathbf{A} \operatorname{supp}(X) := \overline{\operatorname{Int}\{t \in \mathbb{R} \colon f_X(t) > 0\}}.$ 

- (c) X ma rozkład singularny, jeśli  $F_X$  jest ciągła oraz  $F_X'(t) = 0$  dla prawie wszystkich  $t \in \mathbb{R}$ . Przykłady: funkcja Cantora, https://en.wikipedia.org/wiki/Cantor\_function, znak zapytania Minkowskiego, ?(x), https://en.wikipedia.org/wiki/Minkowski%27s\_question-mark\_function.
- (d) Rozkłady mieszane: rozkłady o dystrybuancie

$$F = \alpha_1 F_d + \alpha_2 F_{ac} + \alpha_3 F_s$$

gdzie  $\alpha_i \geq 0$  oraz  $\alpha_1 + \alpha_2 + \alpha_3 = 1$  oraz  $F_d$  - dystrybuanta rozkładu dyskretnego,  $F_{ac}$  - dystrybuanta rozkładu absolutnie ciągłego,  $F_s$  - dystrybuanta rozkładu singularnego. Dowolna dystrybuanta ma taką (jednoznaczną) reprezentację. Jest to Twierdzenie Lebesgue'a o rozkładzie.

#### <span id="page-10-0"></span>CAŁKA WZGLEDEM MIARY

- Niech  $(\Omega, \mathcal{F})$  będzie przestrzenią mierzalną oraz niech  $\mu$  będzie miarą skończoną na  $\mathcal{F}$  (czyli zakładamy, że  $\mu(\Omega) < \infty, \, \mu(\cdot) \geq 0$  oraz przeliczalną addytywność na sumach rozłącznych zbiorów z  $\mathcal{F}$ ). Funkcje  $\mathcal{F}$ -mierzalne będziemy skrótowo nazywać mierzalnymi.
- Konstrukcja całki względem miary opiera się o bardzo typowe (w teorii miary) podejście zwane komplikacją. Będziemy rozważali całki z coraz bardziej skomplikowanych funkcji.

Mając już jakieś doświadczenia z całką Riemanna, wiemy jakie są pożądane własności całek (np. liniowość, czyli  $\int (\alpha f + \beta g) = \alpha \int f + \beta \int g$ ). Po zapostulowaniu takich własności, definicja całki z ogólnej funkcji opiera się na definicji całki z funkcji najprostszych, czyli indykatorach. Dla  $A \in \mathcal{F}$  definiujemy

$$\int_{\Omega} \mathbb{1}_{A}(\omega)\mu(d\omega) := \mu(A).$$

Równoważnym oznaczeniem na tę całkę jest  $\int_\Omega \mathbbm{1}_A d\mu$ 

• Funkcję  $X \colon \Omega \to \mathbb{R}$  nazywamy prostą, jeśli przyjmuje skończonie wiele wartości, tzn. można ją zapisać w postaci

$$X(\omega) = \sum_{k=1}^{n} x_k \mathbb{1}_{A_k}(\omega), \qquad \omega \in \Omega.$$

Bez straty ogólności możemy założyć, że  $x_k \neq x_i$  dla  $k \neq i$ .

- $\blacktriangleleft$  Tak zdefiniowana funkcja jest mierzalna wtedy i tylko wtedy, gdy  $A_k \in \mathcal{F}, k = 1, \ldots, n$ .
- Całkę względem miary  $\mu$  funkcji prostej X definiujemy następująco: (równoważnie mogliśmy zapostulować skończoną addytywność całki)

$$\int_{\Omega} X d\mu = \sum_{k=1}^{n} x_k \mu(A_k).$$

Żeby podkreślić zmienną względem której całkujemy, będziemy tę calkę oznaczali przez  $\int_{\Omega} X(\omega)\mu(d\omega)$ .

•  $\P$  Kluczowy fakt dla konstrukcji całki z ogólnej funkcji X: Jeśli  $X: \Omega \to [0, \infty)$  oraz X jest mierzalna, to istnieje ciąg mierzalnych funkcji prostych  $(Z_n)_{n\geq 1}$  taki, że  $Z_n(\omega) \uparrow X(\omega)$ , gdy  $n\to\infty$  dla wszystkich  $\omega\in\Omega$ . Taki ciąg nazywamy ciągiem podpierającym X. Łatwo jest go skonstruować: niech np.

$$Z_n(\omega) = \sum_{k=1}^{n2^n} \frac{k-1}{2^n} \mathbb{1}_{\left[\frac{k-1}{2^n}, \frac{k}{2^n}\right)}(X(\omega)) + n \mathbb{1}_{[n,\infty)}(X(\omega)).$$

Każdy  $Z_n$  jest mierzalny z mierzalności X ( ). Z konstrukcji widać, że dla każdej  $\omega$ , ciąg  $(Z_n(\omega))_n$  jest niemalejący. Ponadto, dla ustalonej  $\omega \in \Omega$  oraz n takich, że  $n > X(\omega)$  zachodzi

$$0 \le Z_n(\omega) - X(\omega) \le \frac{1}{2^n},$$

co daje zbieżnosć punktowa.

 $\bullet$  Całkę z dowolnej nieujemnej funkcji mierzalnej X definiujemy jako granicę

$$\int_{\Omega} X d\mu = \lim_{n \to \infty} \int_{\Omega} Z_n d\mu,$$

gdzie ciąg  $Z_n$  jest dowolnym ciągiem funkcji prostych podpierającym X.

• Na pierwszy rzut oka nie widać, że definicja ta jest dobra, bo potencjalnie granica może zależeć od wyboru ciągu funkcji prostych  $(Z_n)_{n\geq 1}$ . Żeby pokazać, że to nie problem rozważmy dwa ciągi podpierające,  $(Z_n^{(1)})_{n\geq 1}$ oraz  $(Z_n^{(2)})_{n\geq 1}$  oraz zauważmy, że  $Z_n^{(1)}(\omega)\uparrow X(\omega)\geq Z_k^{(2)}(\omega)$  dla  $\omega\in\Omega$ . Wynika stąd, że wtedy dla każdego

$$\lim_{n\to\infty} \int_{\Omega} Z_n^{(1)} d\mu \ge \int_{\Omega} Z_k^{(2)} d\mu$$

co po wzięciu granicy  $k \to \infty$  daje nierówność pomiędzy granicami. Nierówność w drugą stronę otrzymujemy tak samo.

- Druga istotną kwestią jest tutaj pytanie czy granica w definicji w ogóle istnieje. Jej istnienie wynika z faktu, że jeśli X i Y są funkcjami prostymi oraz  $0 \le X(\omega) \le Y(\omega)$ , to  $\int_{\Omega} X d\mu \le \int_{\Omega} Y d\mu$  co z kolei łatwo widać z definicji całki dla funkcji prostych (  $\clubsuit$  ). Stąd, ciąg liczbowy  $(\int_{\Omega} Z_n d\mu)_{n \ge 1}$  jest niemalejący, a zatem ma granicę ( być może nieskończoną).
- Całkę względem miary z nieujemnych funkcji mierzalnych można równoważnie zdefiniować poprzez

$$\int_{\Omega} X d\mu := \sup \left\{ \int_{\Omega} Y d\mu \colon Y \le X \text{ oraz } Y \text{ prosta} \right\}.$$

• Jeśli  $X: \Omega \to \mathbb{R}$ , to można ją rozłożyć na różnicę jej części dodatniej i ujemnej:

$$X(\omega) = X^{+}(\omega) - X^{-}(\omega) := \max\{X(\omega), 0\} - \max\{-X(\omega), 0\}$$

- $\blacktriangle X^-$  jest nieujemne.
- Jeśli X jest funkcją mierzalną, to  $X^+$  i  $X^-$  też.
- $\blacksquare$  Całkę względem miary dowolnej funkcji mierzalnej  $X \colon \Omega \to \mathbb{R}$  definujemy wtedy jako

$$\int_{\Omega} X d\mu := \int_{\Omega} X^{+} d\mu - \int_{\Omega} X^{-} d\mu$$

o ile choć jedna z całek  $\int_{\Omega}X^+d\mu$ ,  $\int_{\Omega}X^-d\mu$  jest skończona. W takiej sytuacji powiemy, że całka istnieje

- $\blacksquare$  Jeśli obie te całki są skończone, tzn.  $\int_{\Omega} |X| d\mu < \infty$ , to mówimy, że zmienna losowa  $\overline{X}$  jest <u>całkowalna</u> wzgledem miary  $\mu$ .
- ullet Całka względem miary ma wiele oczekiwanych własności. Poniżej zakładamy, że X i Y są funkcjami mierzalnymi na  $(\Omega, \mathcal{F})$ .
  - (1)  $\int_{\Omega} (X+Y) d\mu = \int_{\Omega} X d\mu + \int_{\Omega} Y d\mu$  (o ile X i Y są całkowalne względem  $\mu$ ), (2)  $\int_{\Omega} cX d\mu = c \int_{\Omega} X d\mu$  dla każdego  $c \in \mathbb{R}$ ,

$$\mu(\{\omega \in \Omega \colon X(\omega) \le Y(\omega)) = \mu(\Omega),$$

to  $\int_{\Omega} X d\mu \leq \int_{\Omega} Y d\mu$  (o ile X i Y są całkowalne względem  $\mu).$ 

- (4)  $\left| \int_{\Omega} X d\mu \right| \leq \int_{\Omega} |X| d\mu$  (o ile X jest całkowalny względem  $\mu$ ).
- (5) Jeśli  $X \geq 0$ , to  $\int_{\Omega_2} \left[ \int_{\Omega_1} X(\omega_1, \omega_2) \mu_1(d\omega_1) \right] \mu_2(d\omega_2) = \int_{\Omega_1} \left[ \int_{\Omega_2} X(\omega_1, \omega_2) \mu_2(d\omega_2) \right] \mu_1(d\omega_1)$ .
- (6) Jeśli  $\mu(\{\omega \in \Omega : X(\omega) \ge 0\}) = \mu(\Omega)$  oraz  $\int_{\Omega} X d\mu = 0$ , to  $\mu(\{\omega \in \Omega : X(\omega) = 0\}) = \mu(\Omega)$ .

Własności najpierw dowodzimy dla funkcji prostych, kiedy zwykle to jest łatwe. Następnie ogólne funkcje mierzalne aproksymujemy funkcjami prostymi.

• Najprostszym przykładem są całki względem miar dyskretnych. Niech  $\delta_a, a \in \mathbb{R}$ , będzie miarą na  $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ zdefiniowaną wzorem  $\delta_a(B) = \mathbb{1}_B(a), B \in \mathcal{B}(\mathbb{R})$ . Jeśli  $(x_i, p_i)$  jest dyskretnym rozkładem prawdopodobieństwa, a  $\mu$  odpowiadającą miarą na  $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ , czyli

$$\mu(B) := \sum_{i} p_i \delta_{x_i}(B), \qquad B \in \mathcal{B}(\mathbb{R}).$$

Wtedy

$$\int_{\mathbb{R}} f(x)\mu(dx) = \sum_{i} p_{i} \int_{\mathbb{R}} f(x)\delta_{x_{i}}(dx) = \sum_{i} p_{i}f(x_{i}).$$

• Drugim najważniejszym przykładem miary względem której będziemy często całkowali jest miara Lebesgue'a  $\lambda$  na  $(\Omega, \mathcal{F}) = (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ . Nie jest to miara skończona  $(\lambda(\mathbb{R}) = \infty)$ , ale jest  $\sigma$ -skończona, tzn.  $\mathbb{R}$  jest przeliczalną sumą zbiorów mierzalnych z których każdy ma skończona miarę (np.  $\mathbb{R} = \bigcup_{n \in \mathbb{Z}} [n, n+1)$ ) co usprawiedliwia wcześniejszą konstrukcję całki dla miary Lebesgue.

Wprowadzimy teraz związek całki względem miary Lebesgue'a z tradycyjną całką Riemanna. Zauważmy, że

$$\int_{[a,b]} 1 \,\lambda(dx) = \lambda([a,b]) = b - a = \int_a^b 1 \, dx,$$

gdzie po prawej stronie mamy zwykłą całkę Riemanna. Prawdziwe jest następujące twierdzenie:

**TW.** Niech  $f: [a, b] \to \mathbb{R}$  będzie funkcją ograniczoną.

(1) Jeśli f jest całkowalna w sensie Riemanna, to f jest całkowalna w sensie Lebesgue'a oraz

$$\int_{[a,b]} f(x)\lambda(dx) = \int_a^b f(x)dx.$$

(2) Funkcja f jest całkowalna w sensie Riemanna wtedy i tylko wtedy, gdy

$$\lambda(\{x: x \text{ jest punktem nieciągłości } f\}) = 0.$$

Z uwagi na równość całek z punktu (1), przyjeło się upraszczać oznaczenie: zamiast  $\lambda(dx)$  będziemy pisali poprostu dx. Ponieważ  $\lambda(\{x\})=0$  do dowolnego  $x\in\mathbb{R}$ , to całki  $\int_{[a,b]}, \int_{(a,b)}, \int_{[a,b)}, \int_{(a,b)}$  są sobie równe oraz mogą być zastąpione przez symbol  $\int_a^b$ . Oznacza to też, że w przypadku miary Lebesgue'a działają zwykłe metody liczenia całek takie jak całkowanie przez podstawienie czy przez części.

• Wiemy już, że jeśli funkcja ograniczona jest całkowalna w sensie Riemanna, to jest też całkowalna w sensie Lebesgue'a. Odwrotne twierdzenie nie jest prawdziwe, tzn. możemy całkować więcej funkcji w sensie Lebesgue'a. Sztandarowym kontrprzykładem jest funkcja Dirichleta zdefiniowana następujaco:

$$f(x) = \mathbb{1}_{\mathbb{Q}}(x) = \begin{cases} 1, & x \in \mathbb{Q}, \\ 0, & x \in \mathbb{R} \setminus \mathbb{Q}. \end{cases}$$

Ponieważ miara Lebesgue pojedynczego punktu wynosi 0 oraz  $\mathbb{Q}$  jest przeliczalny, to  $\mathbb{Q} \in \mathcal{B}(\mathbb{R})$ ,  $\lambda(\mathbb{Q}) = 0$  oraz  $\int_{\mathbb{R}} f d\lambda = 1 \cdot \lambda(\mathbb{Q}) + 0 \cdot \lambda(\mathbb{R} \setminus \mathbb{Q}) = 0$ .

• Jeśli  $\mu = \lambda$ , to  $\mathcal{F}$  jest  $\sigma$ -ciałem Lebesgue'a. Ponieważ  $\mathcal{B}(\mathbb{R}) \subset \mathcal{F}$ , to możemy całkować względem miary Lebesgue'a wszystkie funkcje borelowskie.

<span id="page-12-0"></span>(5.1) Niech  $(\Omega, \mathcal{F}, \mathbb{P})$  będzie przestrzenią probabilistyczną, a X zmienną losową na  $(\Omega, \mathcal{F})$ . Wartością oczekiwaną zmiennej losowej X nazywamy wartość

$$\mathbb{E}[X] = \int_{\Omega} X d\mathbb{P} = \int_{\Omega} X(\omega) \mathbb{P}(d\omega),$$

o ile całka po prawej stronie istnieje.

- (5.2) **TW.** Własności wartości oczekiwanej:
  - (a) Jeśli X i Y są całkowalne, to  $\mathbb{E}[X+Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ .
  - (b)  $\mathbb{E}[cX] = c \mathbb{E}[X] \text{ dla } c \in \mathbb{R},$
  - (c)  $\mathbb{E}[c] = c \text{ dla } c \in \mathbb{R},$
  - (d) Jeśli  $\mathbb{P}(X \geq 0) = 1$ , to  $\mathbb{E}[X] \geq 0$ ,
  - (e) Jeśli  $\mathbb{P}(X \leq Y) = 1 \text{ oraz } \mathbb{E}[X] \text{ i } \mathbb{E}[Y] \text{ istnieja, to } \mathbb{E}[X] \leq \mathbb{E}[Y],$
  - (f) Jeśli  $\mathbb{E}[X]$  istnieje, to  $|\mathbb{E}[X]| \leq \mathbb{E}[|X|]$ ,
  - (g) Jeśli  $\mathbb{P}(X \geq 0) = 1$  oraz  $\mathbb{E}[X] = 0$ , to  $\mathbb{P}(X = 0) = 1$ .
- (5.3) **TW.** (Twierdzenie o zamianie zmiennych) Dla dowolnej funkcji borelowskiej g zachodzi

$$\mathbb{E}[g(X)] = \int_{\Omega} g(X(\omega)) \mathbb{P}(d\omega) = \int_{\mathbb{R}} g(t) \mathbb{P}_X(dt),$$

o ile jedna z całek powyżej istnieje. W szczególności  $\mathbb{E}[X] = \int_{\mathbb{R}} t \, \mathbb{P}_X(dt)$ .

Szkic dowodu: Z uwagi na konstrukcję całki względem miary, wystarczy sprawdzić dla  $g(t) = \mathbbm{1}_A(t)$  dla  $A \in \mathcal{B}(\mathbb{R})$ . Mamy

$$\int_{\Omega} \mathbb{1}_A(X(\omega)) \mathbb{P}(d\omega) = \int_{\Omega} \mathbb{1}_{X^{-1}(A)} \mathbb{P}(d\omega) = \mathbb{P}(X^{-1}(A)) = \mathbb{P}_X(A) = \int_{\mathbb{R}} \mathbb{1}_A(t) \mathbb{P}_X(dt).$$

(5.4) **LEM.** Wartość oczekiwana dla rozkładów dyskretnych. Niech  $\mathbb{P}(X = x_k) = p_k > 0$  oraz  $\sum_k p_k = 1$ . Wtedy

$$\mathbb{E}[g(X)] = \sum_{k} g(x_k) \, p_k.$$

 $X \sim \text{geo}(p)$ , jeśli  $\mathbb{P}(X=k) = p(1-p)^{k-1}$  dla  $k=1,2,\ldots$  Wtedy  $\mathbb{E}[X] = 1/p$ .

(5.5) **LEM.** Wartość oczekiwana dla rozkładów absolutnie ciągłych. Niech  $f_X$  będzie gęstością X. Wtedy

$$\mathbb{E}[g(X)] = \int_{\mathbb{R}} g(t) f_X(t) dt$$

 $X \sim \mathrm{U}([a,b])$ , jeśli  $f_X(t) = \frac{1}{b-a}\mathbbm{1}[a,b](t)$ . Wtedy  $\mathbb{E}[X] = (b+a)/2$ .

(5.6) Wartość oczekiwana dla rozkładów mieszanych. Dwa sposoby:

• Jeśli  $\mathbb{P}(X \ge 0) = 1$ , to  $\mathbb{E}[X] = \int_0^\infty (1 - F_X(t)) dt$ . Szkic dowodu:

$$\int_{[0,\infty)} t \, \mathbb{P}_X(dt) = \int_{[0,\infty)} \int_0^t ds \, \mathbb{P}_X(dt) = \int_{[0,\infty)} \int_0^\infty \mathbb{1}(s < t) ds \, \mathbb{P}_X(dt) = \int_0^\infty \int_{[0,\infty)} \mathbb{1}(s < t) \mathbb{P}_X(dt) \, ds$$
$$= \int_0^\infty \mathbb{P}_X((s,\infty)) ds = \int_0^\infty (1 - F_X(s)) ds.$$

• Rozważamy tylko przypadek, gdy  $F_X$  nie ma składowej singularnej. Niech  $NC(F_X)$  oznacza punkty nieciągłości  $F_X$ , tzn.  $t \in NC(F_X)$  wtedy i tylko wtedy, gdy  $\Delta F_X(t) := F_X(t) - F_X(t-) > 0$ . Wtedy

$$\mathbb{E}[X] = \sum_{t \in NC(F_X)} t \cdot \Delta F_X(t) + \int_{\mathbb{R}} t F_X'(t) dt.$$

 $\mathbf{A} \Delta F_X(t) = \mathbb{P}(X=t).$ 

Zbiór  $NC(F_X)$  jest co najwyżej przeliczalny.

 $oldsymbol{A}$  Wiemy, że jeśli  $\lambda(\{x\in\mathbb{R}:f(x)\neq g(x)\})=0$  (czyli f i g są sobie równe z dokładnością do zbioru miary Lebesgue'a zero), to  $\int_{\mathbb{R}} f(x)dx=\int_{\mathbb{R}} g(x)dx$ . Funkcja  $F_X$  jest nieróżniczkowalna w punktach skoków (i być może innych problematycznych punktach typu 'dziubki'), więc generalnie napis  $F_X'(t)$  może nie mieć sensu dla pewnych  $t\in\mathbb{R}$ . Jednak zbiór takich punktów ma miarę Lebesgue'a zero. Nie musimy się zatem przejmować punktami dla których  $F_X'(t)$  jest niezdefiniowane.

 $\mbox{\bf$ 

$$\mathbb{E}[X] = p \,\mathbb{E}[X_d] + (1-p)\mathbb{E}[X_{ac}],$$

gdzie  $X_d$  jest zmienną losową o dystrybu<br/>ancie  $F_d$ , a  $X_{ac}$  jest zmienną losową o dystrybu<br/>ancie  $F_{ac}$ . Ponadto, mamy

$$\Delta F_X(t) = p\Delta F_d(t) = p\mathbb{P}(X_d = t) \text{ dla } t \in \mathbb{R}$$

oraz

$$F_X'(t) = (1-p)F_{ac}'(t) = (1-p)f_{ac}(t)$$
 dla prawie wszystkich  $t \in \mathbb{R}$ .

$$\bullet \ \, \boldsymbol{\mathfrak{C}}_{\boldsymbol{x}}^{\boldsymbol{g}} \text{ Obliczyć } \mathbb{E}[X], \text{ gdy } F_X(t) = \begin{cases} 0, & t < 0, \\ t, & t \in [0, 1/2), \\ 1, & t \geq 1/2. \end{cases}$$

6. W6 - Wariancja, nierówności i wektory losowe

- <span id="page-13-0"></span>(6.1)  $\blacksquare$  Momentem zwykłym rzędu  $n \in \mathbb{N}$  zmiennej losowej X nazywamy  $m_n := \mathbb{E}[X^n]$ .
  - $\blacksquare$  Momentem centralnym rzędu  $n \in \mathbb{N}$  zmiennej losowej X nazywamy  $\mu_n := \mathbb{E}[(X \mathbb{E}[X])^n]$ .
  - $\blacksquare$  Moment centralny rzędu 2 nazywamy wariancją. o Var[X].
  - $\blacksquare$  Odchyleniem standardowym zmiennej losowej X nazywamy  $\sigma_X := \sqrt{\operatorname{Var}[X]}$ .
- (6.2) **TW.** Własności wariancji:
  - (a)  $Var[X] = \mathbb{E}[X^2] \mathbb{E}[X]^2$ ,
  - (b)  $Var[X] \geq 0$ ,
  - (c)  $\operatorname{Var}[X] = 0 \iff \operatorname{rozkład} X$  jest jednopunktowy, tzn.  $\exists c \in \mathbb{R}$  takie, że  $\mathbb{P}(X = c) = 1$ ,
  - (d)  $Var[aX + b] = a^2 Var[X],$
  - (e)  $\operatorname{Var}[X] = \inf_{a \in \mathbb{R}} \mathbb{E}[(X a)^2].$

(6.3) **TW.** (Nierówność Cauchy'ego-Schwarza) Jeśli  $\mathbb{E}[X^2], \mathbb{E}[Y^2] < \infty$ , to

$$|\mathbb{E}[XY]| \leq \sqrt{\mathbb{E}[X^2]\mathbb{E}[Y^2]}.$$

Szkic dowodu: Dla dowolnego  $t \in \mathbb{R}$  mamy  $\mathbb{E}[(tX+Y)^2] \geq 0$ , rozpisać, przekształcić  $\Delta \leq 0$ .

(6.4) **TW.** (Nierówność Jensena) Jeśli g jest funkcją wypukłą, to

$$g(\mathbb{E}[X]) \le \mathbb{E}[g(X)].$$

Szkic dowodu: Z definicji wypukłości funkcji g mamy

$$\forall x \in \mathbb{R} \ \forall x_0 \in \mathbb{R} \ \exists m(x_0) \qquad g(x) \ge g(x_0) + m(x_0)(x - x_0).$$

Wziąć x = X,  $x_0 = \mathbb{E}[X]$  oraz obłożyć obie strony nierówności wartością oczekiwaną.

(6.5) **TW.** (Nierówność Markowa) Jeśli  $\mathbb{P}(X \geq 0) = 1$  oraz  $\mathbb{E}[X] < \infty$ , to dla każdego  $\varepsilon > 0$ 

$$\mathbb{P}(X \ge \varepsilon) \le \frac{\mathbb{E}[X]}{\varepsilon}.$$

Szkic dowodu:  $\varepsilon \mathbb{1}_{X(\omega) \geq \varepsilon} \leq X(\omega)$ .

(6.6) **TW.** (Nierówność Czebyszewa) Jeśli  $\mathbb{E}[X^2] < \infty$ , to dla każdego  $\varepsilon > 0$ 

$$\mathbb{P}(|X - \mathbb{E}[X]| \ge \varepsilon) \le \frac{\operatorname{Var}[X]}{\varepsilon^2}.$$

Szkic dowodu: szybki wniosek z Nierówności Markowa.

- (6.7) **LEM.** (Reguła  $3\sigma$ ) Jeśli  $\mathbb{E}[X^2] < \infty$ , to  $\mathbb{P}(|X \mathbb{E}[X]| \ge 3\sigma_X) \le 1/9$ . W szczególności, jeśli  $X \sim N(0,1)$ , to  $\sigma_X = 1$  oraz  $\mathbb{P}(|X \mathbb{E}[X]| \ge 3\sigma_X) \approx 0.0027$ .
- (6.8) Niech  $(\Omega, \mathcal{F})$  będzie przestrzenią mierzalną. Funkcję  $\underline{X} \colon \Omega \to \mathbb{R}^n$  nazywamy wektorem losowym, jeśli jest ona  $\mathcal{F}$ -mierzalna, tzn.

$$\forall B \in \mathcal{B}(\mathbb{R}^n) \quad \underline{X}^{-1}(B) := \{ \omega \in \Omega \colon \underline{X}(\omega) \in B \} \in \mathcal{F}.$$

**E** Rozkładem prawdopodobieństwa wektora <u>X</u> nazywamy funkcję

$$\mathbb{P}_X(B) := \mathbb{P}(\underline{X} \in B), \qquad B \in \mathcal{B}(\mathbb{R}^n).$$

 $\blacksquare$  <u>Dystrybuantą wektora losowego</u>  $\underline{X}=(X_1,\ldots,X_n)$  nazywamy funkcję  $F_{\underline{X}}\colon\mathbb{R}^n\to[0,1]$  zdefiniowaną wzorem

$$F_{\underline{X}}(\underline{t}) = \mathbb{P}\left(\left\{\omega \in \Omega \colon X_i(\omega) \le t_i \text{ dla } i = 1, \dots, n\right\}\right),$$

gdzie  $\underline{t} = (t_1, \dots, t_n) \in \mathbb{R}^n$ .

**TW.** Podobnie jak w przypadku jednowymiarowym, dystrybuanta  $F_{\underline{X}}$  jednoznacznie wyznacza rozkład prawdopodobieństwa  $\mathbb{P}_X$ .

- ullet Z lenistwa, będziemy pisali  $\{X \in A, Y \in B\}$  zamiast  $\{X \in A\} \cap \{Y \in B\} = \{\omega \in \Omega \colon X(\omega) \in A \land Y(\omega) \in B\}$ .
- $\blacksquare$  W szczególności dystrybuantą wektora losowego (X,Y) nazywamy funkcję

$$\mathbb{R}^2\ni (s,t)\mapsto F_{(X,Y)}(s,t):=\mathbb{P}(X\leq s,Y\leq t)=\mathbb{P}_{(X,Y)}((-\infty,s]\times (-\infty,t]).$$

- (6.9) **TW.** Własności dystrybuanty dla n=2.
  - (a)  $F_{(X,Y)}$  jest prawostronnie ciągła po współrzędnych,
  - (b)  $\forall a_1 \leq b_1 \text{ oraz } \forall a_2 \leq b_2$ ,

$$\Delta_{(a,b)}^{(2)}F_{(X,Y)} := F_{(X,Y)}(b_1,b_2) - F_{(X,Y)}(a_1,b_2) - F_{(X,Y)}(b_1,a_2) + F_{(X,Y)}(a_1,a_2) \ge 0.$$

Ponadto 
$$\Delta_{(a,b)}^{(2)} F_{(X,Y)} = \mathbb{P}_{(X,Y)}((a_1,b_1] \times (a_2,b_2]).$$

- (c)  $\lim_{(s,t)\to(\infty,\infty)} F_{(X,Y)}(s,t) = 1$ ,
- (d) Dla każdego  $s,t\in\mathbb{R}$  zachodzi  $\lim_{x\to-\infty}F_{(X,Y)}(x,t)=0=\lim_{x\to-\infty}F_{(X,Y)}(s,x)$

lacktriangle Warunek (b) dla ogólnego n można rozumieć w następujący sposób: niech  $\mathbb{P}_{\underline{X}}$  będzie miarą wyznaczoną przez dystrybuantę  $F_X$ , wtedy wymagamy, by

$$\mathbb{P}_{\underline{X}}((a_1, b_1] \times \ldots \times (a_n, b_n]) \ge 0.$$

dla dowolnych  $\underline{a}, \underline{b} \in \mathbb{R}^n$  takich, że  $a_i < b_i$ , i = 1, ..., n. Lewą stronę powyżej oznaczmy przez  $\Delta_{(\underline{a},\underline{b})}^{(n)} F$ . Można napisać ten warunek jawnie w terminach  $F_{\underline{X}}$ . Definiujemy najpierw operatory różnicowe: dla k = 1, ..., n oraz a < b niech

$$\Delta_{(a,b)}^{(k)} F(\underline{x}) := F(x_1, \dots, x_{k-1}, b, x_{k+1}, \dots, x_n) - F(x_1, \dots, x_{k-1}, a, x_{k+1}, \dots, x_n).$$

Wtedy

$$\mathbb{P}_{\underline{X}}((a_1,b_1]\times\ldots\times(a_n,b_n])=\Delta_{(a_1,b_1)}^{(1)}\ldots\Delta_{(a_n,b_n)}^{(n)}F_{\underline{X}}(\underline{x})=:\Delta_{(\underline{a},\underline{b})}^{(n)}F_{\underline{X}}(\underline{x})$$

(6.10)  $\overset{\bullet}{\mathbf{x}}$  Miary produktowe. Niech  $F_1, \ldots, F_n$  będą jednowymiarowymi dystrybuantami. Wtedy

$$F(t_1,\ldots,t_n):=\prod_{k=1}^n F_k(t_k)$$

jest n-wymiarową dystrybuantą oraz  $\Delta_{(a,b)}^{(n)} F = \prod_{k=1}^n \left( F_k(b_k) - F_k(a_k) \right)$  (  $\clubsuit$  ).

- (6.11)  $\triangle$  Podobnie jak w przypadku rozkładów zmiennych losowych, definiujemy nośnik rozkładu wektora. Niech  $X: \Omega \to \mathbb{R}^n$ .
  - Nośnikiem (rozkładu) wektora losowego  $\underline{X}$  ( $\bigcirc$  supp( $\underline{X}$ )) nazywamy najmniejszy taki zbiór domknięty  $D \subset \mathbb{R}^n$  dla którego

$$\mathbb{P}(\underline{X} \in D) = 1.$$

#### 7. W7 - Wektory Losowe Ciąg dalszy

- <span id="page-15-0"></span>(7.1) Przykłady rozkładów wielowymiarowych.
  - (a) Wielowymiarowe rozkłady dyskretne. Ciąg par  $((\underline{x}^{(k)}, p_k))_k$  nazywamy  $\underline{n}$ -wymiarowym dyskretnym rozkładem prawdopodobieństwa, jesli  $\underline{x}^{(k)} \in \mathbb{R}^n$ ,  $\underline{x}^{(k)} \neq \underline{x}^{(j)}$  dla  $k \neq j$ ,  $p_k > 0$  oraz  $\sum_k p_k = 1$ .

**A** Jeśli  $\mathbb{P}(\underline{X} = \underline{x}^{(k)}) = p_k$  dla wszystkich k, to  $\operatorname{supp}(\underline{X}) := \{\underline{x}^{(k)} : k = 1, 2, \ldots\}.$ 

Rozkład wielomianowy. Przeprowadzamy n niezależnych prób eksperymentu, przy czym każda próba może skończyć się jednym z  $r \in \mathbb{N}$  rodzajów sukcesów (i-ty rodzaj sukcesu zachodzi z p-stwem  $p_i$ ) lub porażką. Niech  $\underline{X} = (X_1, \dots, X_r)$ , gdzie  $X_i$  jest zmienną losową reprezentującą liczbę sukcesów i-tego rodzaju,  $i = 1, \dots, r$ . Wtedy

$$\mathbb{P}(X_1 = k_1, \dots, X_r = k_r) = \binom{n}{k_1, \dots, k_r} p_1^{k_1} \dots p_r^{k_r} (1 - \sum_{i=1}^r p_i)^{n - \sum_{i=1}^r k_i}, \qquad k_i \ge 0, \ \sum_{i=1}^r k_i \le n,$$

gdzie

$$\binom{n}{k_1, \dots, k_r} := \frac{n!}{k_1! \dots k_n! (n - \sum_{i=1}^r k_i)!}.$$

 $\operatorname{supp}(\underline{X}) = \{(k_1, \dots, k_r) \in (\mathbb{N} \cup \{0\})^r \colon \sum_{i=1}^r k_i \le n\}.$ 

 $\bullet$   $X \sim m_r(n, p)$ .

(b) Miary absolutnie ciągłe względem miary Lebesgue  $\lambda_n$ . Jeśli  $f: \mathbb{R}^n \to \mathbb{R}$  jest borelowska, prawie wszędzie nieujemna oraz całkuje się (względem  $\lambda_n$ ) do 1, to

$$F(s_1,\ldots,s_n) = \int_{(-\infty,s_1]} \ldots \int_{(-\infty,s_n]} f(t_1,\ldots,t_n) dt_n \ldots dt_1$$

jest n-wymiarową dystrybuantą oraz  $\Delta_{(a,\underline{b})}^{(n)}F=\int_{(a_1,b_1]}\ldots\int_{(a_n,b_n]}f(\underline{t})dt_n\ldots dt_1$  (  $\clubsuit$  ).

**A** Jeśli wektor losowy  $\underline{X}$  ma gęstość  $f_{\underline{X}}$ , to supp $(\underline{X}) := \inf\{\underline{t} \in \mathbb{R}^n : f_{\underline{X}}(\underline{t}) > 0\}.$ 

Wektor losowy  $(X_1, \ldots, X_n)$  ma wielowymiarowy rozkład normalny  $N_n(\underline{\mu}, \Sigma)$ , z parametrami  $\mu \in \mathbb{R}^n$  i  $\Sigma \in \operatorname{Sym}_+(n)$ , jeśli

$$f_{\underline{X}}(\underline{x}) = \frac{1}{(\sqrt{2\pi})^n \sqrt{\det \Sigma}} e^{-\frac{1}{2}(\underline{x} - \underline{\mu})^\top \cdot \Sigma^{-1} \cdot (\underline{x} - \underline{\mu})}, \qquad \underline{x} \in \mathbb{R}^n.$$

 $\triangle$  Sym<sub>+</sub>(n) oznacza zbiór macierzy symetrycznych dodatnio określonych wymiaru  $n \times n$ .

- (7.2) Niech  $\underline{X}: \Omega \to \mathbb{R}^n$  będzie wektorem losowym. Podwektory wektora  $\underline{X}$ , tzn.  $(X_{i_1}, \dots, X_{i_k})$  dla k < n również są wektorami losowymi, a ich rozkłady nazywamy rozkładami brzegowymi wektora  $\underline{X}$ .
  - Wektor  $\underline{X} = (X_1, X_2, X_3)$  ma 6 podwektorów  $(X_1, X_2), (X_1, X_3), (X_2, X_3), (X_1), (X_2), (X_3).$
- (7.3) **LEM.** Jeśli  $F_{\underline{X}}$  jest dystrybuantą wektora  $\underline{X} = (X_1, \dots, X_n)$ , to

$$F_{\underline{X}^{(-j)}}(t_1,\ldots,t_{j-1},t_{j+1},\ldots,t_n) = \lim_{t_i \to \infty} F_{\underline{X}}(t_1,\ldots,t_{j-1},t_j,t_{j+1},\ldots,t_n).$$

jest dystrybuantą wektora  $\underline{X}^{(-j)} = (X_1, \dots, X_{j-1}, X_{j+1}, \dots, X_n).$ 

Szkic dowodu: Wykorzystujemy ciągłość z góry prawdopodobieństwa, tak samo jak w przypadku własności dystrybuanty jednowymiarowej.

(7.4) **LEM.** Jeśli wektor  $\underline{X} = (X_1, \dots, X_n)$  ma gęstość  $f_{\underline{X}}$ , to dowolny rozkład brzegowy również posiada gęstość. Ponadto

$$f_{\underline{X}^{(-j)}}(t_1,\ldots,t_{j-1},t_{j+1},\ldots,t_n) = \int_{\mathbb{R}} f_{\underline{X}}(t_1,\ldots,t_{j-1},t_j,t_{j+1},\ldots,t_n) dt_j.$$

jest gęstością wektora  $\underline{X}^{(-j)} = (X_1, \dots, X_{j-1}, X_{j+1}, \dots, X_n).$ 

(7.5) **LEM.** Jeśli wektor  $\underline{X} = (X_1, \dots, X_n)$  ma rozkład dyskretny, to dowolny rozkład brzegowy również jest dyskretny. Ponadto

$$\mathbb{P}(\underline{X}^{(-j)} = \underline{t}^{(-j)}) = \sum_{t,i} \mathbb{P}(\underline{X} = \underline{t}),$$

gdzie jak wcześniej  $\underline{X}^{(-j)} = (X_1, \dots, X_{j-1}, X_{j+1}, \dots, X_n)$  oraz  $\underline{t}^{(-j)} = (t_1, \dots, t_{j-1}, t_{j+1}, \dots, t_n)$ .

Rozkład wielomianowy dla  $r=2, (X,Y) \sim m_2(n,(p_1,p_2))$ . Mamy

$$\mathbb{P}(X_1 = k_1, X_2 = k_2) = \frac{n!}{k_1! k_2! (n - k_1 - k_2)!} p_1^{k_1} p_2^{k_2} (1 - p_1 - p_2)^{n - k_1 - k_2}, \qquad k_1, k_2 \ge 0, \ k_1 + k_2 \le n.$$

Wtedy  $\mathbb{P}(X_1 = k_1) = \sum_{k_2=0}^{n-k_1} \mathbb{P}(X_1 = k_1, X_2 = k_2) = \binom{n}{k_1} p_1^{k_1} (1-p_1)^{n-k_1}$  dla  $k_1 = 0, \dots, n$ , czyli  $X_1$  ma rozkład dwumianowy b $(n, p_1)$ .

(7.6)  $\blacksquare$  Zmienne losowe  $X_1, \ldots, X_n$  (określone na tej samej przestrzeni  $(\Omega, \mathcal{F})$ ) są <u>niezależne</u>, jeśli

$$\forall B_i \in \mathcal{B}(\mathbb{R}), i = 1, \dots, n, \qquad \mathbb{P}(X_1 \in B_1, \dots, X_n \in B_n) = \mathbb{P}(X_1 \in B_1) \dots \mathbb{P}(X_n \in B_n).$$

f A Tak naprawdę powinniśmy mówić o  $\Bbb P$ -niezależności, ponieważ własność ta zależy od prawdopodobieństwa  $\Bbb P$  na  $(\Omega, \mathcal F)$ . Może zdarzyć się tak, że X i Y są  $\Bbb P$ -niezależne ale już nie  $\H P$ -niezależne, gdzie  $\H P$  jest innym prawdopodobieństwem na  $(\Omega, \mathcal F)$ . Zwykle jednak mamy jedno prawdopodobieństwo i dlatego mówienie o samej niezależności nie wprowadza zamieszania.

(7.7) **LEM.** Jeśli zmienne losowe  $X_1, \ldots, X_n$  są niezależne oraz  $f_i$  są funkcjami borelowskimi dla  $i = 1, \ldots, n$ , to zmienne losowe  $f_1(X_1), \ldots, f_n(X_n)$  również są niezależne.

**LEM.** Jeśli zmienne losowe  $X_1, \ldots, X_n$  są niezależne oraz oraz  $\phi \colon \mathbb{R}^k \to \mathbb{R}$  i  $\psi \colon \mathbb{R}^{n-k} \to \mathbb{R}$  są borelowskie, to zmienne losowe  $\phi(X_1, \ldots, X_k)$  oraz  $\psi(X_{k+1}, \ldots, X_n)$  są niezależne.

(7.8) **TW.** Zmienne losowe  $X_1, \ldots, X_n$  są niezależne wtedy i tylko wtedy, gdy

$$\forall (t_1, \dots, t_n) \in \mathbb{R}^n \qquad F_{\underline{X}}(t_1, \dots, t_n) = F_{X_1}(t_1) \dots F_{X_n}(t_n).$$

Szkic dowodu: W prawą stronę oczywiste. W lewą: trzeba się dobrze zastanowić, by zrozumieć, że to wynika z faktu, że dystrybuanta wyznacza rozkład jednoznacznie.

(7.9) **LEM.** Niech  $\underline{X} = (X_1, \dots, X_n)$  ma rozkład dyskretny. Zmienne losowe  $X_1, \dots, X_n$  są niezależne wtedy i tylko wtedy, gdy

$$\forall (k_1,\ldots,k_n) \in \operatorname{supp}(\underline{X}) \qquad \mathbb{P}(X_1 = k_1,\ldots,X_n = k_n) = \mathbb{P}(X_1 = k_1)\ldots\mathbb{P}(X_n = k_n).$$

(7.10) **LEM.** Niech  $\underline{X} = (X_1, \dots, X_n)$  ma rozkład o gęstości  $f_{\underline{X}}$ . Zmienne losowe  $X_1, \dots, X_n$  są niezależne wtedy i tylko wtedy, gdy

$$\forall (t_1,\ldots,t_n) \in \mathbb{R}^n \qquad f_{\underline{X}}(t_1,\ldots,t_n) = f_{X_1}(t_1)\ldots f_{X_n}(t_n).$$

 $\mathbf{A}$  Jeśli istnieją funkcje  $g_1, \ldots, g_n$  (niekoniecznie gęstości) takie, że dla dowolnego  $(t_1, \ldots, t_n) \in \mathbb{R}^n$  gęstość  $f_{\underline{X}}$  się faktoryzuje

$$f_X(t_1, \dots, t_n) = g_1(t_1) \dots g_n(t_n),$$

to zmienne losowe  $X_1, \ldots, X_n$  są niezależne.

(7.11)  $(X_1, \dots, X_n)$  Niech zmienne losowe  $X_1, \dots, X_n$  będą niezależne oraz zdefiniujmy  $M = \max\{X_1, \dots, X_n\}$  oraz  $m = \min\{X_1, \dots, X_n\}$ . Wtedy

$$F_M(t) = \prod_{k=1}^n F_{X_k}(t), \qquad F_m(t) = 1 - \prod_{k=1}^n (1 - F_{X_k}(t)).$$

- (7.12) Powiemy, że zmienne losowe  $X_1, \ldots, X_n$  są <u>i.i.d.</u> (independent and identically distributed), jeśli są niezależne oraz mają takie same rozkłady.
- (7.13)  $(x_1, \dots, x_n)$  będą zmiennymi i.i.d. o dystrybuancie F. Niech  $X_{k:n}(\omega)$  będzie k-tą co do wielkości wartością spośród  $X_1(\omega), \dots, X_n(\omega)$ .  $[X_{k:n}]$  jest tzw. k-tą statystyką pozycyjną.] Zdefiniujmy  $A_j(t)$  zdarzenie, że dokładnie j spośród X'ów jest mniejszych lub równych t. Wtedy

$$\mathbb{P}(X_{k:n} \le t) = \mathbb{P}(\bigcup_{j=k}^{n} A_j(t)) = \sum_{j=k}^{n} \mathbb{P}(A_j(t)) = \sum_{j=k}^{n} \binom{n}{j} F(t)^j (1 - F(t))^{n-j}.$$

(7.14) **LEM.** Jeśli  $\operatorname{supp}(\underline{X}) \neq \operatorname{supp}(X_1) \times \ldots \times \operatorname{supp}(X_n)$ , to zmienne losowe  $X_1, \ldots, X_n$  nie są niezależne. Szkic dowodu: Zawsze mamy  $\operatorname{supp}(\underline{X}) \subset \operatorname{supp}(X_1) \times \ldots \times \operatorname{supp}(X_n)$ . Jeśli  $\operatorname{supp}(\underline{X}) \neq \operatorname{supp}(X_1) \times \ldots \times \operatorname{supp}(X_n)$ , to istnieja niepuste zbiory  $B_1, \ldots, B_n \in \mathcal{B}(\mathbb{R})$  takie, że

$$B_1 \times \ldots \times B_n \subset (\operatorname{supp}(X_1) \times \ldots \times \operatorname{supp}(X_n)) \setminus \operatorname{supp}(\underline{X})$$

oraz  $\mathbb{P}(X_i \in B_i) > 0$  dla  $i = 1, \dots, n$  (ponieważ  $B_i \subset \text{supp}(X_i)$ ). Ponieważ

$$(B_1 \times \ldots \times B_n) \cap \operatorname{supp}(\underline{X}) = \emptyset,$$

to mamy  $\mathbb{P}(\underline{X} \in B_1 \times ... \times B_n) = 0$ , co przeczy niezależności.

#### 8. W8 - Wektory Losowe Dalszy Ciąg Dalszy

- <span id="page-17-0"></span>(8.1) Transformacje wektorów losowych.
  - $\bullet$  Dodawanie zmiennych losowych. Niech (X,Y) będzie wektorem losowym o znanym rozkładzie oraz zdefiniujmy Z = X + Y.
    - (a) ♠ Nośnik zmiennej losowej Z jest zadany przez

$$\operatorname{supp}(Z) = \{x + y \colon (x, y) \in \operatorname{supp}(X, Y)\}.$$

W szczególności, jeśli X i Y są niezależne, to  $supp(X,Y) = supp(X) \times supp(Y)$ , a więc wtedy

$$\operatorname{supp}(Z) = \{x + y \colon x \in \operatorname{supp}(X), y \in \operatorname{supp}(Y)\} =: \operatorname{supp}(X) + \operatorname{supp}(Y).$$

(b) Jeśli (X,Y) ma rozkład dyskretny, to Z ma rozkład dyskretny oraz

$$\mathbb{P}(Z=z_k) = \sum_{j} \mathbb{P}(X=x_j, Y=z_k - x_j).$$

 $\mathbf{x}_{\mathbf{x}}^{\mathbf{x}}$  Niech  $(X,Y) \sim \mathrm{m}_2(n,(p_1,p_2))$ . Wtedy

$$\mathbb{P}(Z=k) = \sum_{l=0}^{k} \mathbb{P}(X=l, Y=k-l) = \binom{n}{k} (p_1 + p_2)^k (1 - p_1 - p_2)^{n-k}, \qquad k = 0, 1, \dots, n,$$

czyli  $Z \sim b(n, p_1 + p_2)$ .

Niech  $X \sim \mathrm{b}(n_1,p)$  oraz  $Y \sim \mathrm{b}(n_2,p), X$  i Y niezależne. Wtedy

$$\mathbb{P}(Z=k) = \sum_{l=\max\{0,k-n_2\}}^{\min\{n_1,k\}} \mathbb{P}(X=l)\mathbb{P}(Y=k-l) = \binom{n_1+n_2}{k} p^k (1-p)^{n_1+n_2-k}, \qquad k=0,1,\ldots,n_1+n_2,$$

czyli  $Z \sim b(n_1 + n_2, p)$ .

Inaczej:  $X \stackrel{d}{=} \sum_{k=1}^{n_1} I_k$ , gdzie  $(I_k)_k$  są i.i.d. z rozkładu b(1,p). (c) Ogólnie, dystrybuanta zmiennej losowej Z = X + Y dana jest przez

$$F_Z(t) = \mathbb{P}(X + Y \le t) = \mathbb{P}_{(X,Y)}(\{(x,y) \in \mathbb{R}^2 : x + y \le t\}) = \iint_{\{(x,y) \in \mathbb{R}^2 : x + y \le t\}} \mathbb{P}_{(X,Y)}(dx, dy).$$

**A** Zgodnie z wprowadzonymi wcześniej oznaczeniami powinniśmy raczej pisać  $\mathbb{P}_{(X,Y)}(d(x,y))$ , a nie  $\mathbb{P}_{(X,Y)}(dx,dy)$ , ale d(x,y) dziwnie wygląda.

Jeśli X i Y są niezależne, to  $\mathbb{P}_{(X,Y)}(dx,dy) = \mathbb{P}_X(dx)\mathbb{P}_Y(dy)$  oraz możemy rozważać całki iterowane:

$$F_Z(t) = \int_{-\infty}^{\infty} \int_{-\infty}^{t-y} \mathbb{P}_X(dx) \mathbb{P}_Y(dy) = \int_{-\infty}^{\infty} F_X(t-y) \mathbb{P}_Y(dy)$$
$$= \int_{-\infty}^{\infty} \int_{-\infty}^{t-x} \mathbb{P}_Y(dy) \mathbb{P}_X(dx) = \int_{-\infty}^{\infty} F_Y(t-x) \mathbb{P}_X(dx)$$

(a) Jeśli (X,Y) ma gęstość, to Z również ma gęstość oraz

$$f_Z(t) = \int_{\mathbb{R}} f_{(X,Y)}(t-y,y) dy = \int_{\mathbb{R}} f_{(X,Y)}(x,t-x) dx.$$

Szkic dowodu: Ponieważ (X,Y) ma gęstość, to  $\mathbb{P}_{(X,Y)}(dx,dy)=f_{(X,Y)}(x,y)dx\,dy$ . Zatem,

$$F_{Z}(t) = \iint_{\{(x,y) \in \mathbb{R}^{2} : x+y \le t\}} f_{(X,Y)}(x,y) dx dy = \int_{-\infty}^{\infty} \int_{-\infty}^{t-y} f_{(X,Y)}(x,y) dx dy$$
$$= \int_{-\infty}^{\infty} \int_{-\infty}^{t} f_{(X,Y)}(z-y,y) dz dy = \int_{-\infty}^{t} \int_{-\infty}^{\infty} f_{(X,Y)}(z-y,y) dy dz = \int_{-\infty}^{t} f_{Z}(z) dz.$$

Inaczej: Różniczkujemy pod znakiem całki po prawej stronie równości:

$$F_Z(t) = \int_{-\infty}^{\infty} \int_{-\infty}^{t-y} f_{(X,Y)}(x,y) dx \, dy.$$

Korzystamy z własności typu:

 $\triangle$  Jeśli funkcja h jest ciągła w punkcie t, to

$$\frac{d}{dt} \int_{t}^{t} h(s)ds = h(t),$$

gdzie \* jest dowolne, byleby nie zależało od t.

lacktriangle Jeśli funkcja  $H: \mathbb{R}^2 \to \mathbb{R}$  jest ładna (np.  $\left| \frac{d}{dx} H(x,y) \right| \leq g(y)$  dla pewnej całkowalnej funkcji g), to

$$\frac{d}{dx} \int_{\mathbb{R}} H(x, y) dy = \int_{\mathbb{R}} \frac{d}{dx} H(x, y) dy.$$

Niech  $X \sim G(p_1, a)$  oraz  $Y \sim G(p_2, a)$  i niech X i Y będą niezależne. Wtedy dla t > 0,

$$f_Z(t) = \int_{\mathbb{R}} f_X(t-y) f_Y(y) dy = \frac{a^{p_1 + p_2} e^{-at}}{\Gamma(p_1) \Gamma(p_2)} \int_0^t y^{p_2 - 1} (t-y)^{p_1 - 1} dy = \frac{a^{p_1 + p_2}}{\Gamma(p_1 + p_2)} t^{p_1 + p_2 - 1} e^{-at},$$

czyli  $Z \sim G(p_1 + p_2, a)$ .

• Dzielenie zmiennych losowych. Niech (X,Y) ma gęstość. Wtedy  $\mathbb{P}(Y=0)=0$  oraz  $Q=\frac{X}{Y}$  jest dobrze zdefiniowaną zmienną losową. Wtedy

$$F_{Q}(t) = \mathbb{P}(X \le tY, Y > 0) + \mathbb{P}(X \ge tY, Y < 0)$$
  
=  $\int_{0}^{\infty} \int_{-\infty}^{ty} f_{(X,Y)}(x, y) dx dy + \int_{-\infty}^{0} \int_{ty}^{\infty} f_{(X,Y)}(x, y) dx dy.$ 

Różniczkujac otrzymujemy

$$f_Q(t) = \int_{\mathbb{R}} |y| f_{(X,Y)}(ty,y) dy.$$

Niech X, Y będa i.i.d. z rozkładu N(0, 1). Wtedy

$$f_{\frac{X}{Y}}(t) = \frac{1}{\pi(1+t^2)}, \quad t \in \mathbb{R},$$

czyli  $\frac{X}{Y} \sim C(1)$ .

(8.2)  $\blacksquare$  Wartością oczekiwaną wektora losowego  $\underline{X} = (X_1, \dots, X_n)$  nazywamy wektor

$$\mathbb{E}[\underline{X}] = (\mathbb{E}[X_1], \dots, \mathbb{E}[X_n]),$$

o ile wszystkie  $\mathbb{E}[X_i]$ ,  $i = 1, \ldots, n$ , istnieją.

(8.3) **LEM.** Jeśli  $\underline{X}$  ma gęstość oraz  $\phi \colon \mathbb{R}^n \to \mathbb{R}^k$  jest borelowska, to

$$\mathbb{E}[\phi(\underline{X})] = \int \cdots \int_{\mathbb{R}^n} \phi(\underline{t}) f_{\underline{X}}(\underline{t}) dt_1 \dots dt_n.$$

W szczególności, jeśli  $g \colon \mathbb{R}^2 \to \mathbb{R}$ , to

$$\mathbb{E}[g(X,Y)] = \iint\limits_{\mathbb{R}^2} g(x,y) f_{(X,Y)}(x,y) dx \, dy.$$

(8.4) **TW.** Jeśli  $X_1, \ldots, X_n$  są niezależnymi zmiennymi losowymi, to

$$\mathbb{E}[X_1 \dots X_n] = \mathbb{E}[X_1] \dots \mathbb{E}[X_n],$$

o ile  $\mathbb{E}[X_i] < \infty, i = 1, \dots, n$ .

Szkic dowodu: Wystarczy udowodnić dla n=2, dla dowolnego n indukcja. Równość zachodzi dla zmiennych indykatorowych, tzn. gdy  $X_1=\mathbbm{1}_A, X_2=\mathbbm{1}_B,$  gdzie  $A,B\in\mathcal{F}$  są zdarzeniami niezależnymi. Z liniowości wartości oczekiwanej, mamy tezę, gdy  $X_1$  i  $X_2$  są funkcjami prostymi. Dowolne nieujemne  $X_1$  i  $X_2$  aproksymujemy funkcjami prostymi. Znakowane  $X_1$  i  $X_2$  rozkładamy na części dodatnie i ujemne.

A Twierdzenie w odwrotną stronę nie zachodzi.

(8.5) Niech X, Y beda zmiennymi losowymi na tej samej przestrzeni takimi, że  $\mathbb{E}[X^2], \mathbb{E}[Y^2] < \infty$ . Kowariancją wektora (X,Y) nazywamy wielkość

$$Cov[X, Y] = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])].$$

- (8.6) **TW.** Własności kowariancji.
  - (a) Cov[X, Y] = Cov[Y, X],
  - (b) Cov[X, X] = Var[X],
  - (c)  $\operatorname{Cov}[X, Y] = \mathbb{E}[XY] \mathbb{E}[X]\mathbb{E}[Y],$
  - (d)  $|Cov[X, Y]| \le \sqrt{Var[X]Var[Y]}$ ,
  - (e) Jeśli X i Y są niezależne, to Cov[X, Y] = 0,
  - (f)  $\operatorname{Cov}[aX + bY + c, dX + eY + f] = \operatorname{ad} \operatorname{Var}[X] + (ae + bd)\operatorname{Cov}[X, Y] + \operatorname{be} \operatorname{Var}[Y],$ (g)  $\operatorname{Var}[\sum_{i=1}^{n} X_i] = \sum_{i=1}^{n} \operatorname{Var}[X_i] + 2\sum_{1 \leq i < j \leq n} \operatorname{Cov}[X_i, X_j],$ (h) Jeśli zmienne losowe  $X_1, \dots, X_n$  są i.i.d., to

$$\operatorname{Var}\left[\frac{1}{n}\sum_{k=1}^{n}X_{k}\right] = \frac{1}{n}\operatorname{Var}[X_{1}].$$

Szkic dowodu: (c) Należy po prostu rozpisać definicje. (d) Nierówność Cauchy'ego-Schwarza. (e) Poprzednie Twierdzenie. (f) Kowariancja jest liniowa ze względu na każdy z argumentów. (g) Wynika z (f). (h) Wynika z

**A** Warunek Cov[X,Y] = 0 w ogólności nie implikuje niezależności Xi Y.

- 9. W9 KOWARIANCJA, ZBIEŻNOŚĆ WEDŁUG PRAWDOPODOBIEŃSTWA I SPWL
- <span id="page-19-0"></span>(9.1)  $\blacksquare$  Współczynnikiem korelacji wektora (X,Y) (dla którego  $\mathbb{E}[X^2], \mathbb{E}[Y^2] < \infty$ ) nazywamy wielkość

$$\rho(X,Y) = \frac{\operatorname{Cov}[X,Y]}{\sqrt{\operatorname{Var}[X]\operatorname{Var}[Y]}}.$$

- (9.2) **TW.** Własności korelacji.
  - (a)  $|\rho(X,Y)| < 1$ ,
  - (b)  $|\rho(X,Y)| = 1 \iff \mathbb{P}(X = aY + b) = 1$  dla pewnych stałych  $a, b \in \mathbb{R}$ ,
  - (c) Jeśli X i Y sa niezależne, to  $\rho(X,Y)=0$ .

Szkic dowodu: (a) i (c) wynikają z własności kowariancji. (b) Równość w nierówności Cauchy'ego-Schwarza zachodzi wtedy i tylko wtedy, gdy funkcje są liniowo zależne (Y jest funkcją liniową X).

A Z uwagi na drugą i trzecią własność, współczynnik korelacji jest interpretowany jako miara zależności liniowej.

(9.3)  $\blacksquare$  Jeśli Cov[X,Y] = 0, to powiemy, że zmienne losowe X i Y są nieskorelowane.

 $\Delta$  Zmienne niezależne są nieskorelowane, ale nieskorelowane nie są niezależne. Np. jeśli  $X \sim N(0,1)$  to X i  $Y := X^2 - 1$  są nieskorelowane, ale oczywiście są zależne.

(9.4)  $\blacksquare$  Macierzą kowariancji wektora  $\underline{X} = (X_1, \dots, X_n)$  nazywa

$$\Sigma(\underline{X}) = (\operatorname{Cov}[X_i, X_j])_{1 \le i, j \le n} = \begin{pmatrix} \operatorname{Var}[X_1] & \operatorname{Cov}[X_1, X_2] & \cdots & \operatorname{Cov}[X_1, X_n] \\ \operatorname{Cov}[X_1, X_2] & \operatorname{Var}[X_2] & \cdots & \operatorname{Cov}[X_2, X_n] \\ \vdots & & \ddots & \vdots \\ \operatorname{Cov}[X_1, X_n] & \operatorname{Cov}[X_2, X_n] & \cdots & \operatorname{Var}[X_n] \end{pmatrix}.$$

Równoważnie:  $\Sigma(\underline{X}) = \mathbb{E}\left[(\underline{X} - \mathbb{E}[\underline{X}]) \cdot (\underline{X} - \mathbb{E}[X])^{\top}\right]$ 

- (9.5) **TW.** Własności macierzy kowariancji.
  - (a)  $\Sigma(X)$  jest macierza symetryczna,
  - (b)  $\Sigma(\underline{X})$  jest macierzą nieujemnie określoną.

Szkic dowodu: Macierz K jest nieujemnie określona, jeśli dla każdego  $\underline{t} \in \mathbb{R}^n$  zachodzi

$$t^{\top} \cdot K \cdot t \ge 0.$$

Mamy

$$\underline{t}^{\top} \Sigma(\underline{X}) \underline{t} = \sum_{i=1}^{n} \sum_{j=1}^{n} t_i t_j \operatorname{Cov}[X_i, X_j] = \mathbb{E} \left[ \left( \sum_{i=1}^{n} t_i (X_i - \mathbb{E}[X_i]) \right)^2 \right].$$

(9.6)  $\mathbf{\Phi}_{\mathbf{a}}^{\mathbf{x}}$  Jeśli  $\underline{X} \sim \mathcal{N}_n(\underline{\mu}, \Sigma)$  dla  $\underline{\mu} \in \mathbb{R}^n$  oraz  $\Sigma \in \mathrm{Sym}_+(n)$ , to  $\mathbb{E}[\underline{X}] = \mu$  oraz  $\Sigma(\underline{X}) = \Sigma$ . Innymi słowy, dla

$$f_{\underline{X}}(\underline{x}) = \frac{1}{(\sqrt{2\pi})^n \sqrt{\det(\Sigma)}} e^{-\frac{1}{2}(\underline{x} - \underline{\mu})^\top \cdot \Sigma^{-1} \cdot (\underline{x} - \underline{\mu})}, \qquad \underline{x} \in \mathbb{R}^n$$

mamy

$$\mathbb{E}[X_i] = \int_{\mathbb{R}^n} x_i f_{\underline{X}}(\underline{x}) d\underline{x} = \mu_i, \qquad i \in \{1, \dots, n\},$$

oraz

$$\Sigma(\underline{X})_{ij} = \operatorname{Cov}[X_i, X_j] = \int_{\mathbb{R}^n} (x_i - \mu_i)(x_j - \mu_j) f_{\underline{X}}(\underline{x}) d\underline{x} = \Sigma_{ij}, \quad i, j \in \{1, \dots, n\}.$$

Ponadto, rozkłady brzegowe wektorów normalnych są normalne:

$$X_i \sim N(\mu_i, \Sigma_{ii}), \qquad i \in \{1, \dots, n\}$$

oraz ogólniej, dla  $A \subset \{1, \dots, n\},\$ 

$$\underline{X}_A := (X_i : i \in A) \sim \mathcal{N}_{|A|}(\mu_A, \Sigma_{AA})$$

gdzie  $\underline{\mu}_A = (\mu_i \colon i \in A)$  oraz  $\Sigma_{AA} = (\Sigma_{ij})_{i,j \in A}$ .

(9.7) Niech  $(X_n)_{n \geq 1}$  będzie ciągiem zmiennych losowych na  $(\Omega, \mathcal{F}, \mathbb{P})$ . Niech X będzie zmienną losową na  $(\Omega, \mathcal{F}, \mathbb{P})$ . Powiemy, że  $(X_n)_{n\geq 1}$  jest zbieżny według prawdopodobieństwa do zmiennej losowej X ( $\textcircled{\bullet}$   $X_n \stackrel{\mathbb{P}}{\longrightarrow} X$ ), jeśli

$$\forall \ \varepsilon > 0$$
  $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \varepsilon) = 0.$ 

- (9.8)  $\triangle$  Bezpośrednio z definicji wynika, że  $X_n \stackrel{\mathbb{P}}{\longrightarrow} X \iff |X_n X| \stackrel{\mathbb{P}}{\longrightarrow} 0 \iff X_n X \stackrel{\mathbb{P}}{\longrightarrow} 0.$
- (9.9)  $\overset{\bullet}{\bullet}$  Jeśli  $X_n \sim \mathrm{b}(1,1-\frac{1}{n}), \ n=1,2,\ldots,$  to  $X_n \stackrel{\mathbb{P}}{\longrightarrow} 1.$
- (9.10) **4** Jeśli  $X_n \sim b(n, p)$ , to

$$\mathbb{P}\left(\left|\frac{X_n}{n} - p\right| > \varepsilon\right) \le \frac{\operatorname{Var}[X_n]}{n^2 \varepsilon^2} = \frac{p(1-p)}{n \varepsilon^2} \to 0,$$

czyli  $\xrightarrow{X_n} \xrightarrow{\mathbb{P}} p$ .

(9.11) **LEM.** Granica według prawdopodobieństwa wyznaczona jest jednoznacznie, tzn. jeśli  $X_n \stackrel{\mathbb{P}}{\longrightarrow} X$  oraz  $X_n \stackrel{\mathbb{P}}{\longrightarrow} Y$ , to  $\mathbb{P}(X=Y)=1$ .

Szkic dowodu:

$$\begin{split} \mathbb{P}(|X-Y|>\varepsilon) &\leq \mathbb{P}(|X_n-X|+|X_n-Y|>\varepsilon) \leq \mathbb{P}(\{|X_n-X|\geq \varepsilon/2\} \cup \{|X_n-Y|>\varepsilon/2\}) \\ &\leq \mathbb{P}(|X_n-X|\geq \varepsilon/2) + \mathbb{P}(|X_n-Y|>\varepsilon/2). \end{split}$$

(9.12) **LEM.** Jeśli  $X_n \stackrel{\mathbb{P}}{\longrightarrow} X$  oraz  $Y_n \stackrel{\mathbb{P}}{\longrightarrow} Y$ , to  $X_n + Y_n \stackrel{\mathbb{P}}{\longrightarrow} X + Y$ . Szkic dowodu:

$$\mathbb{P}(|X_n + Y_n - X - Y| > \varepsilon) \le \mathbb{P}(|X_n - X| + |Y_n - Y| > \varepsilon) \le \mathbb{P}(\{|X_n - X| > \varepsilon/2\} \cup \{|Y_n - Y| > \varepsilon/2\})$$
  
$$\le \mathbb{P}(|X_n - X| \ge \varepsilon/2) + \mathbb{P}(|Y_n - Y| > \varepsilon/2).$$

Powiemy, że ciąg  $(X_n)_{n\geq 1}$  spełnia <u>Słabe Prawo Wielkich Liczb</u> (SPWL), jeśli

$$\frac{\sum_{k=1}^{n} (X_k - \mathbb{E}[X_k])}{n} \stackrel{\mathbb{P}}{\longrightarrow} 0.$$

 $oldsymbol{\Delta}$  Jeśli granica  $\lim_{n\to\infty} \frac{\sum_{k=1}^n \mathbb{E}[X_k]}{n}$  istnieje i jest skończona, to SPWL mówi nam, że

$$\frac{\sum_{k=1}^{n} X_k}{n} \xrightarrow[n \to \infty]{\mathbb{P}} \lim_{n \to \infty} \frac{\sum_{k=1}^{n} \mathbb{E}[X_k]}{n}.$$

W szczególności, jeśli  $\mathbb{E}[X_k] = \mu$ dla  $k = 1, 2, \ldots,$  to SPWL implikuje

$$\frac{\sum_{k=1}^{n} X_k}{n} \stackrel{\mathbb{P}}{\longrightarrow} \mu.$$

(9.14) TW. (SPWL Markowa) Jeśli spełniony jest warunek Markowa, tzn.

$$\lim_{n\to\infty}\frac{1}{n^2}\mathrm{Var}\left[\sum_{k=1}^n X_k\right]=0,$$

to dla  $(X_n)_{n\geq 1}$  zachodzi SPWL.

Szkic dowodu: Nierówność Czebyszewa.

**A** Powyższe twierdzenie stosuje się tylko do zmiennych losowych, dla których drugi moment jest skończony  $(\mathbb{E}[X_k^2] < \infty, k = 1, 2, \ldots)$ .

(9.15) **TW.** (SPWL Chinczyna) Jeśli  $(X_n)_{n\geq 1}$  mają takie same rozkłady, są parami niezależne oraz  $\mathbb{E}[|X_1|] < \infty$ , to

$$\frac{\sum_{k=1}^{n} X_k}{n} \stackrel{\mathbb{P}}{\longrightarrow} \mathbb{E}[X_1].$$

Szkic dowodu: Dla  $n \in \mathbb{N}$  zdefiniujmy  $Y_n = X_n \mathbb{1}_{|X_n| \leq n}$ . Wtedy

$$\sum_{n=1}^{\infty} \mathbb{P}(X_n \neq Y_n) = \sum_{n=1}^{\infty} \mathbb{P}(|X_n| > n) = \sum_{n=1}^{\infty} \mathbb{P}(|X_n| > n) = \sum_{n=1}^{\infty} \mathbb{P}(|X_1| > n) \leq \int_0^{\infty} \mathbb{P}(|X_1| > t) dt = \mathbb{E}[|X_1|] < \infty.$$

Zatem, z lematu Borela-Cantelliego,  $\mathbb{P}(\limsup_n \{X_n \neq Y_n\}) = 0$ , czyli  $\mathbb{P}(\liminf_n \{X_n = Y_n\}) = 1$ . Stąd wynika, że (wystarczy zauważyć, że licznik jest ograniczony)

$$\frac{\sum_{k=1}^{n} (X_k - Y_k)}{n} \stackrel{\mathbb{P}}{\longrightarrow} 0.$$

Wystarczy zatem pokazać, że zachodzi SPWL dla ciągu  $(Y_n)_n$ . Zastosujemy SPWL Markowa, sprawdzamy warunek Markowa:

$$\frac{\operatorname{Var}[\sum_{k=1}^{n} Y_{k}]}{n^{2}} \stackrel{\text{nzl}}{=} \frac{\sum_{k=1}^{n} \operatorname{Var}[Y_{k}]}{n^{2}} \leq \frac{\sum_{k=1}^{n} \mathbb{E}[Y_{k}^{2}]}{n^{2}} = \frac{\sum_{k=1}^{n} \mathbb{E}[X_{k}^{2} \mathbb{1}_{|X_{k}| \leq k}]}{n^{2}} \leq \frac{n \mathbb{E}[X_{1}^{2} \mathbb{1}_{|X_{1}| \leq n}]}{n^{2}}$$

$$= \frac{1}{n} \left( \mathbb{E}[X_{1}^{2} \mathbb{1}_{|X_{1}| < n^{1/3}}] + \mathbb{E}[X_{1}^{2} \mathbb{1}_{|X_{1}| \in [n^{1/3}, n]}] \right) \leq \frac{1}{n} \left( n^{2/3} + n \mathbb{E}[|X_{1}| \mathbb{1}_{|X_{1}| > n^{1/3}}] \right) \stackrel{n \to \infty}{\longrightarrow} 0.$$

Ostatecznie,

$$\lim_{n \to \infty} \frac{\sum_{k=1}^{n} \mathbb{E}[Y_k]}{n} = \mathbb{E}[X_1].$$

10. W10 - Zbieżność z prawdopodobieństwem 1 (MPWL), w  $L_p$  i według rozkładu

<span id="page-21-0"></span>(10.1) Niech  $(X_n)_{n\geq 1}$  będzie ciągiem zmiennych losowych na  $(\Omega, \mathcal{F}, \mathbb{P})$ . Niech X będzie zmienną losową na  $(\Omega, \mathcal{F}, \mathbb{P})$ . Powiemy, że  $(X_n)_{n\geq 1}$  jest zbieżny z prawdopodobieństwem 1 do zmiennej losowej X ( $\textcircled{\bullet}$   $X_n \stackrel{1}{\longrightarrow} X$ ), jeśli

$$\mathbb{P}\left(\left\{\omega \in \Omega \colon \lim_{n \to \infty} X_n(\omega) = X(\omega)\right\}\right) = \mathbb{P}\left(\lim_{n \to \infty} X_n = X\right) = 1.$$

▲ Zbieżność z prawdopodobieństwem 1 bywa nazywana zbieżnością prawie na pewno.

(10.2) **LEM.** Warunki równoważne zbieżności z prawdopodobieństwem 1.

$$X_{n} \xrightarrow{1} X \iff \mathbb{P}\left(\left\{\omega \colon \forall \varepsilon > 0 \; \exists N > 0 \; \forall n > N \; | X_{n}(\omega) - X(\omega)| \leq \varepsilon\right\}\right) = 1$$

$$\iff \mathbb{P}\left(\cap_{\varepsilon > 0} \cup_{N > 0} \cap_{n > N} \left\{|X_{n} - X| \leq \varepsilon\right\}\right) = 1$$

$$\iff \forall \varepsilon > 0 \; \mathbb{P}\left(\bigcup_{N > 0} \cap_{n > N} \left\{|X_{n} - X| \leq \varepsilon\right\}\right) = 1$$

$$\iff \forall \varepsilon > 0 \; \mathbb{P}\left(\liminf_{n} \left\{|X_{n} - X| \leq \varepsilon\right\}\right) = 1$$

$$\iff \forall \varepsilon > 0 \; \mathbb{P}\left(\limsup_{n} \left\{|X_{n} - X| > \varepsilon\right\}\right) = 0$$

$$\iff \forall \varepsilon > 0 \; \lim_{N \to \infty} \mathbb{P}\left(\cup_{n > N} \left\{|X_{n} - X| > \varepsilon\right\}\right) = 0$$

$$\iff \forall \varepsilon > 0 \; \lim_{N \to \infty} \mathbb{P}\left(\sup_{n > N} |X_{n} - X| > \varepsilon\right) = 0$$

$$\iff \forall \varepsilon > 0 \; \lim_{N \to \infty} \mathbb{P}\left(\sup_{n > N} |X_{n} - X| > \varepsilon\right) = 0$$

$$\iff \sup_{n > N} |X_{n} - X| \xrightarrow{\mathbb{P}} 0, \qquad (N \to \infty).$$

(10.3) **TW.** Niech  $(X_n)_n$  będzie ciągiem zmiennych losowych na  $(\Omega, \mathcal{F}, \mathbb{P})$ . Wtedy

$$X_n \xrightarrow{1} X \implies X_n \xrightarrow{\mathbb{P}} X.$$

Szkic dowodu: Wniosek z warunków równoważnych zbieżności z prawdopodobieństwem 1.

- (10.4) A Odwrotna implikacja nie jest prawdziwa.
  - Niech  $(A_n)_{n\in\mathbb{N}}$  będzie ciągiem niezależnych zdarzeń takich, że  $\lim_{n\to\infty}\mathbb{P}(A_n)=0$  oraz  $\sum_{n=1}^{\infty}\mathbb{P}(A_n)=\infty$ . Zdefiniujmy  $X_n(\omega) := \mathbb{1}_{A_n}(\omega)$ . Ciąg  $X_n$  zbiega według prawdopodobieństwa do 0, ale nie z prawdopodobieństwem 1. Faktycznie dla  $\varepsilon \in (0,1), \mathbb{P}(|X_n-0|>\varepsilon)=\mathbb{P}(A_n)\to 0.$  Z drugiej strony, z założeń o ciągu  $(A_n)_n$  oraz Lematu Borela-Cantelli'ego II wynika, że  $\mathbb{P}(\limsup_n A_n) = 1$ . Ponadto, dla  $\varepsilon \in (0,1)$ ,  $\mathbb{P}\left(\limsup_{n}\{|X_n-0|>\varepsilon\}\right)=\mathbb{P}\left(\limsup_{n}A_n\right)=1$ , co przeczy zbieżności z prawdopodobieństwem 1.  $\mathbb{P}$ -prawie na pewno,  $X_n(\omega)$  jest niezbieżnym ciągiem zer i jedynek.
- (10.5) **LEM.** Warunki dostateczne zbieżnoci z prawdopodobieństwem 1.

  - (a) Jeśli  $\sum_{n=1}^{\infty} \mathbb{P}(|X_n X| > \varepsilon) < \infty$  dla każdego  $\varepsilon > 0$ , to  $X_n \xrightarrow{1} X$ . (b) Jeśli  $\sum_{n=1}^{\infty} \mathbb{E}[|X_n X|^p] < \infty$  dla pewnego p > 0, to  $X_n \xrightarrow{1} X$ .

Szkic dowodu: (a) z podaddytywności mamy

$$\forall \varepsilon > 0 \lim_{N \to \infty} \mathbb{P}\left(\bigcup_{n > N} \{|X_n - X| > \varepsilon\}\right) \le \lim_{N \to \infty} \sum_{n > N} \mathbb{P}\left(\{|X_n - X| > \varepsilon\}\right) = 0.$$

- (b) Z nierówności Markowa mamy  $\mathbb{P}(|X_n X| > \varepsilon) \leq \mathbb{E}[|X_n X|^p]/\varepsilon^p$ .
- (10.6)  $\blacksquare$  Powiemy, że ciąg  $(X_n)_{n\geq 1}$  spełnia Mocne Prawo Wielkich Liczb (MPWL), jeśli

$$\frac{\sum_{k=1}^{n} (X_k - \mathbb{E}[X_k])}{n} \xrightarrow{1} 0.$$

(10.7) **TW.** (MPWL Kołmogorowa I) Niech  $(X_n)_{n>1}$  będzie ciągiem niezależnych zmiennych losowych dla którego  $\mathbb{E}[X_n^2] < \infty$ ,  $n \in \mathbb{N}$ . Jeśli spełniony jest warunek Kołmogorowa, tzn.

$$\sum_{n=1}^{\infty} \frac{\operatorname{Var}[X_n]}{n^2} < \infty$$

to dla ciągu  $(X_n)_{n>1}$  zachodzi MPWL.

(10.8) **TW.** (MPWL Kołmogorowa II) Niech  $(X_n)_{n>1}$  będzie ciągiem i.i.d. Jeśli  $\mathbb{E}[|X_1|] < \infty$ , to

$$\frac{\sum_{k=1}^{n} X_k}{n} \stackrel{1}{\longrightarrow} \mathbb{E}[X_1].$$

(10.9)  $\overset{\bullet}{\mathbf{x}}$  Niech  $(X_n)_{n\geq 1}$  będzie ciągiem i.i.d. o dystrybuancie F. Niech  $F_n$  będzie dystrybuantą empiryczną zbudowaną w oparciu o  $(X_k)_{k=1}^n$ , tzn.  $\hat{F}_n(t) := \frac{1}{n} \sum_{k=1}^n \mathbb{1}_{(-\infty,t]}(X_k)$ . Dla ciągu  $(\mathbb{1}_{(-\infty,t]}(X_k))_{k>1}$  zachodzi MPWL, bo jest to ciąg i.i.d. o skończonym pierwszym momencie. Zatem,

$$\hat{F}_n(t) \xrightarrow{1} \mathbb{E}[\mathbb{1}_{(-\infty,t]}(X_1)] = \mathbb{P}(X_1 \le t) = F(t), \qquad t \in \mathbb{R}.$$

A Zachodzi znacznie mocniejszy wynik, znany jako Twierdzenie Gliwienki-Cantellego. Przy założeniach jak powyżej zachodzi

$$\sup_{t \in \mathbb{R}} |\hat{F}_n(t) - F(t)| \stackrel{1}{\longrightarrow} 0.$$

(10.10)  $\blacksquare$  Niech  $(X_n)_{n\geq 1}$  będzie ciągiem zmiennych losowych na  $(\Omega, \mathcal{F}, \mathbb{P})$ . Niech X będzie zmienną losową na  $(\Omega, \mathcal{F}, \mathbb{P})$ . Powiemy, że  $(X_n)_{n\geq 1}$  jest zbieżny w (przestrzeni)  $L_p$ , p>0, do zmiennej losowej X (a  $X_n \xrightarrow{L_p} X$ ), jeśli  $\mathbb{E}[|X_n|^p] < \infty, \, \mathbb{E}[|X|^p] < \infty \text{ oraz}$ 

$$\lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0.$$

 $\begin{array}{cccccccccccccccccccccccccccccccccccc$ 

Szkic dowodu: Obie zbieżności implikują zbieżność według prawdopodobieństwa. Granica według prawdopodobieństwa jest z kolei wyznaczona jednoznacznie.

(10.13)  $\triangle$  Zbieżność z prawdopodobieństwem 1 w ogólności nie implikuje zbieżności w  $L_p$ . (  $\clubsuit$  )

**TW.** (Twierdzenie Lebesgue'a o zbieżności zdominowanej) Niech  $X_n \xrightarrow{1} X$  oraz  $|X_n(\omega)| \leq Y(\omega)$ , gdzie Y jest całkowalną zmienną losową (czyli  $\mathbb{E}[Y] < \infty$ ). Wtedy

$$\lim_{n \to \infty} \mathbb{E}[X_n] = \mathbb{E}[\lim_{n \to \infty} X_n] = \mathbb{E}[X].$$

(10.14) Wniosek: Niech  $X_n \stackrel{1}{\longrightarrow} X$  oraz niech f będzie funkcją ciągłą i ograniczoną. Wtedy z ograniczoności f oraz Twierdzenia Lebesgue'a o zbieżności zdominowanej mamy

$$\lim_{n \to \infty} \mathbb{E}[f(X_n)] = \mathbb{E}[\lim_{n \to \infty} f(X_n)].$$

Z kolei z ciągłości funkcji f,

$$\mathbb{E}[\lim_{n \to \infty} f(X_n)] = \mathbb{E}[f(\lim_{n \to \infty} X_n)] = \mathbb{E}[f(X)].$$

(10.15) Powiemy, że ciąg zmiennych losowych  $(X_n)_n$  zbiega według rozkładu do zmiennej losowej X ( $\textcircled{\bullet}$   $X_n \stackrel{d}{\longrightarrow} X$ ),

$$\forall f \in C_b(\mathbb{R}) \quad \lim_{n \to \infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)],$$

gdzie  $C_b(\mathbb{R})$  oznacza zbiór funkcji ciągłych i ograniczonych na  $\mathbb{R}$ .

 $\triangle$  Co do zasady, każda ze zmiennych  $X_n$  może być określona na innej przestrzeni probabilistycznej  $(\Omega, \mathcal{F}, \mathbb{P})$ . Powyższy warunek zależy wyłącznie od rozkładów X'ów: mamy  $\mathbb{E}[f(X_n)] = \int_{\mathbb{R}} f(t) \mathbb{P}_{X_n}(dt)$ .

- Odpowiednikiem powyższej zbieżności w analizie funkcjonalnej jest tzw. słaba zbieżność z \*.
- (10.16)  $\mathbf{A}_{n}^{*}$  Niech  $X_{n} \sim \mathrm{U}(\{0,1,\ldots,n-1\})$ . Dla  $f \in C_{b}(\mathbb{R})$  mamy

$$\lim_{n \to \infty} \mathbb{E}\left[f\left(\frac{X_n}{n}\right)\right] = \lim_{n \to \infty} \sum_{k=1}^{n-1} f\left(\frac{k}{n}\right) \frac{1}{n} = \int_0^1 f(x) dx,$$

gdzie po prawej stronie mamy całkę Riemanna. Z drugiej strony, zauważmy, że jeśli  $X \sim \mathrm{U}([0,1])$ , to  $\mathbb{E}[f(X)] =$  $\int_0^1 f(x)dx$ , gdzie mamy całkę Lebesgue'a. Ponieważ dla ładnych funkcji, całka Riemanna i Lebesgue'a się pokrywają, to z definicji mamy

$$\frac{X_n}{n} \xrightarrow{d} U \sim \mathrm{U}([0,1].$$

 $\blacktriangle$  Zapis  $\frac{X_n}{n} \stackrel{d}{\longrightarrow} U([0,1])$  nie ma sensu.

<span id="page-23-0"></span>

Rozważmy ciąg niezależnych zmiennych  $(X_n)_{n\geq 2}$  o rozkładach

$$\mathbb{P}(X_n = \pm n) = \frac{1}{2}p_n, \qquad \mathbb{P}(X_n = 0) = 1 - p_n.$$

Wtedy mamy  $\mathbb{E}[X_n] = 0$  oraz  $\operatorname{Var}(X_n) = n^2 p_n$ .

Rozważmy 3 konkretne wyboru ciągu  $(p_n)_n$ .

I 
$$p_n = \frac{1}{n^{\alpha}}$$
 dla pewnego  $\alpha > 1$ ,  
II  $p_n = \frac{1}{n \log(n)}$ ,

II 
$$p_n = \frac{n}{n \log(n)}$$
,

III 
$$p_n = \frac{1}{n}$$
.

Pokażemy, że

- a) dla ciągu I zachodzi MPWL, a więc również zachodzi SPWL
- b) dla ciagu II zachodzi SPWL, ale nie zachodzi MPWL,
- c) dla ciągu III nie zachodzi SPWL, a więc też nie zachodzi MPWL.

Tym samym, definiując $Y_n=\frac{\sum_{k=1}^n(X_k-\mathbb{E}[X_k])}{n}=\frac{\sum_{k=1}^nX_k}{n},$ mamy

- a)  $Y_n \stackrel{1}{\longrightarrow} 0$ ,
- b)  $Y_n \stackrel{\mathbb{P}}{\longrightarrow} 0 \text{ oraz } Y_n \not\stackrel{1}{\longrightarrow} 0$ ,
- c)  $Y_n \not\stackrel{\mathbb{P}}{\longleftrightarrow} 0$ .
- a) Dla ciągu I zachodzi MPWL: rzeczywiście, spełniony jest wtedy warunek Kołmogorowa:

$$\sum_{n=1}^{\infty} \frac{\text{Var}(X_n)}{n^2} = \sum_{n=1}^{\infty} \frac{n^2 p_n}{n^2} = \sum_{n=1}^{\infty} \frac{1}{n^{\alpha}} < \infty,$$

ponieważ  $\alpha > 1$ .

b) Dla ciągu II zachodzi SPWL, ale nie zachodzi MPWL: sprawdzamy najpierw warunek Markowa:

$$\lim_{n \to \infty} \frac{1}{n^2} \text{Var}(X_1 + \ldots + X_n) = \lim_{n \to \infty} \frac{\sum_{k=1}^n k^2 p_k}{n^2}.$$

Zauważmy, że

$$\frac{n^2 p_n}{n^2 - (n-1)^2} = \frac{n^2 \frac{1}{n \log(n)}}{2n - 1} \to 0, \qquad n \to \infty,$$

więc z Twierdzenia Stoltza mamy również  $\frac{\sum_{k=1}^{n} k^2 p_k}{n^2} \to 0$ , czyli warunek Markowa jest spełniony.

Dla tego ciągu nie jest spełnione MPWL: przeprowadzamy rozumowanie nie wprost. Gdyby MPWL zachodziło, to definiując  $S_n := \sum_{k=1}^n X_k$ , mamy

$$\frac{X_n}{n} = \frac{S_n - S_{n-1}}{n} = \frac{S_n}{n} + \frac{n-1}{n} \frac{S_{n-1}}{n-1} \xrightarrow{1} 0,$$

ponieważ oba składniki po prawej stronie zbiegają do 0 z prawdopodobieństwem 1. Oznacza to, że zbieżność z p-stwem 1 ciągu  $(X_n/n)_n$  do 0 jest warunkiem koniecznym MPWL. Pokażemy, że ciąg  $(X_n/n)_n$  nie zbiega z prawdopodobnieństwem 1, co będzie przeczyło zachodzeniu MPWL. W tym celu udowodnimy następujący lemat.

**LEM.** Niech  $(Y_n)_{n\geq 1}$  będzie ciągiem niezależnych zmiennych losowych. Wtedy

$$Y_n \xrightarrow{1} 0 \qquad \Longleftrightarrow \qquad \forall \varepsilon > 0 \quad \sum_{n=1}^{\infty} \mathbb{P}(|Y_n| > \varepsilon) < \infty.$$

Dowód. Dostateczność powyższego warunku wynika z **LEM.** (1.1) a). Pokażemy teraz konieczność. Ustalmy  $\varepsilon > 0$  oraz zauważmy, że z niezależności elementów ciągu  $(Y_n)_n$  wynika, że zdarzenia  $A_n := \{|Y_n| > \varepsilon\}$  są niezależne. Zatem, z lematów Borela-Cantellego, wynika, że

$$\sum_{k=1}^{\infty} \mathbb{P}(A_n) < \infty \qquad \iff \qquad \mathbb{P}(\limsup_{n} A_n) = 0.$$

Ale warunek  $\mathbb{P}(\limsup_n\{|Y_n|>\varepsilon\})=0$  jest równoważny (patrz poprzedni wykład) stwierdzeniu  $Y_n\stackrel{1}{\longrightarrow}0.$ 

Wracamy do (b): chcemy pokazać, że ciąg  $(X_n/n)_n$  nie zbiega do 0 z p-stwem 1. Mamy dla  $\varepsilon \in (0,1)$ ,

$$\sum_{n=1}^{\infty} \mathbb{P}\left(\left|\frac{X_n}{n}\right| > \varepsilon\right) = \sum_{n=1}^{\infty} (1 - \mathbb{P}(X_n = 0)) = \sum_{n=1}^{\infty} p_n = \sum_{n=1}^{\infty} \frac{1}{n \log(n)} = \infty.$$

gdzie ostatnią równość łatwo widać z całkowego kryterium zbieżności szeregów. Z wcześniejszego lematu wnioskujemy, że  $\frac{X_n}{n} \not \longrightarrow 0$ , a więc MPWL nie zachodzi.

c) Dla ciągu III nie zachodzi SPWL, więc tym bardziej MPWL. Z rachunku poczynionego w b), jasne jest że nie zachodzi MPWL. Argument dla niezachodzenia SPWL nie jest zbyt prosty, więc go nie podaję (należy oszacować z dołu  $\mathbb{P}(|Y_n| > \varepsilon)$  - można w tym celu skorzystać z "dolnej" nierówności Czebyszewa (której nie znamy)).

Dla ciągów I-III przeprowadzamy symulacje: generujemy 10<sup>3</sup> niezależnych trajektorii (czyli wykresów [10<sup>4</sup> ] 3 n 7→ X1+...+X<sup>n</sup> n ) i rysujemy na wspólnym wykresie. W I bierzemy α = 3/2 > 1.

![](_page_25_Figure_3.jpeg)

#### Wnioski:

(1) Z definicji zbieżności <sup>1</sup> −→ wiemy że jeśli Y<sup>n</sup> 1 −→ 0, to dla P prawie każdej ω i dowolnego ε > 0 istnieje N = N(ω, ε), że |Yn(ω)| ≤ ε dla n ≥ N. Na wykresie I rzeczywiście widzimy, że każda z trajektorii osobno zdaje się zbiegać do 0.

- (2) Z definicji <sup>P</sup> −→ wiemy, że P(|Yn| > ε) musi maleć do 0 gdy n → ∞. Nie znaczy to jednak, że wszystkie trajektorie muszą zbiegać do 0. Na wykresie II widzimy, że wraz ze wzrostem n, coraz mniej trajektorii skacze.
- (3) Trochę nie widać by coś się zmieniało z n na wykresie III.

#### 11. W11 - Zbieżność według rozkładu ciąg dalszy

<span id="page-26-0"></span>(11.1) TW. Niech (Xn)n≥<sup>1</sup> będzie ciągiem zmiennych losowych oraz niech (Fn)n≥<sup>1</sup> będzie ciągiem odpowiadających im dystrybuant.

$$X_n \xrightarrow{d} X \qquad \Longleftrightarrow \qquad \lim_{n \to \infty} F_n(t) = F_X(t) \quad \forall t \in C(F_X),$$

gdzie C(FX) oznacza zbiór punktów ciągłości dystrybuanty FX.

Szkic dowodu: Najpierw =⇒ .

Ustalmy 
$$\varepsilon > 0, t \in \mathbb{R}$$
 oraz zdefiniujmy  $f_+(x) = \begin{cases} 1, & x < t \\ 1 + \frac{t-x}{\varepsilon}, & x \in [t, t+\varepsilon] \text{ (rysunek jest pomocny). Oczywiście} \\ 0, & x > t + \varepsilon \end{cases}$ 

f<sup>+</sup> ∈ Cb(R) oraz

$$\mathbb{1}_{(-\infty,t]}(x) \le f_+(x) \le \mathbb{1}_{(-\infty,t+\varepsilon]}(x).$$

Zatem,

$$\limsup_{n \to \infty} F_n(t) = \limsup_{n \to \infty} \int_{\mathbb{R}} \mathbb{1}_{(-\infty, t]}(x) \mathbb{P}_{X_n}(dx) \le \limsup_{n \to \infty} \int_{\mathbb{R}} f_+(x) \mathbb{P}_{X_n}(dx)$$
$$= \int_{\mathbb{R}} f_+(x) \mathbb{P}_X(dx) \le \int_{\mathbb{R}} \mathbb{1}_{(-\infty, t+\varepsilon]}(x) \mathbb{P}_X(dx) = F_X(t+\varepsilon)$$

Z dowolności ε > 0 oraz prawostronnej ciągłości F<sup>X</sup> mamy lim supn→∞ Fn(t) ≤ FX(t) dla każdego t ∈ R. Niech f−(x) := f+(x + ε). Ponownie f<sup>−</sup> ∈ Cb(R) oraz

$$\mathbb{1}_{(-\infty,t-\varepsilon]}(x) \le f_{-}(x) \le \mathbb{1}_{(-\infty,t]}(x).$$

Wtedy

$$\begin{aligned} & \liminf_{n \to \infty} F_n(t) = \liminf_{n \to \infty} \int_{\mathbb{R}} \mathbbm{1}_{(-\infty,t]}(x) \mathbb{P}_{X_n}(dx) \geq \liminf_{n \to \infty} \int_{\mathbb{R}} f_-(x) \mathbb{P}_{X_n}(dx) \\ & = \int_{\mathbb{R}} f_-(x) \mathbb{P}_X(dx) \geq \int_{\mathbb{R}} \mathbbm{1}_{(-\infty,t-\varepsilon]}(x) \mathbb{P}_X(dx) = F_X(t-\varepsilon). \end{aligned}$$

Z dowolności ε > 0, mamy lim infn→∞ Fn(t) ≥ FX(t−) dla każdego t ∈ R. Podsumowując, dla każdego x ∈ R mamy

$$F_X(x-) \le \liminf_{n \to \infty} F_n(x) \le \limsup_{n \to \infty} F_n(x) \le F_X(x).$$

Jeśli x ∈ C(Fx), to FX(x−) = FX(x) oraz otrzymujemy implikację w prawą stronę. Teraz ⇐= . Zauważmy, że dla f ∈ Cb(R) mamy

$$\int_{\mathbb{R}} f(x) \mathbb{P}_{X_n}(dx) = \int_{(-\infty, -M) \cup (M, \infty)} f(x) \mathbb{P}_{X_n}(dx) + \int_{[-M, M]} f(x) \mathbb{P}_{X_n}(dx)$$

oraz pierwsza całka dla dużych n może być ograniczona przez c P(|X| > M) dla pewnej stałej c (zależnej tylko od funkcji f). Dobierając M dostatecznie duże, widzimy, że pierwsza całka jest dowolnie mała. Z kolei, funkcje ciągłe na przedziale zwartym są jednostajnie ciągłe i można jest jednostajnie aproksymować funkcjami prostymi, których zbieżność szybko wynika ze zbieżności dystrybuant.

- (11.2) 3 Przyjmijmy, że limn→∞ P(X<sup>n</sup> ≤ t) = 1(0,∞)(t) dla t ∈ R. Czy ciąg (Xn)<sup>n</sup> zbiega według rozkładu? Jeśli tak, to do jakiej granicy?
- (11.3) 3 Niech X<sup>n</sup> ∼ U({0, 1, . . . , n − 1}). Wtedy dla t ∈ [0, 1) z twierdzenia o 3 ciągach mamy

$$F_{X_n/n}(t) = \frac{\lfloor nt \rfloor + 1}{n} \xrightarrow{n \to \infty} t = F_{\mathrm{U}([0,1])}(t),$$

czyli <sup>X</sup><sup>n</sup> n d −→ U ∼ U([0, 1].

(11.4) 3 (Twierdzenie Poissona) Niech X<sup>n</sup> ∼ b(n, pn), gdzie limn→∞ np<sup>n</sup> = λ > 0. Wtedy X<sup>n</sup> d −→ X ∼ Pois(λ). (11.5) **LEM.** Jeśli  $X_n \stackrel{\mathbb{P}}{\longrightarrow} X$ , to  $X_n \stackrel{d}{\longrightarrow} X$ .

▲ Implikacja odwrotna nie jest (w ogólności) prawdziwa.

Szkic dowodu: Weźmy  $t \in C(F_X)$  i  $\varepsilon > 0$ . Mamy

$$F_{X_n}(t) = \mathbb{P}(X_n \le t, |X_n - X| \le \varepsilon) + \mathbb{P}(X_n \le t, |X_n - X| > \varepsilon).$$

Stąd,

$$F_{X_n}(t) \le \mathbb{P}(X - \varepsilon \le t, |X_n - X| \le \varepsilon) + \mathbb{P}(|X_n - X| > \varepsilon) \le F_X(t + \varepsilon) + \mathbb{P}(|X_n - X| > \varepsilon).$$

Zatem,  $\limsup_{n\to\infty} F_{X_n}(t) \leq F_X(t+\varepsilon)$  dla dowolnego  $\varepsilon > 0$ , a stąd  $\limsup_{n\to\infty} F_{X_n}(t) \leq F_X(t+\varepsilon) = F_X(t)$  (z prawostronnej ciągłości  $F_X$ ).

Podobnie od dołu,

$$F_{X_n}(t) \ge \mathbb{P}(X + \varepsilon \le t, |X_n - X| \le \varepsilon) \ge F_X(t - \varepsilon) - \mathbb{P}(|X_n - X| > \varepsilon).$$

Stąd,  $\liminf_{n\to\infty} F_{X_n}(t) \geq F_X(t-\varepsilon)$  dla  $\varepsilon > 0$ . Przechodząc z  $\varepsilon \to 0$  oraz korzystając z faktu, że  $t \in C(F_X)$  otrzymujemy, że  $\liminf_{n\to\infty} F_{X_n}(t) \geq F_X(t-) = F_X(t)$ . Pokazaliśmy, że dla  $t \in C(F_X)$ ,

$$F_X(t) \le \liminf_{n \to \infty} F_{X_n}(t) \le \limsup_{n \to \infty} F_{X_n}(t) \le F_X(t),$$

co kończy dowód.

(11.6)  $\blacksquare$  Funkcją generującą momenty zmiennej losowej X nazywamy funkcję  $M_X : \Theta \to \mathbb{R}$  zadaną przez

$$M_X(\theta) = \mathbb{E}[e^{\theta X}], \quad \theta \in \Theta.$$

gdzie  $\Theta = \{ \theta \in \mathbb{R} \colon \mathbb{E}[e^{\theta X}] < \infty \}.$ 

 $\triangle$  Zawsze mamy  $0 \in \Theta$ .

(11.7)  $\bullet$  Jeśli  $X \sim \text{EXP}(\lambda)$ , to

$$\mathbb{E}[e^{\theta X}] = \begin{cases} \frac{\lambda}{\lambda - \theta}, & \theta < \lambda, \\ \infty, & \theta \ge \lambda. \end{cases}$$

Tutaj  $\Theta = (-\infty, \lambda)$ .

(11.8)  $\mathbf{Q}_{\mathbf{a}}^{\mathbf{a}}$  Jeśli  $X \sim N(\mu, \sigma^2)$ , to

$$\mathbb{E}[e^{\theta X}] = e^{\theta \mu + \frac{\theta^2}{2}\sigma^2}, \qquad \theta \in \Theta = \mathbb{R}.$$

(11.9)  $\bullet$  Jeśli  $X \sim \text{Pois}(\lambda)$ , to

$$\mathbb{E}[e^{\theta X}] = e^{\lambda(e^{\theta} - 1)}, \qquad \theta \in \Theta = \mathbb{R}.$$

- (11.10) **TW.** (Własności funkcji generującej momenty) Niech  $(-\theta_0, \theta_0) \subset \Theta$  dla pewnego  $\theta_0 > 0$  (innymi słowy, niech  $M_X$  będzie określona w otoczeniu zera). Wtedy
  - (a)  $\mathbb{E}[|X|^k] < \infty \text{ dla } k \in \mathbb{N},$
  - (b)  $M_X(t) = \sum_{n=0}^{\infty} \frac{t^n}{n!} \mathbb{E}[X^n]$  dla  $t \in (-\theta_0, \theta_0),$
  - (c)  $M_X^{(k)}(0) = \mathbb{E}[X^k] \operatorname{dla} k \in \mathbb{N}.$

Szkic dowodu: Mamy  $e^{|t|} \le e^t + e^{-t}$ , zatem  $\mathbb{E}[e^{t|X|}] < \infty$  dla  $t < \theta_0$ . Ponadto,  $\frac{t^k}{k!} |X|^k \le e^{t|X|}$  dla t > 0, wiec mamy (a).

Żeby uzasadnić zamianę kolejności  $\mathbb{E}[\cdot]$  oraz  $\sum_{n=1}^{\infty}$  w (b) skorzystamy z Twierdzenia Lebesgue'a o zbieżności zdominowanej (patrz W10). Zdefiniujmy  $S_n = \sum_{k=0}^n \frac{t^k}{k!} X^k$  oraz zauważmy, że  $S_n \xrightarrow{1} e^{tX}$ . Ponadto,

$$\mathbb{E}[\lim_{n \to \infty} S_n] = M_X(t) \quad \text{oraz} \quad \lim_{n \to \infty} \mathbb{E}[S_n] = \sum_{n=0}^{\infty} \frac{t^k}{k} \mathbb{E}[X^k].$$

Ponieważ  $|S_n| \leq Y := e^{|tX|}$  oraz  $\mathbb{E}[Y] < \infty$ , Twierdzenie Lebesgue'a daje nam (b).

Punkt (b) mówi nam, że  $M_X$  jest szeregiem potęgowym. Z ogolnej teorii wiemy, że szeregi potęgowe możemy różniczkować wyraz po wyrazie wewnątrz ich promienia zbieżności (który tutaj wynosi co najmniej  $\theta_0 > 0$ ). W ten sposób otrzymujemy (c).

(11.11) **TW.** Niech X i Y będą zmiennymi losowymi takimi, że  $M_X(t) = M_Y(t)$  dla  $t \in (-\varepsilon, \varepsilon)$  dla pewnego  $\varepsilon > 0$ . Wtedy X i Y mają takie same rozkłady. Innymi słowy, funkcja generująca momenty, jesli jest określona w otoczeniu zera, jednoznacznie wyznacza rozkład.

 $oldsymbol{\Delta}$  Dowód powyższego twierdzenia opiera się zwykle na wykorzystaniu związku FGM z transformatą Laplace'a.  $oldsymbol{\Delta}$  Ponieważ FGM jest "generowana" przez momenty, powyższy wynik oznacza, że jeśli FGM istnieje w otoczeniu 0, to ciąg momentow  $(\mathbb{E}[X^n])_{n=1}^{\infty}$  jednoznacznie wyznacza rozkład X.

Ogólnie, jeśli X ma wszystkie momenty skończone, ale jego FGM nie istnieje (czyli poza 0 jest nieskończona), to mogą istnieć rożne rozkłady posiadające te same momenty. Przykładem rozkładu, który nie jest wyznaczony jednoznacznie przez momenty jest tzw. rozkład log-normalny (rozkład  $X = e^N$ , gdzie  $N \sim N(\mu, \sigma^2)$ ).

(11.12)

$$\mathbb{E}[e^{\theta(X+Y)}] = \mathbb{E}[e^{\theta X}]\mathbb{E}[e^{\theta Y}] = e^{\theta(\mu_1 + \mu_2) + \frac{\theta^2}{2}(\sigma_1^2 + \sigma_2^2)},$$

czyli  $X + Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ .

(11.13) **TW.** (Zasada Helly'ego) Niech  $(F_n)_{n\geq 1}$  będzie ciągiem dystrybuant. Istnieje jego podciąg  $(F_{n_k})_{k\geq 1}$  oraz funkcja F takie, że

$$\lim_{k \to \infty} F_{n_k}(t) = F(t) \qquad \forall t \in C(F),$$

gdzie F jest niemalejąca, prawostronnie ciągła oraz  $0 \le F \le 1$  (ale F nie musi być dystrybuantą). Szkic dowodu:

- Ponumerujmy wszystkie liczy wymierne  $\mathbb{Q} = (q_1, q_2, \ldots)$ .
- Ponieważ ciąg liczbowy  $(F_n(q_1))_{n\geq 1}$  jest ograniczony, więc z twierdzenia Bolzano-Weierstrassa istnieje podciąg  $(l_k^{(1)})_{k\geq 1}\subset \mathbb{N}$  taki, że

$$\lim_{k \to \infty} F_{l_k^{(1)}}(q_1) = F(q_1).$$

Na tym etapie  $F(q_1)$  jest po prostu oznaczeniem granicy, nic nie wiemy jeszcze o funkcji F.

• Rozważmy teraz ciąg  $(F_{l_k^{(1)}}(q_2))_{n\geq 1}$ , z którego ograniczoności znowu wnioskujemy istnienie podciągu  $(l_k^{(2)})_{k\geq 1}$  takiego, że

$$\lim_{k \to \infty} F_{l_k^{(2)}}(q_2) = F(q_2).$$

• Iterując takie postępowanie, konstruujemy podciągi  $\ell^{(m)} := (l_k^{(m)})_{k \geq 1}$  dla których

$$\lim_{k \to \infty} F_{l_k^{(m)}}(q_m) = F(q_m).$$

•  $\P$ Kluczowa obserwacja jest następująca. Ponieważ  $\mathbb{N} \supset \ell^{(1)} \supset \ell^{(2)} \supset \ell^{(m)}$ , to w rzeczywistości pokazaliśmy, że

$$\lim_{k \to \infty} F_{l_k^{(m)}}(q_i) = F(q_i) \qquad \text{dla } i = 1, 2, \dots, m.$$

•

$$\lim_{k \to \infty} F_{n_k}(q_i) = F(q_i) \qquad \text{dla } i = 1, 2, \dots,$$

czyli mamy zbieżność dla wszystkich liczb wymiernych.

- Powyżej określiliśmy funkcję F na wszystkich liczbach wymiernych. Dla dowolnego  $x \in \mathbb{R}$  definiujemy  $F(x) := \inf\{F(q) \colon q \in \mathbb{Q}, q > x\}.$
- Prawostronna ciągłość (monotoniczność, ograniczoność)  $F_n$  daje prawostronną ciągłość (monotoniczność, ograniczoność) F.

#### 12. W12 - Centralne Twierdzenie Graniczne

<span id="page-28-0"></span>(12.1) **TW.** (Twierdzenie o ciągłości dla funkcji generujących momenty) Niech  $M_{X_n}$  będzie funkcją generującą momenty zmiennej losowej  $X_n,\,n=1,2,\ldots$  Jeśli dla pewnego  $\varepsilon>0$  zachodzi  $M_{X_n}(s),M_X(s)<\infty$  dla  $s\in(-\varepsilon,\varepsilon)$  oraz

$$\lim_{n \to \infty} M_{X_n}(s) = M_X(s) \qquad \text{dla } s \in (-\varepsilon, \varepsilon),$$

to  $X_n \stackrel{d}{\longrightarrow} X$ .

Szkic dowodu:

Oznaczmy  $F_n=F_{X_n}$ . Z Zasady Helly'ego, z ciągu  $(F_n)_{n\geq 1}$  można wybrać podciąg  $(F_{n_k})_k$  dla którego mamy

$$\lim_{k \to \infty} F_{n_k}(t) = F(t) \qquad \forall t \in C(F).$$

Plan dowodu: pokażemy kolejno, że

- F jest dystrybuanta
- $F = F_X$ ,
- cały ciąg  $(F_n)_{n>1}$  też zbiega do F.

Dla dowolnego x > 0 oraz  $\beta \in (0, \varepsilon)$ ,

$$F_n(-x) + 1 - F_n(x) = \int_{(-\infty, -x]} e^{\beta t} e^{-\beta t} \mathbb{P}_{X_n}(dt) + \int_{(x, \infty)} e^{-\beta t} e^{\beta t} \mathbb{P}_{X_n}(dt)$$

$$\leq e^{-\beta x} \int_{(-\infty, -x]} e^{-\beta t} \mathbb{P}_{X_n}(dt) + e^{-\beta x} \int_{(x, \infty)} e^{\beta t} \mathbb{P}_{X_n}(dt)$$

$$\leq e^{-\beta x} (M_{X_n}(-\beta) + M_{X_n}(\beta)).$$

Stad dla  $n = n_k$ ,

$$F_{n_k}(-x) + 1 - F_{n_k}(x) \le e^{-\beta x} (M_{X_{n_k}}(-\beta) + M_{X_{n_k}}(\beta)).$$

Przechodząc z  $k \to \infty$  otrzymujemy

$$F(-x) + 1 - F(x) \le e^{-\beta x} (M_X(-\beta) + M_X(\beta)),$$

a stąd  $\lim_{x\to\infty} (F(-x) + 1 - F(x)) = 0$ . Zatem

$$0 \le \lim_{x \to \infty} F(-x) \le \lim_{x \to \infty} (F(-x) + 1 - F(x)) = 0,$$

$$0 \le 1 - \lim_{x \to \infty} F(x) \le \lim_{x \to \infty} (F(-x) + 1 - F(x)) = 0,$$

czyli F jest dystrybuantą. Pokazaliśmy już, że ciąg  $(X_{n_k})_k$  zbiega według rozkładu, ale jeszcze nie wiemy że granicą jest X, a także nie wiemy czy cały ciąg  $(X_n)_n$  też zbiega. Pokażemy teraz, że F jest dystrybuantą zmiennej losowej X. Niech  $\mu$  będzie miarą generowaną przez dystrybuantę F. Z definicji zbieżności według rozkładu wiemy, że dla każdej funkcji ciągłej i ograniczonej f mamy

$$\lim_{k \to \infty} \int_{\mathbb{R}} f(x) \mathbb{P}_{X_{n_k}}(dx) = \int_{\mathbb{R}} f(x) \mu(dx).$$

Dla  $s \in (-\varepsilon, \varepsilon)$  oraz N > 0 zdefiniujmy  $f_s^{(N)}(x) := \begin{cases} e^{sx}, & |x| \leq N \\ 0, & |x| > N \end{cases}$ . Co prawda  $f_s \notin C_b(\mathbb{R})$ , bo nie jest ciągła, ale zbieżność (\*\*) nadal zachodzi o ile  $N \in C(F)$ . Zatem

$$\lim_{k \to \infty} \int_{[-N,N]} e^{sx} \mathbb{P}_{X_{n_k}}(dx) = \int_{[-N,N]} e^{sx} \mu(dx).$$

Z drugiej strony, z założenia (\*) mamy

$$\lim_{k \to \infty} M_{X_{n_k}}(s) = \lim_{k \to \infty} \int_{\mathbb{P}} e^{sx} \mathbb{P}_{X_{n_k}}(dx) = \int_{\mathbb{P}} e^{sx} \mathbb{P}_X(dx).$$

Przechodząc w (\*\*\*) z  $N \to \infty$  oraz porównując z powyższą linijką otrzymujemy dla  $s \in (-\varepsilon, \varepsilon)$ ,

$$\int_{\mathbb{D}} e^{sx} \mu(dx) = \int_{\mathbb{D}} e^{sx} \mathbb{P}_X(dx).$$

Z jednoznaczności funkcji generującej momenty otrzymujemy, że  $\mu = \mathbb{P}_X$ , czyli  $F = F_X$ . Wiemy już, że  $X_{n_k} \stackrel{d}{\longrightarrow} X$ . Pokażemy teraz, że  $X_n \stackrel{d}{\longrightarrow} X$ . Wiemy, że  $X_n \stackrel{d}{\longrightarrow} X$  wtedy i tylko wtedy, gdy

$$\forall x \in C(F) \ \forall \varepsilon > 0 \ \exists N > 0 \ \forall n > N \qquad |F_n(x) - F(x)| < \varepsilon.$$

Zaprzeczeniem tego warunku jest

$$\exists x_0 \in C(F) \ \exists \varepsilon_0 > 0 \ \forall N > 0 \ \exists n_N > N \qquad |F_{n_N}(x) - F(x)| > \varepsilon.$$

Dla ciągu  $(F_{n_N})_N$  można jednak powtórzyć wszystkie wcześniejsze kroki oraz znaleźć podciąg zbieżny punktowo do F. Sprzeczność.

(12.2) **TW.** (Centralne Twierdzenie Graniczne) Niech  $(X_i)_{i\geq 1}$  - ciąg i.i.d. oraz  $\mathbb{E}[X_1^2] < \infty$ . Oznaczmy  $\mu = \mathbb{E}[X_1]$  oraz  $\sigma^2 = \operatorname{Var}[X_1] > 0$ . Wtedy

$$\frac{X_1 + \dots X_n - n\mu}{\sqrt{n\sigma^2}} \xrightarrow{d} Z \sim N(0,1).$$

Szkic dowodu gdy  $M_X(t) < \infty$  dla  $t \in \mathbb{R}$ 

- Dla  $Y_k := \frac{X_k \mu}{\sigma}$  mamy  $\mathbb{E}[Y_k] = 0$  oraz  $\text{Var}[Y_k] = 1$ . Ciąg  $(Y_k)_k$  jest i.i.d.
- $M_{Y_1}(s) = 1 + \frac{s^2}{2} + r(s)$ , gdzie  $r(s)/s^2 \to 0$ , gdy  $s \to 0$ .
- $M_{\frac{Y_1 + \dots + Y_n}{\sqrt{n}}}(s) = (M_{Y_1}(\frac{s}{\sqrt{n}}))^n = \left(1 + \frac{s^2/2 + nr(s/\sqrt{n})}{n}\right)^n \to e^{s^2/2}, \text{ gdy } n \to \infty.$

Szkic dowodu gdy wiemy tylko, że  $\mathbb{E}[X^2] < \infty$ :

• Zamiast funkcji generującej momenty  $M_Y$  definiujemy tzw. <u>funkcję charakterystyczną</u> (w innym kontekście jest zwana transformatą Fouriera)

$$\phi_Y(s) := \mathbb{E}[e^{isY}] = \mathbb{E}[\cos(sY)] + i \mathbb{E}[\sin(sY)], \quad s \in \mathbb{R}$$

Funkcja charakterystyczna, w odróżnieniu od funkcji generującej momenty, przyjmuje wartości zespolone oraz zawsze istnieje: mamy  $|\mathbb{E}[e^{isY}]| \leq \mathbb{E}[|e^{isY}|] = 1$ . Ponadto, funkcja charakterystyczna jednoznacznie wyznacza rozkład oraz zachodzi twierdzenie o ciągłości dla funkcji charakterystycznych  $(X_n \stackrel{d}{\longrightarrow} X$  wtedy i tylko wtedy, gdy  $\phi_{X_n}(s) \to \phi_X(s)$  dla każdego  $s \in \mathbb{R}$ ).

• Jeśli istnieją odpowiednie momenty zmiennej losowej, to funkcję charaktertystyczną można rozwijać. W szczególności, jeśli  $\mathbb{E}[Y^2] < \infty$ , to

$$\phi_Y(s) = 1 + is\mathbb{E}[Y] - \frac{s^2}{2}\mathbb{E}[Y^2] + r(s),$$

gdzie  $r(s)/s^2 \to 0$ , gdy  $s \to 0$ .

 $\bullet$  Podobnie jak dla funkcji generującej momenty, mamy zatem dla  $s \in \mathbb{R}$ 

$$\phi_{\frac{Y_1 + \dots + Y_n}{\sqrt{n}}}(s) = \left(1 + \frac{-s^2/2 + nr(s/\sqrt{n})}{n}\right)^n \to e^{-s^2/2}$$

- Jeśli funkcja generująca momenty istnieje, to zwykle zachodzi  $\phi_Y(s) = M_Y(is)$ . Jeśli  $Z \sim N(0,1)$ , to  $\phi_Z(s) = M_Z(is) = e^{-s^2/2}$ . Zatem, twierdzenie o ciągłości dla funkcji charakterystycznych kończy dowód.
- (12.3) **A** W CTG nie mamy zbieżności według prawdopodobieństwa, a więc tym bardziej z prawdopodobienstwem 1. Żeby to zobaczyć, załóżmy nie wprost, że

$$\frac{S_n}{\sqrt{n}} := \frac{X_1 + \dots X_n - n\mu}{\sqrt{n\sigma^2}} \xrightarrow{\mathbb{P}} Z.$$

Zatem.

$$\frac{S_{2n} - S_n}{\sqrt{n}} = \sqrt{2} \frac{S_{2n}}{\sqrt{2n}} - \frac{S_n}{\sqrt{n}} \stackrel{\mathbb{P}}{\longrightarrow} \left(\sqrt{2} - 1\right) Z.$$

Ponieważ zbieżność według prawdopodobieństwa implikuje zbieżność według rozkładu, mamy stad

$$\frac{S_{2n} - S_n}{\sqrt{n}} \stackrel{d}{\longrightarrow} \left(\sqrt{2} - 1\right) Z.$$

Ale dla każdego  $n,\,\frac{S_{2n}-S_n}{\sqrt{n}}$ ma taki sam rozkład jak  $\frac{S_n}{\sqrt{n}},$  więc z CTG wiemy, że

$$\frac{S_{2n} - S_n}{\sqrt{n}} \stackrel{d}{\longrightarrow} Z.$$

Otrzymujemy stąd i z  $(\P)$ , że  $F_{(\sqrt{2}-1)Z}(t) = F_Z(t)$  dla  $t \in \mathbb{R}$ , co jest niemożliwe jeśli  $\mathbb{P}(Z \neq 0) > 0$ . Sprzeczność.

#### 13. W13 - Warunkowa wartość oczekiwana

- <span id="page-30-0"></span>(13.1) Jeśli  $\mathbb{P}(B) > 0$  dla pewnego  $B \in \mathcal{F}$ , to  $\mathbb{P}_B(\cdot) := \mathbb{P}(\cdot|B)$  jest prawdopodobieństwem na  $(\Omega, \mathcal{F})$ . Możemy więc liczyć całki względem  $\mathbb{P}_B$ . Rozważmy zmienną losową X taką, że  $\mathbb{E}[|X|] < \infty$ .
  - 🗸 Definiujemy warunkową wartość oczekiwaną (WWO) pod warunkiem zdarzenia

$$\mathbb{E}[X|B] := \int_{\Omega} X(\omega) \mathbb{P}_B(d\omega).$$

 $\blacksquare$  Niech X będzie zmienną losową na  $(\Omega, \mathcal{F})$ . Rozkładem warunkowym X pod warunkiem zdarzenia B nazywamy funkcję  $\mathbb{P}_{X|B}$  zadaną przez

$$\mathbb{P}_{X|B}(C) := \mathbb{P}(X \in C|B) = \frac{\mathbb{P}(\{X \in C\} \cap B)}{\mathbb{P}(B)}, \qquad C \in \mathcal{B}(\mathbb{R}).$$

Dystrybuanta rozkładu warunkowego X pod warunkiem zdarzenia B definiowana jest wzorem

$$F_{X|B}(t) := \mathbb{P}_{X|B}((-\infty, t]) = \mathbb{P}(X \le t|B).$$

(13.2) **LEM.** Jeśli  $\mathbb{P}(B) > 0$  oraz X jest całkowalną zmienną losową, to  $\mathbb{E}[X|B] = \frac{\mathbb{E}[X \mathbbm{1}_B]}{\mathbb{P}(B)}$ . Szkic dowodu: Ponieważ obie strony są liniowe w X, wystarczy sprawdzić dla  $X = \mathbbm{1}_A$  dla  $A \in \mathcal{F}$ . Mamy

$$\int_{\Omega} \mathbb{1}_A(\omega) \mathbb{P}_B(d\omega) = \mathbb{P}_B(A) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)} = \frac{\mathbb{E}[\mathbb{1}_A \mathbb{1}_B]}{\mathbb{P}(B)}.$$

Dowolną zmienną losową X aproksymujemy przez ciąg funkcji prostych.

(13.3) **LEM.** Jeśli  $(B_n)_n$  jest nietrywialnym przeliczalnym rozbiciem  $\Omega$  oraz X jest całkowalną zmienną losową, to

$$\mathbb{E}[X] = \sum_{n} \mathbb{E}[X|B_n]\mathbb{P}(B_n).$$

Szkic dowodu:  $1 = \mathbb{1}_{\Omega}(\omega) = \sum_{n} \mathbb{1}_{B_n}(\omega)$ .

(13.4)  $(X_n)_n$  będzie ciągiem zmiennych losowych o takiej samej wartości oczekiwanej oraz niech N będzie zmienną losową niezależną od  $(X_n)_n$  taką, żę  $\mathrm{supp}(N) = \{0,1,\ldots\}$ . Niech  $S_0 = 0$ ,  $S_n = X_1 + \ldots + X_n$  dla  $n \in \mathbb{N}$ . Wtedy  $\mathbb{E}[S_n] = n \, \mathbb{E}[X_1]$  oraz

$$\mathbb{E}[S_N] = \sum_{n=0}^{\infty} \mathbb{E}[S_N | N = n] \mathbb{P}(N = n) = \sum_{n=0}^{\infty} \frac{\mathbb{E}[S_N \mathbb{1}_{N=n}]}{\mathbb{P}(N = n)} \mathbb{P}(N = n) = \sum_{n=0}^{\infty} \mathbb{E}[S_n \mathbb{1}_{N=n}]$$

$$\stackrel{\text{nzl}}{=} \sum_{n=0}^{\infty} \mathbb{E}[S_n] \mathbb{E}[\mathbb{1}_{N=n}] = \mathbb{E}[X] \sum_{n=0}^{\infty} n \, \mathbb{P}(N = n) = \mathbb{E}[X] \mathbb{E}[N].$$

(13.5)  $\mathbf{Q}_{\bullet}^{\bullet}$  Niech  $(X,Y) \sim m_2(m,(p_1,p_2))$ . Wtedy  $\mathbb{P}(Y=l) = \binom{m}{l} p_2^l (1-p_2)^{m-l}$  dla  $l=0,1,\ldots,m$  oraz

$$\mathbb{P}(X = k | Y = l) = {m - l \choose k} \left(\frac{p_1}{1 - p_2}\right)^k \left(1 - \frac{p_1}{1 - p_2}\right)^{m - l - k}, \qquad k = 0, 1, \dots, m - l.$$

Widzimy, że rozkład warunkowy X pod warunkiem zdarzenia  $\{Y=l\}$  to  $\mathbf{b}(m-l,\frac{p_1}{1-p_2})$ . Będziemy pisali

$$X|Y=l \sim \mathrm{b}\left(m-l, \frac{p_1}{1-p_2}\right)$$
 lub nawet  $X|Y \sim \mathrm{b}\left(m-Y, \frac{p_1}{1-p_2}\right)$ .

Wnioskujemy też stąd, że  $\mathbb{E}[X|Y=l] = (m-l)\frac{p_1}{1-p_2}$  oraz  $\text{Var}[X|Y=l] = (m-l)\frac{p_1}{1-p_2}(1-\frac{p_1}{1-p_2})$ .

lack A  $\mathbb{E}[X|Y=l]$  jest po prostu wartością oczekiwaną liczoną względem rozkładu warunkowego X|Y=l.

**A** A Skoro znamy funkcję  $m(l) := \mathbb{E}[X|Y=l]$ , to możemy równie dobrze rozważyć  $m(Y(\omega)) = \mathbb{E}[X|Y=l]$ , zwykle oznaczane przez  $\mathbb{E}[X|Y](\omega)$ . Zauważmy, że jest to zmienna losowa!

- <span id="page-31-0"></span>(13.6) Poprzedni przykład był prosty, bo dotyczył rozkładów dyskretnych.
  - Niech (X,Y) ma rozkład jednostajny na  $T=\{(x,y)\in\mathbb{R}^2\colon 0\leq y\leq x\leq 2\}$ , tzn.  $f_{(X,Y)}(x,y)=\frac{1}{2}\mathbbm{1}_T(x,y)$ . Chcielibyśmy znaleźć rozkład X|Y=1. Intuicyjnie powinno to być  $\mathrm{U}([1,2])$ , ale  $\mathbb{P}(Y=1)=0$ , więc żeby rozważać to formalnie, do problemu trzeba podejść inaczej. Najpierw powinnismy lepiej zrozumieć przypadek dyskretny.
- (13.7) Niech N będzie zmienną losową o rozkładzie typu dyskretnego. Jeśli  $\mathbb{E}[|X|] < \infty$ , to warunkową wartością oczekiwaną X pod warunkiem zmiennej losowej N nazywamy zmienną losową  $\mathbb{E}[X|N]$  zdefiniowaną przez

$$\mathbb{E}[X|N](\omega) = \sum_{n \in \text{supp}(N)} \mathbb{E}[X|N=n] \mathbb{1}_{N(\omega)=n},$$

tzn. jeśli  $N(\omega) = n$ , to  $\mathbb{E}[X|N](\omega) = \mathbb{E}[X|N = n]$ .

- (13.8) **LEM.** Własności WWO pod warunkiem dyskretnej zmiennej losowej.
  - (a)  $\mathbb{E}[X|N](\omega) = m(N(\omega))$  dla pewnej borelowskiej funkcji m,
  - (b)  $\mathbb{E}[X\mathbbm{1}_{N\in B}] = \mathbb{E}[\mathbb{E}[X|N]\mathbbm{1}_{N\in B}]$  dla każdego  $B\in\mathcal{B}(\mathbb{R})$ .

Szkic dowodu:

- (a) Oczywiste z definicji.
- (b) Niech  $B \in \mathcal{B}(\mathbb{R})$  oraz  $B \cap \text{supp}(N) = \{n_1, \dots, n_k\}$ .

$$\mathbb{E}\left[\mathbb{E}[X|N]\mathbb{1}_{N \in B}\right] = \sum_{n} \mathbb{E}[X|N = n]\mathbb{E}[\mathbb{1}_{N = n}\mathbb{1}_{N \in B}] = \sum_{i = 1}^{k} \mathbb{E}[X|N = n_{i}]\mathbb{P}(N = n_{i}) = \sum_{i = 1}^{k} \mathbb{E}[X\mathbb{1}_{N = n_{i}}] = \mathbb{E}[X\mathbb{1}_{N \in B}].$$

- (13.9) Niech Y będzie zmienną losową. Jeśli  $\mathbb{E}[|X|] < \infty$ , to warunkową wartością oczekiwaną X pod warunkiem zmiennej losowej Y nazywamy zmienną losową  $\mathbb{E}[X|Y]$  spełniającą dwa warunki:
  - $\overline{I \mathbb{E}[X|Y](\omega)} = m(Y(\omega))$  dla pewnej borelowskiej funkcji m,
  - II  $\mathbb{E}[X \mathbb{1}_{Y \in B}] = \mathbb{E}[\mathbb{E}[X|Y] \mathbb{1}_{Y \in B}]$  dla każdego  $B \in \mathcal{B}(\mathbb{R})$ .
  - lacktriangled Dla  $A \in \mathcal{F}$  oznaczmy  $\mathbb{P}(A|Y) = \mathbb{E}[\mathbb{1}_A|Y]$ .
- (13.10) **TW.** Jeśli  $\mathbb{E}[|X|] < \infty$ , to  $\mathbb{E}[X|Y]$  istnieje. Ponadto, jest ona wyznaczona jednoznacznie z dokładnościa do zbiorów miary  $\mathbb{P}$  0, tzn. jeśli Z również spełnia warunki definicji, czyli:
  - $Z(\omega) = m(Y(\omega)),$
  - $\mathbb{E}[X\mathbb{1}_{Y\in B}] = \mathbb{E}[Z\mathbb{1}_{Y\in B}]$  dla każdego  $B\in\mathcal{B}(\mathbb{R})$ ,

to  $\mathbb{P}(Z \neq \mathbb{E}[X|Y]) = 0$ .

- (13.11) Niech X będzie całkowalną zmienną losową.
  - Warunkową wartością oczekiwaną zmiennej losowej X pod warunkiem zdarzenia  $\{Y = y\}$  dla  $y \in \text{supp}(X)$ , nazywamy wielkość

$$\mathbb{E}[X|Y=y] = m(y),$$

gdzie funkcja m jest funkcja z definicji  $\mathbb{E}[X|Y]$ , tzn.  $\mathbb{E}[X|Y] = m(Y)$ .

lacktriangle Ponieważ  $\mathbb{E}[X|Y]$  zawsze istnieje (o ile  $\mathbb{E}[|X|] < \infty$ ), to funkcja  $y \mapsto \mathbb{E}[X|Y=y]$  jest dobrze określona. Nawet wtedy, gdy  $\mathbb{P}(Y=y)=0$ !

**A** Jeśli  $\mathbb{P}(Y=y) > 0$ , to powyższa definicja pokrywa się z Definicja (13.1).

 $\blacksquare$  Warunkowym prawdopodobieństwem zdarzenia  $A \in \mathcal{F}$  pod warunkiem zdarzenia  $\{Y = y\}$  nazywamy

$$\mathbb{P}(A|Y=y) := \mathbb{E}[\mathbb{1}_A|Y=y].$$

(13.12) Kontynuacja przykładu (13.6). Szukamy rozkładu warunkowego X pod warunkiem  $\{Y = y\}$ . Spodziewamy się, że X|Y = y powinien mieć rozkład jednostajny  $U([y, 2]), y \in [0, 2]$ . Pokażemy najpierw, że

$$\mathbb{E}[\mathbb{1}_{X \le t} | Y] = \begin{cases} 0, & t < Y, \\ \frac{t - Y}{2 - Y}, & Y \le t < 2, \\ 1, & t \ge 2. \end{cases}$$

Warunek I definicji  $\mathbb{E}[\mathbbm{1}_{X < t} | Y]$  jest oczywiście spełniony. Warunek II jest spełniony jeśli

$$\mathbb{E}[\mathbbm{1}_{X \leq t} \mathbbm{1}_{Y \in B}] = \mathbb{E}\left[\frac{t-Y}{2-Y} \mathbbm{1}_{Y \leq t < 2} \mathbbm{1}_{Y \in B}\right] + \mathbb{E}[\mathbbm{1}_{t \geq 2} \mathbbm{1}_{Y \in B}].$$

Lewa strona wynosi dla  $t \in [0, 2)$  wynosi

$$\begin{split} \int_{B} \int_{-\infty}^{t} f_{(X,Y)}(x,y) dx \, dy &= \frac{1}{2} \int_{B} \int_{-\infty}^{t} \mathbb{1}_{0 \le y \le x \le 2} dx \, dy = \frac{1}{2} \int_{B \cap [0,t]} \int_{y}^{t} dx \, dy \\ &= \frac{1}{2} \int_{B \cap [0,t]} (t-y) dy. \end{split}$$

Z kolei z prawej strony mamy dla  $t \in [0, 2)$ ,

$$\mathbb{E}\left[\frac{t-Y}{2-Y}\mathbbm{1}_{Y \leq t}\mathbbm{1}_{Y \in B}\right] = \int_{B \cap (-\infty,t]} \frac{t-y}{2-y} f_Y(y) dy = \int_{B \cap (-\infty,t]} \frac{t-y}{2-y} \frac{2-y}{2} \mathbbm{1}_{[0,2]}(y) dy = \frac{1}{2} \int_{B \cap [0,t]} (t-y) dy.$$

Podobnie postępujemy dla t>2 i otrzymujemy tożsamość  $\mathbb{E}[\mathbbm{1}_{Y\in B}]=\mathbb{E}[\mathbbm{1}_{Y\in B}]$ . Z kolei dla t<0 mamy 0=0. Ale  $\mathbb{E}[\mathbbm{1}_{X\leq t}|Y]=\mathbb{P}(X\leq t|Y)$ . Oznacza to, że dystrybuanta warunkowa X pod warunkiem zdarzenia  $\{Y=y\}$  dana jest przez

$$F_{X|Y=y}(t) := \mathbb{P}(X \le t | Y = y) = \begin{cases} 0, & t < y, \\ \frac{t-y}{2-y}, & y \le t < 2, \\ 1, & t \ge 2. \end{cases}$$

czyli rzeczywiście  $X|Y=y\sim \mathrm{U}([y,2]),\,y\in[0,2].$ 

- 14. W14 Warunkowa wartość oczekiwana ciąg dalszy
- <span id="page-32-0"></span>(14.1) Przypomnienie:
  - $\blacksquare$  Niech Y będzie zmienną losową. Jeśli  $\mathbb{E}[|X|] < \infty$ , to warunkową wartością oczekiwaną X pod warunkiem zmiennej losowej Y nazywamy zmienną losową  $\mathbb{E}[X|Y]$  spełniającą dwa warunki:
    - I  $\mathbb{E}[X|Y](\omega) = m(Y(\omega))$  dla pewnej borelowskiej funkcji m,

II  $\mathbb{E}[X\mathbb{1}_{Y\in B}] = \mathbb{E}[\mathbb{E}[X|Y]\mathbb{1}_{Y\in B}]$  dla każdego  $B\in\mathcal{B}(\mathbb{R})$ .

f A Zmienną losową  $\mathbb{E}[X|Y]$  interpretujemy jako średnią wartość X pod warunkiem znajomości (losowej) wartości Y.

- (14.2)  $\triangle$  Pojęcie WWO pod warunkiem Y naturalnie uogólnia sie na przypadek, gdy Y jest wektorem losowym (nwymiarowym,  $n \in \mathbb{N}$ ). W warunku II wystarczy zastąpić  $B \in \mathcal{B}(R)$  przez  $B \in \mathcal{B}(R^n)$ .
  - lacktriangle Jeśli  $Y = (Y_1, \dots, Y_n)$ , to  $\mathbb{E}[X|Y_1, \dots, Y_n] := \mathbb{E}[X|Y]$ .
- (14.3) **TW.** Własności WWO. Niech  $\mathbb{E}[|X|] < \infty$ .
  - (a) Jeśli X = f(Y) dla pewnej funkcji borelowskiej f, to  $\mathbb{E}[X|Y] = X$ .
  - (b) Jeśli  $\mathbb{P}(Y=c)=1$  dla pewnego  $c\in\mathbb{R}$ , to  $\mathbb{E}[X|Y]=\mathbb{E}[X]$ .
  - (c) Jeśli f jest borelowska i różnowartościowa (na supp(Y)), to  $\mathbb{E}[X|f(Y)] = \mathbb{E}[X|Y]$ .
  - (d) Jeśli f jest funkcją borelowską, to  $\mathbb{E}[\mathbb{E}[X|Y, f(X,Y,Z)]|Y] = \mathbb{E}[X|Y]$ .
  - (e) Jeśli f jest funkcją borelowską, to  $\mathbb{E}[\mathbb{E}[X|f(Y)]|Y] = \mathbb{E}[X|f(Y)]$ .
  - (f)  $\mathbb{E}[\mathbb{E}[X|Y]] = \mathbb{E}[X]$ .
  - (g) Jeśli Y = f(Z) dla pewnej borelowskiej funkcji f oraz  $\mathbb{E}[|XY|] < \infty$ , to  $\mathbb{E}[XY|Z] = Y\mathbb{E}[X|Z]$ .
  - (h) Jeśli X oraz Y są niezależne, to  $\mathbb{E}[X|Y] = \mathbb{E}[X]$ .

Szkic dowodu:

- (a) X spełnia warunki I i II definicji WWO.
- (b) Z warunku I,  $\mathbb{E}[X|Y]$  jest stałą.
- (c) Z różnowartościwości mamy  $\{y \colon y \in B\} = \{y \colon f(y) \in f(B)\}$ . Zdefiniujmy  $Z(\omega) = \mathbb{E}[X|f(Y)](\omega)$ . Warunek I jest trywialnie spełniony. Sprawdzamy warunek II: dla  $B \in \mathcal{B}(\mathbb{R})$ ,

$$\mathbb{E}[Z\mathbb{1}_{Y\in B}] = \mathbb{E}[Z\mathbb{1}_{f(Y)\in f(B)}] = \mathbb{E}[X\mathbb{1}_{f(Y)\in f(B)}] = \mathbb{E}[X\mathbb{1}_{Y\in B}].$$

(d) Dla każdego  $B \in \mathcal{B}(\mathbb{R})$  mamy

$$\begin{split} \mathbb{E}[\mathbb{E}[X|Y]\mathbb{1}_{Y\in B}] &= \mathbb{E}[X\mathbb{1}_{Y\in B}] = \mathbb{E}[X\mathbb{1}_{(Y,f(X,Y,Z)\in B\times \mathbb{R}]} \\ &= \mathbb{E}[\mathbb{E}[X|Y,f(X,Y,Z)]\mathbb{1}_{Y\in B}] = \mathbb{E}\left[\mathbb{E}[\mathbb{E}[X|Y,f(X,Y,Z)]|Y]\mathbb{1}_{Y\in B}\right], \end{split}$$

gdzie każda z nierówności wynika z II.

- (e) Wynika z (a), ponieważ  $\mathbb{E}[X|f(Y)]$  jest funkcją Y.
- (f) Weźmy  $B = \mathbb{R}$  w II.
- (g) Wystarczy sprawdzić dla  $Y = \mathbb{1}_{Z \in B}$ ,  $B \in \mathcal{B}(\mathbb{R})$ . Dowolną zmienną losową Y aproksymujemy przez funkcje proste. Dla  $A \in \mathcal{B}(\mathbb{R})$  mamy

$$\mathbb{E}[\mathbb{E}[XY|Z]\mathbbm{1}_{Z\in A}] \stackrel{\text{II}}{=} \mathbb{E}[XY\mathbbm{1}_{Z\in A}] = \mathbb{E}[X\mathbbm{1}_{Z\in B}\mathbbm{1}_{Z\in A}] = \mathbb{E}[X\mathbbm{1}_{Z\in A\cap B}] \stackrel{\text{II}}{=} \mathbb{E}[\mathbb{E}[X|Z]\mathbbm{1}_{Z\in A\cap B}] = \mathbb{E}[Y\mathbb{E}[X|Z]\mathbbm{1}_{Z\in A}],$$
ponieważ  $A\cap B\in \mathcal{B}(\mathbb{R}).$ 

(h) Dla każdego  $B \in \mathcal{B}(\mathbb{R})$  mamy

$$\mathbb{E}[\mathbb{E}[X|Y]\mathbbm{1}_{Y\in B}] \stackrel{\text{II}}{=} \mathbb{E}[X\mathbbm{1}_{Y\in B}] \stackrel{\text{nzl}}{=} \mathbb{E}[X]\mathbb{E}[\mathbbm{1}_{Y\in B}] = \mathbb{E}[\mathbb{E}[X]\mathbbm{1}_{Y\in B}].$$

- (14.4)  $\mathfrak{A}^{\sharp}$  Niech  $\Omega = [-1,1], \, \mathcal{F} = \mathcal{B}([-1,1]), \, \mathbb{P} = \lambda_1/2$  oraz  $Y(\omega) = |\omega|$ . Znajdź  $\mathbb{E}[X|Y]$ . Oczywiście z warunku I mamy  $\mathbb{E}[X|Y](\omega) = m(Y(\omega)) = m(|\omega|)$ .
- (14.5) **TW.** Rozważmy tzw. zagadnienie prognozy. Przewidujemy nieobserwowany Y na podstawie obserwowanego X. Załóżmy, że  $\mathbb{E}[Y^2] < \infty$ . Szukamy takiej funkcji borelowskiej  $h^*$  dla której

$$\mathbb{E}[(Y - h^*(X))^2] = \inf_{h \text{-borelowska}} \mathbb{E}[(Y - h(X))^2].$$

Okazuje się, że  $h^*(x) = \mathbb{E}[Y|X=x]$ .

Szkic dowodu: Niech  $h_0(x) = \mathbb{E}[Y|X=x]$ . Wtedy

$$\mathbb{E}[(Y - h(X))^2] = \mathbb{E}[(Y - h_0(X) + h_0(X) - h(X))^2]$$
  
=  $\mathbb{E}[(Y - h_0(X))^2] + \mathbb{E}[(h_0(X) - h(X))^2] + 2\mathbb{E}[(Y - h_0(X))(h_0(X) - h(X))].$ 

Ale z własności (a), (f) i (g) z poprzedniego Twierdzenia mamy

$$\mathbb{E}[(Y - h_0(X))(h_0(X) - h(X))] = \mathbb{E}[\mathbb{E}[(Y - h_0(X))(h_0(X) - h(X))|X]]$$
$$= \mathbb{E}[(\mathbb{E}[Y|X] - h_0(X))(h_0(X) - h(X))] = 0.$$

Zatem  $\mathbb{E}[(Y - h(X))^2] = \mathbb{E}[(Y - h_0(X))^2] + \mathbb{E}[(h_0(X) - h(X))^2]$  oraz infimum po funkcjach borelowskich h jest osiągane dla  $h^* = h_0$ .

(14.6)  $\triangle$  Powyższe Twierdzenie można traktować jako definicję  $\mathbb{E}[Y|X]$  w sytuacji, gdy wiemy że  $\mathbb{E}[Y^2] < \infty$ .

(14.7) **LEM.** (Użyteczny sposób liczenia WWO dla rozkładów absolutnie ciągłych) Jeśli (X, Y) ma rozkład o gęstości  $f_{(X,Y)}$ , to warunkowy rozkład X pod warunkiem  $\{Y=y\}$  również ma gęstość. Jest ona dana wzorem

$$f_{X|Y=y}(x) = \begin{cases} \frac{f_{(X,Y)}(x,y)}{f_Y(y)}, & f_Y(y) > 0, \\ 0, & f_Y(y) = 0. \end{cases}$$

Wtedy dla  $y \in \text{supp}(Y)$  mamy

$$\mathbb{P}(X \in A|Y = y) = \int_{A} f_{X|Y=y}(x)dx$$

lub ogólniej dla dowolnej funkcji borelowskiej h,

$$\mathbb{E}[h(X)|Y=y] = \int_{\mathbb{R}} h(x) f_{X|Y=y}(x) dx.$$

Szkic dowodu: Musimy pokazać, że dla

$$m(y) = \int_{\mathbb{R}} h(x) f_{X|Y=y}(x) dx,$$

zachodzi warunek II, czyli

(\*) 
$$\mathbb{E}[h(X)\mathbb{1}_{Y\in B}] = \mathbb{E}[m(Y)\mathbb{1}_{Y\in B}], \qquad \forall B \in \mathcal{B}(\mathbb{R}).$$

Ponieważ wektor (X,Y) ma gęstość, to równość (\*) jest równoważna

$$\int_{B} \int_{\mathbb{R}} h(x) f_{(X,Y)}(x,y) dx dy = \int_{B} m(y) f_{Y}(y) dy.$$

Ale  $f_{X|Y=y}(x)f_Y(y) = f_{X,Y}(x,y)$  oraz

$$\int_B m(y)f_Y(y)dy = \int_B \int_{\mathbb{R}} h(x)f_{X|Y=y}(x)dx f_Y(y)dy = \int_B \int_{\mathbb{R}} h(x)f_{(X,Y)}(x,y)dx dy.$$

- (14.8)  $\triangle$  Jeśli znajdziemy  $\mathbb{E}[h(X)|Y=y]$  z powyższego wzoru oraz wiemy, że  $\mathbb{E}[|h(X)|]<\infty$ , to E[h(X)|Y] dostajemy poprzez podstawienie Y w miejsce y.
- (14.9) Which  $f_{(X,Y)}(x,y) = \frac{1}{y^3} \mathbb{1}_{x>0,y\geq \max\{1,x\}}$ . Which  $f_{Y}(y) = \frac{1}{y^2} \mathbb{1}_{y\geq 1}$  orazidla  $y \in \text{supp}(Y) = [1,\infty), X|Y = y \sim U([0,y])$  oraz  $\mathbb{E}[X|Y = y] = y/2$ . Zatem  $\mathbb{E}[X|Y] = Y/2$ .
- (14.10) Niech  $(X,Y) \sim N_2(\underline{m},\Sigma)$ , gdzie  $\underline{m} = (m_1,m_2)^\top = (\mathbb{E}[X],\mathbb{E}[Y])^\top$  oraz

$$\Sigma = \begin{pmatrix} \operatorname{Var}[X] & \operatorname{Cov}[X,Y] \\ \operatorname{Cov}[X,Y] & \operatorname{Var}[Y] \end{pmatrix} = \begin{pmatrix} \sigma_X^2 & \rho \, \sigma_X \sigma_Y \\ \rho \, \sigma_X \sigma_Y & \sigma_Y^2 \end{pmatrix}.$$

Wtedy dla  $y \in \mathbb{R}$ ,

$$X|Y = y \sim N\left(m_1 + \rho \frac{\sigma_X}{\sigma_Y}(y - m_2), (1 - \rho^2)\sigma_X^2\right),$$

tzn. warunkowe rozkłady wektora normalnego również są normalne.

- (14.11) **©**\*Ogólniejsza definicja WWO.
  - B Rozważmy przestrzeń probabilistyczną  $(\Omega, \mathcal{F}, \mathbb{P})$  oraz  $\sigma$ -ciało  $\mathcal{G} \subset \mathcal{F}$ . Jeśli  $\mathbb{E}[|X|] < \infty$ , to warunkową wartością oczekiwaną X pod warunkiem  $\sigma$ -ciała  $\mathcal{G}$  nazywamy zmienną losową  $\mathbb{E}[X|\mathcal{G}]$  spełniającą dwa warunki:
    - I  $\mathbb{E}[X|\mathcal{G}]$  jest  $\mathcal{G}$ -mierzalna,
    - II  $\mathbb{E}[X\mathbb{1}_B] = \mathbb{E}[\mathbb{E}[X|\mathcal{G}]\mathbb{1}_B]$  dla każdego  $B \in \mathcal{G}$ .
    - $\blacksquare$   $\sigma$ -ciałem generowanym przez zmienną losową Y nazywamy rodzinę  $\sigma(Y) = \{Y^{-1}(B) : B \in \mathcal{B}(\mathbb{R})\}$ .  $\Theta$  Pokazać, że rodzina  $\{Y^{-1}(B) : B \in \mathcal{B}(\mathbb{R})\}$  jest  $\sigma$ -ciałem.
    - Można pokazać, że zmienna losowa Z jest  $\sigma(Y)$ -mierzalna wtedy i tylko wtedy, gdy  $Z(\omega) = m(Y(\omega))$  dla pewnej borelowskiej funkcji m.
    - Zatem, WWO pod warunkiem zmiennej losowej definiowana wcześniej to po prostu  $\mathbb{E}[X|Y] = \mathbb{E}[X|\sigma(Y)]$ .
    - $\mathbf{A}$  Ponieważ nie każde  $\sigma$ -ciało  $\mathcal{G}$  jest  $\sigma$ -ciałem generowanym przez jakąś zmienną losową, to powyższa definicja jest ogólniejsza.

#### 15. W15 - Co warto pamietać + uzupełnienia

- <span id="page-35-0"></span>(15.1) Święta czwórka:  $\sigma$ -ciało, prawdopodobieństwo  $\mathbb{P}$ , zmienna losowa X, rozkład  $\mathbb{P}_X$ .
- (15.2) Wzór włączeń i wyłączeń (W1), Wzór na prawdopodobienstwo całkowite (W2), Wzór Bayesa (W2).
- (15.3) Niezależność zdarzeń i zmiennych losowych, Lematy Borela-Cantellego (W3).
- (15.4) Wartość oczekiwana:
  - dla rozkładów dyskretnych.

Niech S będzie zbiorem przeliczalnym dla którego  $\sum_{k \in S} \mathbb{P}(X = k) = 1$  oraz  $\mathbb{P}(X = k) > 0$  dla każdego

- X ma rozkład typu dyskretnego,
- $-S = \operatorname{supp}(X),$
- $\begin{array}{l} \ \mathbb{E}[h(X)] = \sum_{k \in \mathrm{supp}(X)} h(k) \mathbb{P}(X=k). \\ \ \mathrm{Te \ same \ wzory \ zachodza, \ gdy} \ X \ \mathrm{jest \ wektorem \ losowym.} \end{array}$
- dla rozkładów absolutnie ciągłych.

Niech  $F_X$  będzie dystrybuantą zmiennej losowej X. Jeśli  $\int_{\mathbb{R}} F_X'(x) dx = 1$ , to

- -X ma rozkład typu absolutnie ciaglego,
- gęstość X to  $f_X = F_X'$ ,
- $-\mathbb{E}[h(X)] = \int_{\mathbb{R}} h(t) f_X(t) dt.$
- Dla wektorów losowych wymiaru n zamieniamy  $F_X'$  na  $\frac{\partial^n F}{\partial x_1...\partial x_n}$  i powyższe trzy punkty nadal są prawdziwe.
- dla rozkładow mieszanych dyskretno-absolutnie ciągłych: Niech  $NC(F_X) = \{t \in \mathbb{R} : \Delta F_X(t) > 0\}$ . Wtedy

$$\mathbb{E}[h(X)] = \sum_{t \in NC(F_X)} h(t) \cdot \Delta F_X(t) + \int_{\mathbb{R}} h(t) F_X'(t) dt,$$

gdzie  $\Delta F_X(t) := F_X(t) - F_X(t-) = \mathbb{P}(X=t)$ . Elementy  $NC(F_X)$  nazywane są czasem <u>atomami</u> rozkładu

• Dla ogolnych rozkładów: Jeśli  $h(t) = \int_{-\infty}^{t} h'(s)ds$ , to

$$\mathbb{E}[h(X)] = \int_{\mathbb{R}} h(x) \mathbb{P}_X(dx) = \int_{\mathbb{R}} h'(t) (1 - F_X(t)) dt.$$

Szkic dowodu:

$$\int_{\mathbb{R}} \int_{\mathbb{R}} \mathbbm{1}_{s < x} h'(s) \, ds \, \mathbb{P}_X(dx) = \int_{\mathbb{R}} h'(s) \int_{\mathbb{R}} \mathbbm{1}_{s < x} \, \mathbb{P}_X(dx) \, ds = \int_{\mathbb{R}} h'(s) \mathbb{P}_X((s, \infty)) \, ds.$$

(15.5) Warunkowa wartość oczekiwana:

Jeśli znamy rozkład warunkowy X pod warunkiem Y = y, to dla dowolnej funkcji borelowskiej h

$$\mathbb{E}[h(X)|Y=y] = \int_{\mathbb{D}} h(x) \mathbb{P}_{X|Y=y}(dx),$$

gdzie w zależności od typu rozkładu X|Y=y stosujemy jeden ze wzorów z poprzedniego punktu.

(15.6) Warunkowe rozkłady:

Żeby stosować poprzedni punkt, powinniśmy umieć znajdować rozkład warunkowy X|Y=y.

f A Znajomość rozkładu warunkowego Y|X oraz rozkładu X daje nam pełną informację odnośnie rozkładu łącznego: dla borelowskich zbiorów A i B mamy

$$\mathbb{P}(X \in A, Y \in B) = \mathbb{E}[\mathbb{1}_{X \in A} \mathbb{P}(Y \in B|X)].$$

Możemy wtedy też znaleźć rozkład warunkowy X|Y. Poniższe wzory można traktowac jako wersje wzoru Bayesa.

 $\bullet\,$  Jeśli wektor (X,Y)ma rozkład typu dyskretnego, to

$$\mathbb{P}(X=k|Y=n) = \frac{\mathbb{P}(X=k,Y=n)}{\mathbb{P}(Y=n)} = \frac{\mathbb{P}(Y=n|X=k)\mathbb{P}(X=k)}{\sum_{m}\mathbb{P}(Y=n|X=m)\mathbb{P}(X=m)}.$$

• Jeśli wektor (X,Y) ma rozkład typu absolutnie ciągłego, to

$$f_{X|Y=y}(x) = \frac{f_{(X,Y)}(x,y)}{f_Y(y)} = \frac{f_{Y|X=x}(y)f_X(x)}{\int_{\mathbb{R}} f_{Y|X=u}(y)f_X(u)du}.$$

• Jeśli rozkład X|Y=y jest typu dyskretnego, a Y absolutnie ciągly, to

$$\mathbb{P}(X = k | Y = y) = \frac{f_{Y|X=k}(y)\mathbb{P}(X = k)}{f_{Y}(y)} = \frac{f_{Y|X=k}(y)\mathbb{P}(X = k)}{\sum_{m} f_{Y|X=m}(y)\mathbb{P}(X = m)}.$$

 $\bullet\,$  Jeśli rozkład X|Y=kjest typu absolutnie ciągłego, a Yma rozkład dyskretny, to

$$f_{X|Y=k}(x) = \frac{\mathbb{P}(Y=k|X=x)f_X(x)}{\mathbb{P}(Y=k)} = \frac{\mathbb{P}(Y=k|X=x)f_X(x)}{\int_{\mathbb{P}} \mathbb{P}(Y=k|X=u)f_X(u)du}.$$

•  $\bullet$  Niech  $X \sim \mathrm{U}([0,1])$  oraz  $Y|X = x \sim \mathrm{b}(n,x)$ . Wtedy

$$f_{X|Y=k}(x) = \frac{\binom{n}{k} x^k (1-x)^{n-k} \mathbb{1}_{[0,1]}(x)}{\int_{\mathbb{R}} \binom{n}{k} u^k (1-u)^{n-k} \mathbb{1}_{[0,1]}(u) du} = \dots = C_{n,k} x^k (1-x)^{n-k} \mathbb{1}_{[0,1]}(x).$$

Jest to tzw. rozkład beta pierwszego rodzaju z parametrami  $k+1,\,n-k+1.$ 

(15.7) Zbieżności:  $\xrightarrow{1}$ ,  $\xrightarrow{\mathbb{P}}$ ,  $\xrightarrow{L_p}$ ,  $\xrightarrow{d}$  i zwiazki między nimi:

$$\begin{array}{ccc}
\stackrel{1}{\longrightarrow} & \Longrightarrow \stackrel{\mathbb{P}}{\longrightarrow}, \\
\stackrel{L_p}{\longrightarrow} & \Longrightarrow \stackrel{\mathbb{P}}{\longrightarrow}, \\
\stackrel{\mathbb{P}}{\longrightarrow} & \Longrightarrow \stackrel{d}{\longrightarrow}, \\
X_n \stackrel{d}{\longrightarrow} c & \Longrightarrow X_n \stackrel{\mathbb{P}}{\longrightarrow} c.
\end{array}$$

Pozostałe implikacje w ogólności nie zachodza.

(15.8) Twierdzenia graniczne:

• PWL: Jeśli  $(X_n)_n$  są i.i.d. oraz  $\mathbb{E}[|X_1|] < \infty$ , to (MPWL Kołmogorowa II)

$$\frac{\sum_{k=1}^{n} X_k}{n} \xrightarrow{1} \mathbb{E}[X_1].$$

• CTG: Jeśli  $(X_n)_n$  są i.i.d. oraz  $\mathbb{E}[X_1^2] < \infty$ , to

$$\sqrt{n} \left( \frac{\sum_{k=1}^{n} X_k}{n} - \mathbb{E}[X_1] \right) = \frac{\sum_{k=1}^{n} (X_k - \mathbb{E}[X_1])}{\sqrt{n}} \xrightarrow{d} Z \sim \mathcal{N}(0, \text{Var}(X)).$$

- Istnieją wersje obu powyższych twierdzeń, gdy  $(X_n)_n$  są (trochę) zależne oraz ich rozkłady (trochę) się różnią. Oczywiście istnieją też wersje, gdy zamiast ciągu zmiennych losowych rozważamy ciągi wektorów (wtedy mamy zbieżność do wielowymiarowego rozkładu normalnego).
- Na powyższych twierdzeniach granicznych opierają się (standardowe) metody Monte Carlo.
- Twierdzeniach graniczne mają olbrzymie znaczenie w statystyce.
- (15.9) Wielowymiarowy rozkład normalny:

Standardowo definiowany przez gęstość dla  $\mu \in \mathbb{R}^n$  oraz  $\Sigma \in \operatorname{Sym}_+(n)$ ,

$$f_{\underline{X}}(\underline{x}) = \frac{1}{(\sqrt{2\pi})^n \sqrt{\det \Sigma}} e^{-\frac{1}{2}(\underline{x} - \underline{\mu})^\top \cdot \Sigma^{-1} \cdot (\underline{x} - \underline{\mu})}, \qquad \underline{x} \in \mathbb{R}^n.$$

W szczególności dla n=2 mamy

$$f_{(X_1,X_2)}(x_1,x_2) = \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}} \exp\left\{-\frac{1}{2(1-\rho^2)} \left[ \frac{(x_1-m_1)^2}{\sigma_1^2} - 2\rho \frac{(x_1-m_1)(x_2-m_2)}{\sigma_1\sigma_2} + \frac{(x_2-m_2)^2}{\sigma_2^2} \right] \right\},$$

gdzie  $\Sigma = \begin{pmatrix} \sigma_1^2 & \rho \sigma_1 \sigma_2 \\ \rho \sigma_1 \sigma_2 & \sigma_2^2 \end{pmatrix}$  oraz  $\rho$  jest wspołczynnikiem korelacji zmiennych  $X_1$  i  $X_2$ .

Własności:

• rozkłady brzegowe są normalne: dla  $A \subset \{1, \ldots, n\}$ ,

$$\underline{X}_A := (X_i \colon i \in A) \sim \mathcal{N}_{|A|}(\mu_{A}, \Sigma_{AA}),$$

gdzie  $\underline{\mu}_A = (\mu_i : i \in A) \text{ oraz } \Sigma_{AA} = (\Sigma_{ij})_{i,j \in A}.$ 

• rozkłady warunkowe są normalne:

$$X|Y = y \sim N\left(m_1 + \rho \frac{\sigma_X}{\sigma_Y}(y - m_2), (1 - \rho^2)\sigma_X^2\right)$$

• Sumy niezależnych zmiennych losowych o rozkładach normalnych nadal mają rozkłady normalne. Fakt ten można uogólnić na przekształcenia afiniczne.

Załóżmy, że X ∼ Nn(µ, Σ). Niech Y = AX + B, gdzie A ∈ Mat(k, n) jest macierzą rzędu k ≤ n oraz B ∈ R k . Wtedy

$$\underline{Y} \sim N_k(A\mu + \underline{B}, A\Sigma A^{\top}).$$

• Wiemy, że jeśli X i Y są niezależne, to Cov(X, Y ) = 0 (o ile istnieje).

LEM. Załóżmy, że (X, Y ) ∼ N2. Jeśli Cov(X, Y ) = 0, to X i Y są niezależne.

Szkic dowodu: Łatwo widać z postaci gęstości dla n = 2.

3 Jeśli (X, Y ) ∼ N<sup>2</sup> oraz α = Cov(X, Y )/Var(X), to zmienne losowe

$$X$$
 oraz  $\tilde{Y} = Y - \alpha X$ 

są niezależne. Rzeczywiście, X Y˜ = X <sup>Y</sup> <sup>−</sup> αX = 1 0 −α 1 X Y , więc (X, Y˜ ) ma rozkład normalny. Ponadto,

$$Cov(X, Y - \alpha X) = Cov(X, Y) - \alpha Var(X) = 0.$$

- (15.10) Y Fakt, że X i Y są niezależne zwykle oznacza się przez X ⊥⊥ Y .
- (15.11) Warunkowa niezależność:

Przypomnijmy, że zmienne losowe X i Y są niezależne jeśli dla borelowskich zbiorów A i B mamy

$$\mathbb{P}(X \in A, Y \in B) = \mathbb{P}(X \in A)\mathbb{P}(Y \in B).$$

Jest to nie tylko własność pary (X, Y ), ale również prawdopodobieństwa P. Zamiast prawdopodobieństwa P możemy rozważać inne, w szczególności p-stwo warunkowe. Powiemy, że X i Y są warunkowo niezależne pod warunkiem zmiennej losowej Z, jeśli

$$\mathbb{P}(X \in A, Y \in B|Z) = \mathbb{P}(X \in A|Z)\,\mathbb{P}(Y \in B|Z).$$

Wiele twierdzeń (w tym twierdzenia graniczne) zachodzi "warunkowo", gdy zastąpimy zwykłą niezależność przez warunkową niezależność.

Projekt "NERW 2 PW. Nauka - Edukacja - Rozwój - Współpraca" współfinansowany ze środków Unii Europejskiej w ramach Europejskiego Funduszu Społecznego.

Zadanie 10 pn. "Modyfikacja programów studiów na kierunkach prowadzonych przez Wydział Matematyki i Nauk Informacyjnych", realizowane w ramach projektu "NERW 2 PW. Nauka - Edukacja - Rozwój - Współpraca", współfinansowanego jest ze środków Unii Europejskiej w ramach Europejskiego Funduszu Społecznego.

![](_page_37_Picture_21.jpeg)

![](_page_37_Picture_22.jpeg)

![](_page_37_Picture_24.jpeg)