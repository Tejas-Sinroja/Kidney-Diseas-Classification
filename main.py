from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_model_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    prepare_base_model_pipeline = PrepareBaseModelTrainingPipeline()
    prepare_base_model_pipeline.main()
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"

try:
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation"

try:
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    evaluation_pipeline = EvaluationPipeline()
    evaluation_pipeline.main()
    logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e