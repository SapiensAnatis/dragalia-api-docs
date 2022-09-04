/chara/get_chara_unit_set
==================================================

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
	    "chara_id_list": [
	        10140101,
	        10830101,
	        10130102,
	        10850403
	    ]
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
	        "chara_unit_set_list": [
	            {
	                "chara_id": 10140101,
	                "chara_unit_set_detail_list": []
	            },
	            {
	                "chara_id": 10830101,
	                "chara_unit_set_detail_list": []
	            },
	            {
	                "chara_id": 10130102,
	                "chara_unit_set_detail_list": []
	            },
	            {
	                "chara_id": 10850403,
	                "chara_unit_set_detail_list": []
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------