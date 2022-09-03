/bigdata/v1/analytics/events/config
====================================

- Base address: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
- Method: GET
- Status code: 200

Request headers
----------------

.. code-block:: text

	Authorization: Bearer <id_token>
	User-Agent: com.nintendo.zaga/2.19.0 ONEPLUS A6003/11 NPFSDK/Unity-2.33.0-0a4be7c8
	Accept-Language: en-US; q=1, en; q=0.5, *; q=0.001
	Host: 48cc81cdb8de30e061928f56e9bd4b4d.baas.nintendo.com
	Connection: Keep-Alive
	Accept-Encoding: gzip


Request body
----------------

.. code-block:: json

	null

Response headers
----------------

.. code-block:: text

	Content-Type: application/json
	X-Cloud-Trace-Context: 345e32044ae61c353b7b68d438516ac7
	Date: Wed, 31 Aug 2022 21:53:05 GMT
	Server: Google Frontend
	Content-Length: 1282
	Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"


Response
----------------

.. code-block:: json

	{
	    "accessToken": "ya29.c.b0AXv0zTMZUgBUXZezKRvtxKEwTp6IczViDqC0Al4bAOCOm_3DxemeBgL3LfoTFeUhAPMyiY1Kni4zZgC_0bakAHd8L5MkD3YzTge0fDioYmeYtdlt17HMCP9t3nAQWj-pMQEUzQHrJn-9pmX16n5XjsqmZzc6EUTUxmGUl1hmI7obTl578MR42FEy5OqIWWBBGDWpb0LONW2KXZtAmF7ss_okgB8tJ1o........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................",
	    "applicationId": "c6e6e04aaa8c635a",
	    "city": "<city>",
	    "country": "GB",
	    "expirationTime": 1661985485477,
	    "immediateReporting": true,
	    "mode": "V2",
	    "region": "eng",
	    "reportingPeriod": 60000,
	    "topic": "projects/npf-baas-prod-gluon/topics/analytics-event-v02"
	}

Notes
------
