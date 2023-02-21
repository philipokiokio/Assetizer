

# Assetizer.

## What could be done.
1. Present all available Assets on Exchanges.

2. If user aspect was to included emails could be stored and every 12 hours who waitlisted get a reminder.

3. Outstanding techincal stuff is writing tests.


## Usage

first thing is to set up your virtual environment. 

By way of illustration I will provide snippets to help you setup.

Ps. All commands below are terminal commands.



creating a virtualenv via venv
```
python3 -m venv {name of your env}
```

To activate your venv

```
source {name of your venv}/bin/activate
```



Please create a dotenv file for your environment variables. An example environment variable is provided. This file is called ```.example.env```.

Installing Requirements can be done by using this command.


```
pip install -r requirements.txt

```


Starting your Server

```
uvicorn src.app.main:app --reload

```

## Celery Job 
This code starts the celery job, this job runs every 12 hours.

```
celery -A src.jobs.celery_task worker -B --loglevel=info
```
Sample data for BTC/USDT.
```
{
  "message": "All asset data  available",
  "status": 200,
  "data": [
    {
      "id": 1,
      "asset": {
        "id": 2,
        "title": "BTC/USDT",
        "date_added": "2023-02-21T13:39:50.456922+01:00"
      },
      "price": 24638.34,
      "price_change": -163.08,
      "funding_rate": 0.0001,
      "open_interest": 113656.989,
      "volume": 343027.53641,
      "marketcap_ratio": null,
      "date_added": "2023-02-21T13:47:28.532846+01:00"
    },
    {
      "id": 2,
      "asset": {
        "id": 2,
        "title": "BTC/USDT",
        "date_added": "2023-02-21T13:39:50.456922+01:00"
      },
      "price": 24630.98,
      "price_change": -171.46,
      "funding_rate": 0.0001,
      "open_interest": 113656.989,
      "volume": 343046.55701,
      "marketcap_ratio": null,
      "date_added": "2023-02-21T13:47:57.385909+01:00"
    },
    {
      "id": 3,
      "asset": {
        "id": 2,
        "title": "BTC/USDT",
        "date_added": "2023-02-21T13:39:50.456922+01:00"
      },
      "price": 24638.86,
      "price_change": -191.76,
      "funding_rate": 0.0001,
      "open_interest": 113656.989,
      "volume": 340011.62834,
      "marketcap_ratio": null,
      "date_added": "2023-02-21T14:09:48.625863+01:00"
    },
    {
      "id": 4,
      "asset": {
        "id": 2,
        "title": "BTC/USDT",
        "date_added": "2023-02-21T13:39:50.456922+01:00"
      },
      "price": 24638.78,
      "price_change": -191.09,
      "funding_rate": 0.0001,
      "open_interest": 113656.989,
      "volume": 340010.13349,
      "marketcap_ratio": null,
      "date_added": "2023-02-21T14:09:49.951861+01:00"
    },
    {
      "id": 5,
      "asset": {
        "id": 2,
        "title": "BTC/USDT",
        "date_added": "2023-02-21T13:39:50.456922+01:00"
      },
      "price": 24637.56,
      "price_change": -192.57,
      "funding_rate": 0.0001,
      "open_interest": 113656.989,
      "volume": 340013.9484,
      "marketcap_ratio": null,
      "date_added": "2023-02-21T14:09:51.780942+01:00"
    }
    ]
}```