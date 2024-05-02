import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to generate random samples and calculate means
def sample_means(data, sample_size, num_samples):
    means = []
    for _ in range(num_samples):
        # Generate samples from the data and calculate the mean
        sample = np.random.choice(data, size=sample_size, replace=False)
        means.append(np.mean(sample))
    return means

# Function to plot histogram of sample means
def plot_sample_means(sample_means, distribution_name):
    fig, ax = plt.subplots()
    ax.hist(sample_means, bins='auto', color='skyblue', edgecolor='black', alpha=0.7)
    ax.set_xlabel('Sample Means')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Distribution of Sample Means ({distribution_name})')
    ax.grid(True)
    st.pyplot(fig)

# Function to generate normal distribution data and plot
def generate_normal_data_and_plot(mean, std_dev):
    st.write("Generating 1000 sample means from normal distribution...")
    sample_means_data = [np.mean(np.random.normal(mean, std_dev, size=100)) for _ in range(1000)]
    plot_sample_means(sample_means_data, 'Normal Distribution')

# Function to generate custom distribution data and plot
def generate_custom_data_and_plot(data_input):
    try:
        data = [float(x.strip()) for x in data_input.split(',')]
        st.write("Your data:")
        st.write(data)

        # Automatically generate sample size as a tenth of data inputted 
        sample_size = round(len(data)/10)
        num_samples = 1000  

        st.write("Generating 1000 sample means...")
        sample_means_data = sample_means(data, sample_size, 1000)
        plot_sample_means(sample_means_data, 'Custom Distribution')
    except ValueError:
        st.error("Invalid input. Please enter numerical values separated by commas.")

# Function to generate Cauchy distribution data and plot
def generate_cauchy_data_and_plot(location, scale):
    st.write("Generating 1000 sample means from Cauchy distribution...")
    sample_means_data = [np.mean(np.random.standard_cauchy(size=100) * scale + location) for _ in range(1000)]
    plot_sample_means(sample_means_data, 'Cauchy Distribution')

# Streamlit app
st.title('Central Limit Theorem Demonstration')

option = st.selectbox("Select a distribution", ('Normal', 'Cauchy', 'Custom'))

if option == 'Normal':
    mean = st.slider("Mean:", min_value=100, max_value=200, value=150)
    std_dev = st.slider("Standard Deviation:", min_value=1, max_value=50, value=10)

    if st.button("Regenerate"):
        generate_normal_data_and_plot(mean, std_dev)

elif option == 'Cauchy':
    location = st.slider("Location:", min_value=-100, max_value=100, value=0)
    scale = st.slider("Scale:", min_value=1, max_value=50, value=10)

    if st.button("Regenerate"):
        generate_cauchy_data_and_plot(location, scale)

elif option == 'Custom':
    st.write("### Enter your data separated by commas:")
    data_input = st.text_area("Data")

    if st.button("Generate"):
        generate_custom_data_and_plot(data_input)
