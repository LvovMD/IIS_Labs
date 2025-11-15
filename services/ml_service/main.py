from fastapi import FastAPI
from api_handler import FastAPIHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram


app = FastAPI()
app.handler = FastAPIHandler()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

prediction_metric = Histogram(
    'prediction_metric_histogram',
    'histogram of predicted prices',
    buckets=(0, 1, 2, 3)
)


@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(item_id: int, item_features: dict):
    if item_features['four_g'] == 1:
        item_features['high_speed_ethernet'] = 'four_g'
    elif ['three_g'] == 1:
        item_features['high_speed_ethernet'] = 'three_g'
    else:
        item_features['high_speed_ethernet'] = 'none'

    prediction = app.handler.predict(item_id, item_features)

    prediction_metric.observe(prediction)

    return ({
             "price_range": str(prediction),
             "item_id": str(item_id)
            })