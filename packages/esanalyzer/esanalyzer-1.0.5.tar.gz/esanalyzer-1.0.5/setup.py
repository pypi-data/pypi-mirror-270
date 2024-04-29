from setuptools import setup, find_packages

setup(
    name='esanalyzer',
    version='1.0.5',
    author='Ajay Singh Rajput',
    description='Emotion("fear", "anger", "surprise", "sadness", "disgust", "joy") and Sentiment("Positive","Negative") Analysis',
    url='https://github.com/ajaysingh111444/python/tree/esanalyzer/esanalyzer/version/1.0.5',
    long_description="""# esanalyzer

    The Python Emotion and Sentiment Analysis library you've been looking for.

    ## Services
    - Emotion Analysis("fear", "anger", "surprise", "sadness", "disgust", "joy")
    - Sentiment Analysis("Positive","Negative")
    - Multi Language Support

    ## Usage
    - Install using `pip install esanalyzer`

    ```python
    from esanalyzer import EmotionAnalyzer

    # Create an instance of EmotionAnalyzer
    analyzer = EmotionAnalyzer()

    # Call the analyze method with the text
    text = "Wow, I am so happy"
    result = analyzer.analyze(text)

    # Use the result as needed
    print(result)
    
    
    {'library': 'default', 'result': {'surprise': 80}, 'max_prediction': {'label': 'surprise', 'percentage': 80}, 'sentiment': 'Positive', 'sentiment_score': 0.999592125415802, 'threshold_value': 0.8}
    
    ```
    
    """,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    py_modules=["esanalyzer"],
    packages=find_packages(),
    install_requires=[
        'nrclex==3.0.0',
        'datasets==2.16.1',
        'scikit-learn==1.3.2',
        'pandas==2.1.4',
        'numpy==1.26.3',
        'googletrans==4.0.0-rc1',
        'transformers==4.36.2',
        'nltk==3.8.1'
    ],
    package_dir={'':'esanalyzer/src'}
    # Include other metadata like description, author, etc.
)
