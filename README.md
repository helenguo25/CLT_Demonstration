# Central Limit Theorem Demonstration

This is a Streamlit application that demonstrates the Central Limit Theorem (CLT). The CLT result states that the sampling distribution of the sample mean approaches a normal distribution as the sample size gets larger, regardless of the shape of the population distribution.

## Understanding the Central Limit Theorem:

- **Normal Distribution:** Demonstrates how the sample mean distribution tends towards normality regardless of the underlying distribution.
- **Cauchy Distribution:** Shows how the CLT doesn't apply to all distributions, as the Cauchy distribution doesn't have a finite mean or variance. 
- **Custom Distribution:** Allows users to input their own data to observe the CLT in action.

## How to Launch:

1. **Install Streamlit:** If you haven't already, install Streamlit by running:

   pip install streamlit

3. **Download the Script:** Copy the provided code into a Python script file (e.g., `clt_edu_tool.py`).

4. **Launch the App:** Run the Streamlit app by executing the following commands in your terminal:

   streamlit run clt_demo.py

### 1. Select Population Distribution:
- Choose between three populuation distributions: Normal, Cauchy, or Custom.

### 2. Parameters:
- **Normal Distribution:**
  - Set mean and standard deviation using sliders.

- **Cauchy Distribution:**
  - Adjust location and scale using sliders. Notice how the CLT does not apply to the Cauchy distribution.

- **Custom Distribution:**
  - Enter your data separated by commas.

### 3. Generate:
- Click the "Regenerate" or "Generate" button to generate sample means and observe the distribution of these means.

