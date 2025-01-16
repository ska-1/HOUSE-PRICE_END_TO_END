# House Price Prediction with ZenML & MLflow (MLOps Pipeline)

This project demonstrates an end-to-end machine learning pipeline for house price prediction using ZenML and MLflow on Windows. It incorporates MLOps principles to automate and track various steps of the pipeline, including data ingestion, preprocessing, model building, and deployment.

## Pipeline Overview
![image](https://github.com/user-attachments/assets/7adec222-56a1-4831-9470-52f8baaf312a)

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Pipeline Steps](#pipeline-steps)
- [How to Run the Project](#how-to-run-the-project)
- [Experiment Tracking with MLflow](#experiment-tracking-with-mlflow)
- [Deployment](#deployment)
- [CI/CD](#cicd)
- [Results](#results)

## Introduction

The project aims to predict house prices based on various features of the house. It leverages ZenML to create reproducible machine learning pipelines and MLflow for experiment tracking and model deployment. The pipeline automates the process from data ingestion to model evaluation and is set up for continuous integration and deployment (CI/CD) for machine learning.

## Project Structure

```
house-price-predictor/
├── analysis/
│   ├── EDA.ipynb                    # Exploratory Data Analysis notebook
│   └── analyze_src/
│       ├── basic_data_inspection.py    
│       ├── bivariate_analysis.py
│       ├── missing_values_analysis.py    
│       ├── univariate_analysis.py  
├── data/
│   └── archive.zip                  # Raw data for house prices
├── extracted_data/
│   └── AmesHousing.csv              # Processed data
├── src/
│   ├── data_splitter.py             # Splitting data into training and test sets
│   ├── feature_engineering.py       # Feature engineering logic
│   ├── handle_missing_values.py     # Handling missing values
│   ├── ingest_data.py               # Data ingestion logic
│   ├── model_building.py            # Model training logic
│   ├── model_evaluator.py           # Model evaluation logic
│   ├── outlier_detection.py         # Detect and handle outliers
├── steps/
│   ├── data_ingestion_step.py       # Data ingestion logic
│   ├── data_splitter_step.py        # Data splitting into training and test sets
│   ├── feature_engineering_step.py  # Feature engineering logic
│   ├── handle_missing_values_step.py# Handling missing values
│   ├── model_building_step.py       # Model training step
│   ├── model_evaluator_step.py      # Model evaluation step
│   ├── outlier_detection_step.py    # Detect and handle outliers
│   ├── predictor.py                 # Script for making predictions
├── pipelines/
│   ├── deployment_pipeline.py       # Definition of the deployment pipeline
│   ├── training_pipeline.py         # Definition of the training pipeline
├── run_pipeline.py                  # Script to run the pipeline
├── deployment.py                    # Script to deploy the model using MLflow
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
```

## Technologies Used

- **ZenML**: Framework for creating reproducible ML pipelines.
- **MLflow**: Experiment tracking, model management, and deployment.
- **Python**: Core programming language for the project.
- **Pandas, Scikit-learn**: Data manipulation and machine learning libraries.

## Pipeline Steps

- **Data Ingestion**: Reads the raw data from a ZIP file and loads it into a Pandas DataFrame.
- **Handling Missing Values**: Cleans the dataset by filling missing values using specified strategies.
- **Feature Engineering**: Creates new features, applies log transformations to relevant features.
- **Outlier Detection**: Identifies and removes outliers from the dataset based on specific criteria.
- **Data Splitting**: Splits the data into training and test sets.
- **Model Building**: Trains a machine learning model using Scikit-learn and tracks the experiment with MLflow.
- **Model Evaluation**: Evaluates the model using MSE and other metrics, and logs them to MLflow.

## How to Run the Project (Windows)

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/house-price-predictor.git
    cd house-price-predictor
    ```

2. **Set Up a Virtual Environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install the Requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install ZenML with Server Support**:
    ```bash
    pip install "zenml[server]==0.64.0"
    ```

5. **Initialize ZenML and Set Up Stack**:
    ```bash
    zenml init
    zenml integration install mlflow -y
    zenml experiment-tracker register mlflow_tracker --flavor=mlflow
    zenml model-deployer register mlflow --flavor=mlflow
    zenml stack register local-mlflow-stack -a default -o default -d mlflow -e mlflow_tracker --set
    ```

6. **Run the ZenML Server**:
    ```bash
    zenml up --blocking
    ```

7. **Run the Pipeline**:
    Open another terminal and run:
    ```bash
    python run_pipeline.py
    ```

## Experiment Tracking with MLflow (Windows)

To access the MLflow UI, open a new terminal after starting the ZenML server and run the following command:

```bash
mlflow ui --backend-store-uri 'file:C:\Users\your-account\AppData\Roaming\zenml\local_stores\1557ac67-da77-4577-a969-51f921786ec6\mlruns'
```

Then, open your browser and navigate to [http://localhost:5000](http://localhost:5000) to inspect your experiment runs.

![image](https://github.com/user-attachments/assets/4c191489-9539-4465-88cb-620b2b2ea8fc)
![image](https://github.com/user-attachments/assets/ffa3b758-63d3-48d0-8882-ec7110021151)

## Deployment

The project includes a deployment script (`deployment.py`) to deploy the trained model using MLflow. To deploy, simply run the following command:

```bash
python deployment.py
```

## CI/CD

This project adheres to basic CI/CD principles for machine learning, enabling automated runs, versioning of pipelines, and seamless deployment. Integration with tools like GitHub Actions can be added for fully automated pipelines.

## Results

After running the model, the evaluation metrics such as Mean Squared Error (MSE) are tracked in MLflow. The trained model can be accessed and evaluated through the MLflow dashboard.


