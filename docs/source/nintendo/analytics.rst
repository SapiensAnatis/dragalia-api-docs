/bigdata/v1/analytics/events
=============================

- Base address: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
- Method: POST
- Status code: 202

Request headers
----------------

.. code-block:: text

    Content-Type: application/json
    Authorization: Bearer eyJraWQiOiJhYjI2ODE1YS0yZjk0LTQ1NTUtOWQwMS0yYTk1OTg0OWJhM2QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiNWU5ZDU0YjE3NjZlZjJmIiwiYXVkIjoiYzZlNmUwNGFhYThjNjM1YSIsImlzcyI6Imh0dHBzOi8vNDhjYzgxY2RiOGRlMzBlMDYxOTI4ZjU2ZTliZDRiNGQuYmFhcy5uaW50ZW5kby5jb20iLCJ0eXAiOiJ0b2tlbiIsImJzOmdydCI6MiwiZXhwIjoxNjYxOTc0Nzg4LCJpYXQiOjE2NjE5NzM4ODgsImJzOmRpZCI6Ijc5MWIwOGE0M2UxNWIxMDIiLCJqdGkiOiI2NjJhNzg0Mi00MDRmLTQ5NjctYmQyZi01ZjNjZGUwZDkxNzYifQ.oCNoTl3beHhGEz6dmP97RY2yXeymKPkhKNAIPVkXOAaVNgGtwgja-2xl80t1WlMv81k_EEw4r8VkCEg29kwdHjvk43Sc2hmzp1BBS9iJ1J0WW895nJqb4dyOXYAMgu8TdmuegS_Flf4KtVXAEbxQfA5_kl-t9yinp49BmXUTkp7HoP7Hb7pNXSMKmeFehF6XQYpbBqv1XeaK30Rz4QFIogeFoHx2fR78nrNKmd51RaTUQhLH9YnzwtXoOu6VjNz569qKzaxX9bwc3750HZtn1-uSk1hNGxmJlL2tEtLAKTnbjzGDFTyvPr-3pFtQAb1xRrye6Z-cek7MQiDpp0xiTg
    Content-Encoding: gzip
    User-Agent: com.nintendo.zaga/2.19.0 ONEPLUS A6003/11 NPFSDK/Unity-2.33.0-0a4be7c8
    Accept-Language: en-US; q=1, en; q=0.5, *; q=0.001
    Host: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
    Connection: Keep-Alive
    Accept-Encoding: gzip
    Content-Length: 450

Request body
----------------

.. code-block:: json

    [
        {
            "cacheInfo": {
                "appVersion": "2.19.0",
                "carrier": "giffgaff",
                "deviceAnalyticsId": "a2J1YmFhYWFERG1NamZtckpNTmVqSHZ6UGJWUE9FUwA=",
                "deviceName": "ONEPLUS A6003",
                "locale": "en-US",
                "manufacturer": "OnePlus",
                "networkType": "wifi",
                "osType": "Android",
                "osVersion": "11",
                "sdkVersion": "Unity-2.33.0-0a4be7c8",
                "sessionId": "791b08a43e15b102-1661973890238",
                "timeZone": "Europe/London",
                "timeZoneOffset": 3600000
            },
            "deviceAccount": "791b08a43e15b102",
            "eventCategory": "NPFCOMMON",
            "eventId": "SESSION",
            "eventTimestamp": 1661973890238,
            "market": "GOOGLE",
            "payload": {
                "action": "start",
                "duration": 0
            },
            "userId": "b5e9d54b1766ef2f"
        },
        {
            "cacheInfo": {
                "appVersion": "2.19.0",
                "carrier": "giffgaff",
                "deviceAnalyticsId": "a2J1YmFhYWFERG1NamZtckpNTmVqSHZ6UGJWUE9FUwA=",
                "deviceName": "ONEPLUS A6003",
                "locale": "en-US",
                "manufacturer": "OnePlus",
                "networkType": "wifi",
                "osType": "Android",
                "osVersion": "11",
                "sdkVersion": "Unity-2.33.0-0a4be7c8",
                "sessionId": "791b08a43e15b102-1661973592306",
                "timeZone": "Europe/London",
                "timeZoneOffset": 3600000
            },
            "deviceAccount": "791b08a43e15b102",
            "eventCategory": "NPFCOMMON",
            "eventId": "SESSION",
            "eventTimestamp": 1661973622564,
            "market": "GOOGLE",
            "payload": {
                "action": "pause",
                "duration": 30258
            },
            "userId": "b5e9d54b1766ef2f"
        }
    ]

Response headers
----------------

.. code-block:: text

    X-Cloud-Trace-Context: 86a9c5054b9f6fd49ca8462bf60c924f;o=1
    Date: Wed, 31 Aug 2022 19:24:49 GMT
    Content-Type: text/html
    Server: Google Frontend
    Content-Length: 0
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"

Response
----------------

Empty

Notes:
---------
