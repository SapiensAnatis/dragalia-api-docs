bigdata/v1/analytics/events/config
===
Request headers
---
.. code-block:: text

Authorization: Bearer <accessToken>
User-Agent: com.nintendo.zaga/2.19.0 ONEPLUS A6003/11 NPFSDK/Unity-2.33.0-0a4be7c8
Accept-Language: en-US; q=1, en; q=0.5, *; q=0.001
Host: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
Connection: Keep-Alive
Accept-Encoding: gzip

Request body
---
Empty

Response headers
---
.. code-block:: text
Content-Type: application/json
X-Cloud-Trace-Context: ddd6b5b0888a3429f69131915ff5fc96
Date: Wed, 31 Aug 2022 19:24:49 GMT
Server: Google Frontend
Content-Length: 1282
Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"

Response body
---
.. code-block:: json
{
    "accessToken": "ya29.c.b0AXv0zTMjOSxhtUjp1uo2c9BXG61fnoofVTi_KS4dEa5oKpaVjthJcgR_6qjG0QuMPPZlYlm-rsrlTtl_aTdAQFcC_I7P_C31TfJ0XMZX_0wSANNmTccTRk9WMYcGVjKf0k5qw7jNRXF-H9lbWMuoah-TX6rjVuBRnH-M_dlrm1ssTFoErRwy1WxIiT-1QIzmc8r13L8bqtTthA1urlRxBhaqM6BSNxo........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................",
    "applicationId": "c6e6e04aaa8c635a",
    "city": "earley",
    "country": "GB",
    "expirationTime": 1661976589062,
    "immediateReporting": true,
    "mode": "V2",
    "region": "eng",
    "reportingPeriod": 60000,
    "topic": "projects/npf-baas-prod-gluon/topics/analytics-event-v02"
}