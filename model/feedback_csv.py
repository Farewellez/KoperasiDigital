import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from DB_Context import *

def to_csv_allfeedback():
    all_feedback = get_all_feedbackDB()
    all_feedback_df = pd.DataFrame(all_feedback)
    all_feedback_df.to_csv('allFeedback.csv', mode='a', header=False, index=False, index=False)
    return all_feedback_df