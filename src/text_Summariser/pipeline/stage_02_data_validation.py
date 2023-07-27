from text_Summariser.config.configuration import ConfigurationManager
from text_Summariser.components.data_validation import DataValidation
from text_Summariser.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()