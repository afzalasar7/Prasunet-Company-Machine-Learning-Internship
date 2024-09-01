# <center><i>Prasunet Company Machine Learning Project - 02</i></center>

# <center><b>Mall Customers Clustering</b>
</center>

## Objective 🏠
- The goal is to develop a K-means clustering algorithm to group customers based on their purchase history. By identifying distinct customer segments, the retail store can tailor its marketing efforts, optimize inventory management, and personalize the shopping experience for different customer groups.

---

## About the Dataset 📊

- Download the dataset from here: <a href = 'https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python/data'>Kaggel Dataset</a> 

<br>

<center><img style='width:1000px;' src = 'images\readme-clustering-2.jpeg'></center>

<br>

- In a competitive retail environment, understanding customer behavior is paramount to enhancing customer satisfaction, improving marketing strategies, and boosting sales. Retail stores accumulate extensive data on customer purchases, which can be analyzed to uncover patterns and trends. However, the sheer volume of data can make it challenging to draw actionable insights without appropriate data analysis techniques.

- You own the mall and want to understand the customers like who can be easily converge [Target Customers] so that the sense can be given to marketing team and plan the strategy accordingly.

## Key Variables 🏡

- `CustomerID` ->  Unique ID assigned to the customer.
- `Gender` ->  Gender of the customer.
- `Age` ->  Age of the customer.
- `Annual Income` ->  Annual Income of the customer scaled to 1000$
- `Spending Score` ->  Score assigned by the mall based on customer behavior and spending nature

<br>

## Clustering 🧩

- Clustering is done based on `Annual Income` and `Spending Score`

## Model Performance 🤖

<img src = 'images/clustering-1.png'>

<br>


<img src = 'images/clustering-2.png'>

<br>

## How to Set Up This Project 🛠️

This guide walks you through setting up the project's environment.

**1. Install Python 🐍**

If you don't have Python installed yet, head over to the official download page: [Python Download Guide](https://wiki.python.org/moin/BeginnersGuide/Download) and follow the instructions for your operating system (Windows, macOS, or Linux).


**<u>Optional: Creating a Virtual Environment</u>**

1. Install virtualenv (if not already installed):

   If you haven't installed virtualenv, you can do so using pip:
    ```bash
    pip install virtualenv
    ```
2. Create a virtual environment:

    In the terminal and run this command:
    ``` bash
    virtualenv venv
    ```

3.  Activate the virtual environment:

    To activate the virtual environment:
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
2. navigate to repo directory
3. Run the following command to install dependencies from requirements.txt:

``` bash
pip install -r requirements.txt
```

**4. Host the project Locally 🌐**

- After installing the required dependencies, run the following command to start the project locally:

``` bash
streamlit run server.py
```

