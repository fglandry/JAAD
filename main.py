import os
from jaad_data import JAAD

if __name__ == "__main__":
    data_path = os.path.dirname(os.path.realpath(__file__))
    jaad = JAAD(data_path)

    # Available functions in jaad object
    db = jaad.generate_database()
    #jaad.get_data_stats()
    #jaad.balance_samples_count()
    #jaad.get_detection_data()
    sequence = jaad.generate_data_trajectory_sequence("train")
    test = 5