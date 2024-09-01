# <center><i>Prasunet Company Machine Learning Project - 04</i></center>

# <center><b>Hand Signs Classification</b>
</center>

## Objective 🏠
- the goal is to design and develop a robust hand gesture recognition model capable of accurately identifying and classifying various hand gestures from both image and video data. The goal is to enable intuitive human-computer interaction and gesture-based control systems in applications such as virtual reality, robotics, and smart environments.

<br>

## About the Dataset 📊

- Download the dataset from here: <a href = 'https://www.kaggle.com/datasets/gti-upm/leapgestrecog'>Kaggel Dataset</a> 

<br>

<center><img style='width:1000px;' src = 'images\dataset-cover.png'></center>

<br>

- Hand gesture recognition database is presented, composed by a set of near infrared images acquired by the Leap Motion sensor.

- The database is composed by 10 different hand-gestures (showed above) that were performed by 10 different subjects (5 men and 5 women)



## Image Classes 📷

`palm`  
`L`  
`fist`  
`fist-side`  
`thumb`  
`index`  
`ok`  
`palm-side`  
`C`  
`down`

<br>

## Model Architecture 👾

<img src = 'images/model-arch.png'>

<br>

## Model Performance 🤖

<img src = 'images/model_performance.png'>

<br>

<img src = 'images/confusion_matrix.png'>

<br>

## How to Set Up This Project 🛠️

This guide walks you through setting up the project's environment.

**1. Install Python 🐍**

If you don't have Python installed yet, head over to the official download page: [Python Download Guide](https://wiki.python.org/moin/BeginnersGuide/Download) and follow the instructions for your operating system (Windows, macOS, or Linux).

**<u>Optional: Creating a Virtual Environment</u>**

1. Install virtualenv (if not already installed):

   - If you haven't installed virtualenv, you can do so using pip:
    ```bash
    pip install virtualenv
    ```
2. Create a virtual environment:

    - In the terminal and run this command:
    ``` bash
    virtualenv venv
    ```

3.  Activate the virtual environment:

    - To activate the virtual environment:
    ``` bash
    venv\Scripts\activate
    ```

**2. Download the Repo 📥**


1. Open your Git client or terminal.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command, replacing `<repository_url>` with the actual URL of the project's repository:

```bash 
git clone <repository_url>
```

**3. Install required Dependencies  📦**
1. Open terminal/cmd.
2. Navigate to repo directory
3. Run the following command to install dependencies from requirements.txt:

``` bash
pip install -r requirements.txt
```

**4. Host the project Locally 🌐**

- After installing the required dependencies, run the following command to start the project locally:

``` bash
streamlit run server.py
```

