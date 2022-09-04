/ability_crest/set_favorite
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888772683139715	Request-Time: 1662300388	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 36

Request body
----------------

.. code-block:: json

	{
	    "ability_crest_id": 40030005,
	    "is_favorite": 1
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Expires: Sun, 04 Sep 2022 14:06:29 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:06:29 GMT	Content-Length: 243	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "ability_crest_list": [
	                {
	                    "ability_crest_id": 40030005,
	                    "buildup_count": 0,
	                    "limit_break_count": 0,
	                    "equipable_count": 1,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "is_new": 1,
	                    "is_favorite": 1,
	                    "gettime": 1662299722
	                }
	            ],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
