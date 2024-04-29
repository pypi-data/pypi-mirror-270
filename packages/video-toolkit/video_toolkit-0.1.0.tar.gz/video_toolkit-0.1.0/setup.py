from setuptools import setup, find_packages
# status: published online
setup(
    author= "Dear Norathee",
    description="package to help you with extraction of video information eg audio, subtitle",
    name="video_toolkit",
    version="0.1.0",
    packages=find_packages(),
    license="MIT",
    install_requires=["os_toolkit","pandas","dataframe_short","seaborn","python_wizard","pysrt","pydub","playsound"],
    

)