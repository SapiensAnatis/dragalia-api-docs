/core/v1/gateway/sdk/login
=======================

- Base address: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Content-Type: application/json	User-Agent: com.nintendo.zaga/2.19.0 ONEPLUS A6003/11 NPFSDK/Unity-2.33.0-0a4be7c8	Accept-Language: en-US; q=1, en; q=0.5, *; q=0.001	Host: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com	Connection: Keep-Alive	Accept-Encoding: gzip	Content-Length: 714

Request body
----------------

.. code-block:: json

	{
	    "timeZone": "Europe/London",
	    "timeZoneOffset": 3600000,
	    "deviceAnalyticsId": "a2J1YmFhYWFERG1NamZtckpNTmVqSHZ6UGJWUE9FUwA=",
	    "appVersion": "2.19.0",
	    "sdkVersion": "Unity-2.33.0-0a4be7c8",
	    "manufacturer": "OnePlus",
	    "deviceName": "ONEPLUS A6003",
	    "osType": "Android",
	    "osVersion": "11",
	    "locale": "en-US",
	    "networkType": "wifi",
	    "carrier": "giffgaff",
	    "assertion": "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjb20ubmludGVuZG8uemFnYTowYzNkNzg5ZjVlZDIzZjJiMzRjNzk2NjBhMzcxOTBkMWM4NzNhM2YyIiwiaWF0IjoxNjYxOTgyNzg1LCJhdWQiOiJodHRwczpcL1wvNDhjYzgxY2RiOGRlMzBlMDYxOTI4ZjU2ZTliZDRiNGQuYmFhcy5uaW50ZW5kby5jb20ifQ==.NSFTB_fOmQaOMAmRZOsF-2dv1wsJF7nz8LFbT_0cf58=",
	    "deviceAccount": {
	        "id": "791b08a43e15b102",
	        "password": "kxtb6zyefdnBq1objgBq6046d90muquo1jpe3pgq"
	    }
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/json	X-Cloud-Trace-Context: d8929c522be7f5028cac2fb2e7f601db	Date: Wed, 31 Aug 2022 21:53:05 GMT	Server: Google Frontend	Content-Length: 2357	Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"

Response
----------------

.. code-block:: json

	{
	    "idToken": "<id_token>",
	    "accessToken": "eyJraWQiOiJhYjI2ODE1YS0yZjk0LTQ1NTUtOWQwMS0yYTk1OTg0OWJhM2QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiNWU5ZDU0YjE3NjZlZjJmIiwiYXVkIjoiYzZlNmUwNGFhYThjNjM1YSIsImlzcyI6Imh0dHBzOi8vNDhjYzgxY2RiOGRlMzBlMDYxOTI4ZjU2ZTliZDRiNGQuYmFhcy5uaW50ZW5kby5jb20iLCJ0eXAiOiJ0b2tlbiIsImJzOmdydCI6MiwiZXhwIjoxNjYxOTgzNjg1LCJpYXQiOjE2NjE5ODI3ODUsImJzOmRpZCI6Ijc5MWIwOGE0M2UxNWIxMDIiLCJqdGkiOiJlYjU2NWVjNS1iMjE5LTRmNWMtYTQ5Yi1hZmI4MTZiNzRjZWYifQ.Hq_UPUEcFpFUPJgxzET9R2mC4OlwTcESY4iXBWHF8vwnJmFQtERYt0Oea80y2S3qarq2VMJjClvBcFyKJFYEKGmmFcDJv_Vn416mt8f0doVxdRbBsG9mHmwOkb3b7cY02snXUOGFR1BAGll7ktCZLIkPJiDcGVf5jnnCYoNDh6K1R_eBV7l1bWKkjQM7x5n82zmOlU6azKTRXm0kMgABH4jLk3Vr9Y6qXREepT3BRoGSvdO7JxKTCqYJlKXSl8-bAkKe2SvRegxRosT7TJRJfl3PmD7jdJ66FwUAXNboSO9fiOAROG7zHfXXbvi5J53kIWUUpeMzGnnX9nLLHQ2eOQ",
	    "user": {
	        "id": "b5e9d54b1766ef2f",
	        "nickname": "",
	        "country": "",
	        "birthday": "0000-00-00",
	        "gender": "unknown",
	        "deviceAccounts": [
	            {
	                "id": "791b08a43e15b102"
	            }
	        ],
	        "links": {},
	        "permissions": {
	            "personalAnalytics": true,
	            "personalNotification": true,
	            "personalAnalyticsUpdatedAt": 1661897705,
	            "personalNotificationUpdatedAt": 1661897705
	        },
	        "createdAt": 1661897705,
	        "updatedAt": 1661897705,
	        "hasUnreadCsComment": false
	    },
	    "createdDeviceAccount": null,
	    "sessionId": null,
	    "error": null,
	    "expiresIn": 900,
	    "market": null,
	    "capability": {
	        "accountHost": "accounts.nintendo.com",
	        "accountApiHost": "api.accounts.nintendo.com",
	        "pointProgramHost": "my.nintendo.com",
	        "sessionUpdateInterval": 180000
	    },
	    "behaviorSettings": {}
	}

Notes
------
