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

# Script generated for node Customer_Curated
Customer_Curated_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="as_glue_db",
    table_name="customer_curated",
    transformation_ctx="Customer_Curated_node1",
)

# Script generated for node Steptrainer_landing
Steptrainer_landing_node1688659584862 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://as-glue/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="Steptrainer_landing_node1688659584862",
)

# Script generated for node Join SerialNumber
JoinSerialNumber_node1688659685761 = Join.apply(
    frame1=Customer_Curated_node1,
    frame2=Steptrainer_landing_node1688659584862,
    keys1=["serialnumber"],
    keys2=["serialNumber"],
    transformation_ctx="JoinSerialNumber_node1688659685761",
)

# Script generated for node Drop Fields
DropFields_node1688664012648 = DropFields.apply(
    frame=JoinSerialNumber_node1688659685761,
    paths=[
        "customername",
        "email",
        "phone",
        "birthday",
        "serialnumber",
        "registrationdate",
        "lastupdatedate",
        "sharewithresearchasofdate",
        "sharewithpublicasofdate",
    ],
    transformation_ctx="DropFields_node1688664012648",
)

# Script generated for node Steptrainer_trusted
Steptrainer_trusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1688664012648,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://as-glue/step_trainer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="Steptrainer_trusted_node3",
)

job.commit()
