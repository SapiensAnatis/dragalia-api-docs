/tutorial/update_step
=======================

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
    DeviceId: 94e58eeb39e0f05c528aa0582d4032f8
    DeviceName: OnePlus ONEPLUS A6003
    OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
    GraphicsDeviceName: Adreno (TM) 540
    SID: 5f7d426cb80a8e890ab40e65393ee0280f6b693d1f1080451829653f5434d921
    Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
    Res-Ver: y2XM6giU6zz56wCm
    Request-Token: 27883448920180896
    Request-Time: 1661983065
    Content-Type: application/x-msgpack
    X-Unity-Version: 2019.4.31f1
    Content-Length: 12  


Request body
----------------

.. code-block:: javascript

    {
        "flag_id": 1022
    }

Response headers
----------------

.. code-block:: text

    Content-Type: application/x-msgpack
    Access-Control-Allow-Origin: *
    Content-Length: 145
    Expires: Wed, 31 Aug 2022 21:57:57 GMT
    Cache-Control: max-age=0, no-cache, no-store
    Pragma: no-cache
    Date: Wed, 31 Aug 2022 21:57:57 GMT
    Connection: keep-alive

Response
----------------

.. code-block:: json

    {
        "data_headers": {
            "result_code": 1
        },
        "data": {
            "tutorial_flag_list": [
                1020,
                1022
            ],
            "update_data_list": {
                "functional_maintenance_list": [
                ]
            },
            "entity_result": {
                "converted_entity_list": [
                ]
            }
        }
    }
    
Notes
------

- Write down any remarks or comments here