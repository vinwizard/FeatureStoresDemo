import pandas as pd
from feast import FeatureStore
from feast.infra.offline_stores.file_source import SavedDatasetFileStorage

# Getting our FeatureStore
store = FeatureStore(repo_path=".")

entity_df = pd.read_parquet(path="data/movie_ratings.parquet")

training_data = store.get_historical_features(
    entity_df=entity_df,
    features = [
        "cleaned_movie_data:movieID",
	"cleaned_movie_data:rating",
        "user_data:age",
	"user_data:gender",
	"user_data:occupation",
	]
     )


dataset = store.create_saved_dataset(
    from_=training_data,
    name="enhanced_movie_dataset",
    storage=SavedDatasetFileStorage("data/enhanced_movie_dataset.parquet")
)
