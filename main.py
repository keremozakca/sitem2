import time


min = int(input("Kurulacak dakika değeri : "))
sec = int(input("Kurulacak saniye değeri : "))

if sec == 0:
  print(min,":",sec)
  time.sleep(1)
  sec = 59
  min -= 1

while True:

  print(min,":",sec)
  sec -= 1
  time.sleep(1)
  if sec == 0:
    print(min,":",sec)
    time.sleep(1)
    sec += 59
    min -= 1
  if min == 0 and sec == 1:
    print(min,":",sec)
    time.sleep(1)
    sec = 0
    print(min,":",sec)
    break  

