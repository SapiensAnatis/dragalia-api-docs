/fort/set_new_fort_plant
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
	    "fort_plant_id_list": [
	        100201
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
	        "result": 1,
	        "update_data_list": {
	            "fort_plant_list": [
	                {
	                    "plant_id": 100201,
	                    "is_new": 1
	                }
	            ],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------