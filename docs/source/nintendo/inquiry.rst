/inquiry/v1/users/b5e9d54b1766ef2f
===================================

- Base address: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
- Method: GET
- Status code: 200

Request headers
----------------

.. code-block:: text

    Authorization: Bearer eyJraWQiOiJhYjI2ODE1YS0yZjk0LTQ1NTUtOWQwMS0yYTk1OTg0OWJhM2QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiNWU5ZDU0YjE3NjZlZjJmIiwiYXVkIjoiYzZlNmUwNGFhYThjNjM1YSIsImlzcyI6Imh0dHBzOi8vNDhjYzgxY2RiOGRlMzBlMDYxOTI4ZjU2ZTliZDRiNGQuYmFhcy5uaW50ZW5kby5jb20iLCJ0eXAiOiJ0b2tlbiIsImJzOmdydCI6MiwiZXhwIjoxNjYxOTgwMjEzLCJpYXQiOjE2NjE5NzkzMTMsImJzOmRpZCI6Ijc5MWIwOGE0M2UxNWIxMDIiLCJqdGkiOiJjZjViYWFiMi0yYWFkLTQ0ZjYtYjcxNC04YjFlZmJkYmVkN2UifQ.BbNpqbKIQhAty8pMPKMAdo3vB3OzNRRtdm_QvrMAx_ZWfoUVe1G97gz5PW4unAmhlBK0lrzFLAsFHh0emEMhlqrw2ZT7OJDIH4rf11nSwXLiJ3JfZLGa7fr6UeNz2Ji8XtvNfLIjDgtP0075EaKFapvM3SwN4HyZ9i7wCHNFdq-EIrVNkNe63Eht_XIjSuDP3kHlm2oMw2Q6UgxP9oeyCLzS-IYruzODJjiHO0EByyHl_wnBVBeAkKOgGBKLb1SPYpoWFhDYYyG2giNhtCrGZD3E39JokS7nOO1J4uXWZ1h_BPOBwNCs9fvcW_XyvkarMiHC_-PldBaRdCLyrIjEfQ
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
    X-Cloud-Trace-Context: 4d0231fadc87bb7b782550dba1e0fd24
    Date: Wed, 31 Aug 2022 20:55:16 GMT
    Server: Google Frontend
    Content-Length: 70
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"

Response
----------------

.. code-block:: json

    {
        "hasUnreadCsComment": false,
        "updatedAt": 0,
        "userId": "b5e9d54b1766ef2f"
    }

Notes
------

- The endpoint itself is dynamic based on the user ID, fetched from :doc:`/nintendo/login`