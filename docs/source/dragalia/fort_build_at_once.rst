/fort/build_at_once
==================================================

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
	SID: c618b26d84f5cd808d716a910287efa157685d7a56111075f57a0474621bf1a3
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27891770117327236
	Request-Time: 1662479049
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 29


Request body
----------------

.. code-block:: json

	{
	    "build_id": 1360643,
	    "payment_type": 3
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 51
	Expires: Tue, 06 Sep 2022 15:44:10 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Tue, 06 Sep 2022 15:44:10 GMT
	Connection: keep-alive


Response
----------------

::.. note:: This is an error response code, because the button to rush was pressed after the building was complete. As this endpoint only differs from :doc:`/dragalia/fort_levelup_at_once`
by the fact that the building is newly placed, it should be possible to use the levelup endpoint response to infer the content of a successful response from this endpoint.

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 10019
	    },
	    "data": {
	        "result_code": 10019
	    }
	}

Notes
------
