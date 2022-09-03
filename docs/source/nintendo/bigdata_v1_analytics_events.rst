/bigdata/v1/analytics/events
===============================

- Base address: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
- Method: POST
- Status code: 202

Request headers
----------------

.. code-block:: text

	Content-Type: application/json
	Authorization: Bearer <id_token>
	Content-Encoding: gzip
	User-Agent: com.nintendo.zaga/2.19.0 ONEPLUS A6003/11 NPFSDK/Unity-2.33.0-0a4be7c8
	Accept-Language: en-US; q=1, en; q=0.5, *; q=0.001
	Host: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
	Connection: Keep-Alive
	Accept-Encoding: gzip
	Content-Length: 418


Request body
----------------

.. code-block:: json

	[
	    {
	        "eventTimestamp": 1661982880717,
	        "eventCategory": "NPFCOMMON",
	        "eventId": "SESSION",
	        "userId": "<user_id>",
	        "market": "GOOGLE",
	        "deviceAccount": "<device_account>2",
	        "payload": {
	            "action": "resume",
	            "duration": 82021
	        },
	        "cacheInfo": {
	            "timeZone": "Europe/London",
	            "timeZoneOffset": 3600000,
	            "sessionId": "<device_account>2-1661982786598",
	            "deviceAnalyticsId": "<device_analytics_id>",
	            "appVersion": "2.19.0",
	            "sdkVersion": "Unity-2.33.0-0a4be7c8",
	            "manufacturer": "OnePlus",
	            "deviceName": "ONEPLUS A6003",
	            "osType": "Android",
	            "osVersion": "11",
	            "locale": "en-US",
	            "networkType": "wifi",
	            "carrier": "giffgaff"
	        }
	    }
	]

Response headers
----------------

.. code-block:: text

	X-Cloud-Trace-Context: ad26e304f0be1daf2b743bef11c4b818
	Date: Wed, 31 Aug 2022 21:54:39 GMT
	Content-Type: text/html
	Server: Google Frontend
	Content-Length: 0
	Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"


Response
----------------

.. code-block:: json

	null

Notes
------
