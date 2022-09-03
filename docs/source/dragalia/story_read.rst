/story/read
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
	    "unit_story_id": 210001011
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
	        "unit_story_reward_list": [
	            {
	                "entity_type": 23,
	                "entity_id": 0,
	                "entity_quantity": 25
	            }
	        ],
	        "update_data_list": {
	            "unit_story_list": [
	                {
	                    "unit_story_id": 210001011,
	                    "is_read": 1
	                }
	            ],
	            "present_notice": {
	                "present_count": 0,
	                "present_limit_count": 41
	            },
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": []
	        }
	    }
	}

Notes
------