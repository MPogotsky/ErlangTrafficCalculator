# ErlangTrafficCalculator
Program do wyznaczania współczynnika blokady w systemach ze stratami zgłoszeń opisanych modelem Erlanga.

# Podstawowe pojęcia
**Model Erlanga** - model stochnistyczny stosowany do analizy ruchu w systemach kolejkowych.
Model pozwala oszacowa prawdopodobieństwo(lub współczynnik) blokady, sytuacji, gdy klient nie może być obsłużony przy danych parametrach modelu.

W programie jest używany podstawowy model Elranga (model B).

## Model Erlanga B
Model Erlanga B, znana również jako formuła straty Erlanga. Jest to najprostszy model, w którym zakłada się, że w momencie blokady żądanie klienta jest anulowane, dzięki czemu nie tworzy się kolejka. Wciąż jednak klient ten może losowo generować dalsze żądania.

Dla obliszenia współczynnika blokady w programie jest wykorzystywany wzor rekurencyjny:

![image](https://user-images.githubusercontent.com/60144533/140714471-1c885024-bb55-4d85-b664-98b58b41cb62.png)

Gdzie:
* P(A,N) - prawdopodobieństwo blokady
* A - jest liczbą reprezentująca średnią wartość ruchu (w erlangach). 
* N - jest ilością kanałów.

# Założenia modelu
* Niezależne generowanie żądań przez źródła (abonenci nie decydują, że będą razem dzwonić o ustalonej porze),
* Czas obsługi żądania (n.p. rozmowy telefonicznej) ma rozkład wykładniczy,
* Obsługa ma charakter FIFO (First In First Out) – żądania obsługuje się w kolejności ich przychodzenia.
