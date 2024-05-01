# gemini_txt_analyser

**Gemini TXT Analyser** is an application used to analyse ".txt" files with Google Gemini AI integrated into it.

# Source Code

The source code of the application **Gemini TXT Analyser** is available in 
[Source Code](https://github.com/SoftwareApkDev/gemini_txt_analyser/blob/master/gemini_txt_analyser/gemini_txt_analyser.py).

# Installation

```
pip install gemini_txt_analyser
```

# How to Use the Application?

Pre-requisites:

1. [Python](https://www.python.org/downloads/) installed in your device.
2. .env file in the same directory as <GEMINI_TXT_ANALYSER_DIRECTORY> and has the value of GEMINI_API_KEY.

```
cd <GEMINI_TXT_ANALYSER_DIRECTORY>
python3 gemini_txt_analyser.py
```

**Note:** Replace <GEMINI_TXT_ANALYSER_DIRECTORY> with the path to the directory of the 
application **Gemini TXT Analyser**.

Then, the application will start with something looking like in the screenshot below.

![Application](images/Application.png)

You will then be asked to input the following values.

1. Temperature - between 0 and 1 inclusive
2. Top P - between 0 and 1 inclusive
3. Top K - at least 1
4. Max output tokens - at least 1

The following screenshot shows what is displayed after inputting the mentioned values.

![TXT File Path Input](images/TXT%20File%20Path%20Input.png)

You will be required to input the path to the **.txt** file you want to analyse. Then, the contents of the text file
will appear and you will be asked to enter your question for analysis.

![Question Input](images/Question%20Input.png)

Once you entered your question, the application will display the answer based on your question and the contents of the
**.txt** file.

![AI Response](images/AI%20Response.png)

Then, you will be asked whether you want to continue using the application or not. Enter "Y" for yes. Enter anything
else for no.
