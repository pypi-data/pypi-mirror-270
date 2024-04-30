from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.7'
DESCRIPTION = 'Data analysis for Attrition predictions'
# Setting up
setup(
    name="LnT_HR_AI",
    version=VERSION,
    author="Radeesh",
    author_email="<vpsrad2002@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    entry_points={"console_scripts":[
                                       "DataPreproccessing=DataAnalysis_Package:DataPreProcessing",
                                       "DataVisualization=DataAnalysis_Package:data_visual",
                                       "DataStatisticalAnalysis=DataAnalysis_Package:data_analysis",
                                       "DataMLModels=DataAnalysis_Package:Run_MLModels",
                                    ],
                },
    install_requires=['scipy','catboost','lightgbm','xgboost','matplotlib','seaborn','scikit-learn', 'pyautogui', 'pyaudio'],
    keywords=['python','Machine Learning','Data Analysis','Data Science','Data processing'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)