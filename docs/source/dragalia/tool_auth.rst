/tool/auth
=======================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com
	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)
	Accept: */*
	Accept-Encoding: deflate, gzip
	App-Ver: 2.19.0
	Device: 2
	Platform: 2
	Carrier: OnePlus
	DeviceId: <device_id>
	DeviceName: OnePlus ONEPLUS A6003
	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
	GraphicsDeviceName: Adreno (TM) 540
	SID: 6b4a7cb93afcd1c848e76c8062d88e963a3ba8ae04f3bbe0c1d107b9dee39fff
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27883445044644105
	ID-TOKEN: <id_token>
	Request-Time: 1661982833
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 964


Request body
----------------

.. code-block:: json

	{
	    "uuid": "59479867-638e-4780-9673-3de708e4b0a8",
	    "id_token": "<id_token>"
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 161
	Expires: Wed, 31 Aug 2022 21:53:57 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 21:53:57 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "viewer_id": 66709573935,
	        "session_id": "9b46d3c0236a76ba3284273b6163dde855c8e3debb83a74c018d728365ba92c1",
	        "nonce": "1h6SlQl1BfW9bvUXLxT7NA=="
	    }
	}

Notes
------
