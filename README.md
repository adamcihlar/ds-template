# Template
This repo serves as a general template for DS/ML/AI projects with a more or less standardized pipeline possibly consisting of the following steps:
 
### Main pipeline:
1. Ingestion
	* Module for getting the raw data from the source(s).
	* Result of this module is data saved in `data/raw/`.
2. Preprocessing
	* Cleansing, taking care of duplicates, errors, irrelevant data, merging sources. 
	* It should contain only steps that are carried out always, regardless what the future usage is.
	* Result of this module is data saved in `data/preprocessed/`.
3. Transformation
	* Preparing the data for the particular model, analysis, application. 
	* Splitting, imputation, feature engineering, encoding.
	* Result of this module is data saved in `data/final/`.
4. Training/modelling/analysis
	* Whatever the core of the project is.
	* Result is an asset, a trained model, file with identified parameters,...
	* All results of this steps should be stored in `output/` and `models/`.
5. Testing
	* If applicable, code that tests the selected model on the held-out dataset.
	* Result of this step should be stored in `output/`.
6. Inference
	* If applicable, module for performing inference with the trained model/pipeline on unseen data.
	* If applicable, differentiation between single and bulk inference.
	* Results of the bulk inference stored in `output/predictions/`.
7. API/app
	* If applicable, module building an API or an app for interacting with the trained model.

### Complementary elements:
* The pipeline is orchestrized by `makefile` and/or `main.py`, if suitable.
* Ad-hoc analysis are stored independantly in a seperate file (`analysis.py`) or folder (`analysis/`) and does not interact with the pipeline. Its results are stored `output/assets/`.
* `requirements.txt` and `setup.py` are a matter of course.
* The organization and configuration of the project, pipeline and single steps is stored in `config/` folder. 
	* The `config.yaml` file stores constants, parameters and can contain multiple different setups. Every inner file of the `config.yaml` contains field `name`, based on which the whole configuration is loaded. The structure of this file is dependant on the project itself and may be subject to change even after the project is finished.
	* The `paths.py` defines and documents the structure of the repo. Unlike the `config.yaml`, this structure should remain fixed once defined.
* Dockerfiles.
* Helper functions and everything reusable across the whole project is stored in `utilities.py`.

### Notes:
* Based on the size of the project, the single steps and elements above correspond to single scripts or separate directories.
* The repo is WIP.
* Next step to figure out is credentials, logs saving, experimentation tracking.

