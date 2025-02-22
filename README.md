# Flask Mini App

This repository contains a mini project using the Flask web framework. The project developed a Flask API web application labeling images through PyTorch pre-trained ResNet50 model. Front-end web templates were developed with CSS3 and HTML5 markup inside Jinja2.


## Projects Included

- **Image Detector**: A web application that utilizes a pretrained model to detect and identify objects within images.

## Getting Started

To run these applications locally, follow the steps below:

### Prerequisites

- **Python**: Ensure you have Python installed on your machine. You can download it from the [official Python website](https://www.python.org/).

- **Flask**: Install Flask using pip:

  ```bash
  pip install Flask
  ```

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/JoonghyunAn/flask-mini-app.git
   cd flask-mini-app
   ```

2. **Set Up a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   Navigate to the specific project directory and install any required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: Each project may have its own `requirements.txt` file.*

### Running the Application

Within the project's directory, execute:

```bash
flask run
```

This will start the development server, and you can view the application by navigating to `http://127.0.0.1:5000/` in your web browser.


### Referred from
- Sato, Masaki. 2022. Introduction to Web Application Development with Python Flask.

---
