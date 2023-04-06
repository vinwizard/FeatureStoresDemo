from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path=".")

#training_df = store.get_saved_dataset(name="enhanced_movie_dataset").to_df()

training_df = pd.read_parquet('data/enhanced_movie_dataset.parquet')
print(training_df.head(5))
