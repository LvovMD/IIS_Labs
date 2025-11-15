import logging
import pandas as pd
import dill as pkl
# import psycopg2
from datetime import datetime

# import os

logger = logging.getLogger("uvicorn.error")

class FastAPIHandler():

    def __init__(self):
        logger.warning('Loading model...')
        try:
            self.model = pkl.load(open('../models/model.pkl', 'rb'))
            logger.info('Model is loaded')
        except Exception as e:
            logger.error('Error loading model\n'+str(e.args[1]))

    def predict(self, item_id, item_features:dict):
        item_df = pd.DataFrame(data=item_features, index=[0])
        prediction = self.model.predict(item_df)

        # db_cred = {"dbname": "my_db_name",
        #            "user": 'admin',
        #            "password": 'admin',
        #            "host": "database"}
        
        # db_conn = psycopg2.connect(**db_cred)
        # cur = db_conn.cursor()

        # now = datetime.now()
        # cur.execute(f"INSERT INTO public.features \
        #             (flat_id, ts, blue, dual_sim, four_g, three_g, touch_screen, wifi, high_speed_ethernet, battery_power, clock_speed, fc, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time) \
        #             VALUES ({item_id}, '{now}', {item_features['blue']}, {item_features['dual_sim']}, {item_features['four_g']}, {item_features['three_g']}, {item_features['touch_screen']}, {item_features['wifi']}, {item_features['high_speed_ethernet']}, {item_features['battery_power']}, {item_features['clock_speed']}, {item_features['fc']}, {item_features['int_memory']}, {item_features['m_dep']}, {item_features['mobile_wt']}, {item_features['n_cores']}, {item_features['pc']}, {item_features['px_height']}, {item_features['px_width']}, {item_features['ram']}, {item_features['sc_h']}, {item_features['sc_w']}, {item_features['talk_time)']};")
        # cur.execute(f"INSERT INTO public.predictions \
        #             (flat_id, ts, price_range) VALUES ({item_id}, '{now}', {prediction[0]});")

        # db_conn.commit()

        return (prediction[0])