# Kidney-Diseas-Classification

A deep learning project for classifying kidney diseases using CNN models, with MLflow for experiment tracking and DVC for data versioning.

## Project Structure

```
Kidney-Diseas-Classification/
├── artifacts/            # Training artifacts
├── config/               # Configuration files
├── logs/                 # Training logs
├── model/                # Saved models
├── research/             # Jupyter notebooks for experimentation
├── src/                  # Source code
│   ├── cnnClassifier/    # Main package
│   │   ├── components/   # Pipeline components
│   │   ├── config/       # Configuration management
│   │   ├── entity/       # Configuration entities
│   │   ├── pipeline/     # Training pipelines
│   │   └── utils/        # Utility functions
└── templates/            # Web templates
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Tejas-Sinroja/Kidney-Diseas-Classification.git
cd Kidney-Diseas-Classification
```

2. Create and activate conda environment:
```bash
conda create -n kidney python=3.8 -y
conda activate kidney
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Install DVC (if not already installed):
```bash
pip install dvc
```

## Usage

### Training Pipeline
```bash
python main.py
```

### Web Application
```bash
python app.py
```

### MLflow Tracking
Start MLflow UI:
```bash
mlflow ui
```

### DVC Commands
Initialize DVC:
```bash
dvc init
```

Reproduce pipeline:
```bash
dvc repro
```

## Model Architecture
The project uses a CNN-based architecture for kidney disease classification:
- Input: CT scan images
- Preprocessing: Normalization, resizing
- Model: Custom CNN with multiple convolutional and pooling layers
- Output: Disease classification probabilities

## Configuration
Update the following files as needed:
- `config/config.yaml` - Main configuration
- `params.yaml` - Training parameters
- `.env` - Environment variables (create if not exists)

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
