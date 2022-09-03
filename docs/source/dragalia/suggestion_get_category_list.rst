/suggestion/get_category_list
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
	    "language_code": "en_eu"
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
	        "category_list": [
	            {
	                "category_id": 1,
	                "name": "About the gameplay/controls"
	            },
	            {
	                "category_id": 2,
	                "name": "About the characters"
	            },
	            {
	                "category_id": 3,
	                "name": "About the story and setting"
	            },
	            {
	                "category_id": 4,
	                "name": "About the sound and graphics"
	            },
	            {
	                "category_id": 5,
	                "name": "About game modes/events"
	            },
	            {
	                "category_id": 6,
	                "name": "About summoning"
	            },
	            {
	                "category_id": 7,
	                "name": "Requests for additional features"
	            },
	            {
	                "category_id": 8,
	                "name": "Other (about the game in general)"
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------