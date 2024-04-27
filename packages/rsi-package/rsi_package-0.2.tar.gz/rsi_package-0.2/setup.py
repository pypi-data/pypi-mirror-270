from setuptools import setup, find_packages

setup(
    name='rsi_package',
    version='0.2',
    description='A package for calculating Relative Strength Index (RSI) from financial data.',
    long_description='''\
        Hi, my name is Kartikey Vyas, This package provides functions for calculating the Relative Strength Index (RSI) 
        from financial data. It includes tools for loading data, calculating gains and losses, 
        computing rolling averages, and deriving RSI values
        use the below mentioned code to see the latest day's RSI Value (Tested on many scripts of indian stock market)
        import pandas as pd
        from rsi_package.rsi_calculator.rsi_calculator import calculate_rsi

        # Load your data into a pandas DataFrame (replace 'your_data.csv' with your actual data file)
        df = pd.read_csv("yourfile.csv") (#limitation = your file should have two columns one date and other close)

        # Calculate RSI
        rsi_values = calculate_rsi(df)

        # Add RSI values as a new column to the DataFrame
        df['RSI'] = rsi_values
        # Drop unnecessary columns
        df = df[['date', 'close', 'RSI']]
        # Display the DataFrame with RSI values
        print(df.tail())
                .
            ''',
    long_description_content_type='text/markdown',
    url='https://github.com/Richkart700/RSI-Package',
    author='Kartikey Vyas',
    author_email='kvsvyas@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        # Add any other dependencies here
    ],
)
