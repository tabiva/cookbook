# FSM 101

Finite state machine workflow UI and REST API

## Online demo

https://demo.viewflow.io/review/

## Quickstart

```bash
$ git clone https://github.com/viewflow/cookbook.git --depth=1

$ python3 -m venv cookbook/fsm101/venv
$ source cookbook/fsm101/venv/bin/activate

$ pip install -r cookbook/fsm101/requirements.txt --extra-index-url https://pypi.viewflow.io/<licence_id>/simple/
$ python3 cookbook/fsm101/manage.py migrate
$ python3 cookbook/fsm101/manage.py createsuperuser
$ python3 cookbook/fsm101/manage.py runserver
```

Navigate to http://127.0.0.1:8000/api/

## Related documentation
- [FSM Workflow](https://docs.viewflow.io/fsm/index.html)

## Most interesting files
- [flows.py](./review/flows.py) - FSM workflow definition
- [admin.py](./review/admin.py) - Django admin integration
- [rest.py](./review/rest.py) - Generic REST API
- [viewset.py](./review/viewset.py) - Generic template based UI
