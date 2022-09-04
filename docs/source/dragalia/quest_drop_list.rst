/quest/drop_list
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: b6a54796b1e3e6cdd20880aa0f862f201bd3f91adc8f8b59b7d65c2d6cd8b352	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888899015575716	Request-Time: 1662307911	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 15

Request body
----------------

.. code-block:: json

	{
	    "quest_id": 201010104
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 848	Expires: Sun, 04 Sep 2022 16:11:59 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 16:11:59 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "quest_drop_info": {
	            "drop_info_list": [
	                {
	                    "entity_type": 8,
	                    "entity_id": 101001003
	                },
	                {
	                    "entity_type": 8,
	                    "entity_id": 103001003
	                },
	                {
	                    "entity_type": 8,
	                    "entity_id": 102001003
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40030004
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40030005
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40030006
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40030013
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40030014
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40030015
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40030023
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40030026
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40030018
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40030034
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40030036
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40040002
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40040014
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40040034
	                },
	                {
	                    "entity_type": 39,
	                    "entity_id": 40050002
	                },
	                {
	                    "entity_type": 26,
	                    "entity_id": 10101
	                }
	            ],
	            "host_drop_info_list": [],
	            "fever_drop_info_list": [],
	            "quest_bonus_info_list": [
	                {
	                    "entity_type": 8,
	                    "entity_id": 101001003
	                },
	                {
	                    "entity_type": 18,
	                    "entity_id": 0
	                }
	            ],
	            "quest_reborn_bonus_info_list": [],
	            "campaign_extra_reward_info_list": []
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
