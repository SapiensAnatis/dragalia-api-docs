/quest/get_quest_clear_party
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
	    "quest_id": 100010101
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
	        "quest_clear_party_setting_list": [],
	        "lost_unit_list": [],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------