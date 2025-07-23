---

# 🚀 Vehicle ML Project with End-to-End MLOps Pipeline

Welcome to the **Vehicle ML Project**, an end-to-end Machine Learning pipeline engineered using **MLOps principles** to ensure scalability, reproducibility, and robust deployment. This project demonstrates a production-grade approach with **CI/CD, AWS integration, MongoDB, data pipelines, and model serving**, designed to impress recruiters and real-world teams.

---

## ✨ **Key Features & Workflow**

### 🛠️ **1. Project Initialization**

* **Template Creation**: Execute `template.py` to generate standardized project structure.
* **Setup Local Packages**: Implement `setup.py` and `pyproject.toml` to manage local package imports efficiently.

  > Learn more in [crashcourse.txt](./crashcourse.txt).

### 🌐 **2. Virtual Environment Setup**

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list   # Verify package installation
```

---

## 🍃 **3. MongoDB Atlas Integration**

✅ **Steps:**

1. Sign up at **MongoDB Atlas** and create a new project.
2. Deploy **M0 cluster** with default settings.
3. Setup **DB user** credentials.
4. Allow network access from all IPs (`0.0.0.0/0`).
5. Obtain and store **connection string** securely.

💻 **Notebook Integration:**

* Create `notebook/mongoDB_demo.ipynb` with Python kernel `vehicle`.
* Push data to MongoDB and verify in **Atlas Collections**.

---

## 📝 **4. Logging, Exception Handling, EDA**

* **Logger**: Developed and tested via `demo.py`.
* **Exception Handler**: Integrated for pipeline robustness.
* **EDA & Feature Engineering Notebooks**: Added for dataset understanding and preprocessing.

---

## 📥 **5. Data Ingestion Pipeline**

* **Configurations**:

  * Constants defined in `constants/__init__.py`.
  * MongoDB connections in `configuration/mongo_db_connections.py`.
* **Components**:

  * Data fetching via `data_access/proj1_data.py`.
  * Entities defined in `entity/config_entity.py` and `entity/artifact_entity.py`.
  * Component logic implemented in `components/data_ingestion.py`.
* **Run**: Execute `demo.py` after setting MongoDB URL.

🔧 **Set Environment Variable Example (Windows PowerShell):**

```powershell
$env:MONGODB_URL = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
echo $env:MONGODB_URL
```

---

## ✅ **6. Data Validation, Transformation & Model Training**

* **Data Validation**: Schema defined in `config/schema.yaml`.
* **Data Transformation & Estimator**: Preprocessing pipelines for training-ready data.
* **Model Trainer**: Built with reproducibility and performance tuning.

---

## ☁️ **7. AWS Integration**

### 🔑 **AWS IAM & S3**

1. **IAM User**: Created with AdministratorAccess.
2. **Access Keys**: Configured via environment variables.
3. **S3 Bucket**:

   * Name: `my-model-mlopsproj05`
   * Region: `us-east-1`
   * Public access disabled for security.
4. **AWS Connection Logic**: Implemented in `configuration/aws_connection.py` and `aws_storage/`.

---

## 🧠 **8. Model Evaluation & Pusher**

* Evaluates model drift using configurable threshold.
* Pushes updated models to **S3 model registry** if improvements are detected.

---

## 🔮 **9. Prediction Pipeline & App Deployment**

* **Prediction Pipeline** structured with `app.py`.
* **Static** and **Template** directories for Flask-based UI.

---

## ⚙️ **10. CI/CD Deployment with GitHub Actions & AWS EC2**

### 🚀 **Steps:**

1. **Docker**:

   * `Dockerfile` and `.dockerignore` configured for containerization.
2. **GitHub Actions**:

   * Workflow YAML setup in `.github/workflows/aws.yaml`.
3. **AWS ECR**:

   * Repository created to store Docker images.
4. **AWS EC2 (Ubuntu)**:

   * Instance created with Docker and Self-Hosted Runner installed.
5. **GitHub Secrets**:

   * Added for AWS credentials and ECR repository URI.
6. **Trigger Deployment**:

   * CI/CD pipeline deploys app on EC2 instance.
7. **App Access**:

   * Public IP + Port 5080 hosts the deployed application.
   * `/training` route available for on-demand model training.

---

## 💡 **11. Key Technologies**

| Category             | Tools/Services                          |
| -------------------- | --------------------------------------- |
| **Programming**      | Python, Conda, Pip, Jupyter Notebook    |
| **Data & ML**        | Pandas, Sklearn, Feature Engineering    |
| **Database**         | MongoDB Atlas                           |
| **Cloud & DevOps**   | AWS (S3, EC2, IAM, ECR), GitHub Actions |
| **Containerization** | Docker                                  |
| **MLOps Concepts**   | CI/CD, Model Registry, Model Serving    |

---

## ✨ **Why This Project Stands Out?**

✅ End-to-end scalable ML pipeline
✅ Real-world MLOps CI/CD implementation
✅ AWS and MongoDB integration for production readiness
✅ Modular, reusable, and professional project structure

---

## 🙌 **Get In Touch**

If you find this project inspiring or wish to discuss MLOps opportunities, feel free to connect via [www.linkedin.com/in/sk-mahiduzzaman](#) or drop a message at [skmahiduzzaman@gmail.com](mailto:your-email@example.com).

---

> **⭐ Please consider starring the repository to support and share this work.**

---

### *“Turning Machine Learning solutions into robust, scalable products through MLOps.”*

---