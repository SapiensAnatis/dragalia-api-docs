/option/set_option
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: c618b26d84f5cd808d716a910287efa157685d7a56111075f57a0474621bf1a3	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27891771509836167	Request-Time: 1662479132	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 216

Request body
----------------

.. code-block:: json

	{
	    "option_setting": {
	        "is_enable_auto_lock_unit": 0,
	        "is_auto_lock_dragon_sr": 0,
	        "is_auto_lock_dragon_ssr": 1,
	        "is_auto_lock_weapon_sr": 0,
	        "is_auto_lock_weapon_ssr": 0,
	        "is_auto_lock_weapon_sssr": 0,
	        "is_auto_lock_amulet_sr": 0,
	        "is_auto_lock_amulet_ssr": 0
	    }
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 293	Expires: Tue, 06 Sep 2022 15:45:33 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Tue, 06 Sep 2022 15:45:33 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "option_data": {
	            "is_enable_auto_lock_unit": 0,
	            "is_auto_lock_dragon_sr": 0,
	            "is_auto_lock_dragon_ssr": 1,
	            "is_auto_lock_weapon_sr": 0,
	            "is_auto_lock_weapon_ssr": 0,
	            "is_auto_lock_weapon_sssr": 0,
	            "is_auto_lock_amulet_sr": 0,
	            "is_auto_lock_amulet_ssr": 0
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
