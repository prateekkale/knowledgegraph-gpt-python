# kg-gpt-python
This is small project to showcase how we can use chatgpt api to generate knowledge graphs using python. Idea is not to showcase fancy graphs but to extract entities and their relationships.
Prompt reference is taken from https://github.com/varunshenoy/GraphGPT

# Requirements
Make sure you have python 3.8 or higher version and below python packages installed.
1. pandas
2. networkx
3. matplotlib

Open AI api key:
Please generate and save your open ai api key from here https://platform.openai.com/account/api-keys


# How to Run
Please follow below instructions to run this project
1. Download or clone the project repo.
2. Install required python packges.
3. Open cmd and Goto ->  knowledgegraph-gpt-python folder.
4. Run "python3 knowledgegraph.py"
5. After running it will ask for knowledge base file name where you have your text, for testing i have kept supplychain.txt in knowledgebase folder. You can add any text file in this folder for your purpose.
6. For testing give "supplychain.txt" as input.
7. Next it will ask for openai api key. please provide your api key generated from https://platform.openai.com/account/api-keys
8. Wait for sometime and knowledge graph will be generated. You can also use list of entities and relationships for your projects.

![supplychainKG](https://github.com/prateekkale/kg-gpt-python/assets/34265183/e4a5ec62-4eb0-4448-a371-c3ee182548bb)


