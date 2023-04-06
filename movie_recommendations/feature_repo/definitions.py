# Importing dependencies
from google.protobuf.duration_pb2 import Duration
from feast import Entity, Feature, FeatureView, FileSource, ValueType, Field
from feast.types import Float32, Int64, String

# Declaring an entity for the dataset
user = Entity(
    name="userID", 
    value_type=ValueType.INT64, 
    description="The ID of the User")

# Declaring the source of the first set of features
f_source1 = FileSource(
    path=r'data/movie_ratings.parquet',
    event_timestamp_column="timestamp"
)

# exit(0)
# Defining the first set of features
df1_fv = FeatureView(
    name="cleaned_movie_data",
    # ttl=Duration(seconds=86400 * 3),
    entities=[user],
    schema=[
        Field(name="movieID", dtype=Float32),
        Field(name="rating", dtype=String),
        ],    
    # batch_source=f_source1,
    source = f_source1
)

# Declaring the source of the second set of features
f_source2 = FileSource(
    path=r'data/user_details.parquet',
    event_timestamp_column="timestamp"
)

# Defining the second set of features
df2_fv = FeatureView(
    name="user_data",
    # ttl=Duration(seconds=86400 * 3),
    entities=[user],
    schema=[
        Field(name="age", dtype=Float32),
        Field(name="gender", dtype=String),
        Field(name="occupation", dtype=String),
        ],   
    source=f_source2
)

