# Physical Therapy AI Assistant

## SI 568 Final Project
**Use Case:** Utilizing the OpenAI API, this program creates a baseline physical therapy
plan for users. Because time is limited during a patient's first PT appointment,
the baseline plan is meant to complement the physical examination performed on the patient
by their therapist and serve as a secondary source of data when creating the patient's final
PT plan. Having more information regarding patient pain, limitations, and goals may help
improve patient outcomes and ultimately help them achieve their physical therapy goals.

## Getting Started

### Dependencies
- Python3
- OpenAI API key pasted in file called 'api-key'

### Installing
`pip install -r requirements.txt`

### Executing the program
`python3 PT_Plan.py`

### User Guide:
- This tool is designed to help you create your baseline physical therapy plan. To begin, please download all of the files, save your unique OpenAI API key to a file called 'api-key' in the same folder as the other files, and run 'PT_Plan.py' to launch the first prompt in the command line.

- The first set of prompts will ask you to provide the number of weeks you plan to participate in physical therapy (e.g., 8), the primary area in your body where you are experiencing pain (e.g., neck), one activity you are physically limited from performing (e.g., vacumming), and one goal you would like to accomplish through completing PT (e.g., running).

- After providing your input, the tool will return a summary of the inputs you provided followed by a detailed week by week baseline physical therapy plan with exercises. The tool will then ask if you would like to save your plan to a file that you can reference later.

- After saving your physical therapy plan, the tool will ask you if you would like to get detailed instructions for one of the exercises in your plan (e.g., how to perform toe raises). If you choose to, the tool will return step-by-step instructions on how to perform the specific exercise.




