import requests
import json
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os

# defining the api-endpoint
API_ENDPOINT = "https://api.openai.com/v1/completions"
API_KEY = ""
prompt_text = ""
kb_input = ""

# data to be sent to api
def createGraph(df,rel_labels):
  G = nx.from_pandas_edgelist(df, "source", "target",
                              edge_attr=True, create_using=nx.MultiDiGraph())
  plt.figure(figsize=(12, 12))

  pos = nx.spring_layout(G)
  nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos=pos)
  nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=rel_labels,
    font_color='red'
  )
  plt.show()

def preparingDataForGraph(api_response):
  # extracting response text
  response_text = api_response.text
  entity_relation_lst = json.loads(json.loads(response_text)["choices"][0]["text"])
  entity_relation_lst = [x for x in entity_relation_lst if len(x) == 3]
  source = [i[0] for i in entity_relation_lst]
  target = [i[2] for i in entity_relation_lst]
  relations = [i[1] for i in entity_relation_lst]

  kg_df = pd.DataFrame({'source': source, 'target': target, 'edge': relations})
  relation_labels = dict(zip(zip(kg_df.source, kg_df.target), kg_df.edge))
  return kg_df,relation_labels

def callGptApi(api_key,prompt_text):
  # sending post request and saving response as response object
  try:
      data = {"model": "text-davinci-003",
              "prompt": prompt_text,
              "max_tokens": 1600,
              "stop": "\n",
              "temperature": 0
              }
      headers = {"Content-Type": "application/json", "Authorization": "Bearer " + api_key}
      r = requests.post(url = API_ENDPOINT,headers=headers ,json = data)
      return r
  except Exception as e:
      print("Error : ", e)

def main(kb_file_name,api_key):
  with open(f"knowledgebase/{kb_file_name}", "r") as kb_text:
      kb_input = kb_text.read()


  with open("prompts/knowledge.prompt", "r") as f:
    prompt_text = f.read()

  prompt_text = prompt_text.replace("$prompt", kb_input)
  api_response = callGptApi(api_key,prompt_text)
  df,rel_lables = preparingDataForGraph(api_response)
  createGraph(df,rel_lables)

def start():
  while True:
      kb_file_name = str(input("Please enter knowledge base filename: "))
      if not os.path.exists(f"knowledgebase/{kb_file_name}"):
        print("File does not exists: Please provide valid file name")
      else:
        break
  while True:
      API_KEY = str(input("Please enter openai api key: "))
      if len(API_KEY)==0:
        print("Please provide valid key")
      else:
        break
  main(kb_file_name,API_KEY)

start()