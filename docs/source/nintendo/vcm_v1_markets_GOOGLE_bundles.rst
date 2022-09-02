/vcm/v1/markets/GOOGLE/bundles
===============================

- Base address: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
- Method: GET
- Status code: 200

Request headers
----------------

.. code-block:: text

    Authorization: Bearer eyJraWQiOiJhYjI2ODE1YS0yZjk0LTQ1NTUtOWQwMS0yYTk1OTg0OWJhM2QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiNWU5ZDU0YjE3NjZlZjJmIiwiYXVkIjoiYzZlNmUwNGFhYThjNjM1YSIsImlzcyI6Imh0dHBzOi8vNDhjYzgxY2RiOGRlMzBlMDYxOTI4ZjU2ZTliZDRiNGQuYmFhcy5uaW50ZW5kby5jb20iLCJ0eXAiOiJ0b2tlbiIsImJzOmdydCI6MiwiZXhwIjoxNjYxOTgzOTExLCJpYXQiOjE2NjE5ODMwMTEsImJzOmRpZCI6Ijc5MWIwOGE0M2UxNWIxMDIiLCJqdGkiOiJhYTM1YmUyMS00YmE1LTRjZTEtYTdmMi02ZTY5ZTM3NDhjODQifQ.nvf7sJObhX2C_R11Xs8fcLabZyjyWoCILOx1F6w_rDTDrwwEjXEEQG_jigpLSPQERuMt-PJPfaQJB0pTE2-Zaz4y0j08tY3_sVJzdyjz6q-rW4iVe3lKqRb2QKmDx3iZbH6G_2zWQebOYyOkrSJpXAcHd96ZQh-mC6wMH84g000e0u89cvaKfEFlqHsC6dA7Y_np7zGBi63rglJHXURPIEH79YqCScE_eBRXkkMUPoBxri_lqaK7ADtSkj1ur5Wj6vhf9-9_cVcWOirGwIg0Sn3wunxlTKoDt3uBhpGE4rWNm0NRtHk5Jw3EskEA_6vIJyZ4Fkc1NixmavzR729FgQ
    User-Agent: com.nintendo.zaga/2.19.0 ONEPLUS A6003/11 NPFSDK/Unity-2.33.0-0a4be7c8
    Accept-Language: en-US; q=1, en; q=0.5, *; q=0.001
    Host: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
    Connection: Keep-Alive
    Accept-Encoding: gzip

Request body
----------------

Empty

Response headers
----------------

.. code-block:: text

    Content-Type: application/json
    X-Cloud-Trace-Context: a4717690fe08fe6d01ac9b16da0351fa
    Date: Wed, 31 Aug 2022 21:57:51 GMT
    Server: Google Frontend
    Content-Length: 41736
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
    
Response
----------------

.. note:: 
    
    The following response contained repetitively long data which was trimmed. You can view the raw unabridged file `on GitHub. <https://raw.githubusercontent.com/SapiensAnatis/dragalia-api-docs/main/data_samples/bundles.json>`__

.. code-block:: javascript

    [
        {
            "virtualCurrencyName": "diamond",
            "market": "GOOGLE",
            "items": [
                {
                    "id": "41ba5c3fdc3d110b",
                    "virtualCurrencyName": "diamond",
                    "amount": 384,
                    "extraAmount": 116,
                    "sku": "com.nintendo.zaga.2019.newyearpack1.tier8",
                    "usdPrice": 7.99,
                    "price": 7.99,
                    "priceCode": "USD",
                    "title": "",
                    "detail": null,
                    "disabled": false,
                    "eventNotifyStartAt": 1,
                    "customAttribute": null
                },
                // --- array trimmed ---
            ],
            "market": "GOOGLE",
            "virtualCurrencyName": "diamond"
        }
    ]


Notes
------

- Write down any remarks or comments here