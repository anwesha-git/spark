import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node step_trainer_trusted
step_trainer_trusted_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="as_glue_db",
    table_name="step_trainer_trusted",
    transformation_ctx="step_trainer_trusted_node1",
)

# Script generated for node Accelerometer_trusted
Accelerometer_trusted_node1688663659428 = glueContext.create_dynamic_frame.from_catalog(
    database="as_glue_db",
    table_name="accelerometer_trusted",
    transformation_ctx="Accelerometer_trusted_node1688663659428",
)

# Script generated for node Join timestamp
Jointimestamp_node1688663691735 = Join.apply(
    frame1=Accelerometer_trusted_node1688663659428,
    frame2=step_trainer_trusted_node1,
    keys1=["timestamp"],
    keys2=["sensorreadingtime"],
    transformation_ctx="Jointimestamp_node1688663691735",
)

# Script generated for node Drop Fields
DropFields_node1688664242718 = DropFields.apply(
    frame=Jointimestamp_node1688663691735,
    paths=["timestamp"],
    transformation_ctx="DropFields_node1688664242718",
)

# Script generated for node machine_learning_curated
machine_learning_curated_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1688664242718,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://as-glue/step_trainer/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="machine_learning_curated_node3",
)

job.commit()
