/core/v1/gateway/sdk/login
=================================

- Base address: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
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
	    "timeZone": "Europe/London",
	    "timeZoneOffset": 3600000,
	    "deviceAnalyticsId": "<device_analytics_id>",
	    "appVersion": "2.19.0",
	    "sdkVersion": "Unity-2.33.0-0a4be7c8",
	    "manufacturer": "OnePlus",
	    "deviceName": "ONEPLUS A6003",
	    "osType": "Android",
	    "osVersion": "11",
	    "locale": "en-US",
	    "networkType": "wifi",
	    "carrier": "giffgaff",
	    "assertion": "<assertion>",
	    "deviceAccount": {
	        "id": "<device_account>",
	        "password": "<password>"
	    }
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/json
	X-Cloud-Trace-Context: d8929c522be7f5028cac2fb2e7f601db
	Date: Wed, 31 Aug 2022 21:53:05 GMT
	Server: Google Frontend
	Content-Length: 2357
	Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"

Response
----------------

.. code-block:: json

	{
	    "idToken": "<id_token>",
	    "accessToken": "<access_token>",
	    "user": {
	        "id": "<user_id>",
	        "nickname": "",
	        "country": "",
	        "birthday": "0000-00-00",
	        "gender": "unknown",
	        "deviceAccounts": [
	            {
	                "id": "<device_account>"
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
