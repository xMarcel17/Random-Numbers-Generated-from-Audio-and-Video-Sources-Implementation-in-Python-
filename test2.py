import cv2
import numpy as np

# Wczytanie filmu
cap = cv2.VideoCapture('Kanye_West_-_Gotcha.mp4')

# Pobranie pierwszej klatki
ret, frame1 = cap.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

# Utworzenie obiektu do przechowywania wartości półwariancji
variances = []

while True:
    # Pobranie kolejnej klatki
    ret, frame2 = cap.read()
    if not ret:
        break
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    # Obliczenie różnicy między klatkami
    diff = cv2.absdiff(frame1_gray, frame2_gray)
    
    # Obliczenie półwariancji
    variance = np.var(diff)
    
    # Dodanie wartości półwariancji do listy
    variances.append(variance)
    
    # Aktualizacja klatki referencyjnej
    frame1_gray = frame2_gray

    # Wyrzucenie pierwszej klatki z pamięci, jeśli mamy już 3 klatki
    if len(variances) > 3:
        variances.pop(0)
    
    # Jeśli mamy już zebrane 3 klatki, porównaj zmiany
    if len(variances) == 3:
        # Obliczenie różnicy między pierwszą a drugą klatką
        diff1 = np.abs(cv2.subtract(frame1_gray, frame2_gray))
        # Obliczenie różnicy między drugą a trzecią klatką
        diff2 = np.abs(cv2.subtract(frame2_gray, frame1_gray))
        # Obliczenie półwariancji różnic między klatkami
        variance_diff1 = np.var(diff1)
        variance_diff2 = np.var(diff2)
        # Wyświetlenie wyników
        print("Variance between frame 1 and frame 2:", variance_diff1)
        print("Variance between frame 2 and frame 3:", variance_diff2)
        
# Zwolnienie zasobów
cap.release()
cv2.destroyAllWindows()