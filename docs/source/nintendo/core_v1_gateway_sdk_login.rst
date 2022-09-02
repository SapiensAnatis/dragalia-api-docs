/core/v1/gateway/sdk/login
==============================

- Base address: https://48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

    Content-Type: application/json
    User-Agent: com.nintendo.zaga/2.19.0 ONEPLUS A6003/11 NPFSDK/Unity-2.33.0-0a4be7c8
    Accept-Language: en-US; q=1, en; q=0.5, *; q=0.001
    Host: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
    Connection: Keep-Alive
    Accept-Encoding: gzip
    Content-Length: 714

Request body
----------------

.. code-block:: json

    {
        "appVersion": "2.19.0",
        "assertion": "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjb20ubmludGVuZG8uemFnYTowYzNkNzg5ZjVlZDIzZjJiMzRjNzk2NjBhMzcxOTBkMWM4NzNhM2YyIiwiaWF0IjoxNjYxOTczODg5LCJhdWQiOiJodHRwczpcL1wvNDhjYzgxY2RiOGRlMzBlMDYxOTI4ZjU2ZTliZDRiNGQuYmFhcy5uaW50ZW5kby5jb20ifQ==.lRPhNGds2CTB01TeI1P8ew6ZvDasBdYHU3CmQTAWCnk=",
        "carrier": "giffgaff",
        "deviceAccount": {
            "id": "791b08a43e15b102",
            "password": "kxtb6zyefdnBq1objgBq6046d90muquo1jpe3pgq"
        },
        "deviceAnalyticsId": "a2J1YmFhYWFERG1NamZtckpNTmVqSHZ6UGJWUE9FUwA=",
        "deviceName": "ONEPLUS A6003",
        "locale": "en-US",
        "manufacturer": "OnePlus",
        "networkType": "wifi",
        "osType": "Android",
        "osVersion": "11",
        "sdkVersion": "Unity-2.33.0-0a4be7c8",
        "timeZone": "Europe/London",
        "timeZoneOffset": 3600000
    }

Response headers
-------------------

.. code-block:: text

    Content-Type: application/json
    X-Cloud-Trace-Context: 750c6e4c8c864a8fe33d3cfc3bc5e595
    Date: Wed, 31 Aug 2022 19:24:48 GMT
    Server: Google Frontend
    Content-Length: 2357
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"

Response
----------------

.. code-block:: json

    {
        "accessToken": "eyJraWQiOiJhYjI2ODE1YS0yZjk0LTQ1NTUtOWQwMS0yYTk1OTg0OWJhM2QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiNWU5ZDU0YjE3NjZlZjJmIiwiYXVkIjoiYzZlNmUwNGFhYThjNjM1YSIsImlzcyI6Imh0dHBzOi8vNDhjYzgxY2RiOGRlMzBlMDYxOTI4ZjU2ZTliZDRiNGQuYmFhcy5uaW50ZW5kby5jb20iLCJ0eXAiOiJ0b2tlbiIsImJzOmdydCI6MiwiZXhwIjoxNjYxOTc0Nzg4LCJpYXQiOjE2NjE5NzM4ODgsImJzOmRpZCI6Ijc5MWIwOGE0M2UxNWIxMDIiLCJqdGkiOiI2NjJhNzg0Mi00MDRmLTQ5NjctYmQyZi01ZjNjZGUwZDkxNzYifQ.oCNoTl3beHhGEz6dmP97RY2yXeymKPkhKNAIPVkXOAaVNgGtwgja-2xl80t1WlMv81k_EEw4r8VkCEg29kwdHjvk43Sc2hmzp1BBS9iJ1J0WW895nJqb4dyOXYAMgu8TdmuegS_Flf4KtVXAEbxQfA5_kl-t9yinp49BmXUTkp7HoP7Hb7pNXSMKmeFehF6XQYpbBqv1XeaK30Rz4QFIogeFoHx2fR78nrNKmd51RaTUQhLH9YnzwtXoOu6VjNz569qKzaxX9bwc3750HZtn1-uSk1hNGxmJlL2tEtLAKTnbjzGDFTyvPr-3pFtQAb1xRrye6Z-cek7MQiDpp0xiTg",
        "behaviorSettings": {},
        "capability": {
            "accountApiHost": "api.accounts.nintendo.com",
            "accountHost": "accounts.nintendo.com",
            "pointProgramHost": "my.nintendo.com",
            "sessionUpdateInterval": 180000
        },
        "createdDeviceAccount": null,
        "error": null,
        "expiresIn": 900,
        "idToken": "<id_token>",
        "market": null,
        "sessionId": null,
        "user": {
            "birthday": "0000-00-00",
            "country": "",
            "createdAt": 1661897705,
            "deviceAccounts": [
                {
                    "id": "791b08a43e15b102"
                }
            ],
            "gender": "unknown",
            "hasUnreadCsComment": false,
            "id": "b5e9d54b1766ef2f",
            "links": {},
            "nickname": "",
            "permissions": {
                "personalAnalytics": true,
                "personalAnalyticsUpdatedAt": 1661897705,
                "personalNotification": true,
                "personalNotificationUpdatedAt": 1661897705
            },
            "updatedAt": 1661897705
        }
    }

Notes
-------

- The response is after selecting "link later", which may explain the empty/null fields -- there is no Nintendo account associated, so it seems dummy data is used.
- The `accessToken` appears in the request header of other requests, e.g. to /eula/get_version_list, as the value for the field `ID-TOKEN`