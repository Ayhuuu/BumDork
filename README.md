# Ayhuuu
kullanım: cyberDork.py [-h] [-d DORK] [-n NUM_RESULTS] [-o DOSYA ADI] [-c [CHECK_RESULT]]

isteğe bağlı argümanlar: -h, --help

-d DORK, --dork DORK Dork terimlerinizi bir boşlukla ayırarak tırnak içine alın. Ör: "intext:@gmail.com dosya türü:log"

-n NUM_RESULTS, --num_results NUM_RESULTS  sonuç sayısını girin. Varsayılan: 10. Google, sonuçları sorgu başına maksimum 100 ile sınırlayacaktır.

-o DOSYAADI, --output DOSYAADI Sonuçları belirtilen dosyaya çıkar

-c [CHECK_RESULT], --check_result [CHECK_RESULT] HTTP 200 yanıt kodu için bağlantı sonucunu kontrol edin

Kullanım Örnekleri:

python3 cyberDork.py -d "intitle:webcamXP inurl:8080" -n 20 -c
python3 cyberDork.py -d "intitle:index of / P intext:index of /" -n 20 -c
python3 cyberDork.py -d "intext: filetype.txt'ye izin ver" -n 20 -c

