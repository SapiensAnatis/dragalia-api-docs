/summon/get_summon_point_trade
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com

Request body
----------------

.. code-block:: json

	{
	    "summon_id": 1020203
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "summon_point_trade_list": [
	            {
	                "trade_id": 1020203001,
	                "entity_type": 1,
	                "entity_id": 10250203
	            },
	            {
	                "trade_id": 1020203002,
	                "entity_type": 1,
	                "entity_id": 10450202
	            },
	            {
	                "trade_id": 1020203003,
	                "entity_type": 7,
	                "entity_id": 20050217
	            }
	        ],
	        "summon_point_list": [
	            {
	                "summon_point_id": 1020203,
	                "summon_point": 10,
	                "cs_summon_point": 0,
	                "cs_point_term_min_date": 0,
	                "cs_point_term_max_date": 0
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------