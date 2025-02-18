UNOFFICIAL ARABAM.COM API

Quick Start
-----------
Python dosyasini projenin icine surukleyip asagidaki sekilde baska dosya icerisinden kullanabilirsiniz

.. code-block:: python

    from arabamapi import arabamcom

    araba = arabamcom.arabacek("https://www.arabam.com/ilan/galeriden-satilik-hyundai-accent-1-3-ls/1998-hyundai-accent-1-3-ls/27892288")
    print(araba)#verilen linkteki aracin tum ozelliklerini dondurur
    
    print(dict(arabamcom.sayfacek("https://www.arabam.com/ikinci-el/otomobil?page=2")[0]).get("fiyat")) #2. sayfanin 1. ilanindaki aracin fiyatini yazdirir
