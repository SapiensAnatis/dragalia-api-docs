/inquiry/v1/users/<user_id>
==================================================

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
	X-Cloud-Trace-Context: 1b4e9e41b5078a969801af2fb86129ac
	Date: Sat, 03 Sep 2022 12:28:29 GMT
	Server: Google Frontend
	Content-Length: 79
	Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"


Response
----------------

.. code-block:: json

	{
	    "userId": "<user_id>",
	    "hasUnreadCsComment": false,
	    "updatedAt": 1636055991
	}

Notes
------
