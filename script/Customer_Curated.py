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

# Script generated for node Accelerometer-landing
Accelerometerlanding_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="as_glue_db",
    table_name="accelerometer_landing",
    transformation_ctx="Accelerometerlanding_node1",
)

# Script generated for node Customer-trusted
Customertrusted_node1688578917880 = glueContext.create_dynamic_frame.from_catalog(
    database="as_glue_db",
    table_name="customer_trusted",
    transformation_ctx="Customertrusted_node1688578917880",
)

# Script generated for node Inner Join
InnerJoin_node1688578956120 = Join.apply(
    frame1=Accelerometerlanding_node1,
    frame2=Customertrusted_node1688578917880,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="InnerJoin_node1688578956120",
)

# Script generated for node Drop Fields
DropFields_node1688579055746 = DropFields.apply(
    frame=InnerJoin_node1688578956120,
    paths=["user", "timestamp", "x", "y", "z", "email", "phone", "birthday"],
    transformation_ctx="DropFields_node1688579055746",
)

# Script generated for node customer_curated
customer_curated_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1688579055746,
    connection_type="s3",
    format="json",
    connection_options={"path": "s3://as-glue/customer/curated/", "partitionKeys": []},
    transformation_ctx="customer_curated_node3",
)

job.commit()
